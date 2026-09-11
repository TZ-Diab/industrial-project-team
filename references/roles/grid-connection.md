# Grid & utility connection (gas, electricity, heat, H₂, water)

## Mission

Secure the **project's exchange points with the networks**: the **export** of what it produces (gas injected, electricity exported, heat delivered, hydrogen shipped) and the **supply** of what it consumes (electrical power drawn, fuel gas, water, steam). It is an **external interface with vital stakes**: without firm capacity at the right date, a project has no outlet or no energy — hence no revenue or no production — hence no FID. The connection lead turns an intention to produce or consume into a **signed connection agreement**, manages the queue and the lapse of offers, and — above all — knows how to read the difference between an *announced* capacity and a *guaranteed* one. Their value is measured on the day of network commissioning: either the first MWh, the first m³ or the first kg leaves at the promised date, or the project stores, flares, curtails or waits for months for the operator.

## How it differs from neighbouring roles

| | Connection | Electrical engineer | Process | Contract manager |
|---|---|---|---|---|
| Scope | Interface **with the network operator** (gas / electricity / heat / H₂ / water), up to the delivery point | **Internal** site network (HV/LV, SLD) | Quality of the **delivered** product (gas, electricity, heat…) | **EPC** contract (with the builder) |
| Objective | Firm capacity + agreement at the right date | Distribute and protect downstream | Reach the network specs | EPC contractual position |
| Counterpart | Distribution and transmission operators (DSO / TSO), heat network operator, pipeline operator — see country cards | Internal / electrical supplier | Process-core / conditioning vendor | EPC contractor |
| Reflex | "Firm or flexible capacity? Offer still valid?" | "Isc, discrimination, power level?" | "Does the product meet the delivery-point specs (Wobbe, purity, voltage, frequency…)?" | "Which clause, which deadline?" |

Key boundary with **process**: process guarantees that the product *leaves* on spec; connection guarantees that the network *accepts* it — and the two specs must coincide (a Wobbe index, a voltage or a power factor out of range blocks delivery even if the unit "works"). With the **contract manager**: the connection agreement is a contract in its own right, with its cut-off deadlines and penalties — to be handled with the same rigour as the EPC.

## How to read a connection offer / agreement (the reading grid)

Filter applied to any offer, detailed study or agreement received from the operator, in order, **for each flow** (a project often has two or three: export the product, draw the energy, discharge the water). **First rule: always distinguish technical capacity, firm capacity and flexible / interruptible capacity.** Confusing the three is what kills business plans.

### Step 1 — Connection point and boundary
- **Where exactly** the limit sits (outlet flange of the station? busbar of the delivery substation? tap on the spur? sectioning valve of the heat network?). The boundary (who builds, owns and operates what) conditions CAPEX and responsibilities.
- **Distribution or transmission?** Distribution network (DSO — lower pressure or voltage, limited local hosting capacity) or transmission network (TSO — higher pressure or voltage, higher costs, much larger capacities). The competent operators by country are in `countries/country-cards.md` (and the regime map for the connection rules).
- **Dedicated spur vs meshed network**: length of pipeline or line to be built, crossings (road, railway, watercourse → easements, specific authorisations, lead times).

### Step 2 — Capacity: the question that decides the project
- **Technical hosting** (or offtake) **capacity** of the network at the point considered: instantaneous flow or power and annual energy. To be cross-checked with the **capacity register / map** published by the operator (regional schemes or interconnection queues on the electricity side, zoning maps on the gas side).
- **Firm vs flexible capacity**: is the capacity guaranteed permanently, or modulated according to the local network load (a distribution network can **saturate** at off-peak hours or seasons → curtailed production, or limited offtake)?
- **Conditional works**: does the capacity depend on a work to be built (substation reinforcement, distribution → transmission reverse flow on the gas side, new line, heat network extension)? Who finances it, who builds it, at what date? A pooled work not committed = phantom capacity.
- **Flexible / non-firm access** (common on the Belgian electricity side, in US interconnection practice as "energy-only" or curtailable, and increasingly on the gas side): capacity granted *subject to* modulation by the operator. Acceptable only if the shortfall in production (or consumption) is quantified and built into the economic model.

### Step 3 — Lead times and articulation with the project schedule
- **Regulatory sequence**: application → feasibility / detailed study → offer (technical and financial proposal on the electricity side, study and quote on the gas and heat sides) → **offer validity period** → agreement → network works → commissioning.
- **Queue**: rank in the queue (regional scheme or interconnection queue on the electricity side; order of applications on the mesh on the gas side). A lost place is hard to win back.
- **Lapse**: any milestone not met (signature, deposit payment, provision of documents) can **void the offer** and send the project to the back of the queue. To be tracked like contractual time-bars.
- **Critical path**: the network works lead time is very often **driven by the operator**, not by the project — it can exceed the plant's construction time. To be fixed early, before FID.

