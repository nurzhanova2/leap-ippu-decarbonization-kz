"""Render one PDF page to a PNG for read-only visual inspection."""

import argparse
from pathlib import Path
import fitz


parser = argparse.ArgumentParser()
parser.add_argument("pdf")
parser.add_argument("page", type=int, help="One-indexed page number")
parser.add_argument("output", type=Path)
args = parser.parse_args()

document = fitz.open(args.pdf)
page = document.load_page(args.page - 1)
pixmap = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
args.output.parent.mkdir(parents=True, exist_ok=True)
pixmap.save(args.output)
