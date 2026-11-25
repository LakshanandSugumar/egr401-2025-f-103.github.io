---
title: The Problem
---

# The Problem

Single-axis solar trackers rotate rows of panels to follow the sun across the sky. In a typical layout, one **drive row** carries the motor, and several **follower rows** are mechanically linked to it so they turn together.

If a follower row's tilt drifts out of alignment with the drive row:

- the farm produces less energy, because those panels no longer face the sun correctly, and
- the row can be mechanically damaged.

ARRAY Technologies needs a **low-cost way to measure the follower row's tilt angle relative to the drive row** and report it to the ARRAY controller.

## Sponsor constraints

!!! danger "No power on the follower row"
    Power exists only on the drive (main) row. Anything placed on the follower row has to work without electricity.

!!! warning "Under $10 per unit"
    The final device cost to ARRAY has to stay under $10 per unit. See [Budget & Unit Cost](budget.md) for what that figure covers.

!!! info "6–8 m between rows"
    The sensor has to work across the full gap between rows in the field.

!!! info "Outdoors, all year"
    Direct sunlight, heat up to a +60 °C target, and weather. The enclosure needs to be sealed (IP66 target).

!!! success "±1° accuracy, RS-485 output"
    Tilt must be measured to within ±1° and reported to the ARRAY controller over RS-485.

## Standards we design to

| Standard | What it covers |
| --- | --- |
| IEC 60529 | Ingress protection (IP66 target) |
| UL 508A | Industrial control panels (UL / cULus preferred by the sponsor) |
| TIA/EIA-485 | RS-485 electrical interface |
