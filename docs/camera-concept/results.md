---
title: Results
---

# Simulation Results

Each row is one run of 40 random follower angles between −55° and +55°, using the physics-based [field simulation](simulation.md) with a 7 m row gap. The camera was taught once at noon. Defaults are 6 m/s mean wind with gusts, 10% lens dust and 3 DN read noise. Errors are measured against the true angle at the markers. Results vary a little from run to run.
{ .md-caption }

## Daylight

| Conditions | Markers read | 95% within | Max error | Tube twist at markers |
| --- | ---: | ---: | ---: | ---: |
| Jun 21, 12:00, markers at the drive point | 35/40 | 0.23° | 0.31° | 0.00° |
| Same, 12 m/s wind | 38/40 | 0.36° | 0.36° | 0.00° |
| Jun 21, 12:00, markers 25 m out | 39/40 | 0.28° | 0.30° | up to 1.99° |
| Same, 12 m/s wind | 39/40 | 0.20° | 0.47° | up to 5.72° |
| Jun 21, 09:00 | 36/40 | 0.33° | 0.53° | 0.00° |
| Jun 21, 06:12, camera facing the low sun | 36/40 | 0.59° | 0.60° | 0.00° |

## Night (Dec 21, 18:30, sun 12° below the horizon)

| Conditions | Markers read | 95% within | Max error |
| --- | ---: | ---: | ---: |
| No flash | 0/40 | – | – |
| Flash, 4 cd LED | 1/40 | – | – |
| Flash, 8 cd LED | 30/40 | 0.52° | 0.52° |
| Flash, 20 cd LED | 38/40 | 0.35° | 0.36° |
| Flash, 40 cd LED | 37/40 | 0.26° | 0.33° |

!!! success "Accuracy"
    Every reading the camera made was within the ±1° target, including in strong wind, low sun and at night with a bright enough flash.

## What the physics showed

**Wind twists the follower row far more than ±1°, so where you put the markers matters.** The follower is driven at one point, and wind torque twists the tube along its length. With the assumed 60 m row and 127 mm tube, the angle 25 m from the drive point swings up to 2° in a 6 m/s breeze and almost 6° at 12 m/s, oscillating at the tube's 1.9 Hz twist frequency. The camera measured these swings correctly, because the markers move with the row. That changes the question:

- **Markers at the drive point** measure the linkage misalignment ARRAY cares about, with no wind twist mixed in.
- **Markers near the row end** measure linkage misalignment plus wind twist. That's useful for structural monitoring, but readings need averaging over a few seconds to remove the gust swings.

**The camera needs a 20 cd or brighter LED at night.** The retroreflected light falls off with the square of the distance. An 8 cd LED is marginal at 7 m, and 4 cd is too dim. A 20 cd LED gives reliable readings.

**The camera post barely moves.** Under 12 m/s wind a 2 in. steel post leans about 0.01°, and the two-marker gap cancels even that.

**Heat shimmer is negligible.** At 7 m over hot ground it moves the markers about 0.006 pixel.

**Facing the low sun costs accuracy but stays in spec.** The 95% error roughly doubles at sunrise with the camera facing east.

**Near edge-on the module hides the far marker.** At about +6° to +14°, the near pink marker picks the right reading.

## Still to prove with hardware

- Real color behavior and auto white balance of an OV2640 camera in Arizona sun
- The real retroreflected return from a chosen LED and tape at 7 m
- ARRAY's real row length, tube size and drive-point location, which set the twist
- Marker fading under UV over months