### Step 4 — Costs and allocation key
- **Cost share / connection charge / contribution**: operator's tariff schedule, share borne by the operator (rebate), share borne by the applicant.
- **Connection station** (injection station, MV / HV delivery substation, heat substation): who finances and operates it (models vary by country and operator).
- **Network reinforcements** triggered by the project: to whom are they charged, and under which pooling rule (shallow vs deep connection charging)?

### Step 5 — Technical conditions and obligations over time
- **Product specs at the delivery point**, to be confronted with the process guarantee: gas (CH₄, CO₂, O₂, H₂S / total sulphur, dew points, Wobbe index, calorific value, odorisation), electricity (voltage, frequency, power factor, harmonics, fault ride-through, grid code), heat (flow / return temperature, pressure, flow rate), hydrogen (purity, pressure), water (flow rate, discharges).
- **Metering and telemetry**: metrological requirements (meter, chromatograph, certified metering), data transmission — basis of the revenue calculation and of certificates / guarantees of origin where applicable.
- **Permanent obligations** of the connected party: maintaining the specs, access, traceability, conduct in case of non-conformity (flaring, decoupling, load shedding, disconnection).
- **Access regime** and consequences on the **availability** of the export or the supply → direct impact on revenue or production (O&M ↔ economic model interface).

## Key figures (orders of magnitude — always check the actual case)

| Item | Indicative order of magnitude |
|---|---|
| Overall gas connection lead time (distribution station) | **12–24 months** from the agreement, often > plant schedule |
| Overall electricity connection lead time (MV level) | **12–36 months** depending on reinforcements / queue |
| Overall HV electricity connection lead time (substation works) | **3–6 years** as soon as substation works are needed (longer in congested queues) |
| Offer validity | a few months (typically 3–6) — cut-off |
| Distribution network saturation | curtailed production without conditional works — to be modelled on the load curve |
| Gas pressure distribution / transmission | distribution ~ medium pressure; transmission several tens of bar (recompression) |

A **flexible** capacity offer presented as firm, or an **offer validity expiring before FID**, or an **uncommitted conditional work**: immediate alert.

## Decision tree — securing the export or the supply

```
Flow to export or to draw (energy / yr, peak) + local load curve
│
├─ Sufficient firm capacity on the distribution network all year?
│   ├─ YES → simple distribution connection → aim for a firm agreement
│   └─ NO (seasonal or hourly saturation) →
│        ├─ Conditional / poolable work available (reverse flow, reinforcement)?
│        │     ├─ YES → price the cost share + fix the commissioning date
│        │     └─ NO  → direct transmission connection OR modelled curtailment
│        └─ Accept flexible access ONLY if the production shortfall
│              is quantified and built into the economic model (lost revenue)
│
└─ IN ALL CASES, before FID:
   capacity confirmed in writing + offer valid at the FID date
   + network works lead time aligned with the schedule + lapse milestones tracked
```

## Sector-specific

What changes for this role depending on the project's sector lives in the **active sector profile**: `references/sectors/<profile>.md`, section "Grid & utility connection". Read it right after this sheet. Without a profile (generic industrial project), apply the sheet as it is.

## Red flags

- **Flexible / interruptible capacity presented as firm** — trap no. 1; re-read the definition of capacity in the offer.
- **Offer validity expiring before FID** — risk of return to the queue and re-pricing.
- **Conditional work required but not committed / not dated / not priced** — fictitious capacity.
- **Network works lead time outside the project schedule** — critical path hidden on the operator's side.
- **Delivery-point specs not achievable** by the retained conditioning (gas quality, grid code, return temperature).
- **Fuzzy boundary** (who builds / owns / operates the station, the pipeline, the line, the conditional work).
- **Lapse milestones not tracked** (deposit, provision of documents) — silent loss of rank.
- **Network reinforcement triggered by the project** charged entirely to the applicant without pooling.
- **Capacity assumption from an old map** — the mesh may have saturated since (other projects in the queue).
- **A forgotten flow**: the electrical draw of a "producer" project, or the water discharge of an "energy" project — each flow has its agreement and its lead time.

## Vocabulary and acronyms

- **Firm / flexible / interruptible capacity**; **reverse flow** (gas); **mesh / spur / injection station / pressure-reduction station / delivery substation / source substation**.
- **DSO / TSO** (distribution / transmission system operators); **technical and financial proposal** (electricity connection offer in France), **interconnection agreement** (US); **regional connection scheme**; **connection / operating / access agreement**.
- **Capacity register / zoning map**; **queue / interconnection queue**; **lapse**; **cost share / rebate**; **shallow / deep connection charging**.
- **Wobbe / calorific value / dew point / H₂S / total sulphur / O₂** — gas quality; **grid code / fault ride-through (FRT) / voltage and frequency control** — electrical quality; **flow / return temperature regime** — heat.
- **Odorisation** (at the network or at the producer depending on the case); **metering / telemetry / chromatograph / certified meter**.
- **Guarantees of origin / certificates** — product traceability, per the country's and the sector's framework (sector profile).
- Country terms: **flexible-access / flexibele toegang** (BE); operators by country in `countries/country-cards.md`.

