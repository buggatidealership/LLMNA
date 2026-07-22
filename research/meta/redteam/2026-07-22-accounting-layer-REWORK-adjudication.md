# 2026-07-22 — ACCOUNTING-LAYER REWORK after K3 "NOT SAFE TO MERGE"

**What this is:** the repair of `claude/harness-accounting-audit-it2e0w` after
K3's blind cross-family review found it NOT SAFE TO MERGE (5 load-bearing
findings) and a separate Opus session reproduced the top findings by execution.
Each of the 7 rework items was **reproduced before fixing** and **proved through
the ACTIVATION CHAIN** (the way `settings.json` actually fires the hook), not by
a `--selftest`. A selftest green is what shipped the original failure.

**Merge gate (unchanged):** this branch is handed back for a **second K3
cross-family pass**. I am the same model lineage as the builder whose blind
spots shipped the first version; I do not self-certify merge-ready. Nothing here
was merged to main.

## The failure that caused the first miss (and the discipline that answers it)
The builder tested every hook with `python3 hook.py --selftest` (the COMPONENT)
and never fired it the way the harness does (bare path). The two core hooks
shipped mode `100644` → invoked by bare path they exit 126 and enforce nothing.
**L38: component-green ≠ system-green.** Every rework item below carries an
activation-chain receipt for that reason.

A second discipline recurred four times this session and is a codification
candidate — **"an FP-fix is a patch and needs its own adversarial pass"**
(proposed L41): loosening a matcher to kill a false-positive can open a real
hole. It bit the original branch (the `[^>0-9]` redirect FP-fix opened `1>`/`2>`;
the `LLMNA_HOOK_TEST` probe-tag became a scoreboard lever). This rework ran an
explicit refute-my-own-loosening pass on every FP-fix (push-skip, malformed-line
detector, tee/cp dest matcher) and each caught a would-be regression before ship.

## The 7 items → reproduction → fix → activation receipt

| # | Item (K3 finding) | Commit | Reproduced (before) | Proved via activation chain (after) |
|---|---|---|---|---|
| 1 | exec-bit / L38 | 7c137b0 | bare-path fire of both hooks → **exit 126** (Permission denied) | both committed `100755`; `test_hook_activation_chain.py` 26/26 — parses settings.json, asserts every wired script hook committed-executable via `git ls-files -s`, fires the 2 new hooks by bare path (receipts BLOCKS a fabricated claim, exit 2; heartbeat exit 0) |
| 2 | receipts laundering + repo-ahead FP | 301be0c | fabricated SHA FAILs, then after its block-line is committed to the log the identical claim LAUNDERS to pass; "I haven't pushed yet" / "Yesterday I pushed" FALSE-FAIL while ahead | corpus-grounding REMOVED (fabrication can't launder); PUSH_SKIP covers contractions + unambiguous historical + intent; **adversarial pass**: "I already pushed" still FAILs while ahead; selftest 25/25; backtest live-prose FAIL = 0; fabricated-SHA blocked by bare-path fire (exit 2) |
| 3 | heartbeat: receipt-to-close, malformed/poison, log-before-state | c6a8708 | unreceipted `[x]` silently closes; `DUE: ` (space) invisible → "all current"; poison date crashes the whole lane; state written before log | receipt required to close (else stays OVERDUE + flagged); malformed/poison surfaced LOUD, lane survives; log-before-state; **adversarial pass**: fenced format-examples not mis-flagged; selftest 15/15; **bare-path fire against a poison registry** surfaced poison + unreceipted-[x] + the real overdue below the poison line, exit 0 |
| 4 | git-guard global-option commit-n + tee/redirect/cp | e09e8cd | 10 live bypasses: `git -c x=1 commit -n`, `--no-pager`, `1>`/`2>`, tee, cp/install onto protected → exit 0 | commit-n adjacency widened to any git global options; fd-redirect digit-exclusion dropped (2>&1 still safe); tee/cp/install/mv dest guarded via boundary-correct PROTECTED_DEST; **adversarial pass**: `cp CLAUDE.md CLAUDE.md.bak` NOT blocked; `test_git_guard_rework4.py` 24/24; no regression on 3 prior batteries; 4 representative bypasses blocked by **bare-path** guard fire |
| 5 | metric: env-var lever, log rewrite, cross-hook injection | 09b0118 | `LLMNA_HOOK_TEST` tag zeroes numerator; alarm-log rewritable in a mixed commit; a promise-heartbeat line containing the fire phrase is miscounted | env tag REMOVED (tests isolate via temp CLAUDE_PROJECT_DIR — a non-stealth lever); pre-commit Function 6 makes hook-fire-log APPEND-ONLY (real-commit test: append passes, delete BLOCKS, operator override passes); metric regex anchors hook-source after the timestamp; metric selftest 14/14 |
| 6 | re-verify + close CLAUDE.md drift | 3477f66 | branch's own `computed-counts.py --audit` flagged its CLAUDE.md "19 live" as DRIFT (territory 21) | CLAUDE.md points at computed-counts.md (21); --audit no drift, --check clean; 4 git-guard tests isolated; **NO-POLLUTION invariant**: real hook-fire-log md5 UNCHANGED across the full suite |
| 7 | this artifact | (this commit) | — | full-suite receipt below |

## Full-suite receipt (re-run at rework close, HEAD 3477f66)
- 7 fixture batteries exit 0 (activation-chain, git-guard bypass/adjacency/redirect/rework4, tier-gate, pre-commit append-only)
- 4 selftests exit 0 (receipts, heartbeat, computed-counts, metric)
- `computed-counts.py --check` exit 0 (map == territory)
- real `hook-fire-log.md` byte-stable across the entire suite (no test writes to the numerator source)

## Honest residuals (named, not hidden)
1. **Not externally re-reviewed.** Same-lineage builder; the second K3 pass is the
   real merge gate. This artifact stops at "ready for K3 re-review."
2. **Receipts is still Phase 1.** It catches parseable action-claims; a claim
   phrased entirely outside the verb+object patterns is UNVERIFIABLE, not caught.
   Removing corpus-grounding makes the backtest show 6 historical-record-file
   citations (ledgers/logs the live hook never reads as messages) — classified
   out, live-prose FAIL = 0.
3. **git-guard residuals remain by design:** a literal `git commit -n` inside
   unstripped prose still blocks (documented); the guard is a confused-agent
   backstop, not an adversarial-human sandbox.
4. **Metric denominator** still partly gameable by non-telemetry filler commits;
   a single normalizer cannot be un-gameable (stated in the metric).
5. **L41 candidate** (FP-fix-is-a-patch) reached N=4 this session — recommend
   codifying it into `predictions/lessons.md` + a biases entry next session.
6. **Nap-window propagation** (content-scoped recursion guard beyond receipts-hook)
   and the headless-absence of the commit+push gate remain registered promises
   from the prior session, out of this rework's scope.

**Position implication: NO ACTION (harness-meta). 🟢 all 5 K3 findings + the CLAUDE.md
irony repaired, each reproduced-before-fixed and proved through the activation
chain, no test pollutes the numerator source. 🟡 every FP-fix got its own
adversarial pass (L41), catching 3 would-be regressions before ship. 🔴 NOT
self-certified merge-ready — the second K3 cross-family pass is the gate; main
untouched.**
