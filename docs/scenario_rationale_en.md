# Rationale for exploratory mitigation scenarios

Русская версия: [scenario_rationale.md](scenario_rationale.md).

## Purpose

This note documents how the three LEAP pathways are interpreted in the article. It prevents an important overstatement: the remaining-emissions factors entered in LEAP are **analytical scenario envelopes**, not estimates of the standalone potential of an individual technology, official targets of the Government of Kazakhstan, or a least-cost optimisation result.

The available Kazakhstan inventory data are sufficient to construct a transparent 2024 process-emissions baseline and to test the consequences of alternative reduction depths. They are not sufficient to estimate plant-level technology shares, investment schedules, abatement costs, or rates of technology adoption. The scenario design therefore uses broad process groups and represents the joint effect of a portfolio of measures through the `Non Energy Effect Loading` multiplier. The model is documented in the [scenario protocol](leap_scenarios_2023_2050_en.md).

## Evidence base and interpretation rule

The measure portfolios follow the direction of the international industrial-decarbonisation literature. For cement and other mineral processes, the relevant portfolio includes lower clinker content and alternative binders/materials, process improvements and, for residual calcination emissions, carbon capture. For iron and steel and ferroalloys, it includes material efficiency, scrap-based production where applicable, changes in reduction routes including hydrogen-based direct reduction, and carbon capture for remaining process routes. For chemical processes, it includes process optimisation, nitric-acid N2O abatement, lower-carbon hydrogen/feedstock routes and capture or abatement of residual emissions.

These mechanisms justify examining progressively deeper reductions; they do **not** empirically validate one percentage for Kazakhstan. The International Energy Agency identifies clinker substitution and carbon capture among the core levers for low-carbon cement, and resource efficiency, scrap/electric-arc-furnace routes, hydrogen-based direct reduction and CCUS among the portfolios for iron and steel. Kazakhstan's published 2060 carbon-neutrality policy direction provides national context, but it does not specify the process-group percentages used here. The numerical factors are consequently author-selected sensitivity assumptions, stated completely below.

## Scenario definitions

All branches start from their corrected 2024 Current Accounts value (2024 base year, 2023 inventory proxy). `Baseline` keeps those values constant. In the two mitigation cases, LEAP linearly interpolates to the remaining-emissions factors in 2030 and 2050. A factor of 85%, for example, means a 15% reduction relative to the 2024 branch value; it does not mean that a single technology reduces emissions by 15%.

| Process group | Moderate mitigation: 2030 / 2050 remaining emissions | Ambitious mitigation: 2030 / 2050 remaining emissions | Interpretation of the range |
|---|---:|---:|---|
| Mineral industry: cement, lime, glass and other carbonates | 85% / 60% | 70% / 30% | Moderate combines gradual material and process improvements; ambitious represents a deeper portfolio of clinker/material substitution and capture of residual calcination emissions. |
| Metal industry: pig iron, steel, sinter, pellets, ferroalloys, aluminium CO2 and zinc | 90% / 65% | 75% / 35% | Moderate represents incremental efficiency, reductant/burden improvements and feasible circular-material measures. Ambitious represents much wider deployment of scrap/EAF routes where applicable, low-carbon reduction routes and/or capture for residual process emissions. |
| Chemical industry: ammonia, nitric acid N2O and calcium carbide | 90% / 65% | 70% / 30% | Moderate represents optimisation and partial abatement, including nitric-acid N2O controls. Ambitious represents deep route change and high abatement/capture of residual emissions. |

The differing factors across groups are a deliberate sensitivity design. Mineral and chemical branches are assigned greater late-period reduction in the ambitious case because their narrative includes residual-process-emission capture or abatement. This is a modelling assumption, not a claim that these branches are easier to decarbonise than metals in Kazakhstan.

## Translation from measures to LEAP variables

The current model is a process-emissions sensitivity model, not a technology-stock model. It does not create separate branches for calcined clay, electric arc furnaces, hydrogen direct reduction, carbon capture units or nitric-acid abatement equipment. Instead, each portfolio is represented as an exogenous remaining-emissions factor:

`Interp(2024, base, 2030, base × f2030, 2050, base × f2050)`.