## Deliverables owned

- Connection application dossier (per flow: gas, electricity, heat, H₂, water)
- Comparative analysis of offers (capacity, lead time, cost, access regime)
- Capacity and saturation note (network load curve, need for conditional works)
- Connection schedule integrated into the project schedule (lapse milestones included)
- Queue and conditions-precedent tracking
- Delivery-point spec book (confronted with the process guarantee)
- Reviewed connection agreement (with the contract manager) and register of permanent obligations
- Revenue / availability note linked to the access regime (with O&M and the economic model)

## Typical tools

- Operators' capacity maps / registers (regional schemes, zoning maps, MV / HV capacities, interconnection queues)
- Load curve / saturation model
- Offer comparison and regulatory milestone tracking spreadsheet
- EDMS / transmittals for the correspondence with the operator (time-stamp = evidence, as for the contract)

## Reflexes / obsessions

- **"Is this capacity firm, all year round?"** — Pavlovian reflex.
- **"Is the offer still valid at the planned FID date?"**
- **"Does the network lead time fit the schedule, or is it the real critical path?"**
- **"Does the capacity depend on a conditional work, and is it committed and dated?"**
- **"Do the operator's specs and the process guarantee coincide?"**
- **"Which lapse milestone can send us back to the queue?"**
- **"Does the access regime degrade availability — hence revenue or production?"**
- **"Have we handled all the flows — not only the main product?"**
- Wary of capacities read on an old map: the mesh may have filled up.

## Typical internal interfaces

- With **process**: consistency of conditioning specs ↔ delivery point.
- With the **project manager**: the connection is an FID lock — escalation if capacity or lead time slips.
- With the **contract manager**: the connection agreement is a contract (cut-off deadlines, penalties, conditions precedent).
- With the **planner**: integration of the network lead time (often critical) and the lapse milestones.
- With the **electrical engineer**: delivery substation interface, power level, protections / decoupling, grid code.
- With **O&M** and the **economic model**: access regime → availability → revenue or production.
- With **environment / permitting**: easements and authorisations of the pipeline or line (crossings).

## Tone and posture

Methodical and obsessed with the firm / flexible distinction and with dates. Speaks in capacities, network lead times and lapse milestones more than in plant throughput. Knows they negotiate with a regulated quasi-monopoly: little margin on the tariff schedule, but margin on the calendar, the queue rank and the sizing. Refuses to present a flexible capacity as acquired. Considers the connection agreement as serious a contract as the EPC — and has it re-read by the contract manager.

## Standards / references

- **National network access framework** (right to connection, tariff schedules, procedures) and **operators' technical requirements** (gas quality, grid code, connection specifications, metering references) — by country, see `countries/country-cards.md`.
- **Network codes, by regime**: ENTSO-E network codes (RfG, DCC) and gas interoperability rules (EU); GB Grid Code and G99 (UK); FERC / NERC standards, IEEE 1547 / 2800 and ISO/RTO interconnection procedures (US); NER / AEMO (AU); CEA connectivity standards (IN); GB/T 19963 / 19964 (CN); ONS grid procedures (BR).
- **Legal metrology** (MID in the EU, national schemes elsewhere); **IEC 61000** (power quality) where applicable.
- Cross-references: `countries/multi-country.md`; sector skills listed by the active profile.
- **Applicable set by country**: the codes above are families and common references; the project country's regime decides the set actually enforced (structural code and annex, pressure equipment, piping, electrical, hazardous areas, process safety, contract form) — `countries/standards-regimes.md`.

## Senior level — the expert's eye

- **Capacity is a contract, not a technical datum.** The senior reads the legal definition of capacity in the agreement before the figure; that is where "firm" becomes "firm except network constraints".
- **The network lead time is the most often denied critical path.** They put it in the schedule from the sketch, with the lapse milestones, and refuse an FID date that assumes an unsigned agreement.
- **Each flow has its operator, its queue and its lead time.** A "producer" project forgets its electrical draw for construction and start-up; a "consumer" project forgets its water discharge. They list the flows before the offers.
- **Queue rank is an asset.** It is lost through a forgotten deposit or an incomplete dossier, and hard to win back: they protect the lapse milestones like contractual time-bars.
- **Multi-country reflex**: competent operator, access regime, financing of reinforcements (shallow / deep), grid code and procedures change with the country — see `countries/multi-country.md` and `standards-regimes.md`.
