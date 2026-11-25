---
title: Results
---

# Simulation Results

Results with every fix in place. The [Test Log](log.md) records what failed, why, and how it was fixed.

Each row is one run of 40 random follower angles between −55° and +55°, using the [field simulation](simulation.md) with a 7 m row gap and 10 cm markers. The camera was taught once at noon on June 21. Errors are against the true angle at the markers. Defaults: 6 m/s wind with gusts, 40 °C air, 10% lens dust, 4 e⁻ read noise. Results vary a little from run to run.
{ .md-caption }

!!! success "Every condition below is within the ±1° target"
    Every reading in every condition below was within ±1°, and the camera produced a reading at every angle.

## Daytime and weather

| Conditions | Markers read | 95% within | Max error |
| --- | ---: | ---: | ---: |
| Clear, 12:00 | 40/40 | 0.17° | 0.23° |
| Clear, 09:00 | 40/40 | 0.60° | 0.68° |
| Sunrise 06:12, camera facing the sun | 40/40 | 0.32° | 0.34° |
| Windy, 14 m/s | 40/40 | 0.48° | 0.50° |
| Light rain | 40/40 | 0.37° | 0.40° |
| Monsoon thunderstorm, 50 mm/h, 15 m/s | 40/40 | 0.53° | 0.58° |
| Hail, 25 mm stones | 40/40 | 0.42° | 0.48° |
| Snow | 40/40 | 0.24° | 0.24° |
| Dust storm (haboob), 60 m visibility, 18 m/s | 40/40 | 0.45° | 0.47° |
| Fog, 120 m visibility | 40/40 | 0.19° | 0.49° |
| 50 °C air (sensor about 65 °C) | 40/40 | 0.29° | 0.46° |

## Night (Dec 21, retroreflective markers, 20 cd LED, 2 ms flash pulse)

| Time | Markers read | 95% within | Max error |
| --- | ---: | ---: | ---: |
| 17:45, dusk | 40/40 | 0.51° | 0.61° |
| 18:30 | 40/40 | 0.53° | 0.59° |
| 19:30 | 40/40 | 0.40° | 0.69° |
| 04:30, pre-dawn | 40/40 | 0.53° | 0.54° |
| 18:30 in a thunderstorm, markers 25 m out | 40/40 | 0.44° | 0.55° |

## Mechanics and aging

| Conditions | Markers read | 95% within | Max error | Notes |
| --- | ---: | ---: | ---: | --- |
| Markers 25 m out, 12 m/s | 40/40 | 0.11° | 0.11° | Tube twisted up to 5.8° under the markers, measured correctly |
| Night, 25 m out, 12 m/s | 40/40 | 0.42° | 0.49° | 2 ms flash pulse freezes the twisting row |
| Prismatic sheeting after 10 years | 40/40 | 0.37° | 0.51° | |
| Lens distortion k₁ = −0.40 | 40/40 | 0.19° | 0.31° | |
| Drive linkage backlash 1° | 40/40 | 0.32° | 0.34° | Measured as real misalignment |

## What it takes to work in all conditions

| Requirement | Why |
| --- | --- |
| Near-marker fallback in firmware | The torque tube blocks the far marker at about +5° to +14° |
| Lens hood + water-shedding window coating | Rain, hail and snow on the window |
| 7-frame median in precipitation, 3 otherwise | Drops and flakes crossing the markers |
| Noise-adaptive color threshold | Faded markers and dim conditions |
| Snow caps over the markers | Snow on the marker faces |
| 10-year-rated prismatic retroreflective sheeting | UV fading. Vinyl fails within 3 years, fluorescent within 6 months |
| 20 cd or brighter LED, 2 ms pulse, flash/no-flash subtraction | Night, and freezing the row's motion |
| Teach once on site against a reference inclinometer | Absorbs lens distortion and mounting geometry |

## What it found about the tracker itself

- **Wind twist:** with the assumed tube, the follower 25 m from the drive point twists up to about 6° at 12 m/s and about 9° at 19 m/s. Markers at the drive point measure linkage misalignment alone. Markers near the row end also see wind twist.
- **Torsional galloping:** in flat stow above about 18 m/s the twist damping turns negative. Torsional dampers fix it. A 30° stow avoids it but takes a large steady twist. This is ARRAY's structure, so raise it with ARRAY.

These numbers depend on assumed row and tube sizes. Swap in ARRAY's values when they arrive.
