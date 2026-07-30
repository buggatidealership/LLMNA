# 2026-07-30 THU — THE EARNINGS REWARD-FUNCTION MAP (operator brain-dump → mental model request)

**WORKFLOW: INGEST + MACRO-FIRST (#9).** Operator ask, extracted from a brain-dump: not an earnings recap — a **mental model of what this market rewards and punishes**, built from the Tue/Wed AMC print set, with the SK Hynix paradox (verified-strong demand, third down day) as the test case the model must explain. Four Opus agents in flight: (A) full Tue+Wed AMC print set + tonight's calendar; (B) analyst reward-function/positioning research; (C) live price action + tonight's setup; (D) hyperscaler capex aggregate + cash-cover + memory pass-through.

**NO POSITION ACTION — user-gated.**

## §1 COMPUTED PATTERN from corpus-booked figures (pre-agent, T1/T1-adjacent inputs)

| Name | Rev surprise | EPS surprise | Reaction | capex/OCF | Note |
|---|---|---|---|---|---|
| MSFT | +0.71% | +9.53% | **+8.88%** (AH) | n/a (OCF not yet booked) | Azure +43% vs cons 40.2%; RPO $678B +84% |
| META | −0.93% | −16.03% | **−7.45%** (AH) | **0.976** | capex $31.08B / OCF $31.86B; FCF $784M |
| GOOGL (07-22) | n/a | n/a | ~−6.5% | **>1.0 (negative cover)** | capex $44.9B, **FCF −$5.9B first negative quarter**; Cloud +82% |
| SKHY (07-29) | −5.64% | −5.53% (OP) | **−9.61%**, then −6.28% | n/a | OPM 76% record; capex RAISED to ₩40조 후반 |
| KLAC | n/a | n/a | **−10.80%** | n/a | **on a RAISED guide** |
| STX | n/a | n/a | +2.29% | n/a | HDD beat — only memory-adjacent gainer |
| INTC (07-24) | n/a | n/a | +13% AH | n/a | DCAI +59%, guide up |

**Computed (this session, python):** META capex/OCF = 31.08/31.86 = **0.976 → 97.6% of operating cash consumed by capex**. GOOGL: capex exceeded OCF entirely (FCF −$5.9B).
**The diagnostic asymmetry (computed):** META missed EPS by −16.03% and fell −7.45%; SKHY missed OP by −5.53% and fell −9.61%. **Miss magnitude does NOT rank the punishment** — the ranking variable is something other than the print.

## §2 HYPOTHESIS UNDER TEST (my model, pre-agent-verification — falsifiers stated)
**The regime switched from pricing AI EXPOSURE to pricing AI CASH CONVERSION**, which splits the complex into three tiers with different reward rules:
1. **MONETIZERS** (cloud/platform w/ a visible revenue line): rewarded only if attach is visible AND capex is cash-covered. Evidence: MSFT +8.88% vs GOOGL −6.5% — same demand direction, opposite outcome, differing on FCF cover.
2. **SPENDERS** (capex without attached revenue): punished regardless of demand narrative. Evidence: META (97.6% of OCF consumed, FCF $784M).
3. **SUPPLIERS** (the cost input inside everyone else's capex): punished *when the market questions capex*, because their own fundamentals are a lagging report of the buyer's spending decision. Evidence: SKHY on record margins; KLAC on a raised guide.
**Why SKHY specifically carries three de-rating channels its earnings cannot fix (my model):** (a) its revenue IS hyperscaler capex → it is re-rated on the buyer's discipline, not its own results; (b) **Warsh 07-29 put memory-chip prices inside the FOMC's inflation question set** (T1 transcript, booked 07-30 wake) → memory-price strength now feeds a rates headwind, i.e. the upcycle is partly self-limiting in this regime; (c) CXMT/China-DUV caps the cycle's DURATION, which is what a multiple pays for.
**Falsifiers for the hypothesis:** (i) AMZN tonight prints rising capex WITH decelerating AWS and RALLIES → cash-conversion framing dead; (ii) a supplier prints strong and rallies while hyperscaler capex is being questioned → tier-3 rule dead; (iii) analyst commentary shows the market rewarding capex-raises as growth signals → the whole switch is my artifact.
