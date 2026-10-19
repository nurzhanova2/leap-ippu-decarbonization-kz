# Industrial process emissions in Kazakhstan: inventory harmonisation and exploratory LEAP pathways to 2050

Русская версия: [manuscript_full_ru.md](manuscript_full_ru.md).

> **Status (19 October 2026).** Journal version on the CRT 2026 inventory (1990–2024). Sections 1–5 are drafted. All numbers are taken from the `_crt2026` files in `data/processed/`, and every in-text reference is in [references.bib](references.bib). The archived conference version (CRT 2025) is in [manuscript_historical_results_discussion_en.md](manuscript_historical_results_discussion_en.md) and is not changed.

## Abstract

Industrial process emissions cannot be removed by decarbonising energy supply alone, yet scenario studies for Kazakhstan seldom represent them at process level. This study combines Kazakhstan's 2026 greenhouse-gas inventory submission (CRT 2026, 1990–2024) with an exploratory LEAP model of 15 process-emission branches that cover 85.6% of emissions from industrial processes and product use (IPPU) in 2024. According to CRT 2026, IPPU emissions fell from 18,018 kt CO2eq in 1990 to 7,705 kt CO2eq in 1996 and rose to 25,790 kt CO2eq in 2024. Recalculations relative to the previous submission lowered the series in every year, by 20.8% in 1990, mainly through sinter. In 2021, inventory activity data agree exactly with national production statistics for clinker, lime, crude steel and ferroalloys, whereas apparent differences for pig iron and zinc reflect plant- and stream-level boundaries. From a 2024 base of 22,088 kt CO2eq, the Moderate and Ambitious scenarios reduce included emissions to 19,418 and 16,072 kt CO2eq in 2030 and to 13,896 and 7,236 kt CO2eq in 2050. Literature-based factors support the 2050 Moderate level (14,009 kt CO2eq) but imply slower reductions before 2030. About one fifth of the avoided emissions comes from the use of limestone and dolomite (2.A.4.d), a residual inventory estimate without an identified end use. Under plausible activity growth, the remaining-emissions factors matter about 2.5–3 times more than growth in 2050; only sustained growth of physical output of about 3% per year reverses this. The pathways are exploratory results for a defined process boundary, not forecasts or an assessment of national targets.

**Keywords:** Kazakhstan; industrial processes and product use; greenhouse-gas inventory; LEAP; decarbonisation scenarios; sensitivity analysis

## 1. Introduction

Industrial processes and product use (IPPU) form a distinct part of national greenhouse-gas inventories: their emissions arise from chemical and physical transformations of materials, such as the calcination of carbonates in clinker production or the use of carbon as a reductant in metallurgy, rather than from fuel combustion. They therefore cannot be removed by decarbonising energy supply alone. For this reason, research on cement and steel examines process emissions, material substitution, new reduction routes and carbon capture (Obrist et al., 2021; Tautorat et al., 2023; Müller et al., 2024), and the IPCC assessment treats industry as a sector with its own mitigation options (Bashmakov et al., 2022).

In Kazakhstan, IPPU emissions reached 25,789.9 kt CO2eq in 2024, 43.1% above their 1990 level, according to the 2026 inventory submission (Republic of Kazakhstan, 2026a). The updated NDC sets an economy-wide reduction of 15% (unconditional) and 25% (conditional) by 2030 relative to 1990 (Government of the Republic of Kazakhstan, 2023, p. 4), and the Strategy for achieving carbon neutrality by 2060 was approved in 2023 (President of the Republic of Kazakhstan, 2023).

Most quantitative pathways for Kazakhstan are energy-system studies. Zhakiyev et al. (2023) use a TIMES model to compare a reference scenario with a carbon-neutrality scenario to 2060; De Miglio and Bakdolotov (2024) explore the energy sector under a user-defined risk criterion; Cassetti et al. (2023) develop scenarios, including a net-zero pathway, for four countries of the Central Asian and Caspian region; and Zhakiyev, Kayisli, et al. (2025) forecast emissions from the energy and industrial sectors under scenarios with a high share of renewables. Reviews examine the region's energy transition, policies and reliance on fossil fuels (Radovanović et al., 2021; Zhakiyev, Khamzina, et al., 2025). Studies of Kazakhstan's industry examine carbon capture hubs (Khoyashov et al., 2024), the emissions trading system (Khussain et al., 2025) and the decarbonisation of mining and steel (Aubakirova et al., 2023; Menzies et al., 2024; Holtz et al., 2025).

For bottom-up modelling of industry, LEAP (Heaps, 2022) has been applied to technology pathways of cement and steel: for example, the G-LEAP model for China's cement industry (Tan et al., 2022), a combined LEAP-LCA perspective (Dang et al., 2026) and LEAP-based simulations of iron and steel production, including hydrogen metallurgy (Duan et al., 2022; Wan & Li, 2024). These studies show the value of representing processes explicitly, but their parameters belong to other industrial systems.

Khamzina et al. (2026) provide the closest precedent: Kazakhstan-specific IPPU scenarios to 2040 (without, with current and with additional measures), built from category-level trends of the national inventory and a cement material-efficiency measure supported by molecular modelling. This study complements that work in four respects. First, it uses the latest inventory submission (CRT 2026, 1990–2024) and shows that recalculations between submissions change the 1990 level by about one fifth. Second, it works at process level, with activity data and intensities for 15 branches, and tests their comparability with national statistics. Third, it applies mitigation factors to all major mineral, metal and chemical process branches, extending mitigation beyond cement, and tests them against published pathways. Fourth, it separates activity growth from process intensity and shows which of the two dominates the 2050 outcome. The results of the two studies are not directly comparable: Khamzina et al. (2026) cover all IPPU emissions, including F-gases, to 2040, whereas this study covers 85.6% of IPPU emissions in 2024, without F-gases, to 2050.

The article addresses four questions: (1) how Kazakhstan's IPPU emissions and their composition changed in 1990–2024; (2) how the CRT 2026 recalculations change the historical series and the model base; (3) to what extent apparent differences between national statistics and inventory activity data arise from product and process boundaries; and (4) how included process emissions evolve to 2030 and 2050 under exploratory mitigation factors, literature-based factors and alternative activity growth. Section 2 describes the data and methods, Section 3 reports the results, Section 4 discusses them, and Section 5 concludes.

## 2. Data and methods

### 2.1. Inventory data

The study uses Kazakhstan's 2026 greenhouse-gas inventory submission to the UNFCCC: the Common Reporting Tables (CRT 2026; Republic of Kazakhstan, 2026a), which cover 1990–2024, and the National Inventory Document (NID 2026; Republic of Kazakhstan, 2026b). Total IPPU emissions by category are taken from CRT Table 2(I), and emissions and activity data by subcategory from Tables 2(I).A–H. The previous submission (CRT 2025, 1990–2023; Republic of Kazakhstan, 2025a) is used only to quantify recalculations. The methodological references for the included categories are the 2006 IPCC Guidelines (IPCC, 2006) and the 2019 Refinement (IPCC, 2019).

All aggregate values are in kt CO2eq with 100-year global warming potentials (GWP100) from the IPCC Fifth Assessment Report: CO2 = 1, CH4 = 28 and N2O = 265 (Myhre et al., 2013, Table 8.7, p. 714). These are the values that Parties use for reporting under the enhanced transparency framework (UNFCCC, 2019, decision 18/CMA.1, annex, para. 37). Both CRT 2025 and CRT 2026 use AR5 GWPs, so differences between them are recalculations rather than metric effects.

### 2.2. Activity data and national statistics

