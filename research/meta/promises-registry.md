# Promises Registry — machine-checked dated commitments

**Born:** 2026-07-22 (accounting-layer commission, K3 themes 1+4: "promises made
faster than kept" — ≥6 dated re-evals silently died; the deadline-catcher scanned
document *titles* while deadlines hid in prose).

**Contract:** every dated promise the harness makes (re-eval, adjudication,
recalibration, review pass, audit) gets ONE line here at promise time.
`promise-heartbeat.py` (SessionStart) parses this file every session and FAILS
LOUD (🚨 banner + hook-fire-log append) on any OPEN line past its DUE date.
A promise leaves the loud list only by being marked DONE **with a receipt**
(file path, commit SHA, or log entry) — a header/status line is a PROMISE,
not a receipt (K3-Swarm G-07).

**Line format (machine-parsed; one line per promise):**
```
- [ ] DUE:YYYY-MM-DD | WHAT: <one-line promise> | SOURCE: <file/anchor that made it>
- [x] DUE:YYYY-MM-DD | WHAT: ... | SOURCE: ... | DONE:YYYY-MM-DD RECEIPT: <path/SHA/log line>
```

## Open promises

- [ ] DUE:2026-07-24 | WHAT: Receipts-hook Phase-1 diff review pass by K3 + a fresh session before the hook is considered settled (spec step 4, author-blind boundaries) | SOURCE: meta/hooks/receipts-hook-spec.md §Phase-1 checklist item 4
- [ ] DUE:2026-07-24 | WHAT: triage the promise-heartbeat prose-sweep backlog (41 past-dated promise-phrases at first sweep 2026-07-22) — each becomes a registry line, a DONE-with-receipt, or a documented retirement | SOURCE: first run of meta/hooks/promise-heartbeat.py
- [ ] DUE:2026-07-24 | WHAT: subagent-cost-yield-ledger append-discipline decision — backfill 07-10→07-22 gap or formally scope it | SOURCE: meta/subagent-cost-yield-ledger.md header caveat (c)
- [ ] DUE:2026-07-24 | WHAT: PRUNING DISCIPLINE monthly pass (context-hygiene) | SOURCE: meta/todo.md P2 recurring
- [ ] DUE:2026-08-03 | WHAT: Receipts-hook count-leg joins (1c recompute-and-compare; needs 2 weeks of anti-fab fire-log data) | SOURCE: meta/hooks/receipts-hook-spec.md check #2
- [ ] DUE:2026-08-06 | WHAT: structural-output/priming-hook keep-vs-retire adjudication via structural-output-metric.py (normalized rate falling → keep; flat/rising → retire) | SOURCE: research/CLAUDE.md structural-output-hook entry + meta/structural-output-metric.py
- [ ] DUE:2026-08-15 | WHAT: Critical Rule #16 verification-subagent cost-yield re-eval (the revived G-08 dead loop — 07-15 instance ran 5 days late only because an external audit caught the silent death) | SOURCE: meta/subagent-cost-yield-ledger.md header
- [ ] DUE:2026-08-22 | WHAT: receipts-hook falsifier review — blocks declining month-over-month? zero-block avoidance audit? FP >2/week narrowing? | SOURCE: meta/hooks/receipts-hook-spec.md §Falsifiers
- [ ] DUE:2026-09-12 | WHAT: B45 regime-corrected-priors quarterly recalibration (15-name basket re-verification) | SOURCE: research/CLAUDE.md B45 banner + meta/session-prime.md
- [ ] DUE:2026-09-12 | WHAT: session-prime cohort recalibration | SOURCE: meta/session-prime.md §Audit line

## Done

(archive: move completed lines here with DONE + RECEIPT fields)
