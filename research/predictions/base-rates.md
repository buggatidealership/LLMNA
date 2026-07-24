# BASE-RATE LIBRARY (BR-1v2 rewrite 2026-07-18 — K3 build-verification E4/E5 fixes; classes bind EX-ANTE; min n=15 or parent+flag; regime tripwire suspends to parent; computed rates NEVER stack with B45 lift)

## Binding conventions (v2, K3-tightened)
1. **Membership is rule-based:** "tracked universe at registration date" (any name with a companies/ thesis at the time of the call) — no fixed list, no survivorship boundary.
2. **Vendor recorded per row; convention = strict `>` on the RECORDED vendor's estimate; meets/near-meets are NOT beats.**
3. **Both variants published** (strict + robust-excluding-near-meets |Δ|≤$0.01); **the PROGRAM PRIOR anchors on the ROBUST variant** (vendor-fragility bounded: FMP-strict 90.6% vs cross-vendor strict 77-83% per K3 recompute — an 8-13pt vendor swing, discovered 2026-07-18).
4. **Class-internal tripwire:** realized rate >10pp below class base for 2 consecutive quarters → class auto-suspends to parent pending recompute (independent of the macro PC-18 tripwire).
5. Rolling recompute quarterly + on any tripwire.

## BR-1 — Tracked AI-complex name beats quarterly EPS consensus (trailing 8 reported qtrs; vendor: FMP /stable/earnings, epsEstimated = FMP consensus snapshot, finer precision than press medians — see data-access.md gotcha)
- **PROGRAM PRIOR (robust): 82.8% (53/64)** · strict-FMP: 90.6% (58/64) · cross-vendor strict (K3, chartmill/Yahoo/stockstory): ~77-83% · **published range 77-91%, anchor = robust**
- Computed 2026-07-18 (v2 re-derivation, row table below); per-name robust deltas concentrated in MRVL + AVGO near-meets.

