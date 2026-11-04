# Contributing

Thanks for helping improve this collection.

## Adding or updating a skill

1. Pick a category from [categories.json](categories.json) and create
   `skills/<category>/<skill-name>/SKILL.md`.
2. Use a lowercase, hyphenated folder name that is unique across all
   categories, and set the same value in the `name` frontmatter field.
3. Write a `description` that says what the skill does **and when to use it**.
4. Keep supporting material in `references/` or `scripts/` inside the skill
   folder. Do not commit secrets, credentials or files over 50 MB.
5. If the skill comes from somewhere else, keep the original license file and
   credit the author. Add the source to [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Moving a skill to another category

Move the folder with `git mv skills/<old>/<skill> skills/<new>/<skill>`.

## Before opening a pull request

```bash
python3 scripts/validate_skills.py
python3 scripts/build_index.py
```

Commit the regenerated `README.md` and `skills/*/README.md` files. CI fails if
the catalog is out of date.

## Commit messages

Use short, imperative subjects, for example `Add premortem skill` or
`Move hoa-decoder to legal-government`.
