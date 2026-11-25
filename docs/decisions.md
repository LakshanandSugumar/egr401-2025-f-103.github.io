---
title: Design Decisions
---

# Design Decisions

The two decisions that shaped the project are the **Nov 3 concept selection** with the sponsor and the **Nov 19 range revision**.

## Oct 28, 2026: Preliminary Design Review

We scored four concepts out of 18 points at PDR. IR time-of-flight led going into the sponsor meeting.

| Concept | Score (out of 18) |
| --- | ---: |
| C1 Optical | 5.25 |
| C2 Magnetic | 11.50 |
| C3 Ultrasonic | 11.75 |
| **C4 IR time-of-flight** | **13.25** |

## Nov 3, 2026: Concept 5 selected

At the sponsor meeting, ARRAY endorsed a hybrid IR approach: **emitter and detector on the drive row, passive reflector on the follower row.**

- **Magnetic encoder rejected** because running wire between rows costs too much.
- **Ultrasonic rejected** because it needs power on the follower row.
- **Both reflector variants approved** for prototyping: flat square and shaped.
- **Action items:** source IR emitters that can be purchased off the shelf, target IP66 sealing, prefer UL / cULus listed parts.

## Nov 16–17, 2026: Plan rebuilt on 11 milestones

Following faculty feedback, the team rebuilt the project plan from 9 to 11 milestones. The board from WBS Day (Nov 16) is the source of truth. See [Milestones](milestones.md).

## Nov 19, 2026: Sensor range revision

!!! warning "Finding"
    The bare SFH 4547 emitter and BPW34 detector pair is only good for about 3–4 m, but rows are 6–8 m apart. The round-trip return in sunlight is the biggest design risk.

**Decision:**

- Keep the bare pair for bench work proving the angle-measurement principle.
- Add one **Benewake TFmini Plus** LiDAR module (~$52) to test the full 6–8 m range in the field.
- The sensor budget line rose from about $100 to about $150, and the total team budget from $490 to **$540**.

## Nov 23, 2026: Budget settled

The team budget was finalized at **$540**. The under-$10 per-unit cost to ARRAY covers the sensing-node electronics at about 100 units. The enclosure and field illuminator are costed separately, and we're confirming that scope with ARRAY. See [Budget & Unit Cost](budget.md).

## Under consideration: getting follower-row data at the test site

Options for under $5 that we're comparing. None has been chosen yet:

| Option | Approx. cost | Notes |
| --- | ---: | --- |
| The reflector itself | $0.20 | The design's own channel |
| Battery + HC-12 RF pair | ~$4 | Test equipment only |
| Small solar cell + nRF24L01+ | ~$4 | ~$2.50 panel + ~$1.50 buffer |
