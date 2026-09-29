"""Find terms in a PDF and print page numbers plus compact context."""

import argparse
from pypdf import PdfReader


parser = argparse.ArgumentParser()
parser.add_argument("pdf")
parser.add_argument("terms", nargs="+")
args = parser.parse_args()

reader = PdfReader(args.pdf)
print(f"pages={len(reader.pages)}")
for page_number, page in enumerate(reader.pages, start=1):
    content = page.extract_text() or ""
    lowered = content.lower()
    for term in args.terms:
        position = lowered.find(term.lower())
        if position >= 0:
            snippet = " ".join(content[max(0, position - 80):position + len(term) + 160].split())
            print(f"page={page_number} term={term}: {snippet}")
