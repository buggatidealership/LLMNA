# 2026-07-31 (Fri) — HYPERSCALER AI-ROI CONVERSION SESSION (operator-requested 07-30, executed 07-31 post-close)

**Workflow:** MACRO-FIRST RESEARCH (#9) — Part 3 rates leg computed first (T1), Parts 1-2 agent-fed
**Scope:** GOOGL / MSFT / AMZN / META — the four the operator named
**NO POSITION ACTIONS — user-gated. But per L47 + the SYMMETRY RULE, a VIEW is mandatory and is stated in §5.**

---

## §0 — ALREADY-DONE CHECK (computed, not recalled)

Three items the Routine lists as "also due tonight" were **completed earlier today** and are NOT re-run. Verified by grep count against `predictions/lessons.md`:

| Item | Status | Where |
|---|---|---|
| **AMZN registered call, T+24h grade** | ✅ **GRADED 07-30** — direction WRONG (−7.4pp); INPUT layer; **retraction condition did NOT fire**, framework confirmed 3-for-3 | `lessons.md` "AMZN Q2 — REGISTERED CALL GRADED" |
| **MURATA Q1 print** | ✅ **GRADED 07-31 AM** — numbers HIT (rev ¥502,264m −0.54%, OP ¥98,454m in-band), **mechanism WRONG on 3 of 3 causal legs** | `lessons.md` "MURATA Q1 FY3/27 — 🟢" |
| **KIOXIA guidance** | ✅ **GRADED 07-31 AM** — pre-print INPUT failure vindicated; OP **2.12× our point** | `lessons.md` "KIOXIA Q1 FY3/27 — 🔴" |

**Note on the AMZN grade specifically:** it was graded against the **07-30 after-hours** print. The reaction ledger in §1 supersedes that with the **settled T+24h close**, which is the correct basis per the Two-Part GRADE protocol. If the settled number differs materially from the AH figure the grade used, **the grade is re-opened, not left standing.**

---

## §3 — THE RATES LEG (T1 FRED, fetched 2026-07-31) — standing requirement per the operator's 07-30 directive

**This section is placed before the company analysis deliberately.** A conversion story is by construction a long-duration cash flow — spend now, revenue later — so the discount rate is not context, it is an input to the valuation of the very thing being measured.

| Date | 2Y | 5Y | 10Y | 30Y | **2s30s** | 2s10s |
|---|---|---|---|---|---|---|
| 07-23 | 4.37 | 4.46 | 4.71 | 5.17 | 80bp | 34bp |
| 07-24 | 4.33 | 4.43 | 4.69 | 5.16 | 83bp | 36bp |
| 07-27 | 4.31 | 4.40 | 4.65 | 5.12 | 81bp | 34bp |
| 07-28 | 4.26 | 4.35 | 4.61 | 5.09 | 83bp | 35bp |
| **07-29** | **4.22** | 4.37 | **4.67** | **5.20** | **98bp** | **45bp** |
| **07-30** | **4.23** | 4.38 | **4.68** | **5.21** | **98bp** | **45bp** |

**FOMC-window move (07-28 → 07-30):** 2Y **−3bp**, 5Y +3bp, 10Y **+7bp**, 30Y **+12bp** → **2s30s 83bp → 98bp = +15bp of steepening, and it HELD on 07-30.** The long end did **15×** the front-end move (computed). Front-end down, long-end up simultaneously = the reaction-function repricing established in addendum #14, not an inflation-expectations shock.

### §3.1 — T1 upgrades to figures we previously carried at T3

Fetching FRED directly resolved four items the 07-31 morning verifier could not:

| Figure | Previously | **Now (T1)** |
|---|---|---|
| 30Y 07-30 | 5.21 (T3 TradingEconomics) | **5.21** ✅ confirmed |
| 10Y 07-30 | 4.66 (T3) | **4.68** — the T3 figure was **2bp wrong** |
| 2Y 07-30 | *"NOT CONFIRMED — 2s30s not computable"* | **4.23** |
| 5Y, any date in window | *"NOT CONFIRMED"* | **4.38** (07-30) |

**⇒ 2s30s for 07-30 IS computable and is 98bp.** The morning verifier's data gap was a routing limitation, not an absence — worth noting because it means "unobtainable" claims from agents should be re-tested against a direct API before being carried as gaps.

### §3.2 — 🔑 What this does to a conversion story, computed

A conversion story pays out years after the spend. Discounting a 20-year-out dollar:

| Discount rate | PV of $1 in 10y | PV of $1 in 20y |
|---|---|---|
| 3.00% | $0.744 | $0.554 |
| **4.68%** (10Y) | $0.633 | $0.401 |
| **5.21%** (30Y) | $0.602 | **$0.362** |

**Moving the discount rate from 3.00% to 5.21% destroys 34.6% of the present value of a 20-year-out dollar** — with nothing whatsoever changing about the business.

**⇒ The rates leg hits BOTH sides of the AI-ROI trade simultaneously:**
1. **Discount side** — it devalues the future conversion the instrument is built to detect.
2. **Funding side** — it raises the cost of the capex being converted (Meta's 40-year paper at ~7%).

**This is why the conversion instrument cannot be read in isolation.** A company whose conversion rate improves by less than the discount-rate drag has, in economic terms, gone backwards while looking like it improved. **Any ranking in §2 that ignores this is measuring the wrong thing** — and that is the specific tie-in the operator's standing rates directive exists to force.

---

## §1 — THE REACTION LEDGER (T1, three-vendor agreement to the cent)

**Reusable instrument shipped:** `meta/tools/earnings_reaction_ledger.py` — parameterised on a `CYCLE` dict, so next quarter you edit the dict, not the code.

Fetch stamps: Finnhub `/quote` **2026-07-31T20:37:21Z** (all five carry exchange ts 20:00:00Z = the 16:00 ET settle) · FMP EOD 20:37:52Z · EODHD EOD 20:40:47Z (rows ≤ T-1 only — same-day row deliberately not read per the documented defect). **0 disagreement rows across 25 OHLC cells.**

| | Print | Base (prior reg. close) | AH reaction | **T+24h settled** | T+48h | **Divergence (raw)** | **Cohort-adjusted** |
|---|---|---|---|---|---|---|---|
| **GOOGL** | 07-22 AMC | $342.09 | −4.90% (range −4.9 to −7.0) | **−7.13%** | −6.53% | −2.23pp | **+0.64pp** ⚠️ circular control |
| **MSFT** | 07-29 AMC | $390.54 | +8.88% | **+15.51%** | +18.99% | +6.63pp | **+6.10pp** ✅ survives |
| **META** | 07-29 AMC | $585.61 | −7.45% | **−7.95%** | −4.94% | −0.50pp | −1.03pp |
| **AMZN** | 07-30 AMC | $235.50 (pre-print) | **+7.41% to +10% — unresolvable** | **+15.32%** | n/a (Fri) | +7.91pp | **+1.18pp** |
| **AAPL** | 07-30 AMC | $333.43 | −6.0% to −7.8% — unresolvable | **−7.35%** | n/a (Fri) | −0.35pp | **−7.09pp** 🔑 |

### §1.1 — 🔴 The headline finding: the "AH under-reacts" pattern is an ARTIFACT

Raw, it looks like a regularity: **|T+24h| > |AH| in all five**, mean **+2.29pp**. **Under a cohort control** (same-session close-to-close of names not reacting to their own print) the mean collapses to **−0.04pp**. **AMZN's +7.91pp raw divergence is ~85% market beta** — GOOGL rose +6.73% the same session on no news of its own.

**SIGN TEST: 0 of 5** had AH and T+24h of opposite sign. **After-hours direction was 5-for-5 correct.** So "AH is pure flow" is **false** here. The correct statement: **direction informative, magnitude not.**

**AAPL is the trap** — raw −0.35pp reads as "AH got it right"; cohort-adjusted **−7.09pp** makes it the most misleading knee-jerk of the five. Only visible once the tape is removed.

**Only MSFT survives the control**, and the mechanism is already on file: decade-high short interest into the print ⇒ **squeeze, not re-rating** ⇒ a *positioning* signal, not an *information* signal.

⚠️ **n=5, one cycle, two strong up-tapes. NOT tradeable on this evidence.**

### §1.2 — 🔴 FOUR corpus figures were intraday ticks, now corrected in place

Forensic test: convert the disputed % to an implied price, check against the session range. **MSFT +16.77%** → $456.03, **$4.93 above the $451.10 settle**. **META −8.73%** → $534.49 and **−10%** → $527.05, both inside range, the latter **$11.98 off**. **GOOGL −6.5%/−7.00%** → both intraday; true **−7.13%**. Corrected in `2026-07-30-thu-earnings-reward-function-map.md`, `2026-07-31-ai-complex-deleveraging-size-tested.md` and `meta/hyperscaler-reward-function-v2.md`, old values retained inline. **L42-b booked.**

**🔴 And the worse half — a Rule #10 CASCADE FAILURE:** the GOOGL figure **had already been corrected once**, on 07-25 in `companies/GOOG/thesis.md`. The stale values survived in the reward-function map five days later and **propagated into v2 today**. **A correction that does not cascade is not a correction.**

### §1.3 — 🔴 AMZN GRADE RE-OPENED (the §0 caveat fired)

Settled **+15.32%** vs the AH **+7.41%** the 07-30 grade used ⇒ **the miss is 2.07× larger on the correct basis.** And the gate was mis-specified: the call required **BOTH** AWS ≥32% **AND** capex ≤~$200bn; **AWS 37% ✅ but capex $220bn ❌ (RAISED)** — only one leg held and the stock rose 15.32% anyway. **A conjunctive gate half-satisfied should have produced a DOWN move on the call's own logic.** Full re-grade in `predictions/lessons.md`.

## §2 — THE ROI-CONVERSION INSTRUMENT

*[agent in flight — time series lands on return]*

## §4 — CROSS-CHECK vs THE REWARD-FUNCTION MAP

*[pending §1-§2]*

## §5 — THE VIEW (mandatory per L47 + SYMMETRY RULE — no neutrality permitted)

*[pending §1-§2]*
