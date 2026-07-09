# 2026-07-09 — SKH ADR FINAL PRICING — divergence-ledger entry #1 GRADE (PROVISIONAL-FINAL)

**Resolution (T2, Reuters via source + TradingKey, 2026-07-09 US-midday):** final price **$149/ADR**, raise **~$26.5bn** — second-largest (or by some counts largest) foreign US listing. Books 7× oversubscribed (~$171.5bn orders, T2 Bloomberg/KoreaJoongAng). SKHYV interim trading Jul-10, regular Jul-13, settlement Jul-14/15. **PROVISIONAL-FINAL tag: "to price at $149, source says" — single-source pre-announcement; confirm against official filing at next wake.**

## VERDICT: **HIT** (the pre-registered second-cut tell fired) — with a mechanism refinement worth more than the binary
Computed deltas (FX 1,504 KRW/USD implied from KoreaJoongAng's own pair; script-run this artifact's commit):
| Comparison | Delta |
|---|---|
| Final ($149) vs Jul-9 re-reference (₩255,500/ADR ≈ $166) | **−12.3% KRW / −10.2% USD = THE SECOND CUT — HIT** |
| Final vs Jul-6 filing reference (₩242,500) | −7.6% |
| Final vs Jul-8 KR close (₩2,076,000) | **+8.0% PREMIUM** |
| Raise $26.5bn vs adjusted ₩43.14tn (~$28.7bn) | −7.6% |
| Raise vs KR-press spot-frame ($24.5bn) | **+8.2% ABOVE** |

**Mechanism read (the actual lesson):** the cut happened AND demand mattered — both, cleanly quantified. Pricing landed ~8% ABOVE the Jul-8 close (7× book pulled it above the mechanical spot-anchor) but ~10-12% BELOW the reference (the KR-spot anchor still binds ADR pricing; a rallying local market drags the ADR reference down with it, demand notwithstanding). **First divergence-ledger datapoint: ADR pricing = spot-anchored with a demand premium on top — neither pure mechanics nor pure bookbuild.** For future cross-listing events: model final price as spot × (1 + demand premium), NOT reference × (1 − cut).

## GRADE discipline notes (3-layer, honest)
- **INPUT:** the morning's 17-23% gap figure was computed off a mislabeled close (Leg A date-shift, caught + corrected to ~12.8% intra-day) — INPUT error caught BEFORE grade time by the verification loop; final actual gap-to-reference −12.3% ≈ the corrected estimate. The correction loop worked.
- **REASONING:** tell fired as pre-registered. **Flag: the pre-registration was BINARY (watch for second cut) with NO locked probability** — ungradeable for calibration purposes. LESSON: divergence-ledger entries must carry a pre-committed P at registration (goes to lessons at next audit; first calibration-ledger row logged with claimed_p=NA as the worked example of the gap).
- **Closes conflict:** RESOLVED direction confirmed again (KoreaJoongAng: "Wednesday closing price 2.08m won" = Jul-8). Jul-9 KR FINAL closes STILL unpinned → tomorrow's good-morning catch-up sweep.

Sources: investing.com/news/stock-market-news/sk-hynix-us-listing-more-than-seven-times-oversubscribed-source-says-4782931 (Reuters $149) · tradingkey.com/analysis/stocks/us-stocks/262020544 ($149/$26.5bn + UBS arb note) · koreajoongangdaily.com/business/sk-hynix-adr-draws-sevenfold-demand... · koreajoongangdaily.com/.../12764927 ($24.5bn spot-frame) · fnnews.com/news/202607090819162372 (KR schedule: SKHYV Jul-10 interim/Jul-13 regular/Jul-14-15 settlement) · seoul.co.kr/news/economy/2026/07/09/20260709500019
