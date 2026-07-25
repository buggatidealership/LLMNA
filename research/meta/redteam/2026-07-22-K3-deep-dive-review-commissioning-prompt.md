# 2026-07-22 — K3 commissioning prompt: cross-family review of the 2026-07-21 harness deep dive

**Status: SENT-PENDING (user pastes to Kimi K3; K3's reply gets adjudicated into `meta/redteam/` per house convention — see the 2026-07-20 K3-swarm precedent). Prompt text below is the verbatim commission.**

---

You are Kimi K3, acting as the external cross-family adversarial reviewer for the LLMNA research OS (GitHub repo: `buggatidealership/LLMNA`, branch `main`). You have reviewed this harness before — your 2026-07-20 spec-vs-reality swarm review is adjudicated at `research/meta/redteam/2026-07-20-K3-swarm-spec-vs-reality-adjudication.md`. Today's commission: independently review the 2026-07-21 harness deep dive and the self-patches that followed it.

## What happened (context you should verify, not trust)

- On 2026-07-21 the resident model (Claude, Fable-5 tier) ran a 337-agent orchestrated workflow over the harness's enforcement layer (19 Claude-Code hooks + 3 git-level hooks + supporting metric/telemetry scripts). It inventoried **362 distinct mechanics** (variable/function/branch-level behaviors) and classified each into four classes: **MATCH** (implementation matches documented spec), **DEFECT** (implementation wrong vs spec), **GAP** (spec or coverage hole), **UPGRADE** (improvement opportunity). Reported counts: **201 MATCH / 83 DEFECT / 72 GAP / 6 UPGRADE**; adversarial verify pass 167 confirmed / 2 refuted; severity floor **0 BLOCKING / 8 HIGH**; 131 patches designed.
- The same night, **5 of the 8 HIGH were self-patched "probe-gated"**: write a probe proving the hole open → patch → probe proves the hole closed AND benign controls still pass → atomic commit + durable test fixture. The remaining 3 HIGH + ~150 MEDIUM/LOW were deferred to a reviewed slot on 2026-07-24.
- Method note the house itself logged: per external benchmark the resident model is the *weaker code-reviewer* (its strength is long agentic execution), so verification leaned on objective probes rather than self-review. Cross-family review — you — is the deliberately-added second leg of that discipline. Your disagreement is the product being purchased.

## Files to read (in order)

1. `research/meta/redteam/2026-07-21-harness-deep-dive-adjudication.md` — summary, applied-patch table, deferrals, new FPs found while patching.
2. `research/meta/redteam/2026-07-21-harness-deep-dive-RAW-journal-extract.json` — all 362 mechanic records + 131 patch designs (large; this is the primary evidence base).
3. The patched files at HEAD: `research/meta/hooks/git-guard-pretooluse.py`, `research/meta/hooks/structural-output-hook.py`, `research/meta/hooks/session-start-hook.py`, `research/meta/structural-output-metric.py`.
4. The probe fixtures: `research/meta/tests/test_git_guard_bypass_probes.py`, `research/meta/tests/test_git_guard_adjacency_fp.py`, `research/meta/tests/test_structural_output_tier_gate.py`.
5. Commits of record (if you have clone/history access): `f25a66f`, `0729b21`, `e04eaef`, `b6ad6d6`, `f19663d`.

## Commission — five questions, answer each separately

**Q1 — CLASSIFICATION AUDIT.** Sample ≥20 mechanics from the RAW extract across all four classes (state which IDs you sampled) and re-derive each classification from the actual code at HEAD. Report agree/disagree per item and an estimated misclassification rate per class. Hunt specifically for DEFECTs mislabeled as MATCH — that is the dangerous direction (a hole recorded as healthy).

**Q2 — SEVERITY AUDIT.** The run reported 0 BLOCKING / 8 HIGH. Adversarially test that floor: is any of the 83 DEFECTs or 72 GAPs actually BLOCKING/HIGH but graded lower? Name the top 5 you would re-grade, each with a concrete exploit or failure path.

**Q3 — PATCH REVIEW.** For each of the 5 applied HIGH patches: is it correct, complete, and minimal? Do the probe fixtures actually pin the hole shut — can you construct an input that PASSES the fixture but re-opens the hole? Bypass attempts are explicitly welcome; a working bypass is the highest-value finding this commission can produce.

**Q4 — DEFERRAL CHALLENGE.** Three HIGH items were deferred to 2026-07-24 (G-28 structural-output-metric numerator reclassification — must land before the 08-06 experiment decision; G-19 session-prime-cascade changeset window; a docs gap). Was deferring safe? State concretely what can break or silently mis-measure between now and 07-24/08-06 if they stay unfixed.

**Q5 — BLIND-SPOT SWEEP.** What did a 337-agent inventory of the harness STILL miss? Look for whole categories absent from the extract rather than item-level nits — e.g., concurrency/ordering behavior between hooks firing on the same event, failure modes of the telemetry layer itself (hook-fire-log as a single point of self-knowledge), the platform-trigger/Routine layer, secrets handling in probes/fixtures, anything structural.

## Output format

Markdown. Per-question numbered findings with `file:line` references. Tag every finding **CONFIRM / REFUTE / RE-GRADE / NEW** plus a severity. Findings without a concrete reproduction path or code reference must be labeled **SPECULATIVE**. End with a ≤10-line overall verdict including a binary call: do you certify the 5 self-patches as review-grade, or demand rework (name which)? Do not soften anything — agreement without inspection is worthless to this process.

## PS — separate small ask

The house day-state references a "pre-locked 6-item rubric" you authored ~2026-07-18 for grading the Jul-22 IBM/NOW earnings registrations. That rubric text was never persisted into the repo (found today as a dead reference). Please re-send it verbatim at the top of your reply so it can be committed and applied retroactively.

**Fallback:** if you cannot fetch the repo, say so explicitly and list which of the numbered files you need pasted — do not review from memory of prior engagements.

---

**Position implication: NO ACTION (harness-meta commissioning artifact).**
