# 2026-07-14 TUE — morning scan (3 Opus ≈ 211k: Leg A 103.7k / Leg B 45.1k / WSJ-verifier 62.4k; EN+KR+JP+CN) + user T2 closes

## 0. INTRADAY-VS-CLOSE CORRECTION (own-relay error, self-corrected)
Leg B's first return carried the Korean MORNING wires ("KOSPI −5% intraday, SKH −8.7% to ₩1,685,000") and I relayed it as "Seoul did not stabilize" — WRONG at the close layer. User T2 finals + Leg A receipts: the −8.7% was the intraday LOW (₩1,845,000 × 0.913 ≈ ₩1,685,000, arithmetic-exact), fully reversed by the close. Lesson instance: morning-wire prints are intraday snapshots; never relay an Asia-session read as a close before 08:30 CEST without a close receipt. (B40-adjacent freshness class, intraday sub-type.)

## 1. TUESDAY SESSION — pre-registered forced-sale-wave read: **GRADED CONFIRMED (FLOW, not information)**
| Item | Number | Source |
|---|---|---|
| KOSPI open | 6,769.06 (−0.56% gap — NO crater) | 파이낸셜뉴스 T2 |
| KOSPI midday spike-low | 6,606.78 print 13:18 (−2.94%); Herald cited 6,400s tape (timing unresolved); KOSDAQ sell sidecar midday | 펜앤마이크 T3 / 헤럴드 T2 / 이투데이 T2 |
| KOSPI close | **6,856.83 +0.73%** (user T2 confirms +0.73%) | 머니투데이 T2 |
| 000660 | open −1.08%, worst −4.74→−8.67% intraday low ₩1,685,000, **close +3.69% ≈ ₩1,913,000 (computed)** | 연합 T2 + user T2 |
| 005930 | **close +3.34% ≈ ₩263,000 (computed)** | user T2 |
| Flows (intraday ~10:14) | foreign +₩253.7bn, institutions +₩1,701.1bn, **retail −₩1,921.9bn** | 뉴스1/fn뉴스 T2 |
| 반대매매 official | Tuesday figure prints T+1 (tomorrow); latest official Jul-9 ₩142.2bn/10.2% | 뉴데일리 T2 — sub-leg OPEN |
Verdict: the dip was bought TWICE (open, midday); retail liquidation absorbed by institutions+foreigners = textbook forced-seller transfer. **Pre-registration (event artifact EVE addendum, 2026-07-13) VALIDATED.** Tokyo mirrored: Nikkei −900+ early → close green (~+0.7%, final unpinned); Kioxia low −6.02% → close ¥67,960 +1.28% (松井 T2; user relay +2.98% — reference gap, flag); SUMCO intraday +7.8%, user close +3.39%; MURATA user close +0.38% (Leg A carried a TradingEconomics −9.60% for MONDAY vs our booked −6.51% — conflict flagged, re-pull final). Taiwan DIVERGED DOWN this time: TAIEX −1.42% (intraday −1,400pts), TSMC 2,420 −20; **Nanya +4.49% GREEN on a red tape** (ETtoday T2) — memory-tightness read intact. User adds: Harmonic Drive +4.14% (robotics cohort); GigaDevice 兆易创新 +8% intraday (China legacy-memory sympathy — CXMT-adjacent color).

## 2. MACRO ANCHOR — **HELD STATE BROKEN, updated (research-verified 2026-07-14 T2)**
US struck **80+ targets in Iran** (incl. IRGC vessels); Iran hit US facilities in Jordan/Kuwait/Bahrain/Oman; **Iran formally closed Hormuz**; Trump reimposed the blockade + will convoy/protect traffic for a **fee of 20% of cargo value** (Axios/CNBC T2). **Brent: Mon +9.6% → $83.30 (best day since May-2020), Tue ~$84.7-84.8.** US 10Y 4.61% (range 4.57-4.62), Waller HIKE comments cited in Tokyo wraps. Replaces "re-escalation, Brent ~$79". The reflex-arc (user thread): oil→inflation-fear→rate-fear is now the live tape (WSJ "Treasury Yields Rise as Oil Moves Higher"). Leg B oddity upgrade: **Hormuz war-risk insurance ~5% of hull value but cover DEMAND falling — owners stop sailing; quantity rationing, not price** (Insurance Journal/LMA T2) = better instrument than Brent. Today: 5 US megabanks pre-open + Warsh first testimony + **June CPI TODAY 14:30 CEST (cons ~3.8% vs 4.2% May)** — USER-CORRECTED: Leg B wrote 'CPI Wed' contradicting its own cited TechTimes headline ('collide Tuesday rare double print'); agent-relay date error, caught by user.