Activity data from the inventory are compared with physical production statistics of the Bureau of National Statistics (BNS, 2022–2026). A numerical difference is treated as a data discrepancy only after the product, unit, geography, technological stream and plant-versus-national boundary are confirmed to be the same. The process-level methods are taken from NID 2025 (Republic of Kazakhstan, 2025b). The comparison year is 2021: for the seven compared processes, the 2021 activity data in CRT 2026 are identical to those in CRT 2025.

### 2.3. Model boundary

The scenario model covers 15 process-emission branches of mineral, metal and chemical industry (Table 1). In 2024, these branches account for 22,088.3 of 25,789.9 kt CO2eq of total IPPU emissions (85.6%). The excluded 3,701.5 kt CO2eq are F-gases (2.F), non-energy products from fuels and solvent use (2.D), lead (2.C.5), CH4 from sinter, PFCs from aluminium and other product use (2.G). Industrial fuel combustion belongs to the Energy sector of the inventory and is outside the boundary.

**Table 1. Model boundary in 2024, kt CO2eq (AR5 GWP100).**

| Branch | IPCC code | Gas | 2024 | Share of boundary |
|---|---|---|---:|---:|
| Pig iron | 2.C.1.b | CO2 | 5,614.6 | 25.4% |
| Cement clinker | 2.A.1 | CO2 | 4,459.9 | 20.2% |
| Other process uses of carbonates | 2.A.4 | CO2 | 3,917.5 | 17.7% |
| Ferroalloys | 2.C.2 | CO2 | 3,760.9 | 17.0% |
| Ferroalloys | 2.C.2 | CH4 | 1.0 | 0.0% |
| Sinter | 2.C.1.d | CO2 | 1,223.7 | 5.5% |
| Lime | 2.A.2 | CO2 | 744.2 | 3.4% |
| Steel | 2.C.1.a | CO2 | 531.4 | 2.4% |
| Ammonia | 2.B.1 | CO2 | 485.5 | 2.2% |
| Aluminium | 2.C.3 | CO2 | 426.5 | 1.9% |
| Pellets | 2.C.1.e | CO2 | 363.8 | 1.6% |
| Zinc | 2.C.6 | CO2 | 275.9 | 1.2% |
| Nitric acid | 2.B.2 | N2O | 160.3 | 0.7% |
| Glass | 2.A.3 | CO2 | 103.5 | 0.5% |
| Calcium carbide | 2.B.5 | CO2 | 19.9 | 0.1% |
| **Included, total** | | | **22,088.3** | **100%** |
| *Excluded:* F-gases | 2.F | HFC, PFC | 3,098.7 | |
| *Excluded:* non-energy products from fuels and solvent use | 2.D | CO2 | 528.2 | |
| *Excluded:* lead | 2.C.5 | CO2 | 58.1 | |
| *Excluded:* CH4 from sinter | 2.C.1.d | CH4 | 10.6 | |
| *Excluded:* PFCs from aluminium | 2.C.3 | PFC | 3.1 | |
| *Excluded:* other product use | 2.G | various | 2.7 | |
| *Excluded, total* | | | *3,701.5* | |

Source: CRT 2026, Tables 2(I) and 2(I).A–H (Republic of Kazakhstan, 2026a); authors' calculations. The excluded components do not sum exactly to the total because of rounding.

### 2.4. Base year and base levels

The base year of the model is 2024, and its Current Accounts equal the CRT 2026 values for 2024. The repository keeps a second base level for the archived conference version, which used the CRT 2025 values for 2023 as a proxy for 2024 (Table 2). All results of this article refer to the CRT 2026 inventory 2024 base.

**Table 2. Base levels of the model, kt CO2eq (AR5 GWP100).**

| Base level | 2024 value | Content | Use |
|---|---:|---|---|
| CRT 2025 proxy base | 23,551.9 | CRT 2025 values for 2023, used for 2024 | archived conference version |
| CRT 2026 inventory 2024 base | 22,088.3 | CRT 2026 values for 2024 | this article |

Source: CRT 2025 and CRT 2026, Tables 2(I).A–H (Republic of Kazakhstan, 2025a, 2026a); authors' calculations.

The CRT 2026 base is 1,463.6 kt (6.2%) lower. Two effects combine: the recalculation of 2023 in CRT 2026 lowers the boundary by 2,975.6 kt, from 23,551.9 to 20,576.3 kt, and the change from 2023 to 2024 raises it by 1,512.0 kt (7.3%).

### 2.5. LEAP implementation

The model is implemented in LEAP 2026.5.0.1 (Heaps, 2022). Each of the 15 branches is represented by the `Non Energy Effect Loading` variable, whose Current Accounts value is the 2024 emission of the branch in tonnes of gas. CO2 branches are entered in metric tonnes; the CH4 branch of ferroalloys and the N2O branch of nitric acid are entered in kilograms, the unit of the LEAP template (34,807 kg CH4 and 604,800 kg N2O). The scenario values are given by the expression

`Interp(2024, base, 2030, base × f2030, 2050, base × f2050)`,

where f2030 and f2050 are remaining-emissions factors. Results are computed using LEAP's deterministic `Interp()` expressions and reproduced in Python; the parameters, the LEAP import workbook and the scripts are listed in the Data availability section.

### 2.6. Scenarios

The Baseline holds every branch at its 2024 value. The Moderate and Ambitious mitigation scenarios interpolate linearly to the factors in Table 3. A factor of 0.85, for example, means emissions 15% below the 2024 branch value at constant activity. The factors are author-selected envelopes for portfolios of recognised measures: clinker and material substitution and, in the deeper case, capture of calcination CO2 for mineral processes; material efficiency, scrap-based routes, low-carbon reduction and capture for metals; process optimisation, nitric-acid N2O abatement, route change and capture for chemicals. They are not technology-specific potentials, official targets or a least-cost result.

**Table 3. Remaining-emissions factors of the main scenarios (share of the 2024 branch value).**

| Process group | Moderate: 2030 / 2050 | Ambitious: 2030 / 2050 |
|---|---:|---:|
| Mineral industry (2.A.1–2.A.4) | 0.85 / 0.60 | 0.70 / 0.30 |
| Metal industry (2.C.1, 2.C.2, 2.C.3, 2.C.6) | 0.90 / 0.65 | 0.75 / 0.35 |
| Chemical industry (2.B.1, 2.B.2, 2.B.5) | 0.90 / 0.65 | 0.70 / 0.30 |

Source: authors' scenario design; parameters in `data/metadata/leap_scenario_parameters_crt2026.csv`. The Baseline factor is 1.00 in all years.

### 2.7. Other process uses of carbonates (2.A.4)

Category 2.A.4 is the third-largest branch of the boundary (Table 1), and almost all of it is subcategory 2.A.4.d, use of limestone and dolomite (Table 4). The inventory estimates 2.A.4.d as domestic sales of limestone and dolomite net of their use in metallurgy, calcium carbide and clinker production; the end use of the residual is not identified (NID 2025, pp. 167–170). In CRT 2026, the use in glass production was added to the deducted quantities (NID 2026, pp. 203–207), whereas lime production (2.A.2) is still not among them (NID 2026, Table 4.6, p. 204).

**Table 4. Composition of category 2.A.4 in 2024.**

| Subcategory | Activity data, kt | Implied factor, t CO2/t | CO2, kt | Share of 2.A.4 |
|---|---:|---:|---:|---:|
| 2.A.4.a Ceramics | 689.1 | 0.0484 | 33.4 | 0.9% |
| 2.A.4.b Other uses of soda ash | 176.6 | 0.4150 | 73.3 | 1.9% |
| 2.A.4.c Non-metallurgical magnesia | NO | NO | NO | — |
| 2.A.4.d Use of limestone and dolomite | 7,631.5 | 0.4994 | 3,810.9 | 97.3% |
| **2.A.4 total** | | | **3,917.5** | **100%** |