### Per-row data (v2 requirement: next cross-family recompute is one command)
| name | date | actual | FMP est | class | near-meet |
|---|---|---|---|---|---|
| NVDA | 2026-05-20 | 1.87 | 1.76 | BEAT |  |
| NVDA | 2026-02-25 | 1.62 | 1.54 | BEAT |  |
| NVDA | 2025-11-19 | 1.3 | 1.26 | BEAT |  |
| NVDA | 2025-08-27 | 1.05 | 1.01 | BEAT |  |
| NVDA | 2025-05-28 | 0.81 | 0.737 | BEAT |  |
| NVDA | 2025-02-26 | 0.89 | 0.848 | BEAT |  |
| NVDA | 2024-11-20 | 0.81 | 0.75 | BEAT |  |
| NVDA | 2024-08-28 | 0.68 | 0.645 | BEAT |  |
| TSM | 2026-07-16 | 4.31 | 3.82 | BEAT |  |
| TSM | 2026-04-15 | 3.49 | 3.31 | BEAT |  |
| TSM | 2026-01-15 | 3.09 | 2.9 | BEAT |  |
| TSM | 2025-10-16 | 2.92 | 2.63 | BEAT |  |
| TSM | 2025-07-17 | 2.5 | 2.38 | BEAT |  |
| TSM | 2025-05-15 | 2.14 | 2.07 | BEAT |  |
| TSM | 2025-01-16 | 2.19 | 2.2 | MISS |  |
| TSM | 2024-11-14 | 1.95 | 1.79 | BEAT |  |
| AVGO | 2026-06-03 | 2.44 | 2.4 | BEAT |  |
| AVGO | 2026-03-04 | 2.05 | 2.03 | BEAT |  |
| AVGO | 2025-12-11 | 1.95 | 1.87 | BEAT |  |
| AVGO | 2025-09-04 | 1.69 | 1.66 | BEAT |  |
| AVGO | 2025-06-05 | 1.58 | 1.57 | BEAT |  |
| AVGO | 2025-03-06 | 1.6 | 1.51 | BEAT |  |
| AVGO | 2024-12-12 | 1.42 | 1.38 | BEAT |  |
| AVGO | 2024-09-05 | 1.24 | 1.22 | BEAT |  |
| MU | 2026-06-24 | 25.11 | 20.98 | BEAT |  |
| MU | 2026-03-18 | 12.2 | 9.19 | BEAT |  |
| MU | 2025-12-17 | 4.78 | 3.96 | BEAT |  |
| MU | 2025-09-23 | 3.03 | 2.86 | BEAT |  |
| MU | 2025-06-25 | 1.91 | 1.6 | BEAT |  |
| MU | 2025-03-20 | 1.56 | 1.43 | BEAT |  |
| MU | 2024-12-18 | 1.79 | 1.75 | BEAT |  |
| MU | 2024-09-25 | 1.18 | 1.12 | BEAT |  |
| ASML | 2026-07-15 | 8.68 | 7.98 | BEAT |  |
| ASML | 2026-04-15 | 8.37 | 7.72 | BEAT |  |
| ASML | 2026-01-28 | 8.55 | 9.04 | MISS |  |
| ASML | 2025-10-15 | 6.41 | 6.27 | BEAT |  |
| ASML | 2025-07-16 | 6.84 | 6.1 | BEAT |  |
| ASML | 2025-04-16 | 6.31 | 6.12 | BEAT |  |
| ASML | 2025-01-29 | 7.3 | 7.41 | MISS |  |
| ASML | 2024-07-17 | 4.36 | 4.06 | BEAT |  |
| MRVL | 2026-05-27 | 0.8 | 0.798 | BEAT | Y |
| MRVL | 2026-03-05 | 0.8 | 0.792 | BEAT | Y |
| MRVL | 2025-12-02 | 0.76 | 0.743 | BEAT |  |
| MRVL | 2025-08-28 | 0.67 | 0.673 | MISS | Y |
| MRVL | 2025-05-29 | 0.62 | 0.612 | BEAT | Y |
| MRVL | 2025-03-05 | 0.6 | 0.59 | BEAT |  |
| MRVL | 2024-12-03 | 0.43 | 0.41 | BEAT |  |
| MRVL | 2024-08-29 | 0.3 | 0.2936 | BEAT | Y |
| SNOW | 2026-05-27 | 0.39 | 0.3193 | BEAT |  |
| SNOW | 2026-02-25 | 0.32 | 0.2725 | BEAT |  |
| SNOW | 2025-12-03 | 0.35 | 0.3116 | BEAT |  |
| SNOW | 2025-08-27 | 0.35 | 0.267 | BEAT |  |
| SNOW | 2025-05-21 | 0.24 | 0.2124 | BEAT |  |
| SNOW | 2025-02-26 | 0.3 | 0.1765 | BEAT |  |
| SNOW | 2024-11-20 | 0.2 | 0.15 | BEAT |  |
| SNOW | 2024-08-21 | 0.18 | 0.161 | BEAT |  |
| NOW | 2026-04-22 | 0.97 | 0.97 | MEET | Y |
| NOW | 2026-01-28 | 0.92 | 0.885 | BEAT |  |
| NOW | 2025-10-29 | 0.964 | 0.851 | BEAT |  |
| NOW | 2025-07-23 | 0.818 | 0.713 | BEAT |  |
| NOW | 2025-04-23 | 0.808 | 0.766 | BEAT |  |
| NOW | 2025-01-29 | 0.734 | 0.73 | BEAT | Y |
| NOW | 2024-10-23 | 0.4143 | 0.69 | MISS |  |
| NOW | 2024-07-24 | 0.626 | 0.565 | BEAT |  |

## BR-2 — (RESERVED ex-ante) Guide-quarter revenue-guide RAISE at supply-constrained tracked names — define inclusion rule before first computation.

Rules: a class created for one call binds all future matching calls; edits append-only with dates.

## 2026-07-19 — I-4 INSTRUMENT BLOCK (commissioning; per `signals/cross-source-log/2026-07-19-sun-wave2-blind-adversary-results-october-audit-amendments.md`)
Type: measurement; feeds: P-provenance base-P of every registration. Atoms: {beat, "actual > FMP epsEstimated (robust |Δ|>$0.01)", "vendor divergence vs press medians / precision change"}; {snapshot-vintage, "estimate frozen at derivation date", "**derivation vintage ≠ resolution vintage — the 82.8% is a property of WHICH DAY'S estimate; PIN BOTH at BR-1v3**"}; {class-membership, "rule-based ex-ante", "name qualifying for 2 classes / definition drift"}. Blind-adversary non-overlap catches (booked): walk-down world (bar is sandbagged — beat ≠ good quarter; check T-90→T-1 drift + beat-then-selloff fraction at re-derive); regime-conditioning (8 qtrs all in-boom; down-cycle backtest required); non-exchangeability (per-name spread must be disclosed — a 4/8 name and an 8/8 name both "starting at 83%" fits nobody); anchor-contamination (base-P governs BEATS-CONSENSUS only — never anchor reaction/guide questions on it; evidence double-count guard: AI-demand strength is already IN the base). BR-1v3 quarterly re-derive requirements: vintage-pinning, walk-down decomposition, down-cycle backtest, per-name spread, original-universe survivorship reconciliation. Shared-inputs: FMP /stable/earnings (also: brier ledger resolution, earnings calendar) — concentration-flagged. Kill: FMP methodology change or class tripwire fires. Escort: next 3 uses of base-P carry the vintage caveat inline.
