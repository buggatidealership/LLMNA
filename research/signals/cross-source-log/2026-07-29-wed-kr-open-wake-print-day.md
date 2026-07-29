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

## §2.2 KR flows / structure (agent B returned ~01:05Z) — ESCORTED READINGS

### 🔴→🟢 THE PREVIOUSLY-UNREADABLE INSTRUMENT NOW READS — AND THE ESCALATION TRIGGER FIRED
**Foreign net-sell ladder (KOSPI, 🟢 T2-native multi-outlet):** Fri 07-24 **−₩3조2,852억** → Mon 07-27 **−₩2조9,039억** → Tue 07-28 **−₩4조9,664억** = **−₩11조1,555억 over 3 sessions**, independently confirmed as 3 consecutive ([fnnews 07-28](https://www.fnnews.com/news/202607281629568435), [etoday](https://www.etoday.co.kr/news/view/2608394)). **The pre-registered ≥3-session trigger (five-calls addendum #8) has FIRED — magnitude ACCELERATING (−3.29 → −2.90 → −4.97조), and session #4 is in progress intraday (foreign −₩4,100억 at 09:14 KST while the index is +2.00%).**
**Handling (escorted; my model):** the pre-registered consequence (H3 → ~35) is BOOKED AS PENDING, not applied here — because the H3 oil leg simultaneously un-breached (addendum #11) and the two registered triggers point OPPOSITE directions on the same weight. Joint resolution at the good-morning synthesis as already declared, now with both inputs on file. No position contact either way.
**Decomposition nuances (the tape's actual structure):**
- Foreign selling is **KOSPI-only**: on KOSDAQ foreigners net BOUGHT +₩869억 on CB day (etoday) — this is a large-cap/semis-targeted flow, not a Korea-exit.
- Retail absorbed ~103% of the 3-day foreign supply (+₩11조4,931억) — but funded from a **shrinking, unlevered cash pool**: 예탁금 ₩106조 (−₩34조 from 06-04), 미수금 ₩9,455억 first sub-₩1조 since April, 신용잔고 −15.43% from the 06-24 peak (₩38조6,328억 → ₩32조7,410억). **This is a liquidity-drain tape, NOT a margin-cascade tape — the leverage already came out** (🟡 KOFIA legs policy-contaminated per the standing flag: the 07-31 deposit hike is pre-emptively deleveraging the measured balances).
- 반대매매 daily print covering 07-24/27: NOT YET PUBLISHED (latest hard: 07-09 ₩1,422억, 10.2% of 미수금; July daily-avg ratio 3.68% = 3rd straight YTD-high month). Re-check at the covering print.

### SK HYNIX Q2 PRINTED PRE-MARKET (~07:50 KST) — preliminary figures (full adjudication in §2.3 on agent A return)
Rev **₩79조3,187억** (+257% YoY, +50.8% QoQ), OP **₩60조5,426억** (+557.2% YoY, +60.9% QoQ), OPM **76.3%** — both all-time records ([sedaily](https://www.sedaily.com/article/20073077), [zdnet 07:50](https://zdnet.co.kr/view/?no=20260729075046) T2). **BUT a consensus MISS: −5.2% rev / −4.9% OP vs the 22-broker 07-27 consensus (₩83조6,460억 / ₩63조6,594억).** Stock trades UP +3-4% on it regardless. ⚠️ Consensus-basis note for the GRADE: three consensus figures circulate (pre-registration ₩63.0조; Yonhap-14 ₩64.09조; 22-broker ₩63.66조) — the pre-registered P(beat)=75% call grades against its OWN stated basis, and OP ₩60.54조 misses ALL three → **the beat-call leg is WRONG on every basis; the point estimates (rev ₩88조/OP ₩68조) overshot actuals by +11.0%/+12.3% (computed)**. Full 3-layer GRADE deferred to agent A's detail (ASP/GP-bridge/LTA/HBM = the actual adjudication legs). Same morning: Mirae Asset CUT SKH PT to ₩2,800,000 on NAND price concern (T2).

### Structure/context (pinned)
- **Opening auction gapped UP** (+1.09%/+1.11%, §1 machine-confirmed); **no sidecar, no CB at the open** (🟡 absence-of-evidence). 09:14: KOSPI 6,144.11 +2.00%, 전기·전자 +3.23% leading.
- **VKOSPI 83.43 (+7.58%) back above 80** after 5 declines; record 96.94 (06-29). **KOSPI July −28.9% = worst month since 1990**; 07-28 intraday low 5,992.91 (−11.29%), 2nd-largest point drop ever, 4th-largest %. Forward PER **5.1x** (Kiwoom); 200-day MA ~5,600.
- **Futures basis: PRIMARY GAP** (endpoints blocked). Derived proxy 🟡 (my computation via [asiae](https://core.asiae.co.kr/article/2026072810323501385)): at the 07-28 09:06 sidecar, K200 futures −6.42% vs spot −5.26% ≈ 1.2pp backwardation — futures led cash down. Overnight 야간선물: NOT FOUND.
- **Overnight US (T2):** SOX **−4.49%** 4th straight (MU −8.85%, SNDK −14.3%, AMD −8.15%, WDC −6.91%), **NVDA −4.99% @ $196.51, CDS +14bp → 82bp**; Dow +1.03%/S&P +0.21%/Nasdaq −0.22% — the segment-scoped inversion (07-28 EOD artifact) held a second session. **SKH ADR −8.98%, −13% vs the $149 IPO reference** — ADR fell −9% while the local line opens +3% on the print: basis/venue divergence to reconcile at EOD.
- **Regulatory (🟢):** leveraged-ETF 기본예탁금 ₩10m→₩30m cash-only CONFIRMED effective **07-31** (pulled forward); FSC Chairman flags possible **per-individual leverage caps** (~20% of holdings floated, basis/timing NOT fixed); 증안펀드 restart + short-sale ban DEMANDED, not adopted; no new KRX measure overnight.
- Crash-driver attributions (CXMT, DUV, NVDA credit, de-risking) = NARRATIVE-UNGRADED per the standing patch.

### Unfilled (booked as gaps, not zeros)
K200 basis in points + 야간선물 gap (needs broker terminal/KRX portal) · per-name foreign flows 005930/000660 (KRX MDCSTAT024) · 반대매매 covering-print (later today) · auction volume vs norm + program direction (unpublished).
