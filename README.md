<div align="center">

# LEAP-Based modeling of Decarbonization pathways in the IPPU sector of Kazakhstan

### Historical evidence, exploratory LEAP pathways and reproducible research materials

**Language:** [Русский](README_ru.md) · [English](README.md)

[![Status — article evidence package ready](https://img.shields.io/badge/status-article%20evidence%20package%20ready-2e7d32)](docs/article_writing_status_en.md)
[![Coverage — Kazakhstan, 1990–2023](https://img.shields.io/badge/coverage-Kazakhstan%2C%201990–2023-1565c0)](research_design_en.md)
[![Sector — IPCC 2 IPPU](https://img.shields.io/badge/sector-IPCC%202%20IPPU-6a1b9a)](data/metadata/bns_ippu_category_crosswalk.csv)
[![LEAP — results verified](https://img.shields.io/badge/LEAP-results%20verified-2e7d32)](docs/leap_scenarios_2023_2050_en.md)

</div>

> [!IMPORTANT]
> Historical analysis, a corrected 2024-calibrated LEAP implementation, an import workbook, verified AR5 CO2eq results, scenario rationale and conference presentation are available. Results are reported only for the explicitly defined process-emissions boundary.

## Why this project

Emissions from *Industrial Processes and Product Use* (IPPU) are a material, but not always directly comparable, component of Kazakhstan’s national greenhouse-gas inventory. This project brings together official UNFCCC submissions and BNS production statistics to:

```text
collect sources → extract series → verify definitions → compare data → calibrate 2024 → test exploratory pathways
```

The project separates verified historical evidence from scenario assumptions. It reports a transparent selected process-emissions boundary, not a forecast for the entire national IPPU sector.

## What is ready

| Component | Coverage | Status |
|---|---|---|
| Historical IPPU emissions | CRT 2025, 1990–2023 | complete |
| Inventory-version comparison | CRF 2023 and CRT 2025, 1990–2021 | complete |
| UNFCCC activity data | CRT 2025 | extracted |
| Production data | available BNS long and annual series | extracted and documented |
| Comparability assessment | clinker, lime, iron/steel, ferroalloys, aluminium, zinc | NID/NIR methodology review complete |
| Article figures and tables | trend, composition, CRF–CRT, activity-data cases, scenarios | ready |
| LEAP scenario pathways, 2024–2050 | Baseline, Moderate, Ambitious | calculated and CO2eq-verified |
| LEAP exchange workbook | Current Accounts and scenario expressions | imported, run and export-verified |
| Scenario rationale | measure portfolios and claims boundary | complete |
| Conference presentation | scientific conference deck | available in Google Slides |

## Core methodological rule

> [!WARNING]
> A numerical difference does not by itself demonstrate poor data quality. Units, product definitions, process boundaries and inventory methodology must be checked first.

For example, Portland-cement output cannot be directly compared with clinker activity data, and total BNS raw-zinc output cannot be directly compared with the narrow Waelz-process zinc flow reported in CRT. These cases are documented in the [preliminary results](docs/preliminary_results_en.md).

## Quick start

### 1. Navigate the project

| To… | Read |
|---|---|
| understand the research questions and contribution | [research design](research_design_en.md) |
| verify data provenance and hashes | [acquisition log](docs/data_acquisition_log_en.md) |
| review validated findings | [preliminary results](docs/preliminary_results_en.md) |
| access figures and Results wording | [article analysis](docs/article_analysis_en.md) |
| verify process boundaries and activity data | [NID/NIR review](docs/process_methodology_review_en.md) |
| substantiate the research gap and draft the Introduction | [literature review](docs/literature_review_en.md) |
| see the manuscript’s current completion status | [manuscript-writing status](docs/article_writing_status_en.md) |
| review scenario assumptions, results and limits | [scenario protocol](docs/leap_scenarios_2023_2050_en.md) |
| review measure narratives and the evidence boundary for scenario factors | [scenario rationale](docs/scenario_rationale_en.md) |
| view the conference presentation | [Google Slides presentation](https://docs.google.com/presentation/d/1MO3Ly5cWBq1vKcamaa5fa2bCgeq9VQpp85bNB47nBWk/edit?usp=sharing) |
| import or verify the model in LEAP | [LEAP exchange files](outputs/README.md) |
| use the revised abstract | [English conference draft](docs/abstract_draft_en.md) |
| locate all documents | [documentation index](docs/README_en.md) |
| understand the data layout | [data registry](data/README_en.md) |

### 2. Reproduce processed tables

Raw files are kept in `data/raw/`; derived CSV files are kept in `data/processed/`. Scripts read the originals and write outputs separately.

```bash
python scripts/extract_ippu_emissions.py
python scripts/extract_ippu_activity_data.py
python scripts/compare_unfccc_versions.py
python scripts/compare_bns_unfccc_2021.py
python scripts/analyze_leap_scenarios.py
```

Review arguments and paths before running: the scripts assume this repository layout and do not modify files in `data/raw/`.

## Structure

```text
.
├── data/
│   ├── raw/          # immutable primary files
│   ├── processed/    # reproducible CSV extractions and comparisons
│   └── metadata/     # source registry, templates and crosswalk
├── docs/              # bilingual methodological documentation
├── figures/            # publication figures and index
├── outputs/            # LEAP import workbook
├── scripts/           # extraction, comparison and quality control
├── research_design_ru.md
└── research_design_en.md
```

## Sources

- UNFCCC: Kazakhstan CRT 2025, CRF 2023, NID 2025 and NIR 2023;
- Bureau of National Statistics of the Republic of Kazakhstan (BNS);
- IPCC 2006 Guidelines and 2019 Refinement, Volume 3 (IPPU).

The complete source register, coverage and limitations are available in [metadata](data/metadata/README_en.md).

## Exploratory scenario results

| Scenario | 2030, kt CO2eq | 2050, kt CO2eq |
|---|---:|---:|
| Baseline | 23,552 | 23,552 |
| Moderate mitigation | 20,715 | 14,827 |
| Ambitious mitigation | 17,157 | 7,736 |

The figures and complete data table are available in the [scenario protocol](docs/leap_scenarios_2023_2050_en.md). They exclude F-gases, aluminium PFCs, several minor IPPU sources and industrial-combustion emissions.

## Remaining work before submission

1. Assemble the complete manuscript: Introduction, Methods, Results, Discussion and Conclusion, using the existing bilingual drafts and the documented scenario boundary.
2. Add and standardise in-text citations and the final reference list in the target conference or journal style.
3. Perform a final scientific and editorial audit: units, AR5 GWPs, figures, tables, claims, author details and submission format.
4. Add further sensitivity cases only if new evidence supports alternative activity-data or technology assumptions.

Details: [remaining data tasks](docs/data_collection_remaining_en.md).

## Use status

The materials support a research article and future model development. When using a figure, cite the primary UNFCCC/BNS source and retain the submission year, units and GWP framework recorded in the table.
