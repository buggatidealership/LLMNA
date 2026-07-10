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

## 2026-07-10 EVE CHECK-IN (1 Opus verifier, native-KR parallel) — 3 corrections booked, grade UNAFFECTED
**Grade status: CONFIRMED-FINAL stands** — $149.00 × 177.9M = $26,507,100,000 recomputed ✓; strengthen the record framing: **largest-ever foreign US IPO** (surpasses Alibaba ~$25bn; Bloomberg: 3rd-largest share offering ever). Nasdaq Global Select. Book ~7x oversubscribed (~$171.5bn); cornerstones Baillie Gifford / Coatue / Situational Awareness indicated up to $7bn → **scaled back to ~$5bn** (Bloomberg Jul-10) — demand headline real but allocation-constrained.
**CORRECTIONS (cascaded to day-state same commit):**
1. **When-issued timing:** SKHYV began trading **FRIDAY Jul-10** (SEC 424B4 T1: WI Jul-10 under SKHYV, regular Jul-13 under SKHY) — the carried "$158 Thursday indication" was PREMATURE: no WI existed Thursday; "$158" = grey-market/UBS-premium-trade indication at best, NOT a tape print. Friday's actual SKHYV close: UNVERIFIED (quote pages 403) — treat the premium as UNKNOWN until a real print is captured Monday.
2. **ADS ratio (T1 prospectus + 전자신문/뉴스1 native): 1 ADS = 0.1 ordinary (10 ADS per share).** Parity math (computed): $149 × 10 = $1,490/share × FX ~1,504 = ₩2,240,960 → **pricing premium vs ordinary +2.5-2.9%** (vs Thu ₩2,186,000 / Fri ₩2,180,000; reconciles the reported ~2.9%). Denominator disambiguation: "$158 = +6.1%" is vs the $149 IPO price; vs the ORDINARY a $158 print would be **~+9.0% premium** — different denominators, never conflate.
3. **Seoul Jul-10 close: ₩2,180,000 −0.27%** (뉴스핌 T1-adjacent) — the carried "~₩2,274,000 +4.02%" was an INTRADAY HIGH that fully retraced (pre-listing profit-taking; KOSPI itself rallied on ADR sentiment). Data-gap "SKH Jul-10 close" now CLOSED with the corrected value. FX Jul-10: USD/KRW 1,506.2 fixing / ~1,502.7 spot.
**Greenshoe: still UNDISCLOSED** — and the carried "15% ≈ $4.0bn" hypothesis is likely TOO HIGH: "up to ~$27.9bn total" chatter implies ~$1.4bn ≈ 9.4M ADS ≈ **~5% option**. Carry as open with the 5% read favored until the exercised-option 6-K.
**Monday Jul-13 watch spec:** first real SKHY tape → compute premium vs ordinary on the 10:1 ratio + live FX ONLY (never vs $149 alone); anti-debut-chase gate on the one-company pick holds through the print regardless of tape.
