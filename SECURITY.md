# Security

This repository contains **Markdown reference files and one dependency-free Python script**. There is no server, no service, no network call, no telemetry, no data collection.

## What the skill does on your machine

- `SKILL.md` and the files under `references/` are text read by the model. They execute nothing.
- `scripts/team.py` uses the Python standard library only. It reads and writes files **inside the skill folder** and, for `init`, writes one JSON file in the working directory. It makes **no network access**. You can read it end to end in a few minutes — and you should, before running it.
- `config/project.json` and any `project-team.json` you create hold project context (sector, countries, posture). Do not put confidential project data, client names or credentials in them: on a shared repository or a shared skill folder, they travel with the files.

## Reporting a problem

Open a normal issue for anything visible in the repository. For something you would rather not post publicly, use GitHub's **private vulnerability reporting** (Security tab → Report a vulnerability), or write to the contact address on j2globalpartners.com.

## What is not a security issue

Wrong figures, an outdated standard reference or a questionable sector claim are **content defects**, not vulnerabilities — open a normal issue, they are welcome. Every anchor figure in this repository is an order of magnitude and every regulatory reference must be checked against the text in force before it is relied on; see the disclaimer in the README.
