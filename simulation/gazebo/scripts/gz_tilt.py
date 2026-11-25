"""Teach and test the tilt camera inside Gazebo (Harmonic).

Needs gz-sim 8 with Python bindings (gz.transport13, gz.msgs10) and numpy.

  gz sim -r ../tilt_camera.sdf          # terminal 1
  python3 gz_tilt.py teach              # terminal 2: sweep -60..60 deg, writes table.json
  python3 gz_tilt.py test --n 40        # random angles, prints error stats
  python3 gz_tilt.py live               # print the estimate continuously
"""
import argparse
import math
import random
import threading
import time

import numpy as np
from gz.msgs10.double_pb2 import Double
from gz.msgs10.image_pb2 import Image
from gz.msgs10.model_pb2 import Model
from gz.transport13 import Node

import tilt_vision as tv

IMAGE_TOPIC = "/tilt_camera/image"
CMD_TOPIC = "/follower/tilt_cmd"
STATE_TOPIC = "/world/tilt_camera/model/follower_row/joint_state"


class Rig:
    def __init__(self):
        self.node = Node()
        self.lock = threading.Lock()
        self.frame = None
        self.frame_id = 0
        self.true_deg = None
        self.pub = self.node.advertise(CMD_TOPIC, Double)
        self.node.subscribe(Image, IMAGE_TOPIC, self._on_image)
        self.node.subscribe(Model, STATE_TOPIC, self._on_state)

    def _on_image(self, msg):
        rgb = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)
        with self.lock:
            self.frame = rgb.copy()
            self.frame_id += 1

    def _on_state(self, msg):
        for j in msg.joint:
            if j.name == "tilt" and j.axis1:
                with self.lock:
                    self.true_deg = math.degrees(j.axis1.position)

    def set_angle(self, deg, settle=1.5):
        m = Double()
        m.data = math.radians(deg)
        self.pub.publish(m)
        time.sleep(settle)

    def fresh_frame(self, timeout=3.0):
        with self.lock:
            start = self.frame_id
        t0 = time.time()
        while time.time() - t0 < timeout:
            with self.lock:
                if self.frame_id > start:
                    return self.frame
            time.sleep(0.02)
        raise TimeoutError("no camera image: is the simulation running and unpaused (-r)?")

    def measure(self, tol):
        return tv.features(tv.find_markers(self.fresh_frame(), tol=tol))


def teach(rig, args):
    table = []
    for a in range(-60, 61, 2):
        rig.set_angle(a)
        reads = [f for f in (rig.measure(args.tol) for _ in range(3)) if f]
        if reads:
            table.append({"angle": float(rig.true_deg if rig.true_deg is not None else a),
                          "gap": float(np.mean([r[0] for r in reads])),
                          "pink": float(np.mean([r[1] for r in reads]))})
        print(f"{a:+4d} deg  {'ok' if reads else 'markers not found'}")
    tv.save_table(args.table, table)
    print(f"taught {len(table)}/61 angles -> {args.table}")


def test(rig, args):
    table = tv.load_table(args.table)
    errs, missed = [], 0
    for _ in range(args.n):
        a = random.uniform(-55, 55)
        rig.set_angle(a)
        f = rig.measure(args.tol)
        if not f:
            missed += 1
            continue
        est, src = tv.estimate(table, *f)
        errs.append(abs(est - (rig.true_deg if rig.true_deg is not None else a)))
    errs.sort()
    if errs:
        print(f"found {args.n - missed}/{args.n}  median {errs[len(errs)//2]:.2f} deg  "
              f"95% {errs[min(len(errs)-1, int(len(errs)*0.95))]:.2f} deg  max {errs[-1]:.2f} deg  "
              f"within 1 deg {sum(e <= 1 for e in errs)}/{len(errs)}")
    else:
        print("no readings")


def live(rig, args):
    table = tv.load_table(args.table)
    while True:
        f = rig.measure(args.tol)
        if f:
            est, src = tv.estimate(table, *f)
            print(f"true {rig.true_deg:+7.2f}  camera {est:+7.2f} ({src})")
        else:
            print("markers not found")
        time.sleep(0.2)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["teach", "test", "live"])
    ap.add_argument("--table", default="table.json")
    ap.add_argument("--tol", type=float, default=38.0)
    ap.add_argument("--n", type=int, default=40)
    a = ap.parse_args()
    rig = Rig()
    time.sleep(1.0)
    {"teach": teach, "test": test, "live": live}[a.mode](rig, a)
