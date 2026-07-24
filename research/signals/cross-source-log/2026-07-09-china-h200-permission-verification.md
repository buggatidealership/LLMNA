# 2026-07-09 — China H200 "permission" story — Tier-2 verification (user Twitter share + screenshot)

**Trigger:** user screenshot (The Information article) + ALL-CAPS relay claiming "China HAS APPROVED 200,000 H200." 1 Opus verifier ~22.5k, EN+CN-native.

## Verdicts
| # | Claim | Verdict | Tier |
|---|---|---|---|
| 1 | Origin = The Information, 2026-07-08 | CONFIRMED-FRESH | T1 primary |
| 2 | Beijing told Alibaba/ByteDance/DeepSeek they MAY soon get H200 permission | UNVERIFIED-SINGLE-SOURCE (Reuters/Bloomberg/Sina/LTN all attribute to The Information — syndication ≠ corroboration) | T1 primary only |
| 3 | Cap "fewer than 200,000," <half of requests (implies >400k requested) | CONFIRMED as-reported (deliberated CEILING, not set number) | T1/T2 |
| 4 | Training-only; inference → domestic chips; public data only | CONFIRMED as-reported | T1/T2 |
| 5 | No final approvals; timing could change | CONFIRMED | T1/T2 |
| 6 | Tweet: "China HAS APPROVED 200,000" | **REFUTED — headline inflation on 3 axes** (ceiling not grant; "may soon" not approved; "fewer than" not equal) | T3 |

## ⚠️ TWO-GATE SELF-CORRECTION (my framing error, caught by the verifier)
My pre-verification framing ("China-side permission is worthless without a US export license") was **INVERTED**. Verified state: **US gate OPEN since 2026-02-26** (Bloomberg T1: Nvidia H200 export license; Trump framework 25% China-revenue share to US govt, 50% volume cap, TSMC-made→US inspection→re-export) and **~10 Chinese firms US-cleared 2026-05-14** (CNBC T1: Alibaba, Tencent, ByteDance, JD, Lenovo, Foxconn; ~75k/customer cap; chips undelivered as of mid-May). **The binding gate was CHINA'S OWN reluctance** (domestic-silicon push) — Jensen's May "expect nothing" referred to Beijing, not Washington. The Jul-8 story = Beijing easing its own block = the genuinely new increment.

## B40 dedup
Fresh reporting (Jul-8), distinct from: 2025 H20 saga (different chip, 15% rev-share); Feb-2026 US H200 framework; May-2026 US clearance of 10 firms. Same arc, new increment = China's posture.

## Memory read-through (compute note, #43b)
H200 = 141 GB HBM3e/GPU (NVIDIA spec T1). Cap math: 200,000 × 141 GB ≈ 28.2M GB ≈ 27.5 PB HBM3e — **upper bound, and read-through is WEAK**: H200 is existing Hopper silicon; if shipped from built inventory, HBM was consumed at manufacture → no incremental HBM demand unless NVDA schedules NEW H200 builds for this channel. Do NOT model fresh SKH/Micron/Samsung demand off this item.

## Market reaction
NVDA +1 to +1.5% intraday Jul-8 on the report (muted — consistent with US gate already known-open + single-source + capped). A circulating "+3.7% biggest gain in a month" is NOT cleanly attributable to this item — flagged, not booked.

## NET
- NVDA China narrative: directional-positive demand-side signal (Beijing easing), single-source, capped, training-only — sentiment not catalyst.
- HBM cohort: weak read-through (inventory nuance) — no cascade.
- **MURATA/SUMCO: NOT touched** (<200k GPUs = rounding error for MLCC; no China wafer pull). No thesis cascade.
- Structural keeper: training-on-NVDA / inference-on-domestic bifurcation formalizes the China two-stack — feeds CXMT/domestic-substitution watch (candidates file, Jul-7 entry) as REINFORCING context.

Sources: theinformation.com/articles/china-plans-let-top-ai-firms-buy-limited-amount-nvidia-h200-chips · investing.com/news/stock-market-news/...-4782000 (Reuters Jul-8) · bloomberg.com/news/articles/2026-07-08/china-to-let-ai-firms-buy-nvidia-h200-chips-information-says · finance.sina.com.cn/stock/bxjj/2026-07-08/doc-inihckrs8002179.shtml · ec.ltn.com.tw/article/breakingnews/5498860 · cnbc.com/2026/05/14/us-clears-h200-chip-sales-to-10-china-firms... · bloomberg.com/news/articles/2026-02-26/nvidia-gets-us-license-for-small-amount-of-h200-exports-to-china · techpowerup.com/343844 · nvidia.com/en-us/data-center/h200/
