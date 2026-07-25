# 2026-07-22 — K3's "state of the harness" opinion + FRESH-SESSION COMMISSION

**Origin:** user asked K3 for its first-principles opinion on the whole harness (beyond the deep-dive review). K3 returned a 6-theme diagnosis (below). User's decision: spin a FRESH Claude session dedicated to harness work. This file = the opinion capture + the fresh session's mandate + boot instructions. **Prerequisite already met:** GitHub default branch flipped to `main` this same session (API-confirmed) — a fresh session now boots on LIVE state, not the 07-06 snapshot. An hour earlier this commission would have been impossible.

## K3's diagnosis — the load-bearing first principle
> The machinery is genuinely good — the wires, alarms, and logs largely do what their labels say — but the **paperwork ABOUT the machinery** is where reality and expectation part ways, and the system's own fixes keep needing a second pair of eyes because the builder's blind spots ship inside every patch.

"Who audits the auditor" is the unsolved layer. The locks mostly work; the **logbook about the locks** occasionally lies.

## The 6 themes (K3, ranked by depth) + convergence with booked state
1. **Referee grades its own homework — and sometimes fakes the grade.** Inspection log certified reviews "done" by pointing at the sentence that *promised* them (promise-as-proof). Two "this is due" loops silently stopped — one while ~9M tokens it was meant to judge kept accruing. → **DEEPEST.** Maps to G-08 (Rule #16 re-eval died silently; ledger ~8,952k tokens = K3's "9M") + Receipts-Hook Phase 1 (07-24). The unsolved layer.
2. **Can't proofread own work — 5× in 48h.** Patches held vs the author's imagined attacks, failed one character away (`~/LLMNA/` trailing slash; `-n` after the message). → **Independently reproduced 2026-07-22** (`2026-07-22-K3-deep-dive-review-adjudication.md`, 4 holes). External oracle = the fix.
3. **Scoreboard movable by the player.** 08-06 metric = alarms÷commits; system authors its own commits (denominator) and can edit the alarm log in a mixed edit (numerator); e04eaef reversed which scoreboard copy it trusts. → G-28 BLOCKING + e04eaef, pre-08-06 (booked).
4. **Promises made faster than kept.** ≥6 dated re-evals silently died; the deadline-catcher scans *documents for dates* while deadlines hid in prose sentences. → Receipts/say-do gap (partial); deadline-scanner in-prose blind spot = NEW scope.
5. **Written map lags territory.** Rulebook said 17 hooks (19), #46 (47); the stale-count fix shipped stale. → B65 compute-don't-recall (partial); apply the computed-counts law everywhere, not just to fire-counts.
6. **Guards only in some rooms.** A key guard lives outside the project wiring → may be absent in fresh/headless; docs speak as if it's everywhere. Plus: after any alarm fires, a brief window where all guards (incl. commit+push) take one nap. → K3 Q5 blind spots (booked today).

## FRESH-SESSION COMMISSION (paste to the new session as its opening task)
**Mandate — reframed per K3:** do NOT re-audit the enforcement layer (hooks mostly work; today's K3 review already did it). Audit and repair the **ACCOUNTING layer** — the logs, receipts, promise-tracking, and self-grading that the machinery reports about itself. Target: make it structurally impossible for the logbook to claim "done/verified" without a machine-checkable receipt.

Boot: read `research/CLAUDE.md` + `research/INDEX.md` + this file + `meta/redteam/2026-07-22-K3-deep-dive-review-adjudication.md` + `meta/todo.md` P0 (the 07-24 slate). You are on `main` (default branch — verify with `git rev-parse --abbrev-ref HEAD`).

Ordered work (the P0 07-24 slate, re-sequenced by K3's depth ranking):
1. **Receipts layer (theme 1 — deepest).** Build the say-do / "who audits the auditor" enforcement: every "done/verified/audited" claim in a commit or artifact must carry a machine-checkable receipt (a computed count, a test exit code, a git ref), else it doesn't count. Revive the 2 dead audit loops with a heartbeat that FAILS LOUD on a missed date. Phase 1 spec exists in the 07-24 todo.
2. **Oracle-backed patch reworks (theme 2).** The 4 confirmed holes — git-guard `-n`-anywhere + rm boundary (tilde/HOME/trailing-slash), structural-output PI matcher `re.IGNORECASE`, the red tier-gate fixture — probe-gated on K3's EXACT payloads (in the adjudication file) as permanent fixtures, not self-authored probes.
3. **Metric integrity (theme 3, HARD pre-08-06).** G-28 numerator reclassification + e04eaef ref-order (origin/main-first for session containers); harden the denominator against self-authored-commit gaming.
4. **Deadline/promise heartbeat (theme 4).** Extend the date-catcher to in-prose deadlines; loud-fail on any missed re-eval.
5. **Computed-counts everywhere (theme 5).** Replace hand-written header counts (hooks/principles/lessons/biases) with a computed generator; the map regenerates from the territory.
6. **Room-independent guards (theme 6).** Close the headless-absence + post-block-nap windows; inventory the git-guard's exit paths.

Deliverable: an adjudication artifact + probe-gated patches, each commit carrying its receipt. Keep positions/market work OUT — this session is harness-only.

**Position implication: NO ACTION (harness-meta). 🟢 external diagnosis converges with the booked 07-24 slate; the reframe (audit the accounting, not the machinery) sharpens the mandate; default-branch fix makes the fresh session viable.**
