# 2026-08-05 (Wed) — KR-OPEN WAKE: the ETF-divergence test resolved today, and its answer flips on a single name

**Workflow:** KR-OPEN WAKE (scheduled Routine) — time-sensitive leg only. Full 3-leg scan / prose-deadline sweep / quota check #4 reserved for the operator's "good morning".
**Sync:** clean, 0 commits today, no prior operator wake. Full leg.
**Reading:** 00:05Z ≈ **09:05 KST**. **All prices INTRA-SESSION — not a session result until settlement (L42-b).**

---

## TL;DR

🔴 **The registered ETF-divergence test resolves TODAY and it cannot adjudicate.** The FSC single-stock leveraged-ETF rules take effect 2026-08-05. Spread reads **−2.57pp** on the 2-vs-2 basket and **+2.75pp** against the same single control used on 08-03/08-04. **The sign flips on one name.**

🔴 **EODHD index `previousClose` defect — 4th logged instance**, and the largest error yet: KOSDAQ would have read **+7.23%** against a true **+1.27%**, a **5.96pp** overstatement. Singles clean again.

🟢 **Sharp broad bounce.** KOSPI **+4.49%**, SK Hynix **+6.98%**, Samsung **+5.42%**, SEMCO **+14.09%**.

🟡 **Correction to my own 08-04 finding:** H3 instrument lag is **median 2 days today**, not 4. Yesterday's "blind by construction" reading was measured across a weekend and **overstated the structural component.**

---

## §1 — 🔴 VENDOR INDEX DEFECT, 4th LOGGED INSTANCE

| Symbol | vendor `previousClose` | verified 08-04 close | verdict |
|---|---|---|---|
| **KS11.INDX** | 6,257.45 | **6,358.95** | 🔴 **STALE — the 08-03 close** |
| **KQ11.INDX** | 737.35 | **780.72** | 🔴 **STALE — the 08-03 close** |
| 005930.KO | 240,000 | 240,000 | ✅ clean |
| 000660.KO | 1,577,000 | 1,577,000 | ✅ clean |
| 009150.KO | 1,185,000 | 1,185,000 | ✅ clean |
| 042700.KO | 203,000 | 203,000 | ✅ clean |

**Damage had it been read:**

| | TRUE (computed vs verified close) | vendor-implied | error |
|---|---|---|---|
| KOSPI | **+4.49%** | +6.18% | **+1.69pp** |
| **KOSDAQ** | **+1.27%** | +7.23% | 🔴 **+5.96pp** |

**Instance log: 07-28 · 07-31 · 08-04 · 08-05.** Three of the last four sessions, all INDEX-only, singles clean every time. **On 08-04 I called it "intermittent, not permanent" and booked a stub row predicting recurrence within 7 sessions** (`grading-log.md` § wake-call registrations). **It recurred on the next session.** That call resolves TRUE at N=1; leaving the row open until the 08-11 recheck as registered.

**KOSDAQ's +5.96pp is the largest error the defect has produced** — bigger in magnitude than the 08-04 sign inversion (5.22pp), though less dangerous because it doesn't cross zero.

## §2 — 🔴 THE ETF-DIVERGENCE TEST RESOLVES TODAY, AND IT CANNOT ADJUDICATE

The FSC single-stock leveraged-ETF rules are **effective today**. This is the pre-registered adjudicating session.

| Basket | Names | Mean |
|---|---|---|
| **Leveraged-ETF underlyings** | Samsung +5.42% · SK Hynix +6.98% | **+6.20%** |
| **Non-ETF control (2-name)** | Hanmi +3.45% · SEMCO **+14.09%** | **+8.77%** |
| | | **spread −2.57pp** |

**But SEMCO printed +14.09%, and it is the whole answer.** Against **Hanmi alone** — the identical single control used on 08-03 and 08-04 — the spread is **+2.75pp. The sign flips.**

**Full reading history:**

| Session | Spread | Control used |
|---|---|---|
| 08-03 | **−2.09pp** | Hanmi |
| 08-04 | **+2.09pp** | Hanmi |
| **08-05 (adjudicating)** | **−2.57pp** (2v2) **or +2.75pp** (vs Hanmi) | **depends on the choice** |

