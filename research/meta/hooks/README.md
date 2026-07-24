# Hooks — enforcement layer for the AI Sector Research OS

**Purpose:** Hooks ENFORCE behavior. Instructions in CLAUDE.md are choices the model can skip; hooks are deterministic shell-level code that runs regardless of model choice. Anything that matters operationally should be enforced via a hook, not just documented in a rule file.

*(Rewritten 2026-07-06 harness audit — the prior README described the pre-Architecture-A world: `~/.claude/` as production location, install.sh as the activation path, and only 4 of the wired hooks. All of that was stale; see git history for the old text.)*

## Where they live (Architecture A, since 2026-06-26)

- **Source of truth + execution location:** `research/meta/hooks/*.py` — the scripts in THIS directory are what actually runs.
- **Activation:** `<repo-root>/.claude/settings.json` (project-level, version-controlled) wires them with `$CLAUDE_PROJECT_DIR`-relative paths. Ships with `git clone`, so every fresh container has hooks live from turn 1 — no install step, no `~/.claude/` dependency.
- **Dynamic root:** every script resolves the repo root as `os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[3]` — survived the 2026-07-06 Health-Calculators → LLMNA migration with zero path breakage.
- `~/.claude/` is **intentionally unused** by the OS (the environment launcher keeps its own system-managed hooks there, e.g. `stop-hook-git-check.sh` — see below).
- Full rationale + verification protocol: `DURABLE-ACTIVATION.md`.

**Legacy artifacts in this directory (do not follow blindly):**
- `settings.json` (the mirror here, NOT the project one) — legacy `~/.claude/`-path wiring kept for the documented fallback only.
- `install.sh` — **DEPRECATED**; copies hooks + mirror settings into `~/.claude/`, which under Architecture A would DOUBLE-FIRE every hook. It now hard-aborts if project settings exist (override: `FORCE_INSTALL=1`).

## Wired hooks (17 in `<repo>/.claude/settings.json` as of 2026-07-06)

| Event | Hook | Enforces |
|---|---|---|
| SessionStart | `session-start-hook.py` | To-do briefing, P0s, pending grades, stale reviews, recurring DUE/OVERDUE markers, W11 container-swap sentinel check. Always exits 0 (informational). |
| SessionStart | `session-prime-hook.py` | Cold-start injection of `meta/session-prime.md` (skips resume/clear/compact; missing `source` = cold start per 2026-07-06 fix). |
| UserPromptSubmit | `llm-native-priming-hook.py` | Pre-generation LLM-native discipline checklist (priming bracket). |
| Stop | `anti-fabrication-hook.py` | Critical Rule #7 — no uncited/ungrounded numbers (B11). |
| Stop | `cascade-enforcement-hook.py` | Critical Rule #10 — synthesis artifacts cascade to per-ticker theses (B16). |
| Stop | `segment-trajectory-hook.py` | Principle #22 — trajectory, not snapshot (B20). |
| Stop | `nth-order-cascade-hook.py` | Principle #2 — N-th order markers on causal claims (B21). |
| Stop | `bypass-route-hook.py` | Principle #9 / Rule #9 — bypass-route on binding constraints (B22). |
| Stop | `bottoms-up-hook.py` | Principle #1 — bottoms-up before outside view (B23/L1). |
| Stop | `antifragility-mn-hook.py` | Conviction format — M/N marker on full thesis blocks (B24). |
| Stop | `analyst-pt-context-hook.py` | B28/B37 — analyst-PT framing needs structural context. |
| Stop | `signal-ingest-cascade-hook.py` | Rule #10 at INGEST tier — brief/analyst-note shares must produce a cross-source-log file (B39). |
| Stop | `reasoning-tagging-hook.py` | Source-tier labels on probability claims. |
| Stop | `llm-native-reasoning-hook.py` | LLM-native reasoning-structure discipline. |
| Stop | `structural-output-hook.py` | Multi-dimensional structure on large analytical outputs (pruning bracket). |
| Stop | `macro-anchor-hook.py` | Rule #15 — macro-first, research-anchored discipline (B46). |
| Stop | `borrowed-vs-firstprinciples-hook.py` | Consensus-as-anchor framing needs an integrity-gate marker (B38). **Wired 2026-07-06** — created 2026-05-28 but never activated until the harness audit found the gap; 30-day falsifier logged in `biases-watchlist.md`. |

**Plus environment-level (system-managed, NOT in project settings):** `~/.claude/stop-hook-git-check.sh` — requires commit+push before Stop completes, plus commit-signature/committer-email verification. The copy of it in this directory is a dated SNAPSHOT for visibility; upstream is the system-managed file.

**Hook conventions (all Stop hooks):**
- Recursion guard: exit 0 immediately when stdin JSON has `stop_hook_active: true` (all 14 Stop hooks carry this as of the 2026-07-06 audit — five were missing it before).
- Scope guard: only enforce when cwd is inside the repo (prefix match on the dynamic root).
- Exit 0 = pass; exit 2 + stderr = block with actionable feedback.
- Instrumentation: session-prime / structural-output / macro-anchor append to `meta/hook-fire-log.md` on fire (this dirties the tree and is why "log hook fires" commits exist).

## Testing hooks manually

```bash
export CLAUDE_PROJECT_DIR=/path/to/repo   # or run from repo root

# Any hook, empty payload — must exit 0 silently (except session-start's briefing):
echo '{}' | python3 research/meta/hooks/<name>.py; echo $?

# Recursion guard — must exit 0 with no block:
echo '{"stop_hook_active": true}' | python3 research/meta/hooks/<name>.py; echo $?

# End-to-end with a fake transcript (anti-fabrication example):
cat > /tmp/test_transcript.jsonl << 'EOF2'
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"GEV backlog $163B; fabricated $999B"}]}}
EOF2
echo '{"transcript_path":"/tmp/test_transcript.jsonl","stop_hook_active":false}' | \
  python3 research/meta/hooks/anti-fabrication-hook.py
# Expected: exit 2, complains only about $999B (the $163B is repo-grounded)
```

## How to add a new hook

1. Write the script in `research/meta/hooks/<name>.py`. Follow the conventions above (dynamic-root preamble on line 2-4, scope guard, recursion guard, exit 0/2).
2. `chmod +x research/meta/hooks/<name>.py`.
3. Test manually (pass case, fail case, recursion-guard case, empty-stdin case).
4. Register in `<repo>/.claude/settings.json` under the right event, using the `"$CLAUDE_PROJECT_DIR"/research/meta/hooks/<name>.py` form. (Optionally add the `~/.claude/` line to the legacy mirror `settings.json` for fallback parity.)
5. Document: this README's table + `research/CLAUDE.md` §"Enforcement hooks (live)".
6. Add/READ the bias entry in `research/meta/biases-watchlist.md` the hook enforces, with fluidity metadata (codified date, falsifier, re-eval trigger).

## Retirement discipline

Hooks are not permanent. Per the fluid-loop rules in `research/CLAUDE.md`: a hook that fires <5×/month for 3 consecutive months is INERT (retire), and every hook codification carries a falsifier. Current open decision: the two-bracket experiment (llm-native-priming + structural-output) 30-day close was due 2026-07-01 and is pending — see `meta/todo.md`.
