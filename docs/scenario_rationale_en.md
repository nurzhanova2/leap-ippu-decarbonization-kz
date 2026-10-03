# Rationale for exploratory mitigation scenarios

Русская версия: [scenario_rationale.md](scenario_rationale.md).

## Purpose

This note documents how the three LEAP pathways are interpreted in the article. It prevents an important overstatement: the remaining-emissions factors entered in LEAP are **analytical scenario envelopes**, not estimates of the standalone potential of an individual technology, official targets of the Government of Kazakhstan, or a least-cost optimisation result.

The available Kazakhstan inventory data are sufficient to construct a transparent 2024 process-emissions baseline and to test the consequences of alternative reduction depths. They are not sufficient to estimate plant-level technology shares, investment schedules, abatement costs, or rates of technology adoption. The scenario design therefore uses broad process groups and represents the joint effect of a portfolio of measures through the `Non Energy Effect Loading` multiplier. The model is documented in the [scenario protocol](leap_scenarios_2023_2050_en.md).

## Evidence base and interpretation rule

The measure portfolios follow the direction of the international industrial-decarbonisation literature. For cement and other mineral processes, the relevant portfolio includes lower clinker content and alternative binders/materials, process improvements and, for residual calcination emissions, carbon capture. For iron and steel and ferroalloys, it includes material efficiency, scrap-based production where applicable, changes in reduction routes including hydrogen-based direct reduction, and carbon capture for remaining process routes. For chemical processes, it includes process optimisation, nitric-acid N2O abatement, lower-carbon hydrogen/feedstock routes and capture or abatement of residual emissions.

These mechanisms justify examining progressively deeper reductions; they do **not** empirically validate one percentage for Kazakhstan. The International Energy Agency identifies clinker substitution and carbon capture among the core levers for low-carbon cement, and resource efficiency, scrap/electric-arc-furnace routes, hydrogen-based direct reduction and CCUS among the portfolios for iron and steel. Kazakhstan's published 2060 carbon-neutrality policy direction provides national context, but it does not specify the process-group percentages used here. The numerical factors are consequently author-selected sensitivity assumptions, stated completely below.

## Scenario definitions

All branches are calibrated to their corrected 2024 LEAP value. `Baseline` keeps those values constant. In the two mitigation cases, LEAP linearly interpolates to the remaining-emissions factors in 2030 and 2050. A factor of 85%, for example, means a 15% reduction relative to the 2024 branch value; it does not mean that a single technology reduces emissions by 15%.

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

## Sources used for the scenario narratives

1. International Energy Agency (IEA). *Technology Roadmap: Low-Carbon Transition in the Cement Industry* (2018). [Report page](https://www.iea.org/reports/technology-roadmap-low-carbon-transition-in-the-cement-industry).
2. International Energy Agency (IEA). *Iron and Steel Technology Roadmap* (2020). [Report page](https://www.iea.org/reports/iron-and-steel-technology-roadmap).
3. Government of Kazakhstan, Ministry of National Economy. *Draft Strategy for Achieving Carbon Neutrality of the Republic of Kazakhstan until 2060* (policy context; Russian). [Official notice](https://www.gov.kz/memleket/entities/economy/press/news/details/466462?lang=ru).
4. IPCC. *2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 3: Industrial Processes and Product Use* (2006), and *2019 Refinement to the 2006 IPCC Guidelines*, Volume 3. These are the methodological references for the included source categories and gases.
5. Tan, X. et al. (2022). *A technology-driven pathway to net-zero carbon emissions for China's cement industry*; Duan et al. (2022). *Towards lower CO2 emissions in iron and steel production: Life cycle energy demand-LEAP based multi-stage and multi-technique simulation*; and the other reviewed studies in the project's [literature review](literature_review_en.md). These sources inform model architecture and the distinction between technology detail and aggregate scenarios; their parameters are not transferred to Kazakhstan.

## Next modelling increment

A future technology-explicit version should replace group multipliers with activity, technology-share and emission-factor trajectories for individual processes. It would require, at minimum, national clinker-to-cement ratios; route-specific steel, ferroalloy and aluminium production; scrap and reductant use; plant-level information on nitric-acid N2O controls; and evidence on capture, fuel and electricity availability. Until those inputs are available, the present factor-based design is the most transparent representation of uncertainty.