Source: CRT 2026, Table 2(I).A–H (Republic of Kazakhstan, 2026a); authors' calculations. NO: not occurring.

Three features of 2.A.4.d matter for the scenarios. First, no specific abatement lever can be attached to consumers that are not identified. Second, the residual may overlap with lime production; the upper bound of this overlap is the 2.A.2 emission of 744.2 kt, or 19.5% of 2.A.4.d in 2024 (an author estimate). Third, the CRT 2026 activity data for 2.A.4.d (7,426.2 kt in 2023 and 7,631.5 kt in 2024) are lower than the limestone and dolomite totals in NID 2026 (8,653.5 and 8,857.2 kt; Table 4.7, p. 205), while the emissions agree. The resulting implied factors, 0.519 and 0.499 t CO2/t, exceed the dolomite factor of 0.477 t CO2/t, which is possible only if part of the activity data is missing in the CRT. This observation requires clarification with the inventory compilers.

The main scenarios keep 2.A.4 in the mineral group with the factors of Table 3, as in the LEAP workbook. In the literature-based factor sets (Section 2.8), both 2.A.4 branches have f = 1.00, and the emissive share of 2.A.4.d is s = 1.00. The sensitivity analysis adds three variants for 2.A.4.d: the lower bound s = 0.80, which removes the full possible overlap with lime; the mineral-group factors of the main scenarios; and the 2022–2024 mean (3,645.8 kt) instead of the 2024 value as the base.

### 2.8. Literature-based factors

To test the factors of Table 3, low, central and high values of f2030 and f2050 were derived for each process from published pathways (Table 5). A factor multiplies emissions at constant activity, so literature values were converted to intensity multipliers: f equals the ratio of the target intensity to the base intensity, one minus the share of near-zero-emission production, or one minus the percentage reduction. Values that include lower demand were not used, because activity is varied separately (Section 2.9). The low value is the deepest intensity reduction supported by the literature; the central value is a reference scenario where one exists and otherwise the midpoint of low and high; the high value is the least ambitious evidence or a documented Kazakhstan constraint. The finding that carbon capture and storage (CCS) is not expected in Kazakhstan's metals industries within 10–15 years (Holtz et al., 2025, p. 37) is used as a constraint for all CCS-dependent levers in 2030 only.

In 2030, the central value rests on a reference scenario for 6 processes (57.1% of the base), on a midpoint for 5 processes (23.3%) and on an author assumption for 5 processes (19.5%). In 2050, the corresponding figures are 8 processes (60.1%), 3 processes (20.4%) and 5 processes (19.5%).

**Table 5. Literature-based remaining-emissions factors (low / central / high).**

| Process | f2030 | f2050 | Basis of the central value | Main sources |
|---|---|---|---|---|
| Cement clinker (2.A.1) | 0.84 / 0.97 / 1.00 | 0.06 / 0.71 / 0.85 | reference scenario | IEA (2023, p. 96); IEA and Cement Sustainability Initiative (2018, Table 2); high: author assumption (clinker ratio from BNS data, CCS timing after Holtz et al., 2025, p. 37) |
| Lime (2.A.2) | 0.90 / 0.95 / 1.00 | 0.10 / 0.53 / 0.95 | midpoint | European Lime Association (2023, pp. 18–19) |
| Glass (2.A.3) | 0.70 / 0.85 / 1.00 | 0.30 / 0.60 / 1.00 | author assumption | not found |
| 2.A.4.a+b and 2.A.4.d | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | author assumption | not found |
| Pig iron, steel, sinter, pellets (2.C.1) | 0.79 / 1.00 / 1.00 | 0.11 / 0.38 / 0.83 | reference scenario | IEA (2020, pp. 43, 73, 97); Menzies et al. (2024, pp. 17, 49) |
| Ferroalloys (2.C.2) | 0.60 / 0.80 / 1.00 | 0.50 / 0.75 / 1.00 | midpoint | Jayakumari et al. (2026, p. 2); Holtz et al. (2025, p. 35) |
| Aluminium (2.C.3) | 0.93 / 1.00 / 1.00 | 0.04 / 0.73 / 0.99 | reference scenario | IEA (2023, p. 95); Menzies et al. (2024, pp. 17, 49) |
| Zinc (2.C.6) | 0.75 / 0.90 / 1.00 | 0.35 / 0.65 / 1.00 | author assumption | not found |
| Ammonia (2.B.1) | 0.97 / 0.99 / 1.00 | 0.05 / 0.30 / 1.00 | midpoint (2030); reference scenario (2050) | IEA (2021, p. 10); Holtz et al. (2025, p. 41) |
| Nitric acid (2.B.2) | 0.02 / 0.51 / 1.00 | 0.02 / 0.37 / 1.00 | midpoint (2030); reference scenario (2050) | European Commission (2007, Table 3.14, p. 140); NID 2025 (p. 175) |
| Calcium carbide (2.B.5) | 0.70 / 0.90 / 1.00 | 0.30 / 0.65 / 1.00 | author assumption | not found |

Source: `data/metadata/leap_sensitivity_factors.csv` and `data/metadata/scenario_levers_literature.csv` (entries L01–L36, with page or table for every value). Where no literature was found, low equals the Ambitious factor, central the Moderate factor and high 1.00.

Compared with these ranges, the 2030 factors of Table 3 assume more reduction than the literature supports for lime, aluminium and ammonia in both scenarios, and for cement clinker and, marginally, iron and steel in Ambitious. In 2050, apart from 2.A.4, only the Ambitious factor for ferroalloys (0.35) lies outside the range.

### 2.9. Activity growth and sensitivity analysis

In the sensitivity runs, the emissions of each branch equal activity × intensity × f(t), and for 2.A.4.d they are also multiplied by s. Activity is the CRT 2026 activity in 2024 multiplied by a growth index; intensity is the 2024 ratio of emissions to activity and is held constant; f(t) follows the `Interp()` rule of Section 2.5. For 2.A.4.a+b, whose two activity series have different units, CO2 is used as the activity proxy. For 2.A.4.d, CO2 is used as the activity proxy as a forced measure, because the CRT 2026 activity data are inconsistent with the emissions (Section 2.7). With zero growth and the factors of Table 3, the method reproduces the main scenarios to within 0.001 kt.

Five growth variants are used (Table 6). Four of them are treated as plausible; the fifth is a stress test. The official forecast of the Ministry of National Economy gives growth of sector value added, not of physical output, and the mapping of sectors to processes is an author assumption, so this variant is closer to an upper estimate. The stress test corresponds to about 3% per year of physical output for 26 years, which the value-added forecast does not support; it shows only the condition under which the main conclusion stops holding. The trend of glass is set to zero: since 2022 the series includes flat glass from a single new plant, which makes up about three quarters of glass CO2 in 2024 (78.7 of 103.5 kt, derived from NID 2026, pp. 197–198), so the log-linear trend measures the plant's entry rather than growth. The trend is applied only to 2030, because extrapolating it to 2050 would multiply clinker activity 11.6-fold.

**Table 6. Activity-growth variants after 2024.**

| Variant | Rule | Source |
|---|---|---|
| Zero | activity constant at the 2024 level | main scenarios |
| Trend to 2030 | log-linear trend of CRT 2026 activity data for 2010–2023, applied in 2025–2030 and constant afterwards; zero for glass | CRT 2026 (Republic of Kazakhstan, 2026a) |
| Official 2025–2029 | sector rates in 2025–2029, constant afterwards: manufacturing 5.8%, mining 2.9% (pellets), construction 9.3% (2.A.4.d) per year | Ministry of National Economy of the Republic of Kazakhstan (2024, pp. 14–15) |
| 1.5% per year to 2050 | 1.5% per year for all branches in 2025–2050 | author assumption |
| Stress test | half the official sector rates (2.9%, 1.45% and 4.65% per year) in 2025–2050 | stress test, not a projection |

