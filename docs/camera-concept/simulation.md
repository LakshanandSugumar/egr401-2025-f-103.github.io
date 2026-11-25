---
title: Field Simulation
hide:
  - toc
---

# Field Simulation

A physics-based model of the field near Phoenix, covering:
- **Sun and light:** the real sun path and daylight, twilight and night light levels
- **Weather:** rain, thunderstorms, hail, snow, dust storms and fog
- **Structure:** gusting wind that twists the torque tube, including torsional galloping, and drive-linkage backlash
- **Optics:** a real lens with distortion, and UV fading of the markers
- **Sensor:** a camera with real exposure limits and noise

It runs in your browser. Built by Lakshanand Sugumar.

[Open full screen](sim/index.html){ .md-button .md-button--primary target="_blank" }

<div style="position:relative; width:100%; aspect-ratio:16/10; min-height:600px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; overflow:hidden">
  <iframe src="../sim/index.html" title="Tilt camera field simulation" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; border:0"></iframe>
</div>

## Try this

1. Press **Teach** at midday. This is the on-site calibration sweep against a reference inclinometer.
2. Press **Run 40-angle test** to see the accuracy, or **Find marker losses** to sweep every degree and list where a marker goes missing and why.
3. Pick a **Weather** condition, then turn the **Fixes** off one at a time to see what each one does.
4. Move **Markers and camera along the row** toward the row end, raise the wind, and watch the tube twist.
5. Slide past sunset. The flash keeps it working all night. Try the **glow-in-the-dark cores** instead and watch them fade.

## The physics

| Part | Model |
| --- | --- |
| Sun | Solar position for 33.4° N. Direct beam through the Kasten–Young air mass, about 105 lm/W. Clear-sky diffuse light and published twilight levels down to 0.0007 lx |
| Clouds | Overcast cuts the direct beam and scales the diffuse light for each weather type |
| Visibility | Koschmieder extinction, σ = 3.912 / visibility. Rain adds σ ≈ 0.21 R^0.74 per km |
| Rain, snow, hail | Falling at real speeds and drifting with the wind. Hail falls at its terminal velocity with impact energy shown. Drops and flakes on the window refract and blur the image |
| Tracking | True tracking with backtracking. Generic stow rules: hail and snow to 60°, wind above 17 m/s to 30° or flat |
| Wind | Gusts with 20% turbulence intensity and a 25 m length scale. Torque = ½ρU² · C<sub>M</sub>(tilt) · chord² |
| Tube twist | Steel torsion, first mode about 1.9 Hz, 3% damping. Galloping is modeled as negative aerodynamic damping near flat tilt |
| Drive linkage | A backlash deadband that flips side when the torque reverses, plus elastic wind-up |
| Camera post | 2 in. schedule-40 steel pipe bending under wind drag |
| Lens | Barrel distortion with k₁ adjustable |
| Sensor | 640 × 480. Auto exposure from 1/8000 s to 1/15 s, then gain to 16×. Read noise, shot noise and dark current in electrons, with dark current doubling every 6.5 °C. Rounded to 8 bits after the noise |
| Sensor heat | Enclosure temperature from the air and the sun. Warns above the OV2640's 50 °C stable-image and 70 °C operating limits |
| Night flash | Retroreflected luminance = R<sub>A</sub> × LED intensity ÷ distance². Flash frames can be 2 ms pulses |
| Glow cores | Strontium aluminate afterglow decaying as t^−1.1. Night stacking of ten 2 s exposures |
| UV aging | Color fades exponentially with years in the field, at a different rate for each marker material |

!!! warning "Assumed values, not from ARRAY"
    ARRAY hasn't given row dimensions, tube size, stow angles or wind data yet, so these are assumptions:
    60 m rows driven at the middle, a 127 mm square tube with 3.5 mm wall, 28 kg modules, a hinge-moment peak of C<sub>M</sub> = 0.13, galloping onset near 18 m/s, and linkage stiffness of 1.5 MN·m/rad.
    Fade rates, glow brightness and sensor noise are representative values, not measurements. Swap in real numbers when they arrive.

The camera reports the angle to the ARRAY controller over RS-485. ARRAY hasn't specified the controller's message format yet, so the simulation shows only the angle.
