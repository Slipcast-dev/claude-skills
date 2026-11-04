#!/usr/bin/env bash
# Install skills from this repo into Claude Code's personal skills folder.
# Claude Code expects a flat layout (~/.claude/skills/<skill>/SKILL.md), so the
# category folders are flattened on install.
#
# Usage:
#   scripts/install.sh                      # all skills
#   scripts/install.sh software-engineering # one or more categories
#   DEST=/path/to/skills scripts/install.sh # custom destination
#   MODE=link scripts/install.sh            # symlink instead of copy
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${DEST:-$HOME/.claude/skills}"
MODE="${MODE:-copy}"
mkdir -p "$DEST"

if [ "$#" -gt 0 ]; then
  cats=("$@")
else
  cats=()
  for d in "$ROOT"/skills/*/; do cats+=("$(basename "$d")"); done
fi

n=0
for cat in "${cats[@]}"; do
  dir="$ROOT/skills/$cat"
  [ -d "$dir" ] || { echo "Unknown category: $cat" >&2; exit 1; }
  for skill in "$dir"/*/; do
    [ -f "$skill/SKILL.md" ] || continue
    name="$(basename "$skill")"
    target="$DEST/$name"
    if [ -e "$target" ] || [ -L "$target" ]; then
      echo "skip (exists): $name"
      continue
    fi
    if [ "$MODE" = "link" ]; then ln -s "${skill%/}" "$target"; else cp -R "${skill%/}" "$target"; fi
    n=$((n + 1))
  done
done
echo "Installed $n skill(s) into $DEST"
