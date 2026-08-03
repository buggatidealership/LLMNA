# 2026-08-03 (Mon) — KR-OPEN WAKE: forced liquidation was 6× smaller than the deleveraging, 85.5% of the leverage is still on, and my own intraday hypothesis broke at N=6

**Workflow:** KR-OPEN WAKE (scheduled Routine) — time-sensitive leg only. Full 3-leg scan / prose-deadline sweep / quota check reserved for the operator's "good morning."
**Sync:** clean, not BEHIND. No prior operator wake today (only this Routine's 00:23Z resume). Full leg executed.
**Reading time:** ~09:25–09:35 KST (00:25–00:35 UTC). **Every price below is INTRA-SESSION and is not a session result until settlement (L42-b).**

---

## TL;DR

🟢 **The consensus that "deleveraging is largely complete" is not supported by the leverage data.** Margin loan balance fell **−14.5%** from its June record to ₩32.995조 (07-29) — meaning **85.5% of peak retail leverage was still outstanding** going into last week's crash-and-rip.

🟢 **Forced liquidation is an order of magnitude too small to be the mechanism.** All of July's 반대매매 totalled **2.32% of the margin book**; the book shrank 14.5%. **~6.2× more of the deleveraging was voluntary repayment than forced selling.** The "33조 빚투 청산 공포" framing describes the stock, not the flow.

🔴 **I formed an intraday hypothesis on N=4 and it broke at N=6.** Recorded below rather than quietly dropped.

🔴 **The Routine's own instrument list is one addendum stale** — it asks for the H3 Brent-$95 gate, which ADDENDUM #14 superseded on 07-31.

⚠️ **A WebSearch returned July-3 figures for "8월 3일" and I nearly ingested them.** Caught by cross-check against our own T1 tape.

---

## §1 — The tape (T1 EODHD real-time, escorted; INTRA-SESSION)

Verified before use: **all three prevCloses match our own T1 record for 07-31** (KOSPI 6,595.4502 ✓; SK Hynix 1,718,000 ✓; Samsung 262,500 ✓). **The prevClose corruption logged as defect N+2 on 07-31 did NOT reproduce today** — recorded as non-reproduction, *not* as a fix.

| Name | prevClose (07-31) | open | last (~09:25 KST) | chg% |
|---|---|---|---|---|
| **KOSPI** | 6,595.45 | 6,358.27 | 6,333–6,346 | **−3.78 to −3.97%** |
| **KOSDAQ** | 719.76 | 709.99 | 715.07 | **−0.65%** |
| Samsung Electronics | 262,500 | 248,000 | 245,000 | **−6.67%** |
| SK Hynix | 1,718,000 | 1,642,000 | 1,603,000 | **−6.69%** |
| Samsung Elec (pref) | 191,000 | 183,000 | 180,700 | −5.39% |
| Hanmi Semiconductor | 214,500 | 209,500 | 200,500 | −6.53% |
| **Samsung Electro-Mechanics** | 1,142,000 | 1,221,000 | 1,227,000 | **+7.44%** |
| SK Square | 1,038,000 | 1,070,000 | 1,041,000 | +0.29% |
| LG Electronics | 162,100 | 158,200 | 155,900 | −3.82% |

**Is the flush-repair intact? Computed:**

```
07-30 close (derived from the T1 +17.91%)  : 5,593.63
07-31 close (T1)                           : 6,595.45
now (~09:25 KST)                           : 6,333.49   = -3.97% vs 07-31
                                                        = +13.23% vs the 07-30 pre-rally close
share of the historic one-day gain given back: 26.1%
```

🟡 **Read:** a 26% give-back of the largest one-day gain in index history, with the index still **+13.2% above** where it sat before the rip. **Per B45 this is not "extreme"** — it is an ordinary retrace of an extraordinary move. The flush-repair holds.

### 🔴 A hypothesis I formed and broke, in the same reading

At N=4 names (Samsung −6.3%, SK Hynix −6.5%, SEMCO +3.8%, SK Square +0.5%) I formed: *"the decline is concentrated in the single-stock leveraged-ETF underlyings; names that locked limit-up alongside them but carry no leveraged ETF are up."* Mechanically clean, and it would have been a strong read two days before the 08-05 FSC rules bite.

**It broke at N=6.** **Hanmi Semiconductor −6.53%** carries no single-stock leveraged ETF and fell as hard as the majors; **Samsung Electronics preferred −5.39%** likewise. The actual split is **memory-complex down / non-memory up**, not ETF-underlying down / non-underlying up.

**Booking the process, not just the correction:** this is the same shape as L54 booked last night — a partition drawn across too few specimens, where every specimen happened to sit on one side. Two more names refuted it in under a minute. **Cost of checking: one API call. Cost of not checking: a wrong mechanism in a wake artifact two days before a regulatory event that would have appeared to confirm it.**

---

## §2 — 🟢 THE FINDING: leverage stock vs forced-liquidation flow

Inputs T2 (KOFIA via multi-source KR press: [한국일보](https://www.hankookilbo.com/news/article/A2026072916500001902), [서울경제](https://www.sedaily.com/article/20074468), [뉴시스](https://nwww.newsis.com/view/NISX20260731_0003731176), [NSP](https://www.nspna.com/news/?mode=view&newsid=822706)); index basis is our own T1.

### A) The stock — how much leverage actually came out?

| | |
|---|---|
| 신용거래융자 잔고, June record | **₩38.60조** |
| 신용거래융자 잔고, 07-29 | **₩32.995조** |
| change | **−14.5%** |
| KOSPI July MTD (our T1) | **−22%** |

**The basis point that makes this readable:** 신용거래융자 잔고 is **loan principal, not a market value.** It does not mark down with the index. So a −14.5% move **is** genuine repayment or liquidation — and **85.5% of peak leverage was still outstanding on 07-29**, going into the two circuit-breaker sessions and the record rip.

### B) The flow — how big was forced selling, really?

| | |
|---|---|
| 반대매매 07-30 (peak day) | ₩1,038억 — largest in 14 sessions |
| vs July daily average (₩383억) | **2.71×** |
| vs prior peak 07-09 (₩1,422억) | **−27.0%** — 07-30 did *not* exceed the 07-09 spike |
| peak-day forced sales ÷ margin book | **0.315%** |
| **ALL of July's forced sales ÷ margin book** | **2.32%** |

### C) The discriminator

```
July forced liquidation   = 2.32% of the margin book
Margin book actually fell = 14.5%
=> ~12.2pp was VOLUNTARY repayment, roughly 6.2x more voluntary than forced.
```

🟢 **Read — and it cuts against the consensus we ourselves helped form.** On 07-31 we recorded that Korean brokers had named *"디레버리징이 상당 부분 마무리됐다는 인식"* as a rally driver, and flagged that our positioning-flush thesis had become consensus and *"its edge is spent."* The leverage data says the consensus is **wrong on both halves**: deleveraging is **not** largely complete (85.5% still on), and the part that did happen was **overwhelmingly voluntary, not forced**. The "청산 공포" headline describes a large *stock* of debt while the *flow* through forced liquidation never got close to systemic.

**2nd order (P~60%):** voluntary deleveraging is discretionary and reverses on strength — which is a mechanism for the 07-31 rip that requires no change in demand fundamentals, and a mechanism for today's give-back that requires no bad news.
**3rd order (P~40%):** with 85.5% of leverage still outstanding into the **08-05 FSC tightening**, the marginal-seller overhang is intact, not cleared. This is the opposite of "overhang removed, buy the dip."

### Blind-check on this finding (Principle #51)

```
Blind-check: distinguishes "leverage was flushed" from "leverage is still on"
· reads on 신용거래융자 잔고 (loan principal) + 반대매매 daily flow
· goes blind if leverage migrated to instruments this stat does not cover —
  single-stock leveraged ETFs (₩12조 AUM per the 08-02 sweep), CFDs, or offshore
  swap exposure. Those carry embedded leverage that never appears in 신용거래융자,
  so the book could fall 14.5% while TOTAL system leverage was flat or higher.
  This instrument cannot see that, and the 05-27 leveraged-ETF launch means the
  migration channel demonstrably exists.
```

⚠️ **That blindness is live, not hypothetical.** The single-stock leveraged ETF products launched 2026-05-27 — i.e. **between** the June margin-balance record and the July crash. Read the −14.5% as *"margin-channel leverage fell 14.5%"*, **not** as *"system leverage fell 14.5%."*

---

## §3 — H3 two-path check (and the Routine is stale)

🔴 **The Routine asks for "Brent level vs 95." That gate was superseded on 07-31 by ADDENDUM #14**, which refuted the memory→term-premium hypothesis and **re-labelled H3 as "Fed reaction-function credibility repricing" — explicitly not memory prices, not oil.** Running the current spec instead, and flagging the drift.

| Instrument | Latest (T1 FRED) | Read |
|---|---|---|
| **UST 10Y** (`DGS10`) | **4.68%** (07-30) | **FLAT** — −0.01pp over 5 obs; range 4.61–4.69 |
| UST 2Y (`DGS2`) | 4.23% (07-30) | 2s10s = **+0.45pp** |
| **10y breakeven** (`T10YIE`) | **2.28%** (07-31) | **Still anchored** in the 2.22–2.28 band that refuted the memory-inflation channel |
| HY OAS (`BAMLH0A0HYM2`) | 2.84% (07-30) | 284bps; +3bps vs 07-27. Immaterial |
| Brent **spot** (`DCOILBRENTEU`) | 91.82 (07-27) | 94.12 → **105.32** (07-23) → 100.31 → 91.82 |

🟡 **H3 read: no escalation.** Breakevens anchored at the top of their refuted band; 10Y flat; credit unmoved. The Fed-credibility channel shows **nothing new** since 07-31. **Weights UNCHANGED at H1 60 / H2 11 / H3 29** (my model) — no instrument moved enough to justify a re-weight, and re-weighting on a flat reading would be motion.

⚠️ **Brent cannot adjudicate anything here (L43):** FRED serves **spot FOB**; the retired gate was defined on a **futures settle**. Different instruments. The 07-23 spot spike to **105.32** is recorded as history, not as a live gate read.

**Non-Brent dashboard (Dubai EFS / JKM / war-risk / Hormuz transits): NOT REACHABLE this wake.** No machine route; the escalation review still cannot run. Standing gap, unchanged.

---

## §4 — ⚠️ INTAKE CATCH: a July-3 article returned for "8월 3일"

A Korean-language search for today's opening flows returned a confident summary: *"코스피는 7739.75에 개장… 오전 9시 20분 기준 7603.97… 외국인 7736억원 순매도, 개인 6729억원 순매수, 기관 584억원 순매수."*

**Rejected.** Our T1 tape has KOSPI opening at **6,358.27** — a **22% discrepancy**, and 7,739 does not reconcile with any figure in our record (07-31 close 6,595.45). The lead source in the result set is dated **2026/07/03**. The summary silently re-attributed **July 3** figures to **August 3**.

**Caught only because we had an independent T1 tape to check against.** This is the same failure class as the unidentified −₩1.25조 foreign-flow figure on 07-31 and is now **specimen #5 for the open INTAKE-BOUNDARY P0**. The flow figures were internally plausible — they even fail to sum to zero in the normal way, which is *correct* behaviour for investor-type data and would have passed a sanity check.

**⇒ The 투자자별 (investor-type) flow discriminator is DATA-GAPPED for 08-03 at this hour.** KRX `data.krx.co.kr` needs POST/JS; press flow prints land mid-morning and at close. Not invented. Re-attempt at the operator's "good morning" or the close.

**Unverified datum surfaced, recorded but NOT ingested:** a T3 source claims 연기금 (national pension) took ~₩40조 in valuation losses and was expected to hold a sell position **at least through August**. If true this is a material supply overhang orthogonal to retail leverage. **T3, single-source, no date anchor on the expectation — needs verification before any use.**

---

## §5 — What this wake changes

**Nothing fires. No position action (user-gated).**

| Item | Status |
|---|---|
| H1/H2/H3 weights | **UNCHANGED 60 / 11 / 29** — no instrument moved materially |
| Flush-repair | **INTACT** — index +13.2% above the pre-rally close after giving back 26% of the historic gain |
| "Deleveraging largely complete" consensus | 🔴 **UNSUPPORTED** — 85.5% of peak margin leverage still on at 07-29; forced selling was 2.32% of the book for all of July |
| KOSPI vs KOSDAQ | −3.9% vs −0.7% — the give-back is **large-cap memory-specific**, not a market-wide risk event |
| 08-05 FSC tightening | Now lands with the leverage overhang **intact**, not cleared |

**Held names:** no KR-listed positions directly affected this session. **MURATA / SUMCO** unchanged from last night's FX cascade — the MOF intervention-disclosure window **opens today** and runs to 08-07; SUMCO's Q2 interim on 08-06 sits inside it.

**Reserved for the operator's "good morning":** full 3-leg scan · prose-deadline sweep · **quota check #4 and the P0 FORCED BINARY it must record (now 6 days overdue)** · KIOXIA + MURATA T+24h reads · 반대매매 07-31 print · investor-type flows at the close.
