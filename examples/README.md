# Examples

- **[`sample-answers.md`](sample-answers.md)** — three real answers produced by the skill (one role on a cost report, a multi-role decision, and the same plant in another country). Start here if you want to judge the skill before installing it.
- **`sectors/`** — five sector profiles, unreviewed, described below.

## Sector profiles (unreviewed)

Five sector profiles written as **illustrations of the expected density** of `references/sectors/_template-sector.md`: solar PV, hydrogen, refining & petrochemicals, thermal power, manufacturing plant. They were produced from general industry knowledge by the author's AI assistant and have **not been validated by field practitioners**. Figures are indicative and dated; regulatory references are given by family with examples, the project country deciding the actual set (`countries/standards-regimes.md`).

They are deliberately kept out of `references/sectors/`, so the skill ships no sector. To use one: copy it into `references/sectors/<slug>.md`, run `python scripts/team.py profile <slug>` (it must report zero orphan headings), then review every line with a practitioner of the sector — and open a pull request if you correct it.

| File | Sector | Sector-specific roles (compact sheets inside) |
|---|---|---|
| `sectors/solar-pv.md` | Solar PV plants (ground, carports, agrivoltaics, rooftops) | PV / yield & performance engineer |
| `sectors/hydrogen.md` | Hydrogen by electrolysis | Electrolysis & H₂ integration engineer |
| `sectors/refining-petrochemicals.md` | Refining / petrochemical units (greenfield and brownfield) | Licensing / process package engineer; Turnaround / tie-in coordinator |
| `sectors/thermal-power.md` | Thermal power (CCGT, biomass, waste-to-energy, cogeneration) | Power island engineer |
| `sectors/manufacturing-plant.md` | Manufacturing plants (pharma, food, aerospace, automotive, batteries) | Industrialisation & qualification engineer; HVAC / cleanroom & clean utilities engineer |