Average annual growth rates by branch for each variant are in `data/processed/leap_ippu_sensitivity_growth_rates_crt2026.csv`.

Six factor sets are combined with each growth variant: the factors of the three main scenarios ("Baseline-growth", "Moderate-growth" and "Ambitious-growth") and the literature low, central and high factors. The reference case for one-at-a-time analysis combines the literature central factors, the trend to 2030, f = 1.00 and s = 1.00 for 2.A.4.d, and the 2024 base value. To compare the two sources of uncertainty, the range of 2050 emissions across growth variants (with central factors) is set against the range across factor sets (with the trend).

## 3. Results

### 3.1. Historical trend

According to CRT 2026, Kazakhstan's total IPPU emissions fell from 18,018.3 kt CO2eq in 1990 to a minimum of 7,705.1 kt CO2eq in 1996, a decline of 57.2% (Figure 1). They then rose to 23,882.3 kt CO2eq in 2023 and 25,789.9 kt CO2eq in 2024, the highest value of the series. The 2024 level is 234.7% above the 1996 minimum, 43.1% above 1990 and 8.0% above 2023. The series is the official inventory trajectory, not a direct measure of physical output: changes reflect output, technology, product composition, data sources and inventory methods.

![Figure 1](../figures/figure_1_ippu_total_emissions_1990_2024_crt2026.png)

*Figure 1. Total IPPU emissions of Kazakhstan, 1990–2024, kt CO2eq (AR5 GWP100). Source: CRT 2026, Table 2(I) (Republic of Kazakhstan, 2026a); authors' calculations.*

### 3.2. Composition by category

Metal industry (2.C) remained the largest category, but its share fell from 76.3% in 1990 to 47.6% in 2024, when it emitted 12,269.5 kt CO2eq (Figure 2). The share of mineral industry (2.A) rose from 16.1% to 35.8% (9,225.0 kt CO2eq in 2024). F-gases (2.F), absent in 1990 and above 1% of the total from 1998, reached 12.0% in 2024 (3,098.7 kt CO2eq). Chemical industry (2.B) fell from 7.6% to 2.6% (665.7 kt CO2eq), and non-energy products from fuels and solvent use (2.D) accounted for 2.0% (528.2 kt CO2eq). A model of Kazakhstan's IPPU emissions therefore needs separate mineral, metal and F-gas branches.

![Figure 2](../figures/figure_2_ippu_category_composition_1990_2024_crt2026.png)

*Figure 2. Composition of Kazakhstan's IPPU emissions by IPCC category, 1990–2024, kt CO2eq (AR5 GWP100). Source: CRT 2026, Table 2(I) (Republic of Kazakhstan, 2026a); authors' calculations.*

### 3.3. Recalculations between CRT 2025 and CRT 2026

CRT 2026 reports lower total IPPU emissions than CRT 2025 in every year of 1990–2023 (Figure 3): by 4,723.0 kt CO2eq (20.8%) in 1990, by 7,325.0 kt CO2eq (44.8%) in 1998, the largest relative difference, and by 2,890.4 kt CO2eq (10.8%) in 2023. Because both submissions use AR5 GWPs, the differences are recalculations. In 2023, the change is concentrated in metal industry (−2,609.2 kt CO2eq) and mineral industry (−512.3 kt CO2eq), partly offset by chemical industry (+131.6 kt CO2eq) and F-gases (+99.5 kt CO2eq). The sinter recalculation accounts for 94.1% of the difference in 1990, 96.3% in 1996 and 85.2% in 2023. Table 7 lists the main subcategory recalculations and the reasons given in NID 2026.

![Figure 3](../figures/figure_3_crt_2025_vs_crt_2026_total_ippu_comparison_crt2026.png)

*Figure 3. Recalculation of total IPPU emissions between the CRT 2025 and CRT 2026 submissions, 1990–2023, % of CRT 2025. Upper panel: total CO2eq (AR5 GWP100 in both submissions); lower panel: CO2. Source: CRT 2025 and CRT 2026, Table 2(I) (Republic of Kazakhstan, 2025a, 2026a); authors' calculations.*

**Table 7. Main subcategory recalculations, CRT 2025 → CRT 2026, kt CO2eq (AR5 GWP100).**

| Subcategory | 2023 | 1990 | Reason (NID 2026) |
|---|---|---|---|
| 2.C.1.d Sinter | 3,548.4 → 1,085.7 (−2,462.7) | 6,916.7 → 2,473.7 (−4,443.0) | whole series recalculated in response to review recommendations to avoid double counting: coke-oven and blast-furnace gas recalculated with density and calorific value; limestone used for sintering added (pp. 226–230) |
| 2.C.1.b Pig iron | 5,041.0 → 4,901.0 (−140.0) | 7,919.1 → 7,653.7 (−265.4) | limestone CO2 moved from pig iron to sinter (p. 221; p. 229) |
| 2.A.4.d Limestone and dolomite use | 4,400.0 → 3,855.5 (−544.5) | 341.5 → 341.5 | limestone and dolomite used in glass production added to the deducted uses (pp. 203–207) |
| 2.B.1 Ammonia | 326.0 → 457.6 (+131.6) | 995.5 → 1,095.7 (+100.2) | all natural gas used at the ammonia plant allocated to IPPU and removed from 1.A.2.c (pp. 209–210) |
| 2.A.3 Glass | 24.5 → 97.8 (+73.4) | 0 → 0 | flat glass from a plant operating since October 2022 added (pp. 197–199) |
| 2.A.4.a Ceramics | 73.5 → 32.4 (−41.2) | 7.1 → 3.1 (−4.0) | factor of 0.44 t CO2/t carbonate applied and the series recalculated (p. 200) |

Source: CRT 2025 and CRT 2026, Tables 2(I).A–H (Republic of Kazakhstan, 2025a, 2026a); NID 2026 (Republic of Kazakhstan, 2026b); authors' calculations.

The recalculations change the historical narrative. For the same years, growth from the 1996 minimum to 2023 is 118.4% in CRT 2025 and 210.0% in CRT 2026, because the recalculation lowers 1996 by 37.1% and 2023 by 10.8%. Within the model boundary, the 2023 value falls from 23,551.9 to 20,576.3 kt CO2eq (−12.6%).

### 3.4. Activity-data comparability at process level

Agreement between BNS and inventory activity data depends on whether the two indicators have the same product definition and boundary (Table 8). Clinker, lime, crude steel and total ferroalloy output agree exactly in 2021. Two large apparent differences compare different populations. For zinc, BNS reports total unwrought zinc, whereas the inventory reports zinc produced from Waelz cakes in Waelz kilns at one plant (NID 2025, p. 200). For pig iron, the inventory uses integrated-plant data with coke, limestone and carbon-balance inputs (NID 2025, pp. 179–184), so the 11.8% difference is not an established inconsistency. For primary aluminium, the published BNS long series combines aluminium and aluminium oxide, so no valid comparison is possible (NID 2025, pp. 194–195).

**Table 8. Comparability of BNS and inventory activity data, 2021, Mt.**

