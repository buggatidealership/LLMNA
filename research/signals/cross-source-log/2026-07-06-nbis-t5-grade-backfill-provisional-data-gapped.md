# 2026-07-06 — NBIS T+5 inclusion grade — PROVISIONAL BACKFILL (data-gapped)

**Trigger:** 2026-07-06 harness audit found the T+5 grade (due 2026-06-27 per `predictions/2026-06-19-NBIS-nasdaq-100-inclusion-pre-registration.md`) never ran, and the T+0 anchor (2026-06-22 inclusion-day open) was never captured. Backfilled today, 9 days late, ahead of tomorrow's T+15 checkpoint. 2 verification subagents (price-window + catalyst-register) per Critical Rule #16.

**⚠️ DATA-QUALITY BANNER:** all aggregator pages (Yahoo/StockAnalysis/MarketBeat/Nasdaq/WSJ) returned HTTP 403 in this environment; every price below is search-summary grade (**T2-minus, unverified**). The load-bearing T+0 anchor (06-22 open AND close) is **UNOBTAINABLE** from accessible sources. This grade is PROVISIONAL until broker-grade numbers (user DeGiro export or equivalent) lock the anchors — required before the T+30 PRIMARY ADJUDICATION (2026-07-22).

## Price record as obtained (all T2-)

| Date | Session | Close | Notes |
|---|---|---|---|
| 06-22 (T+0, inclusion) | Mon | **UNAVAILABLE** (open + close both) | intraday ATH $299.86 printed this day; "modest pullback from high" per sources |
| 06-23 (T+1) | Tue | ~$275.25-275.50 | |
| 06-25 (T+3) | Thu | ~$256.63 | |
| **06-29 (T+5 by trading-day count)** | Mon | **$261.15** | 06-27 was a SATURDAY — the pre-registration's "T+5 ~2026-06-27" was a calendar-count error; correct T+5 trading day = 06-29 |
| 07-01 | Wed | $229.18 (−17.01%) | Meta-Compute Bloomberg story (NBIS-specific independent catalyst) |
| 07-02 | Thu | **$215.62** (window trough; AH $215.89) | cohort-wide selloff day (KOSPI −7.89%) |
| 07-03 | Fri | MARKET CLOSED | Jul-4 observed — NOT a shortened session |

## Anchor contradictions flagged (do NOT silently overwrite)

1. **On-file "06-26 reference $275.50" (the −15% trim-falsifier base) is likely MIS-DATED** — sources tie $275.50 to 06-23, and the 06-25 (~$256.63) / 06-29 ($261.15) closes make a 06-26 close of $275.50 implausible. Needs broker verification; re-date if confirmed.
2. **On-file "07-02 close $211.12 (5-source convergence)" vs today's $215.62 (T2-)** — ~2.1% gap. **Decision-impact: NONE** — both numbers are far below the $234.18 trim trigger; the falsifier breach and the executed exit stand under either value. Precision matters only for the T+30 return math.

## Provisional T+5 read (vs pre-registered H1-H4)

- No T+0 anchor → strict band classification impossible. Proxy read: from the T+1 close (~$275.4) to T+5 ($261.15) = ~−5.2% (my model, T2- inputs); from the 06-22 intraday ATH ($299.86) = ~−12.9%.
- **Provisional bucket at T+5: H2-zone entry (attenuated pullback, −5 to −15%)** — 🟡 DIRECTIONAL, anchor-gapped.
- **INPUT-layer finding (pre-registration defect, logged for the T+30 grade):** the confound clause modeled only POSITIVE independent catalysts (H4: "rallies +15%+ on independent AI-demand catalysts"). The actual window delivered a large NEGATIVE independent catalyst — Meta-Compute (07-01, NBIS −17%, T2 multi-source) plus a cohort-wide macro day (07-02). A naive "post-inclusion pullback" reading would spuriously credit inclusion microstructure for what the catalyst register shows is fundamental + macro. The H-buckets cannot cleanly adjudicate B48/R2 unless the T+30 grade separates pre-07-01 drift (inclusion-attributable) from post-07-01 drift (catalyst-attributable).
- Pre-07-01 drift alone (T+1 ~$275.4 → 06-30 ~$276.17): **≈ FLAT** — 🟡 consistent with H1 (no material inclusion fade) BEFORE the independent catalysts hit.

## Catalyst register (from the parallel sweep; full detail in agent output)

| Date | Event | Class |
|---|---|---|
| 06-22 | NDX inclusion effective; intraday ATH $299.86 | the test variable |
| 06-23 | Global tech/chip selloff (KOSPI −4.6%) | cohort-wide |
| ~06-26 | Eigen AI acquisition completed; analyst PT $280 | NBIS-specific positive |
| 07-01 | **Meta-Compute** (Meta to sell excess AI compute; $27B customer-concentration threat) — NBIS −17%, ~$12B mkt cap | NBIS-specific NEGATIVE (unmodeled confound class) |
| 07-01 | Nvidia revenue-share cloud program (Sharon AI + Firmus, 210k GB GPUs) | cohort/structural |
| 07-02 | Cohort selloff (KOSPI −7.89%, Samsung −9%, SKH −14%) | cohort-wide |
| 07-02 | SoftBank "SB Neo" neocloud entity (10GW ambition, FY27) | cohort/structural |

## Actions

1. T+15 grade due TOMORROW (2026-07-07) — run with whatever 07-06/07-07 closes are obtainable; carry the anchor-gap flag.
2. **USER INPUT REQUESTED:** broker-grade (DeGiro) numbers for: 06-22 open + close, 06-26 close, 07-02 close — to lock anchors before the 07-22 T+30 primary adjudication.
3. B48/R2 codification gate: expect INPUT-CONFOUND deferral unless the T+30 grade can separate pre-/post-07-01 drift (per the finding above).
4. grading-log.md NBIS row updated (T+5 = provisional H2-zone, data-gapped).

**Position implication: ⚪ NO ACTION — 🟡 — position already exited 2026-07-03 on the fired trim-falsifier; grades resolve as pre-registered data-generation only; falsifier decision robust to the $211.12-vs-$215.62 discrepancy (both far below the $234.18 trigger).**
