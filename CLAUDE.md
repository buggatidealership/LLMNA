# LLMNA — LLM-Native Investing Research OS

This repository is the complete, living operating system of an LLM-native
investing research firm. The corpus lives under `research/`.

**Boot order (mandatory):**

1. Read `research/CLAUDE.md` — the operating system: workflows, conventions, file map.
2. Read `research/INDEX.md` — single-file retrieval entry point ("where did we cover X?").

Everything else — holdings, theses, signals, predictions, methodology,
biases, lessons — is reachable from those two files. Write into the
hierarchy (one canonical home per fact); read through the references
(INDEX, tags, cross-links).

Hooks are version-controlled at `research/meta/hooks/` and activated by
`.claude/settings.json` via `$CLAUDE_PROJECT_DIR`-relative paths — see
`research/meta/hooks/DURABLE-ACTIVATION.md`.

History note: this OS was built inside `buggatidealership/Health-Calculators`
(May–July 2026) and migrated here with full commit history on 2026-07-06.
The old repo retains a frozen copy as a safety net; this repo is the sole
live workspace going forward.
