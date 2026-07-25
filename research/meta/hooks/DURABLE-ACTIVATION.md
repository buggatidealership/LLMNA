# Durable Hook Activation — Claude Code on Web

**Status:** ✅ RESOLVED 2026-06-26 via Architecture A (project-level `.claude/settings.json`)
**Created:** 2026-06-19 (post H1-CONTAINER-EPHEMERALITY-FIX `7be02c0`). ⚠️ SHA note (2026-07-20, K3-Swarm G-40): the four provenance SHAs originally cited here pre-dated a history rewrite and no longer exist in the object DB; remapped to their current-history equivalents by commit message.
**Resolved:** 2026-06-26 via H1 PROJECT-LEVEL SETTINGS test confirming Claude Code on Web reads `<repo>/.claude/settings.json`
**Last verified working:** 2026-06-26 14:52:32Z (diagnostic hook fired from project-level settings)

## TL;DR (current architecture)

Hook activation lives at **`<repo-root>/.claude/settings.json`** with `"$CLAUDE_PROJECT_DIR"`-relative paths to in-repo hook scripts at `research/meta/hooks/*.py` (portable across machines and clone locations since the 2026-07-06 llmna migration). This file is **version-controlled and ships with the repo**, so every fresh container clone has hooks active from turn 1, with **zero laptop dependency, zero install.sh dependency, zero `~/.claude/` dependency**.

The previous Architecture (install.sh copies to `~/.claude/`) is **deprecated** as the activation mechanism; install.sh remains in the repo as a fallback only.

## Why this works

Claude Code merges settings from multiple sources:
- `launcher-settings.json` (system-managed, contains system hooks like git-identity + git-check)
- `~/.claude/settings.json` (user-level, ephemeral in cloud containers)
- `<repo>/.claude/settings.json` (project-level, version-controlled — THIS is what we use)

All three merge; hooks in each layer fire in sequence. The project-level layer is the **only** layer that survives container resets without external configuration, because it ships with the repo via `git clone`.

**To prevent duplicate firing of the same hook,** `~/.claude/settings.json` is intentionally kept empty (post-migration 2026-06-26) — its prior hook list has been wholly migrated to project-level. Backup of pre-migration state at `~/.claude/settings.json.bak.pre-arch-a-2026-06-26`.

## What lives where (Architecture A, 2026-06-26)

| Layer | File | Contents | Lifecycle |
|---|---|---|---|
| System | `~/.claude/launcher-settings.json` | system hooks (git-identity, git-check, reply-gate) | managed by platform; we don't touch |
| User | `~/.claude/settings.json` | INTENTIONALLY EMPTY (just `{"hooks": {}}` + Skill permissions) | ephemeral; gets wiped on container reset; that's now fine |
| Project | `<repo-root>/.claude/settings.json` | ALL 19 hook scripts (PreToolUse × 1, SessionStart × 2 + hooksPath one-liner, UserPromptSubmit × 1, Stop × 15 — recomputed 2026-07-20) | **version-controlled**; survives container resets |
| Hook scripts | `<repo-root>/research/meta/hooks/*.py` + `.sh` | the hook executables themselves | version-controlled; referenced by `$CLAUDE_PROJECT_DIR`-relative path from project settings.json (corrected 2026-07-06 — this row previously said "absolute path", contradicting the portability commit) |

## Verification protocol

After any cold session start:

```bash
ls -la $CLAUDE_PROJECT_DIR/.claude/settings.json
ls -la $CLAUDE_PROJECT_DIR/research/meta/hooks/*.py | wc -l   # expect 19 (as of 2026-07-20)
cat $CLAUDE_PROJECT_DIR/research/meta/hook-fire-log.md | tail -5  # expect recent fires
```

If hooks are firing per `hook-fire-log.md`, durability is confirmed.

## Fallback architecture (deprecated; for emergencies only)

If for any reason the project-level settings file fails to be read (e.g., Claude Code on Web change in behavior), fall back to the **install.sh approach**:

```bash
bash $CLAUDE_PROJECT_DIR/research/meta/hooks/install.sh
```

This copies all hook scripts and the LEGACY `research/meta/hooks/settings.json` (still kept as the install-target mirror) into `~/.claude/`. Subsequent sessions fall back to user-level enforcement until project-level is restored.

**Note:** if you re-activate the install.sh fallback, you MUST also re-add hooks to `~/.claude/settings.json` (currently emptied for Architecture A). The install.sh handles this automatically because it copies the legacy mirror. **⚠️ DOUBLE-FIRE HAZARD (added 2026-07-06):** do this ONLY after removing `<repo>/.claude/settings.json` — Claude Code merges settings files, so both layers active = every hook fires twice per event. install.sh now hard-aborts in that state unless `FORCE_INSTALL=1`.

## Migration history

- **2026-06-19** `7be02c0` — H1-CONTAINER-EPHEMERALITY-FIX. Identified that `~/.claude/` resets per container; built install.sh + mirror in repo. This was Architecture 0 (ephemeral, requires laptop or per-session run).
- **2026-06-19** `4d0560a` — H1-ACTIVATION-RESOLVED. install.sh ran successfully → ~/.claude/ populated. True for ~12 hours, then container reset wiped it. Confirmed the "needs durable mechanism" finding.
- **2026-06-26** `956d4a7` — Added session-prime-hook + macro-anchor-hook to mirror settings.json. Closed the wiring gap that made install.sh propagation silently drop both hooks.
- **2026-06-26** (this commit) — **Architecture A migration.** Created project-level `<repo>/.claude/settings.json` with all hooks at repo paths. Emptied `~/.claude/settings.json` to prevent merge duplication. install.sh deprecated as primary activation mechanism. **Result: zero laptop dependency for hook durability across all future sessions/containers.**

## Linked

- `$CLAUDE_PROJECT_DIR/.claude/settings.json` — the project-level activation file (Architecture A primary)
- `research/meta/hooks/settings.json` — legacy mirror (Architecture 0 fallback; install.sh still copies this if invoked)
- `research/meta/hooks/install.sh` — Architecture 0 installer (deprecated for activation; available for emergency)
- `research/meta/hooks/README.md` — hook docs
- `research/meta/tier-cascade-log.md` — `[2026-06-19 H1-CONTAINER-EPHEMERALITY-FIX]` + `[2026-06-26 H1-ARCH-A-MIGRATION]` entries
- `research/meta/subagent-cost-yield-ledger.md` — H2 instrumentation surfacing in session-start briefing
- Commit `7be02c0` — install.sh ship (Architecture 0)
- Commit `d446ecd` — H2 ledger ship
- Commit `4d0560a` — H1-ACTIVATION-RESOLVED (12h-evaporation precedent)
- Commit `956d4a7` — session-prime + macro-anchor wiring fix
- This commit — Architecture A migration