🔴 **The test is under-specified and I am recording it as UNRESOLVED rather than reading either number.** Three sessions have produced −2.09, +2.09, −2.57/+2.75 — a series whose sign alternates and whose final value depends on a basket-composition choice that was never fixed in advance. **A 2-vs-2 basket where one member can move 14% cannot separate a mechanical-flow effect from idiosyncratic news.**

**This is L54's failure class** (*a test whose branches are all on one side cannot adjudicate*) in a new form: here the branches are fine, but **the instrument's resolution is smaller than its noise.** The basket was never sized against the dispersion of its own members.

```
Blind-check on the ETF-divergence test: distinguishes "mechanical leveraged-ETF selling
drove the divergence" from "these four names moved for four unrelated reasons"
· reads on the mean spread between a 2-name ETF basket and a 2-name control
· GOES BLIND IF any single member has idiosyncratic news of a magnitude comparable to the
  effect being measured — which is the NORMAL case in this cohort, where B45 records ±5-12%
  single-day moves as routine. The effect sought (~2pp) is smaller than the cohort's own
  daily dispersion. This instrument could never have worked, and that was computable at
  registration from the base rate we already had on file.
```

**Booked as a to-do:** either re-specify with a control basket wide enough to survive one outlier (and pre-register the membership), or **retire the hypothesis as unmeasurable with available instruments.** Do not run a fourth reading of the current design.

**Honest note:** SEMCO's +14.09% has **no verified cause** in this wake — I did not identify news. It may be idiosyncratic or it may be the flow effect landing where I did not expect it. **Unverified either way**, and that uncertainty is exactly why the test cannot be read.

## §3 — 🟢 THE TAPE: broad bounce, but the memory large-caps have NOT round-tripped

| Name | now (09:05 KST) | vs 08-04 | opening auction | drift open→now | **vs 07-31 (pre-flush)** |
|---|---|---|---|---|---|
| **KOSPI** | 6,644.24 | **+4.49%** | *(index open untrusted)* | — | **+0.74%** |
| **KOSDAQ** | 790.67 | **+1.27%** | — | — | **+9.85%** |
| Samsung | 253,000 | **+5.42%** | +5.83% | −0.42pp | **−3.62%** |
| SK Hynix | 1,687,000 | **+6.98%** | +7.36% | −0.38pp | **−1.80%** |
| SEMCO | 1,352,000 | **+14.09%** | +14.01% | +0.08pp | **+18.39%** |
| Hanmi | 210,000 | **+3.45%** | +6.65% | 🔴 **−3.20pp** | **−2.10%** |

🔴 **The index has round-tripped the flush; the two large-cap memory names have not.** KOSPI sits **+0.74% above** its 07-31 pre-flush close while **Samsung is −3.62%** and **SK Hynix −1.80%** below theirs. The KOSPI recovery is being carried by something other than large-cap memory.

**Hanmi is the only name that faded materially** — opened +6.65%, now +3.45%, **−3.20pp of give-back** while the other three held their opening levels within 0.5pp. Noted, not interpreted.

**B45 discipline:** none of these magnitudes is flagged as extreme. +5-12% single-day moves are the documented cohort base rate. **SEMCO's +14.09% sits just outside that band** and is flagged for that reason alone, not as an exhaustion signal.

## §4 — H3 TWO-PATH CHECK, and a correction to yesterday's finding

| Instrument | Latest | Obs date | Lag | 5-session delta |
|---|---|---|---|---|
| UST 10Y | 4.70% | 2026-08-03 | **2d** | +0.050 |
| UST 2Y | 4.25% | 2026-08-03 | **2d** | −0.060 |
| 10y breakeven | 2.23% | 2026-08-04 | **1d** | +0.030 |
| HY OAS | 2.78% | 2026-08-03 | **2d** | −0.030 |
| JPY/USD | 159.16 | 2026-07-31 | 5d ⚠ | −4.550 |
| Brent spot FOB | 91.82 | 2026-07-27 | 9d ⚠ | +4.830 |

