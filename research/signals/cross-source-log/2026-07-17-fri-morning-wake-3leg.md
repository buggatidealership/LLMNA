# 2026-07-17 FRI — GOOD-MORNING WAKE (3-leg + Leg C WSJ ×13) — third rout day; facts-first order executed

**WORKFLOW: #10 two-leg scan + Leg C ingest, under `meta/good-morning-protocol.md`. FACTS-FIRST WAKE ORDER honored: API tape (EODHD/TWSE/FRED/FMP/EDGAR) fetched BEFORE agents; agent claims graded against prints.**

## 0. THE TAPE (computed, T1-API 🟢 — kill-criteria for everything below)

| Print | Value | Source |
|---|---|---|
| **Jul-17 TAIEX** | **42,671.27 −6.47% — closed AT the session low** | EODHD TWII.INDX same-day |
| **Jul-17 Nikkei 225** | **64,141.12 −4.03%** (low 62,704.60 = −6.2% intraday) | EODHD N225.INDX same-day |
| Jul-16 KOSPI (finals reconciled — docket item closed) | 6,820.60 −6.37% | EODHD KS11.INDX |
| Jul-16 SK Hynix / Samsung finals | ₩1,842,000 −11.53% / ₩255,000 −8.77% | EODHD .KO |
| Jul-16 TSMC Taipei | NT$2,470 record close, +30 (+1.2%) on print day | TWSE openapi |
| Jul-16 Taiwan memory/wafer same day | Nanya −8.7% (439), TaiSil −9.9% (471), EMC −1.8% (4,990) | TWSE openapi |
| Jul-16 TSM ADR | $409.74 **−2.32% ON the record print** | FMP |
| US 10Y | 4.62 → 4.58 → 4.55 (Jul-13→15), WSJ Jul-17 AM: "yield fall accelerates" | FRED DGS10 + WSJ T2 |
| SKHY ADR path since entry | $173.45 entry (Jul-10) → 152.35 → **193.92 (Jul-14 IBM-day memory rally)** → 176.46 → **$152.31 Jul-16 = −12.2% on position** (computed) | FMP |
| Jul-17 US futures ~7am ET | NQ ~−1.5/−2%, SPX ~−0.9, Dow ~−0.5 | WSJ chart T2 + Leg B corroboration |
| TSMC Q2 FILING-GRADE | rev NT$1,270.38B +36% YoY; NI NT$706.56B +77.4%; **EPS US$4.31/ADR** — grade completed, see grade artifact addendum | EDGAR 6-K Ex-99.1 |

## 1. Catch-up sweep (docket items closed this wake)
1. **TSMC 6-K re-poll → DONE:** filing-grade EPS $4.31 books the final MISS-LOW (+10.5% above house point $3.90; street $3.81 was −11.6%). L32 **N=2 CONFIRMED** (ASML + TSMC, both band-architecture misses). Ledger row updated to filing grade.
2. **TSM T+0 reaction grade → SELL-THE-RECORD:** −2.32% ADR on a +36%/+77% record print + capex raise. Taipei (+1.2% record close, session ended pre-US-rout) vs ADR divergence = the reaction is a REGIME verdict, not an earnings verdict. "Good news isn't enough" tell #2 this week.
3. **ASML T+24h reaction grade → CLOSED:** +2.23% day-0, −1.67% T+24h, net +0.52% from pre-print vs MU −8.94% same window = RESILIENT; the FY-raise held a falling tape.
4. **KR exact closes (chased since Jul-16) → RECONCILED** via EODHD (table above). The date-trap ₩1,845,000 "Jul-16" figure circulating in search results was indeed the Jul-13 close — actual Jul-16 close ₩1,842,000, confusingly close in level; timestamp-checked.
5. **Wiring tests (roadmap track 2) → Finnhub /news + /company-news LIVE** (minutes-latency headline layer delivered); GDELT 429-flaky (retry later, not load-bearing); **FMP quarterly-estimate granularity VERIFIED** — NOW Q2-26 consensus bar now computable at API level (rev $3.928B avg / EPS $0.859 avg + bands) for the Jul-22 print. Registry updated same commit.

