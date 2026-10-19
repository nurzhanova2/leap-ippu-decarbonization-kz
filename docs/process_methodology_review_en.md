# Activity-data comparability and NID/NIR methodology review

Русская версия: [process_methodology_review.md](process_methodology_review.md).

## Status and interpretation rule

Targeted NID 2025 and NIR 2023 method sections have been reviewed for lime, iron/steel, ferroalloys and primary aluminium; NID 2025 section 4.2.4 on other process uses of carbonates (2.A.4) was reviewed on 18 October 2026. Together with the previously reviewed clinker and zinc sections, they allow BNS–UNFCCC comparisons to be interpreted at process level rather than from table values alone.

**Rule:** a numerical difference can be called a data discrepancy only after product, unit, geography, technological stream, and plant-versus-national-output boundary are confirmed to be the same.

Full machine-readable table: [`data/processed/ippu_process_comparability_2021.csv`](../data/processed/ippu_process_comparability_2021.csv).

## 2021 comparability summary

| Process | BNS, Mt | UNFCCC, Mt | Unit and product | UNFCCC activity-data boundary | Comparability | Conclusion |
|---|---:|---:|---|---|---|---|
| Clinker, 2.A.1 | 7.295700 | 7.295700 | tonnes; cement clinker | national BNS clinker output | direct | Exact agreement; Portland cement cannot replace clinker. |
| Lime, 2.A.2 | 0.933623 | 0.933623 | tonnes; hydrated, quick and hydraulic lime | national BNS aggregate, including own-use lime | direct at aggregate level | Exact agreement; NID uses an 85/15 split for lime types. |
| Pig iron, 2.C.1.b | 3.623764 | 3.195305 | tonnes; BNS covers primary pig-iron forms | Qarmet integrated-plant data and carbon balance | not direct | The −11.8% difference reflects boundaries, not an established error. |
| Crude steel, 2.C.1.a | 4.526071 | 4.526071 | tonnes; crude steel | national BNS data, complemented by Qarmet inputs for carbon balance | direct as output indicator | Exact agreement; output alone is insufficient to calculate emissions. |
| Ferroalloys, 2.C.2 | 2.070038 | 2.070038 | tonnes; ferroalloys | national BNS output; Kazchrome data for reducer/EF | direct as total output | Exact agreement; retain alloy mix and plant data for EF calculation. |
| Primary aluminium, 2.C.3 | — | — | available BNS long series combines aluminium and aluminium oxide | Kazakhstan Electrolysis Plant: output, anodes/reductants, anode effect | no valid comparison | Obtain disaggregated or plant data; the published BNS aggregate is unsuitable. |
| Zinc, 2.C.6 | 0.300886 | 0.081861 | tonnes; BNS unwrought zinc, CRT zinc from Waelz cakes | KazZinc technological stream | not direct | The −72.8% difference is not a data-quality metric. |

The difference is `(UNFCCC − BNS) / BNS`. A negative value merely shows that a narrower UNFCCC measure was compared with a wider BNS measure.

## Process-level methodology review

### 2.A.1 Clinker

NID 2025 uses BNS clinker, not Portland-cement, output; both sources report 7,295.7 kt in 2021. The initial comparison against 12,312.7 kt of Portland cement was methodologically invalid. Source: NID 2025, p.157.

### 2.A.2 Lime

NID 2025 (p.160) and NIR 2023 (pp.188–191) establish that activity data are total BNS output of hydrated, quick and hydraulic lime, including non-market own-use lime. National statistics do not separate high-calcium and dolomitic lime; NID applies an 85/15 split and IPCC 2006 Tier 1 factors of 0.75 and 0.86 t CO2/t, respectively. Thus the 933.623 kt agreement is valid for aggregate activity data, not for product composition.

### 2.C.1 Iron and steel

NID 2025 (pp.179–184) and NIR 2023 (pp.213–218) use IPCC 2006 Tier 2, practically approaching Tier 3 when enterprise data are available. For pig iron, inventory inputs originate from Qarmet (formerly ArcelorMittal Temirtau) and include coke, limestone and carbon-balance information. The 3.195305 Mt is therefore a plant-model input, not necessarily the full national BNS output of 3.623764 Mt.

For steel, NID 2025 explicitly identifies BNS as the source of production volumes, supplemented by Qarmet and electric-steel parameters for the carbon balance. BNS and CRT both report 4.526071 Mt in 2021. This validates output comparability, but not emission estimation by multiplying output by a universal factor.

