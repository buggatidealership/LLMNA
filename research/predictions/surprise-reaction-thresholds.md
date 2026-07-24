# SURPRISE→REACTION THRESHOLDS (v1, fitted 2026-07-15 EVE; user-commissioned)

**What it answers:** how far above street a print's guidance/bookings must land for a reliable positive / strong pop. Output-side complement to `blowout-probability-screen-spec.md` (screen predicts surprise; this prices it).
**Data:** `surprise-reaction-panel.csv` — 32 rows used (agent-assembled T2 press panel, 27 clean + house-seed T1 points; AEHR date corrected to 07-14 per house 8-K vs panel's 07-07). AI-infra cohort, Q3-2025→Jul-2026.

## THE THRESHOLDS (guidance-surprise rows, N=15, logistic fit — INDICATIVE, N-limited)

| Outcome | 50% probability at | 80% probability at |
|---|---|---|
| Positive T+1 reaction | guide **≈ +6.5%** above street | **≈ +10.4%** |
| Strong pop (≥ +8%) | **≈ +13.8%** | **≈ +21.3%** |

Bucket confirmation (no model needed): 0–3% → 1/4 positive · 3–8% → 1/5 positive (mean −2.2%) · **8–20% → 4/4 positive** · >20% → 2/2 strong (mean +18.5%).

## THE FOUR REGIMES (my model, panel-derived)

1. **SELL-THE-NEWS ZONE (<+5% surprise, run-up name): NEGATIVE is the MODAL outcome — 10 of 14 sub-+5% beats fell** (NVDA ×3 beat-and-raise all fell; AMD, MU-Sep, ANET, AMAT, Camtek, AVGO-Dec, Samsung-prelim). In this regime the street bar is a floor the price already stands on.
2. **PAY ZONE (+8% to +20%):** 4/4 positive, mean +6.6% — the reliable-positive region starts ≈ +8–10%.
3. **STRONG-POP ZONE (>+20%):** both instances strong (MU Dec +32→+11; AEHR +64→+26); pay-rate ~0.2–0.4× of surprise.
4. **MISS ZONE:** mean −17.6% on N=2 (IBM −3%→−25.2; SMCI −16%→−10) — downside asymmetry ~6–8×. The distribution is not symmetric; it is a cliff on one side and a ramp on the other.

**Override variable — BOOKINGS/BACKLOG:** when a bookings surprise >+100% prints, it dominates the guide number (ASML Jan: bookings +108% carried a +4% guide to +5%; AEHR: +500% bookings amplified everything). Bookings surprise is the highest-torque single disclosure in the panel — and most cohort names don't disclose it, which is WHY it torques when it appears.

## Caveats (binding)
N=15 guidance rows; several T+1 figures are AH/PM proxies; reactions NOT excess-adjusted vs SOXX (tape-day contamination possible); run-flags qualitative and near-uniformly "up" (regime artifact — the down-run cell is unpopulated); two rows measure vs-prior-guide not vs-street (Advantest, ASML-Jul). **REBUILD clean on the API layer** (close-to-close, SOXX-excess, point-in-time consensus) — the fitted crossings may move ±3-5pts.

## Falsifier / out-of-sample test (pre-registered)
Every print on the house calendar Jul-21→Aug-19 (NOC, IBM-full, SKHY, EMC, NET, MURATA, Kioxia, ALAB, SNDK, Nittobo, IFX, SUMCO, SoftBank, ENR, NBIS, Mitsui, TUC, CRCL, ACMR, GigaDevice) is an out-of-sample test row: log surprise + T+1, grade the fitted crossings. If the 8-20% bucket's 4/4-positive breaks below 60% hit-rate on ≥10 new rows, refit; if the sell-the-news zone stops being modal, the regime changed — re-anchor before trusting either.


## v1.1 ADDENDUM (2026-07-15 EVE, user variable-extension: "market cap, how well known, analyst coverage, options — there might be even more")

**SIZE-CLASS STRATIFICATION (computed on the panel, positive-surprise rows >3%; cap classes coarse/recall-based-flagged):**

| Class | N | mean surprise | mean reaction | pay-rate | % positive |
|---|---|---|---|---|---|
| MEGA (>$200B class) | 11 | +11.1% | **+0.6%** | −0.12 | **45%** |
| MID | 9 | +13.2% | +6.9% | +0.80 | 100% |
| SMALL (<$15B class) | 2 | +39.0% | +19.2% | +0.65 | 100% |

**Finding: size class dominates surprise size in this panel.** The v1 blended crossings are misleading per-class: for MEGAS the crossings are far too low (NVDA guide +7.4% → −5.0%; the entire NVDA/AMD/MU-Sep sell-the-news cluster is mega); for MID/SMALL too high (mid-caps paid from ~+3-5%). MECHANISM (my model): coverage/pre-pricing density — 40-60 analysts + dense options OI + index flows mean the reported surprise-vs-street is not a surprise to the marginal price-setter; in thinner names reported surprise ≈ true surprise. The AEHR pop was as much a COVERAGE-VACUUM effect as a magnitude effect — exactly the user's point.

**CLASS-CONDITIONAL WORKING RULES (v1.1, indicative):** MEGA: reliable pop needs bookings-override disclosure or >+20-30% surprise; sub-+10% beats = sell-the-news modal. MID: pay zone starts ~+3-5%; the v1 +8-20% bucket read is mid-cap-driven. SMALL: pays large but B39 entry-priced and volatile; N=2 only.

**FULL VARIABLE ROSTER for v2 (stratify-don't-regress at N=32; multivariate only on the API-era rebuild, target N=150-300 = cohort × 8-12 quarters):**
1. Surprise %, type-separated (guide / bookings / actuals) — v1 core
2. Size class / liquidity (TESTED above — strongest)
3. Coverage density: analyst count + ESTIMATE DISPERSION (tight consensus = pre-priced bar; wide dispersion = market doesn't know → more reaction per unit surprise)
4. Positioning: run-into-print, short interest, options-implied move (the priced bar)
5. Options structure: OI/gamma at print (dealer hedging amplifies small-cap moves, dampens or accelerates mega moves)
6. Index/passive/product share (live house example: SKHY +27.29% amplified by leveraged single-stock ETF LAUNCHES, on file 07-15 wake artifact)
7. Disclosure structure: bookings/backlog discloser or not (v1 override variable — interacts with #3: undisclosable metrics cannot be pre-priced)
8. Retail attention / how-well-known (user variable; proxy: social volume, retail flow share)
9. Name-specific reaction beta (prior-print reaction history)
10. Calendar congestion (same-day cohort prints — house Aug-5-7 cluster = shared attention denominator)
Unifying frame (my model): variables 2-10 all proxy ONE latent quantity — EXPECTATIONS EFFICIENCY: how much of the reported surprise the marginal price-setter already knew. v2's real spec: reaction = f(true surprise) where true surprise = reported surprise × (1 − expectations efficiency).

Falsifier addendum: out-of-sample grading (Jul-21→Aug-19 calendar) now logs size class per row; if MEGA rows pop on sub-+10% surprises repeatedly, the stratification read is wrong — refit.

## v1.1 INTERPRETIVE NOTE — the size-class variables ARE attention metrics (user-relayed thesis, 2026-07-16 EVE)
User-relayed Twitter frame: *"'Chip stocks will have a lot of earnings' is not a good bull case… The only bull case is continued attention, or a bear case lack thereof."* Adjudication against this panel's own data: HALF-CONFIRMED. The v2 variable roster (mcap, analyst count, options availability, "how well known" — user-commissioned 07-15) is attention quantified; the panel's core stratification result (MEGA pay-rate ≈ 0 vs mid/small +0.80) is what attention SATURATION does to expectations efficiency. Where the frame overreaches (dissent, on file in chat 07-16): horizon conflation (6-24mo: buybacks make earnings their own buyer; attention times the move, fundamentals gate it), attention treated as exogenous (prints GENERATE attention — the event-anchor premise), and the bear symmetry (attention+leverage = the KR ₩62.76T stock, where attention exit = −15% days → falsifier discipline, not attention-chasing). OPERATIONAL RESTATEMENT: bull case = fundamentals-vs-bar × attention structure; the alpha cell (under-attention mid/smalls with inflecting fundamentals — CCL cluster live specimen: EMC June rev +120.7% YoY vs TUC −9.8% same-day tape, 07-16) is this thesis implemented with falsifiers. No new instrument needed; v2 roster naming updated: size-class axis = ATTENTION CLASS.
