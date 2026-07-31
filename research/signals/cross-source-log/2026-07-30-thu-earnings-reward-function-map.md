# 2026-07-30 THU — THE EARNINGS REWARD-FUNCTION MAP (operator brain-dump → mental model request)

**WORKFLOW: INGEST + MACRO-FIRST (#9).** Operator ask, extracted from a brain-dump: not an earnings recap — a **mental model of what this market rewards and punishes**, built from the Tue/Wed AMC print set, with the SK Hynix paradox (verified-strong demand, third down day) as the test case the model must explain. Four Opus agents in flight: (A) full Tue+Wed AMC print set + tonight's calendar; (B) analyst reward-function/positioning research; (C) live price action + tonight's setup; (D) hyperscaler capex aggregate + cash-cover + memory pass-through.

**NO POSITION ACTION — user-gated.**

## §1 COMPUTED PATTERN from corpus-booked figures (pre-agent, T1/T1-adjacent inputs)

| Name | Rev surprise | EPS surprise | Reaction | capex/OCF | Note |
|---|---|---|---|---|---|
| MSFT | +0.71% | +9.53% | **+8.88%** (AH) | n/a (OCF not yet booked) | Azure +43% vs cons 40.2%; RPO $678B +84% |
| META | −0.93% | −16.03% | **−7.45%** (AH) | **0.976** | capex $31.08B / OCF $31.86B; FCF $784M |
| GOOGL (07-22) | n/a | n/a | **−7.13%** ⟨corrected 07-31: was ~−6.5%, an intraday tick; settled close 317.69 vs base 342.09⟩ | **>1.0 (negative cover)** | capex $44.9B, **FCF −$5.9B first negative quarter**; Cloud +82% |
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
- Hyperscaler pays capex → hyperscaler punished (META **−7.95% settled** ⟨was −7.45% AH / −8.73% intraday⟩, GOOGL **−7.13% settled** ⟨was −7.00% intraday⟩ — corrected 07-31) **unless in-quarter conversion is shown** (MSFT +8.88%: Azure 43%, RPO $678B +84%)
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
🔴 **RETRACTED 2026-07-31 — THIS CLAIM IS FALSE.** Tested against the corrected settled reactions + TTM cover: **Spearman ρ = +0.20 on quarterly cover and ρ = −0.80 on TTM cover — i.e. INVERTED on the correct basis.** META has the **best** TTM cover (70.9%) and the **worst** reaction (−7.95%); AMZN has the **worst** cover (109.7% TTM) and the **2nd-best** reaction. The claim was built on (a) the **intraday-tick reaction figures** corrected 07-31 and (b) **quarterly** cover ratios, which are seasonally worthless — AMZN's swung 74.3% → 175.8% on nearly identical capex, a **2.37× swing from OCF seasonality alone**. Per L42-b cover ratios now require a basis stamp: **TTM is load-bearing, quarterly is decoration.** See `signals/cross-source-log/2026-07-31-fri-hyperscaler-ai-roi-conversion-session.md` §4. ~~Original claim: Cash-cover ranking (T1 SEC XBRL) EXACTLY tracks the reaction ranking: MSFT 74.0% (+8.88%) → META 97.6% (−7.45%) → GOOGL 115.0% (−7.00%) → AMZN 169.8% Q1 / 101.7% TTM (prints TONIGHT). Correlation −0.896 (n=3, indicative). The reward threshold sits between 74% and 97.6% cover.~~
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

## §7 SAME-DAY REVERSAL — the US session melted up (16:20 UTC, mid-session; all computed vs verified 07-29 closes, Finnhub/EODHD T1-machine)

**Macro anchor as of 2026-07-30:** the §4 Force-2 positioning stack (semis most-crowded-trade 82% record, put skew 94th pct, short interest all-time high) was the pre-condition; this session is that spring releasing. Ties to the §5 reward function — which HELD while the flow overlay flipped.

| Ripping | | Still falling | |
|---|---|---|---|
| SanDisk **+24.53%** · Lam **+18.53%** · Micron **+16.82%** · **MSFT +15.51%** ⟨corrected 07-31: +16.77% implied $456.03, an intraday tick $4.93 above the $451.10 settle⟩ ~~+16.77%** | | **Meta −8.73%** | |
| WDC +14.41% · INTC +13.68% · AMD +13.37% · MRVL +12.34% · KLAC +8.06% · TSM +7.72% · ARM +7.37% · AMZN +5.64% · **NVDA only +2.23%** | | Apple −2.08% · Alphabet −0.78% | |

**MECHANICAL-REVERSAL TEST (computed):** correlation(07-29 move, 07-30 move) across 13 names = **−0.567** — the harder it fell, the harder it bounced. Recovery multiples: SNDK **3.35×** its Wednesday loss, INTC 2.67×, AMD 2.43×, MU 1.69×. **This is a positioning unwind reversing, not a re-rating.**
**DISCRIMINATION TEST (the tell, computed):** semis/memory mean **+12.05%** (n=10) vs megacap-spenders mean **−3.86%** (n=3) = **15.92pp spread in one session.** **The §5 reward function HELD THROUGH THE REVERSAL** — recipients bought, payers-without-conversion still sold (META −8.73% on the bounce day). MSFT is the payer-with-conversion exception, and its decade-high short interest into the print means a large squeeze component.
**NVDA +2.23% is the loudest quiet number:** if this were "AI is back," NVDA leads. It didn't — memory did. Consistent with a squeeze in the most-shorted corner, not thesis rehabilitation. 🟡 my model.

### ⭐ THE VENUE DISLOCATION — actionable into tomorrow's Seoul open
Seoul closed **06:30 UTC, BEFORE all of this**: SK Hynix **−5.64%** (₩1,322,000), Samsung **−0.72%** (₩207,000) — both T1-machine verified. Meanwhile, trading RIGHT NOW:
- **SK Hynix GDR (HY9H Frankfurt): 828.13 → 936.97 = +13.14%** (from today's open 814.23: +15.07%)
- **Samsung (SSU Frankfurt): 3,190.55 → 3,577.65 = +12.13%** (from open: +9.00%)
**SAME COMPANY, SAME DAY, TWO VENUES: SK Hynix gap = 18.78pp; Samsung gap = 12.85pp (computed).** This is the §3 TSMC-ADR control repeating at 4× the magnitude, and it is the cleanest possible confirmation that **venue/flow — not fundamentals — has been setting these prices all week.** The European lines are pricing the bounce Korea has not yet traded. **Tomorrow's Seoul open is where the gap resolves** — carried as the first read of the next KR wake.
⚠️ **OPERATOR-FLAG: the "Samsung +25%" figure in the operator's question does not reconcile to any verified Samsung line** (Seoul −0.72%, Frankfurt +12.13%). Nearest verified +25% in the complex is **SanDisk +24.53%**. Ticker/venue confirmation requested before any use.

**Caveats:** mid-session, none of these are closes. The registered §6 AMZN call (P~65% down) now faces a materially friendlier tape than at registration — the call and its retraction condition stand as written, ungraded until the print. A news agent is out on whether a NAMED memory catalyst exists (SNDK +24.5% normally requires one) with explicit instruction to return "no catalyst, positioning" if that is the honest answer.
**NO POSITION ACTION — user-gated.**

## §8 THE DRIVER — news agent returned; my §7 "pure positioning" read is PARTIALLY REVISED

**Honest correction to §7: there ARE four named, dated catalysts. I under-weighted the news leg. The revised verdict: the news is PERMISSION, the magnitude is POSITIONING — and the Seoul control proves the split.**

### The catalyst I missed: SAMSUNG Q2 (reported 07-30 KST, T1)
Revenue **KRW 171.5tn (+130% YoY)**; OP **KRW 89.5tn (+1,814% YoY)**; **semiconductor division OP KRW 89.2tn (~$61.7B) = +250× YoY**. Guidance: **shortage persists THROUGH 2028, with 2027 TIGHTER than 2026**; **60-70% of capacity committed to multi-year contracts**; HBM4 **+3× QoQ** in Q3, >60% of H2 HBM revenue; long-term deals signed with **top-5 global datacenter customers**, 5 more closing.
**Why this detonated the memory complex: it is a direct refutation of the CXMT/China-DUV oversupply thesis that CAUSED the 07-28 crash.** Not generic good news — the *specific* bear case answered by the largest supplier. Other named catalysts: **MSFT Azure +43%** accelerating, Azure crossed **$100B** FY revenue (~$260B mcap added); **LRCX Sept guide $8.1B ±$0.4B = ~$1B / 13.6% above consensus**, GM 52% (20-yr high); **ARM 500M Neoverse cores in 9 months** vs 6 years for the first billion; **UBS initiates SKHY ADR BUY, PT $204** (market pricing LT ROE ~17.7% vs UBS 2027-31E 40.2%).

### ⭐⭐ THE FINDING OF THE DAY — FORCE 3 (memory-as-cost-input) NOW PROVEN INSIDE A SINGLE P&L
**Samsung's MOBILE division posted a KRW 700bn LOSS — its FIRST-EVER quarterly loss — because its OWN semiconductor division's chip prices crushed device margins.** Semi +250× YoY; Mobile first loss in company history; same company, same quarter. Samsung explicitly warned of higher phone/PC pricing ahead.
**This upgrades §4 Force 3 from a cross-company inference (QCOM guide-down, PC BOM 20%→35%) to a MEASURED INTRA-COMPANY fact.** The strongest possible form of the claim: the memory upcycle is now destroying its own conglomerate's downstream margin. **→ cascade candidate for `sector/bottlenecks.md` U8/B47 falsifier-side ledger and TC-1's demand-destruction leg.**

### The Seoul control — my venue test independently confirmed by the agent
| Instrument | Intraday | Close |
|---|---|---|
| KOSPI | **+5.5%** | **−1.23%** |
| Samsung | **+7%** | **−0.72%** |
| SK Hynix | record +557% OP | **−9.61%** |
**Seoul traded the IDENTICAL Samsung print hours earlier — was up as much as +5.5% — and CLOSED RED. US-listed memory on the same news: +15% to +25%.** If the news were sufficient, the most direct expression of it would not close red. **The Seoul↔New York delta is positioning, not information. §3/§7 CONFIRMED by an independent route.** (Korea also introduced NEW ETF curbs 07-30 — forced-selling mechanics still active there.)

### Flow evidence, pre-registered (🟢 HARD, dated BEFORE the print)
**MSFT short interest ~92M shares = 1.27% of float, HIGHEST SINCE MAY 2015, largest short-interest increase among the Mag-7, with "virtually no short covering ahead of earnings"** (CNBC 07-28). A decade-high uncovered short base met a beat — that is the cleanest causal fact behind the +8pt extension beyond the after-hours move. Plus: Deutsche Bank systematic positioning **70th percentile**; **SPX dealer gamma 27th percentile** of the past year (thin support → larger swings both ways); the 07-24/28 drawdown itself attributed to "systematic de-risking from quantitative funds." Session PT raises: MS $650, WF $650, Bernstein $647, Wedbush $625, Citi $600, Piper $550.
**SNDK +24.53% — NEGATIVE RESULT CONFIRMED: no SanDisk-specific catalyst dated 07-30.** BofA's $2,500 PT is pre-existing. SNDK is the highest-beta, highest-short, most-drawn-down expression of the complex — **it is the beta, not the news. NARRATIVE-UNGRADED.**

### Macro did NOT drive it (computed)
**Q2 GDP advance +1.5% vs ~2.2% consensus = −0.7pp MISS**; core PCE +3.3% in line; claims 197k vs 200k. **Yet 30Y ROSE +3bp to 5.23% and 10Y +2bp to 4.70% — long yields rose INTO the equity rally.** Bonds did not buy disinflation; they are pricing the Warsh credibility problem (AllianceBernstein's Winograd called the presser *"confusing and often internally contradictory"*). **DXY −0.9% is a YEN story** (USDJPY <159, yen +2.9% to a 2-month high, intervention speculation after 40-yr lows), not a US-data story. **Any "soft-landing data drove the rally" framing is NARRATIVE-UNGRADED.**

### 🔴 THE DURABILITY QUESTION (states the bear case per Rule #18)
**The China-DUV report and CXMT capacity acceleration — the catalysts that STARTED the crash — were NOT refuted today.** No follow-up, no rebuttal published 07-30. **They were out-shouted, not disproven.** Samsung's 2028-shortage guide is a supplier's forward assertion answering a supply-side structural claim; those are not the same evidentiary class. Live tail also unpriced in equities: Iran fired ballistic missiles at US forces at Muwaffaq Salti AB, Jordan (07-28, intercepted); US struck dozens of Iranian targets; Brent +7.9% then giving back to ~$90.
**Cascade: 1st order (P>80%) shorts cover, most-damaged names bounce hardest — realized today. 2nd order (P~60%, my model) Seoul gap-closes at tomorrow's open (18.78pp SKHY dislocation). 3rd order (P~40%) if China-DUV/CXMT produces ANY follow-up datum next week, the same positioning mechanics run in reverse from a higher base. 4th order (P~20%) Samsung's mobile loss becomes the template — downstream device makers guide down on memory costs, and the cost-input reclassification spreads to the names that BUY memory rather than sell it.**

**NO POSITION ACTION — user-gated.**
