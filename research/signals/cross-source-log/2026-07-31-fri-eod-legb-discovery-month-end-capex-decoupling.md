# 2026-07-31 (Fri) EOD — LEG-B DISCOVERY: capex dollars have decoupled from capex units, and my own falsifier is keyed to the wrong instrument

**Workflow:** EOD CONDITIONAL SYNTHESIS — **FULL PATH** (condition check computed: 0 commits since 16:00 UTC, last was 10:33 → evening quiet → discovery leg fires)
**Leg:** ONE unanchored Leg-B agent, evening/month-end press sweep, structural-signal filter
**NO POSITION ACTIONS — user-gated.**

---

## §1 — THE TAPE: the day's real signal is the intraday shape, not the closes

**07-31 US closes (T1 Finnhub, cross-checked vs CNBC — 12/12 match):**

| | Close | Day % | **July %** |
|---|---|---|---|
| S&P 500 | 7,489.72 | +0.70% | **−0.13%** |
| Nasdaq Comp | 25,373.85 | +1.00% | **−3.20%** |
| Dow | 52,485.03 | +0.53% | **+0.32%** |
| **SOX** | 11,311.08 | +0.07% | **−20.61%** |
| SOXX | 504.89 | +0.07% | **−21.21%** |
| SMH | 540.53 | +0.30% | **−17.59%** |

**🔑 The single most informative table of the day — where each name closed relative to its own high:**

| Closed within 0.7% of the high | Gapped up and sold all day |
|---|---|
| AMZN **+15.32%** (−0.6% from high) | **SNDK −5.09%** (gave back **13.5%**) |
| GOOGL **+6.73%** (−0.7%) | **MU −5.90%** (gave back **11.6%**) |
| META +3.28% (−0.3%) | **BE −0.63%** (gave back **12.6%**) |
| MSFT +3.02% (−0.5%) | **CORZ −5.00%** (gave back 9.9%) |
| NVDA +2.93% (−0.6%) | **IREN −3.82%** (9.8%) · **CRWV −2.88%** (8.6%) · **NBIS +1.05%** (6.9%) |

**Every mega-cap platform closed on its high. Every memory / neocloud / power name gapped up 5-11% on the Korea rally and was sold relentlessly into the close.** SOXX was +5.6% at its high and closed +0.07%.

**That is a distribution signature on the last trading day of the month**, and it is the same cohort split the whole week has been about — recipients and levered small-caps sold, self-funding platforms bought.

**⚠️ Month-end effect: real, but I cannot size it and will not invent a number.** The classic pension mechanic was *muted* (equities did not outperform bonds — S&P −0.13% while the 30Y sold off to a 19-year high). The *within-equity* mechanic was enormous: **SOX −20.6% vs Dow +0.3% = ~21pp of one-month dispersion**, and the Morgan Stanley Momentum TMT index fell **−53.5%** in July (T2). Any fixed-weight momentum or risk-parity sleeve had to trade at month-end. **DATA GAP: no dated 07-31 GS/JPM flow estimate — the figures search surfaces are other months and must not be carried across.**

**🔴 THE UNRESOLVED THING, and it is the most interesting on the tape:** KOSPI printed **+17.91%**, its largest single-day gain ever, with Samsung +28% and SK Hynix +30% — **and US-listed memory closed RED the same session** after gapping up. Same assets, same day, opposite directions. **The Korean bounce was a local unwind of local forced selling; the US marginal seller was still selling.** The Korean tape cannot be used as a read-through to US memory this week.

---

## §2 — 🔴 THE FINDING THAT BREAKS MY OWN INSTRUMENT: capex dollars ≠ capex units

### §2.1 — Amazon raised capex and named MEMORY PRICES as the reason

**AMZN raised 2026 capex $200bn → $220bn** (+10%) on the Q2 call. Jassy's stated reason: **"rising memory prices pushed its capex estimate higher"** — and *"even at that amount, we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027 too."* (T2 CNBC, 2026-07-30.) Meta's raise to $125-145bn was likewise attributed partly to **higher component costs**.

**Mechanism:** a **cost-push** increase in the capex line is not the same signal as a **volume-push** increase, but the market reads the headline number identically. It persists as long as memory is the pinch — it is a **pricing-power transfer from buyer to supplier that appears as a bigger number on the buyer's income statement.**

**⇒ "Hyperscaler capex is up" is no longer a clean proxy for physical AI buildout.** Any forecast multiplying capex dollars by a stable $/unit is now **biased high on units**.