### 2.C.2 Ferroalloys

NID 2025 (pp.190–191) and NIR 2023 (pp.225–228) apply Tier 2: total BNS output is combined with Kazchrome reducer data. The difference between enterprise and BNS production is represented as other producers. The 2.070038 Mt match validates the total-output indicator, but LEAP calibration should retain alloy types and reducer consumption. NID assesses activity-data uncertainty at below 10% and total CO2 uncertainty at 7.1%; these are NID assessments, not independent estimates by this study.

### 2.C.3 Primary aluminium

NID 2025 (pp.194–195) and NIR 2023 (pp.228–232) describe the single producer, Kazakhstan Electrolysis Plant. Inputs include output, anode/reductant materials and anode-effect parameters; the method is Tier 3-like. The published BNS long series combines unwrought aluminium with aluminium oxide, so no valid comparison is possible. This is a material data gap for later LEAP work and should not be hidden by imputation.

### 2.C.6 Zinc

NID 2025 (p.200) defines activity data as zinc produced from Waelz cakes in Waelz kilns at KazZinc. In 2021 this is 81.861 kt, versus 300.886 kt of total BNS unwrought-zinc output. These are different production populations; the percentage comparison may illustrate non-comparability but cannot demonstrate unreliability of either BNS or UNFCCC data.

## 2.A.4 Other process uses of carbonates: composition and scenario treatment

Sources: NID 2025, section 4.2.4, pp.163–171 (PDF page numbers equal the printed page numbers); CRT 2025, Table2(I).A-H; IPCC 2006, Vol. 3, Ch. 2, pp.2.24, 2.32–2.37. The 1990–2023 subcategory series is in [`crt_2025_2a4_subcategories_1990_2023.csv`](../data/processed/crt_2025_2a4_subcategories_1990_2023.csv), extracted by [`extract_crt_2a4_subcategories.py`](../scripts/extract_crt_2a4_subcategories.py); the `row_level` column separates the category, subcategory and item rows, and the subcategory rows sum to the 2.A.4 total in every year.

### Composition in 2023

| Subcategory | Carbonate and activity data | Consumers | NID method | Activity data, kt | CO2, kt | Share of 2.A.4 |
|---|---|---|---|---:|---:|---:|
| 2.A.4.a Ceramics | carbonates in clay: product mass × 1.1 × 0.1 (pp.163–164) | bricks, facing tiles, household ceramics; BNS output | Tier 1, IPCC default | 668.521 | 73.537 | 1.6% |
| 2.A.4.b Other uses of soda ash | Na2CO3, 0.415 t CO2/t (p.166) | alumina refining (Aluminium of Kazakhstan JSC) and yellow phosphorus (Kazphosphate LLP); all soda ash is imported (p.165) | Tier 1, enterprise data | 172.265 | 71.489 | 1.6% |
| 2.A.4.c Non-metallurgical magnesia | — | — | NO | NO | NO | — |
| 2.A.4.d Use of limestone and dolomite | CaCO3 0.44 and CaMg(CO3)2 0.477 t CO2/t, IPCC 2006 Table 2.1 (p.167) | not identified: residual of domestic sales (pp.167–168) | reported as Tier 2, key category (p.167) | 9,884.451 | 4,399.988 | 96.8% |
| **2.A.4 total** | | | | | **4,545.014** | 100% |

Activity data and CO2 are from CRT 2025 for 2023. With 4,545.0 kt, 2.A.4 is 19.3% of the 23,551.9 kt model boundary and the second-largest branch after pig iron (5,041.0 kt), ahead of cement clinker (4,345.7 kt). Observation on ceramics: the CRT implied factor is 0.110 t CO2/t product, which numerically coincides with the product 1.1 × 0.1 in the NID formula, while NID does not state the emission factor applied to carbonates (p.164). The factor requires clarification with the NID compilers.

### How 2.A.4.d is estimated

BNS provides only the quantities of limestone and dolomite sold on the domestic market, without a breakdown by economic activity (NID p.167). NID therefore requested limestone and dolomite use from metallurgical plants, including calcium carbide production, and from clinker plants, and takes the difference between domestic sales and that use as activity data (p.168). Agricultural liming is excluded because it is not practised in Kazakhstan (p.167).

