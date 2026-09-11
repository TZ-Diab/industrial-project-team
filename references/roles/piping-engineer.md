# Piping engineer

## Mission

Design, specify and have installed all process and utility piping — from the routing in the 3D model to the fabrication isometrics and the supporting of lines in operation. **The discipline with the largest volume of deliverables** (isos, MTO), often the one that drives site progress. Piping makes physical what the P&ID describes in logic.

## How it differs from neighbouring roles

| | Piping | Process | Mechanical | Civil |
|---|---|---|---|---|
| Owns | The **pipe between** the equipment | The **P&ID / the line list** | The **equipment** | The **rack / the foundation** |
| Question | "Which routing, which class, which support?" | "Which line conditions?" | "Which allowable loads on my nozzles?" | "Which loads on the rack?" |
| Deliverable | Iso, MTO, stress, supports | Line list, conditions, slope | Datasheet, nozzle allowables | Rack drawings, bases |

Key boundary: **process gives the line list and the conditions**; piping decides the **physical routing, the class and the support**; and it **imposes loads on mechanical's nozzles**, which answers with the allowables. The nozzle loads ↔ stress analysis loop is the most sensitive interface of the project.

## Key responsibilities

- **Routing** — placing the lines in the 3D model: plot plan, access, supports, flexibility.
- **Piping class / PMS** — per service: material, schedule, flanges, gaskets, manual valves.
- **Material studies** — CS, LTCS, SS304/316, duplex, Ni alloys… + CA (corrosion allowance).
- **Isometrics** — one iso per line/sub-section, basis of shop prefabrication and erection.
- **MTO** — Material Take-Off, basis of bulk costing and purchasing.
- **Stress analysis** — flexibility (CAESAR II, ROHR2, AutoPIPE) on hot / critical lines.
- **Supports** — standard and special types, loads, fixings.
- **Test packages (hydrotest)**; **prefabrication and site follow-up** (welding WPS/PQR, NDT, insulation).

## Piping class — typical example

A piping class carries a code (e.g. A1A, 1A12-S) with: nominal pressure/temperature (ASME 300 lb, –29/350 °C), material (CS ASTM A106 B), schedule by size, flange type (Weld Neck RF), gaskets (spiral-wound stainless + graphite), bolting (A193 B7 / A194 2H), manual valves (ball for isolation, gate/globe by service), tolerances and required NDT. **Every line of the P&ID carries a class; any change of service or conditions = change of class = material transition (spec break).**

## Anchor figures (tests, allowables, spans, NDT)

- **Hydrotest**: **1.5 × design pressure** (ASME B31.3, corrected by the Sc/S ratio at test temperature). Pneumatic 1.1× (dangerous, to be justified).
- **B31.3 stress allowables**:
  - **Sustained** (pressure + weight) ≤ **Sh** (hot allowable).
  - **Expansion** (thermal displacement range) ≤ **SA = f·(1.25 Sc + 0.25 Sh)**.
  - **Occasional** (sustained + wind/seismic) ≤ **~1.33 Sh**.
- **CA**: ~1.5-3 mm typical, up to 6 mm in severe service; add the **12.5% mill under-tolerance** on pipe thickness.
- **Support span** (water-filled CS, no concentrated load): indicative ~5-6 m in 2", ~7-8 m in 6", ~9 m in 12" — watch deflection and liquid accumulation beyond.
- **Drain/gravity slope**: ≥ ~1% (1:100) typical.
- **Velocities**: liquid 1-3 m/s, gas 15-30 m/s (bounded by API 14E erosion) — flag two-phase and flashing.
- **NDT**: B31.3 Normal Fluid Service ~5% random RT; **100%** in Category M, High Pressure, Severe Cyclic.
- **PMI** (Positive Material Identification): on all delivered alloys — a grade mix-up is a major defect in service.
- **B16.5 flanges**: the **pressure-temperature rating derates with temperature** — a Class 150 does not hold its nominal pressure hot (check the derating).

## How to read an isometric (the grid)

1. **Line number and class** consistent with the line list and the P&ID; spec break in the right place.
2. **Tie-ins / continuity**: upstream/downstream connections, connectors to the other isos that answer each other.
3. **Dimensions and orientation**: lengths, elevations, north arrow; nothing ambiguous for the shop.
4. **Weld count** + marks, type (BW/SW), NDT per weld.
5. **Supports**: marks, types, positions; nothing "floating".
6. **Slopes, high/low points, drains, vents** present.
7. **BOM/MTO** of the iso complete and consistent (pipe, flanges, fittings, valves, gaskets, bolting).
8. **Test pack reference** and status (IFC / AFC / AB).

