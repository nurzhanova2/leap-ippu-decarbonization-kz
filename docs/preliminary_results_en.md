# Preliminary reproducible results

Русская версия: [preliminary_results.md](preliminary_results.md).

**Status:** Results are extracted from primary CRT/CRF and BNS sources. NID Chapter 4 has been checked for cement and zinc; full NIR 2023 method review remains.

## CRT 2025 historical series

CRT 2025 Table 2(I), using AR5 GWP values, reports total IPPU emissions of 22,741.283 kt CO2eq in 1990, 12,257.786 kt in 1996, 26,999.456 kt in 2020, 26,553.652 kt in 2021, and 26,772.704 kt in 2023.

## CRF 2023 and CRT 2025

CRF 2023 total CO2eq values were recalculated from component columns using AR4 GWPs, whereas CRT 2025 reports total CO2eq directly under AR5. The comparison is therefore not a pure inventory-revision measure.

| Year | CRF 2023, kt CO2eq (AR4) | CRT 2025, kt CO2eq (AR5) | CRT-CRF | CO2 difference |
|---:|---:|---:|---:|---:|
| 2020 | 27,031.370 | 26,999.456 | -0.118% | +0.872% |
| 2021 | 27,083.916 | 26,553.652 | -1.958% | -1.231% |

The claim that CRT 2025 is around 10% higher than CRF 2023 in 2020-2021 is not supported by the supplied primary files.

## 2021 BNS-CRT activity-data checks

| BNS indicator | CRT indicator | CRT-BNS | Interpretation |
|---|---|---:|---|
| Clinker, 7.2957 Mt | Clinker production, 7.2957 Mt | 0.0% | directly comparable |
| Portland cement, 12.3127 Mt | Clinker production, 7.2957 Mt | -40.747% | not directly comparable: cement is not clinker |
| Lime, 0.933623 Mt | Lime produced, 0.933623 Mt | 0.0% | directly comparable as a national aggregate; product mix is modelled separately |
| Ferroalloys, 2.070038 Mt | Ferroalloys production, 2.070038 Mt | 0.0% | directly comparable as total output; plant data are needed for EF calculation |
| Unwrought zinc, 0.300886 Mt | Zinc production, 0.081861 Mt | -72.793% | not directly comparable: national total versus a narrow technological stream |

## What NID 2025 explains

- Cement emissions use BNS **clinker** production (7,295.7 kt in 2021) and IPCC 2006 Tier 2. The 40.747% result arises only when this is incorrectly compared with BNS Portland cement output.
- Zinc activity data of 81.86 kt refer to zinc produced from Waelz cakes in Waelz kilns, reported directly by Kazzinc. The BNS 300.88 kt value is total national zinc production.

Accordingly, neither apparent difference is evidence by itself of poor statistics. They demonstrate the risk of comparing activity data with different product definitions and process boundaries.

## Derivative datasets

- `data/processed/unfccc_ippu_emissions_1990_2023.csv` - 2,534 category-year records;
- `data/processed/unfccc_ippu_activity_data_1990_2023.csv` - 572 activity-data records;
- `data/processed/crf_2023_vs_crt_2025_ippu_comparison_1990_2021.csv` - 800 comparisons;
- `data/processed/bns_vs_crt_2025_activity_comparison_2021.csv` - 7 transparent product comparisons.

Historical trends, category composition, CRF–CRT comparison and ready-to-use figure captions are in the [article analysis](article_analysis_en.md).
The complete activity-data and process-boundary review is in the [NID/NIR methodology review](process_methodology_review_en.md).