| 2023 (NID Table 4.5, p.169; Table 4.6, p.170) | Limestone | Dolomite |
|---|---:|---:|
| Sold on the domestic market, kt | 18,854.7 | 1,879.3 |
| Used in metallurgy and clinker production, kt | 10,344.0 | 505.5 |
| Residual = activity data, kt | 8,510.6 | 1,373.7 |
| Emission factor, t CO2/t | 0.44 | 0.477 |
| CO2, kt | 3,744.6 | 655.2 |

The residuals (9,884.3 kt) and emissions (4,399.9 kt) agree with CRT within rounding. NID estimates the uncertainty at 10% for activity data, 5% for the emission factor and 12.1% combined (p.170). Three consequences follow:

1. **End use is unknown, and the whole residual is treated as calcined.** IPCC 2006 cautions against assuming that all limestone and dolomite consumed releases CO2, because use as aggregate or crushed stone is non-emissive (p.2.36; Table 2.7, p.2.37). NID attributes the growth of the category to the construction boom and industrial growth (p.170). Table 2.7 classifies construction use as aggregate as non-emissive. If part of the residual is crushed stone or aggregate, 2.A.4.d may be overstated. This is an observation, not an estimate, and requires clarification with the NID compilers.
2. **Residual arithmetic amplifies annual changes.** From 2022 to 2023, domestic limestone sales rose by 4.7% and use in metallurgy and clinker fell by 8.0%, so the limestone residual rose by 25.8% and 2.A.4.d emissions by 19.0% (pp.169–170). The 2023 value of 2.A.4.d, which serves as the 2024 proxy, is 14.4% above its 2021–2023 mean (3,846.7 kt). For the 2.A.4 total, the 2023 value (4,545.0 kt) is 13.9% above the 2021–2023 mean (3,989.7 kt).
3. **Long-term growth.** 2.A.4.d rose from 341.5 kt CO2 in 1990 to 4,400.0 kt in 2023, and 1.98-fold since 2010 (2,226.0 kt).

### Possible double counting with 2.C.1, 2.C.2, 2.B.5 and 2.A.2

| Category | Is carbonate CO2 included there? | Subtracted from 2.A.4.d? | Assessment |
|---|---|---|---|
| 2.C.1.b Pig iron, including sinter | Yes: 139.991 kt CO2 from limestone in 2023, Table 4.11 (pp.181–182); 0.12 t limestone per t pig iron including sintering (p.183) | Yes, as metallurgical use (p.168) | No double counting by design. Consistency check: 139.991 / 0.44 = 318.2 kt of limestone, versus 0.12 × 2,756.640 kt = 330.8 kt. |
| 2.C.1.a Steel | Not mentioned: the carbon balance covers pig iron, scrap and electrodes (pp.183–184), although Qarmet reported limestone and dolomite use for converter steel (pp.182–183) | Yes, if included in the metallurgical total | Possible omission, not double counting; not quantifiable from NID. |
| 2.C.1.d Sinter | No: coke breeze and gas (p.185); sinter limestone is counted under pig iron (p.183) | — | No overlap. |
| 2.C.2 Ferroalloys | No: CO2 from reductant (coke), 3.3 t CO2/t (pp.190–191) | Not stated: NID does not list which metallurgical plants reported carbonate use | Either an omission (if subtracted) or an allocation to 2.A.4.d instead of 2.C (IPCC: fluxes are reported where consumed, p.2.33 and Table 2.7). No double counting in either case. |
| 2.B.5 Calcium carbide | No: CO2 from coke, 1.7 t CO2/t (p.177) | Yes (p.168) | No double counting. |
| 2.A.2 Lime | Lime output includes non-market own-use lime (p.160) | Not stated: the deduction covers metallurgy, calcium carbide and clinker only (p.168) | Possible double counting for limestone sold to lime kilns outside metallurgy. Upper bound: approximately the 2.A.2 emissions, 721.5 kt CO2 (16.4% of 2.A.4.d), because calcining the same carbonate releases the same CO2; this bound is an author estimate. IPCC asks compilers to avoid double counting between lime production and limestone consumption (p.2.24). |

The main risk is therefore not double counting with metallurgy, which NID deducts explicitly, but (i) an overlap with lime production and (ii) possible non-emissive construction uses inside the residual.

### Scenario treatment: proposal

