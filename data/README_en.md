# Input-data registry

Русская версия: [README.md](README.md).

The folder structure supports reproducible work. Raw source files are retained unchanged and processed derivatives are kept separately.

```text
data/
├── raw/           # unchanged primary-source files
├── processed/     # cleaned and harmonised derivatives
├── metadata/      # registries, crosswalks, and transformation logs
└── README.md
```

## Harmonisation rules

- Preserve both the original and converted values.
- Do not replace `NE`, `NO`, `NA`, `IE`, or confidential entries with zero.
- Keep source units in metadata; standardise mass to tonnes and emissions to kt CO2eq only in derivative fields.
- Compare only matching products and boundaries: cement is not clinker.
- Record source table, sheet, cell or page for every manually extracted observation.

## Status, 28 September 2026

Unchanged BNS, CRT 2025, CRF 2023, NID 2025, and NIR 2023 sources are retained under `raw/`. Literature and official documents used for the scenario factors, the AR5 GWP values and the policy context (decision 18/CMA.1, the 2023 NDC, the 2060 Strategy) are under `raw/literature/` and `raw/official/`; their URLs and SHA-256 are in [source_registry.csv](metadata/source_registry.csv). IPPU emissions and activity data from CRT/CRF, 2021 BNS–CRT checks, the 1990–2023 historical series and category-composition tables have been extracted. Priority IPPU methodology sections in NID/NIR are reviewed; process boundaries and comparability status are in the [methodology review](../docs/process_methodology_review_en.md), and results and figure locations are in the [article analysis](../docs/article_analysis_en.md).

`processed/leap_ippu_scenario_results_2024_2050.csv` contains the full annual results for the selected LEAP process-emissions boundary. It reproduces the corrected 2024–2050 LEAP scenario expressions; the scenario definitions and exclusions are documented in the [scenario protocol](../docs/leap_scenarios_2023_2050_en.md).

`processed/crt_2025_2a4_subcategories_1990_2023.csv` contains the CRT 2025 breakdown of category 2.A.4 (ceramics, other uses of soda ash, non-metallurgical magnesia, use of limestone and dolomite) for 1990–2023, including the 2.A.4.d activity data that the general activity-data extraction skips. The `row_level` column separates category, subcategory and item rows; sum only the subcategory rows. It is created by `scripts/extract_crt_2a4_subcategories.py`; the interpretation is in the [NID/NIR review](../docs/process_methodology_review_en.md).

`processed/leap_ippu_scenario_results_2024_2050_crt2026.csv` contains the main journal scenarios on the CRT 2026 inventory 2024 base. `leap_ippu_sensitivity_*_crt2026.csv` contain the activity-growth and factor sensitivity runs, `bns_index_2024_check_crt2026.csv` compares the BNS 2024 indices with CRT 2026. They are created by `scripts/analyze_leap_scenarios.py --inventory crt2026` and `scripts/analyze_leap_sensitivity.py`; see the [journal version](../docs/leap_scenarios_2023_2050_en.md#journal-version-crt-2026-inventory-2024-base).

**Inventory versions.** Files without a suffix belong to the archived conference version (CRT 2025, 1990–2023). Files with the suffix `_crt2026` belong to the journal version (CRT 2026, 1990–2024). They are created by the same scripts with `--inventory crt2026` (see `scripts/inventory_versions.py`): emissions, activity data, 2.A.4 subcategories, subcategory emissions, historical summary and category shares. `crt_2025_vs_crt_2026_ippu_comparison_1990_2023_crt2026.csv` compares the two submissions by category (`scripts/compare_unfccc_versions.py --pair crt2025_crt2026`).
