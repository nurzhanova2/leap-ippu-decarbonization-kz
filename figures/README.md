# Figures

Русская версия: [README_ru.md](README_ru.md).

| Figure | Description | Reproducible source |
|---|---|---|
| `figure_1_ippu_total_emissions_1990_2023.png` | Total historical IPPU emissions | Historical extraction scripts and CRT 2025 |
| `figure_2_ippu_category_composition_1990_2023.png` | Historical category composition | Historical extraction scripts and CRT 2025 |
| `figure_3_crf_2023_vs_crt_2025_total_ippu_comparison.png` | CRF–CRT comparison | Version-comparison script |
| `figure_4_leap_ippu_scenario_pathways_2024_2050.png` | LEAP scenario pathways | `scripts/analyze_leap_scenarios.py` |
| `figure_5_leap_ippu_avoided_emissions_2024_2050.png` | Avoided emissions by process group | `scripts/analyze_leap_scenarios.py` |
| `figure_4_leap_ippu_scenario_pathways_2024_2050_crt2026.png` | Journal version: main scenarios on the CRT 2026 inventory 2024 base | `scripts/analyze_leap_scenarios.py --inventory crt2026` |
| `figure_5_leap_ippu_avoided_emissions_2024_2050_crt2026.png` | Journal version: avoided emissions by process group | `scripts/analyze_leap_scenarios.py --inventory crt2026` |
| `figure_6_leap_ippu_growth_sensitivity_2024_2050_crt2026.png` | Journal version: activity growth with presented and literature-based factors | `scripts/analyze_leap_sensitivity.py` |
| `figure_7_leap_ippu_tornado_2050_crt2026.png` | Journal version: effect of one assumption at a time in 2050 | `scripts/analyze_leap_sensitivity.py` |
| `figure_1_ippu_total_emissions_1990_2024_crt2026.png` | Journal version (CRT 2026): total historical IPPU emissions | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |
| `figure_2_ippu_category_composition_1990_2024_crt2026.png` | Journal version (CRT 2026): category composition | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |
| `figure_3_crt_2025_vs_crt_2026_total_ippu_comparison_crt2026.png` | Journal version: recalculation between CRT 2025 and CRT 2026 | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |

Figures 1–5 without a suffix belong to the archived conference version (CRT 2025). Figures 4–7 cover only the explicit process-emissions boundary described in [the scenario protocol](../docs/leap_scenarios_2023_2050_en.md); they are not national-total IPPU projections.