## 2. Leg B (unanchored discovery) — what is actually driving rout day 3 (T2 verified, dated Jul-16/17)
**Named mechanisms (FACTS), in rough order of weight:**
1. **Korean leveraged unwind hit the margin-call wall** — KOSPI/KOSDAQ sell-side circuit breakers fired intraday; the ₩62.76T credit overhang (our Jul-16 KOFIA artifact) is the pre-positioned fuel. (Press: Investing.com "Korea's leveraged chip trade hits the margin call wall.")
2. **Capex-fear reading of TSMC's raise:** the $60-64B FY26 guide (vs $52-56B) is being traded as an AI-spend-discipline threat (echoes Meta Compute monetization frame, broke Jul-1), NOT as the demand signal we graded it as. Same datum, opposite market read — this is the disagreement to instrument, not to argue with.
3. **Netflix Q2 (Jul-16 after bell): EPS beat ($0.80 vs $0.79), revenue light ($12.56B vs $12.59B), soft Q3 guide → −8-9%**, dragging megacap sentiment (frame: "even winners get sold").
4. **US–Iran escalation:** strikes near Iran's coast, Hormuz transit drop (Finnhub/Reuters headline layer), Brent +12% on week to ~$85.28. **Yield claim in press KILLED by print:** 10Y is FALLING (4.55 Jul-15, fall accelerating per WSJ this AM) — flight-to-quality dominates the oil-inflation channel. Chevron exploring Hormuz-bypass pipeline (WSJ).
**Verified-fresh non-rout items:** **Kimi K3** (Moonshot, Jul-16: 2.8T-param open-weight, 1M context, weights GA promised Jul-27; benchmark claims near frontier are VENDOR-self-reported — only the Arena front-end-coding preference is third-party; treat as T3 until independent evals) · **Xi at WAIC Shanghai (Jul-17):** global-AI-governance push, open-source promotion, 5,000 training programs, cooperation centers (ASEAN/BRICS/AU/Arab League); "swipe at US" is press FRAME, not quote · **Japan sovereign-AI buy (Jul-16 T2 Bloomberg): 27,500 NVDA Rubin chips, new entity Noetra Corp, ¥387.3B (~$2.4B) through Mar-2027, SoftBank/Preferred Networks/NEC, robotics foundation model, DC online Jun-2028** · **Databricks $188B round (Coatue-led ~$3B): +40% vs $134B earlier this year** · SEC 10-S semiannual proposal still in comment chaos (comment-intake mix-up controversy Jul-14) — meta-watch: our whole grading loop assumes quarterly cadence.

## 3. Leg C (WSJ ×13, T2 headline-layer) — routing table
| Item | Class | Route |
|---|---|---|
| "Nasdaq Futures Drop as Chip Selloff Deepens" + "Chip Stocks Fall as AI Trade Loses Steam" + "Nasdaq Falls Sharply as Chip-Stock Slump Overshadows TSMC Record" | FRAME cluster (one editorial current, not N signals) | Booked as the market's verdict on Jul-16: a record TSMC print could not hold the tape. Regime datum → §4 |
| "U.S. Treasury Yield Fall Accelerates" | FACT (headline) | Confirms FRED direction; flight-to-quality overlay |
| IBM boardroom-debate story | Known thread | Already deep-dived Jul-17 AM (W9 artifact); no new facts in headline |
| Moonshot Kimi / Xi open-source / Japan-NVDA / Databricks | FACT cluster | Verified via Leg B (above); Kimi K3 → private-tracker + China-AI watch; Japan-NVDA → sovereign-AI theme (NVDA demand datum); Databricks → private-tracker mark |
| "Can AI Make Better Drugs? Not on Wall Street's Timeline" (HOTS) | OPINION | Healthcare-rotation thread color — coheres with our Jul-16 verdict (rotation destination mis-specified; medical-AI being SOLD) |
| "Gas Prices Will Stay Higher for Longer" / Chevron Hormuz bypass / Iran headlines | Complement | Energy-geopolitics overlay; funding-node watch |
| SEC quarterly-earnings scrap + complaint flood | Complement/meta | Print-cadence watch (grading-loop dependency) |
| "Why Most Investors Didn't Beat the Market During a Great Quarter" / PE-riches / traders-best-year | FRAME/froth tells | Attention-economy register color |
| Trump student-visa length limits | Complement | Education-instrument watch item (international-student channel) |
| Telegram overlay "the pit: rise n shine. not great but was expecting worse" | T3 sentiment | Retail sentiment: resigned-not-panicked (contrarian-neutral) |
**Unasked (macro):** if a RECORD print from the most systemically important AI supplier cannot hold its own tape for 24h, is the binding variable now POSITIONING (leverage, concentration) rather than FUNDAMENTALS — and which of our tells would detect the hand-off in time? (→ graduates to anomaly-register candidate; pairs with the KOFIA gauge.) **Unasked (micro):** SKHY ADR round-tripped +27% off the Jul-13 low and back in 3 sessions — is the ADR (6% float, retail-heavy) now a LEVERAGE-BETA instrument that will overshoot BOTH directions around Jul-29, and should the pre-registered reaction bands be widened accordingly?