| Process | BNS | CRT 2026 | Status | Interpretation |
|---|---:|---:|---|---|
| Clinker, 2.A.1 | 7.295700 | 7.295700 | direct | same national clinker output (NID 2025, p. 157); Portland cement (12.312700 Mt) is not a substitute |
| Lime, 2.A.2 | 0.933623 | 0.933623 | direct as aggregate | same BNS aggregate; the inventory splits it 85/15 between high-calcium and dolomitic lime (NID 2025, p. 160) |
| Pig iron, 2.C.1.b | 3.623764 | 3.195305 | not direct | national output versus integrated-plant input |
| Crude steel, 2.C.1.a | 4.526071 | 4.526071 | direct as output | emissions also need carbon-balance parameters |
| Ferroalloys, 2.C.2 | 2.070038 | 2.070038 | direct as total output | alloy mix and reductant data remain necessary (NID 2025, pp. 190–191) |
| Primary aluminium, 2.C.3 | — | — | no valid comparison | BNS long series combines aluminium and alumina |
| Zinc, 2.C.6 | 0.300886 | 0.081861 | not direct | national total versus Waelz-kiln stream |

Source: BNS physical-production statistics for 2021 (BNS, 2022–2026); CRT 2026, Table 2(I).A–H (Republic of Kazakhstan, 2026a); NID 2025 (Republic of Kazakhstan, 2025b); authors' calculations. The 2021 values in CRT 2026 are identical to those in CRT 2025.

For 2024, the revised BNS series give the same year-on-year change as CRT 2026 for lime, pellets, ferroalloys and aluminium. For clinker the BNS bulletin index is 4.4 percentage points lower, because CRT 2026 uses a later BNS edition of 8,471.4 kt (NID 2026, p. 191) instead of the 8,106.3 kt published in the bulletin of January 2025.

### 3.5. Main scenarios

With constant activity, included emissions fall from 22,088 kt CO2eq in 2024 to 19,418 kt CO2eq in 2030 and 13,896 kt CO2eq in 2050 under Moderate mitigation, and to 16,072 and 7,236 kt CO2eq under Ambitious mitigation (Table 9, Figure 4).

**Table 9. Main scenarios, kt CO2eq (AR5 GWP100).**

| Scenario | 2030 | 2050 | Reduction vs Baseline, 2030 | Reduction vs Baseline, 2050 |
|---|---:|---:|---:|---:|
| Baseline | 22,088 | 22,088 | — | — |
| Moderate mitigation | 19,418 | 13,896 | 2,670 (12.1%) | 8,192 (37.1%) |
| Ambitious mitigation | 16,072 | 7,236 | 6,017 (27.2%) | 14,852 (67.2%) |

Source: authors' calculations with the LEAP expressions; `data/processed/leap_ippu_scenario_results_2024_2050_crt2026.csv`. Selected process-emissions boundary only (Table 1).

![Figure 4](../figures/figure_4_leap_ippu_scenario_pathways_2024_2050_crt2026.png)

*Figure 4. Included IPPU process emissions under the main scenarios, Kazakhstan, 2024–2050, kt CO2eq (AR5 GWP100). The Baseline is constant by construction. Source: CRT 2026 inventory 2024 base; authors' calculations with the LEAP expressions.*

By group, the metal industry gives the largest avoided emissions in 2050 in both scenarios: 4,269.2 of 8,192.2 kt CO2eq in Moderate and 7,928.5 of 14,852.0 kt CO2eq in Ambitious (Figure 5). In Moderate 2030, the mineral industry gives slightly more (1,383.8 kt CO2eq) than the metal industry (1,219.8 kt CO2eq), because its 2030 factor is lower. These shares follow from the base values and the factors and do not indicate that any technology is more feasible.

About one fifth of the avoided emissions comes from 2.A.4.d, for which no abatement lever is identified: 21.4% (2030) and 18.6% (2050) in Moderate, and 19.0% and 18.0% in Ambitious.

![Figure 5](../figures/figure_5_leap_ippu_avoided_emissions_2024_2050_crt2026.png)

*Figure 5. Avoided emissions relative to the Baseline by process group in 2030 and 2050, kt CO2eq (AR5 GWP100). Source: CRT 2026 inventory 2024 base; authors' calculations with the LEAP expressions. Excludes sources outside the model boundary.*

### 3.6. Literature-based factors and activity growth

At constant activity, the literature central factors give 21,036 kt CO2eq in 2030 and 14,009 kt CO2eq in 2050 (Table 10). In 2050 this is close to Moderate (13,896 kt CO2eq); in 2030 it is higher than Moderate (19,418 kt CO2eq), so the presented factors assume earlier reductions than the literature supports. The literature low factors give 7,169 kt CO2eq in 2050, close to Ambitious (7,236 kt CO2eq).

**Table 10. Included emissions by factor set and growth variant, kt CO2eq (AR5 GWP100).**

| Case, 2030 | Zero | Trend to 2030 | Official 2025–2029 | 1.5% per year | Stress test |
|---|---:|---:|---:|---:|---:|
| Baseline-growth | 22,088 | 27,455 | 30,112 | 24,152 | 26,668 |
| Moderate-growth | 19,418 | 24,027 | 26,444 | 21,233 | 23,429 |
| Ambitious-growth | 16,072 | 19,858 | 21,884 | 17,574 | 19,390 |
| Literature low | 17,864 | 22,389 | 24,525 | 19,533 | 21,661 |
| Literature central | 21,036 | 26,158 | 28,717 | 23,002 | 25,419 |
| Literature high | 22,088 | 27,455 | 30,112 | 24,152 | 26,668 |

| Case, 2050 | Zero | Trend to 2030 | Official 2025–2029 | 1.5% per year | Stress test |
|---|---:|---:|---:|---:|---:|
| Baseline-growth | 22,088 | 27,455 | 30,112 | 32,530 | 50,622 |
| Moderate-growth | 13,896 | 17,163 | 18,916 | 20,465 | 31,714 |
| Ambitious-growth | 7,236 | 8,876 | 9,839 | 10,657 | 16,457 |
| Literature low | 7,169 | 8,684 | 10,390 | 10,558 | 19,460 |
| Literature central | 14,009 | 17,988 | 19,440 | 20,631 | 33,779 |
| Literature high | 20,063 | 24,913 | 27,438 | 29,547 | 46,403 |

Source: `data/processed/leap_ippu_sensitivity_summary_2030_2050_crt2026.csv`; authors' calculations. "-growth" cases use the factors of the main scenarios; with zero growth they equal Table 9.

![Figure 6](../figures/figure_6_leap_ippu_growth_sensitivity_2024_2050_crt2026.png)

*Figure 6. Included IPPU process emissions with activity growth, Kazakhstan, 2024–2050, kt CO2eq (AR5 GWP100). (a) Factors of the main scenarios; (b) literature-based factors. Lines: trend to 2030; bands: range across the four plausible growth variants (the stress test is not shown); grey dots: main scenarios with zero growth. Source: CRT 2026 inventory 2024 base (Republic of Kazakhstan, 2026a); Ministry of National Economy of the Republic of Kazakhstan (2024); literature factors (Table 5); authors' calculations.*

In 2050, the factors matter more than activity growth under all plausible growth variants (Table 11). Across factor sets, 2050 emissions span 16,230 kt CO2eq. Across growth variants, they span 5,431 kt CO2eq if growth stops by 2030 and 6,622 kt CO2eq if activity grows by 1.5% per year to 2050; the factors therefore matter about 2.5–3 times more than growth. The conclusion stops holding only in the stress test, in which growth spans 19,770 kt CO2eq. In 2030, growth matters more than the factors: 7,681 against 5,066 kt CO2eq.

**Table 11. Ranges of 2050 emissions from growth and from factors, kt CO2eq (AR5 GWP100).**

