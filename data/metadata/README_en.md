# Metadata and data dictionaries

Русская версия: [README.md](README.md).

This folder documents sources, mappings and data-entry rules; it does not replace raw or processed datasets.

| File | Purpose |
|---|---|
| `source_registry.csv` | register of primary sources: provenance, coverage, units, status and limitations |
| `activity_data_template.csv` | template for manual activity-data entries, requiring a page, sheet or cell reference |
| `bns_ippu_category_crosswalk.csv` | mapping of BNS products to IPCC IPPU categories and comparability status |
| `leap_scenario_parameters.csv` | single source of LEAP scenario parameters: base values of the 15 branches (tonnes of gas), branch unit in the LEAP template and f2030/f2050 factors; read by `fill_leap_import_template.py` and `analyze_leap_scenarios.py` |
| `scenario_levers_literature.csv` | literature values for mitigation levers by process (L01–L36): metric, 2030 and 2050 values, implied factor, source, page or table, DOI or URL, raw file and applicability to Kazakhstan |
| `leap_sensitivity_factors.csv` | proposed low, central and high f2030/f2050 for additional sensitivity runs, with the lever entries they rely on; the presented scenarios do not use it |
| `leap_scenario_parameters_crt2026.csv` | the same branches, units and factors with base values from CRT 2026 for 2024 (journal version); built by `scripts/build_leap_parameters.py --inventory crt2026` |
| `bns_activity_index_2024.csv` | BNS 2024/2023 activity index by process (central, low/high, variants), edition and release date, quality and share of the base; since the move to CRT 2026 it is used only as a check |
| `leap_growth_variants.csv` | activity-growth variants after 2024 by process: trend series and window, official forecast sector and rate |
| `leap_2a4_variants.csv` | 2.A.4.d options: emissive share s, base-year alternative and the mineral-group factor variant |
| `references_check.csv` | check log for every entry of [docs/references.bib](../../docs/references.bib): where it is cited, status (verified, corrected, added), how it was checked (Crossref DOI record, PDF in data/raw/, official page), DOI and corrections |

CSV field names remain in English for machine readability and interoperability. Original BNS product labels remain in Russian without translation. Values are not duplicated into two language versions because that would create competing data stores; explanatory documentation, interpretation rules and navigation are bilingual.

