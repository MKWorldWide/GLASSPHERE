# Crystal Resonance Data Schema (2025)

Status: Active Development

## Relational Core
```sql
CREATE TABLE sites (
  site_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  country TEXT,
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  notes TEXT
);

CREATE TABLE baselines (
  baseline_id TEXT PRIMARY KEY,
  site_id TEXT REFERENCES sites(site_id),
  timestamp TIMESTAMP NOT NULL,
  em_rms_0_1000_hz DOUBLE PRECISION,
  magnetic_pt DOUBLE PRECISION,
  acoustic_db DOUBLE PRECISION,
  temperature_c DOUBLE PRECISION,
  humidity_pct DOUBLE PRECISION
);

CREATE TABLE stim_sessions (
  session_id TEXT PRIMARY KEY,
  site_id TEXT REFERENCES sites(site_id),
  timestamp TIMESTAMP NOT NULL,
  freq_hz DOUBLE PRECISION,
  amplitude_value DOUBLE PRECISION,
  amplitude_units TEXT,
  duty_cycle_pct DOUBLE PRECISION,
  duration_s DOUBLE PRECISION,
  safety_officer TEXT
);

CREATE TABLE responses (
  response_id TEXT PRIMARY KEY,
  session_id TEXT REFERENCES stim_sessions(session_id),
  em_peak DOUBLE PRECISION,
  magnetic_peak_pt DOUBLE PRECISION,
  acoustic_peak_db DOUBLE PRECISION,
  notes TEXT
);
```

## Minimal JSON Record
```json
{
  "site_id": "giza_gp_01",
  "baseline": {"em_rms_0_1000_hz": 0.0021, "magnetic_pt": 2.3},
  "stimulation": {"freq_hz": 7.83, "amplitude_value": 0.25, "units": "V/m"},
  "response": {"em_peak": 0.0035, "magnetic_peak_pt": 3.1},
  "checksum": "sha256:..."
}
```

## Notes
- Mirrors the schema outlined in `ARCHITECTURE.md` with PNAP‑specific fields.
- Prefer normalized storage with separate raw trace files (referenced by checksums).