| Growth variants compared | Range from growth (central factors) | Range from factors (trend) | Factors / growth |
|---|---:|---:|---:|
| Growth stops by 2030 (zero, trend, official) | 5,431 (14,009–19,440) | 16,230 (8,684–24,913) | 3.0 |
| Plausible (adds 1.5% per year to 2050) | 6,622 (14,009–20,631) | 16,230 (8,684–24,913) | 2.5 |
| Stress test (adds half the official rates to 2050) | 19,770 (14,009–33,779) | 16,230 (8,684–24,913) | 0.8 |

Source: `data/processed/leap_ippu_sensitivity_decomposition_crt2026.csv`; authors' calculations.

Among single assumptions (Figure 7), the factors of all processes together have the largest effect on the 2050 reference case of 17,988 kt CO2eq (16,230 kt CO2eq), followed by the stress test (15,791 kt CO2eq) and plausible growth (6,622 kt CO2eq). Among individual processes, the cement-clinker factor has the largest effect (6,208 kt CO2eq), ahead of iron and steel (5,596 kt CO2eq). Applying the Ambitious mineral-group factors to 2.A.4.d lowers the reference by 3,397 kt CO2eq, and the lower bound s = 0.80 by 971 kt CO2eq.

![Figure 7](../figures/figure_7_leap_ippu_tornado_2050_crt2026.png)

*Figure 7. Effect of one assumption at a time on included IPPU process emissions in 2050, kt CO2eq (AR5 GWP100). Reference: literature central factors, trend to 2030, 2.A.4.d with f = 1.00 and s = 1.00 (17,988 kt CO2eq). The stress test is shown as a separate bar. Source: as for Figure 6; `data/processed/leap_ippu_sensitivity_tornado_2050_crt2026.csv`.*

## 4. Discussion

### 4.1. Process boundaries before percentages

A percentage difference between BNS and inventory values is not, by itself, a measure of data quality. An IPPU category can represent a chemical transformation, an integrated plant route or a narrow technological stream rather than the marketed product in national statistics. The clinker and zinc cases show two forms of the same problem: replacing clinker with Portland cement creates a large artificial difference despite exact agreement for the correct indicator, while comparing national zinc output with one Waelz-kiln stream creates a large difference between populations that were never meant to match. A defensible workflow first establishes the product, coverage, plant boundary, route and unit; only the remaining difference between equivalent indicators can be investigated as an inconsistency.

### 4.2. Inventory recalculations and the base year

The recalculations between CRT 2025 and CRT 2026 are large enough to change both the baseline and the historical narrative. The 1990 level is 20.8% lower, the growth from 1996 to 2023 is 210.0% instead of 118.4%, and the 2023 level of the model boundary is 12.6% lower, mainly because sinter was recalculated to avoid double counting. A scenario study calibrated to one submission is therefore not directly comparable with a study calibrated to another. For this reason the article uses the latest submission and reports both base levels (Table 2); the CRT 2026 base also removes the need for a 2023 proxy, because it contains reported data for 2024.

### 4.3. Category 2.A.4.d as an inventory uncertainty

About one fifth of the avoided emissions in the main scenarios comes from 2.A.4.d, a residual of domestic limestone and dolomite sales with no identified end use. Applying cement-type factors to it assumes levers, such as clinker substitution or capture at kilns, that cannot be attached to unidentified consumers. The residual may also overlap with lime production (up to 19.5% of 2.A.4.d in 2024) and may include uses as aggregate or crushed stone, which the IPCC Guidelines treat as non-emissive (IPCC, 2006, Vol. 3, p. 2.36 and Table 2.7). The CRT 2026 activity data, which imply a factor above that of dolomite, add a further inconsistency. In the sensitivity analysis, the choice between f = 1.00 and the mineral-group factors for 2.A.4.d moves the 2050 reference by 3,397 kt CO2eq, more than the factor ranges of ferroalloys, ammonia or lime. Category 2.A.4.d should therefore be treated as an inventory question before it is treated as a mitigation option. Within mineral industry, cement clinker (2.A.1) accounted for 48.3% of 2.A emissions in 2024 and 2.A.4.d for 41.3% (CRT 2026). Measures limited to cement therefore cover less than half of the process emissions of mineral industry.

### 4.4. Ambition of the factors relative to the literature

The presented Moderate factors are consistent with the literature central values in 2050 (13,896 against 14,009 kt CO2eq at constant activity), but they assume earlier reductions than the literature supports in 2030 (19,418 against 21,036 kt CO2eq). The gap arises for levers that depend on CCS, inert anodes or new reduction routes, which are not expected in Kazakhstan before 2030; for the metals industries, CCS is not expected within 10–15 years (Holtz et al., 2025, p. 37). The Ambitious scenario in 2050 (7,236 kt CO2eq) lies close to the result of the literature low factors (7,169 kt CO2eq), that is, to the deepest intensity reductions found for every process at once. For ammonia, Khoyashov et al. (2024) identify ammonia production and natural gas processing as the lowest-cost CO2 capture options in Kazakhstan, which supports treating ammonia as an early candidate for capture, but the single ammonia plant has no planned CO2 storage infrastructure (Holtz et al., 2025, p. 41).

### 4.5. Factors versus activity growth

Under plausible growth assumptions, the 2050 outcome depends about 2.5–3 times more on the remaining-emissions factors than on activity growth. This supports the focus of the scenarios on process intensity. The conclusion has two limits. First, it reverses in the stress test, in which physical output grows at about 3% per year for 26 years; such growth is not supported by the official value-added forecast, but it shows that sustained industrial expansion could outweigh intensity improvements. Second, in 2030 growth matters more than the factors, because the factors change little before 2030 while the trend and the official forecast concentrate growth in 2025–2030.

### 4.6. Policy context

The scenarios do not assess compliance with national targets. Kazakhstan's updated NDC sets an economy-wide reduction of 15% (unconditional) and 25% (conditional) by 2030 relative to 1990 (Government of the Republic of Kazakhstan, 2023, p. 4), and the Strategy for achieving carbon neutrality by 2060 was approved in February 2023 (President of the Republic of Kazakhstan, 2023). In CRT 2026, IPPU emissions in 2024 are 43.1% above their 1990 level; the NDC target is set for the economy as a whole, and this study does not assess its achievement. The factors of this study are author assumptions tested against the literature; they are not taken from the NDC or the Strategy. Khussain et al. (2025) discuss reforms of Kazakhstan's emissions trading system that would support CCS in metallurgy and processing industries, one of the instruments relevant to the deeper factors.

### 4.7. Limitations

First, the boundary covers 85.6% of IPPU emissions in 2024 and excludes F-gases, which make up 12.0% of the total. Second, the factors are aggregate remaining-emissions multipliers by process; the model does not represent technologies, costs, capital turnover or plant retirement. Third, the literature basis is incomplete: for glass, zinc, calcium carbide and 2.A.4, no lever was found, and these branches (19.5% of the base) rest on author assumptions. Fourth, the growth variants depend on author mappings of sectors to processes, the official forecast refers to value added, and the trend is applied only to 2030. Fifth, the analysis relies on public inventory documentation and cannot audit confidential plant data; the 2.A.4.d activity data and the possible overlap with lime require clarification with the inventory compilers.

## 5. Conclusions

According to CRT 2026, Kazakhstan's IPPU emissions reached 25,789.9 kt CO2eq in 2024, 43.1% above 1990 and 234.7% above the 1996 minimum; the share of mineral industry rose to 35.8% and that of F-gases to 12.0%. The CRT 2026 recalculations lowered the series in every year, by 20.8% in 1990, mainly through sinter. Historical trends and model bases are therefore comparable only within the same submission.

