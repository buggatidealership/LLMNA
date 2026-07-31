# 2026-07-31 (Fri) — MPWR Q2'26: the recipient-side test of whether hyperscaler capex is landing as UNITS

**Workflow:** INGEST + TRACE
**Origin:** operator request — *"check on monolithic power systems is there any mention of that company in the harness… And then I think they reported earnings, so it would be interesting to see what another company that we haven't been following that closely is revealing about markets."*
**Why this name is analytically valuable:** MPWR is a **RECIPIENT** in the recipient/payer taxonomy (`2026-07-31-ai-complex-deleveraging-size-tested.md`) that the harness has **never held, never thesis'd, and never anchored on** — 11 corpus mentions, all as VICR's competitor or as a T9 watchlist line. No confirmation bias to correct for. It sells **parts per socket**, not dollars of capex, which makes its print the cleanest available instrument on tonight's open question: **is hyperscaler capex growing in DOLLARS only (COST-PUSH) or in UNITS (VOLUME-PUSH)?** (`2026-07-31-fri-eod-legb-discovery-month-end-capex-decoupling.md`)

---

## TL;DR

🟢 **The capex is landing as physical component demand, and the channel is empty, not full.** MPS raised its full-year Enterprise Data growth **floor from 85% → 130%** mid-year and cited **low channel inventory and continued sell-through**; days-of-inventory fell 17 days *while* inventory dollars rose. That is a demand-pull signature, not channel stuffing.

🟢 **93.1% of all YoY revenue growth came from two AI-exposed lines.** The rest of the semiconductor economy inside MPS (automotive, consumer, industrial, storage) contributed 6.9%. The AI capex is **not broadening into the real economy — it is narrowing and intensifying.**

🟢 **There is no AI gross-margin premium.** AI/enterprise-data mix went from 21.7% → 38.8% of revenue over four quarters and non-GAAP gross margin moved **+0.1pt** (55.5% → 55.6%). AI power content is priced at the corporate average. All operating leverage came from opex scale, not price.

🟡 **The market took the proof and refused to extrapolate it.** MPWR opened +13.89%, printed +19.15% intraday, and closed **+8.35%** — surrendering 56% of the peak gain in a single settled session.

---

## §1 — Corpus check (the operator's first question, answered plainly)

**11 files mention MPWR. There has never been a `companies/MPWR/` folder, a thesis, or a position.** Chronology:

| Date | Where | What it said |
|---|---|---|
| (undated, VICR build) | `companies/VICR/thesis.md:35,40`, `facts.md:86,92`, `exposures.md:52,54,72` | **The deepest context.** MPWR **designed VICR out of NVIDIA H100**; "lower-cost silicon-integrated solutions; structural cost advantage; growing share at hyperscalers." A long-VICR/short-MPWR pair trade was considered and rejected as *"asymmetric in the wrong direction."* |
| 2026-05-31 | `cross-source-log/2026-05-31-nvda-n1x-unbiased-money-flow-analysis.md:46,121` | "high-conviction non-consensus name in laptop PMIC" — premium 80W mixed-rail VRM = pricing power |
| 2026-06-06 | `watchlist/candidates.md:1126`, `sector/where-we-are.md:426`, `sector/themes.md:195` | Added to watchlist under **T9 Consumer Hardware AI Swap** — i.e. filed under the *AI-PC* thesis, not the *datacenter* thesis |
| 2026-06-07 | `cross-source-log/2026-06-07-triple-brief-plus-npo-unified-cascade.md:190` | T9 deployment candidate for "next cash window" |
| 2026-06-25 | `cross-source-log/…trendforce-800v-hvdc-power-cascade.md:185,187,194` | "POTENTIAL WATCHLIST P3 candidate — IVR (integrated voltage regulator)"; flagged as the **substitution risk to MURATA's MLCC count** and to discrete PMIC stacks |
| 2026-07-02 | `cross-source-log/2026-07-02-oblivious-layer-program-wave1-nominations.md:6` | Listed as already-discovered ("Vicor +179% YTD / MPWR ATH") |

**The retrieval error this exposes:** we filed MPWR under **T9 Consumer Hardware AI Swap (laptop PMIC)** on 2026-06-06 and under **IVR-substitution-risk** on 2026-06-25. Both framings are peripheral. The actual business is now **38.8% datacenter power**, and datacenter is **93% of its growth**. We had the name, filed it in the wrong drawer, and never re-based it. Lesson candidate below.

