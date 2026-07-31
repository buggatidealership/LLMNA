# 2026-07-31 (Fri) — KR-OPEN WAKE: the gap closed and overshot; the flow discriminator INVERTED; H3 needs a re-spec

**Workflow:** KR-OPEN WAKE (time-sensitive leg of `meta/good-morning-protocol.md`), 3 legs fired in parallel at 00:30Z / 09:30 KST + 1 targeted verifier
**Escort status:** I-2 and I-3 instrument blocks (addendum #3) — this is within the "first 3 readings hand-decomposed" window. Decomposition is explicit below.
**Sync:** `git rev-list --left-right --count origin/main...HEAD` = **0 / 0** (mandatory W11 step 1 — live system confirmed)
**NO POSITION ACTIONS — user-gated throughout.**

---

## §0 — 🔴 THREE ANCHOR CORRECTIONS, ALL TO MY OWN INPUTS

Booked first and loudly, because two of them would have inverted conclusions. **All three were errors I introduced in the agent briefs — the agents caught them.**

| # | What I asserted | Verified actual | How it was caught |
|---|---|---|---|
| **A1** | SK Hynix closed **1,401,000** on 07-30 | **1,322,000** on 07-30. 1,401,000 was the **07-29** close | EODHD prevClose + 헤럴드경제/파이낸셜뉴스 (T2). **Self-proving**: 1,322,000/1,401,000−1 = **−5.639%**, which is the −5.64% *my own brief cited in the same sentence*. The brief contradicted itself and I did not notice. |
| **A2** | Brent settled **$90.74 +7.9% on 07-30** | That was **07-29**. 07-30 settled **$89.03, −1.9%** — direction **reversed** | CNBC 07-29 + 07-30 (T2). Corpus addendum #12 said "Wed" and was correct; **I mislabelled it in the prompt.** |
| **A3** | Foreign 07-30 = **net-SELL −₩1.25조**, streak session 4 | **net-BUY +₩1.33조**, AND session 4 was **07-29** not 07-30 | ✅ **REFUTED by 10+ independent newsrooms** (§3). **Two errors: sign inversion AND off-by-one date.** Origin of −₩1.25조 UNIDENTIFIED. |

**A1 is the instructive one.** The self-consistency check that falsifies it was *inside the same sentence*. Cost: had the agent accepted my anchor, every gap-close percentage in this artifact would be wrong by ~6pp. **Candidate rule: any brief that supplies BOTH a price level and a % change must have the implied prior computed and cross-checked before the brief ships.** That is mechanical, cheap, and would have caught this without a subagent.

**Vendor defect #2 (index stale-prevClose) CONFIRMED N+1 on BOTH indices** — EODHD `KS11.INDX` prevClose returned 5,663.24 (= the **07-29** close) and `KQ11.INDX` returned 662.68 (also 07-29). Singles were correct. Every vendor index `change_p` was discarded and recomputed off verified closes. The vendor `open` field for KS11 (5,657.79) was *also* internally inconsistent with a session already printing 6,386 — **same defect family, new field**. Route note for `meta/data-access.md`: the EODHD index defect is not confined to `prevClose`.

---

## §1 — GAP-CLOSE: CLOSED, OVERSHOT, NOW FADING (computed, not narrated)

All levels EODHD real-time, ts **2026-07-31T00:10:00Z = 09:10 KST** (~20-min delayed feed, T2). Bases are the corrected 07-30 closes.

| Instrument | 07-30 close | Open | Session high | **09:10 KST** | Session low |
|---|---|---|---|---|---|
| **SK Hynix** | 1,322,000 | 1,697,000 **+28.37%** | *(= open)* | **1,608,000 +21.63%** | 1,586,000 +19.97% |
| **Samsung** | 207,000 | 257,000 **+24.15%** | 260,000 **+25.60%** | **245,500 +18.60%** | 243,000 +17.39% |
| **KOSPI** | 5,593.56 | — | 6,386.05 **+14.17%** | **6,247.56 +11.69%** | — |
| **KOSDAQ** | 644.78 | — | — | 687.77 **+6.67%** (00:06Z) | — |

Independently corroborated by Bloomberg (T2): *"Kospi rose as much as 14%, the most on record. SK Hynix jumped as much as 28%… Samsung Electronics rose 26%"* — matching the machine prints to the decimal.

### §1.1 — 🔑 THE ADR WAS THE RIGHT ANCHOR, NOT FRANKFURT

This is the methodological finding of the wake, and it is computable rather than interpretive:

| Offshore anchor | Implied gap vs Seoul −5.64% | Residual at open | **Residual at 09:10** |
|---|---|---|---|
| Frankfurt +13.14% | **18.78pp** | +9.59pp over | **+2.85pp over** |
| **US ADR (SKHY) +17.52%** | **23.16pp** | +5.21pp over | **−1.53pp = essentially exactly closed** |

**Frankfurt under-predicted by 4.38pp because it closes before the US memory melt-up** (MU +18.36% to $874.66, T1 Finnhub). The venue that trades *latest and deepest* priced Seoul correctly to within 1.5pp.

**This generalises beyond today** — it is a refinement to the venue-control methodology booked 07-30: *when multiple offshore venues quote the same underlying, the correct predictor is not the nearest venue or the average, but the venue with the LATEST close relative to the driving catalyst.* Frankfurt's error here was not mispricing; it was **clock position**. 🟢 HARD (computed from three machine-verified prints).

### §1.2 — Samsung is the anomaly

Samsung's residual is **+5.75pp over** its implied gap and has *not* given it back, versus SK Hynix's −1.53pp. Samsung overshot roughly **2×** its gap-arb implication. That asymmetry is not explained by gap-closing and needs its own cause — the obvious candidate is its own Q2 print (OP ₩89.5조, +1,813.8%, shortage guided **through 2028**), i.e. Samsung is being **re-rated on fundamentals** while SK Hynix merely **re-converged on arbitrage**. 🟡 DIRECTIONAL — stated as the leading hypothesis, not a conclusion.

### §1.3 — ⚠️ THE FADE, AND WHY I AM NOT CALLING THIS CONFIRMATION

| | Peak | 09:10 | Given back | % of move surrendered |
|---|---|---|---|---|
| SK Hynix | +28.37% | +21.63% | **6.73pp** | 24% |
| Samsung | +25.60% | +18.60% | **7.00pp** | 27% |
| KOSPI | +14.17% | +11.69% | **2.48pp** | 17% |

**Singles are fading ~3× the index rate** — the signature of an auction stuffed with market-on-open demand into thin offer, with real supply arriving after.

**🔴 THE PRECEDENT THAT MATTERS: this exact shape failed 24 hours ago.** On 07-30 KOSPI opened +0.33%, ran to **+6.85%**, and **closed −1.23%** — a complete round-trip. Samsung likewise surrendered an +8% intraday gain to close −0.72% *on the day it reported +1,813.8% operating profit*.

**Per B45, the discipline cuts BOTH ways.** The regime prior exists to stop me under-calling magnitude — but a ±14% index day two sessions after back-to-back circuit breakers is **two-sided instability, not directional confirmation**. The 07-28/29 crash and today's melt-up are the same volatility regime. **I am explicitly NOT reading +21.63% as thesis confirmation**, and the falsifier is live and specific: *if today fades to red the way 07-30 did, the positioning-flush read in §3 is wrong and this is distribution.*

---

## §2 — I-3 DISCRIMINATOR READING (escorted reading, hand-decomposed)

The I-3 block specifies: **PRIMARY** = KRX investor-type flows + KOSPI200 futures basis + night-futures gap + opening-auction sell-concentration; **반대매매** = forced-supply gauge; **KOFIA margin balance** = policy-contaminated SECONDARY.

| I-3 channel | Read | Status |
|---|---|---|
| KRX investor-type flows | ✅ **RESOLVED — corpus REFUTED** (§3) | ✅ READ (07-30 basis; 07-31 unavailable this hour) |
| KOSPI200 futures basis (콘탱고/백워데이션) | **NOT OBTAINED** | ❌ UNREADABLE |
| Overnight CME-linked 야간선물 gap | **NOT OBTAINED** | ❌ UNREADABLE |
| Opening-auction pattern | **gap-up → monotonic fade** (§1.3) | ✅ READ |
| 반대매매 (forced-supply) | 07-28 ₩138.9억 / 07-29 ₩611.3억 (+340%) | ✅ READ (07-30 print outstanding) |
| KOFIA 신용융자잔고 | ₩32조9,950억, −~₩2,000억 DoD | 🟡 POLICY-CONTAMINATED — do not read as fear |

**Honest scorecard: 4 of 6 channels readable** (flows resolved by the verifier). The two most decision-relevant *predictive* channels (futures basis, night-futures gap) are **both dark**, and they are the two that would have told us pre-open what the auction would do. This is a standing instrument gap, not a one-day miss.

### §2.1 — 반대매매: the 07-28 print FOUND (3 days outstanding), and the cascade looks ABORTED

| As-of | 반대매매 | % of 미수금 |
|---|---|---|
| **2026-07-28** | **₩138.9억** | 1.3% |
| **2026-07-29** | **₩611.3억** (+340% DoD) | 5.0% |
| 2026-07-30 | **not yet published** | — |

위탁매매 미수금 (07-29): **₩1조1,999억**. Source: KOFIA via 한국일보/파이낸셜뉴스/서울경제 (T1-originated, T2-carried).

**Mechanism (why the missing print may not matter):** KOFIA publishes T+1 and covering itself lags the crash by a day, so 07-28's −10.84% covered on 07-29 (₩611.3억), and 07-29's −5.98% covers on 07-30 → **that is the print we are missing, and it should be the largest**. But today's **+11.69%** very likely restores collateral ratios (the 140% 담보비율 trigger) *en masse*. **The forced-liquidation cascade has probably been aborted mid-sequence rather than run to completion.** The 07-30 print, when it lands, is therefore **backward-looking, not predictive** — which materially reduces its value and is worth saying before it arrives rather than after.

### §2.2 — Leveraged-ETF measure EFFECTIVE TODAY (T1, FSC)

Source: 금융위원회 `fsc.go.kr/no010101/87403` — **T1**. Scope: **단일종목 leveraged ETF/ETN**, domestic and overseas-listed. **Pulled forward from August** because product turnover grew too fast.

1. 기본예탁금 **₩10m → ₩30m, CASH ONLY**
2. **대용증권 excluded** (stocks/ETFs/bonds no longer count toward the deposit)
3. **T+2 cash recognition** — selling 대용증권 on T does not credit until settlement
4. **Applies to existing investors**, not only new accounts

**Why this contaminates the margin series (the I-3 policy-contamination clause, now with a named mechanism):** rule 3 *mechanically forces* a class of levered retail accounts to sell securities two days before they can redeploy. Any margin-balance decline or selling pressure observed **07-31 → 08-04** is **jointly caused** by crash-deleveraging and by a regulatory cash-conversion requirement, and the aggregate print cannot separate them. **신용융자잔고 is uninformative as a fear gauge this week.** 🟢 HARD (T1 regulator).

**2nd-order (P~60%):** a cash-only deposit rule biting on the day of a +11.7% melt-up **structurally suppresses levered retail participation in exactly the rebound retail just capitulated into.**
**3rd-order (P~40%):** with retail rule-constrained from chasing, the **foreign/institutional bid sets the marginal price** for at least the next several sessions — which makes §3's flow question *more* load-bearing, not less.

### §2.3 — ADR premium: BLEW OUT on conversion opening, now compressing

Ratio confirmed **10 ADR : 1 원주** (T2). ADR **$149.00** (T1 Finnhub, 07-30 US close).

| Local ref | FX 1,400 | FX 1,437.10 | FX 1,460 |
|---|---|---|---|
| 07-30 close 1,322,000 | +57.8% | **+62.0%** | +64.6% |
| **live 09:10 1,608,000** | +29.7% | **+33.2%** | +35.3% |

**Against the 07-30 expectation — I was wrong on direction.** The 07-30 wake called conversion-opening a "compression technical." The premium **widened** from ~25% pre-conversion (07-15) to ~62%, because the ADR line held while Seoul crashed 27.2% in three days. **Today's Seoul rally is doing the compression, not the conversion mechanism.**

**Why the dislocation persists:** conversion is capacity-capped at **17.79m shares 원주-basis** (the newly-issued count, T2), and arbitrage requires routing through a securities firm with FX procedures, fees and settlement delay. A capacity-capped, friction-laden arbitrage can sustain a 30-60% wedge. **Report the band ~30-35%, never a point** — the figure is FX-sensitive by ±2.8pp across a plausible KRW range and live USD/KRW is unavailable (Finnhub forex 403; FRED `DEXKOUS` last = 07-24, pre-crash).

---

## §3 — ✅ THE FLOW DISCRIMINATOR: CORPUS REFUTED, REWEIGHT EXECUTED

**Resolved by an adversarial verifier instructed to KILL the new figure. It survived every attack. Full adjudication in ADDENDUM #13 of the five-calls file.**

**Verdict: the corpus was wrong twice — a SIGN INVERSION on 07-30 and an OFF-BY-ONE DATE SHIFT on the streak position.** 10+ independent newsrooms (아시아경제 / 파이낸셜뉴스 / 아주경제 / 머니투데이 / 한국경제 / 이투데이 / digitaltoday / 경향신문 / 서울경제 / UPI, all T2, separate bylines) report **foreign +₩1.33조 NET BUY**; **zero** sources report net-sell. Refutation attacks that FAILED: date-shift (no session matches 1.25조), KOSDAQ contamination (**inverts against the corpus** — KOSDAQ foreigners were the sole net buyer at +2,481억), intraday staleness (path was +4,330억 → +1조3,252억, positive all day), unit error (explicitly 조-denominated), and an **internal arithmetic-balance test a sign-inverted leg could not pass**.

**The corrected streak — PEAK → COLLAPSE → REVERSE:** −3.28조 / −2.90조 / **−4.98조 (peak, CB day)** / **−0.079조 (session 4 = 1.6% of session 3, 0.70% of the cumulative)** / **+1.33조 (broken)**. **"Persisting" and "accelerating" are false on the data.** True DoD collapse into session 4: **−98.4%**, not the −72% recorded.

**Addendum #12's trigger was still VALIDLY met** on 07-24/27/28 (N=3 ≥ 3). What was false is the 07-30 *confirmation* — **the corpus recorded an escalation on the session that was the reversal.** Also verified: foreigners bought SK Hynix **+₩5,876억 INTO** its −5.64% session — the informed bid was on the other side of the decline.

**🔴 Origin of −₩1.25조: UNIDENTIFIED.** It matches no KOSPI cash session 07-24→07-30 and no 07-30 KOSDAQ figure. **An unexplained number entering the corpus is a live process risk** — routes to the open INTAKE-BOUNDARY P0 as a second live specimen alongside today's KIOXIA intake failure.

**Superseded first-pass text below (kept as the record of what was known pre-verifier):**

| Date | 외국인 (foreign) | 기관 | 개인 (retail) |
|---|---|---|---|
| 07-29 close | net sell (streak session 3) | — | **−₩1.97조** |
| 07-30 10:23 KST | +₩4,330억 | +₩6,831억 | −₩1조1,040억 |
| **07-30 close** | **+₩1조3,252억 NET BUY** ⚠️ | +₩7,440억 | **−₩1조4,220억** |

**The conflict:** the corpus records 07-30 foreign as **−₩1.25조 net SELL** ("session 4, collapsing −72% DoD"). 아시아경제 CORE reports **+₩1.3252조 net BUY**, accelerating 3.1× into the close. The magnitudes are near-mirrors (1.25 vs 1.3252) — **consistent with an upstream sign inversion**, and the total spread on this one number is **₩2.5752조**.

**Why I will not act on it:** it is **single-source**, and it gates a pre-registered reweight. The addendum-#8 trigger *"foreign net-sell persisting ≥3 KR sessions → H3 to ~35"* is what drove H3 from 28 to 35 in addendum #12. **If foreigners were net BUYERS on 07-30, the streak broke at session 4 and that reweight rests on a false input.** A targeted adversarial verifier is running with instructions to *refute* the new figure, and to pin the KOSPI-vs-KOSDAQ / cash-vs-futures / intraday-vs-close traps that could produce exactly this sign flip.

**What is NOT contested, and is directionally decisive on its own:** retail sold **−₩3.392조 across 07-29 + 07-30** (computed). Retail was unambiguously the seller for two sessions running, regardless of how the foreign leg resolves.

### §3.1 — The rotation signature (this is the strongest independent evidence)

On 07-30, **전기전자 was the only major loser** while KOSPI fell just −1.23%: 의약품 +3.51%, 화학 +2.56%, 금속 +2.49%, 운송장비·부품 +2.19%, 보험 +1.96%, 부동산 +1.86% (T2).

**A genuine risk-off takes the whole tape down. This took one sector down and bid six others.** That is a **rotation signature, not a liquidation signature** — and it is the strongest argument that the semiconductor drawdown was **positioning-driven rather than a repricing of the AI thesis**. Today's move is that rotation unwinding violently.

⚠️ **Caveat that must not be smoothed:** we have sector **returns**, not sector **flows**. 전기전자 net-₩ by investor type was **NOT OBTAINED** for either day. Returns and flows are not interchangeable, and the rotation read would be much stronger with the flow decomposition.

---

## §4 — H3 TWO-PATH READING (I-2, escorted) + 🔴 A RE-SPEC PROBLEM

### §4.1 — The two paths point OPPOSITE ways, and the character has changed

| | **PATH 1 (oil)** | **PATH 2 (rates)** |
|---|---|---|
| Direction | **DOWN** ($90.74 → $89.03, −1.9%) | **UP** (10Y +6bp, 30Y +11bp) |
| Gate | **UN-BREACHED, −$5.97, 4th consecutive sub-95 settle** | n/a |
| Escalation | **DE-ESCALATING** — Saudi naval coalition, 40+ nations, transits **14/day** vs single-digits | Bear steepener **accelerating** |
| Implies for H3 | **WEAKER** | **STRONGER** |

Brent settle sequence: **$88.36 → $84.09 → $90.74 → $89.03** (T2 multi-outlet, press-settle basis per addendum #10).

Curve (T1 FRED, latest 07-29): 2Y **4.22**, 5Y **4.37**, 10Y **4.67**, 30Y **5.20**. Since 07-14: 30Y **+12bp** vs 2Y **+4bp** — **the long end doing 3.0× the front-end work**. FOMC day alone: 2Y −4bp, 30Y +11bp = **15bp of steepening in one session**. 2s30s **98bp**.

### §4.2 — 🔑 THE DISCRIMINATING OBSERVATION

**On 07-30 Brent fell 1.9% and the 30Y printed 5.20% — a 2007 high — on the same day.**

**Duration repriced on a day crude fell. That is not an oil story.** The $95 Brent gate may be **measuring the wrong variable**.

### §4.3 — Sept-odds: my 07-30 framing was mechanically wrong

The corpus records *"Sept odds FELL 80→54."* The verifier-grade resolution:

| Instrument | Value | Timing |
|---|---|---|
| CME — hike **BY** mid-Sept (cumulative, **includes July**) | **82.4%** | **pre**-FOMC |
| CME — hike **AT** the Sept meeting | **61.4%** (from 50.6% a month ago) | post-FOMC |
| Kalshi — 25bp hike | 53% | post-FOMC |

**These are different instruments.** The July meeting resolving to a hold **mechanically strips the July leg** out of the cumulative number. **The decline was arithmetic, not dovish repricing** — and September-*specific* odds actually **ROSE** (50.6% → 61.4%). This is another **L46 basis-class error**: I compared two figures on different bases and read a narrative into the difference. Booked as such.

### §4.4 — Non-Brent dashboard: 2/5 elevated → escalation review FIRES, with a caveat

| Channel | Reading | Threshold | Verdict |
|---|---|---|---|
| Brent-Dubai EFS | **UNREACHABLE** | negative | ❌ UNREADABLE |
| JKM | $21.43/MMBtu | >25 | NOT elevated |
| Hull war-risk | **7.5–10% of hull** (from 1–3% weeks ago) | >3% | ✅ **ELEVATED** |
| VLCC TD3C TCE | **$382,397/day** (+33.5% since 07-02) | rate-of-change | ✅ **ELEVATED** |
| EURJPY-EURKRW | not fetched | — | ❌ UNREADABLE |

**2-of-5 elevated → the I-2 rule "escalation review at ANY Brent level" FIRES.**
**⚠️ But the honest denominator is 3, not 5.** Two channels are dark, and **UNREADABLE ≠ not-elevated**. On readable channels the elevated share is **2 of 3 = 67%**. The rule was written assuming 5 readable inputs; it is being evaluated on 3.

**The dashboard CONTRADICTS the flat-crude read**, and this is the substantive finding: tanker rates +33.5% MTD and war-risk premiums at **12–40×** pre-hostilities levels say **the physical risk premium has NOT deflated** even as flat price has. The risk migrated into **freight and insurance**. For Korean industrials that is arguably *worse* than a Brent spike — **a landed-cost tax that Brent alone hides**, which is precisely the blind spot the EFS was designed to catch and precisely the channel we cannot read.

### §4.5 — 🔴 THE STRUCTURAL PROBLEM: are H1 and H3 the same hypothesis?

Warsh named **memory-chip prices** in the FOMC inflation discussion → 24h later Samsung guided memory shortage **through 2028** → Apple fell **6–8% after beating on every line** because of supply constraints Cook said he *cannot remedy*.

**That is one causal chain touching both hypotheses.** If the term-premium repricing is **memory-inflation-driven rather than oil-driven**, then H1 (AI-demand-intact) and H3 (macro/energy shock) are **not independent**, and assigning them independent weights **double-counts**.

**H3 RE-SPEC — I am registering this as a pre-committed question, not resolving it today:**
- **Q: Is H3 an OIL hypothesis, or a TERM-PREMIUM hypothesis that merely used oil as its transmission channel?**
- If **oil** → PATH 1 is actively falsifying it (4 sub-gate settles, de-escalation mechanism forming, transits recovering) and H3 should fall.
- If **term-premium** → PATH 2 is confirming it, and **the transmission channel has rotated from crude to memory**, in which case the $95 Brent gate is a dead instrument and must be replaced.

**✅ VERIFIER RETURNED — §3 RESOLVED, AND THE REWEIGHT EXECUTED (addendum #13).** The corpus figure was **REFUTED**: 10+ independent newsrooms confirm **+₩1.33조 net BUY** on 07-30 (zero sources for net-sell), and every refutation attempt failed — including an internal arithmetic-balance test a sign-inverted leg could not pass. **Two errors, not one:** the sign, AND an off-by-one date shift (session 4 was **07-29**, not 07-30). The corrected streak is **PEAK → COLLAPSE → REVERSE**: −3.28조 / −2.90조 / **−4.98조 (peak)** / **−0.079조 (= 1.6% of session 3)** / **+1.33조 (broken)**. "Persisting/accelerating" is false on the data; true DoD collapse into session 4 was **−98.4%**, not the −72% recorded. **Addendum #12's trigger was nonetheless VALIDLY met** on 07-24/27/28 (N=3) — what was false is the 07-30 *confirmation*, i.e. the corpus recorded an escalation on the session that was actually the reversal. **Origin of −₩1.25조 UNIDENTIFIED — routes to the INTAKE-BOUNDARY P0 as a live specimen.** Also verified: foreigners bought SK Hynix **+₩5,876억 INTO** its −5.64% session.

**H3 REWEIGHT EXECUTED — H1 54→60 / H2 11 / H3 35→29 (my model, addendum #13).** Both H3 escalation legs withdrew (flow refuted; oil un-breached 4th consecutive sub-95 settle with de-escalation forming). H1 up on aligned new evidence, not as residual. **Rule #18 counterweight preserved rather than absorbed: the rates leg is STRENGTHENING while I cut H3** — if the re-spec below resolves toward term-premium, this cut is wrong and H3 must be re-raised AND renamed. Cut executed anyway because a refuted input is a correction, not a judgment call.

**Original deferral note, superseded above:**

**H3 REWEIGHT: was DEFERRED at first pass.** Both registered inputs are unresolved — the oil leg says down, the KR-flow leg is **contested** (§3), and the independence question above would change *what the weight even means*. **Weights held at H1 54 / H2 11 / H3 35 (my model, unchanged).** Deferring a reweight when two of its three inputs are contested is the correct action, not indecision — and the 07-28 precedent (review fired, decision deferred one day, then executed cleanly) is the template.

---

## §5 — CATALYSTS: both JP prints are still AHEAD of us

**Neither has landed.** MURATA prints **14:00 JST**, KIOXIA **15:30 JST** (briefing 16:00). Verified against company IR calendars (T2). **No numbers invented.**

### §5.1 — 🔴 KIOXIA: an INPUT-layer failure graded BEFORE the print

Booked in full at `predictions/2026-07-02-KIOXIA-Q1FY27-earnings-prediction.md` (addendum). Summary:

| Line | Our point (band) | Company's **own** Q1 guide | Guide vs our ceiling |
|---|---|---|---|
| Revenue | ¥1.25tn (1.15–1.35) | **¥1.75tn** | **1.30× above** |
| Operating profit | ¥600bn (550–650) | **¥1.298–1.30tn** (non-GAAP) | **2.00× above** |
| Net profit | ~¥460bn (420–500) | **¥869bn** | **1.74× above** |

**Falsifier #1 ("Rev <¥1.10tn") was UNFIREABLE** — company guidance is **1.59× the falsifier line**. A falsifier public guidance had already made unreachable is decoration, and this **falsifier-design failure is more transferable than the estimate miss**.

**The confession:** the file's own note reads *"MUST re-pull consensus — current aggregator figures discarded as implausible."* **The discarded figures were the company's own guidance, rejected for being too large.** This is **B45 magnitude-conservatism operating inside a prediction file at the intake step** — the same family as the AMZN grade 24h earlier, caught one layer earlier.

**Basis discipline (L46): grade the REVENUE leg only.** OP/NI are non-GAAP-contaminated (and Bloomberg consensus ¥874.1bn sits −32.7% *below* the company's own guide, itself unresolved). Revenue carries no such ambiguity. **Also fixed: resolution date was 2026-08-07 vs the actual 07-31 print (B62).**

### §5.2 — MURATA: grading scaffold, actual column empty

| Item | Our prediction | FY27 guide straight-line | Q1 FY26 base | Actual |
|---|---|---|---|---|
| Revenue | **¥505bn** (490–520) | ¥490bn | ¥416,154m | *pending 14:00 JST* |
| Operating profit | **¥105bn** (95–115) | ¥95bn | ¥61,621m | *pending* |
| FY raise | **P=25%** | — | — | *pending* |

Implicit bar: our ¥505bn = **+21.4% YoY**, ¥105bn OP = **+70.4% YoY**. Grade against company-guide straight-line and the YoY base — **Q1-specific street consensus remains a genuine gap and must not be fabricated**.

**Auto-MLCC negative leg VERIFIED and WIDENED:** Mercedes China Q2 **98,600 units, −30% YoY** confirmed (T2), but the weakness is **cohort-wide** — German premium OEM China Q2 declines run **−30% to −41%** across VW/Mercedes/BMW/Porsche (Fortune, T2). **The thesis leg should be widened from Mercedes-specific to German-premium-cohort.**

### §5.3 — Both T+24h reaction bands: SUSPENDED, not graded

Both were written for crowded, post-run setups that **no longer exist**: KIOXIA **~−70%** from its 06-22 peak (including a −16% limit-down on a **$229m US patent jury verdict, 07-17** — a discrete non-thesis event), MURATA **~−42%**. Grading a reaction band against an inverted positioning setup measures nothing.

### §5.4 — SAMSUNG Q2: T3 → T1/T2 on all four items

| Claim | Verdict | Verified |
|---|---|---|
| Q2 OP ₩89.5조 | ✅ **CONFIRMED** | ₩89.49조 (Samsung Newsroom T1 + 뉴스와이어 T2) |
| +1,814% YoY | ✅ **CONFIRMED** | **+1,813.8%** |
| Shortage through 2028 | ✅ **CONFIRMED + STRENGTHENED** | 2027 shortage *intensifies*, persists into 2028 (conf call, T2 ×4) |
| **MX first-ever quarterly loss ~₩700bn** | ✅ **CONFIRMED** | rev ₩33.2조, **OP −₩0.7조** (뉴시스/전자신문/뉴데일리, T2 ×3) |

Group: revenue **₩171.5조** (+130% YoY), OPM **52%**. **DS OP ₩89.2조 of ₩89.5조 group OP = memory is ~99.7% of company profit.** Q2 ASPs: **DRAM +mid-40% QoQ, NAND +high-60% QoQ**. LTAs heading to **60–70% of total capacity**, 5-year deals with 5 big-tech customers.

Samsung's own stated cause for the MX loss: *"AI 서버 투자 확대로 모바일용 메모리 공급 부족과 가격 상승이 이어지면서 스마트폰 부품 원가 부담이 커졌다"* (T2).

**Mechanism note (Rule #9):** management asserts **no bypass exists on the supply side** — *"신규 팹 건설부터 웨이퍼 생산까지 3년 반 이상"*, a physics constraint rather than a demand forecast. The real bypasses are (a) China capacity (CXMT/YMTC) and (b) **demand destruction at the consumer end — which is already visible in the MX loss itself.**

---

## §6 — CROSS-CUTTING SIGNAL (explicitly NOT a triangulation promotion)

Three independent observations inside 48 hours, all pointing at memory-as-cost-input:

| Source | Segment | Datum |
|---|---|---|
| **Warsh / FOMC** | central bank | named **memory-chip prices** in the inflation discussion |
| **Samsung** | memory-and-storage | MX division **first-ever loss** from its *own* DS division's prices |
| **Apple** | consumer-AI / hardware | **−6 to −7.8% AH** after beating every line; Cook: *"very significant supply constraints with limited flexibility in the supply chain to remedy it"* |

**Per Workflow #3 / Critical Rule #6 this is a CROSS-SEGMENT cluster — it logs here as a cross-cutting signal and is NOT promoted to `triangulation.md`.** Three sources spanning three segments is not three sources within one segment, and the segment rule exists precisely to stop that conflation.

**What it does justify:** the **Samsung MX datum promotes to 🟢 HARD** as the first *intra-company* P&L proof of memory-as-cost-input. A vertically integrated firm capturing 100% of the memory upside **still could not shield its own handset division.** Every non-integrated OEM — Xiaomi, OPPO, vivo, Transsion, PC OEMs — is structurally worse off: they pay the input price without owning the fab.

**🔴 Apple is the most under-appreciated datum of the week.** Beat on revenue ($109.417B, +16%), iPhone +22%, profit +27% — and fell 6–8% **because supply, not demand, capped the guide**. That is memory scarcity showing up as a **revenue ceiling at the best-supplied hardware buyer on earth**. 🟡 DIRECTIONAL (T2, after-hours range unpinned).

---

## §7 — POSITION IMPLICATIONS (all user-gated; SYMMETRY RULE applied)

**SK Hynix / HYNIX:** **NO ACTION — user-gated** — gap closed to within 1.53pp of ADR-implied fair value, so the dislocation the conditional-add was waiting on has **mechanically closed at the open**; the 24%-of-move fade and the 07-30 full-round-trip precedent mean the entry level is not yet established. 🟡

**Samsung (tracked, not held):** **NO ACTION** — the +5.75pp residual overshoot plus a confirmed T1 print (₩89.5조, shortage-through-2028) makes this a fundamentals re-rating rather than gap-arb, but no entry reasoning is established. 🟡

**MURATA / SUMCO:** **NO ACTION** — both prints/interims still ahead (MURATA 14:00 JST today; SUMCO 08-06). The German-premium-cohort widening is a **negative** input to the MURATA package and is now on file ahead of the print rather than after it. 🟡

**KIOXIA:** **NO ACTION** — the pre-print grade is an *instrument* finding, not a position finding. Nothing about the input-layer failure changes the NAND thesis; Samsung's NAND **+high-60% QoQ** independently corroborates the contract-repricing leg we got *right*. Only our level was wrong. 🟡

**SYMMETRY RULE check (per the 07-30 codification):** §4.4's dashboard, §1.3's fade, and §3's contested flow all **argue against adding**. The rule requires answering with a verdict on the *existing* position, not just declining to add: **HOLD across the memory cohort — no trim.** No written falsifier in any held thesis fires on any of these — they are entry-timing and macro-transmission observations, not thesis conditions. Stated explicitly rather than left silent. 🟡

---

## §8 — WHAT THIS WAKE CHANGED, AND WHAT IT COULDN'T

**Resolved:** Seoul gap-close (closed + overshot, ADR was the right anchor) · 반대매매 07-28 print found after 3 days · leveraged-ETF measure T1-sourced with its contamination mechanism named · Samsung Q2 fully T1/T2 verified incl. the MX first-ever loss · KIOXIA input-layer failure graded pre-print · Sept-odds framing corrected (basis error, not dovish repricing) · three of my own anchors corrected.

**Deferred with reason:** H3 reweight (two of three inputs contested) · H1/H3 independence question (registered as a pre-committed re-spec) · both JP prints (still hours away).

**Standing instrument gaps — these recur and should stop being re-discovered each wake:**
1. **KOSPI200 futures basis + night-futures gap** — the two best *pre-open predictors*, both dark. Highest-value gap in the KR stack.
2. **Brent-Dubai EFS** — the one channel that discriminates "global oil calm" from "Asia-specific tightness," which is exactly the question our KR exposure turns on.
3. **전기전자 sector flows by investor type** — we have returns, not flows.
4. **Proxy blocking**: WebFetch returned HTTP 403 on the large majority of financial-press domains across two legs, plus KRX (POST/JS), Naver, Hankyung, Daum, Bloomberg, fnnews. **This structurally caps the harness at T2 for market data** and is an infrastructure problem, not a research problem.

**Falsifier for this artifact's central read:** if KOSPI closes red today after a +14.17% high — the 07-30 shape repeating — then §3's positioning-flush interpretation is wrong and the tape is distributing. That resolves in hours, on a public number.