## 3. SKHY — pre-registered first-regular-close LADDER GRADE (computed, receipts)
- **Mon close $152.35 −9.32%** (JoongAng T2; FXLeaders ~$152.7 T3 — cent-level unreceipted, flag); range $151.30-162.28, vol 56.65M ADS. Position: 37 ADS × ($152.35−$173.45) = **−$780.70 = −12.16% vs entry** (computed).
- **Premium at Mon close: +22.2% / +23.9% / +25.5% at FX 1480/1500/1520** (computed; Reuters cited ~25.6% intraday) → **the >+20% EXTREME branch of the ladder printed and SUSTAINED** — closed-end dynamic holding (one-way fungibility + TSMC ~+21% precedent), mark cushioned vs Seoul's crash but structurally fragile.
- **Catch-down targets recomputed vs TUESDAY ordinary (~₩1,913,000, FX 1500):** Fri-level +15.6% → $147.43 (−15.0% vs entry); gate +5% → $133.92 (−22.8%); parity → $127.54 (−26.5%). Seoul's Tuesday RECOVERY (+3.69%) raised these targets vs Monday's set — the ordinary rising is the benign closure path (premium compresses by denominator, not ADR fall).
- Entry-gate grading live: the +19.7% entry premium now grades against a wider (~+24%) premium — the override remains unpunished via premium, punished via underlying beta (−12.16% mark inside a cohort-wide unwind).
- **INFORMATION (positive, new): Yongin Y1 equipment orders BEGUN; phase-1 opening pulled forward May-2027 → Feb-2027; 1c-nm DRAM feeding HBM4E** (ZDNet KR T2 today 10:24) — capex acceleration = TC-18-consistent revealed preference, supply-response speed also feeds the block-F tail discount.
- TrendForce spot (Jul-8, T1-own): DDR4 1Gx8 3200 +2.88% w/w $37.14; NAND 512Gb TLC −2.87%.

## 4. WSJ-verifier verdicts (Leg C completion)
| Item | Verdict |
|---|---|
| "Data-Center Builders Racing to Offload Stakes" | **REFRAMED — but a GENUINE THIRD AXIS underneath → funding-node tell #11 (asset/equity-level distribution)**: Blackstone→Digital Realty $3.5bn (3 NoVA DCs, $1.2bn cash + $2.3bn shares, Jun-29 Bloomberg T2); Brookfield's Csquare ~$1.35bn IPO with proceeds → $734M revolver + securitized-debt repayment, NOT builds (PitchBook T2); DigiCo Chicago $750M; buyers = REIT paper / IPO retail / sovereign permanent capital (Aligned $40bn BlackRock-GIP-MGX). Frame data: JPM ~$700bn 2026 DC funding needs, $1.4T gap; "five largest builders' combined FCF → zero by Q3-26". Adjacent T3-unverified: QTS Digital Gateway (2,100-acre) terminated. WSJ's "investors want in" dek is itself a distribution-narrative tell — supply of stakes marketed as buyer opportunity |
| "Chinese AI startup DFSX chip" | **CONFIRMED-FRESH (Jul-13 Shanghai): DFSX = 东方算芯 (Dongfang Suanxin), chip DF1000** — "software-defined near-memory-computing 3D chip": 14nm domestic node, wafer-level hybrid-bonded DRAM-on-logic, **replaces HBM with conventional DRAM**; vendor-claimed 520 TFLOPS BF16 + 6.4 TB/s (≳H100-class claims at 14nm — treat as vendor-claimed, extraordinary); chairman Wei Shaojun 魏少军 (Tsinghua/CSIA), backers National AI Fund + Yunfeng + Xiaomi/JD arms; DF2000 Q4-26, DF3000 Q4-27 roadmap (Sina/证券时报/IT之家 T2-CN, SCMP T2). **= HBM design-around instance** → anomaly register (design-around normalization N+1) + Jul-16 engineering-out audit feed + legacy-DRAM-demand cross-current (a bypass that CONSUMES commodity DRAM) |
| "SpaceX Stock Closes at New Low" | **CONFIRMED-FRESH + HOUSE-RECORD REPAIR: SpaceX is PUBLIC — SPCX, Nasdaq, IPO Jun-12-2026** ($135 offer, ~$86bn raised = largest IPO ever, ~$2.1T day-one cap; absorbed xAI PRE-IPO; T1 SEC S-1 + company PDF). Mon close $139.14 −4.24% = all-time listed low, −38% from Jun-16 peak $225.64, $4 above offer. Drivers: CASC reusable Long March 10B sea-landing (T3) + growth selloff + orbital-DC skepticism. Private-tracker updated; the Jul-8 "SpaceX-Cursor $60bn" datum NOT re-verified by this agent (search gap, not a kill) — flagged for re-check |
| SKHY debut headlines ×2 | RECYCLED (Friday-wrap coverage); the real Monday story ($152.35 −9.32%) was absent from the front |

