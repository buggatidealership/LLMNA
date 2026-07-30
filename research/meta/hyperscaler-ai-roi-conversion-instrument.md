# The AI-ROI Conversion Instrument — spec (operator-originated 2026-07-30)

**Origin (operator, verbatim-adjacent):** *"what are the revenue shifting? Where are they getting most of the revenue from? Is the AI spending, their CapEx, paying out? And which companies are showing directional signs of that being the case, and which ones don't? ...it was one in ten first, and then let's say four tenths, and all of a sudden it's gonna break even, and then you reallocate — the AI spending is actually working out for those companies. I think that's a trend you wanna be early on."*

**The thesis in one line:** AI capex ROI is a TRAJECTORY, not a state — it moves 1/10 → 4/10 → break-even → positive, and the alpha is in identifying WHICH large-cap crosses the inflection BEFORE the market prices it.

## Why this is worth building (and why it is not the same as the reward-function map)
The reward-function map (`signals/cross-source-log/2026-07-30-thu-earnings-reward-function-map.md`) measures **how the market is pricing** capex today — a sentiment/flow instrument, and today's tape proved it flips violently. This instrument measures **whether the capex is actually working** — a fundamentals instrument that should move slowly and monotonically. **The two disagreeing is the setup: the alpha is where conversion is improving while the market is still punishing the payer.** That is precisely the state MSFT was in before 07-29 (RPO $678B +84% while capex got punished) and the state the operator wants found EARLY, not after an 8.9% AH move.

## The metric stack (per company, ≥4-6 quarters of history, all computed not narrated)
| Field | Why it matters | Source |
|---|---|---|
| Capex incl. finance leases, quarterly | The denominator. Must include leases — MSFT's 07-29 reclass proved headline capex is manipulable | 10-Q/10-K cash-flow + lease notes |
| **AI-attributable revenue line** | Azure / Google Cloud / AWS. **META HAS NONE — that absence is the finding, not a data gap** | Segment disclosure |
| **CONVERSION RATE = Δ AI-attributable revenue ÷ Δ capex, QoQ** | **The core metric. This is the "1/10 → 4/10" the operator described, made computable** | Computed |
| Backlog / RPO | Forward conversion proxy; MSFT's $678B +84% is the template. **Beware: management will optimise disclosure toward this metric now that the market rewards it** (booked 2nd-order read) | Disclosure |
| D&A as % of revenue + trajectory | The cost side arriving on a lag. MSFT FY26 depreciation +55.9% vs revenue +17.8% = **3.14×** (computed 07-30). Sector: **$549B of 2026 spend, 72.2%, not yet expensed** | XBRL |
| Capex / OCF cover | Already computed 07-30: **MSFT 74.0% · META 97.6% · GOOGL 115.0% · AMZN 169.8% Q1 / 101.7% TTM** | XBRL |
| Useful-life changes | Contaminates comparability. MSFT extended buildings 15→25yr; META servers 5.0→5.5yr; AMZN went the OTHER way 6→5yr | Notes |

## Output required
1. Per-company conversion-rate time series, **ranked by TRAJECTORY (improving / flat / deteriorating)**, not by level.
2. Explicit call on **who is closest to the inflection** and who shows **no directional evidence** — stated as a view, per L47/SYMMETRY RULE.
3. The **reaction ledger** alongside it: AH reaction vs T+24h reaction per print. **The gap between the knee-jerk and the settled read is itself a signal** (knee-jerk = flow, T+24h = considered judgment).
4. Rates leg carried explicitly (standing operator instruction 07-30): term-premium repricing raises both the discount rate on these long-duration conversion stories AND the funding cost of the capex generating them.

