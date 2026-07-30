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
