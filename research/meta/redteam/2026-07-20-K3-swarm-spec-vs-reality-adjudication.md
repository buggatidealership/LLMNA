# 2026-07-20 — K3-SWARM SPEC-VS-REALITY AUDIT → ADJUDICATED SAME EVENING. External 6-agent swarm + orchestrator, evidence base main @ 6493fe1 (1,347 commits, 802 files, all branches). 55 findings (G-01..G-55), 2 BLOCKING — **every spot-checked finding CONFIRMED, zero overturned**: the highest-precision external audit the harness has received.

**Provenance:** user commissioned a fresh K3 session with the GitHub repo link to verify "no gap between expected and actual verifiable/falsifiable harness behavior." Swarm ran READ-only (no execution) and supplied runnable probes for every behavioral claim. Report delivered 2026-07-20 EVE (auditor-clock 07-21). Adjudication protocol: verify every finding against the repo before adoption; run every executable probe; grade my pre-registrations; fix confirmed gaps same turn where computable; date-book the rest.

## Probe execution (their READ-only mandate meant no probe had run — all run here)
| Probe | Their prediction | Result | Verdict |
|---|---|---|---|
| P-1 all 19 hooks compile | OK | **OK 19/19** | r2 claim now RUNTIME-receipted |
| P-2 anti-fab selftest | PASS (22) | **SELFTEST PASS (22 checks)** | ✓ |
| P-6 git-guard bypasses (G-23..G-26, isolated payloads via script — first attempt self-blocked because the probe batch contained a live short-flag `rm -rf` control, which the guard correctly caught) | code-reading predicts exit 0 (bypass) on all 5 | **ALL 5 PASSED-THROUGH pre-patch** (long-flag rm, `find . -delete`, rmtree('.'), lowercase hookspath, `> research/CLAUDE.md`); both controls blocked | **CONFIRMED at runtime → PATCHED same turn → re-probe 5/5 BLOCKED, 9/9 benign controls pass** |
| P-10 C9 master (list_triggers) | expected 4 ACTIVE + 11 inert + 0 deleted | **EXACT MATCH** — both one-shots real (07-24 + 08-03 06:30Z), both Routines active w/ documented last-fires | **930ae1e was a TRUE action-claim**; only the census omission (G-42) stands |
| P-12 hook-count vs docs | 19 vs docs' 17 | 19 | G-05 confirmed; docs fixed |
| G-20 recursion guard | 0 occurrences | grep = 0 | CONFIRMED → guard added + json import (my first patch silently no-op'd on a missing import — caught by compile-check discipline) |
| G-19/21/22/27 code-reads | per rows | all confirmed at cited lines | booked 07-24 (same files as log_fire migration) |

## The two BLOCKING findings — both in the AUDIT tier, both confirmed, both repaired
1. **G-07 — the audit backbone certified a promise as its own receipt.** The 07-17 Test-D line marked the Jul-11 re-evals "Resolved-with-evidence... per CLAUDE.md header" — but the header line IS the promise; both target files are single-commit artifacts (verified: `git log` = 1 each). Struck via appended CORRECTIONS (no silent edits); extractor rule adopted: **header/status lines are PROMISES; only dated execution artifacts or commits are receipts.** The 4 dead re-evals → run-or-retire 07-24 [DUE].
2. **G-08 — the Rule #16 cost-yield adjudication died silently while ~8.95M tokens of verification spend accrued.** Executed tonight, computed from the ledger: 160 entries, 0 ZERO-yield → falsifier NOT fired → **POSITIVE, KEEP** (caveats stamped in the ledger head: self-graded classes; 18 format-drift entries; **the ledger's own appends died 07-10** — a decay the swarm itself missed). Weekly reading folded into Monday quota checks.

## Fixes shipped this commit (beyond the two above)
git-guard 4 bypass classes (G-23..G-26) + `git restore` coverage — probe-verified both directions · cascade-hook recursion guard (G-20) · count-syncs: CLAUDE.md loop caps (#47, PC-21, TC-19, true P-tail "P-1..P-8 + P-11"), methodology 2,071/59, biases B1-B65, tags.md 5 section tails + Rules #19, INDEX 19-wired + B46 rows (G-31..G-35 partial) · Rule 19 canonical text into CLAUDE.md (G-47) · B46 written CONFIRMED into all 3 canonical files, 27 days after the decision (G-14) · B65 promoted VERIFIED + the 1c escalation clause adjudicated explicitly-AMENDED, not silently ignored (G-53: build-now blocked by the 2-week fire-log data dependency; the 08-03 wake guarantees the date) · session-prime MU-phantom line killed + 07-24 scope line now carries INCONCLUSIVE-rate + META-OVERHEAD (G-45/G-50/G-52) · census one-shots appended w/ day-1 rule violation acknowledged (G-42) · DURABLE-ACTIVATION 4 SHAs remapped post-history-rewrite + counts (G-40/G-05) · holdings header re-rolled to the 07-10 canonical book (G-54) · receipts-spec cap-gate incident annotated container-unlogged (G-36) · stale-default-branch named in the audit log as the true cause of all three stale-reviewer incidents (G-44; the fix itself is user-side checklist item 6, booked earlier tonight).

## Pre-registered prediction grades (registered before the report landed)
| Prediction | Outcome |
|---|---|
| Largest gap-class by count = C2 dead promises | **HIT on instances** — 14 DEAD promises in their Appendix A is the largest failure population (by G-ID count C2/C3, C4, C10 tie at 12) |
| ≥1 genuine C1 wiring mismatch | **HIT** — G-03 (git-check genuinely rides ~/.claude) + G-05 (fallback mirror wires a missing file) |
| Empty C4 would be suspicious | Correctly non-empty — 12 findings, 5 runtime-confirmed the same evening |
| NOT predicted | Both BLOCKING findings sit in the audit tier — the layer that grades the others had no one grading it. Author-blindness to boundaries, 4th demonstration in 24h |

## Register updates (append to the r2 residuals register, which this supersedes as the day's final)
12. **NEW (G-29, probe-only):** a dense uncited comps-table can exhaust the 15s grounding budget and route trailing needles to INCONCLUSIVE without infra stress — deterministic variant of residual #1; per-needle skip-reason logging booked 07-24.
13. **NEW (G-51):** residual #3's "sample flips against transcripts" is unexecutable (transcripts don't survive container recycling) — amended to artifact-level instruments (fire-log + verdicts).
14. **NEW:** the swarm's residuals-honesty verdict on the r2 register: **HONEST** — every recomputable claim reproduced exactly; two scoped-overstatements (entries 3, 6) + the "4 of 5" headline undercounting its own 6-row table (G-37) accepted as B65-class drift in my own paperwork, again.

**The arc's law, re-proven by an independent adversary at full-harness scale:** the swarm's negative-results section found the *enforcement* surface (wiring 1:1, fire receipts, grading discipline, 313/318 references) matches its promises — while both BLOCKING failures were *audit-tier self-certifications*. Computed-vs-recalled remains the exact boundary of trustworthiness; the receipts hook (07-24) and count-leg (08-03) are aimed at precisely the surface that failed.

**Position implication: NO ACTION (harness-meta; no market exposure). 🟢 all executable probes run — 5 guard bypasses confirmed-then-closed with fixture-grade probes both directions; C9 reconciled clean against the platform; both BLOCKING findings repaired with receipts; 🟡 residuals +3; the deferred set is dated, not parked (07-24 wake + [DUE] elevation + hard 08-06 sub-deadline for G-28). Net-positive test: an external audit at ~0 marginal build cost closed 2 BLOCKING + 5 runtime-confirmed guard holes and re-proved the program's central law on adversarial evidence.**
