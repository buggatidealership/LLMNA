# 2026-07-22 — K3 CROSS-FAMILY INDEPENDENCE: degrade on the Moonshot-distillation accusation

**Origin:** user-shared AI brief (Jul-22) → Rule #16 verification (`2026-07-22-wed-eve-ai-brief-2day-ingest-jul21-22.md` IN-FLIGHT #1). White House (Kratsios, OSTP, Jul-22 X post) + Treasury (Bessent, Jul-21 Fox Business, conditional) accuse Moonshot of "large-scale covert industrial distillation" of Anthropic's **Claude Fable 5** ("Fable", T1-confirmed Anthropic model, GA ~Jul-1-2026) to build **Kimi K3** — the exact model this harness uses as its cross-family adversarial-review oracle. Assertion of intelligence, NOT published proof. Distillation root is RECYCLED (Anthropic's Feb-2026 charge: ~16M exchanges / ~24k fraudulent accounts, Moonshot ~3.4M ≈ 21%); the Jul-21/22 political escalation is the fresh jacket.

## The assumption at risk
The harness uses K3 as an adversarial reviewer of Claude-authored code/self-assessments BECAUSE it is presumed a different lineage carrying INDEPENDENT blind spots (cross-family review + reproduce-don't-trust gate = the "who audits the auditor" answer). Tonight's K3 merge-gate commission for the accounting-layer rework leans on exactly this.

## The layer-mapping argument (why this bites at the load-bearing joint) — (my model, T2-suggestive evidence)
- **Pretraining = where lineage independence lives.** Evidence (Greenblatt, Redwood) says K3's PRETRAIN is its OWN — ~8-10 months behind Anthropic, different architecture (MoE + linear attention). **GOOD for independence.**
- **Distillation bites hardest at POST-TRAINING** — instruction-following, reasoning style, what the model flags/refuses, formatting, "taste." That is PRECISELY the layer that governs code-review behavior. If K3's post-training imitated Claude/Fable outputs, K3's review JUDGMENTS would correlate with Claude's → **shared blind spots imported into the exact function we rely on it for.** The accusation, if even partly true, attacks the independence claim at its most load-bearing joint.
- **But the high bar is unmet:** accusation-exists (confirmed) ≠ distillation-established (unproven; self-ID has innocent explanations — training-data contamination, Claude transcripts in public data, roleplay leakage; the strongest analysis used an Anthropic model as judge). Further gap: "post-training touched some Claude data" ≠ "K3 inherits Claude's blind spots wholesale" (distillation is partial/diluted; K3 keeps independent pretrain + Chinese-corpus grounding + its own RLHF prefs).

## The load-bearing operational insight — DISAGREEMENT-ASYMMETRY + the reproduce-gate already protects us
The exposure is NOT symmetric across K3's two review functions:
- **K3 FINDS A HOLE (disagreement with Claude):** signal PRESERVED. A shared blind spot cannot manufacture a *false* find — if K3 surfaces a hole, the hole is real (and we reproduce it by execution anyway). All past K3 value (git-guard bypasses, exit-126, PI-casing — every one reproduced by me before acceptance) stands: **it was never K3's authority we trusted, it was the reproducible fact.** The reproduce-don't-trust gate already insulates the finding side completely.
- **K3 SAYS "SAFE/CLEAN" (agreement with Claude):** assurance DEGRADED. A K3 "no holes / safe to merge" verdict can now be explained by *shared* blind spots rather than genuine correctness → weaker independent clearance than assumed. This is a FALSE-NEGATIVE risk (K3 misses the same thing Claude misses) — exactly the correctness-blindness the gate exists to catch.

**Net (my model, wide band — judgment on an unproven allegation, T2-suggestive):** degrade K3 cross-family independence from **HIGH → MODERATE**, concentrated on stylistic/behavioral (post-training) overlap, not deep reasoning-architecture (pretrain) overlap. Discount the *agreement*-as-independent-confirmation bonus by **~⅓ to ½**; keep the *disagreement*/hole-finding signal at ~full weight. Do NOT overcorrect to "compromised/useless" — different pretrain + data + architecture still buy real orthogonality; and B63 (lab-favorable source: the accuser is the US govt + an Anthropic-model-assisted analysis) + political-decoupling motive are live confounds.

## Operating adjustments (effective now)
1. **K3 merge-gate commission (drafted tonight) — annotated, NOT rescinded.** Still run it: its job is to FIND holes (disagreement-preserved). But a K3 "SAFE-to-merge" verdict is **necessary-not-sufficient** — keep the mechanical-reproduction pre-screen, and treat K3-clearance as one input, not the clearance. A HIGH destructive action (merging LIVE enforcement) already needs operator approval (Rule #19) — that gate stands.
2. **Weight K3 by disagreement, not agreement**, in all future cross-family use.
3. **The independence of the review oracle is a VARIABLE, not a constant** — provenance must be periodically re-verified, not assumed once. (Lesson candidate — see below.)

## Re-eval / falsifier
- **~Jul-27-2026: K3 full weights go public** → converts this from T2-suggestive toward T1-testable (weight-level distillation forensics). Re-run this adjudication then; if distillation is established at the post-training layer, deepen the agreement-discount toward the top of the band and consider sourcing a genuinely third oracle (non-Claude, non-K3) for merge-gate clearance. If refuted, restore independence toward HIGH.
- Falsifier for the degrade: weight forensics show K3 post-training is NOT Claude-derived → the accusation was decoupling politics → revert.

## Cascade
- `2026-07-22-wed-eve-ai-brief-2day-ingest-jul21-22.md` IN-FLIGHT #1 → resolved.
- `2026-07-22-accounting-layer-REWORK-K3-merge-gate-commission.md` → independence caveat appended.
- `meta/biases-watchlist.md` B64 (model-affinity) → amendment: the review-ORACLE's own lineage-independence is itself affinity-exposed and must be re-verified, not assumed.
- Lesson candidate (L42?): "a cross-family oracle's independence is a re-verifiable variable; the reproduce-don't-trust gate protects the finding side but not the clearance side — weight oracles by disagreement, discount agreement."

**Position implication: ⚪ NO ACTION (harness-meta, not market). The market angle — US-China AI sanctions/export-control escalation (GB300-in-Thailand + Treasury sanction authority) — feeds the decoupling macro cluster + the China-foreign-fab-ban WATCH from the same brief; not a book input tonight.**

---

## ADDENDUM (2026-07-22 EVE) — the deeper input (Principle #49 application): clearance-by-coverage, not oracle-authority
User invoked #49 ("find the input I'm trying to compute, don't take my words literally") on the request to write a K3 verification probe. The input being computed is NOT "is K3 clean?" but **`review_integrity_dependence_on_oracle_independence` — and whether it can be driven to zero.**

**The computation (decomposition of where the dependency lives):**
- K3 **FINDS a hole** (disagreement): ~0 dependence on K3's independence — every hole is reproduced by execution; a shared blind spot can't manufacture a false find. Integrity here = the reproduce-gate, not the oracle.
- K3 **CLEARS it** ("SAFE" = agreement): this is the ENTIRE exposure — a "no more holes" claim is an ABSENCE, unreproducible, so you're forced to trust the sign-off's independence.

**The move — delete the exposure architecturally:** stop certifying "safe because an independent mind signed off." Certify **"safe because these N enumerated attack classes were each EXECUTED and observed BLOCKED, and the attack set was adversarially expanded by ≥2 diverse minds until it went dry."** Consequences: (1) the oracle's only load-bearing job becomes EXPANDING the attack set (the finding function, already immunized by reproduction); (2) no oracle's SAFE verdict is ever load-bearing — "safe" becomes a coverage FACT, not an authority CLAIM; (3) the distillation accusation stops mattering to what we do — a compromised K3 just fails to expand coverage on shared-blind-spot classes (a gap detected by a second diverse mind or the known-blind-spot corpus, NOT a false clearance we swallow).

**Reframe of "cross-family review":** the family boundary was never the mechanism — it was a proxy for "diverse minds expanding coverage." Coverage-until-dry across diverse minds is the real invariant; oracle lineage-purity is not. This SUPERSEDES the cross-family-review framing as the harness's answer to "who audits the auditor."

**Demotion of the behavioral probe** (`2026-07-22-K3-distillation-behavioral-probe.md`): from THE deliverable → one attack-set-expander among several (it enumerates our known blind spots as reproducible test items = exactly the coverage the new criterion needs). It no longer carries the decision.

**PENDING USER CONFIRM:** rebuild the accounting-layer merge-gate to certify on reproduced-coverage-until-dry (not K3's SAFE) + codify the coverage-not-authority principle (candidate #50). Flagged, not yet executed — awaiting the go (the user framed this as a hypothesis / "find the input," not yet a build order).