## How to read a stress analysis report (the expert grid)

This is where the senior piping engineer's expertise plays out. On a CAESAR II / ROHR2 output:

1. **Load cases defined**: Sustained (SUS), Expansion (EXP), Operating (OPE), Occasional (OCC). All present? Correct combinations?
2. **Code stress ratios**: SUS ≤ Sh, EXP ≤ SA, OCC ≤ 1.33 Sh. **All < 100%?** Where is the peak?
3. **Loads on equipment nozzles**: compared with the **allowables** — API 610 table 5 (pumps), NEMA SM-23 (turbines, combined resultant), WRC 107/297 or local stress (vessels). **This is often the real governing factor, not the pipe stress.** A line "OK to code" can crush a pump.
4. **Loads on supports**: reactions, **uplift** = inactive support → revise the scheme; friction taken into account.
5. **Thermal displacements**: hot interferences (does the line hit a neighbour / the structure?), sufficient clearances at penetrations.
6. **Spring hangers**: variability < ~25%, travel within range (not on stops), cold/hot settings, **locking pins removed at start-up**.
7. **Cold spring / pre-tension**: planned on paper → really executed at erection?
8. **Expansion loop** present between anchors on a hot line?

## Decision trees

**When must a line go to stress analysis?**
```
Connected to a rotating machine (pump, compressor, turbine)?  → YES (nozzle loads)
Hot/cold beyond the threshold (T and size per internal screening)?  → YES
Critical service / high pressure / severe cyclic / Category M?  → YES
Steam, flare lines, transients (water hammer, slug)?  → YES
Otherwise  → visual check / span check, no full analysis
```

**Branch type**
```
Small branch vs run + moderate pressure      → welded outlet (sockolet/weldolet)
Reinforcement needed (B31.3 §304.3)?         → reinforced weldolet / reinforcing pad
Branch = run (equal)                         → forged tee (B16.9)
Severe cyclic / fatigue service              → forged tee, avoid direct stub-ins
```

## Sector-specific

What changes for this role depending on the project's sector lives in the **active sector profile**: `references/sectors/<profile>.md`, section "Piping engineer". Read it right after this sheet. Without a profile (generic industrial project), apply the sheet as it is.

## Red flags — the hunt

