# 2026-07-30 THU — THE EARNINGS REWARD-FUNCTION MAP (operator brain-dump → mental model request)

**WORKFLOW: INGEST + MACRO-FIRST (#9).** Operator ask, extracted from a brain-dump: not an earnings recap — a **mental model of what this market rewards and punishes**, built from the Tue/Wed AMC print set, with the SK Hynix paradox (verified-strong demand, third down day) as the test case the model must explain. Four Opus agents in flight: (A) full Tue+Wed AMC print set + tonight's calendar; (B) analyst reward-function/positioning research; (C) live price action + tonight's setup; (D) hyperscaler capex aggregate + cash-cover + memory pass-through.

**NO POSITION ACTION — user-gated.**

## §1 COMPUTED PATTERN from corpus-booked figures (pre-agent, T1/T1-adjacent inputs)

| Name | Rev surprise | EPS surprise | Reaction | capex/OCF | Note |
|---|---|---|---|---|---|
| MSFT | +0.71% | +9.53% | **+8.88%** (AH) | n/a (OCF not yet booked) | Azure +43% vs cons 40.2%; RPO $678B +84% |
| META | −0.93% | −16.03% | **−7.45%** (AH) | **0.976** | capex $31.08B / OCF $31.86B; FCF $784M |
| GOOGL (07-22) | n/a | n/a | ~−6.5% | **>1.0 (negative cover)** | capex $44.9B, **FCF −$5.9B first negative quarter**; Cloud +82% |
| SKHY (07-29) | −5.64% | −5.53% (OP) | **−9.61%**, then −6.28% | n/a | OPM 76% record; capex RAISED to ₩40조 후반 |
| KLAC | n/a | n/a | **−10.80%** | n/a | **on a RAISED guide** |
| STX | n/a | n/a | +2.29% | n/a | HDD beat — only memory-adjacent gainer |
| INTC (07-24) | n/a | n/a | +13% AH | n/a | DCAI +59%, guide up |

**Computed (this session, python):** META capex/OCF = 31.08/31.86 = **0.976 → 97.6% of operating cash consumed by capex**. GOOGL: capex exceeded OCF entirely (FCF −$5.9B).
**The diagnostic asymmetry (computed):** META missed EPS by −16.03% and fell −7.45%; SKHY missed OP by −5.53% and fell −9.61%. **Miss magnitude does NOT rank the punishment** — the ranking variable is something other than the print.

## §2 HYPOTHESIS UNDER TEST (my model, pre-agent-verification — falsifiers stated)
**The regime switched from pricing AI EXPOSURE to pricing AI CASH CONVERSION**, which splits the complex into three tiers with different reward rules:
1. **MONETIZERS** (cloud/platform w/ a visible revenue line): rewarded only if attach is visible AND capex is cash-covered. Evidence: MSFT +8.88% vs GOOGL −6.5% — same demand direction, opposite outcome, differing on FCF cover.
2. **SPENDERS** (capex without attached revenue): punished regardless of demand narrative. Evidence: META (97.6% of OCF consumed, FCF $784M).
3. **SUPPLIERS** (the cost input inside everyone else's capex): punished *when the market questions capex*, because their own fundamentals are a lagging report of the buyer's spending decision. Evidence: SKHY on record margins; KLAC on a raised guide.
**Why SKHY specifically carries three de-rating channels its earnings cannot fix (my model):** (a) its revenue IS hyperscaler capex → it is re-rated on the buyer's discipline, not its own results; (b) **Warsh 07-29 put memory-chip prices inside the FOMC's inflation question set** (T1 transcript, booked 07-30 wake) → memory-price strength now feeds a rates headwind, i.e. the upcycle is partly self-limiting in this regime; (c) CXMT/China-DUV caps the cycle's DURATION, which is what a multiple pays for.
**Falsifiers for the hypothesis:** (i) AMZN tonight prints rising capex WITH decelerating AWS and RALLIES → cash-conversion framing dead; (ii) a supplier prints strong and rallies while hyperscaler capex is being questioned → tier-3 rule dead; (iii) analyst commentary shows the market rewarding capex-raises as growth signals → the whole switch is my artifact.

## §3 AGENT C RETURN — THE VENUE TEST PARTIALLY FALSIFIES §2's HYPOTHESIS (computed)

**Venue split, 07-29/07-30 reactions (agent-C verified; means computed this session):**
| Venue | n | mean | median | up/total |
|---|---|---|---|---|
| Japan | 7 | **+2.44%** | +2.92% | 5/7 |
| Europe | 3 | +0.96% | +1.20% | 2/3 |
| Korea | 3 | −3.77% | −4.94% | 0/3 |
| **US** | 12 | **−6.75%** | −6.83% | **1/12** |
**JP−US venue spread = +9.20pp (computed).**

**SAME-PRODUCT, DIFFERENT-VENUE — the discriminator (computed spreads):**
- **NAND: Kioxia (JP) +2.92% vs SanDisk (US) −7.32% = 10.24pp** — same product, same day, opposite sign.
- **Equipment: Advantest (JP) +10.85% vs KLAC (US) −10.80% = 21.65pp** — both beat/raised.
- **⭐ Foundry: TSMC local 2330.TW +0.23% vs TSM ADR −4.50% = 4.73pp — THE SAME COMPANY, two listings, one day.** Identical fundamentals, identical news, zero possible fundamental explanation. This is the cleanest control in the dataset.

**BEATS ARE NOT BEING PAID FOR (US venue), n=5:** KLAC beat+raised → −10.80% · ARM beat → −8.11% (−5.73% more AH) · VRT EPS beat/rev miss → −17.26% · Samsung chip-OP beat → −0.72% (gave back +6-8% intraday) · SKHY record 76% OPM → −5.64%.

### ⚖️ MODEL REVISION (my model): the reward function has TWO AXES, and the flow axis currently DOMINATES
§2's single-axis "cash-conversion" hypothesis is **INCOMPLETE — partially falsified.** It explains the US mega-cap split (MSFT +8.88% w/ Azure 43% + RPO $678B vs META −7.45% w/ 97.6% of OCF consumed) but **cannot explain Kioxia rising while SanDisk falls on identical NAND economics, nor TSMC's own two listings diverging 4.73pp.**
- **AXIS 1 — FUNDAMENTAL (what gets rewarded when fundamentals are being priced):** cash conversion + visible revenue attach. Clean expression: MSFT vs META vs GOOGL. Direction: capex is rewarded ONLY when cash-covered and attached; otherwise punished.
- **AXIS 2 — FLOW/VENUE (what is actually dominating right now):** US and Korea are inside a positioning unwind (KR: foreign net-sell 4 sessions −₩11.90조, leveraged-ETF deleveraging into tomorrow's deposit hike, 2 CB days; US: AI-complex crowding, VIX +11.86% to 20.66, SOX −5.33% vs equal-weight −0.90%). Japan and Europe are NOT — and their identical-product names rose. **Magnitude: the venue effect (9.20pp) is larger than almost any fundamental surprise in the set.**
**Nomura's "flows, not fundamentals" (T2, booked 07-30) is therefore CORROBORATED by an independent computed test the analyst didn't run.**

### Why SK Hynix specifically is the worst-placed name on file (my model, 3 stacked channels)
1st order (P>80%): it sits in the **worst venue** (Korea, mid-unwind) — the TSMC-ADR control proves venue alone is worth multiple points/day. 2nd order (P~60%): it is a **tier-3 supplier** on the fundamental axis — its revenue IS hyperscaler capex, so it is re-rated on the buyer's discipline, not its own results; its raised capex (+~50% to ~$31B, T2) reads as the F1 supplier-discipline tripwire to a market already punishing spend. 3rd order (P~40%): **duration compression** — CXMT/China-DUV caps the cycle length, which is what the multiple pays for (Mirae's peer-PBR 6.5x→4.6x derate is exactly this). 4th order (P~20%): **the Warsh channel** — memory prices are now inside the FOMC inflation question, so memory-price strength feeds a rates headwind (30Y 5.20%, 2007 high) that de-rates the whole complex. **None of the four is fixable by an earnings beat, which is precisely why record 76% margins did not stop the fall.**

**Contra-evidence held honestly (Rule #18):** Advantest raised a PROFIT guide and rose 10.85% while SKHY raised a CAPEX guide and fell — a "profit-guide vs spend-guide" reading also fits. But KLAC beat AND raised guidance and fell 10.80%, which breaks the simple version of that rule in the US venue — consistent with flow-dominance, not with a clean fundamental discriminator.

## §4 AGENT B RETURN — the documented evidence base; model CONFIRMED and SHARPENED to three forces

### The reorganizing datum
**30-day correlation between AI SPENDERS and SEMIS collapsed +0.78 → ~0.00, lowest in 4.5 years** (Bloomberg via Yahoo, T2). **Interpretation test (my model): if semis were still priced as capex BENEFICIARIES, that correlation holds. Correlation → 0 means the market stopped treating supplier revenue as a function of buyer spend.** This is the single structural break that explains the whole week — and it is what my venue test (§3) was detecting from the other side.

### Sequencing fact that settles the SKHY causality question (computed)
**SKHY fell −14.65% on 07-27 — TWO SESSIONS BEFORE the 07-29 print.** The de-rating began before the earnings existed; the print landed on an already-broken tape. Compounded 07-27 + 07-29 + 07-30 = **−27.20%** (computed; 07-28 excluded, no verified figure in that set). **The earnings are not the cause. They are the alibi.**

### THREE FORCES (final model; each independently documented)
**FORCE 1 — CAPEX-DURATION PRICING (the fundamental reward function). Documented, multi-source.**
The market is not pricing capex LEVEL; it prices the **LAG between cash out and revenue back**:
- lag ≈ 0-1 quarter (ASML beat-and-raise +5.6%; Seagate record 52.7% GM +3%; MSFT RPO $678B; GEV **EPS MISS but +4.29%** on orders +88%/backlog $176B) → **REWARDED**
- lag ≈ 2-8 quarters (GOOGL, META, SKHY, KLAC, Vertiv) → **PUNISHED regardless of the current quarter**
- lag NEGATIVE — consumes AI without funding it (**AAPL +15% in July, reclaimed #1 mcap ~$4.95T, "avoids capex pitfalls"**) → **BEST PERFORMER**
Supporting hard data: hyperscaler **capex/OCF ~90% aggregate 2026E** (BofA via Epoch AI); OCF +23%/yr vs capex +70%/yr, **crossing ~Q3 2026**; 5-hyperscaler 2026E **net income +25% to ~$506B while combined FCF −91% to ~$16B = FCF is 3.2% of net income** (computed). **Depreciation wall: 2026 AI spend $760B, only $211B expensed → $549B = 72.2% deferred to future P&Ls** (computed) — "the 2027 earnings season is when the accounting math becomes unavoidable." Quotes: Meeks (Freedom Capital) *"no longer giving companies a free ride… demanding monetization, or at least visibility towards monetization"*; Ahlsten (Parnassus) *"what kind of AI revenue is being generated per dollar of compute"*; Bloomberg *"that deal is suddenly breaking down."*
**FORCE 2 — POSITIONING WASHOUT. Documented with hard data; this is what my venue test measured.**
BofA FMS: **"long global semis" most crowded trade at 82% = RECORD HIGH, 3rd straight month**; cash 4.1%→3.6% **triggering BofA's cash-rule SELL signal**; "AI bubble" #1 tail risk 45% (+17pts MoM); **61% expect NO cut to 2026 AI capex** (i.e. the crowd is not fundamentally bearish — it is positioned). **S&P short interest 3.79% of free float = all-time high** (S3, data to 2010); **SOX 25-delta put skew 94th percentile**; SOX/NDX IV premium to SPX widest in a decade; MSFT short interest at a decade high INTO the print (→ the +8.88% is partly a squeeze). Record $46B semi-ETF inflows in 2026 with $5.4B in one session DURING the drawdown = crowding, not capitulation.
**FORCE 3 — MEMORY RE-CLASSIFIED FROM BENEFICIARY TO COST-INPUT. Three same-week confirmations.**
(a) **QCOM guided DOWN on 07-29 and explicitly blamed the memory crunch** — a customer's guide-down caused BY memory pricing; (b) PC OEMs raised prices 15-20%; (c) **memory = 35% of PC BOM vs ~20% a year ago = 1.75× (computed)**. Plus MarketWatch-sourced customer complaints that memory prices *"have to come down. They're way too elevated."* And the hyperscaler wallet-shift: budgets redirected toward power, liquid cooling, custom silicon — **shrinking memory's share of incremental AI investment**. **This is the mechanism by which good memory fundamentals become a bear case: high ASPs are now someone else's margin problem, and that someone is the customer.**

### Corrections and traps caught (booked)
- ⚠️ **STALE-TRAP: the widely-surfaced "Goldman cuts SK Hynix / HBM pricing to decline" note is JULY 2025, not 2026** — excluded (B40 class, agent-caught).
- ⚠️ **META capex direction: the low end was RAISED $125B→$130B (top held $145B). One outlet described this as "cut the midpoint" — arithmetically wrong.** Our booking (low-end raised) is correct.
- Alphabet: print 07-22 AMC, the −7% reaction was **07-23** (our §1 "~−6.5%" refined).
- **CXMT bear case is REBUTTED by the analysts closest to it:** Jefferies — *"CXMT is not yet impacting global memory D&S, since its lower tech does not allow it to meet US AI demand"* (98% commodity DRAM, no HBM); **Morgan Stanley called the selloff "a compelling entry point," citing DC memory prices +25%+ in Q3 alone.** UBS/BofA frame it as a "healthy reset" in a supercycle, HBM bottleneck into 2027. **This materially weakens my §3 3rd-order "duration compression" channel — the duration risk is REAL but is being priced ahead of any demonstrated D&S impact.**
- FactSet context: 88-91.4% of reporters beat EPS (5-yr avg 78%), aggregate surprise +16.4% (5-yr 7.0%) — **yet the market is punishing BOTH positive and negative surprises more than the 5-yr average.** Implied dispersion (DSPX) at a 1-year high of 44.44. **A beat-rate at a multi-year high coexisting with beats being sold is the definitive signature of a flow regime, not a fundamentals regime.**

### Falsifiers (carried forward, unresolved tonight)
AMZN raises capex materially AND rallies without in-quarter conversion → Force 1 dead · memory keeps falling AFTER FMS crowding drops below ~60% and short interest normalizes → Force 2 dead, it was fundamental all along · Q3 DRAM/HBM contract ASPs roll over WHILE memory equities rally → Force 3 dead (multiple, not classification) · FactSet's next update shows beat-reactions back at the +1.0% norm → the whole regime was a two-week air-pocket.

## §5 AGENTS A + D — THE INVERSION THAT COMPLETES THE MAP (all computed)

### ⭐ THE FINDING: memory MAKERS crushed while memory EQUIPMENT rallied — same end-demand, same week
- **MAKERS:** SK Hynix −9.61%, Micron −9.94%, SanDisk −7.32%, Samsung −0.72%
- **EQUIPMENT:** **Lam Research +6.60% AH · FormFactor +10.43% AH · Silicon Motion +8.98% AH · Teradyne +13.6% AH** (faded to −0.39% next day on the market-wide tape)
- **And the guides are MEMORY-LED:** LRCX guided Sept **+13.6% OVER consensus**; TER guided Q3 **+21.8% OVER consensus** with **AI >60% of Q2 revenue and RECORD memory revenue** (DRAM + NAND final-test resurgence). KLAC — logic-weighted process control — guided only **+2.0%** over consensus and fell −10.80%. The equipment tier is not uniformly bid; it is bid **in proportion to memory exposure.**

### THE RULE THAT FITS EVERY DATA POINT (my model; supersedes the §2 tier framing)
**At every layer of the stack simultaneously, the market is PAYING THE RECIPIENT of capex and PUNISHING THE PAYER of it.**
- Hyperscaler pays capex → hyperscaler punished (META −7.45%, GOOGL −7.00%) **unless in-quarter conversion is shown** (MSFT +8.88%: Azure 43%, RPO $678B +84%)
- Memory maker pays capex (**SKHY raised ~50% to ₩40조 후반**) → **memory maker punished** … and **that exact same capex is LRCX/TER/FORM revenue → equipment rewarded**
- Apple pays no AI capex at all → **best performer of the entire complex** (+15% in July, reclaimed #1 mcap ~$4.95T explicitly on "avoids capex pitfalls")

**Computed capex-intensity test (capex/revenue vs reaction, T1 filings):**
| Bucket | n | mean reaction |
|---|---|---|
| LOW intensity (<20% of revenue) | 7 | **+4.63%** |
| HIGH intensity (>20%) | 4 | −0.70% |
| **HIGH intensity EXCLUDING MSFT** | 3 | **−3.89%** |
**Conversion-adjusted spread = +8.53pp.** MSFT is the single high-intensity name that escaped, and it escaped on conversion — which is the whole thesis in one exception.

### T1 SAME-QUARTER PROOF THAT MEMORY DEMAND IS NOT SOFTENING — it is the CONSTRAINT
- **QCOM 8-K verbatim: "despite a challenging MEMORY and supply environment"** — a customer's guide impaired BY memory.
- **ARM 6-K: AGI CPU production revenue SLIPS to Q4 FY27** on "TSMC N3 allocation, **advanced packaging capacity, HBM availability**."
- **TER: AI >60% of Q2 revenue, record memory revenue**; FORM: "HBM + co-packaged optics driving sequential growth."
**Two T1 same-quarter sources naming memory/packaging as the binding constraint on OTHER companies' revenue. TC-1 and TC-5 both get an independent third-party confirmation from the equipment layer.**

### ⚠️ THE CAPEX PLATEAU — the story nobody is telling (computed, agent D)
**Big-4 CY2026 capex: $712.5B now vs $710.0B thirty days ago = +$2.5B = +0.35%.** Alphabet's +$15B raise was almost exactly cancelled by **Microsoft's −$15B, which is ACCOUNTING, NOT A CUT** — Hood verbatim: *"our calendar year 2026 CapEx investment expectations remain unchanged"* (finance→operating lease reclass + building useful life 15y→25y). Ex-reclass the delta is +$17.5B (+2.46%). **Aggregate incl. ORCL/CRWV/NBIS ≈ $860B.**
**Cash-cover ranking (T1 SEC XBRL) EXACTLY tracks the reaction ranking: MSFT 74.0% (+8.88%) → META 97.6% (−7.45%) → GOOGL 115.0% (−7.00%) → AMZN 169.8% Q1 / 101.7% TTM (prints TONIGHT).** Correlation −0.896 (n=3, indicative). **The reward threshold sits between 74% and 97.6% cover.**
**Depreciation wall arriving now:** MSFT FY26 depreciation **+55.9% vs revenue +17.8% = 3.14×** (computed); D&A/revenue 7.81%→10.34%, Q4 alone 11.44%. Sector-wide $549B of 2026 spend (72.2%) not yet expensed.
**Memory share of AI capex (my computation):** $860.5B × 60% server/IT (GOOGL-disclosed split) × 22-32% memory share of AI-server cost = **$114-165B, midpoint $139B = 16.2% of total capex.** 🟡 the 22-32% band is inference, not a published figure.

### 🔴 THE LOAD-BEARING NEGATIVE RESULT (agent D searched explicitly)
**ZERO name-specific, dated, demand-driven AI-capex cuts by any major buyer in the last 30 days.** All five apparent "cuts" resolve to non-demand causes: NY State moratorium (permitting, 07-14) · NVDA Rubin 2.0M→1.5M (SUPPLY — HBM4 qual; KeyBanc says RESOLVED, ramping July, PT RAISED $310→$330) · MSFT $190B→$175B (accounting) · AMZN $25B bond 2.5× covered vs 3.2× (funding friction — the one real crack, on the FINANCING side) · **"30-50% of 2026 US DC projects cancelled" REFUTED AT SOURCE by SemiAnalysis (06-18): their NA hyperscaler self-build forecast moved ~1% in six months.**
⚠️ **STALENESS TRAP: "Microsoft abandons 2GW" (TD Cowen) and "Amazon halts DC leasing" (Wells Fargo) are MARCH 2025 stories** surfacing as current. Excluded. Second B40-class trap this session (with the July-2025 Goldman HBM note).
**And SK Hynix's LTAs are PRICE-SMOOTHING, NOT price-resistance:** ~10 deals up to 5 years "structured to keep prices steady," with deposits — hyperscalers trading volume certainty for ASP stability, i.e. **locking in high prices.** No order deferral, no dual-sourcing pressure, no walk-away. The Q3 contract deceleration (+13-18% vs ~60%) is driven by **consumer-electronics OEMs unable to pay — NOT hyperscalers** (Tom's Hardware). **This materially strengthens the demand leg of the memory thesis while the equities de-rate.**

## §6 GRADEABLE CALL REGISTERED (quota instrument; resolves tonight ~20:00 UTC)
**AMZN Q2 print, Thu 2026-07-30 AMC.** Consensus: rev ~$196.7-196.9B, EPS $1.82, **AWS $40.5-40.6B (+31-31.6%)**, AWS margin 33.8%, Q2 capex ~$48.7B, FY26 capex ~$207B.
**My call (my model, from the reward function above): P~65% AMZN trades DOWN on the print unless AWS growth accelerates to ≥32% AND capex guidance holds at ~$200B or below.** Rationale: AMZN has the WORST cash cover of the Big-4 (101.7% TTM, 169.8% Q1) and is the name closest to the OCF/capex crossover. **P~35% it rallies on an AWS beat — which would be the MSFT template repeating and would CONFIRM force 1.**
**FALSIFIER, stated in advance: if AMZN raises capex materially AND rallies WITHOUT an in-quarter conversion proof point, the capex-duration/cash-cover reward function is DEAD and I retract §4-§5.**

**NO POSITION ACTION — user-gated throughout.**
