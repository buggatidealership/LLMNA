# 2026-07-06 — W11 platform-Routine creation: PRE-REGISTRATION (written BEFORE execution) + test protocol

**Authorization:** user "go" 2026-07-06 ~20:4x UTC, with explicit discipline requirement: verify expected outcome BEFORE executing; after implementation, test against expectation.

**Context:** this session (unlike all prior ones) carries the Claude Code Remote platform tools incl. `create_trigger` — server-side Routines (cloud scheduler, container-independent, fresh-session-per-fire mode). This retires the 07-05 "user-side web-UI only" conclusion IF the test passes.

## Pre-registered expected outcomes

| # | Step | Expected outcome | Fail condition |
|---|---|---|---|
| E1 | `create_trigger` "KR-JP morning wake", cron `22 0 * * *`, fresh-session-per-fire, this environment | Returns trigger id (`trig_*`), enabled; **timezone check: if cron fields are UTC-interpreted, `next_run_at` ≈ 2026-07-07T00:22Z (= 02:22 German CEST = 09:22 KST)**. If `next_run_at` shows a different hour → cron is local-tz-interpreted → recreate with corrected fields | Error return; or next_run_at implies a wrong wall-clock hour that can't be corrected |
| E2 | `create_trigger` "EOD synthesis", cron `17 20 * * *`, fresh-session-per-fire | Same shape; next_run_at ≈ 2026-07-06T20:17Z or (if already past 20:17Z today) 2026-07-07T20:17Z | same |
| E3 | `list_triggers` | Both present, enabled=true, schedules as above | missing/disabled |
| E4 | `fire_trigger` on Routine 1 (manual test fire, run-specific note appended) | A FRESH session spawns, clones LLMNA, executes the wake per Workflow #11, and produces **a commit on origin/main (or claude/w11-wakes fallback) authored OUTSIDE this session within ~30 min** — detectable via the single-session-mode provenance rule (any non-this-session commit = routine evidence). PASS = commit exists containing a scan artifact/day-state touch + ledger entry; PARTIAL = session ran but no commit (diagnose: clone/permission/prompt); FAIL = no evidence within ~45 min | no commit + no run evidence |
| E5 | Durability expectation (resolves overnight, NOT today) | The 00:22 UTC scheduled fire happens WITHOUT this session's container being alive — first-ever wake that survives infrastructure. Graded at tomorrow's wake audit vs this pre-registration | no overnight commit → routine-FAIL, in-session cron 547c1ca4 remains the fallback |

## Risk register (pre-registered, my model 🟡)

- R1: cron timezone ambiguity (docs silent) — mitigated by E1's next_run_at check + recreate-if-wrong.
- R2: fresh routine session may lack push permission to main → prompt carries the claude/w11-wakes fallback; PASS either branch.
- R3: test fire (E4) runs pre-prelim (~20:5x UTC, KR/JP closed) → expected output is a SMALL valid wake (catalyst-clock check, docket read, minimal scan) — small-but-committed = PASS (mirrors WAKE-1 silent-small PASS criterion).
- R4: double-fire risk tonight (routine 00:22 UTC + in-session cron 547c1ca4 00:22 UTC, same minute) — ACCEPTED for one night as redundancy; if both fire, the second sees a clean tree (first's commit pulled) and no-ops or duplicates harmlessly; cron is retired after the routine's first proven scheduled fire.

## Retirement condition (pre-registered)

In-session cron 547c1ca4 gets deleted + Workflow #11 "perpetuity requires user-side setup" language gets rewritten ONLY after E4 PASS **and** E5 PASS (tomorrow's audit). Guide + day-state updated at E4; final retirement at E5.
