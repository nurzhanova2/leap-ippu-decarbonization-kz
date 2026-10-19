<div align="center">

# LEAP-Based modeling of Decarbonization pathways in the IPPU sector of Kazakhstan

### Historical evidence, exploratory LEAP pathways and reproducible research materials

**Language:** [Русский](README_ru.md) · [English](README.md)

[![Status — journal manuscript drafted](https://img.shields.io/badge/status-journal%20manuscript%20drafted-2e7d32)](docs/manuscript_full_en.md)
[![Coverage — Kazakhstan, 1990–2024](https://img.shields.io/badge/coverage-Kazakhstan%2C%201990–2024-1565c0)](docs/manuscript_full_en.md)
[![Sector — IPCC 2 IPPU](https://img.shields.io/badge/sector-IPCC%202%20IPPU-6a1b9a)](data/metadata/bns_ippu_category_crosswalk.csv)
[![LEAP — expressions verified](https://img.shields.io/badge/LEAP-expressions%20verified-2e7d32)](docs/leap_scenarios_2023_2050_en.md)

</div>

> [!IMPORTANT]
> **Journal version.** The analysis uses Kazakhstan's 2026 inventory submission (CRT 2026, 1990–2024) and a LEAP model with a 2024 base of 22,088 kt CO2eq (85.6% of IPPU emissions in 2024). The full manuscript draft is available in English and Russian: [manuscript_full_en.md](docs/manuscript_full_en.md) · [manuscript_full_ru.md](docs/manuscript_full_ru.md). The conference version on CRT 2025 is kept unchanged as an archive (see [below](#archived-conference-version-crt-2025)). Results are reported only for the explicitly defined process-emissions boundary.

## Why this project

Emissions from *Industrial Processes and Product Use* (IPPU) are a material, but not always directly comparable, component of Kazakhstan’s national greenhouse-gas inventory. This project brings together official UNFCCC submissions and BNS production statistics to:

```text
collect sources → extract series → verify definitions → compare data → set 2024 base year → test exploratory pathways
```

The project separates verified historical evidence from scenario assumptions. It reports a transparent selected process-emissions boundary, not a forecast for the entire national IPPU sector.

## What is ready (journal version)

| Component | Coverage | Status |
|---|---|---|
| Historical IPPU emissions | CRT 2026, 1990–2024 | complete |
| Recalculations between submissions | CRT 2025 and CRT 2026, 1990–2023 | complete |
| Activity-data comparability | clinker, lime, iron and steel, ferroalloys, aluminium, zinc | complete |
| LEAP scenarios, 2024–2050 | Baseline, Moderate, Ambitious on the CRT 2026 inventory 2024 base | computed with LEAP Interp() expressions |
| LEAP import workbook | CRT 2026 Current Accounts and scenario expressions | expressions, units and AR5 totals verified |
| Literature-based factors | low, central and high factors by process | complete |
| Activity growth and sensitivity | five growth variants, one-at-a-time analysis | complete |
| References | 46 entries with DOI where available | checked against Crossref and source PDFs |
| Full manuscript | abstract, sections 1–5, 11 tables, 7 figures | draft, English and Russian |

## Core methodological rule

> [!WARNING]
> A numerical difference does not by itself demonstrate poor data quality. Units, product definitions, process boundaries and inventory methodology must be checked first.

For example, Portland-cement output cannot be directly compared with clinker activity data, and total BNS raw-zinc output cannot be directly compared with the narrow Waelz-process zinc flow reported in CRT. These cases are documented in the [NID/NIR review](docs/process_methodology_review_en.md).

## Quick start

### 1. Navigate the project

| To… | Read |
|---|---|
| read the journal manuscript | [full manuscript](docs/manuscript_full_en.md) |
| check the references | [BibTeX library](docs/references.bib) and [check log](data/metadata/references_check.csv) |
| understand the research questions and contribution | [research design](research_design_en.md) |
| verify data provenance and hashes | [acquisition log](docs/data_acquisition_log_en.md) |
| verify process boundaries, activity data and recalculations | [NID/NIR review](docs/process_methodology_review_en.md) |
| review the literature | [literature review](docs/literature_review_en.md) |
| review scenario assumptions, results, sensitivity and limits | [scenario protocol](docs/leap_scenarios_2023_2050_en.md) |
| review the literature basis of the scenario factors | [scenario rationale](docs/scenario_rationale_en.md) |
| import or verify the model in LEAP | [LEAP exchange files](outputs/README.md) |
| locate all documents | [documentation index](docs/README_en.md) |
| understand the data layout | [data registry](data/README_en.md) |

### 2. Reproduce the journal version

Raw files are kept in `data/raw/`; derived CSV files are kept in `data/processed/`. Scripts read the originals and write outputs separately; they do not modify files in `data/raw/`.

```bash
python scripts/extract_ippu_emissions.py --inventory crt2026
python scripts/extract_ippu_activity_data.py --inventory crt2026
python scripts/extract_crt_subcategory_emissions.py --inventory crt2025
python scripts/extract_crt_subcategory_emissions.py --inventory crt2026
python scripts/extract_crt_2a4_subcategories.py --inventory crt2026
python scripts/compare_unfccc_versions.py --pair crt2025_crt2026
python scripts/analyze_ippu_timeseries.py --inventory crt2026
python scripts/build_leap_parameters.py --inventory crt2026
python scripts/fill_leap_import_template.py outputs/leap_ippu_import/Kazakhstan_IPPU_LEAP_final_import.xlsx outputs/leap_ippu_import/Kazakhstan_IPPU_LEAP_import_crt2026.xlsx --parameters data/metadata/leap_scenario_parameters_crt2026.csv
python scripts/analyze_leap_scenarios.py --inventory crt2026
python scripts/analyze_leap_sensitivity.py
```

The outputs carry the suffix `_crt2026`. Without `--inventory`, the scripts reproduce the archived conference version.

## Structure

```text
.
├── data/
│   ├── raw/          # immutable primary files (local only)
│   ├── processed/    # reproducible CSV extractions, comparisons and scenario results
│   └── metadata/     # source registry, parameters, literature factors and crosswalk
├── docs/              # bilingual documentation, manuscript and references.bib
├── figures/            # Figures 1–7 and index
├── outputs/            # LEAP import workbooks
├── scripts/           # extraction, comparison, scenarios and quality control
├── research_design_ru.md
└── research_design_en.md
```

## Sources

- UNFCCC: Kazakhstan CRT 2026 and NID 2026 (journal version); CRT 2025, CRF 2023, NID 2025 and NIR 2023 (comparison and archive);
- Bureau of National Statistics of the Republic of Kazakhstan (BNS);
- IPCC 2006 Guidelines and 2019 Refinement, Volume 3 (IPPU); IPCC AR5 GWP100;
- published pathways for the scenario factors (IEA, IPCC AR6, EU BREF, industry roadmaps, Kazakhstan studies), listed in [references.bib](docs/references.bib).

The complete source register, coverage and limitations are available in [metadata](data/metadata/README_en.md).

## Journal version: main scenarios (CRT 2026)

| Scenario | 2030, kt CO2eq | 2050, kt CO2eq |
|---|---:|---:|
| Baseline | 22,088 | 22,088 |
| Moderate mitigation | 19,418 | 13,896 |
| Ambitious mitigation | 16,072 | 7,236 |

The base is the CRT 2026 inventory 2024 base: 22,088 kt CO2eq, 85.6% of IPPU emissions in 2024. The values exclude F-gases, aluminium PFCs, several minor IPPU sources and industrial-combustion emissions. The literature-based factors, the activity-growth variants and the sensitivity analysis are reported in the [manuscript](docs/manuscript_full_en.md) and the [scenario protocol](docs/leap_scenarios_2023_2050_en.md#journal-version-crt-2026-inventory-2024-base).

## Archived conference version (CRT 2025)

The conference version used CRT 2025 (1990–2023) and the CRT 2025 values for 2023 as a proxy for 2024. Its CSV files, Figures 1–5 and texts are kept unchanged.

| Scenario | 2030, kt CO2eq | 2050, kt CO2eq |
|---|---:|---:|
| Baseline | 23,552 | 23,552 |
| Moderate mitigation | 20,715 | 14,827 |
| Ambitious mitigation | 17,157 | 7,736 |

Materials: [conference Results and Discussion draft](docs/manuscript_historical_results_discussion_en.md) · [scenario protocol, conference sections](docs/leap_scenarios_2023_2050_en.md) · [conference abstract](docs/abstract_draft_en.md) · [IAMC speaker script and Q&A](docs/presentation_speaker_script_en.md) · [Google Slides presentation](https://docs.google.com/presentation/d/1MO3Ly5cWBq1vKcamaa5fa2bCgeq9VQpp85bNB47nBWk/edit?usp=sharing) · [article analysis](docs/article_analysis_en.md) · [preliminary results](docs/preliminary_results_en.md).

## Remaining work before submission

1. Choose the target journal and convert the reference list from APA 7 to its style.
2. Clarify the activity data of category 2.A.4.d and its possible overlap with lime production with the inventory compilers.
3. Perform a final scientific and editorial audit: author details, figure formats and submission requirements.
4. Optionally, import the CRT 2026 workbook into desktop LEAP and compare the results with the reproduced values.

## Use status

The materials support a research article and future model development. When using a figure, cite the primary UNFCCC/BNS source and retain the submission year, units and GWP framework recorded in the table.
