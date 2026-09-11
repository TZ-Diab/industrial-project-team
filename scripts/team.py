#!/usr/bin/env python3
"""team.py — tooling for the `industrial-project-team` skill (standard library only, no network access).

Commands:
  list                                roles (from the SKILL.md catalogue), sector profiles, countries
  profile <slug>                      identity card of a profile + coverage of the role inserts
  check [--config FILE]               validate a configuration and the catalogue / profile consistency
  init --sector X [--countries FR,DE] [--regime eu] [--name "…"] [--posture owner] [--phase …] [--out project-team.json]
  new-sector <slug> [--title "…"]     create references/sectors/<slug>.md from the template, one ### per role
  new-role <slug> --title "…" (--family "…" | --sector-specific) [--when "…"]
                                      create references/roles/<slug>.md from the template and add it to the catalogue
                                      (--sector-specific = family of roles specific to a sector)
  new-country <CODE> --name "…"       add a blank country block to references/countries/country-cards.md

The role catalogue is authoritative in the tables of SKILL.md (one row = `| Title | When | `references/roles/slug.md` |`).
The inserts of a profile are the `###` of its "Role inserts" section, whose heading must equal the catalogue title
(a subtitle after " — " is free).
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
ROLES = ROOT / "references" / "roles"
SECTORS = ROOT / "references" / "sectors"
COUNTRIES = ROOT / "references" / "countries"
CONFIG = ROOT / "config" / "project.json"
SPECIFIC = "Sector-specific roles (created on demand)"
REGIMES = ("eu", "uk", "us", "ca", "au-nz", "gcc", "in", "cn", "jp", "br", "za", "intl-og", "no", "ch", "tr", "eg", "africa-fr", "africa-en", "sg", "my", "id", "kr", "mx", "cl")

ROW_RE = re.compile(r"^\|\s*(?P<title>[^|]+?)\s*\|\s*(?P<when>[^|]*?)\s*\|\s*`references/roles/(?P<slug>[a-z0-9-]+)\.md`\s*\|\s*$")


def norm(s: str) -> str:
    s = s.split(" — ")[0].split(" (")[0]
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def catalogue():
    """Roles of the SKILL.md catalogue: list of dicts {slug, title, when, family}, in file order."""
    roles, family = [], None
    for line in SKILL.read_text(encoding="utf-8").splitlines():
        if line.startswith("#### "):
            family = line[5:].strip()
        m = ROW_RE.match(line)
        if m:
            roles.append({"slug": m["slug"], "title": m["title"].strip(), "when": m["when"].strip(), "family": family})
    return roles


def generic_roles():
    """Generic roles = catalogue minus the sector-specific family."""
    return [r for r in catalogue() if not norm(r["family"] or "").startswith("sector specific")]


def profiles():
    return sorted(p.stem for p in SECTORS.glob("*.md") if not p.name.startswith("_"))


def country_codes():
    txt = (COUNTRIES / "country-cards.md").read_text(encoding="utf-8")
    return sorted(set(re.findall(r"^- \*\*([A-Z]{2})\*\*\s?:", txt, re.M)))  # vocabulary-by-country lines


def sections(md: str):
    """Split a markdown file into {h2_title: [h3_titles]}."""
    out, cur = {}, None
    for line in md.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip(); out[cur] = []
        elif line.startswith("### ") and cur is not None:
            out[cur].append(line[4:].strip())
    return out


def profile_info(slug: str):
    p = SECTORS / f"{slug}.md"
    if not p.exists():
        sys.exit(f"unknown profile: {slug} (available: {', '.join(profiles())})")
    md = p.read_text(encoding="utf-8")
    title = md.splitlines()[0].lstrip("# ").strip()
    secs = sections(md)
    inserts = next((v for k, v in secs.items() if norm(k).startswith("role inserts")), [])
    specific = next((v for k, v in secs.items() if norm(k).startswith("sector specific roles")), [])
    card = []
    m = re.search(r"^## Sector identity card[^\n]*\n(.*?)(?=^## )", md, re.M | re.S)
    if m:
        card = [l for l in m.group(1).splitlines() if l.startswith("- **")]
    return {"slug": slug, "title": title, "inserts": inserts, "specific": specific, "card": card, "md": md}


def coverage(slug: str):
    info = profile_info(slug)
    cat = generic_roles()
    by_norm = {norm(r["title"]): r for r in cat}
    covered, orphans, empty = {}, [], []
    for h in info["inserts"]:
        r = by_norm.get(norm(h)) or next((x for x in cat if x["slug"] == norm(h).replace(" ", "-")), None)
        if r:
            body = re.search(rf"^### {re.escape(h)}\n(.*?)(?=^### |^## |\Z)", info["md"], re.M | re.S)
            txt = body.group(1).strip() if body else ""
            covered[r["slug"]] = "empty" if (not txt or txt.startswith("— nothing specific")) else "ok"
            if covered[r["slug"]] == "empty":
                empty.append(r["slug"])
        else:
            orphans.append(h)
    missing = [r["slug"] for r in cat if r["slug"] not in covered]
    return info, covered, missing, orphans, empty


# ---------------------------------------------------------------- commands
def cmd_list(_):
    cat = catalogue()
    print(f"Catalogue roles ({len(cat)}):")
    fam = None
    for r in cat:
        if r["family"] != fam:
            fam = r["family"]; print(f"  [{fam}]")
        print(f"    {r['slug']:<30} {r['title']}")
    print(f"\nSector profiles ({len(profiles())}): " + ", ".join(profiles()))
    print(f"Country cards ({len(country_codes())}): " + ", ".join(country_codes()) + " — any other country: regime map")
    print("Standards regimes:", ", ".join(REGIMES))
    print("Installation default:", json.loads(CONFIG.read_text(encoding='utf-8')).get("sector"))


def cmd_profile(a):
    info, covered, missing, orphans, empty = coverage(a.slug)
    print(info["title"]); print()
    for l in info["card"]:
        print(" ", l[:160] + ("…" if len(l) > 160 else ""))
    if info["specific"]:
        print("\nSector-specific roles:", "; ".join(info["specific"]))
    ok = [s for s, st in covered.items() if st == "ok"]
    if not info["inserts"]:
        print("\nProfile without role inserts (fallback profile) — the generic sheets apply as they are."); return
    print(f"\nInserts: {len(ok)} filled, {len(empty)} empty, {len(missing)} roles without insert, {len(orphans)} orphan headings")
    if empty: print("  empty          :", ", ".join(empty))
    if missing: print("  without insert :", ", ".join(missing))
    if orphans: print("  orphans        :", ", ".join(orphans), "→ align with the catalogue title")


def load_config(path):
    p = Path(path) if path else None
    if p and p.exists():
        return json.loads(p.read_text(encoding="utf-8")), p
    for cand in (Path.cwd() / "project-team.json", CONFIG):
        if cand.exists():
            return json.loads(cand.read_text(encoding="utf-8")), cand
    sys.exit("no configuration found")


def cmd_check(a):
    cfg, src = load_config(a.config)
    print("Configuration:", src); errors = []
    cat = {r["slug"] for r in catalogue()}
    sec = cfg.get("sector", "auto")
    if sec != "auto" and sec not in profiles():
        errors.append(f"sector '{sec}' unknown (available: {', '.join(profiles())})")
    warnings = []
    for c in cfg.get("countries", []):
        if not (len(c) == 2 and c.isalpha() and c.isupper()):
            errors.append(f"country '{c}' is not an ISO-2 code")
        elif c not in country_codes():
            warnings.append(f"country '{c}' has no card in country-cards.md — the regime map (standards-regimes.md) applies; add detail with new-country {c}")
    if cfg.get("standards_regime") not in (None, "", *REGIMES):
        errors.append(f"standards_regime '{cfg.get('standards_regime')}' outside the list ({', '.join(REGIMES)})")
    for key in ("active_roles", "disabled_roles", "added_roles"):
        for s in cfg.get(key, []):
            if s not in cat:
                errors.append(f"{key}: role '{s}' missing from the SKILL.md catalogue")
            if not (ROLES / f"{s}.md").exists():
                errors.append(f"{key}: sheet references/roles/{s}.md not found")
    if cfg.get("posture") not in (None, "", "owner", "contractor", "epcm", "pmc", "hybrid"):
        errors.append(f"posture '{cfg.get('posture')}' outside the list (owner, contractor, epcm, pmc, hybrid)")
    # catalogue ↔ sheets consistency
    for s in sorted(cat):
        if not (ROLES / f"{s}.md").exists():
            errors.append(f"catalogue: missing sheet references/roles/{s}.md")
    for p in ROLES.glob("*.md"):
        if not p.name.startswith("_") and p.stem not in cat:
            errors.append(f"sheet references/roles/{p.name} missing from the SKILL.md catalogue (→ add the row)")
    # invariant: no sector content in the generic sheets
    leak = re.compile(r"biomethane|biogas|digester|digestate|\bBMP\b|FOS/TAC|\bMWp\b|electrolyser|electrolyzer|\bHRSG\b|as in France|home country|Franco-French", re.I)
    for p in sorted(ROLES.glob("*.md")):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if leak.search(line):
                errors.append(f"sector content in a generic sheet: {p.name}:{i} — move it to a profile")
    for w in warnings: print("  !", w)
    for e in errors: print("  ✗", e)
    if sec != "auto":
        info, covered, missing, orphans, empty = coverage(sec)
        print(f"Profile {sec}: {len([1 for v in covered.values() if v == 'ok'])} inserts filled; without insert: {', '.join(missing) or '—'}; orphans: {', '.join(orphans) or '—'}")
    print("OK" if not errors else f"{len(errors)} problem(s)")
    sys.exit(1 if errors else 0)


def cmd_init(a):
    cfg = json.loads(CONFIG.read_text(encoding="utf-8")); cfg.pop("_doc", None)
    if a.sector not in profiles() and a.sector != "auto":
        sys.exit(f"unknown sector: {a.sector} (available: {', '.join(profiles())})")
    if a.regime and a.regime not in REGIMES:
        sys.exit(f"unknown regime: {a.regime} (available: {', '.join(REGIMES)})")
    cfg.update({"project_name": a.name or "", "sector": a.sector, "standards_regime": a.regime or "",
                "countries": [c.strip().upper() for c in a.countries.split(",") if c.strip()],
                "posture": a.posture, "current_phase": a.phase or "", "contract_model": a.contract or ""})
    out = Path(a.out); out.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("written:", out)


def cmd_new_sector(a):
    dst = SECTORS / f"{a.slug}.md"
    if dst.exists(): sys.exit(f"already exists: {dst}")
    tpl = (SECTORS / "_template-sector.md").read_text(encoding="utf-8")
    title = a.title or a.slug.replace("-", " ").capitalize()
    tpl = tpl.replace("<Sector name> (template)", title, 1)
    # regenerate the ### list from the current catalogue (added roles included)
    heads = "\n".join(f"### {r['title']}\n— nothing specific —\n" for r in generic_roles())
    tpl = re.sub(r"(## Role inserts\n\n.*?\n\n)(### .*?)(?=\n## )", lambda m: m.group(1) + heads, tpl, flags=re.S)
    dst.write_text(tpl, encoding="utf-8")
    print("created:", dst, "— fill in the identity card, then the inserts where the sector changes something")


def cmd_new_role(a):
    if a.sector_specific: a.family = SPECIFIC
    if not a.family: sys.exit("specify --family \"…\" or --sector-specific")
    dst = ROLES / f"{a.slug}.md"
    if dst.exists(): sys.exit(f"already exists: {dst}")
    tpl = (ROLES / "_template-role.md").read_text(encoding="utf-8")
    tpl = tpl.replace("<Role title> (<local equivalent if commonly used>)", a.title, 1).replace("<Short role title>", a.title)
    dst.write_text(tpl, encoding="utf-8")
    row = f"| {a.title} | {a.when or 'To be completed'} | `references/roles/{a.slug}.md` |"
    skill = SKILL.read_text(encoding="utf-8")
    pat = re.compile(rf"(#### {re.escape(a.family)}\n\| Role \| When to call on it \| Sheet \|\n\|---\|---\|---\|\n(?:\|.*\n)*)")
    m = pat.search(skill)
    if m:
        SKILL.write_text(skill[:m.end()] + row + "\n" + skill[m.end():], encoding="utf-8")
        print("created:", dst, "\nadded to the SKILL.md catalogue under", a.family)
    else:
        print("created:", dst, f"\nfamily '{a.family}' not found in SKILL.md — add the row by hand:\n", row)
    print("then: add a ### '" + a.title + "' in the relevant profiles (sectors/*.md)")


def cmd_new_country(a):
    code = a.code.upper()
    tpl = (COUNTRIES / "_template-country.md").read_text(encoding="utf-8")
    block = tpl.split("## 🏳️ <Country>", 1)[1].split("### Row to add", 1)[0]
    block = f"\n## 🏳️ {a.name} ({code})\n" + block.replace("<Country>", a.name)
    fp = COUNTRIES / "country-cards.md"; txt = fp.read_text(encoding="utf-8")
    txt = txt.replace("\n## Vocabulary by country", block + "\n## Vocabulary by country", 1)
    txt = txt.rstrip("\n") + f"\n- **{code}**: (vocabulary to be completed).\n"
    fp.write_text(txt, encoding="utf-8")
    print(f"block {code} added to {fp} — fill in the nine axes, then add the row to the table in multi-country.md:")
    print(f"| 🏳️ {code} | gas distribution | gas transmission | elec distribution | elec transmission | permitting | regulator | language |")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("list").set_defaults(f=cmd_list)
    s = sp.add_parser("profile"); s.add_argument("slug"); s.set_defaults(f=cmd_profile)
    s = sp.add_parser("check"); s.add_argument("--config"); s.set_defaults(f=cmd_check)
    s = sp.add_parser("init"); s.add_argument("--sector", required=True); s.add_argument("--countries", default="")
    s.add_argument("--regime", help="standards regime override: " + ", ".join(REGIMES))
    s.add_argument("--name"); s.add_argument("--posture", default="owner"); s.add_argument("--phase"); s.add_argument("--contract")
    s.add_argument("--out", default="project-team.json"); s.set_defaults(f=cmd_init)
    s = sp.add_parser("new-sector"); s.add_argument("slug"); s.add_argument("--title"); s.set_defaults(f=cmd_new_sector)
    s = sp.add_parser("new-role"); s.add_argument("slug"); s.add_argument("--title", required=True)
    s.add_argument("--family"); s.add_argument("--sector-specific", action="store_true"); s.add_argument("--when"); s.set_defaults(f=cmd_new_role)
    s = sp.add_parser("new-country"); s.add_argument("code"); s.add_argument("--name", required=True); s.set_defaults(f=cmd_new_country)
    a = p.parse_args(); a.f(a)


if __name__ == "__main__":
    main()
