---
title: Budget & Unit Cost
---

# Budget & Unit Cost

<div class="stat-row">
  <div class="stat"><span class="num">$540</span><span class="label">Team prototype budget</span></div>
  <div class="stat"><span class="num">≈ $9.90</span><span class="label">Per-unit electronics cost to ARRAY</span></div>
  <div class="stat"><span class="num">$2.23</span><span class="label">Emitter + detector pair, bare parts</span></div>
</div>

## Team budget and resources

The final table, settled Nov 23, 2026.

| Resource | Linked WBS | Needed | Order by | Vendor | Cost |
| --- | --- | --- | --- | --- | ---: |
| Sensors: SFH 4547 + BPW34 pairs + TFmini Plus | 4.2, 5.4, 7.6 | 01/11/27 | 12/21/26 | Digi-Key / Mouser | $150 |
| Dev board | 4.2, 5.4 | 01/11/27 | 12/28/26 | Digi-Key | $40 |
| Reference inclinometer | 4.2, 7.4, 8.3 | 01/11/27 | 01/04/27 | Amazon / Digi-Key | $40 |
| PCB fabrication (~5 boards) | 5.3, 6.1 | 02/16/27 | 02/02/27 | JLCPCB / OSH Park | $60 |
| PCB components | 5.3, 6.1 | 02/16/27 | 02/06/27 | Digi-Key | $90 |
| Enclosure / gaskets / glands | 5.3, 6.1, 7.2 | 02/08/27 | 01/29/27 | Digi-Key | $50 |
| Mounting / 3D printing | 6.1, 7.2 | 02/08/27 | 02/01/27 | ASU Poly makerspace | $50 |
| Lab bench time | 6.2, 7.4 | 02/19/27 | 02/05/27 | ASU Poly lab | $0 |
| Tilt fixture materials | 7.4 | 03/26/27 | 03/19/27 | Makerspace | $40 |
| USB-to-RS-485 adapter | 7.5 | 03/26/27 | 03/19/27 | Amazon / Digi-Key | $20 |
| ARRAY site access | 8.1, 8.3 | 04/05/27 | 03/06/27 | ARRAY Technologies | $0 |
| SolidWorks | 3.3.2, 5.1 | 11/30/26 | — | ASU student license | $0 |
| KiCad | 5.2 | 01/11/27 | — | Free | $0 |
| **Total** | | | | | **$540** |

Most of the $150 sensor line is the $52 TFmini Plus. The bare emitter and detector parts cost about $2.23 per pair. JLCPCB is the low-cost route for the PCB line.

## Estimated unit cost to ARRAY

Estimated per unit at about 100 units.

| Item | Cost |
| --- | ---: |
| SFH 4547 emitter | $0.44 |
| BPW34 detectors ×2 (differential pair) | $1.44 |
| ESP32-S3 chip (bare) | ~$2.50 |
| RS-485 transceiver (SP3485 class) | ~$0.75 |
| AP63203 buck regulator | $0.71 |
| Inductor 6.8 µH | $0.28 |
| TIA op-amp + emitter-driver MOSFET | ~$0.50 |
| Caps / resistors / passives | ~$0.80 |
| Connectors (power + RS-485) | ~$0.75 |
| PCB (JLCPCB at volume) | ~$1.50 |
| Reflector (follower row) | ~$0.20 |
| **Total** | **≈ $9.90** |

!!! info "What the estimate covers"
    - **Electronics only.** A weatherproof enclosure and glands add roughly $5–15 per unit at these volumes.
    - **Uses the bare MCU chip**, not the module.
    - **Field illuminator supplied by ARRAY.**
    - **Assumes ~100 units.** At 5-unit prototype quantities the same board costs 3–4× more per unit.

    We're confirming with ARRAY whether the under-$10 target means electronics only or the whole unit, enclosure included.