In the current scenarios, 2.A.4 belongs to the mineral group and receives the cement-type factors 0.85/0.60 (Moderate) and 0.70/0.30 (Ambitious). These factors are justified by clinker substitution and capture of calcination CO2 at kilns. Neither lever applies to 2.A.4.d, which has no identified emitting installation and makes up 96.8% of 2.A.4. The share of avoided emissions that comes from 2.A.4 is substantial:

| kt CO2eq | Moderate 2030 | Moderate 2050 | Ambitious 2030 | Ambitious 2050 |
|---|---:|---:|---:|---:|
| Avoided vs Baseline, current scenarios | 2,837.0 | 8,725.0 | 6,395.3 | 15,816.1 |
| of which from 2.A.4 | 681.8 (24.0%) | 1,818.0 (20.8%) | 1,363.5 (21.3%) | 3,181.5 (20.1%) |
| of which from 2.A.4.d | 660.0 (23.3%) | 1,760.0 (20.2%) | 1,320.0 (20.6%) | 3,080.0 (19.5%) |
| Avoided if 2.A.4.d kept at f = 1 (illustration) | 2,177.0 | 6,965.0 | 5,075.3 | 12,736.1 |

Decision for the additional scenario set (confirmed on 18 October 2026). The presented Baseline, Moderate and Ambitious scenarios remain unchanged.

1. **Separate branches:** 2.A.4.a + 2.A.4.b (145.0 kt) and 2.A.4.d (4,400.0 kt), outside the mineral group.
2. **Central case for 2.A.4.d: f = 1.00 and s = 1.00,** where s is the emissive share of the reported value. No mitigation lever can be attached to unidentified consumers. A low/high range is added only if the literature review (stage 2) yields levers for identifiable end uses; otherwise any value other than 1.00 is marked as an author assumption.
3. **Alternative variant: 2.A.4.d with the mineral-group factors** of the current scenarios (0.85/0.60 and 0.70/0.30). The stage-3 tornado shows how much of the result rests on this assumption.
4. **Lower bound s = 0.84:** removes the upper limit of the overlap with 2.A.2 (author estimate). It is a lower bound, not a central value. Possible non-emissive aggregate use is noted as an observation and is not quantified.
5. **Base-year sensitivity for 2.A.4.d:** 2023 value (4,400.0 kt) versus the 2021–2023 mean (3,846.7 kt).
6. **2.A.4.a + 2.A.4.b:** f from the literature review (ceramics raw materials; soda-ash use in alumina refining); f = 1.00 until then. The effect is at most 145.0 kt.
7. **Activity growth (stage 3):** link 2.A.4.d to its residual drivers, domestic limestone and dolomite sales net of metallurgy and clinker, not to cement output.

Suggested Methods wording: “Category 2.A.4 is modelled separately from cement. In the national inventory, 96.8% of its 2023 emissions (2.A.4.d) are estimated as domestic limestone and dolomite sales net of metallurgical and clinker use, with no identified end use (NID 2025, pp.167–170). We therefore apply no technology-specific abatement factor to 2.A.4.d in the central case and treat the residual-based estimate as an inventory uncertainty.”

## Recalculations between CRT 2025 and CRT 2026

The journal version uses the latest inventory: the CRT 2026 submission (16 April 2026, 1990–2024) and NID 2026. The conference version keeps CRT 2025 as an archive. Both submissions use AR5 GWPs, so all differences are recalculations.

Data files:
- [`crt_2025_vs_crt_2026_ippu_comparison_1990_2023_crt2026.csv`](../data/processed/crt_2025_vs_crt_2026_ippu_comparison_1990_2023_crt2026.csv): category-level comparison in the format of the CRF–CRT comparison;
- [`crt_ippu_subcategory_emissions_1990_2023_crt2025.csv`](../data/processed/crt_ippu_subcategory_emissions_1990_2023_crt2025.csv) and [`crt_ippu_subcategory_emissions_1990_2024_crt2026.csv`](../data/processed/crt_ippu_subcategory_emissions_1990_2024_crt2026.csv): subcategory level, from Table2(I).A-H.

**Size.** Total IPPU emissions are lower in every year: by 4,723.0 kt (−20.8%) in 1990, by 7,325.0 kt (−44.8%) in 1998 and by 2,890.4 kt (−10.8%) in 2023. In CRT 2026 the series starts at 18,018.3 kt in 1990, reaches its minimum of 7,705.1 kt in 1996 and rises to 23,882.3 kt in 2023 and 25,789.9 kt in 2024. The model boundary falls from 23,551.9 to 20,576.3 kt in 2023 (−12.6%).