## 4. Synthesis — regime read (my model 🟡)
Three consecutive sessions, three different lead stories (BOK hike Wed / TSMC-record-ignored Thu / margin-unwind Fri), ONE mechanism family: **the leverage that amplified the up-leg is unwinding into strength-agnostic selling.** The discriminator between "healthy de-lever inside an intact demand regime" (H1, P~55 my model) and "the AI-trade top" (H2, P~25) and "macro shock takeover — Iran/oil/funding" (H3, P~20): fundamentals keep printing ABOVE expectations while positioning unwinds (H1-consistent: TSMC +36%/+77%, ASML raise, IBM's problem was TOO MUCH infra demand); H2 requires demand-side falsifiers (hyperscaler capex cuts, LTA walk-backs — none observed; TC-18 intact); H3 requires the yield/oil channel to invert (10Y falling = not yet). **Watch this differently: the KOFIA margin balance is now the single highest-frequency H1/H2 discriminator — a stabilizing margin balance with rising prints = unwind exhausting; continued forced-sale prints = more supply overhang.** (Leg A carries the second-wave numbers.)

## 5. Leg A (KR/JP portfolio-anchored, landed — T2 press-sourced, date-pinned; JP closes carry intraday-vs-close conflicts because Yahoo-JP/Nikkei history 403'd the agent)

**KOREA: NO SESSION TODAY — 제헌절 (Constitution Day) reinstated as a KRX holiday (pre-announced May-20).** No circuit breakers, no stabilization, no continuation — a non-event, not a signal. Last KR prints remain the Jul-16 finals (§0). **Monday Jul-20: Korea REOPENS with ~3 days of global semi weakness accumulated while shut; Japan is CLOSED (海の日) — the two legs of the book alternate blind days.** Whipsaw context booked: Jul-15 KOSPI was +6.24% (7,284.41), fully round-tripped Jul-16.

**JAPAN Jul-17 closes (T2, conflicts flagged):**
| Name | Close | % | Note |
|---|---|---|---|
| Nikkei 225 | 64,141.12 | −4.03% | 5th-largest point drop ever (−2,694); weekly −4,416 = record point drop |
| **SUMCO (held 626)** | ~3,914 (conflict: −12.29% #1 N225 decliner ranking vs −15.17% snapshot) | −12.3~−15.2% | no company news — beta + wafer-cohort contagion; VERIFY close Tue (JP closed Mon) |
| **Murata (held 336)** | 7,632 vs 7,570 snapshots | −9.1~−9.9% | −66.78pt Nikkei contribution |
| Kioxia (watchlist, exited) | 52,110 | **−16.10% STOP-LIMIT-DOWN** | **US patent-verdict loss: Viasat suit, $229M (~¥37.1B) damages, Waco federal jury Jul-16** — idiosyncratic trigger dragging the memory complex |
| Advantest | 26,440 | −10.8~−11.0% | largest index drag (~−772pt) |
| Tokyo Electron | 64,750 (11:30 read) | −8.7% | |
| SoftBank G | 5,424/5,381 | −9.0~−9.7% | |
**JP press frames (NOT facts):** imported SOX −4% + Kioxia verdict + pre-3-day-weekend 持ち高調整 (position-squaring), amplified by Korea's closure thinning regional liquidity + Iran overlay.

**KOFIA second-wave watch (docket): NO Jul-15/16 print published yet** (T+1/T+2 lag + KR holiday) — freshest DATED: Jul-13 KOSPI-only margin ₩27.4472T with Samsung/SKH+2 names = 41.1% concentration; Jul-09 all-market ₩36.63T; **July MTD forced sales >₩450B, daily avg >₩50B ≈ 2× the 1H-26 daily average (₩25.7B)** (T2). Trajectory coheres with our ₩38.6→34.8T margin-stock series (no contradiction). **RE-CHECK MONDAY — the single highest-frequency H1/H2 discriminator (§4) is data-gapped until then.**

**KR policy facts (Jul-16, T1-adjacent — closes the F4-measures watch from the HYNIX thesis):** F4 emergency meeting 15:00 → single-stock leveraged-product curbs: basic deposit **₩10M→₩30M cash-only (Aug-5)**, 20-share trading lots, **new single-stock leverage/inverse/covered-call listings SUSPENDED**, education 2→3hr, brokerage collateral exclusion Aug-19. BOK (same day, already booked Jul-16): +25bp to 2.75%; Gov. Shin: equity vol "not a systemic-risk channel," inflation-first — **no central-bank put, explicitly.**

**KR press frame flagged for Jul-29 bar-setting (T2, NOT verified): SKH Q2 operating income "tracking ~8% below the ₩65T consensus"** — a second bar-lowering current (after KIS). Route to the Jul-29 pre-registration: the whisper is moving DOWN while the ADR trades leverage-beta (unasked-micro, §3).

## 6. Cascades (Rule #10, same commit)
HYNIX (F4 measures + Monday-reopen gap risk + whisper-down frame) · SUMCO + MURATA (today's damage + Tue verification) · KIOXIA (patent verdict) · day-state (Monday calendar + KOFIA recheck) · TSMC grade artifact (filing-grade addendum, done pre-wake) · data-access registry (Finnhub/FMP/EODHD-indices/TWSE-timing, done) · calibration ledger (EPS row filing-grade).

**Position implication: HOLD all three (MURATA 336 / SUMCO 626 / SKHY 37 ADS) — no falsifier fires anywhere: today is positioning-unwind + patent-verdict contagion + holiday-thinned liquidity, while fundamentals keep printing ABOVE expectations (TSMC filing-grade +36%/+77% completes the same week the tape sells it). Rule #8 binds. Sizing note: the book's two largest lines just took −9~−15% in one JP session with Monday blind (JP closed) — no action, but Monday's KR reopen + Tuesday's JP reopen are the next two live risk windows, and the KOFIA Monday print is the discriminator to fetch FIRST.** 🟡
