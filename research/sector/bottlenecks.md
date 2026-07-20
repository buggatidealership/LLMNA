# Bottleneck Forecast — Current, Next, Next-Next

**last_review: 2026-07-06** (monthly run, 2 days late — WAKE-infrastructure failures consumed 07-03/04; 2 Opus verification subagents, web-swept 2026-07-06)
**Next review due: 2026-08-06** (monthly cadence — check at session start)

## 2026-07-06 BOTTLENECK-FORECAST — financing promoted to next-binding; LPDDR5X call CONFIRMED (now already-binding); InP sharpest new pinch

**Inputs:** 2 web verification subagents (current-state delta + next-next sweep) + in-repo triangulated state (TC-1 N=22+, TC-12 N=5, TC-13 N=7+, `sector/ai-funding-shock-node.md` built 07-04). WORKFLOW #7 per Workflow #9 macro-first discipline.

### Today's binding (updated)

| Constraint | Fresh read (date/tier) | Direction | Change vs 06-04 file |
|---|---|---|---|
| **Grid hardware** (transformers >160wk, HV-class 4-5yr; MV switchgear sold out through 2028; 30-50% of planned 2026 US DC capacity delayed) | Build.inc / SemiAnalysis 2026 T2-T3 | Tightening | PROMOTED to co-#1 current binding (was 6-12mo tier) — TC-13 N=7+ confirms |
| **LPDDR5X / conventional DRAM** (+89% QoQ Q2'26 LPDDR5X 12GB; 8GB module $40→$110 in 6mo; relief earliest Q4'27 per Counterpoint) | tweaktown/TechTimes 07-03 T2-T3 | Tightening hard | **06-04 next-binding call CONFIRMED — now already-binding**, ahead of the 6-18mo window we forecast |
| DRAM contract 3Q26 — **3-way dispersion ARBITRATED** | TrendForce 2026-07-03 T2: conventional +13-18% QoQ, PC +15-20%, server +13-18%; Samsung ask "up to +20%" | Tightening, decelerating | The +32% broker note (2026-07-03 day-state open thread) = OUTLIER; low-to-mid case wins; deceleration-from-high-base, not acceleration |
| HBM4 | All 3 makers qualified + producing for Vera Rubin, Q3 shipments; SKH slowing HBM4 ramp for DDR5 profits (TC-12-consistent) | Demand-tight, multi-source qual = relief vs prior gens | HBM no longer the sharpest pinch — margin inversion (TC-12) redirects supplier behavior |
| CoWoS | Fully booked; 75-80k → 120-130k wpm exit-2026 | Tight, ramping | Unchanged read |
| **InP substrate / EML lasers** (>70% supply gap; 2" optical-grade ~3× price YoY; NVDA locked EML capacity, lead times beyond 2027; MOCVD tools 1-2yr) | Digitimes/TrendForce Dec-25→2026 T2 + T3 aggregators | Tightening severely | **SHARPEST NEW ADDITION to current-binding** — TC-7 escalates from geopolitical niche to volume constraint riding the 1.6T/CPO ramp (1.8M→30M+ units 2026) |
| NAND | 3Q26 flat to +0-5%; ent-SSD lead times 8-14wk | **Easing** (exception: SLC NAND/NOR structural shortage into 2H26, TrendForce 06-16 T2) | NEW: first memory sub-segment to ease |

### 6-12 months (next-binding)

| Constraint | Evidence | P(binding) (my model) |
|---|---|---|
| **💰 FINANCING / COST OF CAPITAL — NEW ENTRANT (PD-6 promoted into this file)** | AI/DC credit spreads doubled ~50→>130bps in 3 months (highest since 2009); banks at Oracle-exposure limits; loan syndicates clogging; completions slipping 2027→2028 (Fortune/Bloomberg T2); ~$1.5T tech new debt 2025-27 (CreditSights T2). Gates MARGINAL buildout (neocloud/SPV/tenant-concentrated), NOT mega-cap balance sheets. **Rates-driver note (self-corrected in-cycle):** market prices only ~19% for a hike at the JULY 28-29 meeting specifically (T2/T3) — the near-term leg is quiet, but this does NOT refresh the node's YEAR-END-cumulative hike odds (~two-thirds as of the 07-04 node refresh; different quantity — do not conflate). Live leg near-term = spreads/syndicate-capacity, not the policy rate | **55-65% co-binding on marginal buildout by 2H27** — least consensus-priced item in the sweep |
| 800V HVDC components (SSTs, DC breakers, busbars — Rubin-class racks ship 3Q26, broad 2H27-28; sidecar TAM ~$11B 2028) | TrendForce 06-25 T2; ST shipping 6-20kW boards now T1 | ~60-70% as the grid-hardware SUB-pinch |
| Liquid cooling at 600kW racks | Vertiv CoolChip CDU 600 commercially listed (T1 vendor) — supply forming AHEAD of 2027 need | ~40% (downgraded — supply anticipating) |
| DC skilled trades (439-499K worker shortfall; electricians/substation engineers tightest) | ITIF/Build.inc T2-T3 | 75-80%, but expresses as cost+schedule-slip, not hard stop |

### 12-24 months (next-next — the edge)

| Constraint | Evidence | P(binding by end-2028) (my model) |
|---|---|---|
| InP capacity structural (new capacity only post-2027) | Digitimes T2 | 65-75% through 2027, narrowing to 30-50% gap post-2028 |
| **Low-CTE glass (furnaces)** — the REAL glass-core pinch, not substrate assembly: Corning/Schott/AGC >90% share, furnace build 12-18mo | TrendForce/Digitimes T2; Samsung-Sumitomo ~$310M glass-core JV 2026-07-02 T2; Absolics sampling AMD, first commercial glass-core accelerators late-26/early-27 | 30-40% (enabling-tech more than gate) |
| 300mm leading-edge wafers — price/allocation gate, not shortage cliff: duopoly "margins over volume," step-up LTAs pricing higher yearly through 2027; NXP/Infineon locked pricing | Semiecosystem/Lapedus T2 | 55-65% — **SUMCO wafer-hike thesis CONFIRMED by independent sweep** |
| Water/siting permits | Q1'26 figure (75+ projects/$130B blocked) is STALE — no clean Q2'26 aggregate found; regional gate (WHERE not WHETHER) | 50-60% regional |

### Cross-constraint insight (highest-order finding this cycle)

**Financing is upstream of every physical pinch:** if spreads gate neocloud/SPV buildout, marginal demand comes OUT of the transformer/memory/InP queues — the funding constraint partially RELIEVES the physical ones. This coupling (financing ↔ physical demand) is the next verification cycle's focus and is already modeled in `sector/ai-funding-shock-node.md` (canary basket: CoreWeave $4.2B 2026 maturity; Nvidia 10-Q buyback footnote ~Aug). 2nd order (P~60%, my model): a 2H27 financing squeeze hits neocloud GPU demand before it hits hyperscaler memory LTAs — LTA-floored memory names are the relatively insulated leg (TC-12/Micron 16-SCA structure).

**Held-name implications:** MURATA — MLCC demand leg unchanged (TC-13 #4-ranked pinch; 800V adds mandatory IBC-stage content). SUMCO — margins-over-volume + LTA step-up read independently confirmed this cycle. Watchlist-reference memory names (HYNIX/SNDK/KIOXIA): DRAM-dispersion arbitration lands at low-to-mid case — supportive-but-decelerating; Jul-29/late-Jul print predictions unchanged.

**Position implication: 🟡 HOLD both held names — no size change — grid+financing constraints extend the AI-server MLCC demand runway (MURATA) and the wafer price/allocation gate (SUMCO); no falsifier touched; cash deployment still envelope-gated, and the financing-constraint finding argues for keeping the staged-tranche discipline in `portfolio/targets.md` rather than accelerating deployment.**

---

## 2026-06-04 PM update — LPDDR5X / mobile DRAM promoted to 6-18mo next-binding

**Trigger:** User question on next-bottleneck migration; verification via 4-source segmented-triangulation surfaced LPDDR5X as dominant emerging bottleneck. Full BOTTLENECK-FORECAST artifact: `research/signals/cross-source-log/2026-06-04-next-bottleneck-lpddr5x-mobile-dram-forecast.md`.

**Key evidence (Tom's Hardware T2 + IntuitionLabs T3 + Edge AI Vision Alliance T3 + IDC T2):**
- "Every wafer allocated to an HBM stack for an Nvidia GPU is a wafer denied to the LPDDR5X module of a mid-range smartphone" — Tom's Hardware
- Data centers consuming 70% of memory chips produced worldwide
- LPDDR4X + LPDDR5X undersupplied through H2 2027
- NPU bottleneck is memory-traffic-bound, not compute-bound

**Portfolio beneficiaries (held):** HYNIX 10.13% (direct LPDDR5X), MURATA 11.45% (MLCC for NPU power delivery), SUMCO 4.43% (wafer), ARM 10.5% (NPU royalty), SNDK 5.2% (on-device storage)

**No new entries required** — existing portfolio captures thesis. HOLD all.

*(⚠️ HISTORICAL — annotated 2026-07-06 audit: the held-list and HOLD-all directive above reflect the June-4 book. As of the 2026-07-05 baseline only MURATA + SUMCO are held; HYNIX/SNDK exited ~07-01/02, ARM exited 06-14. Do not treat as current position guidance.)*

---

## TL;DR

Today's binding: **HBM3E + CoWoS-L + Taiwan packaging**. Mostly consensus, mostly priced.
6–12 months out: **Power siting + grid interconnect + advanced cooling**. Partially priced.
12–24 months out: **Networking silicon (CPO, optical interconnect) + advanced substrate**. Largely unpriced — this is where the edge is.

## Today's binding constraint (priced ~80%)

**Update 2026-05-26 (per `research/signals/events/2026-05-25-sk-hynix-ihbm.md`):** SK Hynix announced iHBM (Integrated Cooling Elements at the D2D PHY layer; 30% thermal resistance reduction; HBM5-targeted). This reinforces the HBM bottleneck duration: Samsung HBM3E qualification path (the consensus alternative supplier) now needs to qualify thermal performance parity in addition to capacity + yield — effective TTQ extends. CXL via ALAB remains a substitute topology at the system level (not HBM die level); LPDDR5X alternative topology unchanged. The thermal moat compounds with existing supply moat (3-year capacity gap) + packaging moat (MR-MUF).

| Constraint | Detail | Beneficiaries | Status |
|---|---|---|---|
| HBM3E supply | SK Hynix sold out 2026; Samsung qualification in progress; Micron HBM3E ramping | MU, SK Hynix (.KS), Samsung | Mostly priced |
| CoWoS-L packaging | TSMC ramping from ~55K → ~130K wpm exit-2026; NVDA gets ~60% | TSMC, NVDA, OSAT subset | Mostly priced |
| Frontier-node wafer | TSMC N3/N3P; ASML EUV systems | TSMC, ASML, AMAT, LRCX | Mostly priced |
| Skilled silicon talent | Esp. RTL, packaging engineers — affects competitor ramps | Incumbents (NVDA, TSM), barrier to AMD/custom | Soft constraint, hard to invest in |

## 6–12 month forecast (next-binding — partially priced)

| Constraint | Detail | Beneficiaries | Status | Signals to watch |
|---|---|---|---|---|
| Datacenter power siting | New AI sites need 100MW+ firm power. Grid interconnect queues are 2–7 years in many ISO regions. | VST, CEG, TLN, GEV (turbines), NEE | Partial pricing — VST/CEG already up, but more leg if S3 plays | Hyperscaler PPAs > $50/MWh, new nuclear restart announcements |
| Liquid cooling | GB300 NVL72 needs ~$50K cooling per rack. Air cooling no longer viable at density. | Vertiv (VRT), Dell/HPE/SMCI on system side, specialized cooling cos | Partially priced (VRT up materially) | Hyperscaler RFPs explicitly liquid-cooled |
| Power conversion / electrical | Higher density = more switchgear, transformers, busbars | ETN, GEV, Schneider | Partial pricing | Lead times on transformers extending beyond 24mo |

## 12–24 month forecast (next-next — UNPRICED, this is the edge)

These are the bets where consensus is not yet positioned. Each has a probability of becoming binding.

| Constraint | Detail | P(binding by end 2027) | Beneficiaries | Status |
|---|---|---|---|---|
| **Optical interconnect / CPO** | As compute density rises, copper hits SerDes limits. Co-packaged optics (CPO) becomes mandatory for >800G fabrics. | 55% | MRVL, ANET, COHR, LITE, possibly NVDA (Spectrum-X CPO roadmap), TSM CoWoS-L photonics | Largely unpriced — names like MRVL trade as commodity semi |
| **Advanced substrate (ABF, glass)** | Substrate shortage was 2022's pinch; could return with Blackwell Ultra + Rubin scale. Glass substrate is the next-gen play. | 40% | Ibiden (Japan), Unimicron (Taiwan), AMAT (glass substrate equipment), Intel (glass research) | Unpriced — niche |
| **Inference eval / observability** | As agents scale, the eval/observability/safety stack becomes mandatory enterprise spend. | 65% | DDOG, BSY, custom eval providers, possibly CRWD | Partial — DDOG repricing but more leg |
| **CPU rebalance (agentic)** | If GPU:CPU shifts to 1:4 or tighter, datacenter CPU socket count grows. AMD EPYC + Graviton + ARM benefit. | 50% | AMD (EPYC), ARM, possibly Intel if Xeon recovers | Partially priced via AMD but specific to CPU SKU |
| **Memory bandwidth (DDR + custom DRAM)** | Agentic workloads with large context = memory bandwidth strain. May force HBM4 + premium DDR. | 60% | MU, SK Hynix, Samsung | Priced in HBM; DDR side under-priced |
| **Hyperscaler-internal training silicon scale** | If TPU/Trainium/Maia scale beyond ~30% of inference, AVGO/MRVL/TSM benefit more than NVDA. | 35% | AVGO (custom Si for GOOG), MRVL (AWS/META), TSM | Partial — AVGO up materially but if S2 plays out, more leg |

## How to use this file

- **At INGEST:** when an article mentions any of the constraints above, update the relevant row + the signals column. If a signal fires that confirms a "next-next" constraint becoming "next", promote it and re-evaluate.
- **At BOTTLENECK-FORECAST (monthly):** re-examine each row. Has lead time shortened? Has a new candidate emerged? Has the probability shifted?
- **For each row, ask:** is a name in our universe positioned to benefit when this binds? If not, surface to `watchlist/candidates.md`.

## Historical lessons

- The CoWoS bottleneck of 2023–2024 was visible 18 months before consensus priced it (NVDA earnings call mentions of "supply constraints" in late 2023). Names tied to advanced packaging (specifically TSMC's CoWoS expansion winners) outperformed when consensus caught up.
- HBM was a similar pattern — SK Hynix's pricing power was visible in their margin trajectory before sell-side fully modeled it.
- The lesson: the edge is in the 12–24 month forecast, not the 0–6 month consensus pinch.

---

## 2026-06-02 Computex Day 1 update

Per `signals/cross-source-log/2026-06-02-computex-2026-day1-synthesis.md`:

**Current binding** (added 2026-06-02):
- HBM4 (already in tier): Hynix 70% Vera Rubin / Samsung qualified at 28-30% / Micron 17-18%; 22.2 TB/s per GPU (+10% vs CES spec)
- CoWoS (already in tier): ~130K wpm exit-2026; 4× capacity vs late-2024
- **MLCC (NEWLY ELEVATED)**: +182% per Vera Rubin rack vs GB300 per Morgan Stanley/Korea Herald T2; 26-40wk lead times on premium grades; Goldman 4× demand 2025-2030 vs 10%/yr capacity

**6-12 month next binding** (updated):
- Power infrastructure (already in tier): 800V HVDC adoption + 600kW Rubin Ultra racks
- **CCL/PCB materials (NEWLY ELEVATED)**: M9 quartz fiber chokepoint; CCL +74.5% YoY Korea prices; 6-month lead times with quota systems; 2-year equipment lead times
- CPO transition (already in tier): Wiwynn hyperscale-ready demo + NVDA Spectrum-X Photonics

**12-24 months out**:
- Memory disaggregation + optical interconnect (already in tier) — **NVDA ICMS optical-attached KV memory pool validates this from NVDA itself**
- Rubin Ultra 600kW per-rack infrastructure (H2 2027)

last_review: 2026-06-02 (Computex Day 1 INGEST)


---
## CANDIDATE INPUT for next BOTTLENECK-FORECAST run (logged 2026-07-02; NOT a forecast run — last_review unchanged)
**Packaging MATERIALS + assembly-equipment as the next-next bottleneck (INF-1, P~65% my model):** per `signals/cross-source-log/2026-07-02-ectc-INFERENCE-pass-8-second-order-reads.md` — every post-CoWoS scaling path (sub-25µm bumps, panel warpage/overlay, sub-2µm damascene RDL, microfluidic sealants, glass edge-chemistry) gates on a materials/equipment layer dominated by TSE-listed Japanese chemistry names + bonding-tool vendors (BESI Tier-S). The capacity-slot bottleneck (CoWoS) is priced and now has credible second-sources (EMIB-T cert end-2026); the enabling-layer bottleneck is not. Evaluate for the "next 12-24mo" slot at the next full forecast run alongside the existing power/HBM entries.

---

## 2026-07-08 INTERIM REGISTER UPDATE (not a full monthly run; per `signals/cross-source-log/2026-07-08-ccl-trio-divergence-2agent-workflow9.md` + TC-16 promotion)

**NEW next-binding candidate — the T-glass → HVLP4 rotation in the CCL stack:** (a) Japanese T-glass/NER-glass cloth: Nittobo ~90% share, full capacity, zero inventory, relief 2027 (T1 Nikkei) = the deepest structural choke behind AI server boards; (b) HVLP4 copper foil rotates in as the 6-12mo pinch (Mitsui ~490t/mo vs ~560t/mo H2-26 demand; gap → ~2,500t 2027, T2 Digitimes/Goldman). Visible layer (CCL makers) = pass-through toll-collectors; Nvidia already dual-tracking upstream directly. Bypass-route names: Nittobo 3110.T (the choke itself), Mitsui Kinzoku 5706.T (foil), vs consensus EMC/TUC. Kyber slip does NOT relieve this (shared across GB300/Rubin generations). Slots alongside the existing InP + financing next-binding candidates; full re-rank at the 2026-08-06 monthly run.
**last_review unchanged (2026-07-06 monthly stands; this is an interim addendum).**

---

## 2026-07-18 INTERIM REGISTER UPDATE — NEXT-REGIME sweep (not a full monthly run; last_review unchanged, next full run due 2026-08-06)

**Trigger:** ad hoc BOTTLENECK-FORECAST sweep on WFE/tool strain, memory capex supply-response timing, financing-node update, and a fresh 12-24mo constraint scan. Full source list in chat output of this date; key promotions below.

**1. Current-binding CONFIRMED/escalated:**
- LPDDR5X/DRAM tightness now spilling from AI-servers into GENERAL-PURPOSE servers: enterprise DRAM lead times >40wk, prices +90% since late-2025 (Inventec warning per Digitimes/TechTimes 2026-07-16 🟡 T2). TrendForce: server DRAM contract +13-18% QoQ 3Q26. This sharpens the existing L33 casualty-leg lesson (enterprise-IT vendors as casualties) with a fresh dated print.
- EML/optics gap quantified: 1.6T transceiver 2026 shipments ~15M units vs ~10M-unit gap; Lumentum ~50-60% share of high-end EML, sole volume 200G/lane supplier (T2 industry trade press, 2026). SiPh gaining share as release valve (~40-45% of 800G, ~60% of 1.6T) — directionally consistent with existing InP/EML row, though the %-gap metric differs from the register's ">70% supply gap" figure (different denominator — flagged, not reconciled).

**2. NEW candidate — HBM4E/HBM5 base-die crowding leading-edge LOGIC capacity (promote to 12-24mo slot, P~55-65% my model):** HBM4E base dies move to TSMC/GUC 3nm-class; Samsung's HBM5 base die moves to Samsung's OWN 2nm GAA node (per Tom's Hardware/Siemens/Sammy Fans, 2026 🟡 T2-T3). This is a NEW claim on leading-node LOGIC wafer capacity (TSMC 3nm / Samsung 2nm) layered on top of the existing HBM DRAM-wafer story — under-tracked because consensus models HBM capacity purely as a DRAM-fab-allocation question, not as a foundry-logic-allocation question. Beneficiaries: TSMC (dual-benefit), GUC (2454.TW, thin Western coverage — base-die ASIC design house), Samsung Foundry. Risk: crowds NVDA/AMD/AVGO's own leading-node logic slot competition at the margin.

**3. NEW candidate — advanced-node AI-ASIC test/burn-in capacity concentration (promote to 6-12mo slot, P~60-70%):** KYEC >90% share of Nvidia AI-chip FT/SLT/burn-in, ~100% share of Google TPU final test (Medium/Digitimes 2026 🟡 T2-T3); ASE capex $8.5B 2026 guide "will likely need to be revised up again" per COO Tien Wu (X/Nystedt relay of media report, 🟡 T3) amid "severe capacity shortages"; Advantest ATE lead times >6 months (Digitimes 2026-01-16 🟡 T2); Aehr securing hyperscale AI-ASIC burn-in wins (Aehr 8-K 2026-02 🟢 T1). Genuinely under-priced vs HBM/CoWoS/optics — test capacity is a hard co-requisite no chip ships without, and KYEC/Aehr carry thin Western sell-side coverage.

**4. Financing node ESCALATED, not just confirmed:** Oracle 5Y CDS ~198bps (2026-07 🟡 T2, bondblox/Yahoo) — exceeds 2008 GFC-era levels for the name; ex-Oracle hyperscaler (AMZN/GOOGL/MSFT) CDS ~49bps, highest since 2018 (🟡 T2) — market is discriminating by balance-sheet quality, not pricing AI-debt as a monolithic bloc. Hyperscaler spreads broadly +25bps over IG index (10-yr high). FIRST concrete pulled/delayed deal this cycle: Prime Data Centers postponed $500-600M Nordic bond 2026-07-13 (Bloomberg 🟢 T1/T2) — investors declined proposed terms. Hyperscaler bond cover ratios collapsed 5x (Feb-26) → <2x (Jul-26) (Forbes/Motley Fool 🟡 T2). Amazon still cleared a $25B IG bond 2026-07-07 (🟢 T1) — mega-cap IG issuance still clears; the stress is concentrated in sub-IG/private-credit/SPV-tier names (Oracle-adjacent, neocloud, project-finance). Read: financing-gate remains a MARGINAL-buildout constraint, now with its first dated casualty (Prime DC), not yet a mega-cap constraint.

**5. Memory capacity supply-response timing — CONFIRMS "squeeze runs long," minor Micron acceleration:** Samsung P5 — PO issuance from Q2'27, phase-1 100k wpm, production not until 2028 (SemiWiki/Korea Times 2026-06/07 🟡 T2-T3). SK Hynix M15X Cheongju — H2'26 start at 40k wpm → 80k wpm in 2027; Yongin cluster first-fab 360k wpm DRAM not until H1 2030, part of Yongin online 2028 at 70k+ wpm; SK Hynix targeting 1M wpm total DRAM capacity by 2030 (TrendForce 2026-06-05 🟡 T2). Micron — FY26 capex raised to ~$27B; Idaho fab wafer-out moved UP to mid-CY2027 (from H2'27, a modest acceleration); 2nd Idaho fab construction starts 2026, operational 2028; NY fab groundbreaking early 2026, supply 2030+; Tongluo Taiwan (ex-Powerchip) meaningful shipments mid-2027 (Digitimes/Benzinga/TrendForce 2026 🟡 T2). **Net: no material new DRAM supply before mid-2027 anywhere; most volume lands 2027-2028; Samsung P5 and SK Hynix Yongin main ramps land 2028-2030.** Gates the memory-bottleneck duration at "through 2027, into 2028" — consistent with, and now more precisely dated than, the existing register.

**6. Negative findings (explicitly logged, not upgraded):**
- Liquid cooling for Rubin: no shortage evidence found (cold-plate/CDU vendors "manufacturing now"/"scaling production") — consistent with the register's existing "supply anticipating, ~40%" downgrade. No change.
- CoPoS/panel-level packaging: pilot line mid-2026, mass production 2028-29 (TrendForce/TechTimes/Wedbush 2026 🟡 T2) — confirms this sits at or beyond the 24mo horizon edge, not urgent within the current 12-24mo window; slots as the visible expression of the already-logged INF-1 packaging-materials candidate (2026-07-02).
- 800V HVDC/SiC-GaN: reinforces existing next-binding row with sharper detail (SiC/GaN ~10-15% of Kyber-rack power-semi content, 20-30wk lead times, 2027 mass deployment) — no rank change.

**Helium (WATCH, not yet ACT — source tier weak):** Qatar Ras Laffan disruption (~Mar-2026) removed materially reported helium supply share; EUV lithography + fiber-optic drawing both helium-dependent with no substitute; spot prices reportedly doubled. Sourcing skews T3 (Oregon Group/Boing Boing/Al Jazeera) — flagged as a genuinely under-tracked candidate but NOT triangulated at T1/T2 yet. Action: seek Linde/Air Products/Air Liquide earnings-call commentary before any promotion.

**7. CONSUMABLES LAYER (sweep part 2, adversarially adjudicated — full detail `signals/cross-source-log/2026-07-18-sat-bottleneck-next-regime-sweep-4agent.md` §3):** China tungsten-feedstock cutoff to Japan REAL (zero exports Feb-Apr 2026, 🟡 T2 customs data; Sumitomo Electric CEO 🟢 T1-adjacent) with WF6 price shocks (CN 5N spot +232.7% YoY arithmetic-checked; Korean SK Specialty 70-90% 2H26 hikes to Samsung/SKH, 🟡 KR T2) — BUT the viral "permanent Japanese WF6 production cessation from Jul-1" claim is REFUTED (no TDnet disclosure from 4047/4044; ex-diplomat fake-news label; Kanto Denka guiding FY27 sales +45%). Register treatment: WF6/gases = a COST-inflation constraint (real, broadening to HF/IPA) not a supply-cliff constraint; H2-branch (de facto Japanese output collapse, P~25 my model) carries the pre-registered markers (TDnet feeds, ~Aug Kanto Denka print, fab schedule attributions). NF3: Kanto Denka = sole domestic producer post-Mitsui-exit (🟢 T1) on a fire-damaged line = single-point-of-failure node, logged. Also verified: JX Advanced Metals 5016.T ~64% semiconductor sputtering-target share (company-sourced) — highest single-vendor concentration found anywhere in the consumables stack, newly listed 2025, thin coverage.

**last_review unchanged (2026-07-06 monthly stands; full re-rank due 2026-08-06 — the two NEW candidates §2-§3 above + consumables treatment get formally ranked there).**

---
## CANDIDATE INPUT for the 2026-08-06 monthly run (logged 2026-07-19; NOT a forecast run — last_review unchanged)
**Robot edge-compute/LPDDR leg (TC-19 candidate, 18-24mo+ slot):** edge-first architecture converged N=3+ (Figure/1X/Tesla onboard; Jetson T3000/T2000 32/16GB LPDDR5X SKUs shipping Q1-27) but demand-side is 2028+ per Micron CEO T1 ("multi-decade cycle... latter part of this decade"; humanoids 10× L2+ vehicle memory). Stage for the next-next tier, do NOT promote to 6-12mo. **Also: KVCache-centric serving (N=4 orthogonal: Mooncake/DeepSeek-3FS/NVIDIA-Dynamo/vLLM) = conventional-DRAM + eSSD demand per inference dollar RISING — TrendForce 1Q26 eSSD record $18.46B partly KV-offload-attributed; consider a "serving-substrate memory" row distinct from HBM at the re-rank.** Per `signals/cross-source-log/2026-07-19-sun-eve-weisenthal-mooncake-sunday-3input-batch.md`.
**UPDATE 2026-07-20 → N=5:** Nvidia **CMX (Context Memory eXtension)** = the first NAMED Nvidia-platform instance of KV-cache→SSD offload (Vera Rubin; ICMS CES-Jan-26 → CMX GTC-Mar-26; partner ship 2H-26), with a named memory-maker design win (**Samsung PM175x eSSD**) + the wider WEKA/VAST/Hammerspace vendor set. Direction now well-corroborated (N=5); **the demand MAGNITUDE stays single-source (Citi 35M→100M TB, contradicted by Kiwoom 35M→20M) → do NOT size the row yet** — mint the row at Aug-6 only if a non-Citi magnitude anchor lands. Per `signals/cross-source-log/2026-07-20-mon-samsung-nvidia-nand-cmx-alliance-2agent-INGEST.md`.
**EFFICIENCY-PRONG datum for the GRID-HARDWARE row (2026-07-20, K3-caught B47-N=2):** Google "Frozen v2" (single-sourced, research-stage, 2028) projects 6-10x tokens per unit power via architecture-in-silicon — the first credible category-scale datapoint on the EFFICIENCY side of the power-bottleneck thesis. Almost certainly Jevons-dominated (my model), but it is a U8-class falsifier-side entry: if architecture-ASICs scale fleet-wide, power-demand growth per unit compute slows. Watch alongside the Etched category proxy. Per the K3 adjudication in `signals/cross-source-log/2026-07-20-mon-google-frozen-v2-architecture-in-silicon-2agent-INGEST.md`. **Cross-segment note 2026-07-20 EVE (analysis, not a counted N):** the Google "Frozen v2" architecture-ASIC story confirms the specialization-curve convergence — architecture-ASICs (Frozen v2, Etched Sohu) and even weights-hardwired chips (Taalas HC1) all leave KV-cache + activations HBM/DRAM-bound; every custom-silicon point on the curve preserves the serving-substrate memory demand while attacking compute/weight-fetch. Per `signals/cross-source-log/2026-07-20-mon-google-frozen-v2-architecture-in-silicon-2agent-INGEST.md`.
