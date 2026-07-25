# 2026-07-16 THU EVE — user rotation hypothesis (semis → healthcare?): FIRST COMPUTED READING (EODHD, facts-first)

**WORKFLOW: INGEST (hypothesis scoping).** User brain-dump: possible rotation out of semis into healthcare/medical-AI; named LLY ("performing well") + HeartFlow. Research agent in flight (flows/drivers/counter-case); this file holds the deterministic tape leg, computed from EODHD adjusted closes through 2026-07-15 (4 API calls, in-code returns).

## Computed relative-performance table (EODHD adjusted_close, retrieved 2026-07-16; returns computed in-code)

| Ticker | 1m | 3m | 6m |
|---|---|---|---|
| SOXX (semis ETF) | -6.8% | +38.5% | +68.3% |
| XLV (healthcare ETF) | +3.4% | +6.8% | +1.4% |
| LLY | +2.1% | +25.6% | +7.4% |
| HTFL (HeartFlow) | **-18.0%** | -6.2% | -14.3% |
| **XLV minus SOXX spread** | **+10.2pp** | -31.6pp | -66.8pp |

## Computed observations (my model, on the above)
1. Relative shift toward healthcare is REAL but exactly ~1 month old against 6 months of overwhelming semi dominance; spread decomposition: ~2/3 from semis FALLING, ~1/3 healthcare rising → signature of semi-pullback, not (yet) confirmed destination-absorbing rotation.
2. User's two examples DIVERGE: LLY strength is a 3m story predating the semi weakness (idiosyncratic candidate — agent verifying driver); HTFL, the purest medical-AI expression, is DOWN 18% in the hypothesis month — whatever flows into healthcare is NOT reaching medical-AI small caps.
3. HTFL −18% cuts the opposite way: house thesis (2026-06-10 deep-dive, Watchlist P2, AI-capex-ORTHOGONAL anti-fragility) defined staged entry conditions; name materially cheaper — re-check entry conditions vs agent catalyst scan before any read.
4. User meta-point ("by the time the falsifier hits it's too late") = Principle #44 detection-over-prediction territory → deliverable is a ROTATION TRIPWIRE with pre-registered thresholds firing EARLIER than book falsifiers, not gut-front-running. Spec lands with the agent synthesis.

## Status
OPEN — agent results + tripwire spec + cascades to follow in same-day addendum.

## SAME-DAY ADDENDUM — research agent results (1 Opus, ~58.5k) + tripwire spec

### Verdict: hypothesis PARTIALLY REAL but MIS-SPECIFIED — the user's gut detected a real institutional shift whose destination is NOT the category he named.

| Leg | Verdict | Evidence (date-pinned) |
|---|---|---|
| Broad rotation semis→healthcare | REAL but young + trim-not-exodus | **BofA FMS 2026-07-14 (T2): healthcare OW net +14%→+32% MoM (biggest add), tech cut +26%→+18%**; XLV 1m inflows +$776.9M (T3); BUT zero managers net-short tech; **SOXX +$5.4B single-day inflow 07-08** + hedge funds buying semis fastest in 3.5yrs (T2 benzinga) — two-sided tape, ~2-3 weeks old |
| LLY as rotation evidence | NO — idiosyncratic GLP-1 franchise | Foundayo (orforglipron) oral-GLP-1 FDA approval; FY26 guide RAISED $82-85B (T1 8-K); Medicare Bridge $50/mo from 07-01; first $1T-mcap pharma; JPM PT $1,400 (T3). LLY ≈15% of XLV → LLY strength CAUSES "healthcare" ETF strength — Pills≫Providers split confirmed |
| Medical-AI catching the bid | **CONTRADICTED — the subsegment is being SOLD** | ISRG −27~30% YTD (Q2 prints TODAY AMC); Tempus sliding toward 52wk low (Q2 07-30); **Lunit −34% in one month (₩14,470 06-16 → ₩9,550 07-14)**; HTFL flat = RELATIVE outperformance inside a bleeding cohort |

### 🚨 DECISION-RELEVANT CATCH (HTFL, T1): CMS dropped the CY2027 PFS proposed rule 2026-07-14 — and the companion OPPS rule ACTIVELY INTRODUCES a "Software as a Medical Service (SaMS)" framework. House entry condition #1 ("~Jul-15 passes WITHOUT adverse SaaS/algorithm methodology") is NOT cleanly cleared — it is OPEN/AMBIGUOUS pending a primary-document read of CMS-1848-P + the OPPS SaMS section (comment period to 2026-09-14; final rule later in 2026). PFS conversion factor cut ~1.2-1.7% (T1 CMS fact sheet). Also live: HTFL v. Cleerly patent suit (2026-04); Q1 rev +41% to $52.6M, FY guide raised $228-232M, fell −9.25% AH on the beat (expectations-efficiency instance); lobbying disclosures on Medicare AI-reimbursement Q1-Q2.

### ROTATION TRIPWIRE v1 (pre-registered spec — the detection-over-prediction answer to "by the time the falsifier hits it's too late")
Weekly compute (≈6 EODHD calls, inside quota; Monday wake):
- **Stage-1 CANDIDATE fires when:** XLV−SOXX 1m spread > 0 for 2 consecutive weekly readings AND XLV absolute 1m return > +2% (destination must ABSORB, not just source leak). Current state (07-16 reading): spread +10.2pp ✓ but week 1 of 2, absorption weak (+3.4% mostly ex-LLY unknown — decompose next reading).
- **Stage-2 CONFIRMED fires when:** Stage-1 + (BofA FMS healthcare OW rises AND tech OW falls a second consecutive month [next FMS ~mid-Aug]) OR semi-ETF 4-week net flows turn negative (agent-fetched).
- **Medical-AI leg (separate switch):** cohort basket (HTFL/TEM/ISRG/Lunit) 1m > XLV 1m = "category bid" — currently STRONGLY FALSE.
- Action mapping: Stage-1 = attention only; Stage-2 = BOTTLENECK-FORECAST-style review of book beta + accelerate the orthogonal-names work (HTFL entry-conditions resolution). NO book action on tripwire alone — Rule #8 unchanged; the tripwire buys LEAD TIME, it does not replace falsifiers.
- Monitor falsifier: if 3 months of weekly readings never change a decision, retire the instrument.

### Inputs the user must feed (the direct answer): almost none —
tape leg = self-serve (EODHD weekly); FMS = monthly press coverage (agent-fetched, or user screenshot if paywalled); ETF flows = agent-fetched T2/T3. The ONE user-gated item: nothing. The hypothesis is now instrumented.

### Cascades (this commit)
- `companies/HTFL/thesis.md` — entry-condition #1 status OPEN (CMS SaMS), P1 primary-doc read task; tape + Q1 + Cleerly-suit note.
- `meta/day-state.md` — tripwire armed (weekly, Mondays); HTFL CMS read = P1; ISRG Q2 prints TODAY (cohort tell).
- Ledger: 1 fire ~58.5k HIGH (FMS datapoint + Pills/Providers decomposition + medical-AI counter-tape + the CMS SaMS catch — the single decision-relevant fact vs the Jun-10 thesis).

**Position implication: NO ACTION on the book (semis legs unchanged — the rotation evidence is trim-not-exodus and 2-3 weeks old vs TSMC's same-day +15% capex raise on fundamentals); HTFL stays Watchlist P2 with entry-condition #1 now OPEN-pending-CMS-read (NOT passed, NOT failed) — the primary-doc read is the gating work item, docketed P1; user's gut booked as a correctly-detected institutional shift with a mis-identified destination.** 🟡
