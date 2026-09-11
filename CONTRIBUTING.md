# Contributing

Three contributions carry value; all go through a pull request and through `python scripts/team.py check` without error.

## A sector profile

`python scripts/team.py new-sector <slug> --title "…"`, then follow `references/sectors/_template-sector.md` and the § "Creating the specifics of a sector" of `SKILL.md`. Review criteria:

- the **identity card** fits in twelve lines and really calibrates (scale, contracts, gates, regulation, locks, revenue);
- an insert exists only **where the sector changes something** for the role; elsewhere, "— nothing specific —";
- the **`###` headings** are those of the `SKILL.md` catalogue (`profile <slug>`: zero orphans);
- every figure is **indicative and dated**; every regulatory threshold or tariff is **referred to its source**, not copied;
- no **proprietary** content (a company's internal standards, data from a named project, a contractual document).

Add the detection row (vocabulary → slug) to the table in `SKILL.md`.

## A country card

`python scripts/team.py new-country <CODE> --name "…"`, fill in the nine axes in `references/countries/country-cards.md`, add the row to the table in `multi-country.md`. Name the operators, authorities and regulators; date the support mechanisms, which move fast.

## A correction to a role sheet

The generic sheets contain **no sector content** (`check` verifies it): a sectoral contribution goes into a profile. A correction of method, anchor or red flag is welcome if it comes from field practice; say where it comes from in the pull request.

## Language

The content is in English; EPC acronyms (FID, FEED, EOT, LD, MC, PAC, HAZOP…) are kept as used in the industry. The English of this first edition has not been proofread by a native speaker: wording fixes are welcome, as are corrections to the standards regime map from practitioners of the countries concerned. A translation of a sheet or a profile is a possible contribution, in a `translations/<language>/` folder mirroring the same tree.
