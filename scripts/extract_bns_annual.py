"""Extract IPPU-relevant candidates from a BNS annual physical-output workbook.

Usage: python3 scripts/extract_bns_annual.py YEAR INPUT_XLSX OUTPUT_CSV
"""

import argparse
import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile


NAMESPACE = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
KEYWORDS = ("клинкер", "цемент", "извест", "чугун", "ферросплав", "сталь", "алюмин", "цинк необработанный")


def shared_strings(archive):
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    return ["".join(item.itertext()) for item in root.findall("m:si", NAMESPACE)]


def row_values(row, strings):
    values = {}
    for cell in row.findall("m:c", NAMESPACE):
        value = cell.find("m:v", NAMESPACE)
        text = "" if value is None else value.text
        if cell.attrib.get("t") == "s" and text:
            text = strings[int(text)]
        values[cell.attrib["r"].rstrip("0123456789")] = text
    return values


parser = argparse.ArgumentParser()
parser.add_argument("year")
parser.add_argument("input_xlsx", type=Path)
parser.add_argument("output_csv", type=Path)
parser.add_argument("--value-column", help="Use a documented reporting-period column when no year header exists")
args = parser.parse_args()

with zipfile.ZipFile(args.input_xlsx) as archive:
    strings = shared_strings(archive)
    worksheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
    rows = [row_values(row, strings) for row in worksheet.findall(".//m:sheetData/m:row", NAMESPACE)]

if args.value_column:
    year_column = args.value_column
else:
    year_columns = [column for row in rows for column, value in row.items() if value == args.year]
    if len(year_columns) != 1:
        raise ValueError(f"Expected exactly one {args.year} header, found {year_columns}; use --value-column if the workbook is a reporting-period table")
    year_column = year_columns[0]

records = []
for row in rows:
    product = row.get("A", "")
    if not any(keyword in product.lower() for keyword in KEYWORDS):
        continue
    value = row.get(year_column, "")
    unit = product.rsplit(", ", 1)[-1] if ", " in product else "not_stated"
    records.append({
        "year": args.year,
        "ippu_category": "to_be_mapped_after_inventory_review",
        "product": product,
        "product_definition": "BNS physical industrial output; gross output definition",
        "source_dataset": f"BNS annual physical industrial production {args.year}",
        "source_table_or_sheet": "Лист1; national product row",
        "source_value": value,
        "source_unit": unit,
        "conversion_factor_to_tonnes": "",
        "standardised_value_tonnes": "",
        "reporting_notation": value if value in {"-", "..", "х", "x"} else "numeric_or_blank",
        "comparability_status": "requires_match_to_UNFCCC_activity_data",
        "notes": f"Extracted automatically from column {year_column}; source file and product label retained",
    })

args.output_csv.parent.mkdir(parents=True, exist_ok=True)
with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print(f"Wrote {len(records)} records to {args.output_csv}")
