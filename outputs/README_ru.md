# Файлы обмена с LEAP

English version: [README.md](README.md).

В этой папке находятся файлы для обмена с desktop LEAP. Workbook в `leap_ippu_import/` сохраняет идентификаторы LEAP и содержит исправленные значения Current Accounts 2024 г. (приближение по инвентаризации 2023 г.) и выражения для трёх исследовательских сценариев. Значения заданы в единице ветви из шаблона: `Metric Tonne` для CO2 и `Kilogramme` для ветвей CH4 ферросплавов и N2O азотной кислоты. Перед цитированием результатов прочитайте двуязычный [протокол сценариев](../docs/leap_scenarios_2023_2050.md).

`Kazakhstan_IPPU_LEAP_import_crt2026.xlsx` — книга журнальной версии: те же ветви и идентификаторы, Current Accounts по CRT 2026 за 2024 г. (22 088.3 тыс. т CO2-экв.). Она записана с `--parameters data/metadata/leap_scenario_parameters_crt2026.csv`; конференционная книга `Kazakhstan_IPPU_LEAP_final_import.xlsx` сохраняется как архив.

Не редактируйте вручную идентификаторы, названия листов, пути, имена переменных и единицы. При изменении сценарных допущений отредактируйте `data/metadata/leap_scenario_parameters.csv`, сформируйте workbook заново из свежего экспорта LEAP с помощью `scripts/fill_leap_import_template.py`, затем повторите проверки из раздела [Проверка](../docs/leap_scenarios_2023_2050.md#проверка) протокола.
