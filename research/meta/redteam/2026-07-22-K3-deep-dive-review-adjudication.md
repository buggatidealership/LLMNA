# 2026-07-22 — K3 cross-family review of the 07-21 deep dive: ADJUDICATION

**Commission:** `2026-07-22-K3-deep-dive-review-commissioning-prompt.md`. K3 delivered a 4-agent review (23 findings), pristine-clone at ef5c07f, all flagship bypasses orchestrator-executed. **Every flagship claim independently re-reproduced HERE before adoption** (probe-gated adjudication; a claimed bypass is RUN, not believed). Probe files in scratchpad: `k3_bypass_verify.py`, `k3_pi_verify.py`.

## Rubric PS — handled correctly (B65 pass)
K3 REFUSED to re-send the 07-18 6-item rubric "verbatim," stating it exists nowhere in repo or its context and that reconstructing-and-labeling-verbatim would be the exact recall-as-receipt failure B65 codifies. Correct call — banked as an external B65 confirmation. K3 offered a FRESHLY-AUTHORED substitute, provenance-labeled "authored 2026-07-22 by K3, NOT the 07-18 original," committable only as pre-print before tonight's prints. Committed separately at `predictions/2026-07-22-K3-authored-print-grading-rubric.md` with that provenance intact. The original 07-18 rubric is now formally a LOST ARTIFACT (dead reference retired; if the user surfaces the transcript later it can be reconciled).

## Independent reproduction of K3's flagship claims (all CONFIRMED)

| # | K3 claim | My reproduction | Verdict |
|---|---|---|---|
| Q3-1 | `git commit -m "x" -n` → exit 0 (tempered matcher scans only pre-message flags; git honors `-n` anywhere) | ran: exit **0** | **CONFIRMED HOLE** — regression from MY OWN 07-21 adjacency-tightening (I narrowed the `-n` catch to the pre-`-m` region; `-m "x" -n` defeats it) |
| Q3-2a | `rm -rf ~/LLMNA/` (trailing slash) → exit 0 | ran: exit **0** | **CONFIRMED HOLE** — one trailing slash defeats the f25a66f boundary |
| Q3-2b | `rm -rf ~/` → exit 0 | ran: exit **0** | **CONFIRMED HOLE** |
| Q3-2c | `rm -rf $HOME/LLMNA` → exit 0 | ran: exit **0** | **CONFIRMED HOLE** |
| Q3-2d | slash-less `rm -rf ~/LLMNA` correctly blocks | ran: exit **2** | **CONFIRMED (blocks)** — the patched form works; only the variants above escape |
| Q3-3 | PI matcher case-brittle — lowercase `position implication:` reopens G-27 | code: line 171 regex has NO `re.IGNORECASE` | **CONFIRMED HOLE** (code inspection; my inline probe was schema-invalid — see below) |
| Q3-4 | tier-gate fixture red twice (hardcoded path + case 4 born-red) | ran: `1 MISMATCH` (case 4 got=2 exp=0); line 4 hardcodes `/home/user/LLMNA` | **CONFIRMED** |
| Q3-5 | e04eaef inverted design-130 ref priority (local-main-first vs origin/main-first); ref choice swings week rate 0.196→0.452 | code: line 45 `for cand in ("main","origin/main")` = local-first | **CONFIRMED (code state)**; correctness = 08-06 judgment |

**Self-demonstration of K3's Q5 blind spot (schema drift):** my first PI probe fed `{"messages":[...]}` inline; the hook reads a `transcript_path` FILE (line 186), so it exited 0 on ALL inputs incl. canonical caps — a false "all-pass." Caught by cross-checking against the tier-gate fixture (which builds a real transcript and shows canonical-untiered PI DOES block). This is exactly K3's "stdin-schema drift = invisible enforcement death" finding, reproduced accidentally on myself. Booked.

## Severity re-grades ACCEPTED (from K3's Q2, verified)
- **G-28 (structural-output-metric contaminated numerator) → BLOCKING** under our own 07-20 precedent; still accruing (K3 logged 2 new tier-fires 07-21 21:53/54). Must land before 08-06. The b6ad6d6 size-gate reorder is an *accelerant* (more tier-fires → more numerator poison) — a real second-order cost of last night's G-27 fix.
- **git-guard deletion-class + commit-`-n` + PI-casing → HIGH**, live mechanisms confirmed above.
- **G-19 deferral rationale REFUTED**: "masked by one-commit-per-Stop" is false — the main session itself did 6 commits in ~10 min on 07-21 (K3 verified; consistent with this session's own multi-commit turns). The changeset-window hole is real, not masked.

## Verdict on the 5 self-patches (independent; aligns with K3's REWORK-2/CERTIFY-2-one-conditional)
| Patch | Verdict | Why |
|---|---|---|
| f25a66f git-guard (rm + commit-n) | **REWORK** | 4 boundary bypasses confirmed live |
| e04eaef metric ref-resolution | **REWORK (pre-08-06 hard deadline)** | ref-order swings the adjudicator denominator materially |
| structural-output G-27 size-gate reorder | **CONDITIONAL** | reorder works for canonical casing; underlying PI matcher case-brittle → harden to `re.IGNORECASE` |
| test_structural_output_tier_gate fixture | **REWORK** | red (case 4) + hardcoded path |
| f19663d session-start stale-tier 7→83 | **CERTIFY** | K3 confirmed clean on the real corpus; my 07-21 computed 7→83 stands |

## Routing (all to the 2026-07-24 slot; the 4 hardening fixes now have K3's EXTERNAL payloads as an independent probe oracle — the same-model-blindness that justified probe-gating is removed for these)
1. git-guard: `-n` anywhere-after-commit (not just pre-`-m`); rm boundary = REPO_TOKENS on the tilde/HOME/trailing-slash forms; re-probe on K3's exact 4 strings + the 3 prior FP controls.
2. structural-output PI matcher → `re.IGNORECASE` (+ the 6 K3 spellings as fixtures).
3. tier-gate fixture → `CLAUDE_PROJECT_DIR`-relative path + fix case-4 expectation (adjudicate whether long+H1/H2 should pass the size gate — it should; the fixture's exp=0 is right and the hook over-fires, OR the hook is right and the fixture is wrong — resolve at fix time).
4. e04eaef ref-order → adjudicate design-130 intent (origin/main-first for session containers) BEFORE 08-06; the numerator reclassification (G-28) lands same session.
5. G-28 → BLOCKING queue-top; b6ad6d6-accelerant + probe-pollution second channel both in scope.
6. New from K3 (Q5, booked): one enforcement-free Stop after every block (blanket `stop_hook_active` guard on parallel hooks incl. the commit+push gate); stdin-schema drift as an invisible-death class; 337-agent journal = receipt gap.

**Position implication: NO ACTION (harness-meta). 🟢 cross-family review adopted, every flagship claim independently reproduced; 🔴 2 self-patches REWORK + G-28 re-graded BLOCKING (pre-08-06); 🟡 the arc's-law lesson holds a second time — same-model probes pin holes as imagined, miss holes as spelled — and the fix is now oracle-backed (K3's payloads). Weaker-reviewer discipline vindicated: the review bought exactly what solo probe-gating could not.**
