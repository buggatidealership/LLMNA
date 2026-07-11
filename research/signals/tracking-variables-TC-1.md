# TC-1 — Memory tightness multi-tier — Lead-Lag tracking variables

**Created:** 2026-06-15 PM11 (Principle #38 third application; first was `companies/NBIS/tracking-variables.md` 2026-06-15 PM2; second was `signals/tracking-variables-TC-10.md` 2026-06-15 PM6)
**Convention:** Per `meta/methodology.md` Principle #38 candidate — every tracking variable tagged LEAD (acts BEFORE market-moving event) or LAG (confirms AFTER). LEAD requires deliberate alt-data sourcing because LAG sources surface naturally from research-verified channels.
**Source cluster:** `signals/triangulation.md` TC-1 (N=14 STRUCTURAL-REGIME-CONFIRMATION; 60-year WSTS DRAM ASP trend-line break; H1 75% structural posterior; held cohort cascade — HYNIX direct, SNDK/SUMCO indirect, MURATA via TC-6 adjacency)

## Why this framework matters for TC-1 specifically

TC-1 is the highest-conviction structural cluster in the harness — directly drives held-cohort sizing for HYNIX (largest position) + SNDK + SUMCO + MURATA (TC-6 adjacency). Per Principle #38 application discipline, the cluster needs explicit LEAD vs LAG decomposition because:

1. **TC-1 has more LEAD-indicator richness than TC-10** (regulatory clusters are back-channel-opaque; memory clusters have rich open trade data + supplier IR + customer 10-Q tea leaves)
2. **Memory cycle inflection-catching is the highest-alpha event-type** in the harness (per F1-F13 falsifier set codification 2026-06-14 PM); LEAD-indicator monitoring directly serves the cyclical-inflection-catch protocol
3. **TC-1 N=3 application** validates Principle #38 across cluster types: company-level (NBIS — rich LEAD) + regulatory cluster (TC-10 — sparse LEAD by design) + supply-cycle cluster (TC-1 — rich LEAD with native multilingual signals). If P#38 holds at TC-1 → promotion-ready for CANDIDATE → VERIFIED at June 24 monthly audit

## LEAD indicator stack (ranked by signal-to-noise + accessibility)

| # | LEAD indicator | Source | Cadence | Est. lead-time | Sub-mechanism informed | Tier |
|---|---|---|---|---|---|---|
| 1 | **Korea Customs Service monthly trade data** — semiconductor export volumes + ASP | customs.go.kr (Korean) + KITA k-stat.kita.net (English) | Monthly with ~5-10 day lag from month-end | **30-45 days ahead of WSTS publication** | DRAM + NAND combined; HBM has separate line | 🟢 FREE |
| 2 | **TrendForce / DRAMeXchange monthly contract price guides** | trendforce.com (paid premium); secondary excerpts via Tom's Hardware / Digitimes free | Monthly | 1-2 week lead vs spot reaction | DRAM contract; NAND contract; HBM separate | 🟡 paid-gate (free excerpts) |
| 3 | **SK Hynix / Samsung / Micron / Kioxia / SanDisk capex disclosures** | quarterly earnings calls + IR press releases (T1 each company) | Quarterly + event-driven (mid-quarter updates) | **3-6 month lead on supply response** materializing | Total industry supply trajectory; HBM-vs-DRAM mix shift | 🟢 FREE |
| 4 | **NVDA / AMD 10-Q "memory commitments" line items** | SEC EDGAR | Quarterly (45-day filing lag) | **3-9 month lead** on supplier allocation patterns | HBM allocation share per hyperscaler / accelerator vendor | 🟢 FREE |
| 5 | **Wafer-fab utilization disclosures** | SK Hynix, Samsung, Micron, Kioxia quarterly transcripts | Quarterly | 3-6 month lead on output | DRAM + NAND fab utilization; HBM3E/HBM4 allocation pressure | 🟢 FREE |
| 6 | **SEMI WFE monthly billings** (semi.org) + Lam / AMAT / TEL quarterly memory-segment commentary | SEMI World Fab Forecast + WFE press releases; SEC 10-Q for equipment vendors | Monthly + quarterly | **6-12 month lead on memory fab output** | New fab capacity ramp; HBM capacity expansions | 🟢 FREE for headline numbers |
| 7 | **DRAM inventory levels at hyperscalers** | hyperscaler 10-Q footnotes; rare disclosure | Quarterly | 1-3 month lead on procurement cycle | Inventory destocking/restocking signal | 🟡 spotty disclosure |
| 8 | **Aschenbrenner Q-quarter 13F filings** | SEC EDGAR (45-day filing lag) | Quarterly | Position change is LAG, but DIRECTION of conviction is LEAD on multi-quarter inflection | Conviction signal — Aschenbrenner Q1 2026 13F = $724M SNDK #2 + $878M BE #1 + $556M CRWV per harness anchor | 🟢 FREE |
| 9 | **Korean / Japanese / Taiwanese / Chinese native-language trade press** — ETNews / Nikkei / Digitimes / 工商時報 / 163.com | native-language press feeds | Daily; event-driven | **1-2 weeks ahead of English-language coverage** (per B40.1 stale-recycle pattern N=12+; native-language leads English) | All sub-mechanisms — supplier capacity commentary; customer engagement leaks; pricing rumors | 🟢 FREE |
| 10 | **WSTS monthly memory revenue + ASP data** | wsts.org (subscription); secondary excerpts via TrendForce | Monthly with ~6-8 week lag from month-end | Lead-time vs Tier 1 = ~30-45 days LATER but VERIFIED data point | DRAM + NAND total industry revenue | 🟡 mostly LAG by 6-8wk |
| 11 | **HBM-specific supplier earnings commentary** (SK Hynix HBM3E/HBM4 capacity ramp; Samsung HBM yield) | quarterly earnings + investor day | Quarterly | 3-6 month lead on HBM tier | HBM-specific supply tightness; HBF emerging tier | 🟢 FREE |
| 12 | **Native-Korean political/policy press** — Ministry of Trade, Industry and Energy (MOTIE) announcements | motie.go.kr (Korean); Yonhap English | Event-driven | weeks-months ahead of formal policy | Memory-as-strategic-asset policy signals (Korean sovereignty); export-control adjustments | 🟢 FREE |

## LAG indicator stack (confirmation only; do not chase)

| Source | What | Why LAG | Sub-mechanism |
|---|---|---|---|
| WSTS monthly DRAM/NAND ASP (after publication) | Industry-aggregate prices | Publication = market reaction immediate | Direct ASP |
| TrendForce spot prices | Daily spot quotes | Spot reacts within days | Spot ASP |
| Memory vendor quarterly earnings | Revenue + margin disclosures | 45-day filing lag; market reacts on print | Per-vendor revenue |
| 13F institutional filings | Q-quarter holdings | 45-day filing lag | Smart-money positioning |
| HBM-tier yield disclosure at conferences (VLSI / IEDM / Hot Chips) | Industry tech papers | Publication = post-development | HBM yield + qualification |
| Stock-price reactions to news | Real-time | Price IS the LAG indicator | Sentiment |
| Bernstein / Citi / Goldman sell-side notes | Analyst reports | React to news; do not predict | Consensus framing |

## PAID lead-indicators worth budget if available

| Source | Cost | Why worth it for TC-1 |
|---|---|---|
| TrendForce premium subscription | ~$3-5k/yr | Earliest monthly contract-price visibility + HBM/HBF tier breakdowns; native-EN |
| Mirae Asset Securities Korean sell-side | institutional (via brokerage) | Earliest Korean DRAM/NAND demand-supply intelligence; SK Hynix / Samsung Memory specific channel checks |
| SemiAnalysis ($500-5k/yr tiers) | $500-5k | Highest-leverage paid LEAD source on memory architecture + HBM/HBF integration; "moved NVDA stock with pre-earnings channel checks" pattern per `signals/cross-source-log/2026-06-15-pm-nebius-2subagent-verification-eu-sovereign-bypass-thesis.md` |
| Bloomberg Intelligence | ~$25k/yr terminal | CIO survey aggregation; pre-earnings analyst convergence |

## Cross-cluster informants (signals at adjacent clusters that PRECEDE TC-1 events)

- **TC-6 MLCC AI-server tier bifurcation** — Walsin AGM "past 2027" + Murata CAGR 30% = PRECEDES memory-cycle confirmation by ~6-12mo (MLCC supply-cycle leads memory by 6-12mo per harness historical observation)
- **TC-5 CoPoS / glass-core packaging firming** — substrate-layer tightness signals (IBIDEN ¥500B capex + ASE-TSMC June 2025 PLP co-dev) PRECEDE memory-cycle by 12-18mo (substrate-tier qualification cycles longer)
- **TC-8 Token consumption compounding** — DEMAND-side anchor; TC-8 signals (volume outrunning compression) → expected memory demand pull-through 6-12mo later
- **PC-13 Government 90-min model-shutdown precedent N=2** — would trigger acute sovereign-AI compute demand pull → memory demand spike within 1-2 quarters
- **F1-F13 cyclical-inflection falsifier set** (per `sector/where-we-are.md` pre-committed trim sequence) — any F-falsifier firing PRECEDES TC-1 cluster-state regime change

## Convex-hull / lateral check (Critical Rule #9 + Principle #38 mandatory)

**What world-state would make LEAD indicators USELESS for TC-1?**
- Memory vendors stop publishing quarterly capex disclosures (concentrated decision-making at private CFO level) — would degrade Tier #3
- Korean Customs Service shifts to quarterly reporting or restricts semiconductor-export-volume disclosure (geopolitical motive) — would degrade Tier #1
- Hyperscaler 10-Q disclosure shifts away from "memory commitments" line-item specificity (less footnote granularity) — would degrade Tier #4
- WSTS / TrendForce data sources become paywalled at higher tier OR access restricted — would degrade Tier #2 / #10
- **In all scenarios, LEAD framework partially degrades; rely more on cross-cluster informants + Tier #9 native-language press**

**What world-state would fire ALL TC-1 LEAD indicators simultaneously (positive convex tail)?**
- Anthropic-90-min precedent N=2 fires at OpenAI / Google → sovereign-AI compute panic-procurement → memory demand vertical step-up across all hyperscalers within 1 quarter
- China memory export controls reverse (would massively shift global supply-demand balance)
- HBF productizes earlier than 2027 (Sandisk + SK Hynix pull schedule forward) → HBM-vs-NAND mix shift accelerates
- Multimodal AI consumer-explosion (TC-8 acceleration) → cell density doubling pulls forward + NAND demand 100×

**What would FALSIFY TC-1 thesis (de-promote from ACTIVE STRUCTURAL-REGIME-CONFIRMATION)?**
- Per F1-F13 falsifier set already in harness: F2 ASP rollover for 2 consecutive quarters; F7 hyperscaler inventory pre-buying pattern shift; structural-regime read posterior drops below 50% (H1 75% → <50% via accumulated evidence)
- Memory vendor capex revisions DOWNWARD (signals supply-glut anticipation) for 2+ consecutive quarters
- Korean monthly export ASP declines for 3+ consecutive months (early supply-glut signal)

## Framework validation against B47 (pre-training lead-time conservatism)

Per Principle #38 application discipline: lead-times above are MY-MODEL estimates subject to B47 systematic error (pre-training OVERSTATES fast-track government action; UNDERSTATES regulated processes; calibration uncertain for cyclical industries).

| Lead indicator | Claimed lead-time | Historical case to calibrate against |
|---|---|---|
| Korea Customs Service → WSTS | 30-45 days | VERIFIED — Korea Customs typically publishes mid-month for prior month; WSTS lags ~45 days |
| SK Hynix capex disclosure → output ramp | 3-6 months | TYPICALLY ACCURATE — well-documented memory-vendor capex-to-output cycle |
| NVDA 10-Q "memory commitments" → supplier allocation | 3-9 months | UNVERIFIED but plausible — supplier qualification cycles historically 6-12mo |
| Aschenbrenner 13F direction → multi-quarter inflection | quarterly LEAD on direction; LAG on position size | Calibration uncertain |
| Native-language press → English-language coverage | 1-2 weeks | VERIFIED via B40.1 stale-recycle pattern (N=12+ caught instances; English aggregators recycle native-press 1-2 weeks after origin) |
| SEMI WFE billings → memory fab output | 6-12 months | TYPICALLY ACCURATE — equipment-to-fab-output cycle well-documented |

Action: lead-times flagged as 🟡 my-model with B47 calibration where historical cases unverified; B47 N+1 application opportunity if cyclical-industry lead-time calibration confirmed during cycle.

## 5-source minimum daily stack for TC-1 monitoring

1. **Korea Customs Service / KITA monthly trade data** — daily refresh check; ~5-10 days lag from month-end
2. **TrendForce free excerpts** (via Tom's Hardware / Digitimes secondary) — daily scan for monthly contract-price updates
3. **SK Hynix / Samsung Memory IR newsroom + earnings calendar** — weekly check
4. **NVDA / AMD 10-Q EDGAR Atom feed** — quarterly + event-driven; CIK 1045810 NVDA + CIK 2488 AMD
5. **Native-Korean / Japanese trade press** (ETNews / Chosun Biz / Nikkei xTECH / Mynavi) — weekly scan for memory supply-chain commentary

Plus event-driven:
- Aschenbrenner 13F filings (quarterly)
- SEMI WFE monthly billings + Lam/AMAT/TEL earnings (quarterly)
- China memory export-control policy updates (MOTIE + MOFCOM monitoring)
- Cross-cluster informants (TC-5 substrate + TC-6 MLCC + TC-8 token compounding)

## Cross-references

- `meta/methodology.md` Principle #38 candidate — Lead-Lag Variable Framework
- `companies/NBIS/tracking-variables.md` — first application (N=1)
- `signals/tracking-variables-TC-10.md` — second application (N=2)
- `signals/triangulation.md` TC-1 — cluster state being monitored
- `signals/triangulation.md` TC-5 / TC-6 / TC-8 — cross-cluster informants
- `meta/cross-domain-pattern-register.md` PC-13 — interlocks with TC-1 demand-side via sovereign-AI compute panic-procurement pathway
- `signals/cross-source-log/2026-06-14-pm2-dram-asp-60yr-trend-break-structural-regime-confirmation-subagent.md` — STRUCTURAL-REGIME-CONFIRMATION origin for TC-1
- `sector/where-we-are.md` — F1-F13 cyclical-inflection falsifier set + pre-committed trim sequence

## TV-added 2026-07-10: DRAM-maker GM vs the 85% commodity ceiling (cycle-top mechanical marker)
Origin: Jukan cycle-shape model (T3, anchors verified 2026-07-10) + verifier data: SKH DRAM-segment GM ~90.9% Q2'26 (Bernstein ESTIMATE T2, not company-reported) / Micron 74.4% blended reported FQ2 → guiding ~86% FQ4. Mechanism: no commodity sustains >85% GM — at that level prices eventually crack back toward 70% GM. THE CEILING IS BEING TOUCHED NOW while the physical shortage (MS 2-3yr T2; Jensen "may last years") persists — hold both. Track: SKH segment GM each print (next ~late-Jul), MU quarterly guide, TrendForce contract-price QoQ deceleration. Marker fires when: GM prints/guides DOWN from ceiling + contract price QoQ turns negative → cycle-top mechanical signal → re-read L-series falsifiers + SUMCO LTA-insulation test + MURATA server-build tell SAME COMMIT. Companion sentiment datum: MS equity desk "peak rate of change" Jul-7, DRAM ETF -6.5%, earnings-revision breadth ~89th pct. Per `cross-source-log/2026-07-10-nvda-ndr-memory-jukan-cycle-anthropic-helium-3agent.md`.

## TV-update 2026-07-10 PM: NAND has CONVERGED to the ceiling (SNDK margin trajectory)
SNDK non-GAAP GM: 29.9% (FQ1'26) → 51.1% (FQ2, +21.2pp) → **78.4% (FQ3, +27.3pp)** → **guide 79-81% (FQ4, +1-3pp)** — the QoQ delta collapse IS the flattening-at-ceiling signature. NAND now ~8-13pp below DRAM ceiling (MU ~86% guide / SKH ~91% est) and converging; the historical NAND-lags-DRAM margin prior is compressed. Non-GAAP OM 70.9% FQ3. Rev $5.95B +251% YoY; DC revenue +645% YoY; >1/3 of FY27 bits under multi-year agreements, ~$42B LT supply backlog (T2 slide coverage of T1 PR; GAAP figures not retrieved, 403s). TrendForce: NAND contract +70-75% QoQ Q2'26, shortage through 2026, new capacity volume late-2027/28. **Joint read with the DRAM TV above: the ENTIRE memory complex is now at/near the GM ceiling — entry appeal at this point of the cycle = late (user articulation 2026-07-10, data-confirmed). Ceiling-marker watch now covers SNDK Aug-5 print + Investor Day Aug-13 alongside SKH/MU.** Book note (honest miss): SNDK +635% YTD / ~$275B cap / ~$1,814 vs our exit — read-through exit decision warrants a GRADE entry at next audit; magnitude consistent with B45 tail-under-modeling. Per SNDK-margins agent 2026-07-10 (in `2026-07-10-gitlab-deepdive` artifact set).

## TV-refinement 2026-07-10 EVE: Patel primary quotes land — attribution + ceiling-marker refinement
User supplied direct Patel quotes (Sequoia Training Data pod, identified/verified earlier today — T2 named-analyst model, primary-for-what-Patel-said):
1. **ATTRIBUTION CORRECTION:** the "4x done / 2-3x more / 85% ceiling then halve to 70s" cycle-shape model booked this morning as Jukan's = **PATEL'S model, relayed by Jukan** (verbatim match). One analyst voice, not two — triangulation N-count for the cycle-shape model = 1 (anchors independently verified vs TrendForce/Bernstein remain valid).
2. **CEILING-MARKER REFINEMENT (resolves the morning's like-for-like caveat):** Patel: "We're still NOT at 85-90% GM for memory, but we'll get there." Reconciliation with our data: SKH ~91% = DRAM-SEGMENT Bernstein ESTIMATE; MU 74.4% = BLENDED REPORTED; SNDK 78.4% = NAND blended. **The marker is hereby defined on BLENDED REPORTED GM (measurable, like-for-like): memory-maker blended GMs reaching 85-90% then rolling = the top signal.** Current state: blended 74-78% and climbing → per Patel's model the ceiling is AHEAD, not touched — the morning's "being touched NOW" applied to segment estimates only. Downgraded accordingly.
3. **Quantified gap (Patel model, T2):** capacity +20-30%/yr for 3 years (cumulative 1.73-2.20x, computed) vs demand doubling annually (8x/3yr) → cumulative gap ~4.1x at 25%/yr capacity (computed). Tension flag: carried supply-growth figure +16% (Jun-23 CXMT entry) vs Patel's 20-30% — different vintages/scopes, reconcile at next TC-1 audit. Full-cycle price path per Patel: 8-12x trough-to-peak (4x done × 2-3x forward, computed).
4. Mechanism restated: KV-cache explosion from reasoning inference = the demand leg (consistent with carried TC-1 mechanism).
**Net for the entry-appeal question (user 2026-07-10): two-sided —** Patel's own model says price upside REMAINS (2-3x) before his ceiling→halving sequence; "memory late" is TRUE for the margin-cycle position but EARLY relative to Patel's forward path. The book's stance (HOLD held names on LTA insulation, no NEW memory entries, GM-marker armed on blended-reported basis) accommodates both readings without resolving the unresolvable.

## TV-note 2026-07-10 EVE: HBF/NAND KV-offload = the CONFIRMED bypass route (Rule #9 closure for the memory constraint)
Verifier-confirmed (T1/T2 per `cross-source-log/2026-07-10-eve-soxx-flows-weka-memory-hierarchy-daily-update-2agent.md`): High-Bandwidth Flash — SanDisk + Kioxia, ~512GB @ ~1.2TB/s per stack, HBM-to-SSD tier purpose-built for KV-cache overflow; **SanDisk-SK hynix MoU to standardize HBF for inference servers** (SKH = HBM incumbent co-standardizing its own substitution route = hedged incumbency); WEKA Augmented Memory Grid (NVMe token warehouse, NVIDIA Dynamo integration) + VAST = software tier, private. Status: SAMPLING, pre-volume. Read: the bypass EXISTS and is named — it caps the DRAM/HBM price path at the margin on a 2027+ horizon (TTQ ~1-2yrs to volume), consistent with (not contradicting) the Patel 2-3x forward path on the shorter horizon. Beneficiary direction if memory stays bound: NAND tier (SNDK/Kioxia) gains a NEW demand class beyond SSDs. Watch: HBF volume-production announcements = the bypass going live.

## TV-upgrade 2026-07-10 NIGHT: GM-ceiling marker gains a MECHANISM DIAGNOSTIC
`sector/memory-gross-profit-bridge.md` built (+ `meta/scripts/memory_gp_bridge.py`): the ceiling marker now classifies each print via the SIGN TEST — GM↓+ASP↑ = cost-driven mix artifact (HOLD; GP dollars can grow +13-37% through the compression, computed) vs GM↓+ASP↓ = price-driven crack (Lens 2: 88→70% GM at commodity cost = ASP −58%, GP/unit −67%, ×3.00 units to offset = impossible at 20-30%/yr capacity growth). Run the bridge decomposition at SKH late-Jul / SNDK Aug-5 / MU guide / Samsung prelim. Units line of the bridge = SUMCO demand line (the LTA-insulation instrument).

## TV-note 2026-07-11 SAT: FIRST TrendForce moderation language — the second derivative turns
TrendForce Jul-3 release (T2, surfaced Sat Asia scan per `cross-source-log/2026-07-11-sat-apple-openai-asia-scan-flags-resolved.md`): 3Q26 NAND contract guided **+10-15% QoQ vs 1H26's ~93-98% jumps** — AI-server demand still supportive, consumer weakening, high base. First moderation language of the cycle from the contract-price source the marker tracks. GP-bridge pre-read: ASP still RISING → sign test remains in ARTIFACT territory; but QoQ deceleration is exactly the path INTO the ceiling the marker watches (price gains slow → GM flattens → then the crack-vs-artifact question goes live). NOT a falsifier; it is the marker's expected approach sequence. Watch unchanged: SKH late-Jul print (first bridge run), SNDK Aug-5, MU guide. Consistency note: NAND contract +70-75% QoQ Q2'26 (carried) → +10-15% Q3 guide = the delta collapse arriving at the CONTRACT level, mirroring SNDK's reported-GM delta collapse (+27.3pp → +1-3pp guide).

## TV-print 2026-07-11: NANYA Q2 — first BLENDED-REPORTED GM print inside the high-70s band (climbing, not rolling)
Nanya 2408.TW Q2'26 investor conf Jul-10 (T1 via TW press, per `cross-source-log/2026-07-11-sat-eve-ai-brief-routing.md` verdict): **blended reported GM 79.5%** (+11.6pp QoQ; Q2'25 −20.6%), ASP +60% QoQ, Q3 guided higher (channel +20-30% contract), zero peak language. Marker state: **APPROACH — the cleanest commodity pure-play is now ~5-10pp below the 85-90% Patel zone and still climbing.** Sign state GM↑+ASP↑ = the bridge's compression question not yet live for Nanya. Supply side: 2027 capex 3.85x to ~NT$200bn (Taishan, non-HBM, output 2028) — BUT industry planned wafer growth ~7.5%/yr vs ~12% needed (Nikkei T2) = **supply response UNDERSHOOTS; carry the undershoot, not the glut read.** Watch unchanged: SKH late-Jul (first bridge run), SNDK Aug-5, MU guide; Nanya Q3 print = next legacy-tier ceiling read.

## TV-flag 2026-07-11 EVE: Patel "storage still has room to double" (T3, UNRECONCILED — verbatim check required)
Third-party write-ups of the SAME Jun-30 Sequoia episode render a "storage still has room to double" line (per `cross-source-log/2026-07-11-sat-patel-sequoia-full-episode-extraction.md`). Carried canonical (verified primary quotes 07-10): DRAM "4x done, 2-3x more." IF "double" = his current remaining-DRAM-path view, that is a downgrade of the forward leg with marker implications; more likely NAND-specific or paraphrase compression. RULE: carried 2-3x stays canonical; do not blend; resolve only against verbatim (YouTube captions accessible to the user interactively). No marker change.

## TV-flag RESOLUTION 2026-07-11 NIGHT (user-caught newer appearance): "storage double" garble dies
WisdomTree episode (~Jul-9, per `2026-07-11-sat-patel-sequoia-full-episode-extraction.md` correction section): the CN recap renders storage (SSD-inclusive) upside as **"2-3x" room** — same figure as the carried DRAM path, scope extended to NAND. The "room to double" rendering from the Sequoia write-ups = paraphrase artifact, DISCARDED. Carried "4x done, 2-3x more" stays canonical, now with a T3 NAND-extension. Verbatim confirmation still owed (all transcript routes 403'd); no marker change either direction.