At process level, national statistics and inventory activity data agree for clinker, lime, crude steel and total ferroalloys, whereas pig iron, zinc and aluminium require plant- or stream-level boundaries. Differences between the two sources should be interpreted only after the product and the boundary have been matched.

On the CRT 2026 inventory 2024 base of 22,088.3 kt CO2eq (85.6% of IPPU), the exploratory scenarios reduce included emissions to 19,418 and 13,896 kt CO2eq (Moderate) and to 16,072 and 7,236 kt CO2eq (Ambitious) in 2030 and 2050. Compared with literature-based factors, the presented factors front-load reductions before 2030, while the 2050 Moderate level is consistent with the literature central values (13,896 against 14,009 kt CO2eq). About one fifth of the avoided emissions comes from 2.A.4.d, a residual inventory estimate without an identified end use, which should be clarified with the inventory compilers before it is treated as a mitigation option. Under plausible growth, the remaining-emissions factors matter about 2.5–3 times more than activity growth in 2050; only sustained growth of physical output of about 3% per year reverses this.

Future work should replace the group factors with technology-explicit branches for clinker, iron and steel, ferroalloys and ammonia, add F-gases and link the process model to the Energy sector.

## Data availability

The data, parameters and scripts are in the project repository:
- parameters: `data/metadata/leap_scenario_parameters_crt2026.csv`, `leap_sensitivity_factors.csv`, `leap_growth_variants.csv`, `leap_2a4_variants.csv`, `scenario_levers_literature.csv`;
- LEAP import workbook: `outputs/leap_ippu_import/Kazakhstan_IPPU_LEAP_import_crt2026.xlsx`;
- results: `data/processed/*_crt2026.csv`;
- scripts: `scripts/extract_ippu_emissions.py`, `extract_crt_subcategory_emissions.py`, `build_leap_parameters.py`, `fill_leap_import_template.py`, `analyze_ippu_timeseries.py`, `analyze_leap_scenarios.py`, `analyze_leap_sensitivity.py` (option `--inventory crt2026`);
- sources with URLs and SHA-256: `data/metadata/source_registry.csv`.

## References

<!-- Reference style: APA 7th edition (no target journal selected yet). Source: docs/references.bib. -->

Aubakirova, G. M., Isataeva, F. M., Mazhitova, S. K., & Togaybaeva, L. I. (2023). Decarbonization of mining and steel sectors: Experience of Kazakhstan. *Bulletin of “Turan” University*, (4), 54–69. https://doi.org/10.46914/1562-2959-2023-1-4-54-69

Bashmakov, I. A., Nilsson, L. J., Acquaye, A., Bataille, C., Cullen, J. M., de la Rue du Can, S., Fischedick, M., Geng, Y., & Tanaka, K. (2022). Industry. In P. R. Shukla, J. Skea, R. Slade, A. Al Khourdajie, R. van Diemen, D. McCollum, M. Pathak, S. Some, P. Vyas, R. Fradera, M. Belkacemi, A. Hasija, G. Lisboa, S. Luz, & J. Malley (Eds.), *Climate change 2022: Mitigation of climate change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change* (pp. 1161–1244). Cambridge University Press. https://doi.org/10.1017/9781009157926.013

Bureau of National Statistics of the Republic of Kazakhstan. (2022–2026). *Industrial production statistics: Production of industrial products in physical terms* [Data set]. https://stat.gov.kz/ru/industries/business-statistics/stat-industrial-production/

Cassetti, G., Elia, A., Gargiulo, M., & Chiodi, A. (2023). Reinforcing the Paris Agreement: Ambitious scenarios for the decarbonisation of the Central Asian and Caspian region. *Renewable and Sustainable Energy Transition*, *3*, Article 100048. https://doi.org/10.1016/j.rset.2023.100048

Dang, W., Chen, S., He, B., Song, J., Duan, Z., Duan, H., & Gao, Z. (2026). Decarbonization and clean production in China's cement industry: Strategies from the LEAP-LCA perspective. *Environmental Impact Assessment Review*, *116*, Article 108124. https://doi.org/10.1016/j.eiar.2025.108124

De Miglio, R., & Bakdolotov, A. (2024). A “risk-induced” emission mitigation pathway for Kazakhstan. *Energy Strategy Reviews*, *52*, Article 101332. https://doi.org/10.1016/j.esr.2024.101332

Duan, H., Hou, C., Yang, W., & Song, J. (2022). Towards lower CO2 emissions in iron and steel production: Life cycle energy demand-LEAP based multi-stage and multi-technique simulation. *Sustainable Production and Consumption*, *32*, 270–281. https://doi.org/10.1016/j.spc.2022.04.028

European Commission. (2007). *Reference document on best available techniques for the manufacture of large volume inorganic chemicals – Ammonia, acids and fertilisers*. European IPPC Bureau, Joint Research Centre. https://eippcb.jrc.ec.europa.eu/sites/default/files/2019-11/lvic_aaf.pdf

European Lime Association. (2023). *A pathway to negative CO2 emissions by 2050: The contribution of the lime industry to a carbon-neutral Europe*. https://eula.eu/wp-content/uploads/2023/09/WEB_EULA-2030-Climate-Roadmap_Lime-Acts_A4_v19.pdf

Government of the Republic of Kazakhstan. (2023). *Updated nationally determined contribution of the Republic of Kazakhstan to the global response to climate change* (Approved by Decree of the Government of the Republic of Kazakhstan No. 313 of 19 April 2023; unofficial translation). Ministry of Ecology and Natural Resources of the Republic of Kazakhstan. https://unfccc.int/sites/default/files/NDC/2023-06/12updated%20NDC%20KAZ_Gov%20Decree313_19042023_en_cover%20page.pdf

Heaps, C. G. (2022). *LEAP: The Low Emissions Analysis Platform* (Version 2026.5.0.1) [Computer software]. Stockholm Environment Institute. https://leap.sei.org

Holtz, G., Jülich, A., Knoop, K., Leipprand, A., Acosta-Fernandez, J., Bilici, S., & Viebahn, P. (2025). *Providing a knowledge base for decarbonizing the Kazakh metals industries (DeKaMe): Final report*. Wuppertal Institute; Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ). https://www.giz.de/en/downloads/giz2025-en-knowledge-base-for-decarbonizing-the-kazakh-metals-industries.pdf

IEA. (2020). *Iron and steel technology roadmap: Towards more sustainable steelmaking*. OECD Publishing. https://doi.org/10.1787/3dcc2a1b-en

IEA. (2021). *Ammonia technology roadmap: Towards more sustainable nitrogen fertiliser production*. OECD Publishing. https://doi.org/10.1787/f6daa4a0-en

IEA. (2023). *Net zero roadmap: A global pathway to keep the 1.5 °C goal in reach (2023 update)*. https://iea.blob.core.windows.net/assets/9a698da4-4002-4e53-8ef3-631d8971bf84/NetZeroRoadmap_AGlobalPathwaytoKeepthe1.5CGoalinReach-2023Update.pdf

IEA, & Cement Sustainability Initiative. (2018). *Technology roadmap: Low-carbon transition in the cement industry*. OECD Publishing. https://doi.org/10.1787/9789264300248-en

IPCC. (2006). *2006 IPCC guidelines for national greenhouse gas inventories: Vol. 3. Industrial processes and product use* (H. S. Eggleston, L. Buendia, K. Miwa, T. Ngara, & K. Tanabe, Eds.). Institute for Global Environmental Strategies. https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol3.html

