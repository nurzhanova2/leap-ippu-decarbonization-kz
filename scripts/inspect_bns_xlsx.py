"""Extract national IPPU-relevant production rows from the official BNS workbook.

The source workbook remains unchanged. This script writes a long-form derivative
table and preserves the BNS product label and reporting notation.
"""

import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile


WORKBOOK = Path("data/raw/bns/bns_industrial_production_1990_2025.xlsx")
OUTPUT = Path("data/processed/bns_ippu_activity_data_1990_2023.csv")
NAMESPACE = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
KEYWORDS = ("извест", "ферросплав", "алюмин", "цинк")


def shared_strings(archive):
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    return ["".join(item.itertext()) for item in root.findall("m:si", NAMESPACE)]


def cell_value(cell, strings):
    value = cell.find("m:v", NAMESPACE)
    if value is None:
        return ""
    if cell.attrib.get("t") == "s":
        return strings[int(value.text)]
    return value.text


def row_values(row, strings):
    return {
        cell.attrib["r"].rstrip("0123456789"): cell_value(cell, strings)
        for cell in row.findall("m:c", NAMESPACE)
    }


with zipfile.ZipFile(WORKBOOK) as archive:
    strings = shared_strings(archive)
    worksheet = ET.fromstring(archive.read("xl/worksheets/sheet4.xml"))
    rows = [row_values(row, strings) for row in worksheet.findall(".//m:sheetData/m:row", NAMESPACE)]

years = {column: value for column, value in rows[2].items() if value.isdigit()}
records = []
for index, row in enumerate(rows):
    product = row.get("A", "")
    if not any(keyword in product.lower() for keyword in KEYWORDS):
        continue
    national = rows[index + 1] if index + 1 < len(rows) else {}
    if national.get("A") != "Республика Казахстан":
        raise ValueError(f"National total not found after product: {product}")
    unit = product.rsplit(", ", 1)[-1] if ", " in product else "not_stated"
    for column, year in years.items():
        if 1990 <= int(year) <= 2023:
            records.append({
                "year": year,
                "ippu_category": "to_be_mapped_after_inventory_review",
                "product": product,
                "product_definition": "BNS physical industrial output; gross output definition",
                "source_dataset": "BNS industrial production 1990-2025",
                "source_table_or_sheet": "обрабатыв; Республика Казахстан row",
                "source_value": national.get(column, ""),
                "source_unit": unit,
                "conversion_factor_to_tonnes": "",
                "standardised_value_tonnes": "",
                "reporting_notation": national.get(column, "") if national.get(column, "") in {"-", "..", "х"} else "numeric_or_blank",
                "comparability_status": "requires_match_to_UNFCCC_activity_data",
                "notes": "Extracted automatically; source file and product label retained",
            })

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

products = sorted({record["product"] for record in records})
print(f"Wrote {len(records)} records for {len(products)} products to {OUTPUT}")
for product in products:
    print(product)
