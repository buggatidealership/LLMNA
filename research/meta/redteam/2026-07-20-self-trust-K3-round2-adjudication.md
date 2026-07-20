# 2026-07-20 — K3 ROUND-2 (post-build verification) → ADJUDICATED + PATCHED SAME TURN. All 3 headline defects empirically confirmed before accepting; 8-fix patch shipped; selftest expanded 8→20 checks, PASS.
**Sequence: build shipped (dual-review adjudication) → round-2 verification inputs issued → K3 round-2 returned → THIS adjudication + patch. Fresh-Claude round-2 (empirical, in-repo) still PENDING — it now verifies the PATCHED build. Companion: `2026-07-20-self-trust-dual-review-adjudication.md`.**

## Empirical verification of K3's claims (computed before accepting — Rule: verify, don't take on argument)
| K3 defect | Verification method | Result |
|---|---|---|
| #1 Negative rc (signal-killed grep) → false FIRE | Monkeypatched `_grep_repo` to return rc=-9 → `ground_needle` returned **FABRICATED** | **CONFIRMED** — the `rc is None or rc >= 2` boundary let signal-kills fall through to a fire |
| #2 Leading-dash needle → grep option-injection | Ran `_grep_repo("-12.62%")` → **rc=2** (option-parse error → permanent INCONCLUSIVE for signed forms). Also confirmed LATENT: current regexes capture `'12.62%'` without the sign | **CONFIRMED (latent)** — "latent is how the last bug lived" accepted |
| #5 Fire-log self-minting | Planted a repr-logged needle line in a research/*.md file → re-grep of the RAW needle returned **rc=0 (GROUNDS)**; removed → rc=1 | **CONFIRMED — recursion-grade.** repr quoting does NOT prevent substring match; one fire would mint a permanent exemption for its own fabricated number. `meta/audits/` also exists → same exposure via committed audit packs |
| #3 diag records last form only | Code-read: `diag["rc"]` overwritten per loop iteration | CONFIRMED |
| #4 FIRE-line truncation can drop the cause | Code-read: `entries[:5]` in detail while n= counts all | CONFIRMED |
| #6 Unbounded timeout budget | Arithmetic: 2 forms × retry × 10s × K needles serial | CONFIRMED |
| #7 Empty needle → INCONCLUSIVE spam | Code-read | CONFIRMED |
| #8 Silent log-write failure | Code-read: try/except-pass with no fallback | CONFIRMED |

## PATCHED same turn (anti-fabrication-hook.py; selftest 8→20 checks, PASS 20/20)
1. **Infra-error boundary** = `rc not in (0, 1)` — negative/signal rcs now INCONCLUSIVE, never a false FIRE.
2. **`-e` before the needle** — signed needles grep cleanly (fixture added: signed absent → FABRICATED).
3. **Grounding-corpus exclusions:** `--exclude=hook-fire-log.md --exclude-dir=audits` — the hook can no longer mint its own exemptions; hermetic selftest fixtures prove log-only and audits-only needles do NOT ground while regular files still do.
4. **Per-form diag** `[(form-repr, rc, exc), ...]` + `matched_form` on GROUNDED (raw-vs-collapsed match distinction preserved for FP adjudication).
5. **FIRE lines carry ALL fabricated needles** (the cause can never be truncated away); INCONCLUSIVE detail caps at 5.
6. **Shared 15s budget** (monotonic deadline across all needles/forms; past it → INCONCLUSIVE "BudgetExceeded").
7. **Empty needle → SKIP** (never logged).
8. **`log_fire` returns the formatted line either way; main() embeds it in the block feedback** — the transcript is now the backup log; a disk-full failure can no longer recreate the un-logged condition. (K3's session-start canary for log-writability: already exists de facto — session-prime-hook writes a telemetry line every session start; if the log were unwritable, that line's absence is the canary.)

## Rulings on the non-code findings
- **Canary/avoidance merge — NO DRIFT, confirmed:** shipped 3f text carries BOTH (a) canary and (b) avoidance-audit as separate clauses; K3's complement framing now explicit via amendment (ii).
- **Backtick-deferral — K3 AGREES with the deferral**, and its sharper insight is adopted: the mention-vs-claim class is real (self-discussion resistance), and **the corpus-exclusion fix partially heals it in the wrong direction** — note the subtlety K3 caught: quoting a logged fire NO LONGER grounds (log excluded), so discussion-of-fires may re-fire. Accepted as a NAMED residual (below) with the escape hatch: quoted needles in postmortems get explicit `(illustrative)` hedges (already a citation-pattern the hook accepts).
- **Item-3 concession** recorded: K3 independently confirms the duplication verdict and concedes its round-1 miss — reviewer-quality datum both directions.
- **Recursion hunt — all 5 adopted:** (1) clock-source unverified → monthly cross-check vs git timestamps (todo + 3f amendment iii); (2) **canary-poisons-corpus** → canary lives outside the grounding corpus or is removed same-commit (3f amendment i — this was the sharpest catch: the liveness test would have contaminated the reference corpus, the mechanism-(B) recursion class exactly); (3) unicode-space mechanism held to receipt standard — status PLAUSIBLE-UNRECEIPTED until a per-form diag shows an actual unicode needle (3f amendment iv); (4) verdict-flip must cite its computed source (3f amendment vi + log_fire docstring); (5) fixture-growth rule — every FP adjudication adds a fixture (3f amendment v + selftest docstring).

## Residuals register (updated; supersedes the dual-review list)
1. Real fabrication during infra stress passes as logged INCONCLUSIVE (accepted, audit-visible).
2. Round-number fabrications structurally pass grounding (canaries use unusual precision).
3. Verdict-flip is an LLM discipline — flip must cite computed source; monthly audit samples.
4. Fire-to-commit gap on hard container kill (mitigated: line embedded in block feedback → transcript backup).
5. **NEW — self-discussion resistance:** postmortems quoting fired needles can re-fire the hook (log now excluded from grounding); escape = `(illustrative)` hedge on quoted needles.
6. **NEW — false-FIRE-class closed but monitored:** the negative-rc fix is deterministic; the INCONCLUSIVE rate is monitored monthly (a spike = the hook silently degrading).
7. **NEW — fire-log growth unbounded** (rotation policy at the 07-24 audit, folded into the log_fire house-standard item).
8. 1c emission-time tripwire still unshipped (due 2026-08-03) — the trigger phrasing is closed only by priming item 11 + log existence until then.
9. Clock source unverified (monthly cross-check booked).

**Position implication: NO ACTION (harness-meta). 🟢 patch shipped + selftest-verified 20/20 (all 8 K3-r2 defects closed, 3 empirically confirmed first); 🟡 residuals register updated with 4 new entries; fresh-Claude round-2 now verifies the PATCHED build — its findings adjudicate against this artifact. Net-positive test: two recursion-grade defects (self-minting exemptions, false-FIRE-under-stress) killed for one file edit; every fix has a fixture.**
