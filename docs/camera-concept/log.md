---
title: Test Log
---

# Test Log: Where the Markers Were Lost, and the Fixes

A record of every failure the [field simulation](simulation.md) found, the cause, the fix, and the result before and after. Each test is 40 random follower angles between −55° and +55° unless noted, judged against the ±1° target. The loss sweeps step through every degree from −60° to +60°. Testing and fixes by Lakshanand Sugumar, November 2026.

## Summary

| # | Where it failed | Cause | Fix | Before | After |
| --- | --- | --- | --- | --- | --- |
| 1 | Every condition, follower at +5° to +14° | Torque tube blocks the line of sight to the far marker | Read the angle from the near marker when the far one is blocked | 35–38 of 40 read | 40 of 40, max 0.24° |
| 2 | Thunderstorm, rain | Drops crossing the markers in most frames | 7-frame median in rain, hail and snow | 39/40 within ±1°, max 3.31° | 40/40, max 0.55° |
| 3 | Snow | Snow building up on the marker faces shifts their color unevenly | 3D-printed snow caps over the markers | 30/40 within ±1° | 40/40, max 0.24° |
| 4 | UV aging | Colors fade until the fixed threshold rejects them | Noise-adaptive threshold, and 10-year-rated prismatic sheeting | 0/40 at 10 years | 40/40, max 0.51° |
| 5 | Night, no light | Nothing to see | Retroreflective sheeting with a 20 cd LED flash | 0/40 | 40/40 all night |
| 6 | Night, row twisting in wind | Long exposure blurs the moving markers | 2 ms flash pulse, with the reference frame taken the same way | 39/40, max 1.54° | 40/40, max 0.49° |
| 7 | High wind, flat stow | Torsional galloping: wind damping goes negative | Torsional dampers on the follower | damping −0.6% | damping +7.2% |

## 1. Torque tube blocks the far marker

**Found by:** the loss sweep, in every weather condition. The yellow marker on the far edge disappeared between about +5° and +14°.

**Cause:** at those angles the camera, the torque tube and the far marker line up, so the tube is in the way. I first tried moving the far marker onto a 25 cm arm past the module edge. The loss only moved to +4° to +12°. Any marker on the far side of the tube has to pass behind the tube at some angle, so no mounting position can avoid it.

**Fix:** the near pink marker is never behind the tube. When the far marker is blocked, the camera reads the angle from the near marker's position alone. The camera post moves only about 0.01° in wind, so the near marker alone is accurate.

**Result:** sweeps in clear, windy, rain, thunderstorm, hail, snow, dust storm and fog all had **zero angles without a reading**. Noon test: 40/40, max error 0.24°.

## 2. Rain and storm drops

**Found by:** the thunderstorm test. One reading was off by 3.31°.

**Cause:** in heavy rain, drops on the window and in the air cross the markers in most frames, which a 3-frame median can't reject.

**Fix:** a lens hood with a water-shedding window coating, plus an adaptive filter. The camera takes the median of 7 frames in rain, hail or snow, and 3 otherwise. The follower moves slowly, so the extra half-second costs nothing.

**Result:** thunderstorm 40/40 within ±1°, max 0.55°. Hail max 0.48°. Rain max 0.40°.

## 3. Snow on the markers

**Found by:** the snow test, with a steady bias of about 0.5° rather than random scatter.

**Cause:** snow building up on the markers changes the color of the lit and shaded faces by different amounts, which moves the blob's center.

**Fix:** small 3D-printed snow caps over each marker.

**Result:** without caps, 30/40 within ±1°. With caps, 40/40, max 0.24°.

## 4. UV fading

**Found by:** the aging tests. After 10 years, 0 of 40 readings.

**Cause:** faded markers still stand out from the noise, but the fixed color threshold rejected them.

**Fix:** the threshold now adapts to each image's own noise. It can drop below the old value for faded markers, but never rises above it, so rain clutter can't push it up. The marker material also matters:

| Material | Result |
| --- | --- |
| Prismatic retroreflective sheeting, 10-year rated | **40/40 at 10 years, max 0.51°** |
| Standard colored vinyl | 24/38 within ±1° at 3 years, none found at 6 years |
| Fluorescent vinyl tape | 20/36 within ±1° at 6 months, none found at 1 year |

**Decision:** use 10-year-rated prismatic sheeting.

## 5. Night

**Found by:** night tests. With no light, no readings.

