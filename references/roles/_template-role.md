# <Role title> (<local equivalent if commonly used>)

> Role sheet template. Copy as `roles/<slug>.md`, fill in every section, then add the role's row to the table in `SKILL.md` (or `python scripts/team.py new-role <slug> --title "…" --family …`, which does both). A sheet is only good if a 20-year practitioner recognises it: prefer three true anchors to ten generalities. Figures are orders of magnitude, never design values.

## Mission

In three sentences: what the role **delivers**, what it is **accountable for**, and what it **does not do** (the boundary that keeps it from encroaching on a neighbour).

## How it differs from neighbouring roles

| | <This role> | <Neighbour 1> | <Neighbour 2> | <Neighbour 3> |
|---|---|---|---|---|
| Role | **verb** | verb | verb | verb |
| Question | "…?" | "…?" | "…?" | "…?" |
| Horizon / deliverable | … | … | … | … |

Key boundary: one sentence on the split most often confused.

## Key responsibilities

- 5 to 8 bullets, action verbs, with the associated deliverable or decision.

## How to read <the trade's central document> (the reading grid)

The grid, **in the order the practitioner runs through it** — this is what the skill applies when handed a document:

1. **First thing to look at** — and why.
2. …
3. …

## Anchor figures

Thresholds, margins, ratios, lead times a senior keeps in mind. Every value flagged as **indicative** ("~", "typically", "order of magnitude"). State the context (unit, scale, country), otherwise the anchor misleads.

## Decision trees

```
Binary question?   yes → consequence / action
                   no  → other branch
Never: "…" (the trade's false good idea)
```

## Sector-specific

What changes for this role depending on the project's sector lives in the **active sector profile**: `references/sectors/<profile>.md`, section "<Short role title>". Read it right after this sheet. Without a profile (generic industrial project), apply the sheet as it is.

## Red flags — the hunt

- 8 to 12 signals to hunt for, **in decreasing order of severity**, each with its mechanism ("→ because…").

## Vocabulary and acronyms

- **ACRONYM** — short definition; 10 to 20 entries.

## Deliverables owned

- List of the documents / decisions the role owns.

## Typical tools

- Software, methods, working references.

## Reflexes / obsessions

- **"The question asked first?"** — 6 to 8 reflex questions in quotation marks, as heard in a meeting.

## Typical internal interfaces

- With **role X**: on what, and the usual friction point.

## Tone and posture

One paragraph: how the role speaks, what irritates it, what it demands, how it reacts under pressure.

## Standards / references

- Codes, standards, guides, **by family** (structural, pressure equipment, piping, electrical, hazardous areas, functional safety, process safety…), with the common international references; the country's regime decides the set actually enforced — end with the pointer to `countries/standards-regimes.md`.

## Senior level — the expert's eye

- 6 to 8 bullets of tacit knowledge: **what the junior misses**, the "tells" read by instinct, second-order effects, the unwritten rule. Each bullet starts with a bold sentence, followed by the "because".
- **Multi-country reflex**: what changes for this role once the project country is defined (regime, authority, counterparts) — see `countries/multi-country.md` and `standards-regimes.md`.
