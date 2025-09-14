# Infrared UCNP Benchmarks — Demo Results (2025)

Status: Active Development — simulated environment using numpy-based demos.

## Purpose
Summarize simulated capabilities and target metrics from the infrared nanoparticle integration demos for internal planning and documentation.

## Modules
- `infrared_nanoparticle_integration.py` — UCNP/quartz display models, detection flow, reports.
- `glasssphere_os.py` — neuro-interface layer, touch input processing, brainwave signals.
- `glasssphere_ui_shell.py` — IR overlays, night vision/aura modes, rendering path.

## Target Metrics (Simulation)
- Bands: NIR, SWIR, MWIR, LWIR (0.75–15 μm) — sampled signals per band.
- Upconversion efficiency: 0.85–0.95 (spec-driven in NanoparticleSpecs).
- Thermal map: Random field with spatial gradients; 2D array sized to display resolution.
- Biofield/aura: Synthetic patterns; strictly demo‑only.
- Latency: Per‑frame operations are vectorized; small test frames render in milliseconds.

## Reproduce Locally
```bash
# Minimal dependencies
pip install -r requirements-min.txt

# Run full demo
python glasssphere_infrared_demo.py

# Or import and run a minimal detection pass
python - << 'PY'
from infrared_nanoparticle_integration import InfraredNanoparticleIntegration, DisplayType
import asyncio

async def main():
    ir = InfraredNanoparticleIntegration()
    ir.create_display_system("Bench_01", DisplayType.CRYSTAL_TABLET, "advanced_ucnp", "enhanced_quartz", (320,200), 60.0)
    data = await ir.detect_infrared_signals("Bench_01", 0.5)
    print("bands:", len(data.infrared_bands), "thermal:", data.thermal_map.shape)

asyncio.run(main())
PY
```

## Notes & Caveats
- These are simulation numbers, not hardware benchmarks.
- Any real‑world claims require lab instrumentation and independent verification.
- Keep test frames modest to ensure CI/tier‑1 devices render quickly.

