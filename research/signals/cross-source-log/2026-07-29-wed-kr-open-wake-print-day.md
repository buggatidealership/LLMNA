# 2026-07-29 WED — KR-OPEN WAKE (print day): SK Hynix Q2 = sole adjudicator; bounce open after CB#8

**WORKFLOW: KR-OPEN WAKE (W11 time-sensitive leg).** Sync clean (0 behind origin/main, W11 stale-branch check). Three Opus agents in flight at booking time: (A) SKHY Q2 print fetch (DART-first, Korean-native), (B) KR flows/auction/futures-basis + 반대매매, (C) H3 dashboard. §2+ appended on agent return.

**NO POSITION ACTION — user-gated. The conditional €3-5k add decision belongs to the operator after the print adjudication.**

## §1 TAPE AT 09:25 KST (T1-machine EODHD real-time ts=1785283500; every Δ computed vs the machine-verified 07-28 closes booked in `2026-07-28-tue-eod-legb-discovery-kospi-cb8-cxmt-duv-credit.md` §1 — vendor `previousClose` IGNORED)

| Instrument | Verified 07-28 close | 09:25 open | 09:25 last | Δ open (computed) | Δ last (computed) |
|---|---|---|---|---|---|
| KOSPI (KS11.INDX) | 6,023.66 | 6,089.11 | 6,137.31 | **+1.09%** | **+1.89%** |
| KOSDAQ (KQ11.INDX) | 705.85 (EOD-verified this morning) | 713.71 | 715.13 | **+1.11%** | **+1.31%** |
| SK Hynix (000660.KO) | 1,550,000 | 1,567,000 | **1,597,000** | **+1.10%** | **+3.03%** |
| Samsung (005930.KO) | 220,000 | 226,500 | 229,500 | **+2.95%** | **+4.32%** |

**Vendor prevClose defect N+1 (same split as 07-28):** index real-time feeds carry the T-1 (07-27) close as `previousClose` (KS11 6,755.75; KQ11 764.86) while single-stock feeds are correct (000660 / 005930 carry true 07-28 closes). Standing rule held: computed vs verified closes only.

## §1b Rates leg (T1-machine FRED DGS10, T+1 series lag)
4.60 (07-20) → 4.63 → 4.67 → **4.71 (07-23 peak)** → 4.69 (07-24) → **4.65 (07-27)** — falling into the FOMC; Tuesday's press level 4.62-4.63% (T2, booked 07-28 EOD artifact) extends the decline to ~4 sessions. **H3 Path A (rates-rising) is EASING on the machine series.**

*§2 pending agent returns (print figures, flows/반대매매/basis, H3 dashboard).*

## §2.1 H3 dashboard (agent C returned ~00:50Z) — ESCORTED READING, no auto-action

**Headline: the de-escalation trade broke overnight.** Brent is **+4% toward $88 in the Asian session** ([TradingEconomics](https://tradingeconomics.com/commodity/brent-crude-oil) T2 intraday, single-source level but arithmetically reconciled to the ICE settle basis: 84.09 × 1.04 = 87.45) on **fresh Iranian ballistic missiles at US forces (CENTCOM) + Saudi Eastern-Region oil-facility drone strikes for a second consecutive day** (T1/T2: [PBS](https://www.pbs.org/newshour/world/iran-launched-multiple-missiles-at-american-forces-u-s-military-says), CNN, CBC) — ending the multi-day lull the two sub-$95 settles were priced on.

| H3 leg | Reading | Basis | State |
|---|---|---|---|
| Brent vs $95 gate | settles $88.36 (Mon) / $84.09 (Tue, ±$0.80 outlet spread flagged); **overnight +4% → ~$87.5** | settle / intraday-Asian | **Still BELOW gate — but the un-breach review's premise is now CONTESTED; re-fetch at EU open before any reweight** |
| Rates (Path A) | 10Y **4.62%** Tue close (TE T2; consistent w/ FRED 4.65 07-27 machine series §1b) — ~4th down session | close | EASING — but the bond bid was built on the de-escalation narrative that just reversed |
| FOMC (today 14:00 ET) | hold base case **~62-68%**; hike odds roughly doubled in 2 weeks (~26%→36%); **Sept hike majority-priced 56-82%** (source spread wide — directional only); watch the VOTE SPLIT | multi-source, conflicting — flagged | Blackout, no fresh Fedspeak |
| Physical stress | war-risk **7.5-10% of hull** (stale 6-12d, pre-escalation → likely understates); JKM **$21.03-21.33/MMBtu +32.57% m/m** (stale ~8d); VLCC July UNREACHABLE (June: WS 276, ~$470k/day); Dubai-Brent EFS UNREACHABLE (paywalled) | mixed, stale | EXTREME and pre-dating the overnight events |
| Financial calm | VIX **18.43** (−1.29%), gold **$4,026.33** (−1.25%), both Tue closes (TE/USAGOLD T2) | close | CALM — positioned for a Fed hold |
| Oman mechanism | proposals EXCHANGED, not agreed; fees explicitly VOLUNTARY (Oman opposed imposed fees at IMO 07-09); Iran would not hold sole control ([Reuters/USNews](https://www.usnews.com/news/world/articles/2026-07-28/oman-presented-regional-mechanism-for-hormuz-to-iran-source-says) T2) | — | Earlier "transit-fee regime" framing SOFTENED — voluntary navigation-aid funding, not a toll |

**Escorted decomposition (my model):** the physical-calm divergence (booked 07-22) is now at its widest — physical instruments extreme and stale-to-the-upside, financial instruments priced for a hold, and the overnight tape repricing while Asia trades. **The H3 reweight review (addendum #11) stays OPEN and does NOT resolve this wake:** the settle-basis gate condition (two settles <$95) remains met, but acting on it hours before a FOMC decision and mid-reversal would be exactly the perishable-backdrop error booked as a lesson on 07-24. Decision point: the good-morning full synthesis, with a Brent re-fetch at European open. API crude draw −3.3mb (TE T2) noted.
**Maintenance flag (agent-surfaced):** `research/CLAUDE.md` now exceeds the single-read cap (~734 lines) — agents boot on a truncated harness file. → todo candidate at next pass.
