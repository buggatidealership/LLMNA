# Grading Log — Open + Resolved Predictions

**Last updated:** 2026-07-06 (harness audit: duplicate Samsung/ASML/TSMC rows tagged NOT-CANONICAL; reconciliation note corrected — the duplicate Samsung file exists and is now marked SUPERSEDED)

## TL;DR

Index of every prediction made by the system. Each row resolves to "pending" or "graded." When an event passes its resolution date, run GRADE workflow.

## Pending

| Date made | Resolution target | Ticker | Event | Prediction file |
|---|---|---|---|---|
| ~~2026-06-12~~ | ~~KIOXIA VLSI~~ **✅ GRADED 2026-06-26 — row retained here in error until 2026-07-06 audit; see the [2026-06-26 GRADED] section below** | | | `2026-06-12-KIOXIA-VLSI-symposium-pre-registration.md` |
| **2026-06-19** | **T+15 GRADED-PROVISIONAL 2026-07-07 20:45Z: close $209.47 = NEW window low (−30.1% vs ATH-proxy / −2.9% below the $215.62 trough, computed); verdict CONFOUNDED — inclusion-flow thesis not supported at checkpoint, Meta-Compute idiosyncratic confound dominates; H2-zone continuation; T+30 07-22 = primary adjudicator (may be UNGRADEABLE if confound persists — R2 design note). Prior: T+5 GRADED-PROVISIONAL 2026-07-06 (9d late; correct T+5 trading day was 06-29 — "06-27" was a Saturday) / T+15 ~2026-07-07 / T+30 ~2026-07-22 (primary adjudicator)** | **NBIS** | **Nasdaq-100 inclusion — B48/R2 test. T+5 provisional: H2-zone (~−5% from T+1 close; T2- data), BUT pre-07-01 drift ≈ FLAT (H1-consistent) — window then hit an UNMODELED NEGATIVE independent catalyst (Meta-Compute 07-01, −17%) + cohort macro (07-02); T+0 anchor (06-22 open) UNOBTAINABLE in-environment, user broker numbers requested. See `signals/cross-source-log/2026-07-06-nbis-t5-grade-backfill-provisional-data-gapped.md`** | `2026-06-19-NBIS-nasdaq-100-inclusion-pre-registration.md` |
| 2026-07-02 | ~~2026-07-07~~ | ~~Samsung 005930~~ **⚠️ NOT CANONICAL — do not grade** | ~~rev ₩175-182tn variant~~ — pre-correction duplicate; file marked SUPERSEDED; grade ONLY the canonical Samsung row below | `2026-07-02-SAMSUNG-Q2-prelim-earnings-prediction.md` (SUPERSEDED) |
| 2026-07-02 | ~~2026-07-15~~ | ~~ASML~~ **⚠️ NOT CANONICAL — do not grade** | ~~EPS pt €8.15 variant~~ — pre-correction numbers; grade ONLY the canonical ASML row below (EPS pt €8.20) | `2026-07-02-ASML-Q2-earnings-prediction.md` |
| 2026-07-02 | ~~2026-07-16~~ | ~~TSMC~~ **⚠️ NOT CANONICAL — do not grade** | ~~rev pt $40.8B monthly-math variant~~ — self-corrected same-day; grade ONLY the canonical TSMC row below ($40.1B guide-anchored) | `2026-07-02-TSMC-Q2-earnings-prediction.md` |
| ~~2026-07-02~~ | ~~Samsung prelim~~ **✅ GRADED 2026-07-07 (fundamental leg; reaction T+24h finalizes 07-08) — see GRADED section below.** OP ₩89.4tn band-hit, +4.45% beat vs updated bar; rev ₩171tn small band-miss; reaction leg MISS (−5.35% vs +0-3% band); L27 N=2 fundamental POSITIVE + falsifier-watch counter opened. ASP-dispute adjudication → full print ~Jul-23 (new pending row below) | | | `2026-07-02-SAMSUNG-Q2-prelim-prediction.md` |
| 2026-07-07 | ~2026-07-23 (full print) | Samsung 005930 | CARRY-OVER components from the prelim grade: (a) three-way Q2 blended-DRAM-ASP dispute adjudication (>~63% QoQ test — needs division split); (b) guidance-language component; (c) division-level OP vs the ex-provision >₩100tn wire claims. **PANEL PIN (07-07 user disclosure-card relay): second consensus panel rev ₩173.0tn / OP ₩84.6tn — vs our carried FnGuide ₩84.98tn (07-01) and updated bar ₩85.59tn (07-06); beat magnitude +4.45% to +5.7% depending on panel — state BOTH at full-print grade** | `2026-07-02-SAMSUNG-Q2-prelim-prediction.md` (carry-over section) |
| 2026-07-02 | 2026-07-15 | ASML | ~~rev pt €8.95B / EPS pt €8.20 / bookings pt ~€12.5bn~~ **GRADED 2026-07-15: rev MISS-LOW +3.91% above-band / EPS MISS-HIGH −7.44% below-band / bookings UNGRADEABLE (metric dead at registration → L31) / FY-guide branches under-called (raised €43–45B). T+24h reaction grade 07-16 pending.** Per `signals/cross-source-log/2026-07-15-wed-asml-q2-print-grade.md` | `2026-07-02-ASML-Q2-earnings-prediction.md` |
| 2026-07-02 | 2026-07-16 | TSMC | rev pt $40.1B (guide-anchored; SELF-CORRECTION logged — monthly math not held; v2 at Jul-10 June monthly) / EPS pt $3.90 / capex-raise P~55% | `2026-07-02-TSMC-Q2-earnings-prediction.md` |
| 2026-07-02 | ~2026-07-29 | SK Hynix (HELD #1) | Q2: rev pt ₩88tn / OP pt ₩68tn (vs cons ₩63.0tn; P(beat)~75%) / NI pt ~₩51tn; 2027-HBM-language pre-registered; v2 ensemble T-5d | `2026-07-02-SKHYNIX-Q2-earnings-prediction.md` |
| 2026-07-02 | 2026-07-31 | Murata (HELD) | Q1 FY27: rev pt ¥505bn / OP pt ¥105bn (price-hike quarter front-load) / P(FY-raise)~25%; v2 T-5d | `2026-07-02-MURATA-Q1FY27-earnings-prediction.md` |
| 2026-07-02 | late-Jul→Aug-13 (date TBC) | SanDisk (HELD) | Q4 FY26: rev pt $8.4B (above guide high) / NG EPS pt $33.5 / Q1-FY27 guide pt ~$9.2B; v2 T-5d + L17 leg | `2026-07-02-SNDK-Q4FY26-earnings-prediction.md` |
| 2026-07-02 | 2026-08-07 | Kioxia (HELD) | Q1 FY27: rev pt ¥1.25tn / OP pt ¥600bn / NI pt ~¥460bn; initial-FY-guide-conservative P~70% pre-registered; consensus re-pull at v2 | `2026-07-02-KIOXIA-Q1FY27-earnings-prediction.md` |
| 2026-07-02 | 2026-08-11 | ALAB (initiating) | Q2: rev pt $375M / NG EPS pt $0.75 / Q3 guide pt ~$405M; post-print-dip = staged-entry window note; v2 T-5d | `2026-07-02-ALAB-Q2-earnings-prediction.md` |
| 2026-07-02, **UPGRADED 2026-07-11** | **2026-08-06** (date corrected from 08-12 per 07-06 addendum) | Sumco (HELD) | **CANONICAL = the 07-11 full component-level pre-registration:** rev ¥113bn (¥110-116) / OP −¥1.5bn (−¥3.0 to +¥0.5; P(beat guide)~60) / net −¥5.5bn (−¥8 to −¥3) / OP surprise 35-45-20 / 5 guidance-language P's / three-outcome reaction table (B42-aware post-limit-up). Convergence note: fresh bottoms-up re-derived the SAME central OP/rev as the 07-02 directional entry WITHOUT re-reading it (same model, same data class — consistency, not independent confirmation). 07-02 file retained as the registration-of-record for the directional legs | `2026-07-11-SUMCO-Q2-FY2026-preregistration.md` (canonical) + `2026-07-02-SUMCO-Q2-earnings-prediction.md` |
| **2026-07-01** | **T+0 ~2026-07-30 (Q2 print) + T+24h reaction** | **BE** | **FY2026 guidance revision at Q2 print — ensemble (N=5) modal RAISE (floor-lift) rev $3.6-3.9B / EPS $2.05-2.35 / GM ~34-35% / Q2 ~$800M; L22 read = raise ≈ MEET vs consensus. Tests Rule #17 ensemble spread-vs-outcome + L22 + L13 vintage + L19 reaction** | `2026-07-01-BE-Q2-FY26-guide-prediction.md` |
| 2026-06-23 (retro-registered 2026-07-06) | **RESOLVED 2026-06-24 — formal 3-layer GRADE still owed** | MU | Q3 FY26 print — L27 FIRST empirical regime-test. ⚠️ Never ledgered at registration time (audit catch): pre-registration lives in `signals/cross-source-log/2026-06-23-am-subagent-mu-beat-probability-data-pack-tomorrow-print.md`; outcome informally adjudicated (H1 FIRED, rev $41.46B vs $34.5B cons) in `signals/cross-source-log/2026-06-24-pm-subagent-mu-q3-fy26-earnings-print-l27-first-regime-test.md`. Backfill the 3-layer GRADE + L27 N=1 entry, then move to Graded | (no standalone prediction file — chat/cross-source-log registration) |

**⚠️ DUPLICATE-ROW RECONCILIATION (2026-07-02 PM; CORRECTED 2026-07-06 harness audit):** the table contains TWO row-sets for Samsung/ASML/TSMC. **CANONICAL for grading = the rows referencing `2026-07-02-SAMSUNG-Q2-prelim-prediction.md` / `2026-07-02-ASML-Q2-earnings-prediction.md` (EPS pt €8.20) / `2026-07-02-TSMC-Q2-earnings-prediction.md` (rev pt $40.1B, guide-anchored + Rule #11 self-correction).** The other three rows carry PRE-correction numbers, are marked NOT-CANONICAL in the table, and are NOT graded. **Correction of the original note's false claim:** the duplicate Samsung file `2026-07-02-SAMSUNG-Q2-prelim-earnings-prediction.md` DOES exist on disk (it now carries a SUPERSEDED header); the ASML/TSMC variant rows point at the SAME canonical filenames but with divergent point numbers. The TSMC "$40.8B monthly-math-anchored" claim was explicitly self-corrected same-day (the monthly data was never received — see the TSMC file's Rule #11 section). One prediction, one canonical registration.

**~~KIOXIA T+24h grade WINDOW~~ — CHECKLIST COMPLETED; grade executed 2026-06-26 (see GRADED section below). Retained for audit only (marked 2026-07-06):**
1. Verify MSA-CBA paper actually presented June 14-18 (subagent + VLSI on-demand June 24+ access OR Kioxia/SanDisk co-press release)
2. Pull 285A.T price action June 16-19 (Monday-Thursday JST close) — joint with US semi cohort macro overlay
3. Pull SNDK + HYNIX + MU price action same window (Yokkaichi JV mirror + memory-cluster macro overlay)
4. Compute T+24h stock reaction vs the pre-registered H1/H2/H3/H4 magnitude bands
5. Classify into H bucket + apply 3-layer GRADE structure
6. T+72h follow-up grade ~2026-06-22 to 25 for sustained vs faded magnitude
7. Append lesson to `predictions/lessons.md` if generalizable insight emerges
8. Update KIOXIA thesis with grade outcome + B48 candidate sister-test status

**NBIS T+5/T+15/T+30 grade WINDOW OPENS 2026-06-22 INCLUSION DAY:** Inclusion-day open price = T+0 anchor for all 3 milestones. **PRE-EVENT PREP COMPLETE 2026-06-19:** pre-registration file locked with H1/H2/H3/H4 + falsifiers + bottoms-up magnitude bands + B45 regime-corrected priors + L21 sector regime overlay (Stage 2-3 = mild modifier, NOT severe-negative) + L15 INPUT-checklist discipline note on effective-date verification. **GRADE PREP CHECKLIST:**
1. **2026-06-22 inclusion-day open price = T+0 anchor** (verify before T+5 grade run)
2. Pull NBIS price action 2026-06-22 → 2026-07-22 (30-day window) — daily close + intra-window low
3. Compute T+5 (06-27) + T+15 (07-07) + T+30 (07-22) returns + intra-window low
4. Classify into H1/H2/H3/H4 bucket per criteria in pre-registration file
5. Apply 3-layer GRADE structure (INPUT / COMPUTATION / REASONING)
6. Flag independent positive catalysts during window (DSIT AIRR award, sovereign-AI contract, hyperscaler win) for H4 INPUT-confound check
7. Append lesson if generalizable
8. **B48 candidate codification gate decision:** H1 → promote to N=1; H2 → SPLIT remain N=0; H3 → R2 FALSIFIED + AM7c framework empirically vindicated; H4 → INPUT confound deferred
9. **PM33 entry-timing retrospective:** H3 outcome → monthly audit grade entry "AUTO-EXECUTE STRENGTHENING calibration failure case"
10. Update NBIS thesis with grade outcome + R2 hypothesis status + framework-discipline recalibration if material

**Paper-landscape mapping COMPLETE 2026-06-14 PM5** per `signals/cross-source-log/2026-06-14-pm5-kioxia-vlsi-2026-paper-landscape-mapping.md` (Step 0 of approved Kioxia plan; user authorization 2026-06-14 22:25 UTC). Key inputs locked for T+24h grade:
- T1.4 MSA-CBA joint paper CONFIRMED (M. Noda et al, Kioxia + Sandisk; world-first QLC on multi-stacked array with Cu wafer-to-wafer direct bonding; path to 1,000+ word lines)
- 3 additional Kioxia papers titles undisclosed = H3 wildcard
- Samsung TFS1.3 900-layer CMB paper June 16 = comparison-bar threat
- HBF not confirmed at VLSI 2026 in public program
- H1-H4 trigger map operational; B45-corrected weights unchanged (H1 40% / H2 30% / H3 20% / H4 10%)
- Day 1-2 monitoring active (June 14-15 JST); T+24h grade resolution ~June 19; T+72h ~June 22-25

**Day 1-2 monitoring observation 2026-06-15 PM** per `signals/cross-source-log/2026-06-15-kioxia-vlsi-2026-day1-2-monitoring.md`:
- NEGATIVE FINDING (high value): no live post-presentation coverage indexed for Day 1-2 (academic symposium norm; OnDemand June 24); T1.4 + 3 undisclosed papers PRE-PRESENTATION status confirmed
- B40.1 VENUE CORRECTION: VLSI 2026 is in HONOLULU not Kyoto (Step 0 had stale-recycled pre-training; substance unaffected)
- Pre-event rally assumption re-examined: 285A.T -11.68% Jun 8 (US semi selloff) then recovered to ~81,200 JPY Jun 13 = "rally" partially absorbed already → H2 exhaustion probability LOWER
- Macro overlay: Q1 FY27 forecast ¥869B net profit (~48× prior year) DOMINATES VLSI signal; market cap > Toyota Jun 12
- Provisional H1-H4 reweighting (my model, awaiting formal T+24h grade): H1 40%→45% (elevated); H2 30%→25% (lower); H3 stable 20%; H4 stable 10%
- Critical watch June 16-17: Samsung TFS1.3 formal presentation Jun 16 = first real H2 vs H3 framing test; 285A.T Monday Jun 16 trading reaction
- Formal T+24h grade still scheduled ~June 19

## Graded

| Date made | Resolution | Ticker | Event | Prediction file | Grade file | Outcome |
|---|---|---|---|---|---|---|
| 2026-05-20 | 2026-05-20 | NVDA | Q1 FY27 earnings | `2026-05-20-NVDA-Q1FY27.md` | `2026-05-20-NVDA-Q1FY27-GRADE.md` | RIGHT direction (beat all 4); Q2 guide upside underweighted; L4 added |
| 2026-05-26 | 2026-05-27 | MOD | Q4 FY26 earnings + FY27 guide | `2026-05-26-MOD-Q4FY26.md` | `2026-05-26-MOD-Q4FY26-GRADE.md` | RIGHT direction all 4 targets; EPS magnitude undercalled ($1.71 vs $1.52-1.58 range); CS margin recovery only +80bps not +200bps. 0 falsifiers fired. L6, L7, L8 added |
| 2026-05-27 | 2026-05-27 | SNOW | Q1 FY27 earnings + FY27 guide + Cortex AI run rate | `2026-05-27-SNOW-Q1FY27.md` | `2026-05-27-SNOW-Q1FY27-GRADE.md` | Beat-and-raise across all 4. Revenue $1.33B vs $1.275B predicted ($55M above point). FY27 raise $5.84B = CLEAN HIT within band. NRR 126% — WRONG DIRECTION (predicted 124% dip; actual UP). Cortex run rate not re-quantified but mgmt confidently reframed to volume metrics. 0 falsifiers fired. $6B AWS pact bonus signal. L9 + L10 added. Stock +25% AH |
| 2026-05-27 | 2026-05-27 (fundamental) + 2026-05-28 (stock-reaction) | MRVL | Q1 FY27 earnings + Q2 guide + custom Si FY27 outlook commentary | `2026-05-27-MRVL-Q1FY27.md` | `2026-05-27-MRVL-Q1FY27-GRADE.md` | Direction RIGHT on Targets 1, 2 (partial — at consensus), 5; partial-vintage-miss on Target 4 (FY28 reveal not FY27); reasoning-error catch on Target 3 (sequential conflated with YoY). Revenue $2,418M (vs $2,470 predicted = -2.1% over-shoot). Q2 guide $2,700M (predicted $2.65B+ = HIT). FY27 raised to $11.5B + FY28 NEW $16.5B (+45% YoY) — MISSED CATEGORY (multi-year guide raise not in original prediction targets). Supply-Chain-Cohort Calibration framework PARTIALLY validated; NOT codified yet (N=1). Stock -1.96% pre-market despite green tape (Iran-US deal macro) = Stage 3-4 validated. L11 + L12 + L13 added |
| 2026-05-29 | 2026-06-01 (fundamental) + 2026-06-02 (stock-reaction T+24h) | HPE | Q2 FY26 earnings + Q3 guide + FY26 outlook (2ND application Supply-Chain-Cohort Calibration framework) | `2026-05-29-HPE-Q2FY26.md` | `2026-06-01-HPE-Q2FY26-GRADE.md` | **MASSIVE BEAT — CATEGORY EVENT**. Revenue $10.7B vs $9.95B predicted (+7.5%); EPS $0.79 vs $0.57 predicted (+38% gap — H3C divestiture not in model = L15 INPUT failure). AI backlog $5.9B vs $7-9B predicted (CONVERSION not ACCUMULATION mode = L16 REASONING failure). FY26 raised materially + FY27 framework INTRODUCED (both per Target 5 L13 vintage-distribution — directional HIT). Stock +29-36% T+24h = CATEGORY EVENT override of Stage 3-4 suppression. L14 CODIFIED at N=2. L15 NEW (corporate event INPUT checklist). L16 CANDIDATE (cohort sub-mechanism: accumulation vs conversion). Supply-Chain-Cohort Calibration: REFINE (correct direction; magnitude under-predicted due to H3C INPUT gap + DELL sub-mechanism mismatch). |
| 2026-06-03 | 2026-06-03 AMC (fundamental) + 2026-06-04 (stock-reaction T+24h, macro-confounded) | AVGO | Q2 FY26 earnings + Q3 guide + FY26 AI raise (N=2 Supply-Chain-Cohort + L14 framework test) | `2026-06-03-AVGO-Q2FY26.md` | `2026-06-04-AVGO-Q2FY26-GRADE.md` | **PARTIAL HIT (fundamental) + WRONG DIRECTION (stock-reaction)**. AI semi $10.8B = BULLSEYE. Revenue $22.187B = -0.5% low. EPS $2.44 = -$0.01 low. Q3 guide $29.4B vs my $23.0-23.8B = MASSIVE upside MISS (-24% under). Anthropic 5GW disclosure NOT MODELED. FY26 AI NOT raised — multi-year framing FY27 >$100B instead = L19 REASONING/framing failure. Stock AH -3% to -13.78% (vs predicted +11-13% weighted) = **L14 FIRST FALSIFICATION**. L14-v2 refinement candidate (pre-print rally >10% offsets BEAT+CATEGORY). L19 NEW (multi-year vs FY-raise framing gap). L20 NEW (macro-confounder T+24h discount — Iran-Israel oil-spike risk-off backdrop). B42 candidate (expectations-exhaustion bias). Fundamental cohort signal BULLISH for HYNIX/MURATA/SUMCO/SNDK/ALAB (already cascaded via Alphabet $190B + AVGO Q3 $16B AI guide). |

## Process

When a resolution date hits:
1. Read the prediction file
2. Pull actual results (filing, press release)
3. Run GRADE template from `meta/reasoning-templates.md`
4. Append lesson to `lessons.md` if a generalizable insight emerged
5. Update bias entries in `biases-watchlist.md` if a new pattern was revealed
6. Move row from Pending to Graded with link to grading doc

---

## [2026-07-07 GRADED — fundamental leg; reaction T+24h GRADED-PROVISIONAL 2026-07-08] SAMSUNG Q2 2026 PRELIM (the keystone; registered 2026-07-02, resolved 2026-07-07 ~08:40 KST)

**T+24h REACTION FINALIZATION (2026-07-08, provisional on official settle — T1 tape 403-blocked, same treatment as NBIS T+15; direction corroborated ≥3 independent T2 incl. Korean-native etoday/fnnews, per 1 Opus verification agent):** 07-08 session = **STABILIZATION, not recovery**: Samsung gapped −3.55% (low ₩283,000), reversed to ₩298,500 **+0.84% intraday ~09:55 KST**; SK Hynix **+5.20%** to ₩2,315,500; KOSPI +0.90% after opening −2.66%. Computed cumulative from implied pre-print close (python, both prev-close bases 296,000/297,000): **−6.21% to −6.53% below pre-print** — the print-day loss was RETAINED. Press attribution: bargain-hunting into memory ~60% / AI-capex-doubt backdrop ~25% / HYNIX-specific ADR-oversubscription tailwind ~15% (press-supported weights). Cohort-decoupling (#41) COMPLETED: reporter (Samsung +0.8%) lagged cohort (HYNIX +5.2%) on the bounce — HYNIX pure-play HBM + ADR demand vs Samsung ₩400tn fab-hub capex overhang. **VERDICT: beat-and-no-rally CONFIRMED at T+24h — L27 falsifier counter tick #1 STANDS (1 of 2). No second leg down (base-built), so this is bimodal-print whisper-regime behavior (B42), not capitulation.** Settle-confirm folds into the next KR/JP artifact; basis discrepancy (296,000 vs 297,000 prev close) computed as immaterial to the verdict.

**Executed by the main session as wake catch-up** (both routine-spawned sessions produced no output — see `signals/cross-source-log/2026-07-06-routine-creation-preregistration-and-test.md`). Verification: 1 Opus agent, ≥5 T2 wires corroborating the T1 공시; register in `signals/cross-source-log/2026-07-07-samsung-prelim-grade-wake-catchup.md`.

**Predicted (canonical file):** rev ₩172-183tn pt ₩178tn; OP ₩87-97tn pt ₩92tn; P(OP>consensus)~70%; reaction bands: OP ≥₩90tn → +3-8%, ₩85-90tn → +0-3%, <₩85tn → −5-10%. Graded vs the 07-06 UPDATED bar (FnGuide OP ₩85.59tn) per the prelim-eve addendum.

**Actual (T1 공시 via ≥5 T2 wires):** revenue **₩171tn** (+129% YoY); OP **₩89.4tn** (+1810% YoY, record; single-quarter OP > NVIDIA's latest quarter, T2 framing). Bonus provision ~₩20tn — ex-provision OP >₩100tn per multiple wires. First-hour reaction: 005930 **−5.35%** to ₩301,000; KOSPI −0.46%; SKH sympathy unquantified (flagged).

**Component adjudication:**
- OP: **BAND HIT** (89.4 ∈ 87-97); point −2.8%; **consensus BEAT +4.45%** vs updated ₩85.59tn bar (+5.2% vs original ₩84.98tn) — P(beat)~70% resolved TRUE. Whisper (~₩90tn): whisper-INLINE, exactly the pre-documented scenario.
- Revenue: **BAND MISS (small)** — ₩171tn vs band floor ₩172tn; in-line with consensus. Falsifier 2 (<₩170tn) did NOT fire.
- Provision: ~₩20tn actual = top of the 07-04 preview range (₩10-20tn) — per the pre-registered carve-out, the miss-vs-point is a COMPUTATION one-off (provision), NOT an ASP-model failure; ex-provision >₩100tn implies the ASP flow-through model was right-to-conservative.
- ASP three-way dispute: **NOT ADJUDICABLE at prelim** (consolidated-only, no division split — pre-documented) → transfers to the full print ~Jul-23.
- Reaction (T+0 close CONFIRMED; formal T+24h = 07-08 close): first hour −5.35% → intraday −9.75% (13:51 KST circuit-breaker window) → close **−6.92%** vs the predicted +0-3% band → **REACTION LEG MISS confirmed at the close**; cohort context: SKH −8.45%, KOSPI ~−5% w/ circuit breaker (see 09:15Z update in the wake artifact). Mechanism: whisper-anchoring — the market graded vs the ~₩90tn whisper + brokers-raised bars (News1: bars raised toward ₩90tn into the print), not the official consensus. Cohort-decoupling (#41): 005930 −5.35% vs KOSPI −0.46% = idiosyncratic-leaning, diagnostic incomplete (SKH move unverified).

**3-layer GRADE:**
- INPUT — revenue leg: the pre-flagged gap fired as flagged (Q1 base never independently pulled; QoQ inference leaned on pricing math) → small band-miss. Bar-creep was correctly pre-managed.
- COMPUTATION — sound: OP band hit; point-gap = provision one-off per the pre-registered carve-out.
- REASONING — fundamental leg strong (whisper risk, carve-out, and conditional reaction bands all pre-identified). Reaction leg: the file SAW the whisper-inline risk but kept official-consensus-anchored reaction bands → **generalizable: in whisper-elevated setups, band the reaction vs the WHISPER, not the official bar** (B42/L14-v2 family — logged as B42 N+1, not a new lesson number).

**L27 verdict: N=2 fundamental POSITIVE — beat-pattern intact, regime-test GREEN on the operational leg.** BUT: first clean beat-with-negative-reaction datapoint → **L27 falsifier-watch counter 1 of 2 OPENED (provisional pending T+24h close)** — if HYNIX (Jul-29) or MURATA (Jul-31) also beats operationally with negative cohort response, the "fundamentals diverge from price" reframe question fires per the pre-registered L27 falsifier.

---

## [2026-07-06 GRADED — backfill] MU Q3 FY26 print (registered 2026-06-23 in cross-source-log only; resolved 2026-06-24)

**Status:** GRADED 12 days late (audit-surfaced: prediction was never ledgered at registration time; retro-registered + graded 2026-07-06)
**Pre-registration:** `signals/cross-source-log/2026-06-23-am-subagent-mu-beat-probability-data-pack-tomorrow-print.md`
**Outcome artifact:** `signals/cross-source-log/2026-06-24-pm-subagent-mu-q3-fy26-earnings-print-l27-first-regime-test.md`

**Predicted (5 hypotheses, 2026-06-23):** modal H1 (P~50%, my model): beat consensus ($34.5-35.6B rev / $19.72-20.49 EPS) + Q4 guide ≥$38B → +10-20% continuation; P(operational beat)=85%; Q4 analyst-modeled range $38-42B; H5 (P~10%): beat + structural disclosure → +15-25%.

**Actual (T1 SEC 8-K):** revenue **$41.46B** (+16.5-20.2% vs consensus), non-GAAP EPS **$25.11** (+22-27%), Q4 FY26 guide **$50.0B ±$1.0B** — +131% of the $38B binary gate and +16.6% above the buy-side high ($42.9B); largest forward guide in Micron history. **H1 FIRED (modal) + H5 PARTIAL** (HBM4 volume-ramp-ahead-of-yield-curve disclosure). 6/6 pre-print directional theses validated. AH reaction ~+2.5% muted — classified in the 06-24 artifact as a distortion artifact of the −13.18% pre-print KOSPI-contagion selloff, not disappointment.

**3-layer GRADE:**
- **INPUT — the failed layer (partially):** every modeled magnitude band was demolished — the Q4 scenario range topped at $42B vs actual $50B, and the H1 reaction band (+10-20%) never contemplated a +131%-of-gate guide. The optimistic tail was under-sampled EVEN AFTER B45 correction — B45's recursive-persistence pattern (pre-training magnitude conservatism survives its own codification). Second INPUT defect: process — no grading-log stub was registered at prediction time (Critical Rule: PREDICT workflow step skipped), which is why this grade is 12 days late.
- **COMPUTATION — sound:** 5-hypothesis joint distribution well-formed; P-weights reasonable (modal fired); P(operational beat)=85% resolved TRUE; decoupling of P(beat) from P(positive reaction) was structurally correct.
- **REASONING — sound:** correctly pre-identified the Q4 guide (not the Q3 beat) as the true binary; correctly applied L21 to classify the muted AH reaction as macro-confounded rather than thesis-negative.

**Diagnostic:** direction right, magnitude wrong by tail-underestimate → INPUT layer (B45-class).

**Reaction leg (Two-Part GRADE protocol):** T+24h close was never formally captured (same process gap); AH +2.5% recorded as CONFOUNDED/NON-SCORING for the bimodal-print framework — does not count for or against L27's reaction predictions.

**L27 verdict:** **N=1 POSITIVE — beat-pattern intact, regime-test GREEN.** Next tests: HYNIX Q2 (~Jul-29) = N=2, MURATA Q1 FY27 (Jul-31) = N=3.

**Calibration adjustment:** for the late-July v2 ensembles (HYNIX/MURATA/SNDK, T-5d re-runs per the earnings program), add an explicit above-buy-side-high tail scenario with non-trivial P — regime-confirmation events keep landing in the unmodeled optimistic tail (consistent with L26/L30).

---

## [2026-06-26 GRADED] KIOXIA-VLSI-symposium-pre-registration (2026-06-12)

**Status:** GRADED (4-7 days late vs T+24h/T+72h windows)
**Pre-registration:** `predictions/2026-06-12-KIOXIA-VLSI-symposium-pre-registration.md`
**Grade artifact:** `signals/cross-source-log/2026-06-26-am-subagent-12-kioxia-vlsi-symposium-prediction-grade.md`

**Predicted (4 hypotheses):**
- H1 (P~45% post-PM2 reweight): Material validation + +12-22% T+24h / extension +25-35% T+72h
- H2 (P~25%): Partial validation + flat-to-+8%
- H3 (P~20%): Catalyst surprise / HBF disclosure
- H4 (P~10%): Yield/warpage disappointment

**Actual outcome:**
- T+0 (June 16 Mon VLSI Day 3 close): ¥94,720 (+16.6% vs ¥81,200 anchor)
- T+24h (June 19 Thu close): >¥100,000 (+23.2%) — within H1 band
- **T+72h (June 22 Mon close): ¥112,700 ALL-TIME HIGH = +38.8%** — exceeded H1 extension band by 14-26pp

**Fundamental gates (2.5/4 met = materially validates):**
- (a) BiCS10 332-layer specs: YES (T1 — +59% density / Toggle DDR 6.0 4.8 Gbps)
- (b) 1,000-layer roadmap firm date: PARTIAL (milestone toward >1,000 via MSA-CBA QLC; 2031 reiterated not accelerated)
- (c) Hyperscaler customer named: NO (clear no-fire)
- (d) QLC operation at stack-bonded layer count: YES (T1 — world-first QLC on MSA-CBA via Cu wafer-to-wafer direct bonding)

**Cohort same-day ATH (June 22, critical finding):**
- KIOXIA 285A.T ¥112,700 + SNDK $2,273.73 + MU $1,211.38 + SK Hynix ₩2,945,000 — ALL FOUR memory names ATH same day = TC-1 cluster-state event (N=13+)

**Verdict: H1 FIRED — direction RIGHT + magnitude UNDER-CALLED.**

**3-layer GRADE diagnostic:**
- INPUT: NO failure (inputs current/complete/well-tagged; 12-day anchor verified; cohort beta noted; PM-2 correction applied)
- COMPUTATION: MILD failure (under-modeled right tail; H1 extension band +25-35%; actual +38.8% breached by 3-14pp; L26 trend-break + B45 supercycle base rates NOT explicitly fused into magnitude floor)
- REASONING: MILD failure (framework-composition gap — each lesson L14 + L26 + B45 existed individually; none compounded into band calibration)

**Diagnostic test result:** Directionally RIGHT (H1 fired); magnitude UNDER-called by 14-26pp on T+72h; gap explained by COMPUTATION + REASONING jointly (band-compression because L26+B45 not fused into floor).

**L17 candidate test N=1 resolution:**
- L14 ORIGINAL CONFIRMED at N=1 forward (Kioxia is the case); L14 now N=3 codified (NVDA + HPE + Kioxia)
- L14-v2 candidate REFUTED at N=1 (12% pre-event rally did NOT offset BEAT+CATEGORY signal); L14-v2 likely REGIME-DEPENDENT (held in pre-supercycle; fails in 2026 supercycle)
- B45 PM-2 reweight back to H1-modal EMPIRICALLY VALIDATED

**L30 candidate codified** (see lessons.md): in B45-confirmed supercycle regime + L26 trend-break + L14 CATEGORY-EVENT framework simultaneously applying to Stage 3-4 name, H1 magnitude band MUST be FLOORED by L26+B45 supercycle distribution (+25-50% T+72h) NOT pre-supercycle L14 codified band (+12-22%).

**Position implication: HOLD all current positions; NO retroactive cascade to KIOXIA/SNDK thesis tier; document under-call as REASONING-layer calibration data point.** Pre-reg Option B (reactive post-T+24h entry) was directionally correct but cost ~36pp upside vs Option A; epistemically defensible 9 days post-AVGO-L14-falsification. Lesson is forward-looking — L30 means future predictions get +25-50% magnitude floor, NOT regret-driven retroactive tier change.

**Status: ✅ GRADED (T+0 fundamental + T+24h + T+72h stock-reaction)**


- **2026-07-16 ASML T+24h reaction grade (closes 07-15 pending row): POSITIVE-SUSTAINED** — ADR +2.87% regular close $1,775.64, AH +3.51% toward $1,838 near 52-wk high (T1). Guide-raise frame (3rd consecutive FY raise €43-45B) dominated; no fade. Original bookings-keyed reaction frame remained void (metric dead, L31). Per `signals/cross-source-log/2026-07-16-thu-morning-wake-3leg.md`.
- **2026-07-16 TSMC Q2 pre-registration — PARTIAL: rev component only.** Predicted pt $40.1B; actual $39.62B (NT$1.27T, +36% YoY, ABOVE guide, T1 pre-release Jul-13) = point −1.2% too high, direction right. EPS pt $3.90 + capex-raise P~55% + Q3 guide = PENDING post-call re-scan (armed same day). Status: pending-completion.
- **2026-07-16 TSMC Q2 GRADED (completes the same-day partial):** rev HIT (in-band, pt +1.21% high); EPS MISS-LOW (actual ~$4.25/ADR computed vs band top $4.05; 6-K pending); Q3-up P~80% HIT (+14.1% QoQ mid); **capex-raise P~55% HIT — full raise $52-56B→$60-64B (+14.8% mid)**; FY growth 30%→">40%" outside branch set; falsifiers not fired. Edge-vs-consensus 2-for-2 (rev +1.21 vs street −3.84; EPS −8.2 vs street −10.3). T+24h reaction grade pending tomorrow. Per `signals/cross-source-log/2026-07-16-thu-tsmc-q2-print-grade.md`.
