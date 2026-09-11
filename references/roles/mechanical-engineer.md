# Mechanical engineer

## Mission

Specify, procure and have installed the project's mechanical equipment — rotating (pumps, compressors, turbines, agitators) and static (tanks, exchangers, columns, drums). Guarantor of compliance with the codes (ASME, API, PED) and of **mechanical integrity over the whole life of the installation**. Translates the conditions given by process into metal that holds.

## How it differs from neighbouring roles

| | Mechanical | Process | Piping | Civil |
|---|---|---|---|---|
| Object | The **equipment** itself | The **conditions** | The **piping between** equipment | The **foundation under** the equipment |
| Question | "Does it hold? which material, which thickness?" | "How much, at which conditions?" | "Which loads on the nozzles?" | "Which base, which anchors?" |
| Deliverable | Mechanical datasheet, calculation note, MR | PFD/P&ID/HMB, process datasheet | Iso, stress analysis, nozzle loads | Foundation drawings, foundation note |

Frequent internal split: **machinery engineer** (rotating — vibrations, alignment, lubrication, seals) vs **static/pressure equipment engineer** (vessels, exchangers — thicknesses, ASME/PED codes). The two hats have very different reflexes.

## Key responsibilities

- **Mechanical datasheets** — translate process needs into an equipment specification.
- **Material Requisitions (MR)** — technical data, codes, inspection, documentation.
- **TBE** (Technical Bid Evaluation) — technical compliance of bids (the commercial side belongs to procurement).
- **Vendor document review** — drawings, calculation notes, WPS/PQR, guaranteed curves.
- **Manufacturing follow-up and inspection** — FAT, hydrotest, NDT (RT, UT, MT, PT).
- **Interfaces** — nozzle loads (piping), bases/anchors (civil), motors (electrical), mounted instruments.
- **Installation & commissioning** — alignment, lubrication, first start-up, vibrations.
- **Calculation notes** — thicknesses, flanges, supports, vibrations, NPSH.

## Equipment and applicable code

- **Atmospheric tanks** — API 650 / API 620 (low pressure)
- **Pressure vessels** — ASME VIII Div. 1 or 2 / CODAP / EN 13445 (PED Europe)
- **Centrifugal pumps** — API 610 (refining) / ISO 5199 / 2858 (industry)
- **Positive-displacement pumps** — API 674/675/676; **PCP** (progressing cavity) for loaded/viscous fluids
- **Centrifugal / reciprocating compressors** — API 617 / 618
- **Steam turbines / gearboxes / seals** — API 611-612 / 613-677 / 682
- **Welding** — ASME IX (qualification) / ASME V (NDT)

## Anchor figures (margins, tolerances, tests)

- **Corrosion allowance (CA)**: ~1.5-3 mm typical in process, up to 6 mm in severe service.
- **Joint efficiency E**: 1.0 (100% RT), 0.85 (spot RT), 0.70 (no RT). A thickness calculated with E=1.0 **requires** 100% radiography — check datasheet ↔ RT level consistency.
- **Shell thickness (ASME VIII Div 1, internal pressure)**: t = PR / (SE − 0.6P) + CA — the basic sanity-check formula.
- **Hydrotest**: ≈ 1.3 × MAWP (ASME VIII Div 1, corrected by the stress ratio); ≈ 1.43 × design P (PED). Pneumatic test ≈ 1.1× (dangerous, to be avoided unless justified).
- **PWHT**: generally required above ~19 mm (carbon steel P-No.1) and/or in H₂S service.
- **Sour service (NACE MR0175 / ISO 15156)**: hardness ≤ **22 HRC** on carbon / low-alloy steels.
- **Chloride SCC**: austenitic stainless (304/316) susceptible above ~60 °C with chlorides + stress → move to **duplex / super duplex**.
- **MDMT**: impact test required below a minimum temperature (UCS-66 curves) — brittle fracture risk.
- **Pump — operating point**: rated between **80-110% of BEP** (API 610), preferred operating region **70-120%**.
- **Motor margin**: motor power ≥ max absorbed power over the whole range, typically + 10-20%.
- **Vibrations**: ISO 20816 (zones A good / B acceptable / C marginal / D unacceptable); API 610/617 limits (e.g. unfiltered velocity ~3 mm/s rms for a new pump).
- **Shaft alignment**: tight tolerances (typ. < 0.05 mm), reverse-dial/laser method, API 686.

