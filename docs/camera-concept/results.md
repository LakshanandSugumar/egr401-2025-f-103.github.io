---
title: Results
---

# Simulation Results

Each row is one run of 40 random follower angles between −55° and +55°, using the [field simulation](simulation.md) with a 7 m row gap. The camera was taught once at noon unless noted. Default conditions are 4 m/s wind, 10% lens dust and 3 DN sensor noise. Results vary a little from run to run.
{ .md-caption }

| Conditions | Markers read | Median error | 95% within | Within ±1° |
| --- | ---: | ---: | ---: | ---: |
| Jun 21, 12:00 | 37/40 | 0.06° | 0.25° | 37/37 |
| Jun 21, 09:00 | 32/40 | 0.10° | 0.24° | 32/32 |
| Jun 21, 16:00 | 34/40 | 0.07° | 0.26° | 34/34 |
| Jun 21, 16:00, 15 m/s wind, 40% dust | 37/40 | 0.11° | 0.36° | 37/37 |
| Jun 21, 06:12, camera facing the low sun (east) | 36/40 | 0.17° | 0.44° | 36/36 |
| Jun 21, 06:12, camera facing away from the sun (west) | 37/40 | 0.04° | 0.23° | 37/37 |
| Dec 21, 18:30, dark, no flash | 0/40 | – | – | – |
| Dec 21, 18:30, dark, retroreflective markers + flash | 39/40 | 0.19° | 0.60° | 39/39 |

!!! success "Accuracy"
    Every reading the camera made in daylight or with the flash at night was within the ±1° target. Most were within 0.3°.

## What the simulation exposed

**The panel hides the far marker near edge-on.** At about +6° to +14°, the camera looks almost along the panel surface, and the module partly hides the yellow marker on the far edge. The yellow-minus-pink gap then folds back, so one gap value can match two angles. The near pink marker is never hidden, so the estimator uses its position to pick the right reading. Most of the missed readings in the table are at these angles.

**It can't see at night without help.** After dark, the camera has to turn the gain up so far that noise buries the markers. Retroreflective markers with a small LED flash fix this: the camera takes one frame with the flash and one without, and subtracts them. A table taught at noon still works at night.

**Facing the sun costs accuracy.** With the camera facing east at sunrise, glare lowers contrast and the 95% error roughly doubles, though it stays inside ±1°. A camera facing west at the same time isn't affected. Mounting cameras so the sun is behind them, or adding a second camera facing the other way, avoids this.

**Wind and dust matter less than expected.** Strong wind shakes the camera post, but both markers move together, so the gap between them barely changes. Dust lowers contrast without moving the marker centers much.

## Still to prove with hardware

- Real color behavior of an OV2640 camera in Arizona sun, including auto white balance
- Heat shimmer above hot modules at 6–8 m
- Marker fading under UV over months
- The real retroreflective return from a small LED at 7 m
