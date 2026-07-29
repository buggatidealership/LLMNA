# 2026-07-29 WED — Anon-post intake: "HBM mix dragged the SKH miss; HBM-per-accelerator eats DRAM's bit share" + operator hypothesis (China-entry overreaction)

**WORKFLOW: INGEST.** User-shared anonymous analyst post (T3, engineer/speculator voice) + a Minecraft-style HBM "crafting recipe" infographic (illustrative only — pinned as the metaphor's visual: wafers+TSV→DRAM die; 9 dies+base logic→HBM3E 8-Hi; stacks+compute die→accelerator via CoWoS-L; not evidence). User instruction: don't take literally, extract the intended mechanism, verify, act within the harness on findings. **Operator's own added hypothesis: the KR move may be China-entry (CXMT/DUV) overreaction — booked into the reaction-hypothesis set (it was a NARRATIVE-UNGRADED crash driver in the 07-28 EOD artifact; today's +2% bounce ON a consensus miss is consistent with sentiment-overshoot).**

**Claims extracted (T3 until verified):** (1) SKH miss = MIX story (HBM share up at ~flat HBM pricing vs vertical commodity DRAM → blended ASP dragged); (2) recent memory earnings growth mostly from commodity DRAM, not HBM; (3) ~3:1 DRAM-wafer-per-HBM-wafer trade; (4) NOVEL: more HBM per accelerator (80GB→"148GB"→288GB) = bits migrating OFF the commodity-DRAM tier = future DRAM demand loss; (5) flash offload squeezing DRAM from below (Chinese-lab thing); (6) LTAs timed to mask falling spot; (7) "SK timed the top with the ADR issuance"; (8) packaging hard past 8-Hi. Three Opus verification agents fired (Rule #16): A=mix-vs-price decomposition + call prints; B=bit-migration mechanism; C=LTA-mask + ADR-timing.

**NO POSITION ACTION — user-gated.**

---

## §2.2 Agent B — bit-migration mechanism (returned first, ~08:10Z)

**NET VERDICT: the post's direction is right but the mechanism is MISLABELED — HBM eats DRAM WAFERS, not DRAM BITS. "Less DRAM demand" is FALSE today and does not bind on any 2026-27 timeline.** Per-leg:

| Post leg | Verdict | Deciding datum |
|---|---|---|
| Accelerator HBM ladder | **PARTLY — "148GB" FALSE; escalator PAUSES** | B200 = **180 GB** official (NVIDIA datasheet T1; 192GB third-party); H200 141GB; **B300 was ALREADY 288GB in 2025 and R200 is also 288GB — flat GoG**; Rubin's leap is bandwidth 8→22 TB/s, not GB. Escalator resumes at **Rubin Ultra 1TB HBM4E 2H27** ([Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/nvidia-demonstrates-rubin-ultra-tray-worlds-1st-ai-gpu-with-1tb-of-hbm4e) T2); MI455X 432GB (corpus-confirmed) |
| 3:1 wafer ratio | **PARTLY / going stale** | ~3× per bit HBM3E vs DDR5, **rising ~4× for HBM4** (T2); nuance: HBM4 base dies move to TSMC N12/N3P LOGIC wafers — part of the cost lands outside DRAM fabs; TrendForce wafer-share÷bit-share implies ~2.4:1 (source tension flagged, not reconciled) |
| "Bits migrating off DRAM" | **FALSE as stated** | HBM bit share of DRAM: ~8% ('25) → ~9% ('26) → ~13% ('27); wafer-input share 18→22→30% ([TrendForce](https://www.trendforce.com/presscenter/news/20260602-13074.html) T2). Conventional DRAM bit demand +mid-30s% 2026 vs ~16% bit supply (T2) — demand OUTRUNNING supply, not shrinking. Venice 12→16 channels +33% DIMM slots holds (corpus 07-24). SOCAMM2/LPDDR rotation = still DRAM bits. **DDR5 64GB RDIMM out-earned HBM per wafer in 1Q26 (corpus U8)** — the crowd-out makes DRAM scarcer/dearer, the OPPOSITE sign for memory-maker revenue |
| "Hard past 8-Hi" | **STALE by ~2-3 years** | 12-Hi HBM3E volume since 2025; SKH 16-layer HBM4 (48GB) shown CES 2026, MP target 3Q26; NVIDIA soliciting 16-Hi for Q4-26 (T2). Ceiling is 16; hybrid bonding = the named bypass past that, deferred to HBM4E because TC-bonding reached 16-Hi (constraint = yield/economics, not physics) |
| Flash squeeze "from below, Chinese-lab thing" | **FALSE direction + FALSE attribution** | NVIDIA ICMSP/CMX standardizes NVMe tier-3 KV cache (GA 2H26), Samsung-NVIDIA CMX (07-20, corpus N=5), SanDisk/SKH HBF samples H2-26; zero observed DRAM demand reduction (T2); Micron sells 256GB SOCAMM2 *for* KV offload — the tier below HBM is being filled with MORE DRAM. **Corpus's 06-11 ADDITIVE booking stands unchanged** |

**Timeline read (agent model, 🟡):** the bit-migration bind is a **2029-30 earliest** scenario (3rd order P~30%: accelerator units plateau while per-unit HBM compounds); 4th-order tail (P~15%): HBF pin-compatibility displaces an HBM *stack* → relieves the wafer crowd-out → DRAM prices FALL — the inverse of the post's conclusion. **Routing decision: do NOT carry the post's bit-migration framing into TC-1; the corpus already holds the correct wafer-crowd-out version.** The 2029-30 joint-state scenario goes to the falsifier-watch ledger as a dated far-watch item, next to the existing 2028 disaggregated-inference HBM-substitution watch (TC-1).

*§2.1 (mix-vs-price, call prints) and §2.3 (LTA-mask/ADR-timing) pending agent returns.*

## §2.1 Agent A — mix-vs-price decomposition (returned ~08:25Z; full data in the wake artifact §2.5)

**The post's NEAR-TERM claims largely VERIFY — the company itself half-confirmed the mix story on the call:**
| Post claim | Verdict | Decider |
|---|---|---|
| Miss = mix story | **PARTLY TRUE** — company named BOTH mix (HBM/범용 구성) AND H2 shipment carry-over | 테크M T2 call quote |
| Mix-shift drags blended ASP | **PARTLY — mechanism right, direction sloppy**: HBM was UNDER-shipped in Q2 (pushed to H2); the drag is the STANDING HBM weight on annual contracts, not a Q2 HBM step-up | IR transcript T2 |
| HBM flat vs DRAM vertical | **TRUE and UNDERSTATED** — HBM contract prices DECLINING 2026 ($17-20→$13-17/GB; GS −28% YoY) vs commodity +93-98% then +58-63% QoQ | TrendForce 06-01/06-02 T2 |
| Earnings growth from DRAM not HBM | **TRUE at margin-per-wafer** — HBM profitability below DDR5 64GB RDIMM since 1Q26 (TrendForce); KB: DDR5 margin > HBM3E in 2026. Caveat: HBM still ≈40-55% of SKH DRAM revenue base (inferred band, my model — not disclosed) | TrendForce/KB T2 |
| Bad for SKH specifically | **TRUE** — TrendForce singles out SKH (highest HBM bit mix → constrained ASP); Samsung +93.4% vs SKH +62.5% QoQ 1Q26 | TrendForce 06-01 T2 |

**Joint verdict on the post (with §2.2):** near-term price/mix legs TRUE-to-understated; structural bit-migration leg MISLABELED (wafers not bits) and its factual scaffolding partly false/stale. The post's investable core survives as: **the 2026 pricing-power locus sits in commodity DRAM, and SKH's HBM mix is a relative-ASP headwind until HBM reprices in 2027** — which the corpus now carries with T2 backing. Its long-term conclusion (structural DRAM demand loss) does not survive.
*§2.3 (LTA-mask / ADR-timing) pending agent C.*