Accordingly, the outputs answer a bounded question: **given a constant 2024 activity basis and the stated aggregate remaining-emissions factors, what are the resulting LEAP process-emissions trajectories?** They do not answer how much each measure contributes, how much it costs, or whether it will be deployed by a particular enterprise.

## Claims that are and are not supported

Supported wording:

> The Moderate and Ambitious cases are exploratory, portfolio-based sensitivity pathways. Their group-specific remaining-emissions factors represent progressively deeper combinations of recognised industrial decarbonisation measures and are not technology-specific forecasts or national targets.

Not supported by the present evidence:

- that Kazakhstan has adopted the 2030 or 2050 percentages in this model;
- that one named technology produces the full reduction assigned to a group;
- that the scenarios are least-cost, economically feasible or compatible with a given plant-investment schedule;
- that the results cover F-gases, aluminium PFCs, other excluded IPPU sources or industrial fuel combustion.

Limitation: About one fifth of the avoided emissions in Moderate and Ambitious (19.5–23.3% in 2030 and 2050) comes from 2.A.4.d, use of limestone and dolomite, for which no specific abatement lever is identified (see the [NID/NIR review](process_methodology_review_en.md)). Their 2030 multipliers assume more reduction than the literature found supports for lime, aluminium and ammonia (both scenarios) and for cement clinker and, marginally, iron and steel (Ambitious); the 2050 Ambitious factor for ferroalloys is deeper than the only quantified source supports (see [Literature basis for the factors](#literature-basis-for-the-factors)). The presented figures are not changed.

## Literature basis for the factors

This section, added on 18 October 2026, tests the factors against published pathways and proposes low, central and high values for additional sensitivity runs. The presented Baseline, Moderate and Ambitious scenarios remain unchanged. The extracted values, with page or table, DOI or URL and applicability to Kazakhstan, are in [`scenario_levers_literature.csv`](../data/metadata/scenario_levers_literature.csv) (entries L01–L36). The proposed factors and the basis of each central value are in [`leap_sensitivity_factors.csv`](../data/metadata/leap_sensitivity_factors.csv).

**Conversion rule.** A factor f multiplies a branch's emissions at constant activity, so it is an intensity multiplier. Literature values were converted as follows:
- intensity: f = value / base value;
- share of near-zero emission production: f = 1 − share;
- percentage reduction: f = 1 − reduction;
- clinker: f = (clinker ratio / initial ratio) × (1 − near-zero share).

**Low, central and high.**
- **Low** is the deepest reduction in branch intensity that the literature supports. Values that include reduced demand are not used, because activity is modelled separately in stage 3.
- **Central** is a reference scenario where one exists: the national carbon-neutrality scenario for iron and steel and for aluminium (GIZ 2024), IEA SDS for ammonia, IEA 2018 2DS for cement clinker, and the upper EU BAT level for nitric acid. Otherwise it is the midpoint of low and high, marked "midpoint (no reference)" in the CSV.
- **High** is the least ambitious evidence or a documented Kazakhstan constraint. The CCS constraint (not expected within 10–15 years, i.e. roughly until 2040; Wuppertal Institut / GIZ 2025, p.37) is applied in full only to 2030. Each high value for 2050 is justified separately in the CSV.

| Basis of the central value | 2030: processes (share of the 23,551.9 kt base) | 2050: processes (share of base) |
|---|---|---|
| Reference scenario | 6 (59.7%) | 8 (61.7%) |
| Midpoint (no reference) | 5 (19.7%) | 3 (17.6%) |
| Author assumption (no literature) | 5 (20.7%) | 5 (20.7%) |

| Process | Main levers | f 2030 low / central / high | f 2050 low / central / high | Sources: low; central; high | Current Moderate; Ambitious (2030/2050) | Assessment |
|---|---|---|---|---|---|---|
| Cement clinker (2.A.1) | clinker substitution; CCUS of calcination CO2 | 0.84 / 0.97 / 1.00 | 0.06 / 0.71 / 0.85 | IEA NZE 2023, p.96 (derived); IEA 2018 2DS, Table 2; 2030: Kazakhstan clinker ratio 0.67 and no CCS before ~2040; 2050: ratio 0.60 and 5% early-stage CCS (author assumption) | 0.85/0.60; 0.70/0.30 | Ambitious 2030 below the range |
| Lime (2.A.2) | CCUS, the only lever for process CO2 | 0.90 / 0.95 / 1.00 | 0.10 / 0.53 / 0.95 | EuLA 2023, pp.18–19; midpoint (no reference); 2030: no CCS before ~2040; 2050: 5% early-stage CCS (author assumption) | 0.85/0.60; 0.70/0.30 | Both 2030 values below the range |
| 2.A.4.a+b and 2.A.4.d | не найдено / not found | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | author assumption (decision of 18 October 2026) | 0.85/0.60; 0.70/0.30 | For 2.A.4.d: lower bound s = 0.84; alternative variant with mineral-group factors |
| Pig iron, steel, sinter, pellets (2.C.1) | efficiency (coke is in IPPU), natural-gas and H2 DRI, CCS, scrap | 0.79 / 1.00 / 1.00 | 0.11 / 0.38 / 0.83 | IEA 2020 intensity without demand effect: SDS 2030 read from a chart (p.73) and Faster Innovation 2050 (p.97); national carbon-neutrality scenario (GIZ 2024, pp.17, 49), linear 2030–2060; 2030: no CCS before ~2040; 2050: natural-gas DRI only, 1.0 vs 1.2 t CO2/t (IEA 2020, p.43) | 0.90/0.65; 0.75/0.35 | Ambitious 2030 marginally below the range (the low value is read from a chart) |
| Ferroalloys (2.C.2) | biocarbon reductants | 0.60 / 0.80 / 1.00 | 0.50 / 0.75 / 1.00 | Norwegian industry target −40% to −50% (Jayakumari et al. 2026, p.2), not deeper; midpoint (no reference); low biomass potential in Kazakhstan (Wuppertal Institut / GIZ 2025, p.35) | 0.90/0.65; 0.75/0.35 | Ambitious 2050 below the range; applicability weak |
| Aluminium (2.C.3) | inert anodes | 0.93 / 1.00 / 1.00 | 0.04 / 0.73 / 0.99 | IEA NZE 2023, p.95; national carbon-neutrality scenario, −40% vs 2017 by 2060 at the same output (GIZ 2024, pp.17, 49), linear 2030–2060; national baseline, −1% by 2060 | 0.90/0.65; 0.75/0.35 | Both 2030 values below the range |
| Ammonia (2.B.1) | CCUS on the concentrated feedstock CO2 stream; electrolytic hydrogen | 0.97 / 0.99 / 1.00 | 0.05 / 0.30 / 1.00 | IEA 2021 NZE, p.10; midpoint (2030) and IEA 2021 SDS, p.10 (2050); a single plant without planned CO2 storage infrastructure (Wuppertal Institut / GIZ 2025, p.41) | 0.90/0.65; 0.70/0.30 | Both 2030 values below the range |
| Nitric acid (2.B.2) | De-N2O in the reactor or tail gas, NSCR | 0.02 / 0.51 / 1.00 | 0.02 / 0.37 / 1.00 | lower BAT level 0.12 kg/t vs 5.0 kg/t in Kazakhstan (LVIC-AAF BREF, Table 3.14, p.140; NID 2025, p.175); midpoint (2030) and upper BAT level for existing plants, 1.85 kg/t (2050); no abatement reported or planned (NID 2025, pp.175–176) | 0.90/0.65; 0.70/0.30 | Within the range; Moderate 2050 (0.65) is less ambitious than the BAT reference (0.37) |
| Glass, zinc, calcium carbide | не найдено / not searched | Ambitious / Moderate / 1.00 | Ambitious / Moderate / 1.00 | author assumption | as in the current scenarios | — |

Main findings:

1. **2030.** Current factors assume more reduction than the literature supports for lime, aluminium and ammonia in both scenarios, and for cement clinker and, marginally, iron and steel in Ambitious. These levers depend on CCS, inert anodes or new reduction routes, which are not expected in Kazakhstan before 2030.
2. **2050.** Apart from 2.A.4, only the Ambitious factor for ferroalloys (0.35) lies outside the range: it is deeper than the only quantified source supports (0.50). Compared with the reference values, Moderate is more ambitious for cement clinker (0.60 vs 0.71) and aluminium (0.65 vs 0.73), and less ambitious for iron and steel (0.65 vs 0.38), ammonia (0.65 vs 0.30) and nitric acid (0.65 vs 0.37).
3. **For the Discussion.** On the CRT 2026 inventory 2024 base at constant activity, the reference-based central factors give 14,009 kt CO2eq in 2050, close to the main Moderate scenario (13,896 kt), but 21,036 kt in 2030, above Moderate (19,418 kt). The presented factors therefore assume earlier reductions than the literature supports, while their 2050 Moderate level is consistent with it; the same pattern held on the CRT 2025 proxy base. About one fifth of the avoided emissions in the main Moderate and Ambitious scenarios (18.0–21.4% in 2030 and 2050) comes from 2.A.4.d, use of limestone and dolomite, for which no specific abatement lever is identified. Values are in [`leap_ippu_sensitivity_summary_2030_2050_crt2026.csv`](../data/processed/leap_ippu_sensitivity_summary_2030_2050_crt2026.csv) (growth variant "zero") and [`leap_ippu_2a4d_share_of_avoided_crt2026.csv`](../data/processed/leap_ippu_2a4d_share_of_avoided_crt2026.csv).
4. **Factors versus growth.** Under the plausible growth variants (zero, trend to 2030, official 2025–2029 forecast, 1.5% per year to 2050), the factors matter about two and a half to three times more than activity growth in 2050. Only a stress test, in which physical output grows at half the official sector rates (about 3% per year) until 2050, makes growth more important than the factors. In 2030 growth matters more in every variant (see [Factors versus growth](leap_scenarios_2023_2050_en.md#factors-versus-growth)).

## Sources used for the scenario narratives

1. International Energy Agency (IEA) and Cement Sustainability Initiative. *Technology Roadmap: Low-Carbon Transition in the Cement Industry* (2018). OECD Publishing / IEA, Paris. [https://doi.org/10.1787/9789264300248-en](https://doi.org/10.1787/9789264300248-en).
2. International Energy Agency (IEA). *Iron and Steel Technology Roadmap: Towards More Sustainable Steelmaking* (2020). OECD Publishing / IEA, Paris. [https://doi.org/10.1787/3dcc2a1b-en](https://doi.org/10.1787/3dcc2a1b-en).
3. President of the Republic of Kazakhstan. *Strategy of the Republic of Kazakhstan on Achieving Carbon Neutrality by 2060*, approved by Presidential Decree No. 121 of 2 February 2023 (policy context). Official text: [Adilet, U2300000121](https://adilet.zan.kz/rus/docs/U2300000121); Russian text and unofficial English translation hosted by the UNFCCC: [RU](https://unfccc.int/sites/default/files/resource/Carbon_Neutrlaity_Strategy__Kazakhstan_Ru_Oct2024.pdf), [EN](https://unfccc.int/sites/default/files/resource/Carbon_Neutrlaity_Strategy_Kazakhstan_Eng_Oct2024.pdf). This replaces the earlier link to a Ministry of National Economy notice on the draft.
4. IPCC. *2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 3: Industrial Processes and Product Use* (2006), and *2019 Refinement to the 2006 IPCC Guidelines*, Volume 3. These are the methodological references for the included source categories and gases.
5. Tan, C., Yu, X., & Guan, Y. (2022). *A technology-driven pathway to net-zero carbon emissions for China's cement industry*; Duan, H. et al. (2022). *Towards lower CO2 emissions in iron and steel production: Life cycle energy demand-LEAP based multi-stage and multi-technique simulation*; and the other reviewed studies in the project's [literature review](literature_review_en.md). These sources inform model architecture and the distinction between technology detail and aggregate scenarios; their parameters are not transferred to Kazakhstan.

Full bibliographic records of these and all other sources, including the literature basis for the factors, are in [references.bib](references.bib); the check log is in [references_check.csv](../data/metadata/references_check.csv).

## Next modelling increment

A future technology-explicit version should replace group multipliers with activity, technology-share and emission-factor trajectories for individual processes. It would require, at minimum, national clinker-to-cement ratios; route-specific steel, ferroalloy and aluminium production; scrap and reductant use; plant-level information on nitric-acid N2O controls; and evidence on capture, fuel and electricity availability. Until those inputs are available, the present factor-based design is the most transparent representation of uncertainty.