---

## §2 — The print (T1, SEC 8-K Ex-99.1, filed 2026-07-30)

Source: [SEC 8-K accession 0001628280-26-051029, Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1280452/000162828026051029/mpwr-20260630xexx991.htm) — filing-grade, fetched via `meta/tools/edgar_client.py`.

| GAAP | Q2'26 | Q1'26 | Q2'25 | QoQ | YoY |
|---|---|---|---|---|---|
| Revenue ($M) | **980.6** | 804.2 | 664.6 | +21.9% | +47.6% |
| Gross margin | 55.2% | 55.3% | 55.1% | −0.1pt | +0.1pt |
| Operating margin | 31.0% | 30.0% | 24.8% | +1.0pt | +6.2pt |
| Diluted EPS | $5.22 | $3.92 | $2.81 | +33.2% | +85.8% |

| Non-GAAP | Q2'26 | Q1'26 | Q2'25 |
|---|---|---|---|
| Gross margin | **55.6%** | 55.5% | 55.5% |
| Operating margin | 37.5% | 35.8% | 34.8% |
| Diluted EPS | **$6.50** | $5.10 | $4.21 |

**Revenue by end market ($M):**

| End market | Q2'26 | Q1'26 | Q2'25 | QoQ | YoY | % of rev |
|---|---|---|---|---|---|---|
| **Enterprise Data** | **380.6** | 262.8 | 144.0 | **+44.8%** | **+164.3%** | 38.8% |
| Storage & Computing | 199.8 | 174.4 | 195.3 | +14.6% | +2.3% | 20.4% |
| Automotive | 157.1 | 152.4 | 145.1 | +3.1% | +8.2% | 16.0% |
| **Communications** | **131.5** | 111.5 | 73.8 | +18.0% | **+78.3%** | 13.4% |
| Consumer | 56.8 | 54.5 | 59.7 | +4.2% | **−4.8%** | 5.8% |
| Industrial | 54.8 | 48.6 | 46.7 | +12.7% | +17.3% | 5.6% |
| **Total** | **980.6** | 804.2 | 664.6 | +21.9% | +47.6% | 100% |

**Q3'26 guide:** revenue **$1,140–1,160M** (midpoint +17.3% QoQ on top of a +21.9% QoQ quarter); non-GAAP GM 55.4–56.0%; buyback authorization raised +$500M to $1B.

**Balance-sheet quality (the part nobody reads):**

| | Q2'26 | Q1'26 | Q2'25 |
|---|---|---|---|
| Inventory ($M) | 675.8 | 619.2 | 490.6 |
| **Days of inventory (current-qtr rev)** | **140** | 157 | 150 |
| **Days of inventory (next-qtr rev)** | **121** | 128 | 135 |
| Days sales outstanding | **32** | 34 | 27 |
| Operating cash flow ($M) | 227.9 | 250.3 | 237.6 |

**Management, verbatim-adjacent (T1 filing):**
- *"We extended our capacity goal significantly beyond $6B"* — against a current annualised run-rate of ~$4.6bn on the Q3 guide midpoint. A **supplier committing its own capex ~30% ahead of its own run-rate.**
- *"We began sampling High Voltage AC to DC products for 800V data center architectures"*
- *"We received initial orders for high-speed DDR5 memory components"*
- *"All end markets grew sequentially with Enterprise Data growing 45% as we continued to see strong, broad-based ordering patterns."*

