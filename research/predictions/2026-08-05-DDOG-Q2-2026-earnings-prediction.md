# DDOG (Datadog) — Q2 2026 earnings prediction

**Registered:** 2026-08-05, pre-print
**Resolves:** 2026-08-06, **PRE-MARKET** (see §1 — this is a structural finding, not an assumption)
**Workflow:** PREDICT (Workflow #4). Mandatory pre-read done: `predictions/lessons.md` (L1, L4, L6, L7, L42-b, L53, L54, L56) + `meta/biases-watchlist.md` (B45).
**Position at stake: NONE.** DDOG was fully exited by the operator 2026-06-22 (26sh @ $203.37 BEP). This is a pure calibration call — no sizing consequence, which is exactly why it is a clean instrument.
**Data provenance:** all price and estimate figures from machine routes (Finnhub `/quote`, FMP `/stable/historical-price-eod/full`, FMP `/stable/earnings`), pulled 2026-08-05. Percentages computed from levels, never from vendor change fields (L42-b, and the FMP `changePercent` defect documented in `meta/tools/earnings_reaction_ledger.py`).

---

## §1 — 🔴 STRUCTURAL FINDING FIRST: Datadog reports PRE-MARKET, so the reaction is the SAME session

This determines how the whole reaction leg is defined, and getting it wrong would have made the call ungradable. **Tested, not assumed** — the opening-gap share of each report-day move:

| Report date | prev close | open | gap % | close | full-day % | **share of move in the gap** |
|---|---|---|---|---|---|---|
| 2026-05-07 | 143.71 | 187.99 | **+30.81%** | 188.73 | +31.33% | **98%** |
| 2025-11-06 | 154.98 | 178.89 | +15.43% | 190.82 | +23.13% | 67% |
| 2023-11-07 | 79.55 | 98.99 | +24.44% | 102.20 | +28.47% | 86% |
| 2023-08-08 | 106.30 | 84.38 | **−20.62%** | 88.04 | −17.18% | 120% |
| 2024-05-07 | 126.97 | 113.26 | −10.80% | 112.40 | −11.48% | 94% |

**The news is in the price before the first trade.** So, unlike SanDisk (after-close, reaction at T+1), **Datadog's reaction leg is the 2026-08-06 close versus the 2026-08-05 close.**

---

## §2 — 🔴 THE CENTRAL FINDING: the bar is the highest it has ever been

Datadog has beaten on **both lines in 13 of 13 reported quarters**, and the revenue beat sits in a remarkably tight band (min +2.72%, max +4.82%, 8-qtr median +3.75%). That record is why this looks like a free call. It isn't.

**What the street is asking for, quarter by quarter — consensus-implied QoQ revenue growth:**

| Report | consensus-implied QoQ | actual QoQ | street shortfall |
|---|---|---|---|
| **2026-08-06 (this one)** | 🔴 **+7.17%** | pending | — |
| 2026-05-07 | +0.73% | +5.58% | +4.86pp |
| 2026-02-10 | +3.73% | +7.63% | +3.89pp |
| 2025-11-06 | +3.15% | +7.12% | +3.98pp |
| 2025-08-07 | +3.88% | +8.56% | +4.68pp |
| 2025-05-06 | +0.50% | +3.23% | +2.73pp |
| 2025-02-13 | +3.65% | +6.91% | +3.27pp |
| 2024-11-07 | +3.06% | +6.93% | +3.87pp |
| 2024-08-08 | +2.56% | +5.57% | +3.01pp |
| 2024-05-07 | +0.40% | +3.66% | +3.26pp |
| 2024-02-13 | +3.87% | +7.69% | +3.82pp |
| 2023-11-07 | +2.89% | +7.47% | +4.59pp |
| 2023-08-08 | +3.92% | +5.76% | +1.84pp |

**In twelve prior quarters the street never asked for more than +3.92% QoQ. This quarter it asks +7.17% — 83% higher than the previous record bar.** Consensus $1,078.575m implies **+30.46% YoY**, i.e. a *deceleration* from Q1's +32.15%, but a sequential step-up far beyond anything previously modelled.

**Read it plainly: the street has finally priced the AI-observability acceleration.** The structural sandbag that produced 13/13 beats is the thing that has just been arbitraged away.

## §3 — 🔴 AND THE REACTION TRACKS THE BEAT MAGNITUDE, NOT THE NARRATIVE

Three candidate predictors of the same-day move, correlated across n=12:

| Predictor | correlation with reaction |
|---|---|
| **Revenue beat magnitude** | 🔴 **+0.736** |
| 5-session run-in | +0.254 |
| Height of the bar (consensus-implied QoQ) | −0.162 |

**The beat magnitude dominates, and it is the only one of the three strong enough to act on.** Sorted:

| Revenue beat | Same-day reaction |
|---|---|
| +4.82% | **+31.33%** |
| +4.50% | −0.42% ⚠️ the one clear exception |
| +4.46% | **+28.47%** |
| +3.86% | **+23.13%** |
| +3.76% | +1.12% |
| +3.75% | **+13.74%** |
| +3.68% | −2.35% |
| +3.25% | −11.48% |
| +3.15% | −8.24% |
| +2.93% | +5.57% |
| +2.72% | +0.34% |
| +1.77% | **−17.18%** |

**Beats ≥ +3.7%: mean reaction +13.6%, 5 of 7 positive. Beats < +3.2%: mean reaction −6.2%, 1 of 5 positive.**

## §4 — The chain, stated so it can be attacked

1. The bar has risen to an all-time high (§2). **[computed, T1-route data]**
2. ⇒ the beat magnitude compresses toward ~+2 to +2.5%, below the 13-quarter minimum of +2.72%. **[my model]**
3. Beat magnitude is the dominant driver of the reaction, corr +0.736 (§3). **[computed]**
4. Sub-3.2% beats have produced a mean −6.2% reaction, 1 of 5 positive. **[computed]**
5. ⇒ **the same-day reaction is more likely NEGATIVE than positive.**

**Corroborating, independent of the chain:** a **+14.86% five-session run-in into a new all-time high** ($288.15 on 08-04 vs prior ATH $277.49). The largest run-in into any of the twelve prior prints was +7.26%; the median was −0.86%; only 1 of 12 entered above +5%. And the verified same-week regime — **Infineon raised FY guidance on AI demand and fell 3.36%; AMD beat revenue, EPS and datacentre, raised Q3, and fell; SpaceX beat on revenue and fell** — is three independent instances of this market refusing to pay for accelerating AI fundamentals (`signals/cross-source-log/2026-08-05-wed-wsj-15-screenshot-batch-three-verifications-and-four-of-my-own-errors.md` §1).

## §5 — Bottoms-up build (L1: build it, don't average the street)

Not a sell-side weighted average. Built from the company's own sequential and YoY path:

| | |
|---|---|
| Q2-2025 base | $826.76m |
| YoY trajectory | +28.12% → +28.35% → +29.21% → **+32.15%** — accelerating, and the acceleration is itself accelerating (+0.23, +0.86, +2.94pp) |
| Q1→Q2 seasonal QoQ | +8.56% (2025) · +5.57% (2024) · +5.76% (2023), mean +6.63% |
| 8-quarter median QoQ | +6.92% |

At **+33.6% YoY** — continued acceleration, but less than Q1's +2.94pp step — revenue is **$1,105m**, i.e. **+9.79% QoQ**. That sequential is above every historical Q1→Q2 print except 2025's +8.56%, which is the honest cost of believing the acceleration continues.

**L4/L6 scope check, stated explicitly because it cuts against the house habit:** L4 and L6 (smaller sandbag haircut, applied harder at the EPS line) are scoped to **multi-year-contracted-demand** names — NVDA, AVGO, TSM, MU and similar. **Datadog is consumption/usage-based with no contracted backlog.** L4/L6 do **not** apply here, and applying them by reflex would have pushed my revenue point ~$15m too high. Recording the non-application so the grade can check whether the scope judgment was right.

## §6 — THE REGISTERED CALL

**Point estimates:**

| | Point | Range | vs consensus |
|---|---|---|---|
| **Q2 revenue** | **$1,105m** | $1,085–1,130m | **+2.45%** — *below the 13-quarter minimum beat of +2.72%* |
| **Q2 non-GAAP EPS** | **$0.64** | $0.61–0.69 | +9.8% (vs 8-qtr median beat +13.76%) |
| **FY2026 revenue guide** | **raised to ~$4.52bn** | $4.46–4.58bn | current guide $4.30–4.34bn |
| **Same-day move (08-06)** | **−4%** | — | — |

**Probabilities — every one carries its provenance (Program v2):**

| Call | P | Provenance |
|---|---|---|
| **R-1** Revenue > $1,078.575m | **0.84** | DDOG own record 13/13; **BR-1 program prior 82.8% robust** (`predictions/base-rates.md`) — DDOG is NOT in the BR-1 row sample, so the parent class binds. Laplace on 13/13 gives ~0.93; **haircut to ~parent because the bar is at an all-time high** — a named, specific reason to shrink rather than exceed |
| **R-2** Non-GAAP EPS > $0.583 | **0.88** | Above R-1: the EPS beat band has far more cushion (min +6.31% vs revenue's +2.72%), and opex conservatism is a second, independent source of upside that does not require the revenue line to clear |
| **R-3** FY2026 guide raised above $4.34bn | **0.92** | **Near-arithmetically forced.** With my Q2 point, H1 = $2,116m; the current $4.34bn top leaves $2,224m for H2 = $1,112m/quarter, i.e. **+0.2% sequential — the old guide implies H2 goes flat.** Not credible for a company compounding >30%. Residual 8% covers a deliberate macro sandbag or a reiterate-don't-raise posture |
| **R-4** Same-day direction **NEGATIVE** | **0.58** | The §4 chain. Held to 0.58, not higher, because step 2 rests on an unverified premise (§8) and the last three prints went the other way, hard |
| **R-5** \|same-day move\| ≥ 10% | **0.52** | Base rate 6/12 = 50%. Nudged up marginally: a compressed beat against a record bar is a bimodal configuration, and this name's distribution is right-skewed (positive outcomes mean +14.81%, negative mean −7.93%) |

**Reaction baseline: the 2026-08-05 close, which is NOT KNOWN at registration** (US session still open as I write). Registering the baseline as a rule rather than a number, so it cannot be chosen after the fact.

## §7 — Rule #17 ensemble (N=3 independent Opus judges, identical fact set, house view withheld)

| | Rev ($m) | EPS | P(rev beat) | P(EPS beat) | P(raise) | Direction | P(dir) | P(\|move\|≥10%) | Move |
|---|---|---|---|---|---|---|---|---|---|
| **Me (registered)** | **1,105** | **0.64** | **0.84** | **0.88** | **0.92** | **DOWN** | **0.58** | **0.52** | **−4%** |
| Judge 1 | 1,101 | 0.63 | 0.87 | 0.89 | 0.96 | UP | 0.60 | 0.55 | +4.5% |
| Judge 2 | 1,102 | 0.65 | 0.85 | 0.88 | 0.94 | DOWN | 0.57 | 0.52 | −4.5% |
| Judge 3 | 1,101 | 0.65 | 0.85 | 0.88 | 0.93 | UP | 0.57 | 0.55 | +2.0% |
| **Ensemble** | **1,101.3** | **0.643** | **0.857** | **0.883** | **0.943** | **2 UP / 1 DOWN** | — | **0.540** | — |

🟢 **The numeric legs are a genuine 3/3 convergence** — revenue $1,101–1,105m (0.4% spread), EPS $0.63–0.65, and all three of us land the beat/raise probabilities within 3pp. That is the tightest agreement I have recorded on a graded call.

🔴 **The direction leg is a coin-flip dressed as a forecast.** Judge 1 says UP at 0.60; Judge 2 says DOWN at 0.57; I say DOWN at 0.58. **Two judges reasoning from the same facts produced opposite signs with near-identical confidence.** Under Rule #17 that spread IS the result: **this call is genuinely uncertain and must not be reported as conviction.** My 0.58 stands as registered — Program v2, ensemble is report-only and never sets P.

**And the agreement is worth less than it looks (L54 applied to my own ensemble):** all three judges received the same facts, assembled by me, including my framing that the bar is at a record. Convergence measures my sampling consistency, not correctness. Notably **Judge 1 independently reached the same "the beat compresses to ~2%" conclusion and still called UP** — so the disagreement is not about the quarter, it is about whether a compressed beat plus a forced raise reads as good or disappointing.

## §8 — 🔴 FALSIFIERS, each with its BLIND-CHECK (Principle #51)

**1. The bar-jump is a measurement artifact, not a real re-rating.** The historical consensus figures are FMP vendor snapshots; if past-quarter snapshots were captured earlier in each quarter than today's, the apparent jump from ≤3.92% to 7.17% is partly my own instrument. **This is the single load-bearing unverified premise in the entire call — step 2 of §4 collapses without it, and with it R-4.**
> *Blind-check: distinguishes "the street genuinely raised its bar" from "my consensus series is measured at inconsistent vintages" · reads on the snapshot timestamp of each `revenueEstimated` row against its report date · **goes blind if** the vendor does not expose a snapshot date at all — which is the current state, meaning I cannot presently falsify this and am registering anyway with the weakness named. A second vendor's pre-print consensus for THIS quarter would partially resolve it; it would not resolve the historical rows.*

**2. R-1 fails (revenue misses $1,078.575m).** Then "the quarter is fine, only the bar moved" is wrong, the 13/13 streak breaks, and R-4 grades as luck rather than reasoning even if the direction is right.
> *Blind-check: distinguishes "demand decelerated" from "the street simply over-modelled" · reads on reported revenue against both consensus AND the +33.6% YoY path · **goes blind if** the company changes revenue presentation or completes an acquisition that muddies the organic line — no acquisition is pending that I know of, which is itself unverified.*

**3. FY guidance is NOT raised above $4.34bn (R-3 fails).** That would mean management sees something in H2 that the sequential arithmetic cannot: consumption softness, a large customer optimising down, or macro caution.
> *Blind-check: distinguishes "H2 demand is genuinely softer" from "management is sandbagging into an uncertain macro" · reads on the FY revenue guide range versus the H1 actual · **goes blind if** they raise the floor but not the top, or raise by a token amount — a $4.35bn top would technically resolve R-3 TRUE while carrying the opposite meaning. **Recording now: a raise of less than $100m above the current top will be graded as a technical TRUE and a substantive FALSE, and both will be reported.***

**4. \|same-day move\| < 5%.** Then both R-5 and the whole "this print is decisive" framing are wrong — the market found it uneventful, which no branch of this call predicts.
> *Blind-check: distinguishes "the print was uneventful" from "the reaction was absorbed pre-market and reversed intraday" · reads on close-vs-close, with the open recorded separately so the gap and the fade are visible as distinct facts · **goes blind if** a market-wide event dominates the session — grade sector-relative against IGV/WCLD as well as absolute.*

**5. A same-window confound.** The lesson from this week: my SanDisk confound check read the company's own calendar and missed a market-structure event on the grading day.
> *Blind-check: distinguishes "the market repriced Datadog" from "something else moved the tape" · reads on the 08-06 session against a software-cohort control · **goes blind if** the confound is INSIDE the earnings release — the AMD specimen, where a capex line nobody modelled drove the move while I read it as sentiment. **A beat is defined by the lines the street models; a sell-off is caused by any line at all.**

## §9 — What I expect to be wrong about

**If this call fails, the most likely reason is B45 — under-calling upside in this regime.** My documented failure mode is exactly this: the last three Datadog prints delivered +31.3%, +13.7% and +23.1%, and I am calling DOWN into that. The run-in/reaction correlation across the twelve prints is **positive (+0.254)**, not negative — so the "priced for perfection" instinct underneath R-4 is the one thing the data actively contradicts, and I am overriding it on a beat-magnitude relationship measured on n=12.

**Stating the counterfactual now so the grade can hold me to it:** if DDOG prints ≥$1,120m (a ≥+3.8% beat) and rips double digits, the lesson is not "the reaction was unpredictable" — it is that **I let a strong same-week narrative (Infineon/AMD/SpaceX all falling on good news) override a name-specific base rate that pointed the other way.** That is a named, checkable failure, and it is the one I consider most likely.

**Position implication: NO ACTION — 0% — not held; calibration call only.** 🟡 Nothing here is a re-entry recommendation; the operator exited on 2026-06-22 and any re-entry is a separate, user-gated decision.

---

## 🔴 REVISION #1 — 2026-08-05, still pre-print. **The commissioned verifier refuted step 2 of my own chain. R-4 FLIPS.**

The Critical Rule #16 verifier returned T1 company guidance I did not have when I registered. **It does not weaken my headline finding — it re-explains it, and the re-explanation reverses the conclusion I drew from it.**

### 🔴 The "record bar" is real, but it is the COMPANY's bar, not the street's

**T1 (Datadog Q1 release, 2026-05-07) — Q2 FY2026 guidance: revenue $1.07–1.08B · non-GAAP EPS $0.57–0.59 · non-GAAP OI $225–235M (embeds ~$15M of DASH conference cost).**

**Consensus $1,078.575m is 99.87% of the guide TOP.** So the consensus-implied +7.17% QoQ I flagged in §2 is not the street getting aggressive — **the street is simply printing the company's own guide.** And that reframes the whole series:

| Guide | vs prior-quarter actual | guide-TOP implied QoQ |
|---|---|---|
| **Q2-26 $1.07–1.08B** | $1,006.4m | 🔴 **+7.31%** |
| Q1-26 $951–961M | $953.2m | +0.82% |
| Q4-25 $912–916M | $885.7m | +3.43% |

**Datadog itself guided Q2 at +6.3% to +7.3% sequential, against +0.8% and +3.4% the prior two quarters.** That is not the street pricing in an acceleration — **that is management telling you one is coming.** It is a bullish disclosure, and I read it as a bearish setup.

### 🔴 Step 2 of §4 is refuted, and it was load-bearing

My chain said: *bar at all-time high ⇒ beat magnitude compresses to ~2–2.5% ⇒ sub-3.2% beats have produced a mean −6.2% reaction ⇒ DOWN.* **The correct instrument is the beat versus the COMPANY'S GUIDE, not versus consensus** — and consensus ≈ guide top every quarter, so the two only look different when the guide itself moves.

**Guide-relative beat (T1, the clean series):** Q4-25 actual **+4.06%** above guide high · Q1-26 actual **+4.72%** above guide high. Mean **+4.39%** — *n=2 only, and I am not going to pretend that is a base rate.*

| Method | Q2 revenue | vs consensus | QoQ | YoY |
|---|---|---|---|---|
| Guide-high +4.39% | $1,127.4m | +4.53% | +12.02% | +36.37% |
| **Guide-high +3.5% ← NEW POINT** | **$1,117.8m** | **+3.64%** | **+11.07%** | **+35.20%** |
| Street-shortfall method | $1,116.0m | +3.47% | +10.89% | +34.98% |
| ~~My original point~~ | ~~$1,105.0m~~ | ~~+2.45%~~ | | |

**A ~+3.6% beat is a NORMAL beat, not a compressed one — and per my own §3 mapping, beats ≥+3.7% produced a mean +13.6% reaction with 5 of 7 positive.** The relationship I identified as the strongest predictor (corr +0.736) now points the opposite way, because I fed it the wrong input.

**Corroborating leading indicators I did not have (all T1, Q1-26 call):** **RPO $3.48B, +51% YoY**; current RPO **+mid-40s%** — both far above the 29–31% revenue guide. **NRR inflecting up to low-120s%** from ~120%. And the CFO verbatim: *"we are applying a higher degree of conservatism to our largest customer"* — **for the second consecutive quarter.** That is a documented, management-confirmed sandbag sitting underneath a guide that already implies acceleration.

### 🔴 REGISTERED CALLS — REVISED

| Call | Registered | **REVISED** | Why |
|---|---|---|---|
| **Revenue point** | $1,105m | **$1,118m** | guide-relative beat, not consensus-relative |
| **EPS point** | $0.64 | **$0.65** | flow-through on the higher revenue point |
| **R-1** Revenue > $1,078.575m | 0.84 | **0.87** | the guide-relative instrument is cleaner and stronger than the consensus-relative one I used |
| **R-2** EPS > $0.583 | 0.88 | **0.90** | consensus $0.583 sits at the guide MIDPOINT-to-top, not the top — a softer bar than the revenue line |
| **R-3** FY guide raised > $4.34bn | 0.92 | **0.93** | unchanged reasoning; RPO +51% marginally firms it |
| 🔴 **R-4** Same-day direction | **DOWN 0.58** | 🔴 **UP 0.55** | **DIRECTION FLIPPED.** The compressed-beat premise it rested on is refuted |
| **R-5** \|move\| ≥ 10% | 0.52 | **0.60** | **options-implied move ~±13%** (T2, Bloomberg ~2026-07-30); historical mean \|move\| **11.95%**, median **9.86%** |
| **Same-day move point** | −4% | **+3%** | |

### On flipping a direction call the day before it resolves

**I registered DOWN two hours ago and I am now registering UP.** That is a real reversal and it should count against me if the reasoning was sloppy. My defence is narrow and checkable: **the flip is driven by a single T1 document I did not have** — the company's own Q2 guide — and it changes an input, not a preference. The §4 chain is intact as *logic*; step 2's input was wrong.

**What I got right and want on the record:** the bar IS at an all-time high, that finding was mine, computed from machine data, and no source stated it. **What I got wrong:** I attributed it to the street when it belongs to management, and that single misattribution inverted the conclusion. **The lesson is the one from this morning restated: I read a real quantity with the wrong instrument** — consensus-relative beat, when the company publishes a guide that consensus simply copies.

### 🔴 THE BEAR CASE, restated properly, because it did NOT disappear

**The single best bear precedent is now much sharper than before, and it comes from resolving a source contradiction (L42-b):**

**2025-08-07 — Datadog beat revenue by +4.50% (a normal beat), gapped +7.88% at the open, and closed −0.42%. It gave the entire gap back in one session.**

| Basis | Move |
|---|---|
| Gap (prev close → open) | **+7.88%** |
| Open → close | **−7.70%** ← the "−8.4%/−7.7%" figure circulating in secondary sources |
| **Close → close (the graded basis)** | **−0.42%** |

Both figures are real and describe the same session; secondary sources quoting "−8.4%" are using an open-to-close basis. **My close-to-close series was correct and the discrepancy was a basis mismatch, not an error** — but the resolved specimen is far more informative than either number alone: **a normal beat on this name has already, once, produced a full round-trip of an 8% gap.**

That is precisely the risk in a **+14.86% five-session run-in**, and it is why R-4 is 0.55 and not 0.65.

**Basis stamps on the ATH claim (L42-b):** $288.15 (08-04) is the **highest CLOSE** (prior closing ATH $277.49, 2026-06-01, +3.84%). **$289.90 is the 52-week intraday high and was set in the SAME 08-04 session**, so the close sits 0.60% below it. My §4 "new all-time high" stands on a closing basis; both bases are now stamped.

**Analyst price targets $261.68–$270.82 sit BELOW the $288.15 close** *(analyst-PT framing; recorded as neutral context, NOT used as a valuation argument — B28/B37: the sell-side lags structural re-ratings by 2–3 quarters and this cohort is mid-re-rating)*.

### 🔴 Two stale figures killed before they could cascade

1. **"AI-natives are 12% of Datadog revenue"** — that is a **Q3-2025** figure. **Datadog DISCONTINUED the metric after Q3 2025** (verified by absence in both the Q1-26 release and the full Q1-26 call transcript). It has been replaced by growth *excluding* AI-natives (Q1-26: mid-20s%) plus a customer-count cut (22 AI-native customers >$1M, 5 >$10M). **Any live use of "12%" is three quarters stale.** Note the disclosure-quality regression: a percentage-of-revenue series was replaced by a counting metric, which is L10 territory — *when management re-frames a metric, infer from the TYPE of metric chosen.*
2. **The OpenAI-concentration bear case** ($170–300M ARR, "$240M → $80M", the July-2025 Guggenheim ">$150M shortfall by 2026" downgrade) is **mid-2025 vintage and overtaken by three prints** in which revenue *accelerated* 28% → 29% → 32%. Datadog has **never named OpenAI** in any T1 document — only "our largest customer."

### Amended blind-check on the revised call

*Distinguishes "the market repriced Datadog's quarter" from "a good quarter was already fully paid for in the run-in" · reads on the 08-06 close versus the 08-05 close, **with the open recorded separately** so a gap-and-fade is visible as a distinct outcome rather than averaging into a small close-to-close number · **goes blind if** the move is entirely intraday reversal — the 2025-08-07 specimen would grade as "−0.42%, uneventful" on close-to-close alone while actually being a violent +7.9% → −7.7% round trip. **Therefore: gap, open-to-close, and close-to-close will ALL be recorded at the grade, and R-4 grades on close-to-close as registered.***

**FINAL FOR THE PRINT: revenue $1,118m · EPS $0.65 · FY guide ~$4.53bn · R-1 0.87 · R-2 0.90 · R-3 0.93 · R-4 UP 0.55 · R-5 0.60 · move +3%.** Reaction baseline remains the 2026-08-05 close, still unknown at revision time.

**Position implication: NO ACTION — 0% — not held; calibration call only.** 🟡

---

## 🔴 OPERATOR-DRIVEN ADDENDUM — 2026-08-05, pre-print. "Why did the bar jump — the AI story, or extrapolation?"

**Operator's question, registered before the print so it grades honestly.** He asked whether the consensus jump is (a) Datadog being re-rated into the AI basket, or (b) the street mechanically revising up off recent delivery — and asked to see what the street *wanted* versus what Datadog actually *gave* in prior quarters.

**The question is better than the one I was answering.** I treated the record bar as a fact about the setup. He asked what *causes* it, which is the question that generalises.

### The decomposition (T1 guides + FMP consensus snapshots + actuals)

| Quarter | company guide-top implies QoQ | consensus implies QoQ | **consensus vs guide-top** | actual QoQ | actual vs guide-top |
|---|---|---|---|---|---|
| Q4-25 (rep 2026-02-10) | +3.43% | +3.73% | **+0.29%** | +7.63% | **+4.06%** |
| Q1-26 (rep 2026-05-07) | +0.82% | +0.73% | **−0.09%** | +5.58% | **+4.73%** |
| **Q2-26 (rep 2026-08-06)** | **+7.31%** | **+7.17%** | **−0.13%** | *pending* | *pending* |

🔴 **ANSWER: neither (a) nor (b) — on the revenue line the street did nothing at all.** Consensus tracks the company's guide **top** to within 0.6pp in all three quarters, including this one. **The street is not front-running the AI story and is not extrapolating. It is transcribing the guide.**

**The thing that jumped is Datadog's OWN guide: +3.43% → +0.82% → +7.31% sequential.** Management removed its own sandbag. That is a *company* decision, not a market one — and the operator's framing surfaced it because he asked about causation rather than level.

### What the street wanted vs what Datadog gave — the operator's direct question

**In guide-space (T1, the honest space):** Datadog promised ≤$916m and delivered $953.2m (**+4.06% above its own ceiling**); promised ≤$961m and delivered $1,006.4m (**+4.73%**). Mean overshoot of its own ceiling **+4.39%** *(n=2 T1 — thin, and I will not dress it as a base rate)*.

**In consensus-space (13 quarters, FMP):** beat every single time, band **+2.72% to +4.82%**, median **+3.75%**.

**⇒ Datadog has never once been asked for what it actually delivers.** The 13/13 streak is not thirteen acts of outperformance. It is **one act of conservative guidance, repeated thirteen times, with the street copying it each time.**

### 🔴 WHERE THE AI RE-RATING ACTUALLY LANDED — not where the question assumed

The operator's AI-basket hypothesis is **CORRECT, but about the wrong line item.** Over the last 30 days:

| | |
|---|---|
| Price targets | KeyBanc $225→**$320** · Mizuho $220→**$300** · Jefferies $210→**$280** · Morgan Stanley →$300 · BTIG →$289 · Citi →$300. **Mean raise +37.3% where the prior is known (n=3); ≥6 raises total** |
| **Earnings estimates, same window** | **$0.58 → $0.58. Unchanged.** |

🔴 **The AI re-rating went entirely into the MULTIPLE and not at all into the NUMBERS.** Six brokers raised what they think the stock is worth by roughly a third while changing nothing about what they think it will earn. *(Analyst-PT framing recorded as neutral context, not as a valuation argument — B28/B37.)*

**Scale, computed over the guide-raise window:** from the 2026-02-10 pre-print close (**$114.01**) to 2026-08-04 (**$288.15**) the stock rose **+152.7%**. Over the same window the company's own FY26 revenue guide midpoint went **$4.08bn → $4.32bn = +5.88%** (T1). **The price moved 26× the guide; ~96% of the move is re-rating rather than earnings revision** *(my model, single-window, deliberately crude — it ignores the FY27 forward roll, so treat it as an order of magnitude, not a decomposition)*.

**This ties directly to the 2026-08-05 macro read** (`signals/cross-source-log/2026-08-05-wed-wsj-15-screenshot-batch-three-verifications-and-four-of-my-own-errors.md` §1): *fundamentals accelerating while multiples compress.* Datadog is the mirror-image specimen — **a name whose multiple expanded ~26× faster than its numbers, walking into a tape that has spent this week compressing exactly that.** Infineon, AMD and SpaceX all beat or raised this week and fell. That is the risk in R-4 stated in its proper form at last: **not "the beat will be small" but "the multiple did the work, and the multiple is what is under pressure."**

### 🔴 THE FINDING THAT OUTLIVES THIS PRINT — a harness finding, not a Datadog one

**A beat streak measures the distance between guidance and reality. It does not measure the company.** When management stops sandbagging — as Datadog just did, guiding +7.31% against +0.82% one quarter earlier — **the streak ends by construction, with the business unchanged and possibly stronger.**

**So the instrument expires exactly when the news is best**, and a reader who does not decompose books the end of the streak as deterioration.

🔴 **We are exposed to this across the prediction program, not just here.** A grep of `research/predictions/` returns **12 prediction files using beat-history reasoning**, including the SanDisk call resolving *today*, whose structural claim is *"last quarter beat its guide midpoint 1.80×."* **Every one inherits the same hidden assumption — that the street stays behind. None of them states it.**

> **Lesson candidate — L57 (CANDIDATE, N=1): a beat-history base rate measures the GUIDANCE GAP, not the company. Before using one, check whether the gap is still open — compare the current guide's implied sequential growth to the prior two guides'. If the company has re-based its own guide, the historical beat magnitude does not transfer, and the streak's end is not evidence of deterioration.**
>
> *Blind-check (#51): distinguishes "the company is decelerating" from "the company stopped sandbagging" · reads on guide-implied sequential growth versus the trailing two guides, and on actual-vs-guide-top rather than actual-vs-consensus · **goes blind if** the company stops issuing quarterly guidance, or guides on a metric it did not previously guide (the L10 re-framing move) — there is then no guide-space to measure in, and the base rate silently reverts to consensus-space without anyone noticing the substitution.*

**Validation criterion:** if the next three prediction files invoking a beat-history base rate carry an explicit guide-gap check, L57 is being applied. If DDOG's beat lands inside the historical +2.72–4.82% band **despite** the re-based guide, L57 is weakened at N=1 — the sandbag would have been re-established at the new level rather than removed.

### Operator hypotheses, registered as gradable calls

| | Claim | Verdict | Resolves |
|---|---|---|---|
| **O-1** | The consensus jump is caused by Datadog's inclusion in the AI story/basket | 🟡 **PARTIAL — refuted on the revenue line, confirmed on the multiple.** Consensus = guide top (no AI premium in the estimate); PTs +37.3% with EPS estimates flat (all the AI premium in the target) | resolved pre-print, above |
| **O-2** | The street revised upward off recent delivery (extrapolation) | 🔴 **REFUTED.** Consensus never deviates from the guide by more than 0.6pp in any of the three quarters with T1 guide data | resolved pre-print, above |
| **O-3** *(mine, arising from his question)* | Because the guide was re-based, the Q2 beat lands **below** the historical +2.72–4.82% consensus-relative band | **P = 0.45** *(my model)* — my registered point of $1,118m is +3.64%, i.e. **inside** the band, so I am predicting against my own O-3 | 2026-08-06 |

**O-3 is deliberately registered against my own point estimate.** If the beat lands inside the historical band, my revenue call is right and L57 is weakened. If it lands below, L57 is strengthened and my revenue point was too high. **Both outcomes teach something, which is the only reason to register it.**

**Position implication: NO ACTION — 0% — not held; calibration only.** 🟡

---

## §DATA — Last four reported quarters: consensus vs actual (source table)

**Source:** FMP `/stable/earnings?symbol=DDOG`, pulled 2026-08-05. `epsEstimated` / `revenueEstimated` are FMP's pre-print consensus snapshot; actuals are as reported. Beat percentages computed from levels (L42-b).

| Quarter | Reported | Revenue consensus | Revenue actual | Beat | EPS consensus | EPS actual | Beat |
|---|---|---|---|---|---|---|---|
| Q1 2026 | 2026-05-07 | $960.1m | **$1,006.4m** | **+4.82%** | $0.508 | **$0.60** | **+18.11%** |
| Q4 2025 | 2026-02-10 | $918.7m | **$953.2m** | **+3.75%** | $0.555 | **$0.59** | **+6.31%** |
| Q3 2025 | 2025-11-06 | $852.8m | **$885.7m** | **+3.86%** | $0.458 | **$0.55** | **+20.19%** |
| Q2 2025 | 2025-08-07 | $791.1m | **$826.8m** | **+4.50%** | $0.410 | **$0.46** | **+12.11%** |
| **Q2 2026** | **2026-08-06** | **$1,078.575m** | *pending* | — | **$0.583** | *pending* | — |

Unrounded revenue figures as pulled: consensus 960,117,500 / 918,700,800 / 852,761,661 / 791,123,833 / 1,078,575,000; actuals 1,006,426,000 / 953,194,000 / 885,651,000 / 826,760,000.

**8 of 8 lines beaten. Revenue beat band +3.75% to +4.82%** across these four (the 13-quarter band in §2 is wider, +2.72% to +4.82%, because it reaches back further).

**Cross-verification status (stated because it is uneven):**

| Row | Second source? |
|---|---|
| Q2 2026 consensus ($1.08bn rev / $0.58 EPS) | 🟢 **CONFIRMED** by commissioned Opus verification 2026-08-05, independent of FMP |
| Q1 2026 EPS consensus (~$0.51) | 🟢 **CONFIRMED** by the same verification |
| Q1 2026 / Q4 2025 revenue consensus | 🟡 **PARTIAL** — verifier derived ~$959.9m and ~$914.6m, close to but not identical with FMP's $960.1m and $918.7m; vendor-compilation noise, not a contradiction |
| **Q3 2025 and Q2 2025 revenue consensus** | 🔴 **NOT INDEPENDENTLY VERIFIED** — the verifier marked both "not pinned" after most finance hosts returned HTTP 403. **Single-vendor rows.** |
| All actuals | 🟢 Consistent with the T1 company releases cited elsewhere in this file |

**This uneven verification is itself the caveat that matters for §2 and the OPERATOR ADDENDUM:** the consensus series is the load-bearing input to the "record bar" finding, and two of its rows rest on one vendor.
