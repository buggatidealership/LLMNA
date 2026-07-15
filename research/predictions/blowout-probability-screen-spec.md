# BLOWOUT-PROBABILITY SCREEN — input spec (user-commissioned 2026-07-15 EVE: "state what inputs you would need fed to decide which book/watchlist names have the highest probability of blowout guidance, earnings, and profit")

**Loss function (declared at spec time, per the hindsight-gate):** P(blowout) per name = joint P over (i) rev/OP print materially above consensus, (ii) profit/margin above consensus, (iii) guide RAISED above consensus-embedded expectations. Pre-registered per name per component with bands; graded at each print; feeds the edge-vs-consensus ledger metric (2026-07-15 standing rule).

## Inputs REQUIRED (the bar side — mostly NOT on file)

| # | Input | Discriminating power | Source path |
|---|---|---|---|
| 1 | Consensus snapshots (rev/OP/EPS, Q + FY) per name | defines "blowout"; ASML grade showed cost of a soft bar | agents (aggregator, lossy) / **user screenshots: FnGuide (KR), QUICK-Toyo (JP)** — article-pull pattern extended to data |
| 2 | Consensus REVISION trajectory (30/60/90d momentum) | THE discriminator — stale bar vs chasing bar | **Finnhub estimates endpoint post-key-rotation** (US); KR/JP user screenshots |
| 3 | Standing company guidance per name | the anchor to be raised FROM; guide set pre-price-move = coiled spring | agents, self-serve |
| 4 | Positioning: short interest, options-implied move (US), KR foreign flows, run-into-print | grades what's priced (B39/B45) | API layer (US) / KR-native agents / computable from tracked closes |
| 5 | Monthly revenue prints (TW early-Aug; TSMC monthlies) | highest-frequency hard revenue | agents, partially flowing |
| 6 | Daily channel pricing (DRAM/NAND spot, MLCC lead times) | engine at finer resolution than quarterly surveys | paywalled — trade-press proxy / user data-subscription decision |

## ON FILE already (engine side)

TrendForce Q3 survey (DRAM +13-18%/NAND +10-15%) · Q2 contract +58-63% (SKHY branch data) · Nanya Q2 actuals GM 79.5% (earliest TW DRAM tell) · GigaDevice profit-alert · Samsung prelim OP ₩89.4tn record · MU print + 16 take-or-pay SCAs · Murata MLCC hikes live Jul-1 · SUMCO wafer-hike thesis + 07-15 tightness tape · ASML FY raise €43-45B · IBM letter (enterprise demand + magnitude-surprise admission) · KIS ₩60.4tn vs SemiAnalysis ₩67.6-72.2tn GP branches (SKHY = an already-formed blowout question) · calendar peer-print chain (TSMC → NOC → EMC → SKHY → MURATA → SNDK/Nittobo/IFX → SUMCO...).

## Computation (once inputs 1-3 land, minimum viable)

Per name: **surprise-torque** (verified price×mix×volume deltas vs consensus-embedded) × **bar-staleness** (inverse revision momentum) × **guide-anchoring** (guide vintage vs price-move dates) × **smoothing-discount** (LTA/take-or-pay compresses surprise variance both ways — TC-18). Rank → pre-register P(blowout) bands per component → LOCK BEFORE JUL-29 (calendar density rule). Recompute at each peer print (Bayesian chain).

## Refusal note
No ranking is issued on engine data alone — surprise-torque without a bar is uncomputed narrative (the failure class the 07-15 edge-vs-consensus 0-for-2 documented). Fastest unlock: browser session (Finnhub rotation → inputs 2+4 US self-serve) + two user screenshot batches (FnGuide KR / QUICK JP).

## Fluidity metadata
Spec'd 2026-07-15. Falsifier: if the screen's pre-registered P(blowout) rankings show no positive edge vs consensus-implied surprise over the Jul-29→Aug-14 wave (≥6 graded prints), the screen is decoration — retire or redesign at the Aug monthly audit.
