# HBM vs commodity DRAM — operator primer (written 2026-07-30 on direct request)

**Q&A / primer file. All figures research-verified 2026-07-29/30 (T1 DART filing + T2 TrendForce/call transcripts), cross-referenced to `signals/cross-source-log/2026-07-30-thu-earnings-reward-function-map.md`.**

## The plain-language difference
- **DRAM** = the generic working memory in every computer. A commodity, sold by the bit, **repriced QUARTERLY** on contract.
- **HBM (High Bandwidth Memory)** = DRAM dies stacked vertically, bonded, and placed immediately beside the processor. It exists because AI accelerators are starved for **bandwidth, not compute** — the binding constraint is feeding the chip fast enough. HBM solves feeding via many stacked dies with very wide interconnect. Premium tier, **sold on ANNUAL FIXED contracts.**

## The contract-basis difference IS the 2026 story
| | Commodity DRAM | HBM |
|---|---|---|
| Repricing cadence | **Quarterly** | **Annual, fixed** |
| 2026 price path | +93-98% (1Q) then +58-63% QoQ (2Q), +13-18% guided 3Q | **DECLINING** ($17-20 → $13-17/GB; GS −28% YoY) |
| Wafer area per GB | 1× | **~3×**, rising to ~4× for HBM4 |
| Profitability per wafer | **HIGHER since 1Q26** (DDR5 64GB RDIMM) | Lower |

**The counterintuitive conclusion: HBM is the strategic prize; commodity DRAM is where the 2026 money is.** SK Hynix carries the highest HBM bit-mix of the three suppliers, so its blended DRAM ASP rose only **~+30% QoQ** while commodity contracts rose **+58-63%** — its best product was locked into contracts signed before the spike. **Its leadership was a 2026 relative-ASP headwind.** The bull case is the 2027 contract reset, which the company confirmed on its 07-29 call is an **IN-PROGRESS, UNRESOLVED negotiation** — not a booked fact.

## Bypass routes off the HBM bottleneck (Rule #9 — required, not optional)
1. **Substitution DOWN the stack (live):** NVIDIA-standardized NVMe KV-cache tiering + SanDisk/SK Hynix HBF samples H2-26. Corpus verification says this is **ADDITIVE, not subtractive** — Micron sells 256GB SOCAMM2 *for* KV offload, i.e. the tier below HBM gets filled with MORE DRAM. **No effective bypass at the HBM tier on a 2026-27 horizon.**
2. **Second-source / qualification (asymmetric):** CXMT is a real bypass for **commodity** tiers and **blocked at the premium tier** — Jefferies: "its lower tech does not allow it to meet US AI demand" (98% commodity DRAM, zero HBM). Non-consensus beneficiary of that asymmetry: whoever sells the commodity tier the Chinese entrant *can* pressure is exposed; whoever sells the premium tier it cannot reach is insulated.
3. **Packaging ceiling → hybrid bonding:** the old "hard past 8-Hi" claim is stale — 12-Hi shipped since 2025, 16-Hi HBM4 sampling (SKH CES-2026, MP target 3Q26). Hybrid bonding is the named bypass past 16-Hi, **deferred** to HBM4E because TC-bonding/MR-MUF reached 16-Hi — so the current constraint is **yield/economics, not physics**. Non-consensus beneficiaries: the bonding/test layer (Advantest +10.85%, FormFactor +10.43% on 07-30, both memory-led).
4. **Demand-side bypass (being exercised NOW):** buyers who cannot pay simply exit. **Samsung's own mobile division took a KRW 700bn first-ever loss rather than absorb its semiconductor arm's prices**; PC OEMs raised prices 15-20%; the 3Q contract deceleration to +13-18% is driven by **consumer OEMs, not AI buyers**. The bypass at the consumer tier is demand destruction, and it is already visible.
5. **Contract-structure bypass (the one buyers actually chose):** Samsung committed **60-70% of capacity to multi-year contracts**; SK Hynix signed ~10 customers to 5-year deals with deposits. Buyers are routing around **price volatility**, not around supply — trading volume certainty for ASP stability, which locks high prices IN rather than defeating them.
