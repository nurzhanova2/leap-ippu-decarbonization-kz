"""Extract national IPPU-relevant activity data from BNS's annual 2021 table."""

import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile


WORKBOOK = Path("data/raw/bns/bns_physical_production_2021.xlsx")
OUTPUT = Path("data/processed/bns_ippu_activity_data_2021_annual.csv")
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


with zipfile.ZipFile(WORKBOOK) as archive:
    strings = shared_strings(archive)
    worksheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
    rows = [row_values(row, strings) for row in worksheet.findall(".//m:sheetData/m:row", NAMESPACE)]

year_columns = [column for row in rows for column, value in row.items() if value == "2021"]
if len(year_columns) != 1:
    raise ValueError(f"Expected exactly one 2021 header, found {year_columns}")
year_column = year_columns[0]

records = []
for index, row in enumerate(rows):
    product = row.get("A", "")
    if not any(keyword in product.lower() for keyword in KEYWORDS):
        continue
    unit = product.rsplit(", ", 1)[-1] if ", " in product else "not_stated"
    records.append({
        "year": "2021",
        "ippu_category": "to_be_mapped_after_inventory_review",
        "product": product,
        "product_definition": "BNS physical industrial output; gross output definition",
        "source_dataset": "BNS annual physical industrial production 2021",
        "source_table_or_sheet": "Лист1; national product row",
        "source_value": row.get(year_column, ""),
        "source_unit": unit,
        "conversion_factor_to_tonnes": "",
        "standardised_value_tonnes": "",
        "reporting_notation": row.get(year_column, "") if row.get(year_column, "") in {"-", "..", "х"} else "numeric_or_blank",
        "comparability_status": "requires_match_to_UNFCCC_activity_data",
        "notes": "Extracted automatically; source file and product label retained",
    })

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print(f"Wrote {len(records)} records to {OUTPUT}")
for record in records:
    print(record["product"], "=", record["source_value"], record["source_unit"])
