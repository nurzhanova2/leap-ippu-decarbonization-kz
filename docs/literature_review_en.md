# Literature review: IPPU, decarbonisation and LEAP modelling

Русская версия: [literature_review.md](literature_review.md).

## Purpose

This review positions **LEAP-Based modeling of Decarbonization pathways in the IPPU sector of Kazakhstan** at the intersection of: (i) Kazakhstan and Central Asian decarbonisation scenarios, (ii) bottom-up LEAP modelling of heavy industry, and (iii) analyses of process-related emissions from cement and metallurgy. It draws on the 15 studies supplied by the authors; links are provided in the reference list.

## 1. Kazakhstan and Central Asia: existing modelling is primarily energy-system focused

Zhakiyev et al. (2023) is a key predecessor: it uses a TIMES optimisation model to assess a Kazakhstan carbon-neutrality scenario to 2060, considering system-wide energy, technology and investment change. De Miglio and Bakdolotov (2024), De Miglio et al. (2023), and Zhakiyev et al. (2025a) likewise assess mitigation pathways for Kazakhstan or the wider Central Asian and Caspian region. Taken together, these studies establish the need for scenario analysis to meet national climate targets and identify roles for electrification, renewables, hydrogen and energy efficiency.

Their scale, however, is the national energy system, a regional system, or an aggregated industrial sector. This is essential for assessing cross-sector trade-offs, but it does not identify the physical activity data and technological boundaries of individual IPPU processes. In particular, integrated energy models do not determine which production indicator should represent clinker, lime, pig iron, steel, ferroalloys, aluminium, or a technologically narrow zinc stream. This matters in Kazakhstan because national statistics and inventory data can refer to different products or plant boundaries.

The regional literature reinforces the point. Radovanović et al. (2021) and Zhakiyev et al. (2025b) link Central Asia’s transition to carbon-intensive infrastructure, fossil-fuel dependence, and investment and institutional barriers. These studies provide essential context but do not substitute for a process-level IPPU inventory. The present research therefore complements macro- and energy-system literature from the bottom up by establishing verifiable inputs for sectoral modelling.

## 2. LEAP as a technology-rich framework for industrial modelling

LEAP literature demonstrates the value of bottom-up industrial representation. Tan et al. (2022) use G-LEAP to examine a technology-driven net-zero pathway for China’s cement industry, linking product demand, technology change and emissions. Dang et al. (2026) extend this logic by combining LEAP with LCA to examine cleaner cement production, including clinker-calcination emissions and BAU/mitigation scenarios.

For metallurgy, Duan et al. (2022) apply a LEAP-based multi-stage simulation of iron and steel with life-cycle and alternative-technology considerations. The 2024 hydrogen-metallurgy study uses LEAP to compare conventional and hydrogen-based steel pathways. The 2024 LEAP-China study illustrates how long-term sectoral scenarios can be built consistently around alternative demand, technology and policy trajectories.

These studies provide methodological precedents, not a ready-to-transfer parameter set for Kazakhstan. Transferability is constrained by differences in industrial structure, scrap availability, alloy mix, reductant sources, production lines and statistical definitions. A Kazakhstan LEAP application must therefore begin with harmonised baseline activity data and calibration against the official inventory, rather than with a generic technology menu.

## 3. Process emissions and the limits of aggregated scenarios

Research on cement and steel shows that deep industrial decarbonisation is not reducible to electricity decarbonisation. Müller et al. (2024) couple prospective clinker LCA with IAM scenarios and demonstrate the relevance of process emissions for cement pathways. Obrist et al. (2021) examine technology-rich net-zero pathways for cement, including efficiency, process emissions and CO2 capture. Tautorat et al. (2023) map innovation directions for cement and steel and show why deep mitigation requires a portfolio beyond efficiency alone.

The 2022 sub-sectoral integrated-modelling study of Chinese industry similarly indicates that cement, steel and chemicals require distinct technological representation, including hydrogen and CCS. Together, this literature supports a process-level IPPU boundary. In Kazakhstan, it implies that cement should be represented through clinker and metallurgy through the specific technological flows that determine process emissions, rather than through a single aggregate output.

## 4. Research gap

Two complementary bodies of work have not yet been connected. The first models Kazakhstan decarbonisation pathways at energy-system or regional scale. The second provides technology-rich LEAP approaches to cement and steel, largely for China and Europe. Missing is a transparent and reproducible process-level basis for Kazakhstan that simultaneously:

1. uses official UNFCCC IPCC Sector 2 (IPPU) series;
2. tests their comparability with BNS production statistics;
3. distinguishes national output, plant-level data and technologically narrow streams; and
4. can be operationalised as activity-data branches in a bottom-up LEAP model.

This study fills that gap. It does not assume that a numerical BNS–UNFCCC difference automatically indicates poor data quality. Rather, the historical analysis shows that large apparent differences can arise when different products and boundaries are compared: Portland cement against clinker, or total raw zinc against zinc from Waelz cakes. The contribution is therefore not only a new historical series but also a harmonisation protocol required for credible bottom-up modelling.

## 5. Conceptual framework: from inventory to scenario model

Three analytical levels should be distinguished. The first is the national inventory: it answers how much emission is allocated to IPPU categories in each inventory year. The second is activity data: physical product output, reductant consumption, enterprise information, or a technological stream used to calculate the inventory. The third is the scenario model: it transforms a reconciled base year into alternative trajectories of demand, technology, emission factors and policy measures.

Most Kazakhstan-focused studies operate principally at the first and third levels, linking national targets to the development of the energy system. LEAP studies of cement and steel demonstrate the second and third levels, but usually assume that the underlying technological data are already consistent. That assumption cannot be automatically transferred to Kazakhstan. For several IPPU processes, published production statistics measure national gross output while inventory calculations use a single-plant dataset or only a part of a technological stream. Without an explicit bridge between inventory and activity data, a scenario model can be internally consistent yet miscalibrated against national reporting.

The study’s logic is therefore sequential: (1) reconstruct historical dynamics from UNFCCC data; (2) determine which BNS and UNFCCC indicators describe the same physical activity; (3) document uncertainty and non-comparable boundaries; and (4) use only harmonised indicators as LEAP inputs. This sequence distinguishes the research from simply transferring technology scenarios from another country.

## 6. Critical comparison of approaches

National TIMES studies are strong in assessing system interactions: how electricity supply, hydrogen, fuel prices, demand and investment shape national pathways. Their limitation for IPPU is the aggregation of processes in which a material share of emissions is determined not by energy consumption but by chemical transformation of raw materials or the carbon balance of reductants. Lower electricity carbon intensity does not automatically eliminate limestone-calcination emissions in clinker manufacture, anode-carbon emissions in aluminium production, or reductant-related emissions in metallurgy.

Technology-rich LEAP studies can instead identify the contribution of specific measures: lower clinker-to-cement ratios, material substitution, greater scrap use, changes in steelmaking routes, lower anode effects, CCS, or hydrogen. Yet they often rely on industrial systems with different technological structures and more detailed statistics. Chinese cement and steel studies are highly relevant examples of model architecture and scenario design, but their parameters cannot be used as empirical estimates for Kazakhstan without national adaptation.

Studies coupling LCA and IAM occupy an intermediate position: they emphasise life-cycle completeness and long-term system constraints. For this study, this means that a future LEAP model should remain compatible with wider national scenarios, while its IPPU base must retain process specificity. Aggregated national models define scenario boundary conditions; process-level LEAP determines how those conditions translate into emissions from individual industrial processes.

## 7. Theoretical and empirical expectations

The literature review supports four expectations that guide the analysis.

1. Kazakhstan’s IPPU trend should reflect the 1990s transition decline and the subsequent recovery of heavy industry, but recovery will be uneven across categories.
2. The largest risks for bottom-up calibration are not necessarily the largest percentage differences, but processes for which the activity-data boundary is not transparent.
3. Decarbonisation measures should be evaluated separately for process and energy emissions because their technological determinants differ.
4. Kazakhstan requires a staged approach: reconcile historical data first, calibrate the base year second, and analyse technology scenarios only afterward.

These expectations are not hypotheses about future emissions reductions. They are model-quality criteria that prevent false precision in scenario construction.

## 8. How to use the review in the article

### Introduction

Use the Kazakhstan and Central Asian literature (Zhakiyev et al., 2023; De Miglio et al., 2023; De Miglio and Bakdolotov, 2024; Zhakiyev et al., 2025a, 2025b; Radovanović et al., 2021) to establish climate targets, regional carbon intensity and the existing energy-system focus of modelling.

### Methodological rationale

Use Tan et al. (2022), Dang et al. (2026), Duan et al. (2022), the 2024 hydrogen-metallurgy study and the 2024 LEAP-China study to justify a bottom-up LEAP structure and technology scenarios.

### Discussion