| Subcategory | 2023: CRT 2025 → CRT 2026, kt CO2eq | 1990, kt CO2eq | Reason (NID 2026) |
|---|---|---|---|
| 2.C.1.d Sinter | 3,548.4 → 1,085.7 (−2,462.7) | 6,916.7 → 2,473.7 (−4,443.0) | Whole series recalculated on review recommendations I.6 2025KAZOK48 and I.7 2025KAZOK46 to avoid double counting: coke-oven and blast-furnace gas recalculated with density and calorific value; limestone used for sintering added (pp.226–230, Table 4.19) |
| 2.C.1.b Pig iron | 5,041.0 → 4,901.0 (−140.0) | 7,919.1 → 7,653.7 (−265.4) | Limestone CO2 removed from pig iron and reported under sinter; the difference equals the former limestone component (p.221, Table 4.14; p.229) |
| 2.A.4.d Limestone and dolomite use | 4,400.0 → 3,855.5 (−544.5) | 341.5 → 341.5 | Limestone and dolomite used in glass production added to the deducted uses (review recommendation I.3 2025KAZOK55; pp.203–207, Tables 4.6 and 4.9) |
| 2.B.1 Ammonia | 326.0 → 457.6 (+131.6) | 995.5 → 1,095.7 (+100.2) | Method revised on review recommendations I.3 2025KAZOK39 and I.4 2025KAZOK44: all natural gas used at KazAzot is allocated to IPPU and removed from 1.A.2.c (pp.209–210) |
| 2.A.3 Glass | 24.5 → 97.8 (+73.4) | 0 → 0 | Flat glass (OrdaGlass plant, operating since October 2022) added with 0.21 kg CO2/kg (pp.197–199) |
| 2.A.4.a Ceramics | 73.5 → 32.4 (−41.2) | 7.1 → 3.1 | The 0.44 t CO2/t carbonate factor is now applied and the whole series recalculated (review recommendation I.2 2025KAZOK28; p.200, Table 4.5) |

Other differences are small: steel +24.9 kt in 2023, F-gases (2.F) +99.5 kt in 2023 and lead −12.3 kt. Their causes were not reviewed.

Links with the stage-1 review of 2.A.4 (above):
- **Ceramics.** The correction matches our stage-1 observation that the implied factor 0.110 equalled 1.1 × 0.1. In CRT 2026 the implied factor is 0.0484 t CO2/t product (1.1 × 0.1 × 0.44).
- **2.A.4.d.** The recalculation narrows the residual by also deducting glass. Lime production (2.A.2) is still not among the deducted uses (Table 4.6, p.204), so the possible overlap with lime identified in stage 1 remains.
- **Observation on 2.A.4.d activity data.** CRT 2026 reports 7,426.2 kt (2023) and 7,631.5 kt (2024), whereas NID Table 4.7 gives limestone plus dolomite of 8,653.5 and 8,857.2 kt (p.205). The emissions agree, but the CRT implied factors (0.519 and 0.499 t CO2/t) exceed the dolomite factor of 0.477. Possibly part of the activity data is missing in CRT; this requires clarification with the NID compilers. Until then the sensitivity runs use CO2 as the activity proxy for 2.A.4.d.
- **Iron and steel.** The limestone flux is now reported under sinter instead of pig iron, consistent with the metallurgical deduction in 2.A.4.d.

**Check of NID values against CRT.** The NID 2026 values used in the 2024 comparison were transcribed from page images and checked against CRT 2026 for every model branch in 2023 and 2024. They agree within the rounding of the NID tables, with one exception. NID Table 4.13 reports sinter including CH4 (9.5 kt in 2023, 10.6 kt in 2024), whereas the model branch is CO2 only.

## Use in the article

In *Results*, report comparability status rather than rank processes by the absolute percentage difference. In *Discussion*, the supported conclusion is: “National statistics and inventory activity data are aligned for clinker, aggregate lime, steel and total ferroalloy output. Large apparent differences for pig iron and zinc arise when national output is mixed with plant-specific or technologically narrow streams. For primary aluminium, open statistics do not provide a fit-for-purpose activity-data series.”

