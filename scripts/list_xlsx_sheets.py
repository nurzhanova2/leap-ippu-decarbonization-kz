"""List sheet names in an XLSX without modifying the workbook."""

import sys
import xml.etree.ElementTree as ET
import zipfile


NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

for filename in sys.argv[1:]:
    with zipfile.ZipFile(filename) as archive:
        root = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = [sheet.attrib["name"] for sheet in root.findall("m:sheets/m:sheet", NS)]
    print(filename)
    for sheet in sheets:
        print(f"- {sheet}")
