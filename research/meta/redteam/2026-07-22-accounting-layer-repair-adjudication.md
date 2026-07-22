# 2026-07-22 — ACCOUNTING-LAYER REPAIR: adjudication + receipts

**Session:** fresh harness-only session commissioned by
`2026-07-22-K3-harness-state-opinion-and-fresh-session-commission.md`.
**Mandate (K3 reframe):** do NOT re-audit the enforcement hooks (they mostly
work, just reviewed). Repair the **ACCOUNTING layer** — the logs, receipts,
promise-tracking, and self-grading the harness reports about itself. Target:
make it structurally impossible for the logbook to claim "done/verified"
without a machine-checkable receipt.

**Branch:** `claude/harness-accounting-audit-it2e0w` (rebased onto `origin/main`
at 10c7b10 at session start — the default-branch flip made a fresh session boot
on LIVE state, not the 07-06 snapshot).

**Rule this session held itself to:** every commit carries a machine-checkable
receipt (selftest exit code, fixture battery, backtest count, or `--check`).
No commit claims "done/verified" on narration alone — the say-do gap this
session exists to close, applied to the session's own work.

---

## The 6 commission items → commits → receipts

| # | Item (K3 theme) | Commit | Receipt (machine-checkable) |
|---|---|---|---|
| 1 | Receipts layer / say-do gap (theme 1, deepest) | 817ac3a | `receipts-hook.py --selftest` 13/13; `--backtest` 755 files → **0 FAIL** (tuned from 55 raw); wired as Stop hook 16 |
| 1b+4 | Promise heartbeat / dead-loop revival + in-prose deadlines (themes 1+4) | 803547c (corrects 352ab45) | `promise-heartbeat.py --selftest` 8/8; first live sweep = 3 due-soon + 41 prose candidates; wired SessionStart |
| 2 | Oracle-backed reworks — git-guard -n + rm boundary, PI IGNORECASE, tier-gate fixture (theme 2) | 0b214c1 | bypass-probes 24/24 (5 K3-oracle payloads verbatim); adjacency-FP 8/8; tier-gate+casing 16/16 |
| 3 | Metric integrity — G-28 numerator + origin/main-first + denominator (theme 3, BLOCKING pre-08-06) | a16e036 | `structural-output-metric.py --selftest` 12/12; live run ref=origin/main, 168 telemetry commits excluded, trend 0.815→0.197 FALLING on the de-contaminated metric |
| 5 | Computed-counts generator (theme 5) | 7aac61e | `computed-counts.py --selftest` 11/11; `--audit` matched known-good (B65/P47/R19) + flagged 3 real drifts; `--check` clean after `--write` |
| 6 | Room-independent guards — nap window + redirect-FP + exit-path inventory (theme 6) | 832b8ab | redirect-FP 10/10 (incl. exact live-repro); receipts-hook 16/16 (nap cases 14-16); guard-exit-path-inventory.md |

**Consolidated re-run at adjudication time (2026-07-22, HEAD 832b8ab):** all 4
selftests exit 0, all 4 fixture batteries exit 0, `computed-counts --check` clean,
`receipts --backtest` 0 FAIL. Every green light above is reproducible from the
committed tree.

---

## What each fix actually changed (first-principles, not narration)

