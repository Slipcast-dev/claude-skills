# Claude Skills Collection

[![Validate skills](https://github.com/Slipcast-dev/claude-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Slipcast-dev/claude-skills/actions/workflows/validate.yml)
[![License: MIT (tooling)](https://img.shields.io/badge/license-MIT%20(tooling)-blue.svg)](LICENSE)

A categorized collection of **1,814 [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills)** for Claude Code and other tools that read `SKILL.md`, grouped into 16 categories, plus scripts to validate, index and install them.

> [!IMPORTANT]
> Many skills come from third-party authors and keep their original licenses. Read [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before you reuse or redistribute them.

## Contents

- [Catalog](#catalog)
- [Installation](#installation)
- [Repository layout](#repository-layout)
- [Skill format](#skill-format)
- [Maintenance scripts](#maintenance-scripts)
- [Contributing](#contributing)
- [License](#license)

## Catalog

Each category links to a page listing every skill with a short description.

<!-- INDEX:START -->
| Category | Skills | Description |
|---|---:|---|
| [AI & Agents](skills/ai-agents/) | 172 | Designing, evaluating and operating LLM agents, prompts, MCP servers and AI policy. |
| [Software Engineering](skills/software-engineering/) | 175 | Coding, architecture, testing, DevOps, infrastructure and developer tooling. |
| [Security, Privacy & Compliance](skills/security-compliance/) | 61 | Threat modeling, audits, incident response, SOC 2 / ISO 27001 / GDPR readiness. |
| [Data & Analytics](skills/data-analytics/) | 80 | Metrics, dashboards, experiments, forecasting, spreadsheets and data quality. |
| [Product & Design](skills/product-design/) | 68 | Product management, roadmaps, UX research, UI and visual design, accessibility. |
| [Marketing, Sales & Growth](skills/marketing-sales/) | 181 | SEO/AEO, content, ads, launches, sales outreach, pricing and customer success. |
| [Business, Strategy & Finance](skills/business-strategy/) | 188 | Strategy, fundraising, corporate finance, operations, procurement and governance. |
| [People, HR & Leadership](skills/people-leadership/) | 137 | Hiring, management, feedback, careers, teams and meetings. |
| [Writing & Communication](skills/writing-communication/) | 255 | Letters, emails, memos, decks, documentation, storytelling and editing. |
| [Education & Research](skills/education-research/) | 75 | Learning plans, teaching, academic writing and research methods. |
| [Productivity & Workflow](skills/productivity/) | 115 | Planning, task triage, focus, notes, reviews and personal systems. |
| [Thinking & Decision-Making](skills/thinking-decisions/) | 26 | Red-teaming, pre-mortems, steelmanning, brainstorming and second opinions. |
| [Legal & Government](skills/legal-government/) | 53 | Contracts, tenancy, appeals, courts, immigration and official paperwork. |
| [Personal Finance](skills/personal-finance/) | 63 | Budgets, debt, loans, insurance, taxes, retirement and big purchases. |
| [Health & Wellness](skills/health-wellness/) | 27 | Medical visits, medications, fitness, mobility and wellbeing. |
| [Home, Family & Lifestyle](skills/personal-life/) | 138 | Family, relationships, home, travel, hobbies and life events. |
| **Total** | **1814** | |
<!-- INDEX:END -->

Categories were assigned automatically from each skill's name and description, then corrected by hand where the match was obviously wrong. If a skill sits in the wrong place, open an issue or a PR that moves it.

## Installation

Claude Code loads personal skills from `~/.claude/skills/<skill-name>/SKILL.md`, a flat layout. The install script flattens the category folders for you.

```bash
git clone https://github.com/Slipcast-dev/claude-skills.git
cd claude-skills

# Install all skills (existing skills with the same name are skipped)
scripts/install.sh

# Install only some categories
scripts/install.sh software-engineering ai-agents

# Symlink instead of copying, so `git pull` updates installed skills
MODE=link scripts/install.sh

# Install into a project instead of your home folder
DEST=/path/to/project/.claude/skills scripts/install.sh productivity
```

To install one skill by hand, copy its folder:

```bash
cp -R skills/thinking-decisions/premortem-assassin ~/.claude/skills/
```

> [!NOTE]
> Every skill here has `disable-model-invocation: true` in its frontmatter. Claude will not pick it up automatically; you call it by name, for example `/premortem-assassin`. Remove that line from a skill's `SKILL.md` if you want Claude to use it on its own.

## Repository layout

```text
.
├── skills/
│   └── <category>/
│       ├── README.md          # generated list of skills in the category
│       └── <skill-name>/
│           ├── SKILL.md       # required: frontmatter + instructions
│           ├── references/    # optional supporting docs
│           └── scripts/       # optional helper scripts
├── scripts/
│   ├── build_index.py         # regenerates the catalog tables
│   ├── validate_skills.py     # checks structure and frontmatter
│   └── install.sh             # installs skills into ~/.claude/skills
├── categories.json            # category slugs, titles and descriptions
└── .github/                   # CI workflow, issue and PR templates
```

## Skill format

```markdown
---
name: my-skill
description: What the skill does and when to use it. Claude reads this to decide relevance.
disable-model-invocation: true
---

# My Skill

Instructions for Claude...
```

The folder name must be unique across all categories and should match `name`.

## Maintenance scripts

Python 3.9+ with no dependencies.

```bash
python3 scripts/validate_skills.py     # structure and frontmatter checks
python3 scripts/build_index.py         # regenerate README catalog and category pages
python3 scripts/build_index.py --check # fail if the catalog is out of date (CI)
```

CI runs both checks on every push and pull request.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). To report a security problem in a skill or script, see [SECURITY.md](SECURITY.md).

## License

- Repository tooling and documentation (everything outside `skills/`): [MIT](LICENSE).
- Skills in `skills/`: each keeps the license of its original author. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and any `LICENSE` file or `license:` field inside a skill folder.

---

<details>
<summary>На русском</summary>

Коллекция из 1814 скилов для Claude Code, разложенных по 16 категориям в папке `skills/`. Установка всех скилов: `scripts/install.sh`, установка отдельных категорий: `scripts/install.sh <категория>`. Проверка структуры: `python3 scripts/validate_skills.py`. Обновление каталога: `python3 scripts/build_index.py`. Скилы сторонних авторов сохраняют свои лицензии, подробности в [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

</details>
