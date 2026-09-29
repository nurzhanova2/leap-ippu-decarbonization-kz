# Input-data registry

Русская версия: [README.md](README.md).

The folder structure supports reproducible work. Raw source files are retained unchanged and processed derivatives are kept separately.

```text
data/
├── raw/           # unchanged primary-source files
├── processed/     # cleaned and harmonised derivatives
├── metadata/      # registries, crosswalks, and transformation logs
└── README.md
```

## Harmonisation rules

- Preserve both the original and converted values.
- Do not replace `NE`, `NO`, `NA`, `IE`, or confidential entries with zero.
- Keep source units in metadata; standardise mass to tonnes and emissions to kt CO2eq only in derivative fields.
- Compare only matching products and boundaries: cement is not clinker.
- Record source table, sheet, cell or page for every manually extracted observation.

## Status, 28 September 2026

Unchanged BNS, CRT 2025, CRF 2023, NID 2025, and NIR 2023 sources are retained under `raw/`. IPPU emissions and activity data from CRT/CRF, 2021 BNS–CRT checks, the 1990–2023 historical series and category-composition tables have been extracted. Priority IPPU methodology sections in NID/NIR are reviewed; process boundaries and comparability status are in the [methodology review](../docs/process_methodology_review_en.md), and results and figure locations are in the [article analysis](../docs/article_analysis_en.md).