🟡 **CORRECTION TO MY OWN 08-04 FINDING.** Yesterday I computed *"five of six H3 instruments are ≥4 days stale, median lag 4 days"* and concluded the daily check is **"blind by construction."** Today: **median lag 2 days, and only 2 of 6 are ≥4 days.**

**The difference is the weekend.** Yesterday's reading was taken Tuesday against Friday-published data; today is Wednesday reading Monday. **The lag I measured was substantially calendar-driven, not purely structural**, and stating it as "by construction" overstated it. The rates complex (10Y/2Y/breakeven/OAS) runs **1–2 days** on a normal mid-week reading — usable. **JPY (5d) and Brent (9d) remain genuinely stale** and those two are structural.

**The to-do stands but is re-scoped:** the fix is not "the whole H3 set is blind" but **"JPY and Brent are blind; the rates legs are fine mid-week and degrade across weekends."** Amended in `todo.md`.

**Retired gate, reported for Routine-compliance only:** the Routine text still instructs *"Brent level vs 95."* Brent spot FOB **91.82 = BELOW 95** — but the reading is **9 days stale**, is **spot FOB not a settle** (L43), and **ADDENDUM #14 (2026-07-31) retired this gate entirely**, re-labelling H3 as *"Fed reaction-function credibility repricing — not memory prices, not oil."* **This is the second consecutive wake to execute a retired instruction because the Routine prompt has not been edited** — the amendment to-do is now **1 day overdue** and requires the operator's Routines UI.

**LIVE path — DGS10 4.70%, +5bp over 5 sessions, obs 08-03.** No escalation signal. **H1/H2/H3 weights HELD at 62 / 5 / 33** — and today that is *"nothing moved"* rather than 08-04's *"nothing could be seen."* Those are different statements and today the first one is true.

**Non-Brent dashboard (Dubai EFS / JKM / war-risk / Hormuz transits): NOT REACHABLE.** Unchanged standing gap.

## §5 — Discriminator inputs: UNREADABLE, not "not fired"

The Routine specifies these as the **re-based primary discriminators**. All four remain machine-unreachable per `meta/data-access.md`:

| Input | Status |
|---|---|
| KRX 투자자별 investor-type flows (foreign vs retail in electricals) | **UNREADABLE** — KRX POST/JS-walled |
| 반대매매 daily forced-liquidation stats | **UNREADABLE** — KOFIA portal 403s agents |
| KOSPI200 futures basis + overnight CME/EUREX gap | **UNREADABLE** — no route registered |
| KOFIA margin balance (policy-contaminated SECONDARY) | **UNREADABLE** |

🔴 **So the wake's own designated primary discriminators are unavailable for the fourth consecutive session, on the single most important date in the test's calendar.** The ETF-divergence test was designed to be adjudicated by *flow* data; it is being adjudicated by *price* data because that is all that is reachable. **That substitution is the root cause of §2's failure** — a flow hypothesis measured with a price instrument, which is this month's recurring failure class.

**Logged as UNREADABLE, not as "not fired."** Those are different states.

## §6 — What this wake changes

| | |
|---|---|
| **H1 / H2 / H3** | **62 / 5 / 33 — HELD.** Rates legs readable and flat; no escalation |
| **ETF-divergence hypothesis** | 🔴 **UNRESOLVED — instrument failed, not the hypothesis.** Do not run reading #4 on this design |
| **Vendor trust** | **4th index-defect instance in 5 sessions.** The verification step is load-bearing and must not be dropped |
| **Memory large-caps** | Bouncing hard intra-session but **still below pre-flush closes** while the index is above its own |
| **Today's calendar** | 🔴 **SanDisk Q4 FY26 prints 13:30 PT** — registered call unrevised; consensus sits above the guide top; T−1 addendum booked 08-04 · competitive surveillance pass #2 due (first weekly) · quota check #4 overdue 2d |

**NOTHING FIRES. NO POSITION ACTION (user-gated). No falsifier touched.** 🟡
