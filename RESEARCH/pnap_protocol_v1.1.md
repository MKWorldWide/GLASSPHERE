# Pyramid Node Activation Protocol (PNAP) — v1.1 (2025)

Status: Active Development

## Objectives
- Establish a reproducible, non‑invasive protocol to measure resonance behavior at pyramid sites.
- Validate stimulation envelopes safely (very low amplitude, short duration, capped duty cycle).
- Produce anonymized datasets suitable for external review and replication.

## What’s New in v1.1
- Tighter activation envelope and abort thresholds.
- Standard measurement kit and calibration procedures.
- Unified data schema and minimal metadata requirements.
- Independent Safety Officer sign‑off for each activation window.

## Measurement Kit
- LiDAR (cm‑scale), Ground‑Penetrating Radar (50–100 m), fluxgate/quantum magnetometer (≥1 pT), acoustic array (1–100 kHz), EM probes (0.1–1000 Hz), weather station.
- GNSS time sync (PTP/IRIG‑B where available); redundant logging.

## Stimulation Envelope (Low‑Amplitude)
- Frequency set: {7.83 Hz ± 0.1 Hz}, ± Golden‑ratio sidebands, optional acoustic sub‑harmonics.
- Field amplitude cap (site‑specific): Derived from baseline variance; start at 3–5× noise floor, never exceeding heritage review limits.
- Duty cycle: ≤ 10% per 30‑minute window; max 2 windows/day; cooldown ≥ 2 hours.

## Procedure (Condensed)
1. Permissions & Briefing: Approvals from custodians; safety briefing; equipment inventory.
2. Baselines: 30–60 minutes of passive measurement; record environmental context.
3. Calibration: Instrument checks; time sync; cross‑sensor alignment.
4. Micro‑Stimulation: Apply stepwise envelope; log exact parameters; live thresholds/alarms.
5. Cooldown & Post‑Baseline: Verify return to baseline; capture post conditions.
6. Data Packaging: Store as site_id/session_id; export JSON + binary traces with checksums.

## Abort Conditions
- Any sensor exceeds predefined excursion bands.
- Unexpected coupling (e.g., EM spikes beyond cap) or community concerns.
- Weather or environmental instability.

## Data Schema (Minimal JSON)
```json
{
  "site_id": "giza_gp_01",
  "session_id": "2025-09-14T12:00:00Z",
  "baselines": {
    "em_hz_0_1000_rms": 0.0021,
    "magnetic_pt": 2.3,
    "acoustic_db": 38.2,
    "temperature_c": 31.4,
    "humidity_pct": 22.0
  },
  "stimulation": {
    "freq_hz": 7.83,
    "amplitude_units": "V/m",
    "amplitude_value": 0.25,
    "duty_cycle_pct": 10,
    "duration_s": 300
  },
  "responses": {
    "em_peak": 0.0035,
    "magnetic_peak_pt": 3.1,
    "acoustic_peak_db": 41.0
  },
  "notes": "No excursions; clean cooldown; local conditions stable.",
  "hash": "sha256:..."
}
```

## Roles & Oversight
- Field Lead, Instrumentation Lead, Independent Safety Officer, Heritage Liaison, Data Steward.

## Dissemination
- Pre‑registration of sessions, anonymized data release, methods and calibration notes, safety audit summaries.

