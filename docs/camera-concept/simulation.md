---
title: Field Simulation
hide:
  - toc
---

# Field Simulation

A physics-based model of the field near Phoenix. It covers the real sun path and daylight levels, gusting wind that twists the torque tube, a camera post that bends in the wind, and a camera sensor with real exposure limits. It runs in your browser. Built by Lakshanand Sugumar.

[Open full screen](sim/index.html){ .md-button .md-button--primary target="_blank" }

<div style="position:relative; width:100%; aspect-ratio:16/10; min-height:600px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; overflow:hidden">
  <iframe src="../sim/index.html" title="Tilt camera field simulation" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; border:0"></iframe>
</div>

## Try this

1. Press **Teach** at midday. This is the on-site calibration sweep against a reference inclinometer.
2. Press **Run 40-angle test** to see the accuracy.
3. Move **Markers and camera along the row** out toward the row end and raise the **wind**. Watch the tube twist under the markers.
4. Slide past sunset. Without the flash the camera sees nothing. Turn the flash on and lower the **LED intensity** to see where it stops working.

## The physics

| Part | Model | Source of the numbers |
| --- | --- | --- |
| Sun position | Solar declination and hour angle for 33.4° N | Standard solar geometry |
| Sunlight | Direct beam through the atmosphere using the Kasten–Young air mass, about 105 lm/W | Standard clear-sky model |
| Twilight | Sky illuminance from 600 lx at sunset to 0.0007 lx at −18° | Published twilight levels |
| Tracking | True tracking with backtracking for the row gap, ±60° limit, stow at night | Standard single-axis backtracking geometry |
| Wind | Mean speed plus gusts with 20% turbulence intensity and a 25 m length scale | Typical for open desert terrain near the ground |
| Wind torque | Torque per metre = ½ ρ U² · C<sub>M</sub>(tilt) · chord² | Hinge-moment form used for tracker wind design |
| Tube twist | Steel torsion, G = 79.3 GPa, fixed at the drive point. First twist mode about 1.9 Hz, 3% damping | Torsion of a thin-walled square tube |
| Camera post | 2 in. schedule-40 steel pipe, cantilever bending under wind drag | Beam bending |
| Heat shimmer | Angle-of-arrival jitter from air turbulence strength C<sub>n</sub>² | Standard turbulence optics |
| Camera exposure | 1/8000 s to 1/15 s, then gain up to 16×. Read noise and shot noise grow with gain | Typical small CMOS sensor |
| Night flash | Retroreflected luminance = R<sub>A</sub> × LED intensity ÷ distance², R<sub>A</sub> = 250 cd/(lx·m²). Flash frames use their own exposure | Prismatic retroreflective sheeting rating |

!!! warning "Assumed values, not from ARRAY"
    ARRAY hasn't given row dimensions, tube size or wind data yet, so these are assumptions:
    60 m rows driven at the middle, a 127 mm square tube with 3.5 mm wall, 28 kg modules, and a hinge-moment peak of C<sub>M</sub> = 0.13.
    The twist results scale directly with these, so swap in ARRAY's numbers when they arrive.

!!! note "Still not modeled"
    Aeroelastic effects such as torsional galloping, the drive linkage's own flex and backlash, real lens distortion, motion blur during long night exposures, marker fading from UV, and rain.

The camera reports the angle to the ARRAY controller over RS-485. ARRAY hasn't specified the controller's message format yet, so the simulation shows only the angle.