**Theme 1 — referee grades its own homework.** Before: a commit/message could
claim "committed X / pushed / created Y" with nothing re-deriving it; the two
"this is due" loops (Rule #16 re-eval, G-08) died silently while ~8,952k tokens
they were meant to judge accrued. After: `receipts-hook` RE-DERIVES every
action-claim (git cat-file for SHAs, working-tree for file claims, @{u}-sync for
push claims) — three-valued (PASS/FAIL/UNVERIFIABLE), fail-open, corpus-backtested
to 0 FP. `promise-heartbeat` + `promises-registry.md` make any OPEN dated promise
past DUE fail LOUD every session and append to the (git-committed) fire-log — a
silent death is now structurally impossible while sessions start. The heartbeat's
prose sweep reads sentences, not just titles (theme 4's in-prose blind spot).

**Theme 2 — can't proofread own work; external oracle is the fix.** All 4
confirmed K3 holes closed on K3's EXACT payloads as permanent fixtures (not
self-authored probes): commit `-n` anywhere-after-commit (my own 07-21
adjacency-tightening had regressed it); rm boundary for tilde/HOME/trailing-slash
(repo-ancestor spellings); PI matcher `re.IGNORECASE`; tier-gate fixture made
path-relative + case-4 adjudicated (the hook over-fired on the hyphenated
"joint-state" spelling its OWN feedback demands — fixed the hook, kept exp=0).

**Theme 3 — scoreboard movable by the player.** The 08-06 decision metric had
THREE contamination channels, all closed with machine-checkable rules + a
selftest: (A) numerator counted 15 tier-fires that belong to an UNRELATED
enforcement (Principle #37) — now counts only genuine structural-markers-missing;
(B) probe pollution — test runs appended real fires (observed LIVE at 08:29Z) —
now [probe]-tagged and excluded; (C) ref-order origin/main-first per design-130
(local-first swung the rate 0.196→0.452 on ref choice alone); (D) denominator
excludes telemetry-only commits (padding biased the rate toward "priming works").

**Theme 5 — written map lags territory.** `computed-counts.py` regenerates 7
tail counts from their source files; `computed-counts.md` is now canonical and
prose headers point to it. On its FIRST real run it caught live drift (hooks
19→21, Principle tail 46→47, L-tail 39→40 — L40 was added THIS session). A
pre-commit drift-warn (non-blocking pending review) fires when a counted source
is staged.

**Theme 6 — guards only in some rooms.** Full exit-path inventory of both guards
(the git-guard's 5 paths + the commit+push gate's 8 K3-flagged paths). The
post-block nap window is closed for the receipts-hook via a content-scoped
recursion guard (nap only on identical re-sends, re-enforce on any change). The
redirect over-block FP (reproduced LIVE 2×) is fixed by anchoring the protected
match to the redirect TARGET token. The load-bearing residual is NAMED, not
hidden: the commit+push gate runs from the environment launcher and may be ABSENT
headless — unfixable repo-side without a double-fire; recorded honestly.

---

## Honest residuals (named, not hidden — the say-do discipline applied to myself)

1. **Receipts-hook is Phase 1.** Count-leg (1c recompute) joins 08-03; semantic
   tail (sampled verifier) is Phase 3. It catches PARSEABLE action-claims; a
   claim phrased entirely outside the verb+object patterns is UNVERIFIABLE, not
   caught. Falsifier review registered 08-22.
2. **Metric branch mismatch.** Numerator fires are logged globally (working tree)
   while the denominator is trunk-measured (origin/main) — the in-progress
   branch's fires count against trunk commits until merge. Inherent to the log
   format; resolves at merge, before 08-06.
3. **Denominator still partly gameable.** Non-telemetry filler commits can still
   pad it. A single normalizer cannot be un-gameable; stated in the file.
4. **Count "max" ≠ count "present".** Ranges have retired/skipped numbers; the
   headers cite the tail, so max is the right quantity (stated in computed-counts.md).
5. **Nap window closed only for receipts-hook.** The other 15 analytical Stop
   hooks keep the blanket nap; propagation to integrity-critical ones is a
   registered reviewable follow-up (08-01) — a 15-hook unreviewed refactor is
   exactly the "builder's blind spots ship inside every patch" risk.
6. **NOT externally reviewed.** These patches were built and probe-gated SOLO.
   The session's own deepest lesson (theme 2) is that same-model solo probes pin
   holes as imagined and miss holes as spelled. An external adversarial pass
   (K3 or a fresh session) over this diff is registered as a promise (07-24) and
   is the honest gate before these are considered settled.

## Follow-up promises registered (promises-registry.md)

07-24: receipts-hook diff review pass; promote computed-counts --check to
blocking; repo-side commit+push backstop review; prose-sweep backlog triage.
08-01: content-scoped-guard propagation. 08-03: receipts count-leg.
08-06: structural-output adjudication (now on the clean metric). 08-15: revived
Rule #16 re-eval. 08-22: receipts falsifier review. 09-12: B45 + cohort recalibration.

**Position implication: NO ACTION (harness-meta). 🟢 all 6 commission items shipped
with reproducible receipts; the metric is de-contaminated before 08-06 and the
promise loops can no longer die silently. 🟡 the patches are solo-built — the
registered external review (07-24) is the real settle gate, per this session's own
theme-2 lesson. 🔴 the headless-absence of the commit+push gate is a NAMED
residual that cannot be closed repo-side.**
