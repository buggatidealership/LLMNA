# MARKET-STATE FUNCTION — design spec v0.1 [CANDIDATE, not yet built]

**Created:** 2026-07-08 (user design question: "what must be true to create a holistic LLM-native analysis of the overall markets — what variables must be tracked")
**Trigger context:** SKH ADR oversubscribed (primary-market demand) vs deteriorating secondary tape — a signed divergence the harness currently reads ad-hoc, per-event, not systematically.
**Status:** P1 ACTIVE (2026-07-08) — USER DECISION: HYBRID sourcing ("use scrappable sources and keep sharing screenshots"). Constraint discovered same day: environment network policy blocks BOTH Bash-curl AND main-session WebFetch to data hosts (stooq/FRED/frankfurter all proxy-403); research agents' web tools DO reach cnyes/tradingeconomics/kabutan/bloomingbit-class sources. Working shape: (1) templated PULL-AGENT with fixed roster (US wrap + tradingeconomics yields/DXY/oil + cnyes TW + bloomingbit KR + kabutan JP) returning strict CSV → (2) `meta/market-state-compute.py` → (3) `sector/market-state-log.md` entry. Cost ~15-25k tokens/refresh. **UPGRADE PATH (user-side, ~2 min): widen the environment's network access (claude.ai environment settings → network policy → add stooq.com, fred.stlouisfed.org, api.frankfurter.app) → Tier-A becomes a pure script at zero token cost.** First vector computed 2026-07-08 (seed run, mixed-session inputs — see log).
**Scope guard:** the mission excludes macro TRADES. This function is a CONDITIONING layer — it feeds the cash-deployment gate, entry-package timing, and sizing modifiers for AI-sector decisions. It never generates its own positions.

## 1. The LLM-native design principles (what makes this NOT a human macro note)

1. **COMPUTED, not narrated (#43b):** the state vector is arithmetic on pulled data — dispersion, correlations, deltas — executed in python, never eyeballed. Prose only interprets computed output.
2. **JOINT-STATE, not sequential:** all dimensions in ONE matrix per refresh. The signal is CROSS-DIMENSION DIVERGENCE, not any single level. Today's worked example: memory rout + CCL green + energy green + ADR book oversubscribed = a rotation/dispersion signature that "market down" hides entirely.
3. **REGIME-CLASSIFIED with P-weights + pre-registered flips:** at each refresh the function outputs P-weights over a fixed regime taxonomy (see §3) with the flip conditions written BEFORE the regime is needed — else it degrades to daily narration.
4. **DISPERSION > LEVEL:** breadth, cross-cohort spread, and correlation-regime changes carry the information; index levels are one input among many (B45 keeps magnitude reads honest).
5. **DIVERGENCE LEDGER:** every signed divergence (e.g., primary-demand vs secondary-tape; fundamental-beat vs price-reaction = L27; structural-bid vs cohort-beta = today's CCL) gets logged with its historical resolution pattern — the accumulating N is the calibration.

## 2. The variable set (tiered by computability)

| Tier | Variables | Cadence | Source state |
|---|---|---|---|
| A. TAPE (computable, THE BLOCKER) | Held + watchlist + canary-basket closes; cross-cohort day-spreads (semis / software / materials-scarcity / energy / memory); breadth; rolling pairwise correlations; volume anomalies | daily EOD | ⚠️ NO reliable programmatic feed — T1 tape 403-blocked repeatedly (NBIS, Samsung, Naver, Yahoo); current method = user screenshots + per-event agents |
| B. RATES/FX/CMDTY | US 10Y/30Y, Fed-odds, DXY, USDJPY, USDKRW (FX-sensitivity todo 2026-07-01), Brent (Iran gate) | daily | partially agent-pulled today, ad hoc |
| C. CREDIT/FUNDING | the funding-shock node's 5-signal set (neocloud HY spreads/converts, failed raises, hyperscaler capex GUIDES, private-credit markdowns, GPU rental <$1.50/hr) | weekly + event | node built 07-04; signals watched manually |
| D. POSITIONING/SENTIMENT | short interest + options implied moves (already in the NOW ~Jul-20 re-pull), KR/TW/JP foreign flows (외국인/外資), whisper-vs-consensus gaps (B42), primary-market demand reads (ADR books, IPO oversubscription — the SKH example) | per-event → weekly | ad hoc per decision package |
| E. EARNINGS REGIME | L27 counter state; computed beat→reaction spread per cohort print (the treadmill METRIC: reaction% ÷ beat% per event, aggregated across the season) | per print | L27 manual; the ratio is never computed — compute-layer build item |
| F. POLICY/GEO | model-export-control state (read #11), tariff/sanction events, Iran state | event-driven, narrated | banner-based today |
| G. LIQUIDITY/CALENDAR | IPO/ADR calendar, index adds/deletes, expiries, prints | weekly | INDEX.md catalyst calendar exists |

## 3. Regime taxonomy v0 (P-weighted at each refresh; flips pre-registered at adoption)
R1 risk-on broad / R2 AI-complex-specific derisk (07-07's verified state) / R3 broad geopolitical risk-off (explicitly NOT 07-07 — Dow −0.25%) / R4 intra-AI rotation (growth→scarcity variant now live via CCL) / R5 whisper-treadmill earnings regime (L27 2/2 would confirm) / R6 credit-transmission stress (funding-node signals) / R7 melt-up (B45 tail). Weights sum to 1; multiple can be elevated (R2+R5 is today's read, my model).

## 4. WHAT MUST BE TRUE (the user's question, answered precisely)

1. **A machine-readable market-data source.** The single hard blocker. Options: (a) user provisions an API key (any mainstream market-data free tier covers Tier-A); (b) accept ~1 Opus agent/day scraping T2 aggregators (~15-20k tokens/day, degrades #43b purity); (c) hybrid — user screenshots remain canonical for holdings, agent pulls for cohort. DECISION NEEDED (user).
2. **The compute layer exists** — the overdue P2 build (calibration curve, ledger-stats, etc.) extended with: dispersion/correlation script, beat→reaction ratio script, divergence-ledger appender. The state vector is ~200 lines of python once data flows.
3. **Routine execution works** (the E6 saga) — the function's value is DAILY refresh without me in the loop; the EOD wake is its natural home. Currently execution 0/5.
4. **The regime taxonomy + flip conditions are pre-registered** (this file, §3 — done at v0).
5. **A cascade contract:** the state artifact feeds the existing gates (cash-deployment, entry-package timing checkpoints, sizing modifiers) — never trades of its own.

## 5. Build phases
P0 (this commit): spec. P1: data-source decision (user) + Tier-A script against whatever source is chosen; first computed state vector, manually triggered. P2: wire into the EOD wake once routines execute; divergence ledger born. P3: 30-day calibration — do regime P-weights predict anything (graded vs realized next-5-day cohort behavior)? Kill condition: if after 30 refreshes the regime calls are pure narration (no graded predictive content vs just reading the day's headlines), retire to a lighter dashboard.
