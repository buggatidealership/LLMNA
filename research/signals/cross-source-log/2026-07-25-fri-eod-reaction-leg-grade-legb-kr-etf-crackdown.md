# 2026-07-25 FRI EOD — reaction-leg GRADE (2 sessions late) + tape correction + Leg-B discovery: KR leveraged-ETF crackdown

**WORKFLOW: EOD CONDITIONAL SYNTHESIS (scheduled Routine, full leg — condition check found ZERO commits since 16:00Z, last was 13:07Z → evening quiet → lean discovery leg ran).** 1 Leg-B discovery agent (unanchored, ~123k tokens, 39 tool-uses) + orchestrator-run grade sweep on two independent market-data vendors. **Escorted-instrument discipline: every reading below is hand-decomposed and NOT acted on. NO POSITION ACTION (user-gated, Rule #8).**

**TL;DR:** The overdue T+24h reaction legs graded — I-5 TRUE, N-5 FALSE — and grading them surfaced a **temporal misattribution already cascaded into the corpus**: the "IBM −25%" in the twin-print grade is the July-14 pre-warning crash, not the July-22 print reaction (IBM actually closed **+0.43%** on the print). Correcting it made the underlying finding *stronger*: **4 of 5 cohort names had their reaction sign INVERT against their print content.** Separately, Leg B surfaced a genuinely unmodelled, dated flow risk to the largest held position — Korea halting single-stock leveraged ETFs on Samsung/SK Hynix, effective **Aug 5**.

---

## 1. GRADE SWEEP — I-5 / N-5 (resolution close was 07-23; graded today = **2 sessions late**)

Full grade + 3-layer diagnosis in `predictions/2026-07-22-IBM-NOW-GOOGL-twin-print-registrations.md`. Headline:

| Leg | P | Outcome | 07-22 → 07-23 close | Move |
|---|---|---|---|---|
| **I-5** IBM T+24h reaction POSITIVE | 0.55 | ✅ **TRUE** | $205.77 → $206.65 | **+0.43%** |
| **N-5** NOW T+24h reaction POSITIVE | 0.60 | ❌ **FALSE** | $95.46 → $91.94 | **−3.69%** |

**Scores (computed):** reaction legs Brier **0.2812**, 1/2 directional. Full 11-leg slate Brier **0.1344**, **10/11** directional (coinflip 0.25). Print-leg 0.1018 reproduces exactly on recomputation — no arithmetic defect in the original grade.

**Process miss, logged honestly:** the legs were pre-registered with an explicit T+24h resolution and the grade section said "pending 07-23 close." Nothing fired to collect them. Neither the 07-23 EOD close nor the 07-24 monthly-audit build picked them up; they surfaced only because tonight's Routine ran the deadline parser. **This is a receipts-hook-shaped gap** — a written promise ("pending 07-23 close") with no mechanism checking it — and it is exactly the class the Receipts Hook Phase 1 backlog item (G-07: "a header/status line is a PROMISE, not a receipt") exists to close. Routed there rather than logged as a one-off.

### Instrument (escorted)
EODHD daily EOD + Finnhub `/quote`, **two independent vendors agreeing to the cent** on every close used. Finnhub `/stock/profile2` confirmed instrument identity (`IBM` = International Business Machines Corp; `NOW` = ServiceNow Inc; both NYSE) — checked because NOW's absolute price level looked anomalous; it reconciles against ~1,031M shares outstanding / ~$102B market cap, so the level is internally consistent, not a wrong-instrument pull. `adjusted_close == close` across the window → no split/dividend adjustment in play. Print dates pinned via Finnhub earnings calendar: **all five cohort names AMC 2026-07-22**, so the T+24h session is the 07-23 close as pre-registered.

---

## 2. ⚠️ TAPE CORRECTION — "IBM −25%" was the wrong event (already cascaded; now fixed)

| Claim carried in corpus | Verified settled tape | Verdict |
|---|---|---|
| "IBM −25% (worst day on record, guide cut)" *in the print-reaction frame* | print reaction **+0.43%**; the −25.21% was **2026-07-14** (07-13 $290.23 → 07-14 $217.07, vol 67.4M ≈ 4.6× normal) | **TEMPORALLY MISATTRIBUTED — 8 sessions off** |
| "NOW +3.7% AH" | T+24h close **−3.69%** | **AH quote that fully reversed** |
| "GOOGL −5% AH" | **−7.13%** | direction right, **magnitude understated** |
| "TXN −3.6% AH" | **−3.13%** | acceptable |
| "TSLA sold off" | **−14.52%** | right, magnitude far larger than implied |

**Where the error did and did not live.** The −25% is recorded *correctly at its origin* (`2026-07-15-wed-morning-wake-3leg.md`: "−25.21%, −$69B, worst day on record", $217.05 vs tape $217.07) and in the `lessons.md` L-entry. The registration also used it correctly — I-5's P=0.55 reasoned from "bad news pre-released + −25% **reset bar**," i.e. treating it as the prior crash, which is why I-5 graded TRUE. **The defect entered only in the GRADE write-up's cohort line**, written ~23:35 UTC on print night from after-hours quotes, and from there into `companies/IBM/thesis.md`. Both are struck and corrected.

**Honest note on my own first read tonight:** I initially scored this as a possible fabricated number, because the tape showed no −25% session anywhere near the print. Grepping the corpus for the claim's origin — before writing it up — is what produced the correct, much narrower diagnosis. Retrieval-before-verdict, same shape as the L39 "unreachable ≠ fabricated" refinement.

**Direction of the correction: it strengthens the thesis it touches.** GOOGL's true move is worse than recorded, and IBM's inversion is sharper than recorded.

---

## 3. THE FINDING — content stopped predicting reaction sign (N=4 in one session, now computed)

| Name | Print content | T+24h reaction | Sign |
|---|---|---|---|
| IBM | FY26 guide **CUT** | **+0.43%** | **INVERTED** |
| NOW | beat-and-**RAISE** (2nd) | **−3.69%** | **INVERTED** |
| GOOGL | capex **RAISED**, beat | **−7.13%** | **INVERTED** |
| TXN | beat-and-**RAISE** | **−3.13%** | **INVERTED** |
| TSLA | EPS **MISS** | **−14.52%** | aligned |

**In this regime the print's CONTENT stopped predicting the reaction's SIGN — the BAR'S POSITION did.** IBM cut guidance and closed green because July-14 had already reset its bar; the three beat-and-raise names all fell because theirs had not.

This upgrades Principle #48/#49 capex-flip reflexivity from **N=2 inferred off after-hours quotes** (TSMC, GOOGL) to **N=4 measured off settled closes, in a single session.** Independent non-US corroboration the same week: **Disco fell −12.27% the session after a record H1 profit** (+42.5% YoY operating income) — same inversion, different continent, no US-capex narrative attached, which argues the mechanism is regime-wide rather than a US-story artifact.

**Standing dissent (Rule #18) — strongest case against:** one session is one session, and 07-22 carried at least three confounds (Alphabet's first-ever negative FCF, a Gemini-3.5 delay, and a broad risk-off tape). A cohort that all falls on a risk-off day is not proof that *content* stopped mattering — it may just be beta. **What survives that objection:** IBM. On a common-beta explanation IBM should have fallen with the rest; it rose, and it was the one name whose bar had been pre-reset. The bar-position variable explains the cross-section that beta cannot. It does not survive as strongly as N=4 makes it look — call it **N=4 observations, ~N=2 independent events** 🟡.

---

## 4. LEG-B DISCOVERY (unanchored, 8-12 item cap, structural filter)

### 4.1 🚨 NEW MECHANISM — Korea single-stock leveraged-ETF crackdown, effective **Aug 5**
Korea halted **new listings of single-stock leveraged ETFs tied to Samsung/SK Hynix** and raised the minimum deposit **₩10M → ₩30M (~$20.3K)**, effective **2026-08-05** ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/south-korea-to-halt-new-listings-of-single-stock-leveraged-etfs), T1/T2, measure dated 07-16) — against a backdrop where those products plus the two underlyings reportedly drove **~70% of KRX trading value** ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-08/samsung-sk-hynix-and-leveraged-etfs-drive-70-of-korea-trading), 07-08). Transmission visible 07-24 in Tokyo: **Disco −12.27%, Kioxia −9.49%, SoftBank −7.06%, Nikkei −2.73% to 64,611** (T2).

