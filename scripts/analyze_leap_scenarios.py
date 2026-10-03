"""Create reproducible tables and article figures from LEAP scenario assumptions.

The calculations duplicate the formulas written to the LEAP import workbook:
Current Accounts is the 2023 CRT calibration, Baseline is flat after 2023,
and mitigation scenarios linearly interpolate to their 2030 and 2050 targets.
Only branches included in the LEAP IPPU model are reported.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


PROCESSED = Path("data/processed")
FIGURES = Path("figures")

# Base values in tonnes of gas: identical to the LEAP import workbook.
BASE = {
    "Cement clinker": ("Mineral industry", "CO2", 4_345_666.0),
    "Lime": ("Mineral industry", "CO2", 721_506.0),
    "Glass": ("Mineral industry", "CO2", 24_480.0),
    "Other carbonate uses": ("Mineral industry", "CO2", 4_545_014.3),
    "Pig iron": ("Metal industry", "CO2", 5_041_002.44),
    "Steel": ("Metal industry", "CO2", 432_644.70),
    "Sinter": ("Metal industry", "CO2", 3_538_879.52),
    "Pellets": ("Metal industry", "CO2", 287_330.44),
    "Ferroalloys (CO2)": ("Metal industry", "CO2", 3_425_548.28),
    "Ferroalloys (CH4)": ("Metal industry", "CH4", 36.894),
    "Aluminium": ("Metal industry", "CO2", 403_736.76),
    "Zinc": ("Metal industry", "CO2", 274_662.10),
    "Ammonia": ("Chemical industry", "CO2", 326_017.90),
    "Nitric acid": ("Chemical industry", "N2O", 592.4),
    "Calcium carbide": ("Chemical industry", "CO2", 27_426.0),
}

# AR5 GWP100. The raw CH4 and N2O LEAP effects are converted for aggregate charts.
GWP = {"CO2": 1, "CH4": 28, "N2O": 265}

MINERAL = {"Cement clinker", "Lime", "Glass", "Other carbonate uses"}
METALS = {"Pig iron", "Steel", "Sinter", "Pellets", "Ferroalloys (CO2)",
          "Ferroalloys (CH4)", "Aluminium", "Zinc"}


def factors(name: str, scenario: str) -> tuple[float, float]:
    if scenario == "Baseline":
        return 1.0, 1.0
    if scenario == "Moderate mitigation":
        return (0.85, 0.60) if name in MINERAL else (0.90, 0.65)
    if scenario == "Ambitious mitigation":
        return (0.70, 0.30) if name in MINERAL else (0.75, 0.35)
    raise ValueError(scenario)


def factor_in_year(name: str, scenario: str, year: int) -> float:
    if year == 2023 or scenario == "Baseline":
        return 1.0
    f2030, f2050 = factors(name, scenario)
    if year <= 2030:
        return 1 + (f2030 - 1) * (year - 2023) / 7
    return f2030 + (f2050 - f2030) * (year - 2030) / 20


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    PROCESSED.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    scenarios = ["Baseline", "Moderate mitigation", "Ambitious mitigation"]
    years = list(range(2023, 2051))
    detail_rows = []
    totals = {scenario: [] for scenario in scenarios}
    group_totals = {scenario: {group: [] for group in ("Mineral industry", "Metal industry", "Chemical industry")}
                    for scenario in scenarios}

    for scenario in scenarios:
        for year in years:
            by_group = {group: 0.0 for group in group_totals[scenario]}
            for process, (group, gas, tonnes) in BASE.items():
                kt_co2eq = tonnes * GWP[gas] / 1000 * factor_in_year(process, scenario, year)
                by_group[group] += kt_co2eq
                detail_rows.append({
                    "scenario": scenario,
                    "year": year,
                    "process": process,
                    "group": group,
                    "gas": gas,
                    "emissions_kt_co2eq_ar5": round(kt_co2eq, 6),
                })
            totals[scenario].append(sum(by_group.values()))
            for group in by_group:
                group_totals[scenario][group].append(by_group[group])

    write_csv(PROCESSED / "leap_ippu_scenario_results_2023_2050.csv", detail_rows)

    plt.style.use("seaborn-v0_8-whitegrid")
    colors = {"Baseline": "#455A64", "Moderate mitigation": "#F57C00", "Ambitious mitigation": "#00796B"}
    fig, ax = plt.subplots(figsize=(9.8, 5.7), layout="constrained")
    for scenario in scenarios:
        ax.plot(years, totals[scenario], label=scenario, color=colors[scenario], linewidth=2.5)
        for year in (2030, 2050):
            idx = years.index(year)
            ax.scatter(year, totals[scenario][idx], color=colors[scenario], s=24, zorder=3)
    ax.axvline(2023, color="#616161", linewidth=0.9, linestyle="--")
    ax.text(2023.15, max(totals["Baseline"]) * 1.012, "calibration year", fontsize=8, color="#424242")
    ax.set_xlim(2023, 2050)
    ax.set_ylim(bottom=0)
    ax.set_xlabel("Year")
    ax.set_ylabel("kt CO$_2$eq (AR5)")
    ax.set_title("LEAP IPPU scenario pathways, Kazakhstan, 2023–2050")
    ax.legend(frameon=False, loc="upper right")
    fig.savefig(FIGURES / "figure_4_leap_ippu_scenario_pathways_2023_2050.png", dpi=300)
    plt.close(fig)

    # Avoided emissions by broad process group, relative to flat Baseline.
    target_years = [2030, 2050]
    groups = ["Mineral industry", "Metal industry", "Chemical industry"]
    group_colors = {"Mineral industry": "#4E79A7", "Metal industry": "#E15759", "Chemical industry": "#59A14F"}
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.6), sharey=True)
    for ax, scenario in zip(axes, ["Moderate mitigation", "Ambitious mitigation"]):
        bottoms = [0.0, 0.0]
        for group in groups:
            avoided = []
            for year in target_years:
                i = years.index(year)
                avoided.append(group_totals["Baseline"][group][i] - group_totals[scenario][group][i])
            ax.bar([str(year) for year in target_years], avoided, bottom=bottoms,
                   color=group_colors[group], label=group)
            bottoms = [a + b for a, b in zip(bottoms, avoided)]
        for i, value in enumerate(bottoms):
            ax.text(i, value + 170, f"{value:,.0f}", ha="center", fontsize=9)
        ax.set_title(scenario)
        ax.set_ylim(0, max(sum(group_totals["Baseline"][g][years.index(2050)] - group_totals["Ambitious mitigation"][g][years.index(2050)] for g in groups) * 1.13, 1))
    axes[0].set_ylabel("Avoided emissions vs. Baseline\n(kt CO$_2$eq, AR5)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.supxlabel("Year", y=0.105)
    fig.legend(handles, labels, ncol=3, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 0.005))
    fig.suptitle("Avoided IPPU process emissions by group")
    fig.subplots_adjust(left=0.10, right=0.98, top=0.86, bottom=0.22, wspace=0.02)
    fig.savefig(FIGURES / "figure_5_leap_ippu_avoided_emissions_2030_2050.png", dpi=300)
    plt.close(fig)

    print("Wrote scenario table and figures.")


if __name__ == "__main__":
    main()