Use Müller et al. (2024), Obrist et al. (2021), Tautorat et al. (2023) and the 2022 sub-sectoral integrated-modelling study to explain why process emissions, clinker, reductants, CCS and hydrogen cannot be represented adequately by one aggregate industrial-output indicator.

## Extended research-gap and contribution wording

> Although Kazakhstan-focused mitigation studies have examined national energy-system and economy-wide pathways, they do not provide a transparent process-level representation of IPPU activity data that can be reconciled with official UNFCCC inventory reporting and operationalised in a bottom-up LEAP model. This study addresses that gap by compiling the 1990–2023 IPPU emissions series, testing BNS–UNFCCC comparability for key processes, and establishing a harmonisation protocol for subsequent scenario modelling.

More fully, the article contributes by joining two tasks that are normally separated: national-inventory analysis and scenario-model preparation. The CRT historical series serves not only to describe a trend but also as a calibration benchmark. BNS statistics are not treated as an automatic alternative to UNFCCC data; they are tested at product and process-boundary level. The result is a reproducible basis for a future LEAP model that can assess decarbonisation measures without conflating process and energy emissions.

## Sources used

1. Zhakiyev, N. et al. (2023). *Optimization Modelling of the Decarbonization Scenario of the Total Energy System of Kazakhstan until 2060*. **Energies, 16**(13), 5142. [https://doi.org/10.3390/en16135142](https://doi.org/10.3390/en16135142).
2. De Miglio, R., & Bakdolotov, A. (2024). *A “risk-induced” emission mitigation pathway for Kazakhstan*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2211467X24000397).
3. Zhakiyev, N. et al. (2025a). *Forecasting of GHG Emissions from Energy and Industrial Sectors of Kazakhstan and Assessment of Mitigation Scenarios with High Share of Renewables*. **International Journal of Renewable Energy Research, 15**(2). [Article](https://www.ijrer.org/index.php/ijrer/article/view/15837).
4. De Miglio, R. et al. (2023). *Reinforcing the Paris Agreement: Ambitious scenarios for the decarbonisation of the Central Asian and Caspian region*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2667095X23000041).
5. Zhakiyev, N. et al. (2025b). *Energy systems, CO2 emissions, and mitigation policies in three Central Asian countries: A comprehensive review*. **Energy Strategy Reviews, 62**, 101883. [https://doi.org/10.1016/j.esr.2025.101883](https://doi.org/10.1016/j.esr.2025.101883).
6. Radovanović, M. et al. (2021). *Sustainable energy transition in Central Asia: status and challenges*. **Energy, Sustainability and Society**. [Article](https://link.springer.com/article/10.1186/s13705-021-00324-2).
7. Tan, X. et al. (2022). *A technology-driven pathway to net-zero carbon emissions for China's cement industry*. [ScienceDirect record](https://www.sciencedirect.com/science/article/abs/pii/S0306261922010807).
8. Dang, et al. (2026). *Decarbonization and clean production in China's cement industry: Strategies from the LEAP-LCA perspective*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S019592552500321X).
9. Duan, et al. (2022). *Towards lower CO2 emissions in iron and steel production: Life cycle energy demand-LEAP based multi-stage and multi-technique simulation*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2352550922001166).
10. *Exploring hydrogen metallurgy to CO2 emissions reduction in China's iron and steel production: An analysis based on the life cycle CO2 emissions–LEAP model* (2024). [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2352484724002348).
11. *Medium and long-term energy demand forecasts by sectors in China under the goal of carbon peaking & carbon neutrality: Based on the LEAP-China model* (2024). [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S0360544224027919).
12. Müller, et al. (2024). *Decarbonizing the cement industry: Findings from coupling prospective life cycle assessment of clinker with integrated assessment model scenarios*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S0959652624013325).
13. *China's industrial decarbonization in the context of carbon neutrality: A sub-sectoral analysis based on integrated modelling* (2022). [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S1364032122008735).
14. Tautorat, et al. (2023). *Directions of innovation for the decarbonization of cement and steel production – A topic modeling-based analysis*. [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S0959652623012131).
15. Obrist, et al. (2021). *Decarbonization pathways of the Swiss cement industry towards net zero emissions*. [ETH Zurich Research Collection](https://www.research-collection.ethz.ch/entities/publication/72a3bcf1-de4d-4f0e-9efc-5ff6c113c1bc).

> **Bibliographic note:** Before submission, import all 15 items through DOI/publisher pages into Zotero or another reference manager and replace these abbreviated records with the conference or journal reference style. The substantive synthesis uses titles, abstracts and relevance descriptions in the author-supplied list.
