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

## §2 — THE ROI-CONVERSION INSTRUMENT (T1 SEC EDGAR, pulled 2026-07-31)

**Capex defined as cash PP&E + finance leases.** That choice is load-bearing: **finance leases are 21% of MSFT's FY26 capex** ($24.6bn of $140.6bn) — omitting them understates Microsoft by a fifth.

### §2.1 — 🔴 THE OPERATOR'S SPECIFIED RATIO IS AN ARTIFACT. It must be smoothed.

The raw QoQ ratio `Δ AI revenue ÷ Δ capex` is **unusable as specified**:

| | n | mean | sd | **CV** | Δcapex negative |
|---|---|---|---|---|---|
| **MSFT** | 7 | 0.074 | 1.096 | **14.72** | **2 of 7** |
| AMZN | 7 | 0.357 | 0.269 | 0.75 | 1 of 7 |
| GOOGL | 7 | 0.448 | 0.227 | 0.51 | 0 of 7 |

MSFT's mean is ~zero with a standard deviation **14.7× larger**. Mechanism: finance-lease additions swing $3.2bn → $9.1bn → $4.0bn quarter to quarter, so **Δcapex goes negative twice and flips the sign of a ratio whose numerator never does.** The −2.271 print at Q1'26 is pure division artifact (Δcapex −$1.3bn), not information.

**🔴 And the ranking INVERTS under smoothing:**

| Basis | 1st | 2nd | 3rd |
|---|---|---|---|
| Raw QoQ mean | GOOGL 0.448 | AMZN 0.357 | MSFT 0.074 |
| **T4Q smoothed LEVEL** | **MSFT 0.727** | AMZN 0.525 | GOOGL 0.483 |
| **T4Q smoothed TRAJECTORY** | **GOOGL ↑** | AMZN → | MSFT ↓ |

**MSFT goes from worst to best.** The **LEVEL** ranking is an artifact. The **TRAJECTORY** ranking is identical raw and smoothed, **and identical under a third independent construction** (revenue-growth vs capex-growth gap) that uses no ratio-of-differences at all and therefore cannot be produced by the lumpy-denominator mechanism.

**Three bans, adopted:** (a) never quote a single-quarter raw ratio; (b) **never rank companies by ratio LEVEL** — the numerators are not the same object (Microsoft Cloud includes M365/LinkedIn/Dynamics; AWS is pure infra; Google Cloud now includes TPU hardware); (c) always report the growth-gap alongside as the artifact-immune control.

### §2.2 — THE TRAJECTORY RANKING (the only form that survives)

| Rank | | Trajectory | Evidence | AI-rev growth vs capex growth (YoY) |
|---|---|---|---|---|
| **1** | **GOOGL** | **IMPROVING — the only monotone series** | T4Q 0.340→0.404→0.428→**0.483**, 4/4 rising | **+81.8% vs +102.5% — gap CLOSING fast** |
| **2** | **AMZN** | mildly improving, choppy | T4Q noisy, but AWS growth monotone 20.2→23.6→28.4→**36.8%** | +36.8% vs +65.4% — closing |
| **3** | **META** | **UNMEASURABLE** | no numerator exists | n/a |
| **4** | **MSFT** | **DETERIORATING — robust to numerator choice** | T4Q 1.098→0.759→0.812→**0.727**; cross-check on the cleaner Server-Products numerator: FY25 0.643 → FY26 **0.558**, same direction | **+27.0% vs +73.5% — gap WIDENING** |

**All three measurable LEVELS are falling** (MSFT 1.90×→1.53×, AMZN 1.00×→0.84×, GOOGL 0.67×→0.58× on TTM AI-rev ÷ TTM capex). **Nobody is at break-even on a cumulative basis. The differentiator is entirely marginal, not average** — which is exactly the operator's framing and is the reason the trajectory cut is the right one.

### §2.3 — 🔴 GOOGL's #1 RANK IS PARTLY UNEARNED

The **Q2'26 10-Q is the FIRST filing** to describe Google Cloud as generating *"product revenues primarily from the sale of TPU systems,"* and states revenue recognition **began this quarter**. **Alphabet does not disclose the amount.** An unknown slice of GOOGL's best-in-class quarter is **hardware resale, not compute conversion** — booked into the same segment line the ratio uses, **with no restatement of prior quarters**. Anyone computing a Google Cloud growth rate across that boundary — including this instrument — is comparing two different things.

### §2.4 — META: the absence IS the finding

**Meta has no sellable AI revenue line, and this is the business model, not a disclosure gap.** The other three rent compute to third parties, which produces an invoice, which produces a revenue line. Meta consumes 100% internally.

**1st order (P>90%):** the ratio is **undefined**, not unknown. **Any published "Meta AI ROI" figure is an assumption dressed as a measurement.**
**2nd order (P~70%):** the only proxy — Δ total revenue ÷ Δ capex — swings 0.959 → 1.493 → 2.155 → 0.944 because the numerator is advertising revenue driven jointly by ad load, pricing, seasonality and FX. **It measures Meta's ad market, not Meta's AI ROI. Do not use it.**
**3rd order (P~55%):** with no measurable conversion, Meta's capex justification is **necessarily narrative-dependent for the whole market**, making its multiple structurally more sentiment-sensitive than names with a backlog to point at.
**4th order (P~35%):** watch for **any new disclosed metric isolating AI contribution** — that would be a deliberate act of becoming measurable, and it would come from strength.

**What IS measurable for Meta and what it says:** capex/OCF **33.4% → 97.5%** in seven quarters; TTM FCF **$49.3bn → $37.9bn**; not-yet-commenced leases **5.31× YoY — the fastest of the four**; **$24.9bn of senior notes issued May 2026**, the first of the four to visibly debt-fund the ramp. **Meta is spending like the most aggressive of the four while being the only one that cannot show a conversion number.** 🟡

