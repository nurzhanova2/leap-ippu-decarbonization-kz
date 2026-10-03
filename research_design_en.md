# Research design: Kazakhstan IPPU, 1990-2023

Русская версия: [research_design_ru.md](research_design_ru.md).

## Working title

**LEAP-Based modeling of Decarbonization pathways in the IPPU sector of Kazakhstan.**

This is the official conference title. The article combines a historical data-quality assessment with transparent, 2023-calibrated exploratory IPPU scenario pathways to 2050. The pathways are not national forecasts or least-cost optimisation results.

## Objective

To characterise the dynamics of Kazakhstan's *Industrial Processes and Product Use* (IPPU) emissions in 1990–2023, assess the comparability of production statistics with inventory activity data, and quantify exploratory process-emissions pathways for 2030 and 2050 from a 2023 calibration.

## Article research questions

**Main question. How can harmonised official inventory data and production statistics support transparent exploratory decarbonisation pathways for selected IPPU processes in Kazakhstan?**

**RQ1. How did total IPPU emissions and their composition change in Kazakhstan during 1990-2023?**

**RQ2. How do IPPU estimates differ between CRF 2023 and CRT 2025 in overlapping years, once the non-comparability of AR4 and AR5 GWP frameworks is made explicit?**

**RQ3. To what extent do apparent BNS-UNFCCC differences for key IPPU processes arise from product definitions and process boundaries rather than data inconsistency?**

**RQ4. Under explicitly stated, exploratory emissions-reduction assumptions, how do included IPPU process emissions evolve to 2030 and 2050 relative to a flat 2023 baseline?**

## Core expectations

1. IPPU emissions fell during the 1990s and later recovered, with trajectories differing by category.
2. Differences between CRF and CRT exist, but CO2eq comparisons cannot be interpreted as pure inventory revisions without accounting for AR4/AR5.
3. Apparent BNS-UNFCCC discrepancies can result from different product definitions or process boundaries, not only from data errors.
4. The magnitude of exploratory mitigation depends materially on the stated emissions multipliers and model boundary; it must not be interpreted as a full-sector forecast.

## Current contribution

The study:

1. creates a harmonised historical IPPU emissions series from official UNFCCC submissions;
2. documents CRF 2023 and CRT 2025 differences without conflating GWP changes with inventory revisions;
3. compares production statistics and inventory activity data at process level, without equating cement with clinker or national output with a narrow technological stream;
4. provides a transparent, versioned input dataset and QA protocol for LEAP implementation; and
5. reports reproducible exploratory pathways for an explicitly bounded set of process emissions, with a flat baseline and two mitigation sensitivities.

## Scope and rules

- **Geography:** Kazakhstan.
- **Period:** 1990-2023 for CRT; 1990-2021 for the CRF comparison.
- **Sector:** IPCC sector 2 (IPPU). Energy-combustion emissions are excluded.
- **Emissions unit:** kt CO2eq, preserving the GWP framework used by the source.
- **Activity unit:** physical product units, mainly tonnes per year; monetary BNS series are not used as activity data.
- **Comparability:** compare only identical product definitions and process boundaries.
- **Scenario period:** 2023–2050; Current Accounts is 2023 and the first scenario year is 2024.
- **Scenario boundary:** selected mineral, metal and chemical process emissions; F-gases, aluminium PFCs, unlisted IPPU sources and industrial fuel combustion are excluded.

## Calculations

For a valid like-for-like comparison:

\[
\Delta_{abs}=X_{UNFCCC}-X_{BNS}
\]

\[
\Delta_{\%}=\frac{X_{UNFCCC}-X_{BNS}}{X_{BNS}}\times100
\]

Do not calculate a percentage when the BNS value is zero or missing. Do not treat `NE`, `NO`, `NA`, `IE`, or confidential entries as zero.

## LEAP scenario stage

The [scenario protocol](docs/leap_scenarios_2023_2050_en.md) documents the Current Accounts calibration, three scenarios, interpolation expressions and the full output table. A LEAP-compatible import workbook is stored in `outputs/`. A final desktop-LEAP import, calculation and exported-output check is required before the numerical pathways are called LEAP-calculated results.
