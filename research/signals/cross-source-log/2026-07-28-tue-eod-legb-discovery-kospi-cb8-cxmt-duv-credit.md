# 2026-07-28 TUE — EOD Leg-B discovery sweep: KOSPI −10.84% CB#8, China DUV mass-production report, CXMT IPO fallout, AI-credit stress cluster

**WORKFLOW: B-LEG DISCOVERY SCAN (Workflow #10 / Rule #16, EOD lean variant) — 1 Opus agent, 18 searches, 12 items.** Fired by the EOD conditional-synthesis Routine (quiet-evening full path; zero commits since 16:00Z). Grade sweep: no prediction resolves 2026-07-28 (grading-log parsed; next resolution = SK Hynix Q2, 2026-07-29).

**NO POSITION ACTION — user-gated. Nothing here fires a registered falsifier tonight.**

---

## §1 TAPE — machine-verified against EODHD EOD series (T1-machine; computed, never `change_p`)

| Instrument | 07-27 close | 07-28 close | Δ (computed) | Agent/press claim | Verdict |
|---|---|---|---|---|---|
| KOSPI (KS11.INDX) | 6,755.75 | **6,023.66** | **−10.84%** | −10.84% | ✅ EXACT |
| SK Hynix (000660.KO) | 1,816,000 | **1,550,000** | **−14.65%** | −14.7% press | ✅ (rounding) |
| Samsung (005930.KO) | 254,000 | **220,000** | **−13.39%** | −13.4% press | ✅ (rounding) |
| Nikkei (N225.INDX) | 64,931.19 | **62,364.92** | **−3.95%** | −3.95% / −2,566.27pt | ✅ EXACT (pt-drop reconciles; the competing "−2,884" is dead) |
| S&P 500 (GSPC.INDX) | 7,413.18 | **7,435.69** | **+0.30%** | disputed +0.4%/+0.13% | ✅ RESOLVED by machine print |
| Dow (DJI.INDX) | 52,210.08 | **52,810.74** | **+1.15%** | disputed +1.3%/+0.93% | ✅ RESOLVED by machine print |
| Nasdaq-100 (NDX.INDX) | 28,039.21 | **27,819.04** | **−0.79%** | "enters correction" (Bloomberg T1) | close verified; the −10%-from-record framing is T1-press, record not re-derived tonight |

- **Circuit-breaker check:** breaker level 6,213.51 = −8.02% off the verified 6,755.75 prior close ✓ (Korea Times T1; 20-min halt; **8th market-wide CB of 2026** per Seoul Economic Daily T2 — count not independently recomputed).
- **Drawdown check (computed):** KOSPI −33.91% from the verified 06-22 record 9,114.55, over exactly **25 trading sessions** — the Wolf Street T3 "−34% in 25 days" checks precisely on a trading-day basis.
- **The joint state that matters:** Dow +1.15% / S&P +0.30% on the SAME day KOSPI fell −10.84% and US semis were sold (MU ~−9%, SNDK/WDC −12%+, Dell −13%, AMD −8/10%, NVDA ~flat — Benzinga/Bloomberg T1/T2, singles not machine-verified). Beat-and-raise prints outside AI-infra (Sherwin-Williams +8.5%, UPS guide-raise) got NORMAL positive reactions. **The reaction-function inversion (Principle #48/#49, N=6) is segment-scoped to AI-infra, not market-wide — a REFINEMENT, not an N+1.**
- Basis stamps: KRX figures = Seoul 15:30 KST close; US = NY 16:00 ET close; per five-calls addendum #10 declared-cut rule.
- Route note: EODHD Korean singles resolve under **`.KO`** suffix tonight (`.KS` returned HTTPError) — logged for `data-access.md`. Brent has no EODHD route (`BZ.COMM` HTTPError); FRED remains spot-FOB/lagged — Brent settles below are press-tier by necessity.

## §2 FRONT PAGE (12 items, ranked; full sourcing in the agent return, key links inline)

1. **CXMT IPO'd on Shanghai STAR +466% day one** — priced ¥8.66, mcap ~$480-487bn (most valuable China-listed company), **$8.6bn raised**, prospectus discloses **7.67% global DRAM share** late-2025 ([CNBC](https://www.cnbc.com/2026/07/27/cxmt-china-market-debut-chipmaker-ipo.html) T1, 07-27/28). Extends yesterday's CXMT cluster (`2026-07-27-mon-four-ai-brief-batch-cxmt-cluster-nvda-financing.md`) — now with disclosure obligations and a capacity-funding currency.
2. **China begins mass production of homegrown immersion DUV** — Shanghai state consortium (absorbed SMEE + Yuliangsheng/SiCarrier-affiliate); **~5 tools 2026 → ~20 in 2027**; first deliveries to SMIC, Hua Hong, **CXMT**; 28nm single-exposure, multipatterning path to 7nm; **critical components still imported from Japan** ([Reuters exclusive](https://live.euronext.com/en/financial-news/exclusive-china-starts-production-home-grown-immersion-duv-chipmaking-tools-source) T2 — single anonymous source; [TrendForce](https://www.trendforce.com/news/2026/07/28/news-china-reportedly-starts-mass-producing-immersion-duv-tools-smic-hua-hong-cxmt-deliveries-expected-this-year/) T2 echo).
3. **KOSPI −10.84%, CB#8, SK Hynix −14.65%, Samsung −13.39%** (§1, T1-machine). Samsung's worst day in ~2 decades per Korea Times T1.
4. **Nasdaq-100 correction** (−10% from early-June record, Bloomberg T1); SanDisk −50% from peak, Micron −1/3 from peak (T2, unverified singles).
5. **NVDA circular-financing fear at scale** — >$750bn fresh deals framing; SK Group tie-up >$500bn mutual business; $250bn OpenAI lease backstop talks; **NVDA 5yr CDS record 82bp Mon 07-27**, largest single-day gain since the contract began trading Nov-2025 ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-27/nvidia-s-750-billion-deals-revive-fear-of-ai-circular-financing) T1). → TC-2 rung 3.
6. **PJM board proposes backstop capacity auction (Sept) for a 6.8 GW shortfall** — third consecutive short auction — plus a **data-center curtailment registry: DCs ≥50 MW without own generation curtailed near emergencies, from June 2027**; FERC filing end-July; DCs = $6.3bn / 38% of the $16.4bn capacity charge ([Utility Dive](https://www.utilitydive.com/news/pjm-board-backstop-capacity-auction-data-center-curtailment/826347/) T2 + PJM release T1).
7. **ASML −8.5%** on the DUV report, ~$44bn cap erased ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-27/asml-slides-after-report-of-china-beginning-duv-tool-production) T1).
8. **Brent settle $84.09 (−4.8%) Tue after $88.36 (−8.7%) Mon** ([CNBC](https://www.cnbc.com/2026/07/28/oil-price-today-wti-brent-us-iran-hormuz.html) T1 naming settles; WTI $79.26). Hormuz de-escalation diplomacy: **Oman proposes a Malacca-style regional mechanism with voluntary transit fees**, Witkoff/Kushner involved, UK/FR mine-clearing offers (T2/T3). → §4 gate adjudication.
9. **US lawmakers seek national-security probe of CXMT**; ≥2 House members want US purchase bans; Pentagon added CXMT to the 1260H list 08-Jun-2026 (T3 — NY Post-sourced, **needs T1 confirmation before any weight**).
10. **BlackRock's $12.55bn IG bond for a Meta El Paso DC cleared at 7.534% yield (+287.5bp/10yr)** — failed to tighten in syndication, rallied secondary Monday ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-27/blackrock-dodges-ai-bond-flop-as-12-3-billion-debt-deal-rallies) T1). → TC-2 rung 3.
11. **Mercedes cuts FY26 guidance on China (Q2 China sales −30%)**; Porsche +5,000 job cuts; BMW auto margin guided 1-3% in June (Automotive News/Euronews T2). → MURATA auto-MLCC leg.
12. **US macro softening into the FOMC (Wed 07-29 14:00 ET, consensus hold 3.50-3.75%)**: Conference Board 90.8 (Present Situation 114.9, 3rd straight decline); durable goods +0.3% vs +1.6% consensus; 10Y 4.62-4.63% third down session (T1/T2).

## §3 DOT-CONNECTIONS

### 🚨 §3.1 ANTI-CONFIRMATION — the window's loudest signal hits TC-1, the book's #1 conviction cluster
TC-1 (memory tightness, N=22+) rests on a supply premise: disciplined three-player oligopoly, capacity capped by export-controlled lithography. **Both legs were hit in one session:** CXMT now holds an $8.6bn raise + a ~$480bn equity currency to fund DRAM capacity (item 1), and China claims a domestic immersion-DUV line feeding CXMT among first customers (item 2). **Neither fires a registered falsifier today** — ~5 tools/2026 is rounding error against ASML's immersion run-rate, CXMT is at 7.67% share, and the registered falsifier (CXMT premium-tier HBM qualification at NVDA) is explicitly NOT met (zero NVDA/AMD qual, per the 07-27 CXMT-cluster verification). **But the DURATION assumption inside TC-1 — how many quarters the shortage persists — is what took damage, and duration is what the ASP thesis capitalises.**
**⚠️ FALSIFIER MIS-SPECIFICATION FLAG (operator-gated proposal, same class as the 07-27 falsifier-#3 tightening):** TC-1's falsifier watches the HBM door while the commodity-DRAM door is the one being funded. Proposed addition: *"China-DRAM capacity leg: CXMT IPO-proceeds capex conversion into ≥X wpm incremental wafer starts, or verified DUV-tool deliveries enabling DRAM node progression, on a 12-18mo horizon."* Booked as a PROPOSAL in TC-1 (not rewritten unilaterally).

### §3.2 Held names (Rule #10 cascade, same commit)
- **MURATA (held):** the real dot tonight is item 11, not the memory crash — Mercedes China −30% / Porsche cuts / BMW 1-3% margin = **NEGATIVE, partial-INVALIDATE pressure on the auto-MLCC leg**, which the harness has under-modelled relative to the 800V AI-server leg. The 800V/Vera Rubin leg is untouched by China DUV. → thesis back-ref.
- **SUMCO (held):** genuinely two-sided — more Chinese DRAM fabs = more 300mm wafer demand (positive), BUT the TC-15 China-leg correction (07-08) routes incremental Chinese demand to domestic wafer makers, and any Samsung/Hynix capex response-freeze would hit SUMCO's actual customers (negative). **Sign UNRESOLVED — no fake netting. Aug-06 Q2 interim is the adjudicator.** → thesis back-ref.
- **SKHY (watchlist, conditional add gated on tomorrow's print):** the print now lands into a −14.65% session (T1-machine), a Nasdaq-100 correction, and a freshly funded competitor. The pre-registered GP-bridge sign test and the TrendForce contract-price deceleration input are UNCHANGED by the tape. → thesis back-ref.
- Exited names (HYNIX/KIOXIA/SNDK ledger context): thesis-negative window, P&L-irrelevant; the ~Jul-1/2 exits were **process-wrong, outcome-right** — belongs in lessons.md at the next codification pass, NOT as vindication.

### §3.3 Frameworks
- **T2 power-binding → strong VALIDATE, upgraded from forecast to regulation:** PJM ≥50MW curtailment registry (June 2027) converts power from cost variable to **delivery-risk variable in interconnection rules**. TC-13 rung.
- **TC-2 → N+2 on rung 3 (vendor balance sheets / credit):** NVDA CDS record 82bp + Meta-linked DC bond clearing at 7.534% without tightening = two independent same-week credit-structure marks. Booked to TC-2.
- **H3 Brent gate → adjudicated below (§4).**
- **Reaction-function flip → REFINE not increment:** segment-scoped to AI-infra (§1 joint state), materially different from the market-wide pattern as previously booked.

## §4 H3 BRENT GATE — UN-BREACH REVIEW TRIGGERED (escorted instrument, basis stamped)

The gate is **settle-defined**. Two consecutive named settles below $95: **Mon 07-27 $88.36, Tue 07-28 $84.09** (CNBC T1 naming settle; multi-outlet). No machine route exists (EODHD Brent absent, FRED spot-FOB/lagged — `data-access.md`), so this is a **press-settle basis adjudication, stamped as such**. Per five-calls addendum #8's registered trigger ("Brent settle <$95 → un-breach review"): **the review fires now; the reweight decision itself is deferred to the 07-29 wake**, where it can be taken jointly with the SKHY print — noting the structural twist that a Hormuz transit-fee regime would permanently compress the risk premium (structure change, not just price). KR escalation trigger (foreign net-sell ≥3 sessions) remains **UNREADABLE — no KRX flow route**; tonight's −10.84% session makes closing that route more urgent (see absence question).

## §5 NEW NAMES → watchlist routing

| Name | Why on radar |
|---|---|
| Shanghai Aishengna Electronic Technology Group (state, unlisted) | The DUV-producing consortium (absorbed SMEE + Yuliangsheng) |
| Yuliangsheng (private, SiCarrier affiliate) | Built the DUV prototype — the technical core |
| SiCarrier (Huawei-backed, private) | Connective tissue Huawei ↔ litho push |
| Hua Hong Semiconductor | Named DUV recipient alongside SMIC/CXMT |
| CXMT (STAR-listed as of 07-27) | **Status change: private black box → LISTED** — files, discloses capacity, has a price |
| Seagate STX / Western Digital WDC | −7% to −12% today (T2); the storage cohort trades as one book with SNDK |

## §6 NEW THEME / NEXT-BOTTLENECK CANDIDATES

1. **DUV subsystems as the migrated choke point (bypass-route-of-the-bypass-route):** if China solves tool *assembly*, the binding constraint moves upstream to what it still imports from Japan — excimer light sources, precision optics, wafer stages. Names to map: Gigaphoton, Ushio, Canon/Nikon optics, Tokyo Seimitsu. **The Japanese-component dependency is the load-bearing sentence in the Reuters piece and nobody is trading it. Highest-value unworked thread tonight.**
2. **Grid curtailment as de-facto capex governor:** PJM registry → DC siting selects for behind-the-meter generation (itself backlog-constrained: gas turbines/fuel cells); curtailment risk becomes a lease-pricing term feeding item-10 credit spreads.
3. **Chokepoint governance as a tradable regime:** a formalized Hormuz transit-fee mechanism would structurally compress Brent's geopolitical premium — permanent, not headline.
4. **"Lithography Sovereignty Discount" (new thesis candidate):** the market prices the non-China semi-cap/memory complex off *permanence* of the ASML immersion monopoly; today's report prices in a terminal date. Applies unevenly — heaviest at mature-node/commodity DRAM, lightest where EUV binds. Falsifier: the ~20-tools-2027 target slips, or the Japanese-component dependency proves binding.

## §7 THE ABSENCE QUESTION

**The market's dominant conversation tonight is the FINANCING STRUCTURE of AI capex — and the harness has no credit instrument.** NVDA CDS at a record, $750bn circular pledges, a $250bn backstop, a DC bond at 7.53% failing to tighten: TC-2 tracks this as narrative, but there is no spread/CDS route in `data-access.md`, no funding-cost → order-book → memory-demand lead-lag map. Every equity exposure in the book is a late-cycle derivative of a financing condition the desk does not monitor. **Routed to todo as a named P1 candidate (credit-instrumentation leg of the intake-boundary P0).** Secondary absence: **China consumer/auto demand** — MURATA carries a large auto-MLCC leg and the harness has zero China-auto model.

## §8 ANOMALIES (→ anomaly-register)

1. **KR microstructure as regime:** a sidecar every ~3.53 days on average in 2026 (36kr T3) and 8 market-wide CBs YTD (T2) — breakers designed as tail events now firing at regime frequency; no instrument models a whole-index CB regime.
2. **CXMT at ~$480bn on 7.67% DRAM share** — a policy-and-captive-demand price, not a cash-flow price, sitting inside the supply curve of the book's core thesis (T1).
3. **Private US envoys negotiating a Hormuz toll schedule** (Witkoff/Kushner; T2/T3) — durable governance change with no thesis contact and no segment home.

## §9 Rule #14 density check
- CXMT/DUV items: same-segment (chip-and-foundry/memory) same-direction (China supply-side advance) with the 07-27 CXMT cluster → booked as TC-1 duration-risk note + falsifier proposal (§3.1); no new TC cluster opened.
- Credit items: same-segment (infrastructure-IaaS financing) with TC-2 → N+2 booked (§3.3).
- PJM: TC-13 rung (§3.3).

**NO POSITION ACTION — user-gated. No registered falsifier fired. Tomorrow: SK Hynix Q2 print = sole adjudicator of the conditional add; FOMC same day 14:00 ET.**