---

## §4 — CROSS-CHECK vs THE REWARD-FUNCTION MAP: 🔴 A LOAD-BEARING CLAIM IS FALSE

`2026-07-30-thu-earnings-reward-function-map.md` asserts: *"Cash-cover ranking (T1 SEC XBRL) **EXACTLY** tracks the reaction ranking."* **Tested against tonight's corrected settled reactions:**

| | reaction (settled) | quarterly cover | rank match? | **TTM cover** | rank match? |
|---|---|---|---|---|---|
| MSFT | **+15.51%** (1st) | 74.0% (1st) | ✅ | 76.8% (3rd) | ❌ |
| AMZN | **+15.32%** (2nd) | 169.8% (**4th/worst**) | ❌ | **109.7%** (4th) | ❌ |
| GOOGL | **−7.13%** (3rd) | 115.0% (3rd) | ✅ | 72.3% (2nd) | ❌ |
| META | **−7.95%** (4th) | 97.6% (2nd) | ❌ | **70.9% (1st/best)** | ❌ **inverted** |
| | | **Spearman ρ = +0.20** | | **Spearman ρ = −0.80** | |

**The claim is FALSE on both bases, and on the correct (TTM) basis the relationship is INVERTED.** META has the **best** TTM cash cover and the **worst** reaction.

**Why it looked true:** the map was built on the **intraday-tick reaction figures corrected in §1.2 tonight** and on **quarterly** cover ratios. **Quarterly cover is seasonally worthless** — AMZN's went 74.3% (Q4'25) → 175.8% (Q1'26) on nearly identical capex, a **2.37× swing from operating-cash-flow seasonality alone.** Per L42-b, cover ratios now require a basis stamp; **TTM is load-bearing, quarterly is decoration.**

**This is the third framework component to break today** (v2's binary test, the capex-cut falsifier, now the cash-cover correlation) — and all three broke the same way: **a real mechanism measured with the wrong instrument.**

### §4.1 — Corrections to figures I have been carrying

| Figure | Was | **Correct (T1)** |
|---|---|---|
| MSFT not-yet-commenced leases | "$196.6bn → $329.1bn" framed as a year | **that is ONE QUARTER (+67% QoQ)**; true YoY is **$92.7bn → $329.1bn = 3.55×** — *bigger* than I reported |
| Google Cloud backlog | "$106bn → $514bn = 4.85×" | mixes a T2 call figure with a T1 filing; like-for-like T1 = **$108.2bn → $519.5bn = 4.80×** |
| AMZN TTM capex/OCF | 101.7% | **109.7%** (Q2'26 alone 120.7%) |

---

## §5 — 🔴 THE VIEW (mandatory per L47 + SYMMETRY RULE — no neutrality permitted)

**Macro anchor (T1, this session):** 2s30s **98bp**, 30Y **5.21%**, and a 3.00%→5.21% discount-rate move destroys **34.6%** of a 20-year-out dollar (§3). Every conclusion below is stated *net of* that drag.

**THE VIEW ON THE FOUR — stated, not hedged:**

**I do not recommend buying any of the four, and the reason is specific rather than cautious.** The instrument's #1 name (GOOGL) has a rank I cannot underwrite: its best-in-class quarter contains an **undisclosed** TPU-hardware revenue slice, first recognised this quarter, with no prior-period restatement. **Ranking a company first on a number whose composition changed in the ranking quarter is not analysis.** Sizing that TPU contribution is a prerequisite, not a refinement.

**MSFT is the most interesting and the most uncomfortable.** Every conversion measure deteriorates — and the backlog says the opposite: **RPO +84% to $678bn**, leases **3.55× YoY**. Two readings, and the data genuinely cannot separate them:

- **H1 — TIMING (P≈55%, my model):** capex leads revenue by 2-6 quarters; +84% RPO with flat cloud growth is *definitionally* deferred conversion. Predicts cloud growth inflects up within 2-3 quarters.
- **H2 — OVER-BUILD (P≈35%, my model):** four straight quarters of flat 26-27% growth against capex nearly doubling is what over-building looks like from outside. Predicts a capex-guide moderation.
- **H3 — numerator contamination (P≈10%, my model):** Microsoft Cloud includes M365/LinkedIn/Dynamics, so a genuinely accelerating Azure could be masked by flat legacy. Partly supported — Azure did print **+43%**. Untestable without an Azure dollar line, which Microsoft has never disclosed.

**🔴 WHY THIS IS THE ANSWER THAT MATTERS FOR US, AND IT IS NOT ABOUT OWNING MSFT.** Microsoft is the largest capex payer in the set. **If H2 is right, the capex moderation shows up at the largest payer first — and that is the precise event the bypass-ladder work named as the one thing that breaks recipient insulation for our held memory cohort.** The four-name analysis's highest-value output is therefore not a stock pick; it is that **MSFT's cloud-growth-vs-RPO gap is the earliest available read on whether the spending that pays our names is about to moderate.**

**On the held cohort:** the recipient/payer logic **survives everything broken tonight** — it was never built on the cash-cover correlation. All four payers raised or held capex; the money still arrives. **HOLD, no size change, user-gated.** 🟡

**What I would actually do next, in priority order:** (1) size the GOOGL TPU line — without it the #1 rank is unearned; (2) resolve MSFT timing-vs-over-build, because it is our cohort's early-warning system; (3) **stop using quarterly cover ratios entirely.**

**Explicitly NOT recommended:** initiating any position in the four on this analysis. The instrument in its only valid form (trajectory) has four observations per name, one contaminated numerator, one undefined numerator, and a discount rate moving against all of them. **That is not enough to buy on, and saying so is the finding — not a failure to reach one.**