**Fix:** retroreflective sheeting with a 20 cd LED flash on the drive row. The camera takes one frame with the flash and one without, then subtracts them. An 8 cd LED was marginal and 4 cd failed.

**Result (Dec 21):** 40/40 within ±1° at 17:45 (dusk), 18:30, 19:30 and 04:30 (pre-dawn). Max error 0.69°.

### Glow-in-the-dark markers (strontium aluminate)

Glow cores charge in sunlight and glow at night with no power. I modeled the afterglow fading as roughly t^−1.1, starting at 0.3 cd/m² ten minutes after sunset, and the camera stacking ten 2-second exposures.

| Time after sunset | Glow | Result |
| --- | --- | --- |
| 52 min | 49 mcd/m² | All found, but readings biased about 2° (cause not yet found) |
| 97 min | 25 mcd/m² | **40/40 within ±1°, max 0.69°** |
| 157 min | 15 mcd/m² | 0/40, even with 30 cm markers |
| 11.6 h (pre-dawn) | ~1 mcd/m² | 0/40 |

**Decision:** glow markers can't cover the whole night with a camera this cheap, because the afterglow fades too far. The flash covers the whole night, so it's the primary night method. Glow stays in the simulation as an option.

## 6. Motion blur at night

**Found by:** markers 25 m from the drive point, in 12 m/s wind, at night. The row twists up to ±7° at 1.9 Hz.

**Cause:** a 1/15 s exposure blurs the moving markers. The flash's reference frame was also taken later than the lit frame.

**Fix:** a 2 ms flash pulse, with the reference frame taken with the same timing straight after.

**Result:** long exposure 39/40, max 1.54°. Pulse 40/40, max 0.49°. Pulse in a night thunderstorm: 40/40, max 0.55°.

## 7. Torsional galloping

**Found by:** watching the twist live in 19 m/s wind, with the rows in flat stow and the markers 25 m out.

**Cause:** near flat tilt, wind adds negative damping to the twist motion. At 19 m/s the total damping was −0.6%, so the twist grows on its own. It grows slowly at that speed, but the effect increases with wind speed.

| Setup | Total damping | Largest twist in 12 s |
| --- | ---: | ---: |
| Flat stow | −0.6% (galloping) | 0.74°, growing |
| 30° stow | +3.0% | 14.1° (steady wind torque at 30°) |
| Flat stow + dampers | +7.2% | 3.7° |

**Decision:** flat stow with torsional dampers. A 30° stow avoids galloping but takes a large steady twist with the assumed tube. This is ARRAY's structure, so the camera just measures it. Recommend raising it with ARRAY.

## Also checked, no fix needed

| Effect | Result |
| --- | --- |
| Lens barrel distortion, k₁ = −0.40 | The teach table absorbs it: max 0.38°, or 0.31° with correction |
| Drive linkage backlash, 1° | The camera measures it as real misalignment: max 0.34° |
| Camera post bending | About 0.01° at 12 m/s, and the two-marker gap cancels it |
| Heat shimmer | About 0.006 pixel |
| 50 °C air (sensor about 65 °C) | 40/40, max 0.46°. The sensor is above the OV2640's 50 °C stable-image range, so test real hardware |
| Dust storm, fog, sunrise glare | All 40/40 within ±1° |

## Bugs found in the simulator itself

These were problems in my simulation code, not in the design:

- **Night was too bright.** The night sky used an arbitrary light level. Replaced with measured twilight levels.
- **Brighter LED gave worse results.** Flash frames used a fixed exposure, so markers clipped to white. Fixed by setting the exposure from the expected return.
- **Glow was invisible.** The 16-bit image buffer rounded very dim light to zero. Fixed with a 32-bit float buffer.
- **Noise model was too crude.** Replaced with a physical model in electrons (read noise, shot noise, dark current).
- **Image rounded before noise.** Sub-DN signals vanished before stacking could recover them. Fixed by adding noise before 8-bit rounding, as a real sensor does.
- **Mismatched reference.** The test compared a median of frames against an average of true angles. Fixed by keeping the median frame together with its own true angle.

## Still open

- The about 2° bias of glow markers at dusk
- Real hardware: an OV2640's color and white balance in Arizona sun, the real LED return at 7 m, and sensor behavior above 50 °C
- ARRAY's real row length, tube size, stow angles and wind data, which set the twist and galloping numbers
