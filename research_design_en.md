# Research design: Kazakhstan IPPU, 1990-2023

Русская версия: [research_design_ru.md](research_design_ru.md).

## Working title

**LEAP-Based modeling of Decarbonization pathways in the IPPU sector of Kazakhstan.**

This is the official conference title. At the present stage, the article provides an empirical foundation for later LEAP modelling; it does not claim that scenarios have already been calculated.

## Objective

To characterise the dynamics of Kazakhstan's *Industrial Processes and Product Use* (IPPU) emissions in 1990-2023 and assess the comparability of production statistics with activity data used in national inventory reporting.

## Article research questions

**Main question. How comparable are official UNFCCC data and Bureau of National Statistics (BNS) production statistics for analysing Kazakhstan's historical IPPU emissions in 1990-2023?**

**RQ1. How did total IPPU emissions and their composition change in Kazakhstan during 1990-2023?**

**RQ2. How do IPPU estimates differ between CRF 2023 and CRT 2025 in overlapping years, once the non-comparability of AR4 and AR5 GWP frameworks is made explicit?**

**RQ3. To what extent do apparent BNS-UNFCCC differences for key IPPU processes arise from product definitions and process boundaries rather than data inconsistency?**

## Core expectations

1. IPPU emissions fell during the 1990s and later recovered, with trajectories differing by category.
2. Differences between CRF and CRT exist, but CO2eq comparisons cannot be interpreted as pure inventory revisions without accounting for AR4/AR5.
3. Apparent BNS-UNFCCC discrepancies can result from different product definitions or process boundaries, not only from data errors.

## Current contribution

The study does not yet claim completed decarbonisation scenarios. It:

1. creates a harmonised historical IPPU emissions series from official UNFCCC submissions;
2. documents CRF 2023 and CRT 2025 differences without conflating GWP changes with inventory revisions;
3. compares production statistics and inventory activity data at process level, without equating cement with clinker or national output with a narrow technological stream;
4. provides a transparent, versioned input dataset and QA protocol for later LEAP modelling.

## Scope and rules

- **Geography:** Kazakhstan.
- **Period:** 1990-2023 for CRT; 1990-2021 for the CRF comparison.
- **Sector:** IPCC sector 2 (IPPU). Energy-combustion emissions are excluded.
- **Emissions unit:** kt CO2eq, preserving the GWP framework used by the source.
- **Activity unit:** physical product units, mainly tonnes per year; monetary BNS series are not used as activity data.
- **Comparability:** compare only identical product definitions and process boundaries.

## Calculations

For a valid like-for-like comparison:

\[
\Delta_{abs}=X_{UNFCCC}-X_{BNS}
\]

\[
\Delta_{\%}=\frac{X_{UNFCCC}-X_{BNS}}{X_{BNS}}\times100
\]

Do not calculate a percentage when the BNS value is zero or missing. Do not treat `NE`, `NO`, `NA`, `IE`, or confidential entries as zero.

## Link to the subsequent LEAP stage

After this article, harmonised activity data and the comparability protocol can support LEAP base-year calibration and scenario testing for 2030/2050. That is subsequent work, not a fourth research question for this article.
