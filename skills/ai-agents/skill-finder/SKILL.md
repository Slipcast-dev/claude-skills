---
name: skill-finder
description: "Search index of ~1700 hidden installed skills. Use before any specialized task (docs, legal, finance, health, career, marketing, eng) no listed skill covers."
---

# skill-finder

Most installed skills are hidden from the listing to save tokens. They are all still installed. Find one, then use it.

1. Search the index with 2–4 keywords, synonyms included (English names, Russian queries too):
   ```bash
   grep -i -E '\b(kw1|kw2|kw3)' ~/.claude/skill-index.tsv | head -12
   ```
   Format: `name<TAB>what it does<TAB>trigger phrases`.
2. Pick the single best match. If nothing fits, continue without a skill. Don't load several.
3. Use it:
   - Try `Skill(<name>)` first.
   - If that's refused, because hidden skills can't be model-invoked: `Read ~/.claude/skills/<name>/SKILL.md` and follow it as if the skill were loaded. Read files in `references/` or `scripts/` only when the SKILL.md points to them for the current step.
4. Tell the user in one line which skill you used.