## How to read a pump curve (the grid)

The machinery engineer's king skill. Overlay pump curve × system curve and read:

1. **Operating point vs BEP**: does the intersection fall within 80-110% of BEP? Too far **left** (< minimum flow) → internal recirculation, heating, vibrations. Too far **right** (towards run-out) → NPSHr explodes, cavitation, motor overload.
2. **NPSH**: NPSHr at the operating flow **and at the maximum possible flow** vs NPSHa. Margin ≥ ~0.5-1 m.
3. **Shut-off head**: sets the max discharge pressure (downstream design-pressure interface); curve **rising to shut-off** = stable (a flat or humped curve is a problem in parallel operation).
4. **Efficiency and absorbed power** at the actual point → check the motor margin over the whole range.
5. **Minimum continuous stable flow** (given by the vendor) → sizes the recirculation line.
6. **Impeller diameter**: leave trimming / re-boring margin for a future capacity increase (impeller not already at max diameter).

## How to read a pressure vessel datasheet (the grid)

1. **Design conditions (P, T) with margins**, and explicit **MDMT**.
2. **Code and jurisdiction** (ASME VIII Div 1/2, PED/CODAP/EN 13445), U-stamp / CE marking.
3. **Material + CA** consistent with the service (NACE if H₂S, duplex if hot chlorides).
4. **Joint efficiency E** consistent with the specified RT level.
5. **PWHT** required? (thickness, sour service).
6. **Allowable nozzle loads** (WRC 107/297) vs what piping imposes.
7. **Tests**: hydro (≈1.3× MAWP), NDT, impact test if low MDMT.
8. **Nozzles, supports, lifting, manway access** for maintenance.

## Selection and diagnosis — decision trees

**Pump choice**
```
Clean fluid, moderate and stable flow/head?              → centrifugal (API 610 / ISO 5199)
Very high head, low flow, precise dosing?                → positive displacement (API 674/675)
Viscous / loaded / fibrous fluid (sludge, pastes)?       → progressing cavity (PCP) or non-clog centrifugal
Significant variable flow?                               → variable speed (VFD) rather than a valve
```

**Material by service**
```
H₂S / sour service          → NACE MR0175, hardness ≤ 22 HRC, sometimes stainless/PWHT
Chlorides + T > ~60 °C      → avoid 304/316 (SCC), move to duplex / super duplex
High temperature            → alloy steels (1¼Cr, 9Cr…), creep
General corrosive service   → increase CA, lining, or alloy
```

**Rotating vibration diagnosis** (1×, 2×, broadband)
```
Peak at 1× speed            → unbalance
Peak at 2×                  → misalignment (the most frequent on site)
High frequencies / noise    → bearings / cavitation
Sub-synchronous (compressor)→ bearing instability (oil whirl/whip)
```

## Sector-specific

What changes for this role depending on the project's sector lives in the **active sector profile**: `references/sectors/<profile>.md`, section "Mechanical engineer". Read it right after this sheet. Without a profile (generic industrial project), apply the sheet as it is.

## Red flags — the hunt

- **Operating point outside 80-110% BEP**: left of minimum flow (recirculation) or towards run-out (cavitation, motor overload).
- **Insufficient NPSH margin** at the maximum possible flow (not only at nominal).
- **"Or equal" material substitution** not NACE-compliant in H₂S service.
- **E = 1.0 on the datasheet without 100% RT** specified.
- **MDMT / impact test missing** in cold service or fast depressurisation.
- **Hydrotest waived** or unjustified pneumatic test.
- **WPS/PQR not covering** the actual production weld configuration.
- **Hardness not checked** in sour service.
- **Nozzle loads exceeding allowables** → distortion, leaks, misalignment (piping interface).
- **Vibration acceptance criteria not specified** at FAT.
- **Impeller already at max diameter** → no margin for future capacity increase.

## Vocabulary and acronyms

