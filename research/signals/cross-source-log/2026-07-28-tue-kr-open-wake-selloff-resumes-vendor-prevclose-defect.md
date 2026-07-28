# 2026-07-28 TUE — KR-OPEN WAKE: the selloff RESUMED (KOSPI −5.40%, SKHY −8.54%), a vendor prevClose defect caught at intake, and the H3 oil gate is DATA-GAPPED for a second session

**WORKFLOW: KR-OPEN WAKE (scheduled Routine, time-sensitive leg of `meta/good-morning-protocol.md`). Escorted-instrument discipline — every reading below is hand-decomposed and NOT acted on. NO POSITION ACTION (user-gated, Rule #8). Full 3-leg scan, prose-deadline sweep and quota check held for the user's "good morning."**

**Session state at fire:** UTC 2026-07-28 00:24, KST 09:24 Tue — KRX ~24 min in. Repo verified `behind: 0 / ahead: 0`, `is-shallow: false` (checked, not read off the banner). Today's only commit is my own 00:00 spillover from last night, not user-driven evening work ⇒ **full time-sensitive leg, not increment-only.**

---

## 1. ⚠️ INTAKE CATCH FIRST — the vendor's own change_p is wrong on the indices

**EODHD real-time INDEX feeds are carrying a STALE `previousClose` (Friday 07-24), while the single-stock feeds carry the correct Monday 07-27 close.** Caught because I printed `previousClose` explicitly rather than reading `change_p` — the direct consequence of L44b, booked yesterday.

| Instrument | Tick 00:05Z | Vendor prevClose | **TRUE 07-27 close** | Vendor `change_p` | **TRUE %** | Error |
|---|---|---|---|---|---|---|
| KOSPI | 6,390.68 | 6,690.62 ⚠️ stale | **6,755.75** | −4.48% | **−5.40%** | −0.92pp |
| KOSDAQ | 737.71 | 748.22 ⚠️ stale | **764.86** | −1.40% | **−3.55%** | **−2.14pp** |
| SK Hynix | ₩1,661,000 | 1,816,000 ✅ | 1,816,000 | −8.54% | −8.54% | — |
| Samsung | ₩239,250 | 254,000 ✅ | 254,000 | −5.81% | −5.81% | — |
| SK Telecom | ₩91,700 | 97,900 ✅ | 97,900 | −6.33% | −6.33% | — |

**Had I taken `change_p` at face value I would have under-reported the KOSDAQ decline by more than half.** Every figure below is computed from close-to-tick, not read off a vendor field.

**⚠️ BASIS LABEL, stated once and binding: these are INTRADAY TICKS at 00:05Z (09:05 KST), NOT opening-auction prints and NOT closes.** Yesterday's error was labelling exactly this kind of tick an "open" and feeding it a metric defined on the auction. Today's auction print is not yet in the EOD record; **no retracement or open-based metric is computed here.** The settled read comes at the close.

## 2. THE TAPE — the bounce failed and the selloff resumed

| Instrument | Thu 07-23 close | Fri 07-24 | Mon 07-27 | **Tue tick** | **Thu→now** |
|---|---|---|---|---|---|
| KOSPI | 7,096.89 | −5.72% | +0.97% | **−5.40%** | **−9.95%** |
| **SK Hynix** | ₩1,919,000 | −8.34% | +3.24% | **−8.54%** | **−13.44%** |
| Samsung | ₩270,000 | −7.59% | +1.80% | **−5.81%** | **−11.39%** |
| SK Telecom | ₩99,500 | +0.50% | −2.10% | **−6.33%** | **−7.84%** |

**Monday's green close is fully given back and then some.** Yesterday I withdrew a "weak bounce" read and replaced it with "violent two-way reversal, closed green." **Today re-frames Monday again: it was a failed bounce inside a two-day decline, not a recovery.** The corrected Monday tape — gap up to the high, sell through Friday's close to a *new low*, close green — reads in hindsight as distribution into strength, which is exactly what §6.4 of the 07-27 artifact said the single-name shape was.

### Principle #41 cohort-decoupling diagnostic (computed)

| Name | Tue move | vs KOSPI −5.40% | Verdict |
|---|---|---|---|
| **SK Hynix** | **−8.54%** | **−3.13pp** | ⚠️ **IDIOSYNCRATIC component present** |
| Samsung | −5.81% | −0.40pp | systemic — moving with the index |
| SK Telecom | −6.33% | −0.93pp | mostly systemic |

**SK Hynix is the only name with a material idiosyncratic decline, and it is 48 hours from its print.** 🟡

**Magnitude discipline (B45, binding until 2026-09-12):** −8.54% sits **inside** the regime base rate — the empirical cohort shows single-day moves of ±5-12% are routine, multiple times per week. **I am therefore NOT flagging the magnitude as extreme.** What is notable is not size but (a) direction after a failed bounce, (b) the −3.13pp idiosyncratic component, (c) the proximity to a pre-registered decision gate.

## 3. H3 TWO-PATH CHECK

### 3.1 Rates leg — ✅ yesterday's DATA GAP is CLOSED

FRED `DGS10` (T1) has now published **2026-07-24 = 4.69%**, the observation that was missing yesterday.

| 07-17 | 07-20 | 07-21 | 07-22 | 07-23 | 07-24 |
|---|---|---|---|---|---|
| 4.55% | 4.60% | 4.63% | 4.67% | **4.71%** | **4.69%** |

**5-session delta 07-17 → 07-24 = +14bp (computed).** Path B requires 10Y **falling ≥15bp/5d** ⇒ **NOT MET**. **Path A MET.** Clean discrimination, no judgement call.

**One detail worth carrying:** 07-23 → 07-24 is **−2bp**, the first down day of the window. A single down day does not approach the −15bp threshold, but the sign flipped and the Friday rates print is now on file rather than gapped.

### 3.2 Oil leg — 🚨 STILL DATA-GAPPED, second consecutive session, and here is why

**A keyed Brent route DOES exist and I did not have it yesterday: FRED `DCOILBRENTEU`.** But it cannot adjudicate this gate, for two independent reasons:

| Problem | Detail |
|---|---|
| **Basis mismatch** | `DCOILBRENTEU` is **Brent Europe SPOT FOB**. The house gate is defined on a **futures SETTLE**. Different instruments — the L43 rule forbids substituting one for the other |
| **Lag** | Latest observation is **2026-07-20 ($86.99)** — roughly six business days stale. It says nothing about 07-27 or 07-28 |

**⚠️ A tension to carry rather than resolve:** FRED Brent **spot** ran $81.23 (07-16) → $85.01 (07-17) → $86.99 (07-20), while the corpus carries **Brent futures SETTLE $96.78 on 07-24** (T2 ×3 outlets). Getting from one to the other implies roughly **+11% in four sessions** — plausible given the reported run to $100 at the conflict peak, but **the two series are not interchangeable and I am not reconciling them by assumption.** Flagged for the next clean adjudication.

**⇒ The H3 de-escalation trigger (Brent settle < $95) remains UNADJUDICATED. The gate stays open. H3 weights unmoved: H1 60 / H2 12 / H3 28.**

**Harness finding worth recording:** the commodities gap in `meta/data-access.md` is **partially closed** — FRED serves named Brent and WTI daily series on a spot-FOB basis with ~6 business days of lag. **Useful retrospectively, never for a same-day gate.** Recorded so the next session does not re-derive it.

### 3.3 USDKRW — and the basis question the audit raised is now live

EODHD `KRW.FOREX` daily bars: 07-24 **1,459.57** → 07-27 **1,465.07** → 07-28 **1,465.32**. Won weakening modestly off Friday.

**⚠️ Basis flag, unresolved:** this is a **24h/UTC bar**, not the Seoul 15:30 close. The fresh-session audit reported these can differ materially (its claim: the 07-24 −1.09% was the UTC bar while the Seoul close was ~flat). **That question is on the P0 verify-or-kill list and is NOT settled**, so the Path-B FX cluster input is carried as 🟡 basis-uncertain rather than used as a discriminator.

## 4. 🚨 THE INSTRUMENTS THE ROUTINE ASKED FOR AND I CANNOT READ

The Routine specifies the **re-based KR discriminator inputs** as the FIRST fetch. I have **no keyed route to any of them**:

| Instrument | Purpose | Status |
|---|---|---|
| **KRX 투자자별 investor-type flows** (foreign vs retail in electricals) | **The pre-registered escalation trigger: foreign net-sell ≥3 consecutive KR sessions** | ❌ **NO ROUTE** |
| 반대매매 (forced-liquidation) daily stats | Retail-leverage unwind read | ❌ NO ROUTE |
| KOSPI200 futures basis + overnight CME/EUREX gap | Was the decline gapped-in or sold in-session | ❌ NO ROUTE |
| KOFIA margin balance | Policy-contaminated SECONDARY | ❌ NO ROUTE |
| Dubai EFS / JKM / war-risk premia | Non-Brent oil dashboard (2-of-5 escalation review) | ❌ NO ROUTE |

**This is the load-bearing gap of the entire wake, and it is worth stating plainly: the escalation trigger cannot be read.** 07-24 was foreign-net-sell session 1 (~₩3.28조, on file). Whether 07-27 and 07-28 are sessions 2 and 3 — which would **fire the pre-registered escalation** — is **unknown to this harness**. A −5.40% index session with an idiosyncratic memory component is exactly the tape where that trigger matters most, and it is precisely where the instrument is blind.

**Escalation status: UNREADABLE, not "not fired."** Those are different, and recording it as the former is the honest entry. Routed to `meta/data-access.md` as a named gap with a KRX/ECOS route as the fix.

## 5. ESCORTED DECOMPOSITION — what could be driving this (hypotheses, NOT attribution)

**I have no attribution for the selloff.** Holding candidates in parallel rather than collapsing to a narrative *(all weights my model, none research-verified for today's session)*:

- **H1 (P~35%, my model) — Pre-print de-risking + the reaction-function regime.** Six settled-close instances now show good news punished (IBM, NOW, GOOGL, TXN, SK Telecom, Intel). Positioning ahead of Wednesday's SK Hynix print in a tape that has punished six consecutive beats is rational. Fits the SKHY idiosyncratic −3.13pp.
- **H2 (P~30%, my model) — FOMC front-run.** The 07-28/29 meeting begins today, with roughly a 25% market-implied probability of a **HIKE** rather than a cut. A rates-driven risk-off would hit high-multiple Asian tech first and would be **systemic**, which fits Samsung's −0.40pp relative but not SKHY's gap.
- **H3 (P~20%, my model) — The 07-31 leveraged-ETF measure.** Deleveraging ahead of the Friday effective date in the two named underlyings. Predicts exactly the observed shape — both underlyings down hard, SKHY worst — but should show up in 반대매매 and investor-type flows, **which I cannot read.**
- **H4 (P~15%, my model) — Continuation of Monday's US rotation out of AI infrastructure** (Intel −7.9% on a beat, AMD −7.3%, Micron −5%), transmitting to Asia overnight.

**These are not exclusive and the weights are soft.** H1 and H3 both predict the SKHY idiosyncratic component; H2 and H4 predict the systemic component. **The discriminator between them is the investor-type flow data — the one thing I cannot fetch.**

## 6. FALSIFIER CHECK — and Rule #8 is doing exactly the work it was written for

| Falsifier | Fires? | Why |
|---|---|---|
| #1 GP-bridge sign test = CRACK (GM↓ **and** ASP↓ at a print) | ❌ | **There is no print yet.** Wednesday 07-29 is the test |
| #2 AI-tier order cuts reaching HBM | ❌ | No evidence today |
| #3 CXMT relief-valve (capacity **+** Tier-1 AI qualification) | ❌ | Verified yesterday: capacity leg advanced, AI-qual leg unmet |
| #4 Funding-shock node (tell #7 Moody's-Oracle) | ❌ | Verified yesterday: no Moody's action in July 2026 |

**NO FALSIFIER FIRES. A −13.44% two-day decline is not a falsifier and must not be allowed to act as one** — that is Critical Rule #8 verbatim, and this is the exact situation it exists for. The written exit instrument for this position is the **GP-bridge sign test at the print**, not the price.

**Rule #18 — the strongest case AGAINST that framing, stated rather than skipped:** a −3.13pp idiosyncratic decline 48 hours before a print can be information — informed positioning ahead of a bad number. If Wednesday's GP-bridge comes in CRACK, today's tape will look like it front-ran it. **That is a real possibility and I am not dismissing it.** But it is unfalsifiable *today*, it is indistinguishable from H3's mechanical-deleveraging explanation without the flow data, and pre-empting a pre-registered gate on a price move is precisely the behaviour the gate was pre-registered to prevent. **The correct action is to wait 48 hours, which is also the only action available.**

## 7. Position

**NO POSITION ACTION (user-gated, Rule #8). No falsifier fired.**

**The 2026-07-29 SK Hynix Q2 print remains the sole adjudicator of the conditional €3-5k SKHY add** — and today sharpens what to read: the **ASP leg of the GP-bridge** (against a contract path that decelerated from ~+60% to ~+15% QoQ), the **LTA prepayment/duration disclosure**, and — new from last night — any **capex commentary implying a US front-end fab commitment** (Intel Ohio).

**Carried to the user's "good morning":** full 3-leg scan, prose-deadline sweep, quota check. **Carried as open:** the H3 oil settle adjudication (2nd session gapped); the USDKRW basis question (P0 verify-or-kill); the KRX flow-data route (escalation trigger unreadable).
