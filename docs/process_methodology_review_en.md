# Activity-data comparability and NID/NIR methodology review

Русская версия: [process_methodology_review.md](process_methodology_review.md).

## Status and interpretation rule

Targeted NID 2025 and NIR 2023 method sections have been reviewed for lime, iron/steel, ferroalloys and primary aluminium. Together with the previously reviewed clinker and zinc sections, they allow BNS–UNFCCC comparisons to be interpreted at process level rather than from table values alone.

**Rule:** a numerical difference can be called a data discrepancy only after product, unit, geography, technological stream, and plant-versus-national-output boundary are confirmed to be the same.

Full machine-readable table: [`data/processed/ippu_process_comparability_2021.csv`](../data/processed/ippu_process_comparability_2021.csv).

## 2021 comparability summary

| Process | BNS, Mt | UNFCCC, Mt | Unit and product | UNFCCC activity-data boundary | Comparability | Conclusion |
|---|---:|---:|---|---|---|---|
| Clinker, 2.A.1 | 7.295700 | 7.295700 | tonnes; cement clinker | national BNS clinker output | direct | Exact agreement; Portland cement cannot replace clinker. |
| Lime, 2.A.2 | 0.933623 | 0.933623 | tonnes; hydrated, quick and hydraulic lime | national BNS aggregate, including own-use lime | direct at aggregate level | Exact agreement; NID uses an 85/15 split for lime types. |
| Pig iron, 2.C.1.b | 3.623764 | 3.195305 | tonnes; BNS covers primary pig-iron forms | Qarmet integrated-plant data and carbon balance | not direct | The −11.8% difference reflects boundaries, not an established error. |
| Crude steel, 2.C.1.a | 4.526071 | 4.526071 | tonnes; crude steel | national BNS data, complemented by Qarmet inputs for carbon balance | direct as output indicator | Exact agreement; output alone is insufficient to calculate emissions. |
| Ferroalloys, 2.C.2 | 2.070038 | 2.070038 | tonnes; ferroalloys | national BNS output; Kazchrome data for reducer/EF | direct as total output | Exact agreement; retain alloy mix and plant data for EF calculation. |
| Primary aluminium, 2.C.3 | — | — | available BNS long series combines aluminium and aluminium oxide | Kazakhstan Electrolysis Plant: output, anodes/reductants, anode effect | no valid comparison | Obtain disaggregated or plant data; the published BNS aggregate is unsuitable. |
| Zinc, 2.C.6 | 0.300886 | 0.081861 | tonnes; BNS unwrought zinc, CRT zinc from Waelz cakes | KazZinc technological stream | not direct | The −72.8% difference is not a data-quality metric. |

The difference is `(UNFCCC − BNS) / BNS`. A negative value merely shows that a narrower UNFCCC measure was compared with a wider BNS measure.

## Process-level methodology review

### 2.A.1 Clinker

NID 2025 uses BNS clinker, not Portland-cement, output; both sources report 7,295.7 kt in 2021. The initial comparison against 12,312.7 kt of Portland cement was methodologically invalid. Source: NID 2025, p.157.

### 2.A.2 Lime

NID 2025 (p.160) and NIR 2023 (pp.188–191) establish that activity data are total BNS output of hydrated, quick and hydraulic lime, including non-market own-use lime. National statistics do not separate high-calcium and dolomitic lime; NID applies an 85/15 split and IPCC 2006 Tier 1 factors of 0.75 and 0.86 t CO2/t, respectively. Thus the 933.623 kt agreement is valid for aggregate activity data, not for product composition.

### 2.C.1 Iron and steel

NID 2025 (pp.179–184) and NIR 2023 (pp.213–218) use IPCC 2006 Tier 2, practically approaching Tier 3 when enterprise data are available. For pig iron, inventory inputs originate from Qarmet (formerly ArcelorMittal Temirtau) and include coke, limestone and carbon-balance information. The 3.195305 Mt is therefore a plant-model input, not necessarily the full national BNS output of 3.623764 Mt.

For steel, NID 2025 explicitly identifies BNS as the source of production volumes, supplemented by Qarmet and electric-steel parameters for the carbon balance. BNS and CRT both report 4.526071 Mt in 2021. This validates output comparability, but not emission estimation by multiplying output by a universal factor.

### 2.C.2 Ferroalloys

NID 2025 (pp.190–191) and NIR 2023 (pp.225–228) apply Tier 2: total BNS output is combined with Kazchrome reducer data. The difference between enterprise and BNS production is represented as other producers. The 2.070038 Mt match validates the total-output indicator, but LEAP calibration should retain alloy types and reducer consumption. NID assesses activity-data uncertainty at below 10% and total CO2 uncertainty at 7.1%; these are NID assessments, not independent estimates by this study.

### 2.C.3 Primary aluminium

NID 2025 (pp.194–195) and NIR 2023 (pp.228–232) describe the single producer, Kazakhstan Electrolysis Plant. Inputs include output, anode/reductant materials and anode-effect parameters; the method is Tier 3-like. The published BNS long series combines unwrought aluminium with aluminium oxide, so no valid comparison is possible. This is a material data gap for later LEAP work and should not be hidden by imputation.

### 2.C.6 Zinc

NID 2025 (p.200) defines activity data as zinc produced from Waelz cakes in Waelz kilns at KazZinc. In 2021 this is 81.861 kt, versus 300.886 kt of total BNS unwrought-zinc output. These are different production populations; the percentage comparison may illustrate non-comparability but cannot demonstrate unreliability of either BNS or UNFCCC data.

## Use in the article

In *Results*, report comparability status rather than rank processes by the absolute percentage difference. In *Discussion*, the supported conclusion is: “National statistics and inventory activity data are aligned for clinker, aggregate lime, steel and total ferroalloy output. Large apparent differences for pig iron and zinc arise when national output is mixed with plant-specific or technologically narrow streams. For primary aluminium, open statistics do not provide a fit-for-purpose activity-data series.”

