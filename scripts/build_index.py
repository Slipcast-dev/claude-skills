#!/usr/bin/env python3
"""Generate the skill catalog: the index block in README.md and skills/<category>/README.md.

Usage: python3 scripts/build_index.py [--check]
  --check  exit with code 1 if generated files are out of date (used in CI).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"
MAX_DESC = 180


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = m.group(1) if m else ""
    out: dict[str, str] = {}
    for key in ("name", "description"):
        km = re.search(rf"^{key}:\s*(.*?)(?=^\S[\w-]*:|\Z)", fm, re.S | re.M)
        if km:
            val = re.sub(r"^[>|][-+]?\s*", "", km.group(1).strip())
            out[key] = " ".join(val.split()).strip("\"'")
    return out


def short(desc: str) -> str:
    desc = desc.replace("|", "\\|")
    return desc if len(desc) <= MAX_DESC else desc[: MAX_DESC - 1].rstrip() + "…"


def build() -> dict[Path, str]:
    cats = json.loads((ROOT / "categories.json").read_text(encoding="utf-8"))
    files: dict[Path, str] = {}
    summary = ["| Category | Skills | Description |", "|---|---:|---|"]
    total = 0
    for slug, meta in cats.items():
        cdir = SKILLS / slug
        skills = sorted(p for p in cdir.iterdir() if (p / "SKILL.md").is_file()) if cdir.is_dir() else []
        total += len(skills)
        summary.append(f"| [{meta['title']}](skills/{slug}/) | {len(skills)} | {meta['description']} |")
        lines = [f"# {meta['title']}", "", meta["description"], "",
                 f"**{len(skills)} skills.** Back to the [main catalog](../../README.md).", "",
                 "| Skill | Description |", "|---|---|"]
        for s in skills:
            fm = read_frontmatter(s / "SKILL.md")
            lines.append(f"| [`{s.name}`]({s.name}/SKILL.md) | {short(fm.get('description', ''))} |")
        files[cdir / "README.md"] = "\n".join(lines) + "\n"
    summary.append(f"| **Total** | **{total}** | |")
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    block = f"{START}\n" + "\n".join(summary) + f"\n{END}"
    files[readme_path] = re.sub(re.escape(START) + r".*?" + re.escape(END), block, readme, flags=re.S)
    return files


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for path, content in build().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            stale.append(path.relative_to(ROOT))
            if not check:
                path.write_text(content, encoding="utf-8")
    if check and stale:
        print("Out of date, run `python3 scripts/build_index.py`:", *stale, sep="\n  ")
        return 1
    print(f"{'Checked' if check else 'Wrote'} index ({len(stale)} file(s) {'stale' if check else 'updated'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