**Why this is a genuinely new harness object:** it is a **regulatory action on the trading wrapper**, not on fundamentals — a mechanism distinct from the ordinary macro-selloff class the harness already models, and it carries a **hard date**. **Bypass-route read (Rule #9):** the insulated route is holding the *underlying* rather than the leveraged product — which is how SKHY is held (37 ADS, unlevered, US-listed ADR outside the KRX product). Exposure is therefore to the **price** channel, not the **forced-unwind** channel.

**Falsifier check: NONE fired** on SKHY, MURATA, SUMCO. Rule #8 explicitly binds — this is not a sell signal. It is an argument against *adding* into the Aug-5 window, which matters only because a conditional add is already pre-gated on Jul-29.

### 4.2 Other structural items (no held-name falsifier contact)
- **Houthi ballistic missiles/drones struck Saudi Aramco refinery facilities at Jizan and Yanbu**, fires confirmed ([CNN](https://www.cnn.com/2026/07/25/world/live-news/iran-war-trump) T2, 07-25); Trump "close to a decision" on a "massive attack"; House passed a 2nd war-powers resolution 214-208 (non-binding), Senate version failed 47-49. Crude >$100 on 07-23, back to ~$90.47 on 07-24. **H3 gate note: a pullback to ~$90 puts Brent BELOW the $95 gate again** — the 07-24 SETTLE-CONFIRMED breach may be reverting to at-line. Flagged for the next wake to re-read on settle, not acted on.
- **US Section 122 universal 10% tariff expired 07-24 as legally required; USTR finalized a Section 301 replacement — two-tier 10%/12.5% on 60 economies, NO expiration date** ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-24/trump-tariffs-how-us-is-maintaining-import-duties-using-section-301) T1/T2). Temporary → durable authority. Structural, no modelled transmission yet.
- EU electricity/gas market rules in force 07-24 (T1, European Commission). Google fined €890M under the DMA for Search self-preferencing (07-23).
- **AMD–Cerebras inference split** (AMD prompt-processing / Cerebras token-generation) + Intel capex $18B→$20B + AMD/Intel China CPU volume deals (T2, ~48-72h — **flagged outside strict window**). The prefill/decode disaggregation is a **new U8/B47 efficiency-ledger watch-item** (🔴 SPECULATIVE, no verdict).
- **Penalized as restatement (correctly, per the anti-restatement rule):** Korea Jul 1-20 exports, semis **+180.6% YoY** ([Korea Herald](https://www.koreaherald.com/article/10814464) T2, 07-21) — reinforces an already 8-tier-convergent read; no new mechanism.

### 4.3 THE ABSENCE QUESTION — answered, and it is a real gap
**The US-Iran war as a standing macro-regime variable.** Five months running, direct strikes now on Saudi *refining* infrastructure, an escalation decision pending, Congress unable to bind it — and `sector/scenarios.md` has **no scenario** built around sustained Gulf conflict → oil floor → inflation pass-through → Fed interaction (FOMC 07-28/29) → risk appetite for high-multiple AI names. The harness has been tracking H3 as a *gate on a number* (Brent ≥$95) without a *scenario* behind it. **Booked as a scenario-construction gap, not a trade.** → `meta/todo.md`.

### 4.4 Leg-B quality note
Leg B independently reported GOOGL at **−7.1%** — matching my two-vendor computed −7.13% — which is third-party corroboration of §2's correction arrived at by a completely different route. It also correctly self-flagged the Alphabet item as **stale/outside the 24h window** and retained it only as proximate cause. Anti-decorative falsifier: **not tripped** (surfaced 1 new mechanism + 1 framework gap + 3 anomalies).

---

## 5. Signal-density check (Critical Rule #14)
Segment: **memory-and-storage** (SKHY/Samsung wrapper flows) + a cross-cutting market-structure signal. The ETF-crackdown item is **N=1** in-window and has no same-segment same-direction predecessor in the last 90 days (it is a market-structure event, not a demand/supply event). **Skip-rule invoked: logged only, no triangulation promotion.** Auditable here as required. The reaction-function-flip cluster is a different matter — it now has N=4 observations / ~N=2 independent events and is tracked under Principle #48/#49 rather than as a TC cluster.

## 6. Cascade executed (Critical Rule #10)
`companies/IBM/thesis.md` (misattribution corrected) · `companies/SKHY/thesis.md` (flip measured + Aug-5 flow risk) · `companies/NOW/thesis.md` (N-5 FALSE; fundamentals/reaction separation) · `companies/GOOG/thesis.md` (−5% → −7.13%) · `companies/MURATA/thesis.md` + `companies/SUMCO/thesis.md` (sentiment-only, no falsifier) · `companies/KIOXIA/thesis.md` + `companies/DISCO/thesis.md` (Tokyo selloff; Disco = the non-US inversion instance) · `predictions/2026-07-22-...-registrations.md` (grade) · `predictions/grading-log.md` · `predictions/lessons.md` (L42).

## 7. Position implications
**⬜ NO ACTION on every name — user-gated, and nothing here fires a falsifier.** 🟢 HARD on the tape corrections (two-vendor settled closes); 🟡 DIRECTIONAL on the regime read (~N=2 independent events); 🔴 SPECULATIVE on the Gulf-scenario gap and the AMD-Cerebras U8 watch-item. The **Jul-29 SK Hynix Q2 print remains the sole adjudicator** of the conditional €3-5k SKHY add; tonight's work makes that gate harder, not softer, and adds a dated Aug-5 overhang immediately behind it.
