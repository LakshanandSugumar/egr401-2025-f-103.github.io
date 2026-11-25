---
title: Technology
---

# Technology

## The optical link

=== "Emitter: SFH 4547"

    **ams OSRAM SFH 4547**, a 940 nm infrared LED mounted on the drive row.

    - 50 mW/sr radiant intensity
    - $0.86 each in small quantities, $0.44 at 100
    - Pulses at 100 mA, which is more than an MCU pin can supply, so it needs an emitter-driver MOSFET

=== "Detector: BPW34"

    **Vishay BPW34**, a PIN photodiode used as a **differential pair**.

    - 950 nm peak sensitivity, ±65° acceptance angle
    - 100 ns response, fast enough for pulse timing
    - $1.37 each in small quantities, $0.72 at 100
    - Photocurrent is read through a transimpedance amplifier (TIA)

    !!! note
        We aren't using the SFH 309 phototransistor because it's end of life.

=== "Range test: TFmini Plus"

    **Benewake TFmini Plus**, a complete LiDAR module with its own emitter and detector.

    - 0.1–12 m range, IP65
    - ~$52
    - It measures distance, not angle, so it's used **only to validate range** across the 6–8 m gap. It isn't part of the product.

=== "Field illuminator"

    For field use, ARRAY supplies the illuminator. It isn't part of the team budget.

    - Primary: **Bosch IIR-50940-SR**: 940 nm, IP66, cULus, 12–32 V DC, 13 W, rated −50 to +50 °C
    - Alternate: **Pelco IR940M-60**
    - These illuminators stay on continuously with a photocell, so our timing channel uses pulse modulation.
    - We're checking the +50 °C rating against our +60 °C target with ARRAY.

## Electronics

The design builds on the board pattern the team used in EGR 314.

| Block | Part | Notes |
| --- | --- | --- |
| MCU | ESP32-S3, bare chip | ~$2.50 vs. ~$4.50–5 for the WROOM module; keeps the unit under $10 |
| Power | AP63203WU-7 buck, 12 V → 3.3 V, 2 A | With a 6.8 µH inductor, MBRS340T3G Schottky diodes and a PTC polyfuse. Max input is being checked against the 24 V field supply. |
| Output | MAX485 / SP3485-class 3.3 V RS-485 transceiver | ~$0.75; carries tilt readings to the ARRAY controller |
| Analog front end | TIA op-amp + emitter-driver MOSFET | Reads the photodiodes and drives the emitter pulses |
| Enclosure | IP65 polyamide cable glands (M32 / M40), enclosure and gaskets | Weather sealing |

## Bench and test equipment

- **Klein Tools 935DGGP** reference inclinometer (±0.1° near 0°/90°, ±0.2° elsewhere) for building the calibration curve
- **DTECH USB to RS-422/RS-485** FTDI adapter for testing communication
- Breadboard, passives, fuses, bench power supply, multimeter
- 3D-printed enclosures for prototypes

## Power budget

| Location | Power | Breakdown |
| --- | ---: | --- |
| Bench | < 5 W | Prototype electronics |
| Drive row (field) | ≈ 15–16 W | Bosch illuminator 13 W (≈ 0.55 A at 24 V) + electronics 2–3 W, from the drive row's 24 V supply |
| Follower row | **0 W** | Passive reflector only |
