"""Fill a LEAP Export-to-Excel template while preserving its import identifiers.

The script only replaces the Expression cells in column L.  It deliberately
leaves BranchID, VariableID, ScenarioID, RegionID, paths, units and sheet
layout untouched, so the resulting workbook can be read by LEAP's
Import-from-Excel command.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("", NS)

# 2023 CRT values converted to the native LEAP units exported in the template.
CURRENT = {
    344: 4345666.0,    # Cement clinker CO2 (template label is currently IPPU)
    345: 721506.0,     # Lime CO2
    347: 24480.0,      # Glass CO2
    349: 4545014.3,    # Other carbonate uses CO2
    357: 5041002.44,   # Pig iron CO2
    359: 432644.70,    # Steel CO2
    360: 3425548.28,   # Ferroalloys CO2
    361: 36894.0,      # Ferroalloys CH4, kg
    362: 403736.76,    # Aluminium CO2 (PFC excluded from model boundary)
    363: 274662.10,    # Zinc CO2
    365: 3538879.52,   # Sinter CO2
    367: 287330.44,    # Pellets CO2
    352: 326017.90,    # Ammonia CO2
    354: 592400.0,     # Nitric acid N2O, kg
    356: 27426.0,      # Calcium carbide CO2
}

# Factors at 2030 and 2050, indexed by LEAP branch IDs. Baseline is held at
# the calibrated 2023 level. Moderate and ambitious are explicitly
# illustrative sensitivity pathways, not policy forecasts.
MINERAL = {344, 345, 347, 349}
METALS = {357, 359, 360, 361, 362, 363, 365, 367}
CHEMICALS = {352, 354, 356}


def scenario_expression(branch_id: int, scenario: str) -> str:
    value = CURRENT[branch_id]
    if scenario == "Baseline":
        f2030, f2050 = 1.0, 1.0
    elif scenario == "Moderate mitigation":
        if branch_id in MINERAL:
            f2030, f2050 = 0.85, 0.60
        elif branch_id in METALS:
            f2030, f2050 = 0.90, 0.65
        else:
            f2030, f2050 = 0.90, 0.65
    elif scenario == "Ambitious mitigation":
        if branch_id in MINERAL:
            f2030, f2050 = 0.70, 0.30
        elif branch_id in METALS or branch_id in CHEMICALS:
            f2030, f2050 = 0.75, 0.35
    else:
        raise ValueError(f"Unexpected scenario: {scenario}")
    return f"Interp(2024,{value:.6f},2030,{value*f2030:.6f},2050,{value*f2050:.6f})"


def text_from_cell(cell: ET.Element, shared: list[str]) -> str:
    value = cell.find(f"{{{NS}}}v")
    if value is None or value.text is None:
        return ""
    return shared[int(value.text)] if cell.get("t") == "s" else value.text


def main(input_path: Path, output_path: Path) -> None:
    with ZipFile(input_path) as source:
        contents = {name: source.read(name) for name in source.namelist()}

    shared_root = ET.fromstring(contents["xl/sharedStrings.xml"])
    shared = ["".join(t.text or "" for t in item.iter(f"{{{NS}}}t")) for item in shared_root]
    shared_index = {value: index for index, value in enumerate(shared)}

    def add_shared(value: str) -> int:
        if value in shared_index:
            return shared_index[value]
        item = ET.SubElement(shared_root, f"{{{NS}}}si")
        text = ET.SubElement(item, f"{{{NS}}}t")
        text.text = value
        shared_index[value] = len(shared)
        shared.append(value)
        return shared_index[value]

    sheet = ET.fromstring(contents["xl/worksheets/sheet1.xml"])
    for row in sheet.findall(f".//{{{NS}}}row"):
        cells = {cell.get("r").rstrip("0123456789"): cell for cell in row.findall(f"{{{NS}}}c")}
        if "A" not in cells or "G" not in cells:
            continue
        try:
            branch_id = int(text_from_cell(cells["A"], shared))
        except ValueError:
            continue
        if branch_id not in CURRENT:
            continue
        scenario = text_from_cell(cells["G"], shared)
        if scenario == "Current Accounts":
            expression = f"{CURRENT[branch_id]:.6f}"
        else:
            expression = scenario_expression(branch_id, scenario)
        expression_cell = cells["L"]
        expression_cell.set("t", "s")
        for child in list(expression_cell):
            expression_cell.remove(child)
        value = ET.SubElement(expression_cell, f"{{{NS}}}v")
        value.text = str(add_shared(expression))

    shared_root.set("count", str(len(shared)))
    shared_root.set("uniqueCount", str(len(shared)))
    contents["xl/sharedStrings.xml"] = ET.tostring(shared_root, encoding="utf-8", xml_declaration=True)
    contents["xl/worksheets/sheet1.xml"] = ET.tostring(sheet, encoding="utf-8", xml_declaration=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", ZIP_DEFLATED) as target:
        for name, data in contents.items():
            target.writestr(name, data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: fill_leap_import_template.py INPUT.xlsx OUTPUT.xlsx")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
