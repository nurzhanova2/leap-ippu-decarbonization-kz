"""Activity-growth and factor sensitivity runs on the CRT 2026 inventory 2024 base.

These runs belong to the journal version. The archived conference outputs
(CRT 2025 proxy base, Figures 1-5) are not touched.

Emissions = activity x intensity x f(t), and x s for 2.A.4.d:
- activity: CRT 2026 activity data for 2024 (the inventory base year), times a
  growth multiplier after 2024; for 2.A.4.a+b and 2.A.4.d, whose activity data
  are heterogeneous or inconsistent, CO2 is used as the activity proxy;
- intensity: CRT 2026 emissions / CRT 2026 activity for 2024, held constant;
- f(t): the same Interp() rule as the LEAP expressions (1 in 2024, linear to
  f2030 and f2050); AR5 GWP100 (CO2 = 1, CH4 = 28, N2O = 265).

Growth variants (data/metadata/leap_growth_variants.csv): zero; the 2010-2023
trend applied to 2030; the official 2025-2029 sector forecast (value added, an
upper estimate); 1.5% per year to 2050. Half of the official rates to 2050 is
kept only as a stress test and is reported separately from these variants.

Factor sets: the presented factors (as in the LEAP workbook, including the
mineral-group factors for 2.A.4) and the literature low, central and high
factors (2.A.4.a+b and 2.A.4.d at f = 1.00). With zero growth the presented
set reproduces the main journal scenarios (leap_ippu_scenario_results_
2024_2050_crt2026.csv); the script stops if it does not.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


METADATA = Path("data/metadata")
PROCESSED = Path("data/processed")
FIGURES = Path("figures")
SUFFIX = "_crt2026"
BASE_YEAR = 2024

GWP = {"CO2": 1, "CH4": 28, "N2O": 265}
YEARS = list(range(BASE_YEAR, 2051))
A4AB = "Other carbonate uses: ceramics and soda ash (2.A.4.a+b)"
A4D = "Other carbonate uses: limestone and dolomite (2.A.4.d)"
PLAUSIBLE = ["zero", "trend", "official", "constant_1_5"]
STRESS = "stress_half_official"
GROWTH_VARIANTS = PLAUSIBLE + [STRESS]
GROWTH_LABELS = {"zero": "zero growth", "trend": "BNS trend to 2030", "official": "official 2025–2029 (upper)",
                 "constant_1_5": "1.5%/yr to 2050", STRESS: "stress test: half official to 2050"}
REFERENCE_GROWTH = "trend"
FAMILIES = [  # case family, factor set, factor key
    ("Baseline-growth", "presented", "Baseline"),
    ("Moderate-growth", "presented", "Moderate mitigation"),
    ("Ambitious-growth", "presented", "Ambitious mitigation"),
    ("Literature-low", "literature", "low"),
    ("Literature-central", "literature", "central"),
    ("Literature-high", "literature", "high"),
]


def read(name: str, folder: Path = METADATA) -> list[dict]:
    with (folder / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def interp_factor(f2030: float, f2050: float, year: int) -> float:
    """Same linear Interp() rule as the LEAP expressions."""
    if year <= BASE_YEAR:
        return 1.0
    if year <= 2030:
        return 1 + (f2030 - 1) * (year - BASE_YEAR) / 6
    return f2030 + (f2050 - f2030) * (year - 2030) / 20


def load_processes() -> dict[str, dict]:
    params = {row["process"]: row for row in read(f"leap_scenario_parameters{SUFFIX}.csv")}
    series = defaultdict(dict)
    for row in read(f"unfccc_ippu_activity_data_1990_{BASE_YEAR}{SUFFIX}.csv", PROCESSED):
        series["crt_activity:" + row["category_code"]][int(row["inventory_year"])] = float(row["activity_value_kt"])
    a4 = defaultdict(dict)
    for row in read(f"crt_2a4_subcategories_1990_{BASE_YEAR}{SUFFIX}.csv", PROCESSED):
        if row["row_level"] == "subcategory" and row["co2_kt"] not in ("NO", "NA", ""):
            a4[row["category_code"]][int(row["inventory_year"])] = float(row["co2_kt"])
    series["crt_2a4_co2:2.A.4.a+2.A.4.b"] = {y: a4["2.A.4.a"][y] + a4["2.A.4.b"][y] for y in a4["2.A.4.a"]}
    series["crt_2a4_co2:2.A.4.d"] = dict(a4["2.A.4.d"])

    growth = {row["process"]: row for row in read("leap_growth_variants.csv")}
    lit = {row["process"]: row for row in read("leap_sensitivity_factors.csv")}
    mineral = params["Other carbonate uses"]
    mineral_f = {k: (float(mineral[f"{p}_f2030"]), float(mineral[f"{p}_f2050"]))
                 for k, p in (("Moderate mitigation", "moderate"), ("Ambitious mitigation", "ambitious"))}

    processes = {}
    for name, g in growth.items():
        if name in params:
            p = params[name]
            gas, group, base_t = p["gas"], p["group"], float(p["base_t"])
            presented = {k: (float(p[f"{q}_f2030"]), float(p[f"{q}_f2050"]))
                         for k, q in (("Moderate mitigation", "moderate"), ("Ambitious mitigation", "ambitious"))}
        else:
            gas, group = "CO2", mineral["group"]
            base_t = 1000 * (a4["2.A.4.d"][BASE_YEAR] if name == A4D else a4["2.A.4.a"][BASE_YEAR] + a4["2.A.4.b"][BASE_YEAR])
            presented = dict(mineral_f)  # as LEAP branch 349, which carries 2.A.4 as a whole
        s = series[g["trend_series"]]
        processes[name] = {
            "category": g["ippu_category"], "group": group, "gas": gas, "base_t": base_t,
            "activity_kt": s[BASE_YEAR], "intensity": base_t / (s[BASE_YEAR] * 1000),
            "activity_unit": "kt CO2 (proxy)" if g["trend_series"].startswith("crt_2a4_co2") else "kt product",
            "series": {y: v for y, v in s.items() if int(g["trend_window_start"]) <= y <= int(g["trend_window_end"])},
            "growth": g, "literature": lit[name], "presented": presented, "mineral": mineral_f,
        }
    return processes


def trend_rate(series: dict[int, float]) -> float:
    years = sorted(series)
    x = [y - years[0] for y in years]
    v = [math.log(series[y]) for y in years]
    mx, mv = sum(x) / len(x), sum(v) / len(v)
    slope = sum((a - mx) * (b - mv) for a, b in zip(x, v)) / sum((a - mx) ** 2 for a in x)
    return math.exp(slope) - 1


def growth_multiplier(proc: dict, variant: str, year: int) -> float:
    g = proc["growth"]
    if variant == "zero" or year <= BASE_YEAR:
        return 1.0
    if variant == "trend":
        return (1 + proc["trend_rate"]) ** (min(year, int(g["trend_last_year"])) - BASE_YEAR)
    if variant == "official":
        last = int(g["official_last_year"])
        return (1 + float(g["official_rate_pct"]) / 100) ** (min(year, last) - BASE_YEAR)
    rate = float(g["constant_rate_pct" if variant == "constant_1_5" else "half_official_rate_pct"]) / 100  # stress test
    return (1 + rate) ** (min(year, int(g["long_last_year"])) - BASE_YEAR)


def factors_for(name: str, proc: dict, factor_set: str, key: str, overrides: dict) -> tuple[float, float]:
    if name in overrides:
        return overrides[name]
    if factor_set == "presented":
        return (1.0, 1.0) if key == "Baseline" else proc["presented"][key]
    lit = proc["literature"]
    return float(lit[f"f2030_{key}"]), float(lit[f"f2050_{key}"])


def run(processes: dict, factor_set: str, key: str, growth: str, f_overrides: dict | None = None,
        s: float = 1.0, a4d_base_scale: float = 1.0, rows: list | None = None, case: str = "") -> dict[int, float]:
    totals = {year: 0.0 for year in YEARS}
    for name, proc in processes.items():
        f2030, f2050 = factors_for(name, proc, factor_set, key, f_overrides or {})
        for year in YEARS:
            activity_index = growth_multiplier(proc, growth, year) * (a4d_base_scale if name == A4D else 1.0)
            activity = proc["activity_kt"] * activity_index
            f = interp_factor(f2030, f2050, year)
            kt = activity * proc["intensity"] * f * (s if name == A4D else 1.0) * GWP[proc["gas"]]
            totals[year] += kt
            if rows is not None:
                rows.append({"case": case, "factor_set": f"{factor_set}: {key}", "growth_variant": growth, "year": year,
                             "process": name, "ippu_category": proc["category"], "group": proc["group"], "gas": proc["gas"],
                             "activity_index_vs_2024": round(activity_index, 6), "activity": round(activity, 6),
                             "activity_unit": proc["activity_unit"], "intensity_t_gas_per_t": round(proc["intensity"], 9),
                             "f": round(f, 6), "emissions_kt_co2eq_ar5": round(kt, 6)})
    return totals


def check_against_main(processes: dict) -> dict:
    main = defaultdict(lambda: defaultdict(float))
    for row in read(f"leap_ippu_scenario_results_2024_2050{SUFFIX}.csv", PROCESSED):
        main[row["scenario"]][int(row["year"])] += float(row["emissions_kt_co2eq_ar5"])
    for key in ("Baseline", "Moderate mitigation", "Ambitious mitigation"):
        totals = run(processes, "presented", key, "zero")
        worst = max(abs(totals[y] - main[key][y]) for y in YEARS)
        if worst > 1e-3:
            raise SystemExit(f"Reproduction check failed for {key}: max difference {worst} kt")
    return main


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def bns_check(processes: dict) -> list[dict]:
    """BNS 2024/2023 index (stage 3) versus the CRT 2026 ratios 2024/2023."""
    activity = defaultdict(dict)
    for r in read(f"unfccc_ippu_activity_data_1990_{BASE_YEAR}{SUFFIX}.csv", PROCESSED):
        activity[r["category_code"]][int(r["inventory_year"])] = float(r["activity_value_kt"])
    out = []
    for row in read("bns_activity_index_2024.csv"):
        act = activity.get(processes[row["process"]]["growth"]["trend_series"].split(":")[1], {})
        crt_activity = act[2024] / act[2023] if 2023 in act and 2024 in act else None
        out.append({"process": row["process"], "ippu_category": row["ippu_category"], "bns_index_2024": row["index_central"],
                    "bns_edition": row["edition"], "crt2026_activity_ratio_2024_2023": round(crt_activity, 4) if crt_activity else "",
                    "difference_pp": round((float(row["index_central"]) - crt_activity) * 100, 1) if crt_activity else "",
                    "bns_quality": row["quality"]})
    return out


# Dataviz reference palette (light surface).
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
SERIES = {"Baseline-growth": "#2a78d6", "Moderate-growth": "#eb6834", "Ambitious-growth": "#1baf7a"}
ORDINAL = {"Literature-high": "#86b6ef", "Literature-central": "#2a78d6", "Literature-low": "#104281"}
LOWER, HIGHER = "#2a78d6", "#e34948"
SHORT = {"Baseline-growth": "Baseline", "Moderate-growth": "Moderate", "Ambitious-growth": "Ambitious",
         "Literature-low": "low", "Literature-central": "central", "Literature-high": "high"}
KT = plt.FuncFormatter(lambda v, _: "0" if v == 0 else f"{v/1000:,.0f}K")


def style_axes(ax) -> None:
    ax.set_facecolor(SURFACE)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.grid(axis="x", visible=False)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
        ax.spines[side].set_linewidth(0.8)
    ax.tick_params(colors=INK2, labelsize=8.5, length=0)
    ax.set_axisbelow(True)


def figure_6(results: dict, main: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.8), sharey=True)
    fig.patch.set_facecolor(SURFACE)
    panels = [("(a) Presented factors with activity growth", ["Baseline-growth", "Moderate-growth", "Ambitious-growth"], SERIES),
              ("(b) Literature-based factors (stage 2)", ["Literature-high", "Literature-central", "Literature-low"], ORDINAL)]
    ymax = max(max(v.values()) for v in results.values()) * 1.06
    for ax, (title, families, colors) in zip(axes, panels):
        style_axes(ax)
        for family in families:
            if family not in ("Literature-low", "Literature-high"):
                band = [[results[(family, g)][y] for g in PLAUSIBLE] for y in YEARS]
                ax.fill_between(YEARS, [min(b) for b in band], [max(b) for b in band], color=colors[family], alpha=0.12, linewidth=0)
            line = [results[(family, REFERENCE_GROWTH)][y] for y in YEARS]
            ax.plot(YEARS, line, color=colors[family], linewidth=2, solid_capstyle="round", label=family)
            ax.scatter([2050], [line[-1]], s=30, color=colors[family], edgecolor=SURFACE, linewidth=1.5, zorder=4)
            ax.annotate(f"{SHORT[family]} {line[-1]:,.0f}", (2050, line[-1]), xytext=(6, 0),
                        textcoords="offset points", va="center", fontsize=8.5, color=INK)
        if families[0] == "Baseline-growth":
            for values in main.values():
                ax.scatter([2030, 2050], [values[2030], values[2050]], s=22, color=MUTED, edgecolor=SURFACE, linewidth=1.2, zorder=5)
            ax.scatter([], [], s=22, color=MUTED, label="Main scenarios, zero growth (2030, 2050)")
        ax.set_title(title, loc="left", fontsize=10, color=INK)
        ax.set_xlim(BASE_YEAR, 2050)
        ax.set_ylim(0, ymax)
        ax.set_xticks([2024, 2030, 2040, 2050])
        ax.yaxis.set_major_formatter(KT)
        ax.legend(frameon=False, fontsize=8, loc="lower left", labelcolor=INK2)
    axes[0].set_ylabel("kt CO$_2$eq (AR5)", color=INK2, fontsize=9)
    fig.suptitle("IPPU process emissions with activity growth, CRT 2026 inventory 2024 base, Kazakhstan, 2024–2050",
                 x=0.06, ha="left", fontsize=11.5, color=INK)
    fig.text(0.06, 0.015, "Lines: BNS 2010–2023 trend applied to 2030, activity constant afterwards. Bands: range across zero growth, the trend, "
             "the official 2025–2029 forecast and 1.5%/yr to 2050 (stress test not shown). In (b) 2.A.4 is kept at f = 1.00.",
             fontsize=7.3, color=INK2, ha="left")
    fig.subplots_adjust(left=0.07, right=0.90, top=0.86, bottom=0.11, wspace=0.30)
    fig.savefig(FIGURES / f"figure_6_leap_ippu_growth_sensitivity_2024_2050{SUFFIX}.png", dpi=300, facecolor=SURFACE)
    plt.close(fig)


def figure_7(tornado: list[dict], reference: float) -> None:
    bars = sorted(tornado, key=lambda r: r["swing"])
    fig, ax = plt.subplots(figsize=(10.4, 0.48 * len(bars) + 1.8))
    fig.patch.set_facecolor(SURFACE)
    style_axes(ax)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID, linewidth=0.6)
    for i, row in enumerate(bars):
        low, high = row["total_low"], row["total_high"]
        if low < reference:
            ax.barh(i, reference - low, left=low, height=0.5, color=LOWER)
        if high > reference:
            ax.barh(i, high - reference, left=reference, height=0.5, color=HIGHER)
        ax.annotate(f"{low:,.0f}  {row['low_setting']}", (low, i), xytext=(-5, 0), textcoords="offset points",
                    ha="right", va="center", fontsize=7.5, color=INK2)
        ax.annotate(f"{row['high_setting']}  {high:,.0f}", (high, i), xytext=(5, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=7.5, color=INK2)
    ax.axvline(reference, color=INK2, linewidth=1)
    ax.set_yticks(range(len(bars)), [row["parameter"] for row in bars], fontsize=8.5, color=INK)
    lo = min(r["total_low"] for r in bars)
    hi = max(r["total_high"] for r in bars)
    ax.set_xlim(lo - (hi - lo) * 0.5, hi + (hi - lo) * 0.5)
    ax.xaxis.set_major_formatter(KT)
    ax.set_xlabel("Included IPPU process emissions in 2050, kt CO$_2$eq (AR5)", color=INK2, fontsize=9)
    ax.set_title(f"What moves the 2050 result: one assumption at a time around the reference ({reference:,.0f} kt)",
                 loc="left", fontsize=11, color=INK)
    ax.legend(handles=[Patch(color=LOWER, label="lowers 2050 emissions"), Patch(color=HIGHER, label="raises 2050 emissions")],
              frameon=False, fontsize=8, loc="lower right", labelcolor=INK2)
    fig.text(0.01, 0.01, "Reference: CRT 2026 inventory 2024 base, literature central factors, BNS trend to 2030, 2.A.4.d with f = 1.00 and s = 1.00.",
             fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIGURES / f"figure_7_leap_ippu_tornado_2050{SUFFIX}.png", dpi=300, facecolor=SURFACE)
    plt.close(fig)


def main() -> None:
    processes = load_processes()
    for proc in processes.values():
        override = proc["growth"]["trend_rate_override_pct"]
        proc["trend_rate"] = float(override) / 100 if override else trend_rate(proc["series"])
    main_scenarios = check_against_main(processes)

    rows, results = [], {}
    for family, factor_set, key in FAMILIES:
        for growth in GROWTH_VARIANTS:
            results[(family, growth)] = run(processes, factor_set, key, growth, rows=rows, case=family)
    write_csv(PROCESSED / f"leap_ippu_sensitivity_2024_2050{SUFFIX}.csv", rows)

    summary = []
    for family, _, _ in FAMILIES:
        for growth in GROWTH_VARIANTS:
            t, base = results[(family, growth)], results[("Baseline-growth", growth)]
            summary.append({"case": family, "growth_variant": growth, "total_2024": round(t[2024], 1),
                            "total_2030": round(t[2030], 1), "total_2050": round(t[2050], 1),
                            "avoided_vs_baseline_growth_2030": round(base[2030] - t[2030], 1),
                            "avoided_vs_baseline_growth_2050": round(base[2050] - t[2050], 1)})
    write_csv(PROCESSED / f"leap_ippu_sensitivity_summary_2030_2050{SUFFIX}.csv", summary)

    # Factors versus growth (literature factors): range across growth sets with the central factors,
    # and range across factor sets (low/high) with the reference growth (trend).
    decomposition = []
    growth_sets = {"growth stops by 2030: zero/trend/official": ["zero", "trend", "official"],
                   "plausible: plus 1.5%/yr to 2050": PLAUSIBLE,
                   "stress test: plus half official to 2050": GROWTH_VARIANTS}
    for year in (2030, 2050):
        f_values = [results[(f"Literature-{k}", REFERENCE_GROWTH)][year] for k in ("low", "high")]
        f_range = max(f_values) - min(f_values)
        for label, variants in growth_sets.items():
            values = [results[("Literature-central", g)][year] for g in variants]
            g_range = max(values) - min(values)
            decomposition.append({"year": year, "growth_set": label, "growth_min": round(min(values), 1), "growth_max": round(max(values), 1),
                                  "growth_range": round(g_range, 1), "factor_min": round(min(f_values), 1), "factor_max": round(max(f_values), 1),
                                  "factor_range": round(f_range, 1), "factor_to_growth_ratio": round(f_range / g_range, 2)})
    write_csv(PROCESSED / f"leap_ippu_sensitivity_decomposition{SUFFIX}.csv", decomposition)

    # Tornado around the reference (literature central factors + trend), one assumption at a time.
    ref = dict(factor_set="literature", key="central", growth=REFERENCE_GROWTH)
    reference = run(processes, **ref)[2050]
    lit = lambda proc, k: (float(proc["literature"][f"f2030_{k}"]), float(proc["literature"][f"f2050_{k}"]))
    groups = {"f: cement clinker": ["Cement clinker"], "f: lime": ["Lime"],
              "f: iron and steel (4 branches)": ["Pig iron", "Steel", "Sinter", "Pellets"],
              "f: ferroalloys": ["Ferroalloys (CO2)", "Ferroalloys (CH4)"], "f: aluminium": ["Aluminium"],
              "f: ammonia": ["Ammonia"], "f: nitric acid": ["Nitric acid"],
              "f: glass, zinc, carbide (author assumption)": ["Glass", "Zinc", "Calcium carbide"]}
    options = {row["parameter"]: row["value"] for row in read("leap_2a4_variants.csv")}
    a4d = processes[A4D]["series"] | {BASE_YEAR: processes[A4D]["activity_kt"]}
    mean_scale = sum(a4d[y] for y in range(BASE_YEAR - 2, BASE_YEAR + 1)) / 3 / a4d[BASE_YEAR]
    variants = {
        "Activity growth after 2024 (plausible)": {GROWTH_LABELS[g]: dict(ref, growth=g) for g in PLAUSIBLE},
        "Stress test: half official rates to 2050": {"reference (trend)": ref, "stress test": dict(ref, growth=STRESS)},
        "f: all processes (literature low/high)": {"all low": dict(ref, key="low"), "all high": dict(ref, key="high")},
        "2.A.4.d: mineral-group factors": {"f = 1.00": ref,
                                           "Ambitious mineral factors": dict(ref, f_overrides={A4D: processes[A4D]["mineral"]["Ambitious mitigation"]})},
        "2.A.4.d: emissive share s": {"s = 1.00": ref, f"s = {options['s_lower_bound']}": dict(ref, s=float(options["s_lower_bound"]))},
        "2.A.4.d: base value": {"2024": ref, "2022–2024 mean": dict(ref, a4d_base_scale=mean_scale)},
    }
    for label, names in groups.items():
        variants[label] = {k: dict(ref, f_overrides={n: lit(processes[n], k) for n in names}) for k in ("low", "high")}
    tornado = []
    for parameter, settings in variants.items():
        totals = {setting: run(processes, **args)[2050] for setting, args in settings.items()}
        low_setting = min(totals, key=totals.get)
        high_setting = max(totals, key=totals.get)
        tornado.append({"parameter": parameter, "low_setting": low_setting, "high_setting": high_setting,
                        "total_low": round(totals[low_setting], 1), "total_high": round(totals[high_setting], 1),
                        "swing": round(totals[high_setting] - totals[low_setting], 1), "reference_2050": round(reference, 1)})
    tornado.sort(key=lambda r: -r["swing"])
    write_csv(PROCESSED / f"leap_ippu_sensitivity_tornado_2050{SUFFIX}.csv", tornado)

    rates = []
    for name, proc in processes.items():
        g = proc["growth"]
        row = {"process": name, "ippu_category": proc["category"], "activity_2024": round(proc["activity_kt"], 3),
               "activity_unit": proc["activity_unit"], "trend_rate_pct_per_year_2025_2030": round(proc["trend_rate"] * 100, 2),
               "official_rate_pct_per_year_2025_2029": g["official_rate_pct"]}
        for variant in GROWTH_VARIANTS:
            m = growth_multiplier(proc, variant, 2050)
            row[f"multiplier_2050_{variant}"] = round(m, 4)
            row[f"average_rate_pct_2024_2050_{variant}"] = round((m ** (1 / 26) - 1) * 100, 2)
        rates.append(row)
    write_csv(PROCESSED / f"leap_ippu_sensitivity_growth_rates{SUFFIX}.csv", rates)
    write_csv(PROCESSED / f"bns_index_2024_check{SUFFIX}.csv", bns_check(processes))
    share = []
    for key in ("Moderate mitigation", "Ambitious mitigation"):
        f2030, f2050 = processes[A4D]["presented"][key]
        for year, f in ((2030, f2030), (2050, f2050)):
            total = main_scenarios["Baseline"][year] - main_scenarios[key][year]
            a4d = processes[A4D]["base_t"] / 1000 * (1 - f)
            share.append({"scenario": key, "year": year, "avoided_total_kt": round(total, 1), "avoided_2A4d_kt": round(a4d, 1),
                          "share_2A4d_percent": round(a4d / total * 100, 1)})
    write_csv(PROCESSED / f"leap_ippu_2a4d_share_of_avoided{SUFFIX}.csv", share)

    figure_6(results, main_scenarios)
    figure_7(tornado, reference)
    print(f"Reference 2050: {reference:,.1f} kt. Wrote sensitivity tables and Figures 6-7 ({SUFFIX}).")


if __name__ == "__main__":
    main()