## 5. Leg B discovery (segment-agnostic keepers)
- **Japan June PPI +7.1% y/y** (fastest since Mar-2023; fuel +22.8%, non-ferrous +39.2%) — war-energy + AI-materials + weak yen → BOJ pressure (Japan Times/BOJ T1).
- **Triple-collision today:** JPM/BAC/C/WFC/GS pre-open + Warsh Humphrey-Hawkins (House today) + June CPI TODAY (user-corrected from 'Wed'; the TechTimes slug itself says Tuesday) cons ~3.8% vs 4.2% May.
- **Akzo rejects Nippon Paint €7.5bn**; **LG Electronics +5% on NVIDIA AI-server-rack build report** (new rack-integration entrant, CNBC T2); **Shein HK IPO green-lit** (Caixin); **MiniMax raises HK$16bn while Xiaomi cuts jobs** (same-day pairing: China AI capital vs hardware margins); **ByteDance Seed world-model → autonomous driving**; SoftBank Son "¥800T AI infra by 2040" (recycled ambition marker).
- **Anomalous bucket:** JFTC dawn raids (Seven-Eleven display-case bid-rigging cartel); **private Chinese fusion co at tens-of-billions-RMB valuation** (36Kr S2 thin — verify before use); Nasdaq micro-cap same-day delist-to-OTC pipeline (BNBX/PTNM) = shell-segment stress.
- JPMorgan frames chip weakness as **crowded-positioning unwind, not AI-cycle reversal** (T2 via CNBC) — TC-17-consistent street framing.

## 6. Anomaly-register increments (booked this commit)
- **Everything-is-listing wave N+1 cluster:** SpaceX $86bn largest-ever (Jun-12) + SKH $26.5bn second-biggest share sale + "IPO Gold Rush—Texas Coming for New York" (WSJ) + Shein HK + LG India ₹774bn + Csquare + CXMT ¥29.5bn pricing tomorrow.
- **Social-backlash cluster +3 instances in ONE WSJ front:** "Prettier Data Center vs Community Backlash", "Hard-Line Activists Ramping Up for the War With AI", Meta smartglasses privacy uproar.
- **Design-around normalization N+1:** DFSX DF1000 (HBM replaced with commodity DRAM via 3D near-memory stacking).

## 7. CXMT: pricing publishes TOMORROW Jul-15, subscription Jul-16 (证券时报/东方财富 T2 native; ¥29.5bn, 2nd-largest STAR IPO ever) — graded checkpoint stands (adjudicates Nanya-instrument trigger b + capacity-mix conflict).

## Cascades (same commit, Rule #10): SKHY thesis (ladder grade + Yongin Y1); event artifact Tuesday addendum; funding node tell #11; private-tracker SPCX repair; anomaly register ×3; SUMCO/MURATA back-refs; ledger ×3.
**Open re-pulls (midday/tomorrow):** SKHY cent-close receipt; 000660/005930/Nikkei/SUMCO/MURATA close receipts (user T2 booked as current best); Tuesday 반대매매 official; CXMT price; MURATA Monday −6.51% vs −9.60% conflict.

**Position implication: HOLD all three — no size change — Tuesday flow-read CONFIRMED (forced-seller transfer, closes green), macro state updated to Hormuz-closed/Brent ~$85 (real information, NOT a thesis falsifier per Rule #8), Yongin pull-forward positive, funding-node third axis booked as instrument; adjudicators: CXMT price tomorrow, 반대매매 print tomorrow, megabanks/Warsh/CPI this week, SKH Jul-29.** 🟡

**CORRECTION APPENDIX (same day, per `2026-07-14-tue-yongin-y1-equipment-verification-beneficiary-map.md`):** §3's "Yongin Y1 phase-1 opening pulled forward May-2027→Feb-2027 — genuinely new" was WRONG on the news-framing: the pull-forward was OFFICIALLY announced 2026-02-25 (Seoul Economic Daily, on-record; ₩31tn ph1). Genuinely new on Jul-14 = orders-placed-now + Q3-start price negotiations (single-source ZDNet T2, unconfirmed) + 20k wpm first-tranche detail. B40 instance: relayed a trade outlet's news-framing without checking the announcement date of the underlying schedule — the verification layer caught it same-day on the user's full-text share.
