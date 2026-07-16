# 2026-07-16 THU — Korea margin-loan STOCK: JPM/KOFIA chart ingest (user Twitter relay; 1 Opus KR-native verifier, Rule #16)

**WORKFLOW: INGEST + verification.** User-shared JPMAM chart ("Korea margin loans outstanding, KOSPI and KOSDAQ", source KOFIA, cut 2026-06-05, ~₩38T endpoint). Twitter wrapper T3 → JPM packaging T2 → KOFIA series T1-derived. **B40 flag: chart cut Jun-5 = pre-peak AND pre-everything-July** (crash, purge, BOK hike). Verifier caveat: KR article bodies + KOFIA portal 403'd through proxy — figures are search-layer reads of those pages (T2/T1-derived, decimals carry bands).

## THE SERIES, PINNED (verifier, KR-native multi-source)

| Datum | Value | Date | Tier |
|---|---|---|---|
| 신용거래융자 (margin loans) PEAK | **₩38.6328T — all-time record** | **Jun-24** | T2 multi (Newsis/FN/Etoday) |
| Waypoints | 36.47 (May-21) → 38.02 (May-29) → 38.48 (Jun-19) → peak → 37.32 (Jun-end) → **36.63 (Jul-9)** | | T2 |
| House ₩34.79T (Jul-15) | directionally coherent w/ the Jul-13 crash de-lever; NOT independently re-pinned — needs raw KOFIA daily | Jul-15 | house/T2 single |
| **예탁증권담보융자 (collateral loans — the SECOND book)** | **₩25.00T** | Jul-1 | T1-derived (freesis) |
| **신용공여 TOTAL** | **₩62.76T** | Jul-1 | T1-derived |
| 반대매매 July | 288억 (Jul-8) → **1,422억 (Jul-9, 10.2% of shortfalls)** → 816억 (Jul-10); cumulative 425.8B thru Jul-10 (house 451.9B thru Jul-13 consistent) | | T2 |
| **Jul-15/16 second-wave print** | **DOES NOT EXIST YET** — Segye Jul-15: "4258억은 예고편" (the 425.8B was "the trailer"); anticipated, unprinted | | T2 |
| KOSPI context correction | index peaked **>9,100 (Jun-22)**; 8,000-class prints in July = DOWNSLOPE levels (my verifier-prompt framing of "8,088 early-July peak" was wrong — corrected) | | T2 |

**SCOPE ADJUDICATION (the chart's fine print):** JPM's ~38T = 신용거래융자 ONLY. The full retail-leverage stock is **~₩62.76T** — margin loans PLUS a ₩25T securities-collateral book the chart doesn't show (1.66× the margin-only lens, computed). Any reflexivity model keyed to "38T" understates the structure.

**B40 CATCH (live recycle in the wild):** a "₩36.5675T record, 15일 기준" figure circulating in search results is the **MAY-15** print mislabeled as July (Sisajournal/Sedaily cross-check). The genuine July series is LOWER and FALLING. Killed before ingest.

## THE COMPUTED READ (my model, on verified inputs)

1. **The de-lever is real but shallow: peak → Jul-15 = −9.9% (−₩3.84T, computed)** — and forced sales were only **11.8% of it (computed)**; ~88% was voluntary de-risking. The purge metaphor was backwards: the visible 반대매매 was the tip; the iceberg moved on its own.
2. **The overhang is intact at historic scale:** even post-de-lever, ~₩34.8T margin-only ≈ **1.4× the 2021 meme-era peak** (peak was 1.55×, computed) sitting on top of a separate ₩25T collateral book — and the BOK just raised the carrying cost of all of it for the first time in 3.5 years, explicitly citing 빚투 (T1 FN News).
3. **Joint-state into Jul-29 (SKHY print):** margin balances concentrate in Samsung/SKH (verifier: the crash days hit exactly those names hardest). Mechanism, both directions: a print disappointment meets a loaded margin structure (amplified downside); a beat against the KIS-lowered bar meets the same structure as fuel (squeeze). **The leverage stock is a VOLATILITY amplifier, not a directional signal.** 1st order (P>80%): Jul-15/16 반대매매 prints land within days and gauge the second wave. 2nd order (P~60%, my model): F4 measures on leveraged ETFs dampen the single-stock amplifier mechanically before Jul-29. 3rd order (P~40%, my model): if the BOK continues hiking into Q3, the carrying-cost channel forces a structural de-lever that caps KOSPI multiple expansion independent of semi fundamentals — the KR-local leg of the funding-node.
4. **Instrumentation note:** this series is exactly what BOK ECOS / KOFIA freesis serve deterministically — freesis 403s agents (portal, no API), ECOS has an API (user signup queued). Until then this stays agent-fetched with date-pins.

## CASCADES (this commit)
- `companies/HYNIX/thesis.md` — Jul-29 risk-frame refinement (amplifier read + unprinted second-wave gauge).
- `sector/ai-funding-shock-node.md` — KR leg: total 신용공여 ₩62.76T quantified; BOK carrying-cost channel.
- `meta/day-state.md` — watch: KOFIA Jul-15/16 prints; ECOS signup queued.
- Ledger: 1 fire ~39.2k, HIGH (scope adjudication + peak-dating + live B40 recycle kill + my own prompt-framing error corrected + second-wave nonexistence honestly reported).

**Position implication: HOLD SKHY 37 ADS / MURATA 336 / SUMCO 626 — no size change — the leverage stock is context not signal (Rule #8): it raises the VARIANCE of the Jul-29 outcome in both directions without moving the demand thesis (which today's TSMC capex raise independently reinforced); the actionable watches are the KOFIA second-wave prints and F4 ETF measures, both pre-Jul-29.** 🟡
