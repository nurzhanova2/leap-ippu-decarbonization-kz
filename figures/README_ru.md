# Рисунки

English version: [README.md](README.md).

| Рисунок | Содержание | Воспроизводимый источник |
|---|---|---|
| `figure_1_ippu_total_emissions_1990_2023.png` | Историческая динамика суммарных IPPU-выбросов | Скрипты извлечения исторических данных и CRT 2025 |
| `figure_2_ippu_category_composition_1990_2023.png` | Историческая структура по категориям | Скрипты извлечения исторических данных и CRT 2025 |
| `figure_3_crf_2023_vs_crt_2025_total_ippu_comparison.png` | Сопоставление CRF и CRT | Скрипт сравнения версий |
| `figure_4_leap_ippu_scenario_pathways_2024_2050.png` | Сценарные траектории LEAP | `scripts/analyze_leap_scenarios.py` |
| `figure_5_leap_ippu_avoided_emissions_2024_2050.png` | Предотвращённые выбросы по группам процессов | `scripts/analyze_leap_scenarios.py` |
| `figure_4_leap_ippu_scenario_pathways_2024_2050_crt2026.png` | Журнальная версия: основные сценарии на базе CRT 2026 inventory 2024 | `scripts/analyze_leap_scenarios.py --inventory crt2026` |
| `figure_5_leap_ippu_avoided_emissions_2024_2050_crt2026.png` | Журнальная версия: предотвращённые выбросы по группам процессов | `scripts/analyze_leap_scenarios.py --inventory crt2026` |
| `figure_6_leap_ippu_growth_sensitivity_2024_2050_crt2026.png` | Журнальная версия: рост активности с действующими и литературными множителями | `scripts/analyze_leap_sensitivity.py` |
| `figure_7_leap_ippu_tornado_2050_crt2026.png` | Журнальная версия: влияние каждого допущения на 2050 г. | `scripts/analyze_leap_sensitivity.py` |
| `figure_1_ippu_total_emissions_1990_2024_crt2026.png` | Журнальная версия (CRT 2026): суммарные исторические выбросы IPPU | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |
| `figure_2_ippu_category_composition_1990_2024_crt2026.png` | Журнальная версия (CRT 2026): структура по категориям | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |
| `figure_3_crt_2025_vs_crt_2026_total_ippu_comparison_crt2026.png` | Журнальная версия: пересчёт между CRT 2025 и CRT 2026 | `scripts/analyze_ippu_timeseries.py --inventory crt2026` |

Рисунки 1–5 без суффикса относятся к архивной конференционной версии (CRT 2025). Рисунки 4–7 отражают только явно заданную границу процессных выбросов из [протокола сценариев](../docs/leap_scenarios_2023_2050.md), а не прогноз национального итога IPPU.