IPCC. (2019). *2019 refinement to the 2006 IPCC guidelines for national greenhouse gas inventories: Vol. 3. Industrial processes and product use* (E. Calvo Buendia, K. Tanabe, A. Kranjc, J. Baasansuren, M. Fukuda, S. Ngarize, A. Osako, Y. Pyrozhenko, P. Shermanau, & S. Federici, Eds.). https://www.ipcc-nggip.iges.or.jp/public/2019rf/vol3.html

Jayakumari, S., Canaguier, V., Dalaker, H., Van der Eijk, C., & Ksiazek, M. (2026). Developing optimized agglomerates for silicon and ferroalloys industries. In M. Tangstad, H. Rong, A. Valderhaug, B. Andresen, H. Dalaker, & I. G. Page (Eds.), *Silicon for the chemical and solar industry XVIII*. Fagbokforlaget. https://doi.org/10.55669/oa900823

Khamzina, A., Samuratov, T., Omirgaliyev, R., Aldongarov, A., & Zhakiyev, N. (2026). Green cement production technology for reducing GHG emissions from the industrial sector of Kazakhstan. *Future Technology*, *5*(3), 295–308. https://doi.org/10.55670/fpll.futech.5.3.26

Khoyashov, N., Serik, G., Togay, A., Abuov, Y., Alibekov, A., & Lee, W. (2024). Development of carbon capture and storage (CCS) hubs in Kazakhstan. *International Journal of Greenhouse Gas Control*, *138*, Article 104259. https://doi.org/10.1016/j.ijggc.2024.104259

Khussain, B., Zhumatay, N., Kenessary, A., & Mussin, R. (2025). Enhancing the emissions trading system for Kazakhstan's decarbonization. *Sustainability*, *17*(16), Article 7195. https://doi.org/10.3390/su17167195

Menzies, C., Qader, A., & Bologa, A. (2024). *White paper: Decarbonization of the metallurgical sector of Kazakhstan*. Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ). https://www.giz.de/en/downloads/giz2024-en-white-paper-on-decarbonization-of-the-metallurgical-sector-of-kazakhstan.pdf

Ministry of National Economy of the Republic of Kazakhstan. (2024). *Prognoz sotsial'no-ekonomicheskogo razvitiia Respubliki Kazakhstan na 2025–2029 gody (vtoroi etap)* [Socio-economic development forecast of the Republic of Kazakhstan for 2025–2029 (second stage)]. https://www.gov.kz/uploads/2024/9/3/725c4559658fbe7f7712bc00719dd1da_original.631162.pdf

Müller, A., Harpprecht, C., Sacchi, R., Maes, B., van Sluisveld, M., Daioglou, V., Šavija, B., & Steubing, B. (2024). Decarbonizing the cement industry: Findings from coupling prospective life cycle assessment of clinker with integrated assessment model scenarios. *Journal of Cleaner Production*, *450*, Article 141884. https://doi.org/10.1016/j.jclepro.2024.141884

Myhre, G., Shindell, D., Bréon, F.-M., Collins, W., Fuglestvedt, J., Huang, J., Koch, D., Lamarque, J.-F., Lee, D., Mendoza, B., Nakajima, T., Robock, A., Stephens, G., Takemura, T., & Zhang, H. (2013). Anthropogenic and natural radiative forcing. In T. F. Stocker, D. Qin, G.-K. Plattner, M. Tignor, S. K. Allen, J. Boschung, A. Nauels, Y. Xia, V. Bex, & P. M. Midgley (Eds.), *Climate change 2013: The physical science basis. Contribution of Working Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change* (pp. 659–740). Cambridge University Press. https://doi.org/10.1017/CBO9781107415324.018

Obrist, M. D., Kannan, R., Schmidt, T. J., & Kober, T. (2021). Decarbonization pathways of the Swiss cement industry towards net zero emissions. *Journal of Cleaner Production*, *288*, Article 125413. https://doi.org/10.1016/j.jclepro.2020.125413

President of the Republic of Kazakhstan. (2023). *Strategy of the Republic of Kazakhstan on achieving carbon neutrality by 2060* (Approved by Decree of the President of the Republic of Kazakhstan No. 121 of 2 February 2023; unofficial translation). https://unfccc.int/sites/default/files/resource/Carbon_Neutrlaity_Strategy_Kazakhstan_Eng_Oct2024.pdf

Radovanović, M., Filipović, S., & Andrejević Panić, A. (2021). Sustainable energy transition in Central Asia: Status and challenges. *Energy, Sustainability and Society*, *11*(1), Article 49. https://doi.org/10.1186/s13705-021-00324-2

Republic of Kazakhstan. (2025a). *Kazakhstan. 2025 common reporting tables (CRT), 1990–2023* (Version KAZ-CRT-2025-V1.0) [Data set]. UNFCCC. https://unfccc.int/reports

Republic of Kazakhstan. (2025b). *Natsional'nyi dokument ob inventarizatsii parnikovykh gazov 1990–2023 gg.* [National inventory document, 1990–2023]. UNFCCC. https://unfccc.int/documents/646542

Republic of Kazakhstan. (2026a). *Kazakhstan. 2026 common reporting tables (CRT), 1990–2024* (Version KAZ-CRT-2026-V1.0) [Data set]. UNFCCC. https://unfccc.int/documents/656739

Republic of Kazakhstan. (2026b). *Natsional'nyi dokument ob inventarizatsii parnikovykh gazov za 1990–2024 gody* [National inventory document, 1990–2024]. UNFCCC. https://unfccc.int/documents/656738

Tan, C., Yu, X., & Guan, Y. (2022). A technology-driven pathway to net-zero carbon emissions for China's cement industry. *Applied Energy*, *325*, Article 119804. https://doi.org/10.1016/j.apenergy.2022.119804

Tautorat, P., Lalin, B., Schmidt, T. S., & Steffen, B. (2023). Directions of innovation for the decarbonization of cement and steel production – A topic modeling-based analysis. *Journal of Cleaner Production*, *407*, Article 137055. https://doi.org/10.1016/j.jclepro.2023.137055

UNFCCC. (2019). *Decision 18/CMA.1: Modalities, procedures and guidelines for the transparency framework for action and support referred to in Article 13 of the Paris Agreement* (FCCC/PA/CMA/2018/3/Add.2, pp. 18–52). https://unfccc.int/sites/default/files/resource/CMA2018_03a02E.pdf

Wan, F., & Li, J. (2024). Exploring hydrogen metallurgy to CO2 emissions reduction in China's iron and steel production: An analysis based on the life cycle CO2 emissions – LEAP model. *Energy Reports*, *11*, 4552–4563. https://doi.org/10.1016/j.egyr.2024.04.028

Zhakiyev, N., Khamzina, A., Toimbek, D., Omirgaliyev, R., Shakib Kotamjani, S., Alhuyi Nazari, M., & Salem, M. (2025). Energy systems, CO2 emissions, and mitigation policies in three Central Asian countries: A comprehensive review. *Energy Strategy Reviews*, *62*, Article 101883. https://doi.org/10.1016/j.esr.2025.101883

Zhakiyev, N., Khamzina, A., Zhakiyeva, S., De Miglio, R., Bakdolotov, A., & Cosmi, C. (2023). Optimization modelling of the decarbonization scenario of the total energy system of Kazakhstan until 2060. *Energies*, *16*(13), Article 5142. https://doi.org/10.3390/en16135142

Zhakiyev, N. K., Kayisli, K., Kushekkaliyev, A., Sagadatova, N., & Biloshchytskyi, A. (2025). Forecasting of GHG emissions from energy and industrial sectors of Kazakhstan and assessment of mitigation scenarios with high share of renewables. *International Journal of Renewable Energy Research*, *15*(2), 300–309. https://doi.org/10.20508/ijrer.v15i2.15837.g9052
