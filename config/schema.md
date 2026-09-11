# Configuration schema — `project.json` / `project-team.json`

One format, three possible locations, from highest to lowest priority:

1. **The conversation** — "we are on an H₂ project in Germany, contractor posture" always wins.
2. **`project-team.json` at the root of the project folder** (Claude Code / Cowork), or a `project-team:` block in the project's `CLAUDE.md`. This is the recommended pin: once per project, never repeated again. `python scripts/team.py init …` writes it.
3. **`config/project.json` in the skill folder** — the installation default (editable in Claude Code / Cowork; read-only on claude.ai, where only 1 and auto-detection apply).
4. **Auto-detection** from the project's vocabulary (see the table in `SKILL.md`), then **`generic`** with a calibration question.

| Field | Type | Values | Role |
|---|---|---|---|
| `project_name` | text | free | Name used in answers and deliverables. |
| `sector` | text | `auto`, `generic` (the only profile shipped), or the slug of a profile created in `references/sectors/` (`new-sector`) | The sector profile read after the role sheet. `auto` = infer from context; if the detected profile does not exist, the skill offers to create it. |
| `countries` | list | ISO-2 codes — any country in the world | Triggers the country layer: `standards-regimes.md` (applicable codes) and the country card if one exists (FR, BE, PL, ES, DE shipped as examples; others via `new-country`). Several countries = cross-border project (substance risk). |
| `standards_regime` | text | `eu`, `uk`, `us`, `ca`, `au-nz`, `gcc`, `in`, `cn`, `jp`, `br`, `za`, `intl-og`, `no`, `ch`, `tr`, `eg`, `africa-fr`, `africa-en`, `sg`, `my`, `id`, `kr`, `mx`, `cl`, or empty | Optional override of the regime inferred from the country — e.g. `intl-og` for a Gulf project run on ASME / API owner standards, or `us` for a US-owned plant abroad. Empty = inferred from `countries`. |
| `working_language` | text | `en`, `fr`, `de`, `pl`, `es`… | Default language of answers and deliverables. |
| `posture` | text | `owner`, `contractor`, `epcm`, `pmc`, `hybrid` | Who "we" are: changes the contractual reading (who notifies, who takes over, who carries the P&L). |
| `contract_model` | text | free (`lump-sum EPC`, `multi-package`, `EPCM`, `supply + erection`, `licence + EPC`…) | Dominant contractual frame; informs the identity card if it differs from the profile. |
| `current_phase` | text | a phase of the profile's gate model, or free | Calibrates the roles to mobilise first and the expected deliverables. |
| `active_roles` | list | slugs from `references/roles/` | Empty = all generic roles + those of the profile. Filled = restricted team (useful for a meeting simulation or a small project). |
| `disabled_roles` | list | slugs | Roles without object on this project (e.g. `piping-engineer` on a PV plant). |
| `added_roles` | list | slugs of sheets added to `references/roles/` | Roles specific to the project or the organisation (e.g. `hvac-engineer`, `turnaround-coordinator`). Created with `team.py new-role`. |
| `locks` | list | short texts | Replaces the profile's FID locks when filled (e.g. `["land", "HV grid connection", "offtake"]`) — reusable by a portfolio dashboard. |
| `phase_skills` | list | skill names | Skills of the user's ecosystem to favour for substantive detail on this project. |
| `notes` | text | free | Anything that calibrates an answer and fits nowhere else (client, Owner standards, governing contract language, political sensitivities). |

Example of a project pin (the `hydrogen` profile was created beforehand with `new-sector`):

```json
{
  "project_name": "20 MW electrolyser Hamburg",
  "sector": "hydrogen",
  "countries": ["DE", "FR"],
  "working_language": "en",
  "posture": "owner",
  "contract_model": "electrolyser OEM + BoP EPC",
  "current_phase": "FEED",
  "standards_regime": "eu",
  "disabled_roles": ["geotechnical-engineer"],
  "locks": ["RFNBO-compliant PPA", "take-or-pay offtake", "HV grid connection", "BImSchG permit"],
  "notes": "German SPV run from Paris: substance to be documented. Contract language: German."
}
```

Equivalent block in a project `CLAUDE.md`:

```yaml
project-team:
  sector: hydrogen
  countries: [DE, FR]
  posture: owner
  current_phase: FEED
  locks: [RFNBO-compliant PPA, take-or-pay offtake, HV grid connection, BImSchG permit]
```
