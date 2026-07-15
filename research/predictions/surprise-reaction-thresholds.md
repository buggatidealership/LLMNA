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
