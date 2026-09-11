# Sample answers

What the skill produces, so you can judge it before installing it. Three answers, lightly trimmed, from a generic industrial project with no sector profile loaded. The layers the skill is built on — the reading grid in its own order, the anchor figures flagged as indicative, the decision tree, the red flags last — are visible in each one.

---

## 1. One role, one document

**Prompt** — *As the cost controller, here is the monthly report: 42% physical progress, actual cost 38% of budget, EAC = BAC on every account, contingency 61% consumed, three change orders pending at 1.8 M€. Tell me what you see.*

> Sector profile: generic · Country: not stated · Posture: assumed owner
>
> **Cost controller** — Two things in this report contradict each other, and a third is missing.
>
> *Reading grid applied*
> 1. **Life cycle of the euro** — you give me actual cost, not commitments. 38% spent at 42% progress looks healthy only if commitments are near 100% on the packages already ordered and accruals are booked. An account that is silent while the work advances is an underestimated EAC, not a saving.
> 2. **EVM** — CPI ≈ 1.10 on the face of it. I do not believe it at 42% progress with contingency at 61%: one of the two measures is wrong, most often the physical progress (declarative, over-declared early).
> 3. **EAC** — "EAC = BAC on every account" after 40% progress is not a forecast, it is a forecast not done. Three methods give three different answers; I want the range, and a bottom-up EAC on the three heaviest packages.
> 4. **Contingency** — 61% consumed at 42% progress is the alarm of this report. The draw-down is running ahead of progress, so on the current slope the provision is exhausted around 70% progress, with the punch-list and commissioning phases still ahead.
> 5. **Change orders** — 1.8 M€ pending appears nowhere in the EAC. Published without an "open CO exposure" line, this report is wrong.
>
> *Anchors mobilised* (orders of magnitude) — CPI below 0.95 is an alert; the decisive test is % contingency consumed vs % progress, not the absolute; a healthy trend register carries the deviation before it becomes an actual.
>
> *Red flags, by severity*
> - Contingency consumed 1.45× faster than progress, with no draw-down record against materialised risks.
> - EAC copied from the budget: the landing is unknown, not stable.
> - 1.8 M€ of open change orders not provisioned in the forecast.
> - CPI flattered by physical progress I cannot verify: which measurement rule — 0/100, weighted milestones, units installed?
>
> *What I need before the next report* — commitment position by cost account, closing accruals, the three EAC methods with a range, and the trend register updated with the three COs and their probable disposition.

---

## 2. Several roles, one decision

**Prompt** — *The vendor announces a 10-week delay on the main compressor. Client meeting Thursday. What do I say?*

> **Planner** — First question: is it on the critical path? If the compressor drives erection and then commissioning, ten weeks on the supplier lands as ten weeks on the start-up date, minus what re-sequencing absorbs. I look in this order: re-sequence the surrounding work fronts (free), fast-track the sub-assemblies that do not depend on the machine (adds risk), crash the downstream erection (costs money). I need the float on the near-critical paths before promising anything: a recovered path often hands the criticality to the next one.
>
> **Contract manager** — Before the recovery discussion, the notification. If the delay is a vendor fault, the back-charge and the supplier LDs must be preserved now, in writing, whatever we decide afterwards. If it has any client-side cause — a late instruction, a pending approval, an access constraint — then it is an EOT claim on our side and the clock is already running: the notice periods in most forms are counted in days, not in weeks, and they are usually a condition precedent. Cheap protective notice today, particulars later.
>
> **Cost controller** — Three costs, not one: the prolongation of site costs over the delay, the cost of any recovery we choose (crashing is paid in overtime and productivity loss), and the LD exposure on our own contract if the date slips through. I want them priced separately before Thursday, because they are recovered from three different places.
>
> **Procurement** — I check the vendor's story before relaying it: factory order book, whether the slip is on a sub-supplier, and what a partial shipment or a resequenced manufacturing order would give. And I check the advance payment bond is still valid over the new date.
>
> **Project manager (synthesis)** — Thursday, I state the fact, the notified position and the option, not a reassurance. Something like: the machine slips ten weeks, we have notified reserving our rights, two recovery scenarios are priced (re-sequencing alone holds five weeks at no cost, crashing the downstream erection holds the rest at a cost we quantify), and I ask for a decision on the scenario, not for absolution. What I do not do is announce a date I cannot hold — the second announcement is the one that kills credibility.

---

## 3. The country changes the answer

**Prompt** — *Same plant, this time in Texas. What changes for the piping engineer and for the permitting lead?*

> Country: US · Standards regime: `us`
>
> **Piping engineer** — The design code does not change much in name — ASME B31.3 is the reference here as it often is elsewhere — but three things around it do. Pressure equipment is built and inspected under the **ASME BPVC** with stamps and an Authorised Inspector, not under PED with a notified body: that changes the vendor panel, the documentation and the witnessing plan. Material certification runs on **ASTM MTRs**, not EN 10204 3.1 / 3.2 — the equivalence is real but the wording of the requisition must follow the local form or the vendor supplies something else. Welder and procedure qualification is **ASME IX / AWS D1.1**, and personnel NDT certification follows ASNT rather than ISO 9712. Last, the units: specifications, datasheets and vendor drawings will come in psi, °F and inches — every interface document says which system governs.
>
> **Environment & permitting lead** — Here the change is structural, not a matter of names. There is no single integrated permit: expect a **Title V** air permit and, above thresholds, **NSR / PSD** permitting, a **Clean Water Act** discharge permit, and state and county approvals on top, each with its own authority and its own clock. Federal environmental review (**NEPA**) applies only where there is a federal nexus — a federal permit, land or funding — so the first question is whether the project has one. On the process-safety side, the major-hazard regime is **OSHA PSM** with **EPA RMP** above the threshold quantities, not a Seveso-style safety report: the deliverables and the inspecting body differ, even though the underlying hazard study work is largely the same. Construction safety runs under **OSHA 29 CFR 1926**, with no health-and-safety coordinator role of the European kind — the duties sit with the employers on site.
>
> *Multi-country retune* — the axes that actually moved here: permitting regime and authority, process-safety regime, pressure-equipment conformity route, material and welding certification, construction safety, units. Grid connection, applicable law and tax were not asked but move too: an interconnection queue with an ISO/RTO behaves nothing like a European connection offer.

---

These answers were produced with the skill loaded and no other context. Reproduce them, or better, break them: open an issue if a practitioner in your sector or your country would answer differently. That is the contribution the repository is most interested in.
