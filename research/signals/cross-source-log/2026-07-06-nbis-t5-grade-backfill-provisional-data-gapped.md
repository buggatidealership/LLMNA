# 2026-07-06 — NBIS T+5 inclusion grade — PROVISIONAL BACKFILL (data-gapped)

**Trigger:** 2026-07-06 harness audit found the T+5 grade (due 2026-06-27 per `predictions/2026-06-19-NBIS-nasdaq-100-inclusion-pre-registration.md`) never ran, and the T+0 anchor (2026-06-22 inclusion-day open) was never captured. Backfilled today, 9 days late, ahead of tomorrow's T+15 checkpoint. 2 verification subagents (price-window + catalyst-register) per Critical Rule #16.

**⚠️ DATA-QUALITY BANNER (RESOLVED BY USER DECISION 2026-07-06):** all aggregator pages returned HTTP 403 in this environment; every price below is search-summary grade (**T2-minus, unverified**). The load-bearing T+0 anchor (06-22 open AND close) is unobtainable from accessible sources. **User decision 2026-07-06: PROCEED WITH T2- DATA AS FINAL** — anchors for the T+15/T+30 grades = 06-22 intraday ATH $299.86 (best T+0 proxy, conservative: makes pullback reads look WORSE, biasing against H1/R2 ratification) + T+1 close ~$275.4 (secondary anchor) + 07-02 close $215.62. The T+30 grade carries a permanent data-quality caveat, and any B48 promotion off this window is capped at CANDIDATE strength regardless of H bucket.

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
2. ~~USER INPUT REQUESTED: broker-grade numbers~~ **RESOLVED 2026-07-06: user opted to proceed with T2- data as final** (see banner). No broker pull; anchors locked as stated with permanent caveat.
3. B48/R2 codification gate: expect INPUT-CONFOUND deferral unless the T+30 grade can separate pre-/post-07-01 drift (per the finding above).
4. grading-log.md NBIS row updated (T+5 = provisional H2-zone, data-gapped).

**Position implication: ⚪ NO ACTION — 🟡 — position already exited 2026-07-03 on the fired trim-falsifier; grades resolve as pre-registered data-generation only; falsifier decision robust to the $211.12-vs-$215.62 discrepancy (both far below the $234.18 trigger).**

## [2026-07-07 20:45Z] T+15 CHECKPOINT GRADED (provisional; anchors remain T2-; computed per #43b)

**Close 2026-07-07: $209.47 (T2 aggregator convergence — stockanalysis/CNBC/Yahoo snapshots; T1 tape unavailable, 403s). Computed anchors: −30.1% vs the $299.86 ATH-proxy / −23.9% vs T+1 ~$275.40 / −2.9% vs the $215.62 window trough = NEW WINDOW LOW. Day ≈−2.8% (07-06 prior close T3-unconfirmed ~$215.5). Intraday reversal: rallied to $224.97 then gave back −6.9% to close near lows — a FAILED bounce.**

**Classification (drift-split maintained):** pre-07-01 leg unchanged (≈FLAT, H1-consistent — index-flow neutral-to-mild-support); post-07-01 leg DEEPENED — the Meta-Compute confound (Bloomberg 07-01: Meta to monetize excess AI compute → neocloud repricing; NBIS −17% that day, CoreWeave −14%; Morgan Stanley extending the frame 07-03/04, T2 roster in agent return) now fully dominates the checkpoint. **T+15 verdict: CONFOUNDED — index-inclusion-flow thesis NOT SUPPORTED at this checkpoint (no passive-bid stabilization visible; price through the prior trough), but NOT cleanly REFUTED either, because the confound is idiosyncratic-sectoral, not flow-related. H-bucket: H2-zone continuation, confound-attributed.** No NBIS-specific offering/downgrade found 07-03→07-07 (analyst posture 6 Buy/4 Hold, avg PT ~$237 — positioning context only, B28). Position: EXITED 07-03 — grades resolve as data-generation (B48/R2 test). **T+30 (2026-07-22) remains the PRIMARY adjudicator; if the Meta-Compute overhang persists through it, the pre-registered inclusion-flow question may be UNGRADEABLE for this specimen — note for the R2 program design (pick less confounded specimens or model confound-exclusion rules ex-ante).**
