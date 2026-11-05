# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.1.0] - 2026-11-05

### Added

- `driver-mas` and `skill-finder` in AI & Agents; 1,816 skills in total.

### Changed

- Refresh all 1,814 existing skills from the 2026-11-05 source collection, preserving categorized paths and normalized skill directory names.
- Update invocation settings: 1,706 skills require an explicit call; 110 do not disable model invocation.
- Refresh `md-slides` and skill metadata from the supplied source.
- Regenerate the English and Russian catalogs and document external dependencies of the new skills.

### Fixed

- Align the `sample-text-processor` and `playwright-pro` skill directories with their declared names.

## [1.0.0] - 2026-11-05

### Added

- 1,814 skills organized into 16 categories under `skills/`.
- Generated catalog in `README.md` and a README for each category.
- `scripts/validate_skills.py`, `scripts/build_index.py` and `scripts/install.sh`.
- GitHub Actions workflow, issue templates and pull request template.
- English and Russian project documentation with catalogs generated from the same source.
- Repository banner and live GitHub badges for stars, releases and release asset downloads.
