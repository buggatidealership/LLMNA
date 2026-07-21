# 2026-07-21 — Harness deep-dive ADJUDICATION + self-patch log

337-agent workflow; 362 mechanics; 8 HIGH. Self-patched under the operator
no-delay directive, **probe-gated**: every fix = probe proves the hole open →
patch → probe proves the hole closed AND benign controls still pass → atomic
commit + fixture. Model note: Fable-5 is the weaker *reviewer* (CodeRabbit T2),
so verification leaned on OBJECTIVE probes, not self-review confidence.

## Coverage (computed from the journal; raw at `2026-07-21-harness-deep-dive-RAW-journal-extract.json`)
362 mechanics: 201 MATCH / 83 DEFECT / 72 GAP / 6 UPGRADE. Verify pass: 167
confirmed / 2 refuted. **Zero BLOCKING; 8 HIGH.** 131 patches designed.

## APPLIED tonight (5 of 8 HIGH — probe-verified, atomic reversible commits)
| # | Finding | Commit | Verification |
|---|---|---|---|
| 1 | git-guard: recursive delete aimed at the env-var root or the tilde repo path slipped past the G-24 hardening (the rm branch never consulted REPO_TOKENS) | f25a66f | probe 17/17 |
| 2 | git-guard: the short-flag skip on a git commit bypassed pre-commit + commit-msg; TEMPERED then ADJACENCY-tightened to avoid two live prose/message false-positives found while patching | f25a66f (+adjacency follow-up) | probe 17/17 + 8-case FP probe |
| 3 | structural-output-metric crashed (git exit 128) on session-branch containers with no local main ref, killing the 08-06 adjudicator | e04eaef | runs + fallback proven |
| 4 | structural-output: the 800-char size gate ran BEFORE the position-implication tier check, so short sizing lines escaped it (G-27) | f19663d-adjacent | probe: short+untiered blocks; tiered/no-line pass |
| 5 | session-start: the stale-tier scan regex matched 7 of 83 headers (forcing function 92% blind) | f19663d | computed 7→83; runs clean |

## DEFERRED to the 2026-07-24 review-grade slot (3 of 8 HIGH + all MEDIUM/LOW)
- **structural-output-metric numerator reclassification (G-28)** — SEMANTIC change to a PRE-REGISTERED experiment's scoring (position-implication-tier fires wrongly counted in the priming-experiment numerator). Design ready; changing an experiment's adjudication rule warrants review, not a solo late-night apply. Must land before 08-06.
- **session-prime-cascade HEAD-only changeset window (G-19)** — needs diff-against-last-Stop-ref logic; judgment-heavy. Masked today because the git-check forces one-commit-per-Stop.
- **stop-hook-git-check inventory/doc gap** — doc-only (add the system-managed commit+push hook to CLAUDE.md's hook list); batch with the doc sweep.
- ~150 MEDIUM/LOW findings (regex-coverage holes, scope-guard edges, cosmetic) — batched.

## NEW findings surfaced DURING patching (book for 07-24)
1. **redirect-guard over-block (MEDIUM FP):** git-guard's `>`-redirect branch blocked a redirect whose TARGET was a /tmp scratch path, because the command text contained a protected path elsewhere (in a git-show arg). Fix: anchor the protected-path match to the redirect TARGET token, not anywhere-after-`>`.
2. **short-flag-skip prose FP (MEDIUM, MITIGATED tonight):** catching the commit short-flag is inherently prose-FP-prone because the guard scans whole command text. Mitigated to only literal `git`+commit adjacency; residual = a command whose text contains the literal adjacency still blocks. Documented in-code + fixture.
3. **hooks error (exit 1) when run outside the repo** (path resolution from `__file__`) — not fail-open-clean (exit 0), though exit 1 is non-blocking in practice. LOW; note for the fail-open census.

**Position implication: NO ACTION (harness-meta). 🟢 5 HIGH closed with objective probes + durable fixtures, atomic reversible commits; 🟡 3 HIGH + tail deferred to the reviewed slot by design (weaker-reviewer discipline); 3 new FPs/limits surfaced by the act of patching and booked.**
