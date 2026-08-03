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
