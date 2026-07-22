# Computed Counts — regenerated from the territory

**DO NOT hand-edit.** Regenerate: `python3 research/meta/computed-counts.py --write`.
Drift-check (CI/pre-commit): `--check` (exit 2 if this file is stale).
Born 2026-07-22 (commission item 5, K3 theme 5). This file is the CANONICAL
source for tail counts; prose headers should cite it, not restate numbers.

| Artifact | Count | Territory source + method |
|---|---|---|
| Hooks (script) | 21 | .claude/settings.json entries referencing a .py/.sh |
| Hooks (all entries) | 22 | all command entries (PreToolUse 1, SessionStart 4, Stop 16, UserPromptSubmit 1) |
| Lessons (max L#) | 40 | lessons.md `## L#` + `[date] ...L#` |
| Biases (max B#) | 65 | biases-watchlist.md `### B# —` |
| Principles (max #) | 47 | methodology.md `## Principle #` |
| Critical Rules (max #) | 19 | CLAUDE.md `## Critical Rules` section |
| Patterns (max P/PC-#) | 22 | cross-domain-pattern-register.md |
| Triangulation (max TC-#) | 19 | triangulation.md |

Note: 'max #' is the highest index defined; some ranges have intentionally
skipped/retired numbers (e.g. tombstoned lessons, absent biases) so the
count of PRESENT entries can be lower than the max. Max is the tail the
prose headers cite.
