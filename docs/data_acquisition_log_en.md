# Data acquisition and preparation log

Русская версия: [data_acquisition_log.md](data_acquisition_log.md).

## 28 September 2026 — collection, extraction and quality control

### Purpose

To establish a reproducible evidence base for RQ1–RQ4: preserve original sources, document transformations, extract IPPU emissions and activity data, and test whether published production statistics and inventory activity data have matching definitions.

### Original files acquired

| ID | File | Source and coverage | SHA-256 | Status |
|---|---|---|---|---|
| BNS-01 | `data/raw/bns/bns_industrial_production_1990_2025.xlsx` | BNS industrial production, 1990–2025 | `89bdb3cfa1125cace2b2655e66008c7b0b4d38be14e9dc4c3c9f92dd06fb9852` | acquired, unchanged |
| BNS-02 | `data/raw/bns/bns_physical_production_2021.xlsx` | BNS physical output, annual 2021 | `82240dc60edc5a2ad5abbd08d3a28972784f7b59868f840f2846e8e9f32d4e35` | acquired, unchanged |
| BNS-03 | `data/raw/bns/bns_physical_production_2023.xlsx` | BNS physical output, Jan–Dec 2023 | `d3c9dc32e146feba663a0a5c52ac5635671043dd2373626f6d4439540db6717c` | acquired, unchanged |
| CRT-25 | `data/raw/unfccc_crt_2025/KAZ-CRT-2025-V1.0-20250415-143602_awaiting%20submission.zip` | UNFCCC CRT, 1990–2023 | `ae47103e4f444def2aa9a44132a222747a2d9e465c85c23318656e4ef32372f0` | acquired and extracted |
| CRF-23 | `data/raw/unfccc_crf_2023/kaz-2023-crf-15apr23_AR4 (1).zip` | UNFCCC CRF, 1990–2021 | `71f757d1dd24d4abbfabd8ea77f09762d2eaf1e6e1354c754ef6beebdd94ec75` | acquired and extracted |
| NIR-23 | `data/raw/unfccc_reports/kaz-2023-nir-15apr23.zip` | Kazakhstan NIR 2023 | `fd31b08519d870b66cde5366b079fe6fc9e2cd7675aeb16bd6944ba886f05e15` | acquired; priority IPPU method sections reviewed |
| NID-25 | `data/raw/unfccc_reports/NID RK 2025 (2).pdf` | Kazakhstan NID 2025, 1990–2023 | `736fefc315f7565e82c10cab5cee82a63a3bda67d95c3d351dc09dcf40dceecc` | acquired; priority IPPU method sections reviewed |

### Derived datasets

| File | Contents | Interpretation status |
|---|---|---|
| `data/processed/unfccc_ippu_emissions_1990_2023.csv` | 2,534 reported IPPU-emission records | ready for historical analysis |
| `data/processed/unfccc_ippu_activity_data_1990_2023.csv` | 572 reported activity-data records | ready, subject to process-boundary checks |
| `data/processed/crf_2023_vs_crt_2025_ippu_comparison_1990_2021.csv` | 800 matched CRF–CRT observations | ready; GWP framework noted |
| `data/processed/bns_ippu_activity_data_1990_2023.csv` | 136 BNS observations | product-to-IPCC matching incomplete |
| `data/processed/bns_ippu_activity_data_2021_annual.csv` | 21 candidate products, 2021 | ready for controlled comparison |
| `data/processed/bns_ippu_activity_data_2023_annual.csv` | 21 candidate products, 2023 | ready for controlled comparison |
| `data/processed/bns_vs_crt_2025_activity_comparison_2021.csv` | seven screened 2021 comparisons | interpretation recorded below |
| `data/processed/leap_ippu_scenario_results_2024_2050.csv` | annual corrected LEAP scenario results | ready for article use within the stated boundary |

Original files were not edited. Extraction scripts read XLSX files and write separate CSV outputs, retaining product labels, units, values and BNS notation.

### Key quality-control findings

1. The initial 2021 BNS extractor used a fixed column. It was corrected to locate the uniquely labelled `2021` column; figures based on the earlier column must not be used.
2. CRT total IPPU emissions are 22,741.283 kt CO2eq in 1990, 12,257.786 in 1996 and 26,772.704 in 2023. In overlapping years, CRF and CRT total values differ by −0.118% (2020) and −1.958% (2021). An approximately 10% rise in CRT values is therefore unsupported.
3. CRF 2023 uses AR4 and CRT 2025 uses AR5 GWP values. CO2eq differences cannot be treated as inventory revision alone.
4. The apparent 41% cement difference compares BNS Portland cement with CRT clinker. NID 2025 confirms BNS clinker of 7,295.7 kt in 2021, equal to CRT activity data.
5. The apparent 72.8% zinc difference is a boundary mismatch: CRT 2.C.6 covers zinc from Waelz cakes in Waelz kilns (81.861 kt in 2021); BNS reports total raw zinc output (300.886 kt). These figures are not directly comparable.

### Interpretation rule and remaining work

Differences must first be classified as a unit, product-definition, process-boundary or methodology issue. Only residual differences between genuinely comparable measures may be discussed as possible activity-data inconsistency.

Core collection and priority NID/NIR method review are complete. The remaining non-blocking enrichment tasks are longer BNS series for clinker and steel, disaggregated primary-aluminium data, and optional public corroboration of the Kazzinc Waelz stream. They are listed in [Remaining data collection](data_collection_remaining_en.md).

## 3 October 2026 — corrected LEAP calculation

The user provided `Kazakhstan_IPPU_LEAP_results_corrected.xlsx`, exported from LEAP 2026.5.0.1 for the `Kazakhstan IPPU Decarbonization` area. The unmodified file is retained under `data/raw/leap/` (SHA-256 `fd0e4648c9272366d164a2e2de1f45b2d5f529e4930db4eb484f78a58e62c299`) and registered in the source registry.

The export confirms Current Accounts 2024, end year 2050, the `Non Energy Effect Loading` variable, linear `Interp()` expressions and AR5 100-year GWPs. Before the rerun, two non-CO2 units were corrected: ferroalloy CH4, 36.894 t rather than 36,894 t; and nitric-acid N2O, 592.4 t rather than 592,400 t. The resulting CO2eq totals are 23,551.9 kt for Baseline in 2030 and 2050; 20,714.9 and 14,826.9 kt for Moderate; and 17,156.6 and 7,735.8 kt for Ambitious. The full table and figures are in the [scenario protocol](leap_scenarios_2023_2050_en.md).
