---
title: Cost Under $10
---

# Cost Under $10

The whole unit, including camera, 3D-printed shell and mounting hardware, has to cost under $10. A build from off-the-shelf modules with **no custom PCB** gets there.

Estimates at about 100 units. Prices are not quotes.
{ .md-caption }

| Item | Est. cost |
| --- | ---: |
| ESP32-CAM board (ESP32 + OV2640 camera + memory + built-in flash LED) | $4.00 |
| RS-485 adapter module (MAX485 class) | $0.60 |
| 24 V → 3.3/5 V buck module (MP1584 class) | $0.50 |
| Wires, screw terminal, heat-shrink | $0.40 |
| 3D-printed ASA shell, about 40 g | $0.80 |
| Clear window + gasket + small cable gland | $0.50 |
| Mounting: U-bolt or hose clamp + screws | $0.60 |
| Markers on the follower row (colored or retroreflective tape) | $0.30 |
| **Total** | **≈ $7.70** |

## What the margin buys

About $2.30 is left under $10. That can cover price swings or a second camera facing the other way, so one camera always has the sun behind it.

## Trade-offs of no PCB

- **Faster start.** Firmware work can begin right away with no board design or fabrication.
- **Heat rating.** Cheap camera boards and modules usually aren't guaranteed for +60 °C, so test them before trusting them in the field.
- **Wiring.** Hand-soldered joints can loosen with wind vibration. Use screw terminals and strain relief, and pot the connections.
- **Sponsor fit.** ARRAY prefers UL/cULus-listed parts. Whether a module build is acceptable beyond prototypes needs confirming with ARRAY.
