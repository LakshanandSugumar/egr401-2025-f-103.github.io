---
title: Field Simulation
hide:
  - toc
---

# Field Simulation

A 3D model of the field near Phoenix, with physically based lighting, a real sun path for any date and time, and a model of the camera sensor. It runs in your browser. Built by Lakshanand Sugumar.

[Open full screen](sim/index.html){ .md-button .md-button--primary target="_blank" }

<div style="position:relative; width:100%; aspect-ratio:16/10; min-height:600px; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; overflow:hidden">
  <iframe src="../sim/index.html" title="Tilt camera field simulation" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; border:0"></iframe>
</div>

## Try this

1. Press **Teach** at midday. This is the on-site calibration sweep.
2. Press **Run 40-angle test** to see the accuracy.
3. Move **Solar time** toward sunrise with the camera looking east and watch sun glare take over the image.
4. Raise **Dust on the lens** and **Wind**, or slide past sunset and turn on **Retroreflective markers + LED flash**.

## What is modeled

| Part | How it's modeled |
| --- | --- |
| Site | Phoenix, 33.4° N. North–south rows, 5 rows, 38 m long, 6–8 m apart |
| Tracker | Single-axis, follows the sun, ±60° limit, stows flat at night. The follower row adds the misalignment you set |
| Modules | 2.28 × 1.13 m, 1-in-portrait, glass with clearcoat reflections, aluminum frame, white backsheet |
| Sun and sky | Sun position from date and solar time. Physical sky, soft shadows, haze |
| Camera | 640 × 480, 60° horizontal view, on a fixed post 0.5 m above the tube, aimed at the follower's tube |
| Sensor effects | Auto exposure, read and shot noise, 8-bit clipping, veiling glare when the sun is near the view, lens dust |
| Wind | Shakes the camera post and twists the follower row slightly |
| Markers | 10 cm pink and yellow plates on the frame edges, 1 m apart along the row |
| Night option | Retroreflective markers and an LED flash, with one frame taken with the flash and one without, then subtracted |

!!! note "What it doesn't model"
    Heat shimmer over hot modules, real lens distortion, marker color fading from UV, rain, and the exact behavior of a specific camera chip. A bench test with a real ESP32-CAM is still needed.