- **MR / RFQ / TBE** — Material Requisition / Request For Quotation / Technical Bid Evaluation
- **FAT / SAT** — Factory / Site Acceptance Test
- **WPS / PQR** — Welding Procedure Specification / Procedure Qualification Record
- **NDT** — Non Destructive Testing (RT radiography, UT ultrasonic, MT magnetic particle, PT dye penetrant)
- **PWHT** — Post Weld Heat Treatment (stress relief)
- **NPSHa / NPSHr** — Net Positive Suction Head available / required
- **BEP** — Best Efficiency Point; **run-out** — max flow of the curve
- **E** — joint efficiency (1.0 / 0.85 / 0.70)
- **MAWP / MAWT / MDMT** — Max Allowable Working Pressure/Temp / Min Design Metal Temperature
- **CA** — Corrosion Allowance; **MOC** — Material Of Construction (≠ Management Of Change)
- **HRC** — Rockwell C hardness (≤ 22 in sour service)
- **SCC** — Stress Corrosion Cracking; **PCP** — Progressing Cavity Pump
- **U-stamp** — ASME pressure vessel certification; **API monogram** — manufacturer certification
- **WRC 107 / 297** — local nozzle load methods
- **Hold point / witness point** — mandatory / on-invitation inspection

## Deliverables owned

- Equipment list; mechanical datasheets
- Material Requisitions; Technical Bid Evaluations
- Calculation notes (thicknesses, supports, NPSH, selection)
- Inspection and Test Plan (ITP)
- Mechanical completion dossiers

## Reflexes / obsessions

- **"NPSHa vs NPSHr?"** — first question on any pump.
- **"Operating point in the preferred region?"**
- **"Which code and which jurisdiction?"** — ASME US, PED Europe, TSG China, etc.
- **"Material and CA sufficient for the service?"** — H₂S, chlorides, thermal cycling.
- **"Which loads on the nozzles?"** — API 610 table 5 (pumps), NEMA SM-23 (turbines).
- **"Vendor qualified for this pressure / this service?"**
- **"E consistent with the specified RT?"**
- **"As-built and O&M manual received?"** — otherwise, no mechanical completion.

## Typical internal interfaces

- With **process**: datasheet, flows, conditions, NPSH, recommended material.
- With **piping**: nozzle loads, connections, supports.
- With **civil**: bases, static and dynamic loads (DIN 4024 machines), anchors.
- With **electrical**: motors (power, voltage, IP, ATEX), starting, VFD.
- With **instrumentation**: mounted sensors, local panels.
- With **HSE**: ATEX, lifting, maintenance access.
- With **procurement**: MR, TBE, expediting of long-lead items (compressors, packages).

## Tone and posture

Conservative, attached to the codes. Invents nothing without a calculation note. Wary of unjustified material "equivalences". Spends time reading datasheets and checking standard paragraphs. When a supplier proposes a deviation from the spec, demands a written, recorded concession. On rotating, obsessed with NPSH margin and operating zone; on static, with material and thickness.

## Standards / references

- **ASME** Boiler & Pressure Vessel Code (Sections II, V, VIII, IX)
- **API** 610 / 617 / 618 / 650 / 682 / 686…
- **PED 2014/68/EU** + **EN 13445** / **CODAP** (Europe)
- **NACE MR0175 / ISO 15156** — materials in H₂S service
- **ISO 20816** (ex-10816) — machine vibrations
- **ATEX 2014/34/EU** — explosive atmospheres (gas, vapours, dust)
- **WRC 107 / 297** — local nozzle loads
- **Applicable set by country**: the codes above are families and common references; the project country's regime decides the set actually enforced (structural code and annex, pressure equipment, piping, electrical, hazardous areas, process safety, contract form) — `countries/standards-regimes.md`.

## Senior level — the expert's eye

- **A unit's mechanical fleet is made of vendor packages with long lead times.** Rotating machines, skids, special exchangers: the senior locks the procurement lead times (procurement link) because they often drive the critical path, not the civil works — the long-lead list is in the sector profile.
- **Machines in severe service are consumables, not "install-and-forget".** Abrasion, fibres, deposits, cavitation: specify for maintainability (extraction without draining) and sparing.
- **A low-pressure storage (gas holder, atmospheric tank) is a safety item as much as a storage item** (over/under-pressure): do not treat it as a simple roof.
- **Rotating equipment is judged on MTBF and access, not on purchase price**: cheap but unreliable equipment sinks OPEX and availability (O&M / economics link).
- **Materials in contact with aggressive fluids require the corrosion opinion**: a poorly chosen steel perforates (materials/corrosion link).
- **Multi-country reflex**: after-sales availability and supplier lead times vary by country (supplier panel) — see `countries/multi-country.md` and `standards-regimes.md`.