**From the call (T2, [Investing.com transcript summary](https://www.investing.com/news/transcripts/earnings-call-transcript-monolithic-power-systems-tops-q2-2026-estimates-93CH-4826411) / [GuruFocus](https://www.gurufocus.com/news/8993586/monolithic-power-systems-inc-mpwr-q2-2026-earnings-call-highlights-record-revenue-and-raised-enterprise-data-outlook)):** management **raised the full-year Enterprise Data growth floor from 85% to 130%**, citing **low channel inventory and continued sell-through**. Hsing: *"MPS is transitioning from a chip company, a semiconductor company to be a semiconductor-based solution providers."*

---

## §3 — The four computed reads (Principle #43b — compute, don't narrate)

### 3.1 — Growth attribution: 93.1% of the YoY increase is two AI lines

```
Total YoY revenue increase       = 980.6 − 664.6 = $316.0M
  Enterprise Data                = 380.6 − 144.0 = $236.6M
  Communications                 = 131.5 −  73.8 =  $57.7M
  ─────────────────────────────────────────────────────────
  AI-exposed subtotal            =                 $294.3M  →  93.1% of all growth

  Storage & Computing            = 199.8 − 195.3 =   $4.5M
  Automotive                     = 157.1 − 145.1 =  $12.0M
  Industrial                     =  54.8 −  46.7 =   $8.1M
  Consumer                       =  56.8 −  59.7 =  −$2.9M
  ─────────────────────────────────────────────────────────
  Everything else subtotal       =                  $21.7M  →   6.9% of all growth
```

🟢 **Read:** inside one diversified analog supplier, the AI complex and the non-AI economy are running at **+164%/+78% versus +2%/+8%/−5%**. The capex boom is **not** spilling into the broader semiconductor cycle. Anyone modelling "AI lifts the whole analog cycle" is wrong at the segment level, at T1, tonight.

### 3.2 — The AI gross-margin premium does not exist

```
AI (Enterprise Data) mix:  Q2'25  144.0/664.6 = 21.7%
                           Q2'26  380.6/980.6 = 38.8%      Δ = +17.1pt
Non-GAAP gross margin:     Q2'25  55.5%  →  Q2'26  55.6%   Δ = +0.1pt
```

🟢 **Read:** a **+17.1pt mix shift into AI moved gross margin by 0.1pt.** Datacenter power management is sold at the corporate-average margin. The entire operating-margin expansion (+2.7pt YoY non-GAAP) is **opex leverage on a fixed R&D base**, not pricing power. This is the direct counter-evidence to the reflexive assumption that AI content carries premium pricing at the component layer — and it is the same shape as the token-economics premise inversion booked yesterday (`2026-07-30-thu-two-spend-framework…`): **the margin is in the cost line and the scale, not in the ASP.**

### 3.3 — Inventory says demand-pull, not channel-stuffing

```
Inventory dollars:  619.2 → 675.8   (+$56.6M,  +9.1%)
Days of inventory:      157 → 140   (−17 days)
Forward DOI:            128 → 121   (−7 days)
DSO:                     34 → 32    (−2 days)
```

🟢 **Read:** inventory grew 9.1% while revenue grew 21.9% — **stock is being consumed faster than it is built**, on both the trailing and the forward basis, with receivables *also* tightening. The classic false-beat signature (inventory days rising, DSO rising, revenue pulled into the channel) is **absent on all three axes**. Management's "low channel inventory" claim is corroborated by its own balance sheet, which is the strongest form this claim can take.

### 3.4 — The reaction: a beat that got faded (T1, settled session)

Source: Finnhub `/quote`, session settled 2026-07-31 16:00 ET (L42-b basis stamp satisfied).

| | Prev close (07-30, pre-print) | Open | Intraday high | **Close (07-31)** |
|---|---|---|---|---|
| **MPWR** | $1,316.18 | $1,499.00 (+13.89%) | $1,568.21 (+19.15%) | **$1,426.03 (+8.35%)** |
| **VICR** | $206.67 | $220.16 (+6.53%) | $224.00 (+8.39%) | **$207.37 (+0.34%)** |

🟡 **Read (MPWR):** the market **retained 43.6% of the peak gain** (8.35 / 19.15). A record quarter, a 45-percentage-point mid-year guidance-floor raise, a doubled buyback — and more than half the pop sold. On the reward-function ledger this is the **highest-proof / lowest-ask cell** we have observed this cycle (MPS asks for no capex forbearance; it *funds* its own capacity and simultaneously raises the buyback) and it still faded. That is a **regime datum about the buyer, not about MPS**: at these levels the marginal bid is not paying up for confirmed AI proof.

🟢 **Read (VICR):** VICR gapped +6.53% on read-across and **round-tripped 94.8% of the open gap to close +0.34%.** The market explicitly refused to award MPS's beat to Vicor. This is a direct market-priced confirmation of the standing VICR thesis line — *"MPS has structurally won the current generation"* — and it re-prices the pair-trade note in `VICR/exposures.md:54` as correct.

---

## §4 — Hypotheses (what this print does and does not settle)

**The question it was fired at:** hyperscaler capex dollars rose in Q2 while capex *units* may not have (COST-PUSH vs VOLUME-PUSH, booked tonight in the EOD Leg-B artifact). MPS is paid per socket, so its revenue cannot inflate on HBM/wafer price alone.

| | Hypothesis | Prior (tonight, pre-MPWR) | Posterior | What moved it |
|---|---|---|---|---|
| **H-A** | Capex growth is substantially **VOLUME** — real incremental systems shipping | ~50% | **🟡 72%** | +164% YoY in a per-socket business; DOI down 17d; capacity goal raised beyond $6B; Comms +78% on optical modules/switches (a *different* socket set, same direction) |
| **H-B** | Capex growth is substantially **COST-PUSH** — same units, higher memory/wafer prices | ~35% | **🟡 18%** | Cost-push cannot produce a 45pp mid-year raise in a supplier's own unit-driven growth floor, nor destock the channel |
| **H-C** | MPS's number is **share gain**, not end-market growth — it overstates the market | ~15% | **🟡 40%** *(not mutually exclusive with H-A)* | Unresolved from this print alone. MPS has been taking sockets from TI/ADI/Infineon since the H100 design-out. **This is the honest limit of the instrument.** |

**1st order (P>80%):** AI server/rack power-management content is shipping in volume, and the component channel is lean going into Q3.
**2nd order (P~60%):** the Q3 guide (+17.3% QoQ) implies the *build* is accelerating into Q4, not flattening — which is consistent with hyperscaler forward commitments being physical, not accounting.
**3rd order (P~40%):** the flat gross margin means hyperscalers are **capturing the component-layer surplus**. If AI power content earns corporate-average margin at a company with MPS's design-win position, the pricing power in this layer sits with the buyer. Analog suppliers are volume plays here, not margin plays.
**4th order (P~20%):** MPS sampling **800V AC-DC** and taking **initial DDR5 high-speed memory-component orders** is a supplier expanding SAM *into* the next architecture before the current one peaks — the behaviour of a firm that believes the 2027-28 build is real.

---

## §5 — Falsification pass (Critical Rule #18 — the strongest case against my own read)

1. **The share-gain confound (strongest, UNRESOLVED).** MPS designed VICR out of H100 and has been winning sockets from the incumbent analog majors. Some unknown share of +164% is share, not market. *Why it does not kill the read:* share gain still requires **physical sell-through** — it cannot simultaneously destock the channel by 17 days and tighten DSO. Share gain changes *who* ships the units; it does not manufacture units that were never ordered.
2. **Content-per-unit confound.** Higher rack power density = more phases per GPU = more MPS content per system. So **MPWR revenue ≠ GPU unit count**. Correct, and I am stating the weaker claim deliberately: this print evidences that **physical silicon shipped into AI systems is growing fast**, which is still decisively not the COST-PUSH story.
3. **"Floor" ≠ point estimate.** The 85%→130% move raised a *floor*. Part of the delta is catch-up to a conservatively-set initial floor, not pure incremental news. *Mitigant:* 45 percentage points is too large to be entirely floor-conservatism, and management attached a mechanism (channel inventory) rather than a hand-wave.
4. **The tape disagrees with me.** A +56%-of-peak fade is the market saying "known." If this were the clean incremental signal I am calling it, the close would not have been half the high. *This is the honest tension and I am not resolving it in my favour* — see §3.4: I read the fade as a statement about the **marginal buyer's price**, not about the **fundamental**, and I flag that as the interpretation most likely to be wrong.
5. **Instrument-validity check (the K3 commission, applied to my own new falsifier).** Can the falsifier below actually fire? Yes — Enterprise Data revenue and days-of-inventory are both disclosed quarterly at T1 by this issuer. This one is not blind the way the capex-cut falsifier was (`hyperscaler-reward-function-v2.md` §9).

---

## §6 — What this changes in the corpus

| File | Change | Tier |
|---|---|---|
| `companies/MPWR/` | **CREATED** — thesis + facts. First folder, on first real ingest (per CLAUDE.md universe rule) | 🟡 Watchlist |
| `companies/VICR/thesis.md` | Back-reference + the 07-31 read-across round-trip as market-priced confirmation of the "MPS won current gen" line | 🟢 |
| `sector/themes.md` T9 | MPWR **re-based out of the AI-PC/consumer drawer** — 38.8% of revenue and 93% of growth is datacenter | 🟡 |
| `2026-06-25 …800v-hvdc-power-cascade.md` | **T2 → T1 upgrade on timing:** MPS confirms 800V AC-DC products are *sampling* as of Q2'26. Revenue 2027-28. The cascade's timeline holds | 🟢 |
| `predictions/lessons.md` | **L53 candidate — RETRIEVAL-DRAWER ERROR** (see below) | 🔴 candidate |

### L53 candidate — the retrieval-drawer error

> A name filed under the wrong theme is functionally invisible, even when it is in the corpus and even when it is in the watchlist. MPWR was logged three separate times (2026-05-31 laptop PMIC / 2026-06-06 T9 consumer hardware / 2026-06-25 IVR substitution *risk*) and never once under datacenter power — the segment that is now 38.8% of its revenue and 93% of its growth. **All three filings were correct at the time and all three were peripheral.** The failure is not intake, it is **re-basing**: nothing in the harness re-checks whether a watchlist name's *primary* drawer is still its primary drawer.
>
> **Distinct from B60 (anchored-ingest)** — that is about the framing of *new* data. This is about the **decay of a correct old classification**. Same shape as the MURATA re-basing item already open (price-flow-through → volume/utilisation/datacenter-mix).
> **N=2 as of tonight (MPWR, MURATA) → promotable.** Proposed instrument: at each monthly audit, for every watchlist/held name, re-derive the primary drawer from the *latest reported segment mix* rather than from the drawer it was entered in.
> **Falsifier:** if a 30-day pass produces zero drawer changes across the watchlist, the check is decorative — retire it.

---

## §7 — Position implications

**MPWR** — 🟡 **Position implication: NO ACTION — no entry — WATCHLIST retained, drawer re-based from T9-consumer to datacenter-power.** The business quality is confirmed at T1 (record quarter, lean channel, self-funded capacity, no AI margin premium *needed* to work), but three things gate an entry: (a) the stock closed +8.35% at $1,426 after a 19.15% intraday high — the fade is exactly the "confirmed proof does not get paid" regime datum, so this is a poor entry tape; (b) the **share-gain vs end-market ambiguity (H-C 40%) is unresolved** and is the whole thesis; (c) no capacity in the book — the €160k reserve floor and existing cohort take priority. **Re-eval trigger:** Q3'26 print (late Oct) — specifically whether Enterprise Data holds >130% growth *and* DOI stays ≤125 forward days.

**VICR** — 🟢 **Position implication: NO ACTION — no position, no entry — the 07-31 read-across round-trip (+6.53% open → +0.34% close) is market-priced confirmation of the existing thesis line that MPS has structurally won the current generation.** The long-VICR/short-MPWR pair-trade note at `exposures.md:54` is graded **correct in its rejection**. VICR's case remains a next-generation binary (2nd-gen VPD at >3 A/mm²), unchanged tonight.

**MURATA (held)** — 🟡 **Position implication: HOLD — no size change — but the IVR substitution risk flagged 2026-06-25 now has a live, funded, sampling competitor.** MPS raising its capacity goal beyond $6B and sampling 800V AC-DC is the substitution vector that reduces MLCC count per server. This does not fire a falsifier at this timeline (800V revenue is 2027-28), but it is a **named input to the pending MURATA re-basing** due pre-Aug-6. Do not let the re-basing land without pricing this.

**Hyperscaler cohort (MSFT/META/AMZN/GOOGL)** — 🟡 **Position implication: NO ACTION — but the open MSFT timing-vs-over-build question moves.** MPS's lean channel and +17.3% QoQ guide is evidence *against* the over-build reading (over-build shows up first as component channel congestion, and the channel is emptying). **H1 timing 55% → 62%; H2 over-build 35% → 28%; H3 10% unchanged** 🟡 (my model, single-instrument update — one supplier is not a cohort; do not treat as settled).

---

## §8 — What I could not get

- **WebFetch 403 wall held on all press domains** (fool.com, stockstory.org, stocktitan.net, gurufocus.com, investing.com) — consistent with the standing infrastructure constraint in `meta/data-access.md`. The **primary numbers are unaffected** (T1 via SEC EDGAR); only the call Q&A color routes through WebSearch summaries at T2.
- **Customer concentration** not disclosed in the 8-K exhibit — would need the 10-Q. Material to H-C (share gain vs market): if Enterprise Data is one hyperscaler, the read is far narrower than I have priced it. **Open item.**
- **Q3'25 Enterprise Data** not in the release, so the Q3 guide cannot be decomposed YoY by segment.
