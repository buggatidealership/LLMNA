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

## §2.3 Agent C — LTA-mask + ADR-timing (returned ~09:25Z)

**CLAIM 6 ("LTAs timed to mask falling spot") — FALSE on the premise, PARTLY on the mechanism.** DRAM spot is NOT falling: DDR4 8Gb 1Gx8 $35.90 (06-09) → **$42.041 (07-29, session −0.09%) = +17.1% over 7 weeks**; DDR5 16Gb flat at $50.933 ([TrendForce live spot](https://www.trendforce.com/price/dram/dram_spot) T1-vendor). The only falling tier is **512Gb TLC NAND wafer −8.3% over 6 weeks** ($20.638 → $18.931) — the Mirae PT cut is on prospective NAND *contract*, not observed DRAM weakness. 3Q contract guides still RISING (+13-18% DRAM / +10-15% NAND). LTA share ≈50% of revenue (Mirae 🟡 estimate). **The dominant sell-side read is the OPPOSITE of the post: brokers are cutting numbers BECAUSE of LTAs** (한투 −9%/−11% OP to realize LTA price assumptions; 삼성증권: "pre-pay the premium in the boom to collect the downturn insurance" — caps peak-cycle upside; JPM: non-LTA volume keeps repricing up). ⚠️ Unresolved contradiction flagged: 녹색경제 T2/T3 "SKH is the only maker with NO price ceiling in its LTA" (Micron took ceiling+floor) vs the caps-upside broker read — not resolvable open-source today; management language is floor-flavoured ("하방 안정성"). **New pre-registered spot falsifier watches: DDR4 8Gb <$40 (first genuine DRAM spot rollover) · 512Gb TLC <$17 · 4Q26 DRAM contract guide ≤0%. None fired.**

**CLAIM 7 ("timed the top with the ADR issuance") — PARTLY TRUE, framing MATERIALLY MISLEADING (T1 F-1/A decides):**
1. **Nobody monetized.** 100% PRIMARY issuance — "We are offering... our issuance and sale," net ~$28.0B ([F-1/A 07-06](https://www.sec.gov/Archives/edgar/data/2120882/000119312526295501/d32785df1a.htm) T1); **zero selling shareholders, SK Square sold nothing**.
2. **Size had no degrees of freedom:** 17.79M shares = SK Square 20.50% → **exactly 20.00%**, the Monopoly Regulation and Fair Trade Act floor (T1; computed 146.1M/730,492,365).
3. **Not priced at the top:** board resolution + F-1 06-24 (+2d from the 06-22 peak — an SEC-review-clock artifact of a process running since the Dec-2025 조회공시 and a March confidential F-1 🟡); **priced $149 on 07-09 = 17 days and −25.1% AFTER the peak**, at −5.8% vs the 07-03 reference.
4. **The issuance arguably CAUSED part of the local decline it's credited with dodging** (2nd order, P~60%, agent's model — inferred): ADR premium ~16% → foreigners net-sold local SKH ₩1.718T (07-10) + ₩1.447T (07-13) rotating into the dollar line.
5. **Defensible residue:** treasury banked $26.5B at ~₩2.08M-equivalent vs ₩1,401,000 today — value-ACCRETIVE to holders; "good luck plus a legal cap, not a market call."

**Vendor-defect N+1 (logged to data-access):** EODHD's same-day EOD row for KS11 (5,538.15) disagreed with its own real-time print (5,663.24) and press — the EOD row was MID-UPDATE. Standing rule extension: never read a SAME-DAY EOD row; real-time (computed vs verified prior close) until T+1.

## §3 INTAKE SYNTHESIS — the post fully adjudicated (9 claims, 3 agents, ~327k subagent tokens computed from usage 85,523+117,572+123,979)

| Post claim | Final verdict |
|---|---|
| Miss = mix story | PARTLY TRUE (mix + H2 carry-over, company-named) |
| HBM flat vs DRAM vertical | TRUE, understated (HBM DECLINING 2026) |
| Earnings growth from commodity DRAM | TRUE at margin-per-wafer (since 1Q26) |
| SKH-specific disadvantage | TRUE (TrendForce singles SKH out) |
| 3:1 wafer trade | PARTLY (→~4:1 HBM4; base dies moving to TSMC logic wafers) |
| Bits migrating off DRAM | **FALSE** (wafers, not bits; bit demand +mid-30s% vs +16% supply) |
| Flash squeeze, Chinese-lab | FALSE ×2 (NVIDIA-standardized; additive) |
| Hard past 8-Hi | STALE (16-Hi sampling) |
| LTAs mask falling spot | FALSE premise (DRAM spot +17% 7wk); sell-side treats LTAs as upside caps |
| ADR timed the top | MISLEADING (100% primary, law-capped size, priced −25% post-peak; nobody monetized) |

**What the corpus keeps:** the 2026-headwind/2027-tailwind HBM repricing inversion (the post's true core, now T2-backed); three new pre-registered spot falsifier watches; the LTA ceiling-vs-floor unresolved contradiction (adjudication target: the quarterly report's contract disclosures); the ADR-issuance-as-flow-driver mechanism for the July KR decomposition; the far-watch 2029-30 bit-migration joint-state scenario. **What it discards:** bit-migration as a current mechanism, the flash-squeeze, the top-timing narrative. **NO POSITION ACTION — user-gated.**
