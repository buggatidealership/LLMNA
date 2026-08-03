# 2026-08-03 (Mon) — EOD: Korean memory fell 8.8% while US memory rose, on the same day. That is a 12.18pp spread and it settles what July was about.

**Workflow:** EOD CONDITIONAL SYNTHESIS → FULL PATH (condition computed: zero commits since 16:00Z; all of today's work landed 00:30–09:37Z; last session activity 14:38Z).
**Legs:** tape (T1, both closes settled) · grade sweep · ONE Leg-B unanchored agent · docket close.

---

## TL;DR

🟢 **A 12.18pp same-day spread between Korean and US memory settles the causation question.** Samsung **−8.76%** and SK Hynix **−8.79%** while **MU +0.79%** and **SNDK +6.03%**. **If this were a memory-demand event, US memory could not be up.** Today's Korean move is positioning, leverage and regulation — not demand.

🟢 **KOSPI −5.12% vs KOSDAQ +2.44% — a 7.56pp large-vs-small split.** Not a market-wide risk event. A large-cap-memory event.

🟡 **The hypothesis I formed and refuted this morning came back on the PATH, not the level.** The two single-stock-leveraged-ETF underlyings fell a further **−2.09pp** from 09:25 KST to the close, while the non-ETF memory name **recovered +0.94pp** — a **3.03pp divergence inside the memory complex in one session**, two days before the FSC rules bite.

🔴 **MPWR has round-tripped its entire print.** From the pre-print close it is **+2.14%** — it retained **0.1%** of the +19.15% intraday peak gain.

---

## §1 — The tape (T1, both sessions settled)

**Instrument discipline:** EODHD index `open`/`low` remain corrupt (defect N+2). Every `previousClose` below was verified against our own T1 record for 07-31 before use, and all matched. US figures are Finnhub, settled 20:00Z = 16:00 ET.

| Korea (close 2026-08-03) | prevClose | close | chg |
|---|---|---|---|
| **KOSPI** | 6,595.45 | 6,257.45 | **−5.12%** |
| **KOSDAQ** | 719.76 | 737.35 | **+2.44%** |
| Samsung Electronics | 262,500 | 239,500 | **−8.76%** |
| SK Hynix | 1,718,000 | 1,567,000 | **−8.79%** |
| Hanmi Semiconductor | 214,500 | 202,500 | −5.59% |
| Samsung Electro-Mechanics | 1,142,000 | 1,181,000 | **+3.42%** |

| US (close 2026-08-03) | chg |
|---|---|
| QQQ | **+1.76%** · SPY +1.42% |
| SMH +0.91% · SOXX +0.55% | |
| **MU** | **+0.79%** |
| **SNDK** | **+6.03%** |
| NVDA +2.93% · AMD +1.78% · AVGO +0.76% | |
| BE +6.08% · VST +5.23% · CEG +4.17% | |
| **MPWR** | **−5.73%** |

## §2 — 🟢 THE FINDING: a 12.18pp same-day decoupling

```
Samsung / SK Hynix mean : −8.77%
MU / SNDK mean          : +3.41%
SAME-DAY SPREAD         :  12.18pp
```

**This is the cleanest natural experiment the harness has had on the July question.** Korean and US memory names are exposed to the *same* end-demand, the *same* HBM cycle, the *same* hyperscaler capex. They differ in **who owns them and how**.

**1st order (P>80%)** — today's Korean decline is not a demand event. Demand cannot fall 8.8% in Seoul and rise 6% in New York on the same calendar day.
**2nd order (P~60%)** — it is therefore ownership-structural: forced or discretionary selling in a specific investor base. That is consistent with this morning's leverage computation — **85.5% of peak Korean margin debt was still outstanding at 07-29**, so the marginal-seller overhang was never cleared.
**3rd order (P~40%)** — **the "AI top is in" reading (H2) loses its best recent evidence.** July's Korean crash was the single most-cited data point for it, and the US tape today declines to confirm. Knock-on beneficiary: the H1 unwind-inside-intact-demand read.
**4th order (P~20%)** — if Korea keeps de-rating on domestic mechanics while US memory holds, the KRX-listed complex cheapens on a *non-fundamental* basis — which is where the ADR/local spread becomes the instrument worth watching, not the index.

🟡 **Weights (my model): H1 60→65 / H2 11→8 / H3 29→27.** Moved on one clean session, not re-based — a single day's decoupling is strong evidence about *mechanism* and weak evidence about *level*.

## §3 — 🟡 The path revived a hypothesis the level had refuted

This morning at 09:25 KST I formed, then broke at N=6, the claim that the decline was concentrated in the single-stock-leveraged-ETF underlyings. It broke because Hanmi (no ETF) fell as hard as the majors.

**The close says the level was the wrong measurement. The path is the discriminator:**

| | 09:25 KST | close | path |
|---|---|---|---|
| Samsung *(ETF underlying)* | −6.67% | −8.76% | **−2.09pp** |
| SK Hynix *(ETF underlying)* | −6.69% | −8.79% | **−2.10pp** |
| Hanmi *(no ETF)* | −6.53% | −5.59% | **+0.94pp** |
| SEMCO *(no ETF)* | +7.44% | +3.42% | −4.02pp |

**Everything memory-adjacent gapped down together at the open. Over the session the two ETF underlyings fell a further ~2.1pp while the non-ETF memory name recovered ~0.9pp — a 3.03pp divergence inside one session.**

**The methodological point, which is worth more than the finding:** a level snapshot and a path measure different things, and I refuted a correct hypothesis this morning by testing it against the wrong one. **Opening prints are contaminated by the overnight gap — they measure yesterday's news, not today's flow.** Same instrument-validity class as everything else this week: real mechanism, wrong measurement.

**Registered as a forward test rather than banked:** the FSC single-stock-leveraged-ETF tightening takes effect **2026-08-05**. If the ETF-underlying mechanism is real, that divergence should compress after 08-05.

```
Blind-check: distinguishes "ETF-mechanical selling" from "large-cap memory selling"
· reads on the intra-session path spread between ETF underlyings and non-ETF memory peers
· goes blind if the ETF underlyings are ALSO the two largest index weights — which they
  are. Index-level flows (futures, passive redemptions) hit exactly the same two names
  through a completely different channel, and this instrument cannot separate them.
  N=1 session. Do not treat as established.
```

## §4 — MPWR has given the whole print back

| | |
|---|---|
| Pre-print close (07-30) | $1,316.18 |
| Print reaction close (07-31) | $1,426.03 (**+8.35%**) |
| Intraday peak (07-31) | $1,568.21 (+19.15%) |
| **Close 08-03** | **$1,344.37 (−5.73%)** |
| **Cumulative vs pre-print** | **+2.14%** |
| **Retained of the peak gain** | **0.1%** |

🟡 A record quarter, a 45-point mid-year guidance-floor raise, a doubled buyback — and **effectively the entire move is gone within two sessions.** This strengthens rather than weakens the 07-31 read: *confirmed proof is not being paid for at these levels.* Booked as a **T+2 reaction datum on the new folder**, not as a thesis change. **The 08-01 falsifier is unaffected** — it keys to Enterprise Data growth and forward days-of-inventory at the Q3 print, neither of which a price move touches.

**Position implication: NO ACTION — no entry — WATCHLIST unchanged.** The share-gain-vs-end-market ambiguity remains the gate, and a cheaper price does not resolve it. 🟡

## §5 — Grade sweep: NIL, and the reason is documented

No prediction carries a 2026-08-03 resolution date. The KIOXIA and MURATA **T+24h reaction bands were formally SUSPENDED on 07-31** (booked: *"written for crowded post-run setups that no longer exist"*), with **L52 candidate — reaction legs do not survive regime breaks** — now at its third suspension of the week. **Nothing is owed; this is a clean nil, not a miss.**

**Instrument note:** EODHD returns `NA` on Tokyo tickers (`6981.T`, `3436.T`, `285A.T`), confirming the documented gap — *"EODHD tier lacks Tokyo; JP daily tape has no keyless machine route."* Non-reproduction of a route, not a new defect.

## §6 — What did NOT happen today

- **MOF FX intervention totals** — the disclosure window opened today and runs to 08-07. **Nothing confirmed at this hour.** Not asserted either way.
- **반대매매 07-31 print** — not obtained. Still owed.
- **투자자별 close-basis flows** — still owed (the morning attempt returned a July-3 article; specimen #5 for the INTAKE-BOUNDARY P0).

---

# §7 — DISCOVERY LEG (Leg B, unanchored) — and it corrected me twice on stale instruments

The sweep returned 12 items. Two of them **falsify readings I published earlier today**, and the root cause is the same in both: **FRED lags, and I treated its latest available value as "current" without stamping the lag.**

## 🔴 CORRECTION 1 — the MURATA yen tailwind has REVERSED, not extended (held name)

This morning's KR-open wake said: *"the FX tailwind Murata's FY raise leans on has EXTENDED, not faded"*, computed off FRED `DEXJPUS` **163.71**. That was the latest value FRED would serve — **dated 2026-07-24, one week stale.**

**What FRED serves now (T1, same series, re-pulled tonight):**

| date | JPY/USD |
|---|---|
| 2026-07-27 | 163.71 ← *the number I used this morning* |
| 2026-07-29 | 163.86 |
| **2026-07-30** | **159.47** |
| **2026-07-31** | **159.16** |
| 2026-08-03 | ~157 (T2, sweep — FRED not yet published) |

**The yen appreciated ~2.9% in two sessions on 07-30/07-31 — i.e. the intervention was already in the tape when I wrote that the tailwind had extended.** Against Murata's Q1 exit rate of ¥159.49, the yen is now **stronger**, not weaker.

**So the direction of the FX leg flips.** Murata's FY3/27 raise leans on a tailwind that is **reversing**, and the reversal is policy-driven with the MOF disclosure window open through 08-07.

🟡 **Still not a falsifier fire.** H3 on that thesis is *"MISSES — FX/yen/capacity execution drag"*, and nothing has missed. What changes is the **sign of the pressure**: this morning I said the tailwind was strengthening the raise; tonight it is weakening it. **Cascaded to `companies/MURATA/thesis.md`.**

## 🔴 CORRECTION 2 — H3 is escalating, and I marked it flat on the same stale-lag error

This morning: *"10Y 4.68% FLAT (−0.01pp over 5 obs)… H3 read: no escalation… weights UNCHANGED"*, then tonight I moved H3 **29→27**. Both used **`DGS10` 4.68% dated 07-30 as the latest**.

**FRED now serves 2026-07-31 = 4.75%.** The actual path: 4.61 (07-28) → 4.67 → 4.68 → **4.75** = **+14bp over four sessions, +7bp on the final day.** Not flat.

The sweep adds two corroborating T2 legs on the *same channel* ADDENDUM #14 re-specced H3 to (**Fed reaction-function credibility, not oil, not memory**):
- **FOMC held 3.50–3.75% on 07-29 with three hawkish dissents — the most divided vote since 2016**, and market-implied **September HIKE** odds rising through the week. *(Sources disagree 57% / 61% / 68% across dates — treat as a rising range, not a point.)*
- Fed officials explicitly naming **the AI buildout itself** as an inflation contributor — the same channel as Warsh's memory/logic-chip line we confirmed verbatim at T1 on 07-31.

🟡 **H3 revised: 27 → 33 (my model).** Reverting tonight's move and going further, because the instrument that said "flat" was reading a stale print. **H1 65→62 / H2 8→5 / H3 27→33.**

## 🟢 THE SYNTHESIS THE SWEEP EARNED: the capex reaction function is INVERTED BY LAYER

The sweep's strongest finding is a same-week, three-geography convergence of **"beat, then sold"**:

| Name | Print | Reaction | Framing in local press |
|---|---|---|---|
| **SK Hynix** | record profit, FY26 capex guided **+~50% to ≥$31B** | **−19% on the week** | *"concerns big tech such as Meta are building more data centers than they need"* (T2 Bloomberg) |
| **Kioxia** | Q1 net **+46x YoY**; Q2 guide **+31x** vs ~33x expected | sold | 「半導体スーパーサイクル論が後退」 (T1 Nikkei) |
| **TSMC** | strong print | **−2.06%** while TAIEX **+0.62%** | Wall Street *"reassessing AI-infrastructure investment profitability"* (T2 TW press) |

**But we hold a T1 counter-example from the same week, and it is ours: AMZN raised capex +10% to $220bn and closed +15.32%.** MSFT held capex while adding $132.5bn of leases and was not punished either.

**Both patterns are real, and the discriminator is which side of the trade you sit on:**

> **For a PAYER, capex is a demand signal about its own business. For a RECIPIENT, capex is future supply — i.e. a price risk to its own product.**
>
> **The same action carries opposite information content depending on layer.** Hyperscalers get rewarded for spending; memory and foundry suppliers get punished for expanding capacity to serve that spending.

**1st order (P>80%)** — "capex raise = punished" is FALSE as a general rule and TRUE within the supplier layer.
**2nd order (P~60%)** — this is the **recipient/payer taxonomy** (booked 07-31) showing up in the reaction function, not just in credit exposure. The taxonomy is doing more work than it was built for.
**3rd order (P~40%)** — **knock-on casualty: any thesis whose bull case rests on "supplier capex expansion confirms demand" is now reading a signal that the market has re-signed.** That framing appears across the equipment and materials cohort.
**4th order (P~20%)** — if the inversion holds, the supplier layer de-rates on exactly the evidence the payer layer re-rates on, and the spread between them widens without either being "wrong."

## 🟢 The owed 투자자별 flows arrived — and retail is absorbing the distribution

The morning wake recorded these as data-gapped (a search returned a July-3 article). The sweep obtained them:

- **Foreign + institutional combined: −₩4.77조 net sell** (T2 Seoul Economic Daily)
- **Foreign only: −₩2.84조** (T2 Hankook Ilbo)
- **Retail: +₩4.65조 net BUY**

⚠️ **The two sell figures disagree because of ATS/institutional inclusion — which is precisely the KRX-vs-KRX+NXT reconciliation we booked as UNRESOLVED on 07-31 and still is.** Recorded as a range, not a point.

🟢 **Read: retail absorbed institutional distribution, on a −8.8% day, with 85.5% of peak margin leverage still outstanding.** That is the same-day flow confirmation of this morning's stock-vs-flow computation, from an independent source. **Retail is not deleveraging. It is adding into the decline.**

## Items retained without cascade

- **ON Semiconductor −11.3%**, gross margin **−240bp to 37.6%**, EPS miss on a revenue beat. **Non-AI semis** (power/auto/industrial) margin compression — a genuinely uncorrelated read: the pressure is not confined to the AI complex.
- **Palantir** beat and raised FY26 to **$8.15–8.16bn** from $7.65–7.66bn, US commercial **+149% YoY**. **The application layer is strong in the same week the hardware layer is being punished.** That divergence is itself the signal, and it is the cleanest pro-H1 datum in the sweep.
- **Nikkei −0.94%** to 63,754.90, 1,059 decliners vs 462 advancers, **MURATA and Kioxia named decliners** on yen appreciation.
- **Mortgage 30Y ~6.65–6.93%** (sources disagree) — household credit tightening on the same inflation dynamic the Fed cites. Not the same trade as the AI-equity rally.
- **WARN layoffs** at Amazon/Walmart/FedEx alongside retail spending +3.5% YoY. ⚠️ Agent flagged per-name filing dates as **not independently pinned** — directional only.

## What the sweep did NOT get (explicit, per Leg-B spec)

- **MOF cumulative intervention total for August** — confirmed the intervention began 07-30 and continues; **no verified August aggregate exists yet** (MOF publishes daily data on a quarterly lag). Still owed.
- **Treasury refunding** — the event is 08-05. Correctly nothing to report.
- **Healthcare / industrials / transport dated to 08-03** — searched, nothing found. Agent flagged this as a **real blind spot, not a papered-over null.**

## The instrument lesson, which is worth more than either correction

**Both errors have one root cause: I used FRED's latest *available* value as if it were the latest *actual* value.** `DEXJPUS` and `DGS10` publish on a lag, and on 08-03 that lag spanned exactly the two sessions in which the yen moved 2.9% and the 10Y moved 7bp.

**Booked to `meta/data-access.md`.** The rule: **a lagging series must be stamped with its OBSERVATION date at the point of use, and any directional claim must state the gap between that date and today.** This is the same failure family as the FRED credit-window truncation found 08-02 — that one was blind to its *range*, this one blind to its *recency*. Same instrument, two different blindnesses, two days apart.
