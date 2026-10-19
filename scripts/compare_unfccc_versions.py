"""Compare common IPPU observations in two UNFCCC submissions.

Default: CRF 2023 vs CRT 2025 for 1990-2021 (archived output). With
"--pair crt2025_crt2026": CRT 2025 vs CRT 2026 for 1990-2023, in the same
format; both use AR5, so differences are recalculations.
"""

import csv
import sys
from pathlib import Path


PAIRS = {
    "crf2023_crt2025": {
        "inputs": [Path("data/processed/unfccc_ippu_emissions_1990_2023.csv")],
        "output": Path("data/processed/crf_2023_vs_crt_2025_ippu_comparison_1990_2021.csv"),
        "old": ("UNFCCC CRF 2023", "crf_2023", "ar4", "crf"),
        "new": ("UNFCCC CRT 2025", "crt_2025", "ar5", "crt"),
        "years": range(1990, 2022),
        "note": "Total CO2eq comparison combines CRF AR4 and CRT AR5 GWP frameworks; CO2-only difference is less affected by GWP changes.",
    },
    "crt2025_crt2026": {
        "inputs": [Path("data/processed/unfccc_ippu_emissions_1990_2023.csv"),
                   Path("data/processed/unfccc_ippu_emissions_1990_2024_crt2026.csv")],
        "output": Path("data/processed/crt_2025_vs_crt_2026_ippu_comparison_1990_2023_crt2026.csv"),
        "old": ("UNFCCC CRT 2025", "crt_2025", "ar5", "crt2025"),
        "new": ("UNFCCC CRT 2026", "crt_2026", "ar5", "crt2026"),
        "years": range(1990, 2024),
        "note": "Both submissions use AR5 GWPs; differences are recalculations (see NID 2026).",
    },
}
pair = sys.argv[sys.argv.index("--pair") + 1] if "--pair" in sys.argv else "crf2023_crt2025"
spec = PAIRS[pair]
old_source, old_name, old_gwp, old_short = spec["old"]
new_source, new_name, new_gwp, new_short = spec["new"]

rows = []
for path in spec["inputs"]:
    with path.open(encoding="utf-8") as handle:
        rows.extend(csv.DictReader(handle))

index = {(row["source"], row["inventory_year"], row["category_code"]): row for row in rows}
records = []
for year in spec["years"]:
    for code in sorted({row["category_code"] for row in rows if row["inventory_year"] == str(year)}):
        old = index.get((old_source, str(year), code))
        new = index.get((new_source, str(year), code))
        if not old or not new:
            continue
        old_total = float(old["total_ghg_kt_co2eq"])
        new_total = float(new["total_ghg_kt_co2eq"])
        old_co2 = float(old["co2_kt"])
        new_co2 = float(new["co2_kt"])
        records.append({
            "inventory_year": year,
            "category_code": code,
            "category_label": new["category_label"],
            f"{old_name}_total_ghg_kt_co2eq_{old_gwp}": old_total,
            f"{new_name}_total_ghg_kt_co2eq_{new_gwp}": new_total,
            f"total_difference_{new_short}_minus_{old_short}_kt_co2eq": new_total - old_total,
            f"total_difference_percent_of_{old_short}": (new_total - old_total) / old_total * 100 if old_total else "",
            f"{old_name}_co2_kt": old_co2,
            f"{new_name}_co2_kt": new_co2,
            f"co2_difference_{new_short}_minus_{old_short}_kt": new_co2 - old_co2,
            f"co2_difference_percent_of_{old_short}": (new_co2 - old_co2) / old_co2 * 100 if old_co2 else "",
            "interpretation_note": spec["note"],
        })

with spec["output"].open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
print(f"Wrote {len(records)} records to {spec['output']}")
