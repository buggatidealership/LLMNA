# RECEIPTS HOOK — build spec (adjudicated from K3's say–do-gap proposal, 2026-07-20; build slot 2026-07-24, count-leg joins 2026-08-03)
**Principle (K3's formulation, adopted into #43b/3f as the fourth surface):** a say–do gap is a narration that skipped the post-action read. Fix is structural, not attitudinal: **no action-claim may be emitted that isn't constructible from a same-turn receipt** — the hook re-derives the claimed state itself; pasted receipts don't count. Same gap as the calibration gap: claims about the world become trustworthy only when built FROM a receipt, not TOWARD one. Surfaces already live: P-provenance (predictions), truth-tiers (evidence), fire-log+verdicts (hook history); this hook = the fourth (actions).

## Adjudication of K3's proposal (each claim verified against repo before ruling)
| K3 component | Verification | Ruling |
|---|---|---|
| Incident base: L34/L36/mislabeled-commits/cap-gate | L36 VERBATIM-CONFIRMED (lessons.md 07-17: count-then-commit failed 3× as instruction → deterministic); mislabeled-commit class = 2 documented instances (1294267, a4e2bdd per recurring-audit-log); cap-gate fired live tonight | ACCEPTED — the recurring say–do classes are real and documented |
| "Fully eliminate is not available" honesty bound | Consistent with the day's whole evidence base | ACCEPTED — targets are per-class zero on PARSEABLE classes, sampled lane for the tail |
| Receipts check #1 (committed/pushed) | **OVERLAP FOUND: stop-hook-git-check already deterministically enforces clean-tree + pushed + signature.** The marginal value is CLAIM-ACCURACY only (does the SHA/branch I *stated* match reality) | ADOPT-AMENDED — extend, don't duplicate: verify claimed-SHA == `git log -1` and claimed-push == `@{u}` sync; leave push-state enforcement where it lives |
| Check #2 (count-claims recompute) | = the 1c recompute-and-compare spec (dual-review merged, todo 2026-08-03, data-dependent on 2wk fire-log) | ADOPT — **1c is SUBSUMED as this hook's count-leg**; joins at 08-03, not before (data dependency unchanged) |
| Check #3 (file created/updated → path/content-marker check) | No existing coverage | ADOPT |
| Check #4 (environment claims → CronList/sentinel) | No existing coverage; CronList read is cheap | ADOPT (Phase 1 if cheap, else Phase 3) |
| Mandatory `RECEIPTS:` block on every action message | FP/ergonomics risk: action verbs pervade legitimate prose (plans, quotes, others' actions); K3 itself notes the hook must re-run checks regardless | ADOPT-AMENDED — the BLOCK is optional (multi-action turns); the TRIGGER is the verb-pattern and the hook re-derives state itself. **Precondition: corpus FP backtest of the trigger before ship (the 1c methodology — fresh-Claude's zero-FP-across-corpus standard)** |
| Component A: pre-commit message–diff coherence via noun-claim parsing | Free-prose noun-claim parsing = the same trap class as the REJECTED 1c first sketch (regex over semantics) | ADOPT-AMENDED to the NARROW deterministic form: **(i) telemetry-only diff (hook-fire-log.md sole path) + substantive message (>120 chars, lacking "telemetry") → BLOCK** — kills BOTH documented mislabeled-commit instances; (ii) optional: file paths literally named in the message must appear in the staged diff. No semantic parsing |
| Component B: sampled verifier for the semantic tail (1-in-5 action-heavy turns) | Rule #16/L34 verifier discipline exists; the sampled lane + metric is new | ADOPT as Phase 3 |
| Three-valued verdicts + fail-open | House standard (tonight's grounding rebuild) | ADOPT verbatim |
| Metric: weekly 20-claim sample, per-class mismatch rate, dual falsifiers (no decline → redesign; zero blocks → avoidance audit) | House style | ADOPT verbatim |
| Phasing "Phase 1 this week" | Tonight's track record: solo-shipped hooks took 3 external patch-rounds; B47 precedent = review-grade process for new hooks; curation ratio today ~100% courtroom | **AMENDED: spec booked NOW (this file); trigger corpus-backtest + Phase-1 build at the 2026-07-24 hook-work slot (with log_fire rollout + B47 decision + extractor/tests — one coherent hooks day); count-leg 2026-08-03; Phases 2-3 sequenced behind Phase-1's first 2 weeks of data** |

## Phase-1 build checklist (2026-07-24)
1. Corpus FP backtest of the action-verb trigger over research/*.md + recent transcripts (target: FP ≈ 0 at fresh-Claude's standard; measure recall honestly — low recall acceptable, mislabeled as "the catch layer" not).
2. Implement checks 1-amended, 3 (+4 if cheap) with three-valued verdicts, per-claim diag logging to hook-fire-log (house format), fail-open wrapper, embedded selftest with fixtures per the fixture-growth rule.
3. Pre-commit telemetry-only-diff guard (Component A narrow form) into meta/hooks/git/pre-commit battery.
4. Review pass: route the built spec diff through K3 + a fresh session before wiring into settings.json (the day's standing lesson: author-blind boundaries).
5. Metric wiring: weekly 20-claim sample booked into the weekly quota check (Monday wakes).

**Falsifiers (registered at spec time):** blocks don't decline month-over-month → the hook isn't teaching, redesign or retire; blocks hit zero → avoidance audit (dropping action-verbs to dodge the trigger); trigger FP >2/week in live use → narrow the verb-pattern (same ladder as 1c).
