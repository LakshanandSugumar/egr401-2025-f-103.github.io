---
title: Home
hide:
  - toc
---

<div class="hero" markdown>
<p class="eyebrow">Team 20 · EGR 401 / 402 Senior Capstone · ASU Polytechnic</p>

# Solar Tracker Tilt-Sensing System

<p class="pitch">A sub-$10 tilt sensor for solar tracker rows that needs no power on the follower row.</p>

Sponsored by **ARRAY Technologies**, a solar tracker manufacturer.

[The problem](problem.md){ .md-button .md-button--primary } [How it works](solution.md){ .md-button }
</div>

<div class="stat-row">
  <div class="stat"><span class="num">±1°</span><span class="label">Tilt accuracy target</span></div>
  <div class="stat"><span class="num">≈ $9.90</span><span class="label">Est. electronics per unit at ~100 units</span></div>
  <div class="stat"><span class="num">0 W</span><span class="label">Power on the follower row</span></div>
  <div class="stat"><span class="num">6–8 m</span><span class="label">Gap between rows</span></div>
</div>

## What we're building

Single-axis solar trackers turn rows of panels to follow the sun. One **drive row** carries the motor, and the **follower rows** are linked to it mechanically. If a follower row drifts out of line with the drive row, the farm loses energy and the row can be damaged.

Our device measures the follower row's tilt relative to the drive row and reports it to the ARRAY controller over RS-485. Everything powered sits on the drive row. The follower row only carries a passive reflector.

<div class="grid cards" markdown>

-   :material-alert-circle-outline: **[The Problem](problem.md)**

    Why follower-row drift matters and the sponsor's hard constraints.

-   :material-lightbulb-on-outline: **[Our Solution](solution.md)**

    Infrared pulses, a passive reflector and a differential photodiode pair.

-   :material-source-branch: **[Design Decisions](decisions.md)**

    How we got from five concepts to one, and what changed since.

-   :material-chip: **[Technology](technology.md)**

    Emitter, detector, electronics and power budget.

-   :material-currency-usd: **[Budget & Unit Cost](budget.md)**

    The $540 team budget and the per-unit cost to ARRAY.

-   :material-calendar-range: **[Milestones](milestones.md)**

    Eleven milestones from design to handoff on May 1, 2027.

</div>

## Project window

**Fall 2026:** design. **Spring 2027:** build and test. **May 1, 2027:** handoff to ARRAY.

Faculty: Malle Schilling (EGR 401/402 instructor) and Dr. Samantha Brunhaver (course lead).
