# LEAP exchange files

Русская версия: [README_ru.md](README_ru.md).

This directory holds files exchanged with the desktop LEAP model. The workbook in `leap_ippu_import/` preserves LEAP export identifiers and contains corrected 2024 Current Accounts values (2023 inventory proxy) plus expressions for the three exploratory scenarios. Values are entered in each branch’s template unit: `Metric Tonne` for CO2 and `Kilogramme` for the ferroalloy CH4 and nitric-acid N2O branches. See the bilingual scenario protocol in [docs/leap_scenarios_2023_2050_en.md](../docs/leap_scenarios_2023_2050_en.md) before citing the results.

`Kazakhstan_IPPU_LEAP_import_crt2026.xlsx` is the journal-version workbook: the same branches and identifiers with Current Accounts from CRT 2026 for 2024 (22,088.3 kt CO2eq). It is written with `--parameters data/metadata/leap_scenario_parameters_crt2026.csv`; the conference workbook `Kazakhstan_IPPU_LEAP_final_import.xlsx` is kept as an archive.

Do not edit identifiers, sheet names, paths, variable names, or units manually. If scenario assumptions change, edit `data/metadata/leap_scenario_parameters.csv`, regenerate the workbook from a fresh LEAP export using `scripts/fill_leap_import_template.py`, then repeat the checks listed under [Verification](../docs/leap_scenarios_2023_2050_en.md#verification) in the protocol.
