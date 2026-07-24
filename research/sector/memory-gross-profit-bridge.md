# MEMORY GROSS-PROFIT BRIDGE — when does GM compression NOT mean the cycle is over? (BUILT 2026-07-10)

**Origin:** user question 2026-07-10 night — "what must be true for the reduction in gross margin to be offset by increase in unit prices, both for memory/HBM and for NAND? What model must you build?" Built same-session under the CLASS-1 grant (net-positive test: converts the GM-ceiling tracking variable from a binary top-signal into a mechanism-diagnostic — the difference between selling a real crack and selling an accounting artifact). Companion script: `meta/scripts/memory_gp_bridge.py` (all tables computed, #43b).

## The identity that forces the answer
GP dollars = Units × ASP × GM%, and GM = 1 − cost/ASP. These two equations mean **"GM falls but profit holds" can only happen via exactly two mechanisms**, and they are distinguishable in reported data:

### Lens 1 — the universal break-even (mechanism-agnostic)
GP flat ⟺ Revenue must grow by g1/g2 − 1 (computed):
| GM path | Revenue needed to hold GP flat |
|---|---|
| 88% → 80% | +9.4% |
| **88% → 70% (the Patel sequence)** | **+25.0%** |
| 90% → 70% | +28.6% |
| 90% → 60% | +50.0% |

### Lens 2 — PRICE-DRIVEN compression (unit cost ~constant) = the commodity crack
At constant cost, GM and ASP are rigidly linked (p = c/(1−g)), and the arithmetic is brutal (computed):
| GM path | Implied ASP | GP/unit | Units needed to offset |
|---|---|---|---|
| 88% → 80% | −37% | −43% | ×1.75 |
| **88% → 70%** | **−58%** | **−67%** | **×3.00** |
| 90% → 70% | −67% | −74% | ×3.86 |
**Verdict: at commodity cost structure the offset is essentially IMPOSSIBLE** — bit capacity grows 20-30%/yr (Patel, T2), nowhere near the 3x units required. A price-driven GM slide from ceiling to 70s takes gross profit down ~two-thirds. This is what "the cycle has not disappeared" means in dollars.

### Lens 3 — COST-DRIVEN compression (ASP RISES, cost rises faster) = the mix-shift artifact
When product mix walks up the complexity curve (HBM3e→HBM4→HBF-class; more stack, more packaging, worse early yields), GM% falls **while gross-profit dollars per unit grow** (computed):
| Start GM | ASP | Unit cost | Resulting GM | GP/unit |
|---|---|---|---|---|
| 60% | +40% | +60% | 54.3% (falls) | **+26.7%** |
| 60% | +30% | +50% | 53.8% (falls) | +16.7% |
| 75% | +25% | +60% | 68.0% (falls) | +13.3% |
| 70% | +50% | +80% | 64.0% (falls) | **+37.1%** |
**Verdict: this is the ONLY benign path** — GM% compresses as an accounting artifact of selling costlier, higher-ASP product, while the dollars grow.

## So: WHAT MUST BE TRUE (the answer, three conditions, all falsifiable per print)
1. **The GM decline must be COST-DRIVEN, not PRICE-DRIVEN** — i.e., ASP must be RISING through the compression (mix walking to HBM4/HBF/enterprise-QLC), with the cost line rising faster. Sign test: GM↓ + ASP↑ = artifact (hold); GM↓ + ASP↓ = crack (Lens 2 math applies, and no realistic unit growth saves it).
2. **Demand must stay price-INELASTIC at the paying tier** — the AI tier absorbing ASP increases (funding-node: AI tier pays while consumer tier exits/substitutes). The moment the marginal AI buyer balks (order cuts, LPDDR-halving-style engineering-out AT THE HIGH END), condition 1's ASP↑ leg dies.
3. **Supply discipline must hold through the compression** — LTA-priced share high enough that spot cracks don't transmit (SNDK: >1/3 FY27 bits under multi-year agreements; SKH/Micron LTA structures), and no bypass at volume (HBF is ITSELF the mix-up product for NAND — the bypass and the offset are the same object on the NAND side; CXMT capacity 2027-28 is the condition-3 falsifier direction).

**Per-tier read (current state, research-verified 2026-07-10):**
- **HBM/DRAM (SKH/Micron/Samsung):** conditions 1-2 currently SATISFIABLE — HBM4 generational ASP steps exist, AI-tier inelasticity evidenced; condition 3 = LTA share + CXMT watch. The offset window is real but generation-gated: it lasts as long as each new HBM generation lands a big-enough ASP step.
- **Commodity DRAM:** Lens 2 applies almost purely — no offset; this is where the Patel halving hits hardest.
- **NAND (SNDK/Kioxia):** structurally better cost-down (layer scaling) but LOWER starting GM; the offset path runs through HBF (new high-ASP tier, sampling-stage) + enterprise QLC mix + LTA-fication ($42B SNDK backlog). The offset is REAL but arrives 2027+, which is exactly why the SNDK NO-now view stands — the mix-up product isn't shipping in volume yet while the commodity leg sits at its ceiling.

## The model to run at each print (the deliverable)
**Per-maker GP-bridge decomposition** at every memory print (SKH late-Jul, SNDK Aug-5, MU next guide, Samsung prelim): decompose ΔGP into Δunits × ΔASP × ΔGM (script `bridge()` function), then apply the SIGN TEST (GM vs ASP direction) → classify the quarter as ARTIFACT-COMPRESSION (hold) vs CRACK-COMPRESSION (falsifier-relevant). Feed: company prints (T1), TrendForce contract series (T2), HBM-mix disclosures. **This upgrades the TC-1 GM-ceiling marker: the marker now fires with a MECHANISM tag, not just a level.** Book linkage: the Units line of the bridge IS SUMCO's demand line (bits→wafers) — a crack-compression quarter with units still growing = the LTA-insulation thesis confirmed; units falling = L-series falsifier territory.

**Fluidity metadata:** built 2026-07-10; falsifier — if two consecutive memory prints are classified and the classification changes no decision (marker fires identically with or without the mechanism tag), the bridge is decorative → fold back into the TC-1 TV. Re-eval 2026-09-10.
