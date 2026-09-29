"""Compare common IPPU observations in CRF 2023 and CRT 2025."""

import csv
from pathlib import Path


INPUT = Path("data/processed/unfccc_ippu_emissions_1990_2023.csv")
OUTPUT = Path("data/processed/crf_2023_vs_crt_2025_ippu_comparison_1990_2021.csv")

with INPUT.open(encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

index = {(row["source"], row["inventory_year"], row["category_code"]): row for row in rows}
records = []
for year in range(1990, 2022):
    for code in sorted({row["category_code"] for row in rows if row["inventory_year"] == str(year)}):
        crf = index.get(("UNFCCC CRF 2023", str(year), code))
        crt = index.get(("UNFCCC CRT 2025", str(year), code))
        if not crf or not crt:
            continue
        crf_total = float(crf["total_ghg_kt_co2eq"])
        crt_total = float(crt["total_ghg_kt_co2eq"])
        crf_co2 = float(crf["co2_kt"])
        crt_co2 = float(crt["co2_kt"])
        records.append({
            "inventory_year": year,
            "category_code": code,
            "category_label": crt["category_label"],
            "crf_2023_total_ghg_kt_co2eq_ar4": crf_total,
            "crt_2025_total_ghg_kt_co2eq_ar5": crt_total,
            "total_difference_crt_minus_crf_kt_co2eq": crt_total - crf_total,
            "total_difference_percent_of_crf": (crt_total - crf_total) / crf_total * 100 if crf_total else "",
            "crf_2023_co2_kt": crf_co2,
            "crt_2025_co2_kt": crt_co2,
            "co2_difference_crt_minus_crf_kt": crt_co2 - crf_co2,
            "co2_difference_percent_of_crf": (crt_co2 - crf_co2) / crf_co2 * 100 if crf_co2 else "",
            "interpretation_note": "Total CO2eq comparison combines CRF AR4 and CRT AR5 GWP frameworks; CO2-only difference is less affected by GWP changes.",
        })

with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
print(f"Wrote {len(records)} records to {OUTPUT}")