- **Stress ratio > 100%** (SUS, EXP or OCC) unresolved.
- **Nozzle loads exceeding allowables** — the line "passes the code" but crushes the machine.
- **Spring hanger on stops** (top or bottom), or **locking pins left in place** at start-up.
- **Cold spring planned but not executed** at erection.
- **No expansion loop** between two anchors on a hot line.
- **Liquid pocket without drain** (water hammer, freezing); **dead leg** in sensitive service.
- **Spec break inconsistent** with the line list / the class.
- **PMI not done** on an alloy → wrong grade in service.
- **Test pack mixing classes** (low class tested at a high class's pressure).
- **Excessive support span** → deflection, liquid accumulation.
- **Small-bore connections (SBC: vents, drains, instrument tappings)** on a vibrating line → **fatigue failure**, a great classic.
- **Unresolved clash** in the 3D model.
- **Flange under-rated at operating T** (derating ignored).

## Vocabulary and acronyms

- **P&ID / PFD / ISO / MTO** — diagram / upstream / isometric / Material Take-Off
- **Pipe rack** — main support for above-ground piping
- **CS / LTCS / SS / LAS** — Carbon Steel / Low Temp CS / Stainless / Low Alloy Steel
- **CA** — Corrosion Allowance; **NPS / DN** — nominal diameter; **Sch** — schedule (thickness)
- **WN / SO / BL / SW** — Weld Neck / Slip On / Blind / Socket Weld flanges
- **RF / RTJ / FF** — Raised Face / Ring Type Joint / Flat Face
- **Sh / Sc / SA** — hot / cold / expansion-range allowables (B31.3)
- **SUS / EXP / OCC / OPE** — stress load cases
- **WPS / PQR** — welding qualification; **PWHT** — stress relief
- **NDT** — RT, UT, MT, PT; **PMI** — Positive Material Identification
- **Hot / cold / critical line** — lines to be stress-analysed
- **Allowable nozzle load** — allowable loads on equipment nozzles
- **SBC** — Small Bore Connection (vibration weak point)
- **Hydrotest / punch list**
- **IFD / IFR / IFC / AFC / AB** — iso statuses (Design / Review / Construction / Approved / As-Built)
- **PMS** — Piping Material Specification; **EJMA** — expansion joints

## Deliverables owned

- Piping classes / PMS; plot plan (with process)
- 3D layout (E3D, SP3D, Plant 3D); General Arrangement drawings
- Isometrics (hundreds to thousands); material MTO
- Stress calculation notes; list of standard and special supports
- Test packages (hydrotest); surface/painting/insulation specs
- Punch lists and mechanical completion dossiers

## Typical tools

- **AVEVA E3D / SP3D / Plant 3D** — 3D model
- **CAESAR II / ROHR2 / AutoPIPE** — stress analysis
- **Isogen** — automatic iso extraction
- **SPI / Intools** — piping/instrument databases
- **Navisworks** — clash detection and model review

## Reflexes / obsessions

- **"Piping class?"** — first question on any line (change = material transition).
- **"Model up to date? Clash detection run?"** — a clash discovered on site = drama.
- **"Stress check done on hot lines and machines?"**
- **"Nozzle loads within allowables?"** — the most sensitive interface.
- **"Slope ensured for drain and purge?"**
- **"Maintenance and lifting access?"** — a valve at 4 m without access = back to the drawing board.
- **"Test pack consistent with the classes?"** — 1.5× design.
- **"PMI done on the delivered alloys?"**
- Iso production = progress bottleneck → freezes the model early and industrialises.

## Typical internal interfaces

- With **process**: P&IDs, line list, conditions, slope/drain philosophy.
- With **mechanical**: nozzle locations/orientations, allowable loads, accessibility.
- With **civil**: racks, foundations, supports, slab penetrations.
- With **instrumentation**: pressure/temperature tappings, ESD/SDV valves, positioning.
- With **electrical**: cable trays (classic conflicts with lines).
- With **HSE**: access, evacuation, safety distances (acid drains, H₂S lines, ATEX).

## Tone and posture

Pragmatic, attached to physical deliverables (iso, MTO, support). Knows the site, anticipates prefabrication/erection difficulties. Wants to freeze the model early. Wary of late changes that force the re-issue of hundreds of isos. Conservative on piping classes — prefers over-spec to an unrecorded site downgrade. On stress, never trusts the code ratio alone: looks first at what the line inflicts on the machines.

## Standards / references

- **ASME B31.3** — Process Piping (reference); **B31.1** — Power; **B31.4 / B31.8** — liquid / gas pipelines
- **ASME B16.5 / B16.47** — flanges; **B16.34** — valves; **B16.9 / B16.11** — fittings/outlets
- **ASME B36.10 / B36.19** — CS / SS pipe
- **NACE MR0175 / ISO 15156** — H₂S service
- **WRC 107 / 297** — nozzles on vessels (local loads)
- **EN 13480** — EN industrial piping (with PED); **ISO 4427 / EN 12201** — PE pressure pipe
- **MSS SP-58** — supports; **EJMA** — expansion joints
- **Applicable set by country**: the codes above are families and common references; the project country's regime decides the set actually enforced (structural code and annex, pressure equipment, piping, electrical, hazardous areas, process safety, contract form) — `countries/standards-regimes.md`.

## Senior level — the expert's eye

- **Buried HDPE (effluents, low-pressure gas) follows different rules from steel.** Electrofusion / butt-fusion welding, welder qualification, traceability: do not let a steel pipefitter improvise on PE.
- **Dead legs and low points are nests for corrosion and condensates.** In saturated or sour gas service, stagnation kills (materials/corrosion link, MIC): design slopes and purges, not only the routing.
- **Stress analysis of gas and steam lines is not optional**: expansion and supporting — badly supported piping fatigues and leaks.
- **The as-built of buried piping is vital for operations**: nobody digs at random afterwards (document control link) — collect the red-lines as you go.
- **Bulk materials and buried works condition the schedule**: long to procure and to install.
- **Multi-country reflex**: piping codes (ASME/EN), flange standards and welding qualifications vary — see `countries/multi-country.md` and `standards-regimes.md`.