## Falsifiers for the instrument itself
- If the conversion rate is uncomputable for ≥2 of the 4 because segment disclosure is too coarse → the instrument is decorative; replace with backlog/RPO trajectory alone and say so.
- If conversion-rate ranking shows NO relationship to subsequent 2-quarter relative performance → it is an accounting curiosity, not an edge. **Test it retrospectively before trusting it forward.**
- If every company's ratio improves monotonically (because revenue grows and capex is lumpy), the metric is mechanically confounded → switch to a trailing-4-quarter smoothed basis.

**Cadence:** quarterly at the earnings cluster; first full build scheduled 2026-07-31 evening (reminder set, trigger registered). **NO POSITION ACTION — user-gated; the VIEW is required regardless (L47).**

## FIRST DATA POINT — AMZN Q2 2026 (computed 2026-07-30, T1 8-K)
| Framing | Computation | Result |
|---|---|---|
| **QoQ conversion rate** | ΔAWS rev (42.232−37.587 = +$4.645B) ÷ Δcapex (54.208−44.203 = +$10.005B) | **46.4%** |
| Annualized-incremental framing | 4 × YoY AWS rev delta ($45.4B) ÷ TTM capex ($169.0B) | **26.9%** |
**Read: this is literally the operator's "four tenths."** AWS is converting ~46 cents of incremental quarterly revenue per incremental dollar of quarterly capex — and doing it while the AWS operating margin EXPANDED 37.7% → 39.4%, which is the part that matters: conversion improving *with* margin expansion is the inflection signature, not conversion bought by discounting.
**Caveat (honest):** total capex serves retail + logistics + AWS, so the AWS-only numerator against total-capex denominator UNDERSTATES AWS's true conversion — treat both figures as a directional FLOOR, and split by segment capex at the 10-Q if disclosed.
**Instrument status: LIVE, N=1.** Needs MSFT/GOOGL/META on the same basis + ≥4 quarters of history before any ranking is trustworthy — scheduled 07-31 evening.

## SPEND-B DENOMINATOR INPUTS (added 2026-07-30 EVE — back-ref: `signals/cross-source-log/2026-07-30-thu-two-spend-framework-token-economics-premise-inversion.md`)

The two-spend build supplies two inputs this instrument was missing — a **sector-level denominator** to sanity-check per-company conversion against, and a **leading indicator** that moves before any 10-Q does.

**Sector-level context for any single-company conversion rate:**
- Spend-B (token/AI revenue) growing **~2.20×/yr** (realized blended price −3.03×/yr × volume +6.67×/yr), triangulated within 1.4% against MSFT $37B +123% (2.23×) and AWS >$25B (~2.15×)
- Spend-B $110-135B vs hyperscaler **depreciation** $202-228B = **~50% coverage** (capex is the wrong denominator — depreciation is the annual P&L charge revenue must beat)
- ⇒ **Any company printing conversion materially above ~50%-of-depreciation is outperforming the sector aggregate**, not just growing. AMZN's 46.4% QoQ sits right at that line, which reframes it from "good" to "sector-typical" — a useful deflation of the first data point.

**Two indicators folded in as instrument inputs (from §7 of the artifact):**
| # | Input | Bullish | Bearish | Role here |
|---|---|---|---|---|
| **2** | **Committed-consumption backlog YoY** (Google Cloud is the cleanest discloser: **$106B → $514B, 4.85×**) | ≥2.5× | **<2.0×** | Backlog is the *forward* conversion the ratio only sees in arrears — leads the instrument by 2-4 quarters |
| **3** | **Artificial Analysis cost-per-task** | falling | flat/rising | Separates genuine efficiency gains from mix-shift; without it, an improving conversion ratio can be pure model-tier downgrade rather than real ROI |

**⚠️ Instrument-level caveat this adds:** conversion rates computed while frontier ASP is *flat* (the premise inversion — Opus $5/$25 unchanged 8 months, GPT flagship output $10→$30) are not comparable to conversion rates computed after any frontier list-price cut. **A frontier price cut is a structural break in this instrument's time series**, not just a datapoint — re-base the history if one prints.