**For our cohort this is the recipient side of the same coin:** the increment Amazon is paying is being **captured by memory suppliers**. The buyer's rising cost line *is* our names' revenue.

### §2.2 — 🔴 Microsoft held capex flat while adding $132.5bn of lease commitments

**Not-yet-commenced lease commitments: $196.6bn → $329.1bn in one quarter**, with **>$130bn of new data-centre leases signed** — while **capex guidance was MAINTAINED** (T2 Bloomberg / Investing.com, 2026-07-29). 31 new data centres in the quarter, 88 in the fiscal year; Nadella targeting a doubling of capacity over two years.

**Mechanism:** spending is migrating **off the capex line** — the number every analyst models and every capex-cut falsifier is written against — **into lease commitments**, which sit in a footnote and convert to opex over time.

**🔴 THIS DIRECTLY BREAKS MY OWN FALSIFIER.** `meta/hyperscaler-reward-function-v2.md` §7-§8 name *"a hyperscaler cuts capex"* as the single event that ends recipient insulation. **A company can hold or cut the capex line while total forward obligation accelerates.** My falsifier would read "spending intact" from a number that no longer measures spending.

**Same error class as the KIOXIA unfireable falsifier booked this morning — a falsifier keyed to an instrument that cannot register the event it is meant to detect. N=2 in one day makes it a pattern.**

**RE-SPEC REGISTERED:** the trigger is a decline in **TOTAL FORWARD COMMITMENT** = capex guidance **+** not-yet-commenced leases **+** off-balance-sheet JV/SPV financings. **Anything keyed to the capex line alone is retired.**

---

## §3 — TWO ITEMS THAT TOUCH LIVE FALSIFIERS

### §3.1 — 🔴 China's domestic immersion DUV is now DATED, and CXMT is a named recipient

A Shanghai state-backed manufacturer has begun **mass production of immersion DUV lithography**, with **first deliveries this year to SMIC, Hua Hong and CXMT**; target ~5 machines in 2026, ~20 in 2027. Most components domestic; some critical parts still Japanese. ASML ships ~130 immersion systems in 2026 (T2 The Information/Reuters/TrendForce, 2026-07-27/28).

**This is not an ASML revenue event in 2026-27** — 5 and 20 tools against 130. **It is the removal of an export-control chokepoint on China's memory expansion path.** This morning I listed second-sourcing as bypass route #1 and marked it *"live, ramping."* **It now has a date, a tool count and a named recipient.** It is a **tool-access** milestone, which sits *upstream* of the DDR5-8400/LPDDR5X-12000 performance milestone our CXMT falsifier is written against — i.e. our falsifier watches the downstream symptom and this is the upstream cause. 🔴 Route to the CXMT monitor.

### §3.2 — SK Hynix is raising capex ≥50% — the first hard capacity response

FY26 capex to the **"high-KRW-40tn"** range (~$31bn), **+≥50% YoY**, with M15X and Yongin Fab One **pulled forward**, alongside a record Q2 (revenue ₩79.3tn, OP ₩60.5tn, **76% operating margin**, HBM4 in mass production, ~58% HBM share) (T1 SK hynix newsroom, 2026-07-28).

**The entire structural-DRAM thesis rests on suppliers NOT racing to add capacity because 70%+ margins reward restraint. This is the first hard capacity response.**

**⚠️ I am flagging it, not resolving it.** The pre-committed trim sequence keys off **ASP rollover (F2)**, not capex announcements, and a company printing a 76% operating margin is not in distress. But it belongs in front of the **F1 supplier-discipline monitor**, and "capex up 50%" is exactly what the *beginning* of a discipline break looks like from the outside.

---

## §4 — OTHER STRUCTURAL ITEMS (mechanism stated, lower model-impact)

