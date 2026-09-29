"""Create a transparent 2021 BNS-CRT activity-data comparison for selected products."""

import csv
from pathlib import Path


BNS = Path("data/processed/bns_ippu_activity_data_2021_annual.csv")
CRT = Path("data/processed/unfccc_ippu_activity_data_1990_2023.csv")
OUTPUT = Path("data/processed/bns_vs_crt_2025_activity_comparison_2021.csv")

with BNS.open(encoding="utf-8") as handle:
    bns_rows = {row["product"]: row for row in csv.DictReader(handle)}
with CRT.open(encoding="utf-8") as handle:
    crt_rows = [row for row in csv.DictReader(handle) if row["source"] == "UNFCCC CRT 2025" and row["inventory_year"] == "2021"]

crt_index = {(row["category_code"], row["activity_description"]): row for row in crt_rows}
specification = [
    ("Клинкеры цементные, тыс.тонн", "2.A.1", "Clinker production", "directly_comparable"),
    ("Портландцемент (кроме белого), тыс.тонн", "2.A.1", "Clinker production", "not_directly_comparable_product_definition_differs"),
    ("Известь гашенная, негашеная и гидравлическая, тонн", "2.A.2", "Lime produced", "directly_comparable_as_aggregate"),
    ("Чугун передельный, литейный или зеркальный в чушках, болванках или в виде форм первичных прочих, тонн", "2.C.1.b", "Pig iron production", "not_directly_comparable_boundary_differs"),
    ("Ферросплавы, тонн", "2.C.2", "Ferroalloys production", "directly_comparable_as_total_output"),
    ("Сталь нерафинированная, тонн", "2.C.1.a", "Steel production", "directly_comparable_as_activity_indicator"),
    ("Цинк необработанный, тонн", "2.C.6", "Zinc production", "not_directly_comparable_boundary_differs"),
]

records = []
for product, code, description, status in specification:
    bns = bns_rows[product]
    crt = crt_index[(code, description)]
    bns_tonnes = float(bns["source_value"]) * (1000 if bns["source_unit"] == "тыс.тонн" else 1)
    crt_tonnes = float(crt["activity_value_tonnes"])
    records.append({
        "year": 2021,
        "bns_product": product,
        "bns_value_tonnes": bns_tonnes,
        "crt_category_code": code,
        "crt_activity_description": description,
        "crt_value_tonnes": crt_tonnes,
        "difference_crt_minus_bns_tonnes": crt_tonnes - bns_tonnes,
        "difference_percent_of_bns": (crt_tonnes - bns_tonnes) / bns_tonnes * 100,
        "comparability_status": status,
        "interpretation_note": "A numerical difference is not an evidence of data error unless the product definition and reporting boundary are the same.",
    })

with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
print(f"Wrote {len(records)} records to {OUTPUT}")
