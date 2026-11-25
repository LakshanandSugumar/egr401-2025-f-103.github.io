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
| Markers: 10-year-rated prismatic retroreflective sheeting, pink and yellow | $0.40 |
| 20 cd LED + driver MOSFET for the 2 ms night flash | $0.35 |
| Lens hood and marker snow caps (printed with the shell) | $0.20 |
| Water-shedding window coating | $0.05 |
| **Total** | **≈ $8.40** |

The extra items are what the [Test Log](log.md) showed it takes to work in every condition: night, rain, hail, snow, dust and 10 years of UV. Torsional dampers, if ARRAY adds them, are part of the tracker structure and not in this unit cost.

## What the margin buys

About $1.60 is left under $10. That can cover price swings.

## Trade-offs of no PCB

- **Faster start.** Firmware work can begin right away with no board design or fabrication.
- **Heat rating.** Cheap camera boards and modules usually aren't guaranteed for +60 °C, so test them before trusting them in the field.
- **Wiring.** Hand-soldered joints can loosen with wind vibration. Use screw terminals and strain relief, and pot the connections.
- **Sponsor fit.** ARRAY prefers UL/cULus-listed parts. Whether a module build is acceptable beyond prototypes needs confirming with ARRAY.
