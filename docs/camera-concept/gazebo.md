---
title: Gazebo Model
---

# Gazebo Model

The same setup as the browser simulation, built as a Gazebo world so the team can test the vision code against a full physics simulation on a laptop. Built by Lakshanand Sugumar.

Gazebo runs on your computer, not in a web page. The [field simulation](simulation.md) is the in-browser version.
{ .md-caption }

## Files

In the repository under `simulation/gazebo/`:

| File | What it is |
| --- | --- |
| `tilt_camera.sdf` | The world: drive row, follower row on a revolute joint, camera on a fixed post, pink and yellow markers, Arizona sun |
| `scripts/tilt_vision.py` | Color subtraction, marker centers and the taught-table estimator |
| `scripts/gz_tilt.py` | Teach, test and live modes that drive the follower joint and read the camera |

## What's in the world

- Follower row 5.8 m from the camera, on a revolute joint about the row axis, limited to ±60°
- Camera: 640 × 480, 60° horizontal view, 10 Hz, Gaussian noise, on a post 0.5 m above the tube
- 10 cm markers: pink on the near edge, yellow on the far edge, 1 m apart along the row
- Joint angle set over `/follower/tilt_cmd`, ground truth from the joint state topic

## Run it

Needs Gazebo Harmonic (gz-sim 8) with its Python bindings, and numpy. Ubuntu 22.04/24.04 is the easiest setup.

```bash
cd simulation/gazebo
gz sim -r tilt_camera.sdf
```

In a second terminal:

```bash
cd simulation/gazebo/scripts
python3 gz_tilt.py teach
python3 gz_tilt.py test --n 40
```

`teach` sweeps the follower from −60° to +60° in 2° steps and saves `table.json`. `test` tilts it to random angles and prints the error statistics.

!!! warning "Not yet run"
    These files were written to match the browser simulation but haven't been run in Gazebo yet. Expect to adjust joint gains or topic names on the first run.
