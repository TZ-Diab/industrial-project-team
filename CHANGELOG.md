# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

## [1.0.0] — 2026-09-11

First public edition.

- 27 generic role sheets (project management & controls, engineering, safety & environment, procurement-construction-quality-operations, cross-cutting), each with reading grid, indicative anchors, decision trees, red flags and a "Senior level" section.
- Three-layer architecture: generic roles × sector profile × countries. No sector shipped; fallback profile `generic` with express mini-profile; profile template with a density example.
- "Creating the specifics of a sector" protocol (framing by questions, writing, installation, keeping the profile alive) and sector-specific roles created on demand.
- Country layer, worldwide: nine-axis method, a map of technical standards regimes by discipline across 24 regimes (EU, UK, US, Canada, Australia/NZ, Gulf, India, China, Japan, Brazil, South Africa, international oil & gas, Norway, Switzerland, Turkey, Egypt, francophone and anglophone Africa, Singapore, Malaysia, Indonesia, South Korea, Mexico, Chile) so that every role adapts its codes once the project country is defined, five example country cards (FR · BE · PL · ES · DE), substance / permanent-establishment risk, country card template.
- Per-project configuration (`project-team.json`, `CLAUDE.md` block) and profile selection cascade (conversation > project > default > detection > generic).
- `examples/sample-answers.md`: three sample answers showing the layers in use.
- Repository furniture: banner, issue and pull-request templates, `SECURITY.md`, `VERSION`.
- Five example sector profiles under `examples/sectors/` (solar PV, hydrogen, refining & petrochemicals, thermal power, manufacturing plant), explicitly unreviewed, kept out of the shipped `references/sectors/`.
- `scripts/team.py` tool: `list`, `profile`, `check`, `init`, `new-sector`, `new-role [--sector-specific]`, `new-country`; `check` also verifies that no sector content enters the generic sheets.

Origin: generalisation of a biomethane project-team skill (28 roles, sheets reviewed one by one with practitioners), whose sector content was removed for this edition. The English wording of this first edition has not been proofread by a native speaker, and the regime map entries are reference points to be confirmed locally: both are open to correction.
