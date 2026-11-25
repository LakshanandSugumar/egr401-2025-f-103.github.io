"""Color subtraction, marker centroids and the taught-table estimator.

Same method as the browser simulation:
  yellow score = min(R, G) - B
  pink score   = min(R, B) - G
The near pink marker's image row gives a coarse angle (it is never hidden by the module);
the yellow-minus-pink gap gives the fine angle and cancels camera-post sway.
"""
import json
import numpy as np


def find_markers(rgb, tol=38.0, min_px=6):
    """rgb: HxWx3 uint8 or float array. Returns dict with 'yellow' and 'pink' (x, y, n) or None."""
    img = rgb.astype(np.float32)
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    scores = {
        "yellow": np.minimum(r, g) - b,
        "pink": np.minimum(r, b) - g,
    }
    out = {}
    for name, sc in scores.items():
        t = max(tol, 0.45 * float(sc.max()))
        w = np.clip(sc - t, 0, None)
        n = int((w > 0).sum())
        if n < min_px:
            out[name] = None
            continue
        ys, xs = np.indices(sc.shape)
        tot = w.sum()
        out[name] = (float((w * xs).sum() / tot), float((w * ys).sum() / tot), n)
    return out


def features(markers):
    """Returns (gap, pink_row) in pixels, or None if either marker is missing."""
    y, p = markers.get("yellow"), markers.get("pink")
    if y is None or p is None:
        return None
    return y[1] - p[1], p[1]


def _interp_all(table, key, v):
    hits = []
    for a, b in zip(table, table[1:]):
        lo, hi = sorted((a[key], b[key]))
        if lo <= v <= hi:
            u = (v - a[key]) / ((b[key] - a[key]) or 1.0)
            hits.append(a["angle"] + u * (b["angle"] - a["angle"]))
    return hits


def estimate(table, gap, pink_row, agree_deg=1.5):
    """table: list of {'angle', 'gap', 'pink'} ordered by angle. Returns (angle_deg, source)."""
    coarse = _interp_all(table, "pink", pink_row)
    if not coarse:
        end = min((table[0], table[-1]), key=lambda t: abs(t["pink"] - pink_row))
        return end["angle"], "outside"
    c = coarse[0]
    fine = sorted(_interp_all(table, "gap", gap), key=lambda a: abs(a - c))
    if fine and abs(fine[0] - c) < agree_deg:
        return fine[0], "gap"
    return c, "pink"


def save_table(path, table):
    with open(path, "w") as f:
        json.dump(table, f, indent=1)


def load_table(path):
    with open(path) as f:
        return json.load(f)
