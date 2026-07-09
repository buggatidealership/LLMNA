# 2026-07-09 — Tier-2 verification: MURATA 2-claim adjudication (MS Rubin-rack MLCC + memory→handset demand destruction)

**Trigger:** W10 Jul-9 KR/JP scan (Leg A surfaced claim 1 via T3 relay; Leg B surfaced claim 2 as thesis-CONTRADICTING). 1 Opus verifier, ~33.7k tokens, auto-fired per lifted Tier-2 gate. WebFetch host-blocked on several primaries (anti-bot 403s: passive-components.eu, m2ri.jp, Murata IR, wccftech, BigGo) — triangulated via convergent WebSearch result sets + JP-native sources.

## Verdict table

| # | Claim | Verdict | Tier | Freshness (B40) | MURATA thesis effect |
|---|---|---|---|---|---|
| 1 | MS: VR200/Rubin rack MLCC ≈$4,320 vs GB300 ≈$1,530 (+182%) | **CONFIRMED** | T1-adjacent (dated MS note ~2026-05-22) via ≥4 convergent T2 hosts | RECYCLED not breaking (~7wk old; forward-valid, Rubin ships fall 2026) | **REINFORCE** |
| 2a | Memory ~4× YoY ≈90% of low-end handset **price**; JP FY26 handsets −7% | **CONFIRMED** w/ denominator catch | T1 (MM総研 id=714 2026-05-14; Nikkei) | 4×/90% snapshot = Feb-2026; theme current through Jun-2026 Nikkei | see 2b |
| 2b | Inference: "memory tightness destroys MURATA's consumer-MLCC base" | **REFRAME — immaterial** | T1 (Murata IR sensitivity) | current | **NEUTRAL** |

## Claim 1 detail (CONFIRMED)
Identical figures across passive-components.eu (board-level: compute-board MLCC $25→$90, switch $20→$45; 22→26-layer PCB, M7→M8), BigGo, Bitget, leoinai; parent = MS note dated ~2026-05-22 (VR200 NVL72 BOM ≈$7.8M; memory +435% ≈$2M; PCB +233%; MLCC +182%; ABF +82%; GPU share 63%→51%); corroborated by Dan Nystedt (T2) + futunn/wccftech/36kr. Arithmetic recheck (#43b): (4320−1530)/1530 = +182.4% ✓; 2.82×. Primary MS PDF not inspected (paywalled) — tier T1-adjacent-by-convergence. **→ TC-6 N+1 BOOKED (6→7).**

## Claim 2 detail (numbers real, inference immaterial for MURATA)
- MM総研 (T1, 2026-05-14, id=714): JP FY2026 handsets 29.97M (−7.0% YoY), smartphones 29.15M (−7.0%), declining to FY2029, explicitly memory-cost-push attributed — the demand-destruction MECHANISM is real (B47-class datapoint stands for the consumer-electronics cluster).
- **Denominator catch:** Nikkei says memory ≈90% of retail/unit PRICE (売価), not BOM — the "90% of BOM" framing swapped denominators.
- **Materiality math (Murata IR):** FY2025 rev ¥1,830.9bn record; capacitors ¥936.4bn (~51%); computer-use ¥310.4bn (+28.4%), datacenter ¥176.7bn (+73.9%). Murata's own sensitivity: global smartphone −1% ≈ −¥5.0bn. Japan ≈2-3% of global units → JP −7% ≈ −0.18% global units ≈ **−¥0.9bn ≈ 0.05% of revenue = NOISE**. Even a (not-claimed) global −7% ≈ −¥35bn ≈ −1.9%, spread across ALL phone content, not MLCC alone.
- **Second framing catch:** destroyed units are the low-end/1円端末 tail = LOWEST MLCC content per unit → impact smaller still; datacenter capacitor leg grew +~¥75bn YoY alone, dwarfing the drag.

## NET: REINFORCE
Per-rack AI-server MLCC content ~2.8× gen-on-gen (confirmed) strengthens the growth leg; the handset contradicting signal is real-mechanism / immaterial-magnitude for MURATA (targets the low-content tail at Japan scale). Route the −7% JP handset datapoint to consumer-electronics-cluster context, NOT as a MURATA bear leg.

**Open items:** primary MS PDF uninspected; exact Murata smartphone-share-of-MLCC % not pinned — revisit at Jul-31 print if needed.

Sources: passive-components.eu/nvidia-vera-rubin-why-one-ai-rack-needs-so-many-more-mlcc-capacitors/ · bitget.com/news/detail/12560605422208 · finance.biggo.com/news/ZwAZYJ4B-PfaobXfdRKp · wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/ · x.com/dnystedt/status/2058708719551303741 · m2ri.jp/release/detail.html?id=714 · nikkei.com/article/DGXZQOUB1849U0Y6A210C2000000/ · nikkei.com/article/DGXZQOUB059T80V00C26A6000000/ · corporate.murata.com/ja-jp/newsroom/news/irnews/irnews/2026/0430b · corporate.murata.com/en-us/ir/financial/segment · eetimes.itmedia.co.jp/ee/articles/2505/01/news079.html · eetimes.itmedia.co.jp/ee/articles/2605/01/news074.html
