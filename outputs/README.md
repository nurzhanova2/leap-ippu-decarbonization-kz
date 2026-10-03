# LEAP exchange files

Русская версия: [README_ru.md](README_ru.md).

This directory holds files exchanged with the desktop LEAP model. The workbook in `leap_ippu_import/` preserves LEAP export identifiers and contains corrected 2024 Current Accounts values plus expressions for the three exploratory scenarios. See the bilingual scenario protocol in [docs/leap_scenarios_2023_2050_en.md](../docs/leap_scenarios_2023_2050_en.md) before citing the results.

Do not edit identifiers, sheet names, paths, variable names, or units manually. If scenario assumptions change, regenerate the workbook from a fresh LEAP export using `scripts/fill_leap_import_template.py`, then carry out the LEAP verification described in the protocol.
