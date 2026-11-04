#!/usr/bin/env python3
"""Validate the repository layout: skills/<category>/<skill>/SKILL.md.

Checks: known category, SKILL.md with YAML frontmatter, non-empty `name` and
`description`, unique skill folder names across categories, no files over 50 MB.
Exit code 1 on any error. Warnings (e.g. name != folder) do not fail the run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MAX_BYTES = 50 * 1024 * 1024


def main() -> int:
    cats = set(json.loads((ROOT / "categories.json").read_text(encoding="utf-8")))
    errors: list[str] = []
    warnings: list[str] = []
    seen: dict[str, Path] = {}
    count = 0
    for cdir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        if cdir.name not in cats:
            errors.append(f"{cdir.relative_to(ROOT)}: category not listed in categories.json")
        for sdir in sorted(p for p in cdir.iterdir() if p.is_dir()):
            count += 1
            rel = sdir.relative_to(ROOT)
            if sdir.name in seen:
                errors.append(f"{rel}: duplicate skill name (also in {seen[sdir.name]})")
            seen[sdir.name] = rel
            md = sdir / "SKILL.md"
            if not md.is_file():
                errors.append(f"{rel}: missing SKILL.md")
                continue
            m = re.match(r"^---\n(.*?)\n---", md.read_text(encoding="utf-8", errors="replace"), re.S)
            if not m:
                errors.append(f"{rel}/SKILL.md: missing YAML frontmatter")
                continue
            fm = m.group(1)
            name = re.search(r"^name:\s*[\"']?([^\"'\n]*)", fm, re.M)
            if not name or not name.group(1).strip():
                errors.append(f"{rel}/SKILL.md: missing `name`")
            elif name.group(1).strip() != sdir.name:
                warnings.append(f"{rel}: frontmatter name '{name.group(1).strip()}' differs from folder")
            if not re.search(r"^description:\s*\S", fm, re.M):
                errors.append(f"{rel}/SKILL.md: missing `description`")
    for f in ROOT.rglob("*"):
        if ".git" not in f.parts and f.is_file() and f.stat().st_size > MAX_BYTES:
            errors.append(f"{f.relative_to(ROOT)}: larger than 50 MB (GitHub limit)")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"{count} skills, {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
