<div align="center">

# IPPU Kazakhstan · 1990–2023

### Data, historical trends and preparation for LEAP-based decarbonisation modelling

**Language:** [Русский](README_ru.md) · [English](README.md)

[![Status — core collection complete](https://img.shields.io/badge/status-core%20collection%20complete-2e7d32)](docs/data_acquisition_log_en.md)
[![Coverage — Kazakhstan, 1990–2023](https://img.shields.io/badge/coverage-Kazakhstan%2C%201990–2023-1565c0)](research_design_en.md)
[![Sector — IPCC 2 IPPU](https://img.shields.io/badge/sector-IPCC%202%20IPPU-6a1b9a)](data/metadata/bns_ippu_category_crosswalk.csv)
[![LEAP — next stage](https://img.shields.io/badge/LEAP-next%20stage-f57c00)](research_design_en.md)

</div>

> [!IMPORTANT]
> The project is at the historical-analysis and input-data quality-control stage. LEAP decarbonisation scenarios have not yet been built; this repository provides the transparent foundation for their future development.

## Why this project

Emissions from *Industrial Processes and Product Use* (IPPU) are a material, but not always directly comparable, component of Kazakhstan’s national greenhouse-gas inventory. This project brings together official UNFCCC submissions and BNS production statistics to:

```text
collect sources → extract series → verify definitions → compare data → prepare LEAP inputs
```

At this stage, the output is a reproducible dataset and quality-assurance protocol. It does not substitute for the future LEAP model or present scenario projections as completed results.

## What is ready

| Component | Coverage | Status |
|---|---|---|
| Historical IPPU emissions | CRT 2025, 1990–2023 | complete |
| Inventory-version comparison | CRF 2023 and CRT 2025, 1990–2021 | complete |
| UNFCCC activity data | CRT 2025 | extracted |
| Production data | available BNS long and annual series | extracted and documented |
| Comparability assessment | clinker, lime, iron/steel, ferroalloys, aluminium, zinc | NID/NIR methodology review complete |
| Article figures and tables | trend, composition, CRF–CRT | ready for article drafting |
| LEAP model and scenarios | 2030/2050 | subsequent work |

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
├── scripts/           # extraction, comparison and quality control
├── research_design_ru.md
└── research_design_en.md
```

## Sources

- UNFCCC: Kazakhstan CRT 2025, CRF 2023, NID 2025 and NIR 2023;
- Bureau of National Statistics of the Republic of Kazakhstan (BNS);
- IPCC 2006 Guidelines and 2019 Refinement, Volume 3 (IPPU).

The complete source register, coverage and limitations are available in [metadata](data/metadata/README_en.md).

## Next stage

1. Draft the Methods, Results and Discussion sections using the prepared figures, tables and methodology review.
2. Verify citations, units, GWPs and indicator definitions before submission.
3. If needed, extend BNS clinker/steel series and obtain disaggregated primary-aluminium data.
4. Use harmonised data for a LEAP model as separate subsequent work.

Details: [remaining data tasks](docs/data_collection_remaining_en.md).

## Use status

The materials support a research article and future model development. When using a figure, cite the primary UNFCCC/BNS source and retain the submission year, units and GWP framework recorded in the table.