| Item | Mechanism | Tier/date |
|---|---|---|
| **Strait of Hormuz functionally closed** — 10 transits (07-21) vs >130/day pre-war; war-risk premium **7.5-10% of hull** vs ~0.25% pre-hostilities = **~30-40×** | **Insurance capacity, not naval capacity, is the binding constraint.** Underwriters withdrawing cover closes a strait more effectively than mines. QatarEnergy bought **33 US LNG cargoes** to offset; Shell profit more than doubled to $9.8bn | T2, **07-17→07-23 — 8-14 days stale, do NOT present as tonight's state** |
| **Drone strike ignited a fire on two gas vessels at Egypt's Damietta port** | Energy-infrastructure attacks have widened to the **Mediterranean** end of the Suez route, not just Hormuz. 2nd order (P~60%): Suez war-risk follows Hormuz | T2 Reuters, 07-30 |
| **Data-centre debt is now a distinct structured-finance class** — Meta/Blue Owl/PIMCO **$27.3bn** for a 2GW Louisiana campus; 144A issuance; JVs engineered so financing is **not consolidated as debt** | Combined with §2.2, the true consolidated obligation behind AI capacity is **systematically understated by the metrics in common use**. The accounting treatment is the *point* of the structure | T2, **mid-2026, several undated — CONTEXT ONLY** |
| **100% Section 232 tariffs on patented pharma + APIs effective TODAY** | An **onshoring subsidy priced as a penalty** — the 20% reduced tier for approved onshoring plans is the actual instrument. Same policy architecture now applied to semis; **register the tiering-by-onshoring-plan design as a reusable pattern** | T2, effective 2026-07-31 |
| **NXP in talks to acquire Ambarella** | Edge-inference silicon consolidating into an automotive/industrial incumbent — consistent with the TC-19 edge-inference thread | T2, 07-31 |
| **BOJ defended the yen near 160 while holding rates; RBI sold ~$7bn defending the rupee** | Two Asian central banks burning reserves within 48h against a rising-US-yield backdrop | T2, 07-30/31 |

---

## §5 — 🔴 DATA GAPS AND CORRECTIONS (stated, not filled)

1. **The EODHD same-day EOD row printed stale AGAIN** — GSPC 7,479.20 vs actual 7,489.72; SOXX 505.50 vs 504.89. **Vendor defect reproduced; verified closes used for every numerator.** N+1 on the documented family.
2. **No single-name July returns** — exact 07-31 closes obtained but no verified 06-30 single-name bases (EODHD quota discipline). Circulating press figures (SNDK "−45% in a month", MU "−26.82%") have **inconsistent measurement windows and were NOT used.**
3. **Russell 2000 July −3.08% is the IWM ETF proxy**, not the index — `RUT.INDX` returned empty. Labelled as proxy.
4. **No credit-spread or CDS route.** Given §2.2 and the structured-finance item, **this is now a MATERIAL gap, not a theoretical one** — it is the single highest-value data upgrade available to the harness.
5. **Alphabet's actual 2026 capex guidance is UNRESOLVED** — "$180-190bn" and "as much as $205bn" both circulating, $15-25bn apart. Needs the 8-K.
6. **No post-16:00 ET tape**; **no current Hormuz transit count** (latest 07-21); **no oil settle** (route still absent — no price stated).
7. **🔴 Press semi-return figures are mutually inconsistent and should be treated as suspect this weekend:** circulating "SOX −21% / worst since Dec 2002", "SMH −19% / worst since 2008", "SOXX −23% / biggest since 2021", "SOXX −27.43% / worst since Sept 2001", "SOX −28.6% from the June 22 peak." **Our computed figures from verified 06-30 and 07-31 closes: SOX −20.61%, SOXX −21.21%, SMH −17.59%.** The −28.6% is peak-to-trough being quoted interchangeably with a monthly return.
8. **Two stale-headline traps caught and quarantined:** a DOE $17.5bn nuclear-loan story (**2026-06-23**) and Meta's 6.6GW nuclear agreements (**2026-01**) both surfaced in a search for "July 31 2026 nuclear announcement" and read as current. Neither used.

---

## §6 — POSITION IMPLICATIONS (user-gated)

**Memory cohort (SKHY / HYNIX / MU):** **HOLD — no size change.** §2.1 is *recipient-positive* — Amazon's extra $20bn is being captured by memory suppliers, which is our names being paid more. But §3.2 (SK Hynix capex +≥50%) is the first genuine supplier-discipline datapoint pointing the wrong way, and §3.1 gives the China bypass a date. **Neither fires a written falsifier; both belong in front of the F1 monitor.** 🟡

**SUMCO / MURATA:** **NO ACTION — decision packages due pre-Aug-6.** §3.2's capex step-up is *revenue* for the semicap and wafer layer — a supplier-discipline break is bearish for memory ASPs and bullish for whoever sells the tools and wafers. **That tension belongs in both packages explicitly.** SUMCO interim 08-06. 🟡

**BE (not held):** **NO ACTION.** Raise-and-beat of substantial magnitude, and the stock gave back 12.6% from its high to close red. See the grade in `predictions/lessons.md`. 🟡

**Instrument-level (the real output of this leg):** the capex-cut falsifier is **retired in its current form** and re-specified against total forward commitment. That is a harness change, not a position change, and it is the most valuable thing this sweep produced.
