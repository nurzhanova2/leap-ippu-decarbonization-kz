"""Produce reproducible IPPU trend, composition and CRF--CRT comparison outputs.

Inputs are the long-form files generated from unmodified UNFCCC workbooks.
The script writes analysis tables to ``data/processed`` and publication-ready
PNG figures to ``figures``. CRT total CO2eq uses AR5; CRF total CO2eq is
recalculated with AR4. Therefore the CO2eq version comparison is displayed as
a reporting-comparison signal, not as a pure inventory revision.
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


EMISSIONS = Path("data/processed/unfccc_ippu_emissions_1990_2023.csv")
VERSION_COMPARISON = Path("data/processed/crf_2023_vs_crt_2025_ippu_comparison_1990_2021.csv")
PROCESSED = Path("data/processed")
FIGURES = Path("figures")
CATEGORY_CODES = ["2.A", "2.B", "2.C", "2.D", "2.E", "2.F", "2.G", "2.H"]
CATEGORY_LABELS = {
    "2.A": "2.A Mineral industry",
    "2.B": "2.B Chemical industry",
    "2.C": "2.C Metal industry",
    "2.D": "2.D Fuel / solvent use",
    "2.E": "2.E Electronics",
    "2.F": "2.F F-gases",
    "2.G": "2.G Other product use",
    "2.H": "2.H Other",
}


def read_csv(path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    if not rows:
        raise ValueError(f"No rows to write to {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    PROCESSED.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    rows = read_csv(EMISSIONS)
    crt = [row for row in rows if row["source"] == "UNFCCC CRT 2025"]
    index = {(int(row["inventory_year"]), row["category_code"]): row for row in crt}
    years = list(range(1990, 2024))

    historical = []
    shares = []
    values_by_category = {code: [] for code in CATEGORY_CODES}
    totals = []
    for year in years:
        total = float(index[year, "2"]["total_ghg_kt_co2eq"])
        totals.append(total)
        previous = totals[-2] if len(totals) > 1 else None
        historical.append({
            "inventory_year": year,
            "total_ippu_kt_co2eq_ar5": total,
            "annual_change_kt_co2eq": "" if previous is None else total - previous,
            "annual_change_percent": "" if previous in (None, 0) else (total - previous) / previous * 100,
        })
        for code in CATEGORY_CODES:
            value = float(index.get((year, code), {"total_ghg_kt_co2eq": 0})["total_ghg_kt_co2eq"])
            values_by_category[code].append(value)
            shares.append({
                "inventory_year": year,
                "category_code": code,
                "category_label": CATEGORY_LABELS[code],
                "emissions_kt_co2eq_ar5": value,
                "share_of_total_ippu_percent": value / total * 100 if total else "",
            })

    write_csv(PROCESSED / "ippu_historical_summary_1990_2023.csv", historical)
    write_csv(PROCESSED / "ippu_category_shares_1990_2023.csv", shares)

    comparisons = [
        row for row in read_csv(VERSION_COMPARISON)
        if row["category_code"] == "2"
    ]
    write_csv(PROCESSED / "crf_crt_total_ippu_comparison_1990_2021.csv", comparisons)

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5.6), layout="constrained")
    ax.plot(years, totals, color="#00695C", linewidth=2.5, marker="o", markersize=3)
    for year in (1990, 1996, 2023):
        value = totals[years.index(year)]
        ax.scatter(year, value, color="#E65100", zorder=3)
        ax.annotate(f"{year}: {value:,.0f}", (year, value), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=9)
    ax.set_title("Kazakhstan IPPU emissions, 1990–2023")
    ax.set_ylabel("kt CO$_2$eq (AR5)")
    ax.set_xlabel("Inventory year")
    ax.set_xlim(1989.3, 2023.7)
    fig.savefig(FIGURES / "figure_1_ippu_total_emissions_1990_2023.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5.8), layout="constrained")
    colors = ["#4E79A7", "#F28E2B", "#59A14F", "#E15759", "#B07AA1", "#76B7B2", "#EDC948", "#9C755F"]
    ax.stackplot(years, *(values_by_category[code] for code in CATEGORY_CODES),
                 labels=[CATEGORY_LABELS[code] for code in CATEGORY_CODES], colors=colors, alpha=0.9)
    ax.set_title("Composition of Kazakhstan IPPU emissions by IPCC category")
    ax.set_ylabel("kt CO$_2$eq (AR5)")
    ax.set_xlabel("Inventory year")
    ax.set_xlim(1990, 2023)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8, frameon=False)
    fig.savefig(FIGURES / "figure_2_ippu_category_composition_1990_2023.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    comparison_years = [int(row["inventory_year"]) for row in comparisons]
    total_diff = [float(row["total_difference_percent_of_crf"]) for row in comparisons]
    co2_diff = [float(row["co2_difference_percent_of_crf"]) for row in comparisons]
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True, layout="constrained")
    for ax, series, title, color in (
        (axes[0], total_diff, "Total CO$_2$eq difference: CRT 2025 (AR5) − CRF 2023 (AR4)", "#8E24AA"),
        (axes[1], co2_diff, "CO$_2$ difference: CRT 2025 − CRF 2023", "#1565C0"),
    ):
        ax.axhline(0, color="#424242", linewidth=0.8)
        ax.plot(comparison_years, series, color=color, linewidth=1.7)
        ax.set_ylabel("Difference, % of CRF")
        ax.set_title(title, fontsize=10)
    axes[1].set_xlabel("Inventory year")
    axes[1].set_xlim(1990, 2021)
    fig.suptitle("Comparison of total IPPU emissions in two UNFCCC submissions", fontsize=13)
    fig.savefig(FIGURES / "figure_3_crf_2023_vs_crt_2025_total_ippu_comparison.png", dpi=300)
    plt.close(fig)

    minimum = min(historical, key=lambda row: float(row["total_ippu_kt_co2eq_ar5"]))
    print(f"Wrote historical tables and figures. Minimum: {minimum['inventory_year']} = "
          f"{float(minimum['total_ippu_kt_co2eq_ar5']):,.3f} kt CO2eq.")


if __name__ == "__main__":
    main()

