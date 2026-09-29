"""Extract IPPU emissions from Kazakhstan CRT 2025 and CRF 2023 workbooks.

The script reads the unmodified country-year workbooks and writes a long-form
CSV. CRT totals are reported directly in Table 2(I); CRF 2023 totals are
recalculated from its AR4 component columns and documented as such.
"""

import csv
from pathlib import Path
import re
from openpyxl import load_workbook


CRT_DIR = Path("data/raw/unfccc_crt_2025/extracted")
CRF_DIR = Path("data/raw/unfccc_crf_2023/extracted")
OUTPUT = Path("data/processed/unfccc_ippu_emissions_1990_2023.csv")
AR4_CH4_GWP = 25
AR4_N2O_GWP = 298
AR4_SF6_GWP = 22800


def number(value):
    return float(value) if isinstance(value, (int, float)) else 0.0


def crt_category(label):
    match = re.match(r"^(2(?:\.[A-H](?:\.\d+)?)?)\.\s*(.*)$", str(label).strip())
    if not match:
        return None, None
    return match.group(1), match.group(2).strip()


def crf_rows(workbook_path):
    book = load_workbook(workbook_path, read_only=True, data_only=True)
    worksheet = book["Table2(I)s1"]
    parent = None
    rows = []
    for values in worksheet.iter_rows(values_only=True):
        label = values[0]
        if not isinstance(label, str):
            continue
        label = label.strip()
        if label == "Total industrial processes":
            code, short_label = "2", label
        elif match := re.match(r"^([A-H])\.\s*(.*)$", label):
            parent, code, short_label = match.group(1), f"2.{match.group(1)}", match.group(2).strip()
        elif match := re.match(r"^(\d+)\.\s*(.*)$", label):
            if parent is None:
                continue
            code, short_label = f"2.{parent}.{match.group(1)}", match.group(2).strip()
        else:
            continue
        co2, ch4, n2o, hfc, pfc, mixed, sf6, nf3 = (number(values[i]) for i in range(1, 9))
        total = co2 + AR4_CH4_GWP * ch4 + AR4_N2O_GWP * n2o + hfc + pfc + mixed + AR4_SF6_GWP * sf6 + nf3
        rows.append({
            "source": "UNFCCC CRF 2023",
            "submission_date": "2023-04-15",
            "inventory_year": re.search(r"KAZ_2023_(\d{4})_", workbook_path.name).group(1),
            "category_code": code,
            "category_label": short_label,
            "total_ghg_kt_co2eq": total,
            "co2_kt": co2,
            "ch4_kt": ch4,
            "n2o_kt": n2o,
            "hfc_kt_co2eq": hfc,
            "pfc_kt_co2eq": pfc,
            "sf6_kt": sf6,
            "total_method": "recalculated_AR4_from_Table2(I)s1",
            "source_table": "Table2(I)s1",
        })
    return rows


def crt_rows(workbook_path):
    book = load_workbook(workbook_path, read_only=True, data_only=True)
    worksheet = book["Table2(I)"]
    rows = []
    for values in worksheet.iter_rows(values_only=True):
        code, label = crt_category(values[1] if len(values) > 1 else None)
        if code is None:
            continue
        rows.append({
            "source": "UNFCCC CRT 2025",
            "submission_date": "2025-04-15",
            "inventory_year": re.search(r"V1\.0-(\d{4})-", workbook_path.name).group(1),
            "category_code": code,
            "category_label": label,
            "total_ghg_kt_co2eq": number(values[14]),
            "co2_kt": number(values[2]),
            "ch4_kt": number(values[3]),
            "n2o_kt": number(values[4]),
            "hfc_kt_co2eq": number(values[5]),
            "pfc_kt_co2eq": number(values[6]),
            "sf6_kt": number(values[8]),
            "total_method": "reported_directly_in_CRT_Table2(I)",
            "source_table": "Table2(I)",
        })
    return rows


records = []
for workbook in sorted(CRF_DIR.glob("*.xlsx")):
    records.extend(crf_rows(workbook))
for workbook in sorted(CRT_DIR.glob("*.xlsx")):
    records.extend(crt_rows(workbook))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print(f"Wrote {len(records)} records to {OUTPUT}")
