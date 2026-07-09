# TRUST MAP — generated 2026-07-09 by `meta/scripts/calibration_curve.py` (DO NOT HAND-EDIT)

**Regenerate:** `python3 research/meta/scripts/calibration_curve.py` | Feed the summary into session-prime at each monthly audit.

## P-band calibration curve (from calibration-ledger.csv — the computable record)
| Band | N graded | N TRUE | Hit rate | Calibration read |
|---|---|---|---|---|
| 80-100% | 7 | 7 | 100% | in-band |
| 60-79% | 15 | 11 | 73% | in-band |
| 40-59% | 10 | 7 | 70% | underconfident |
| 20-39% | 2 | 1 | 50% | underconfident |
| 0-19% | 1 | 1 | 100% | underconfident |

*Ledger rows: 76 total, 41 skipped (unresolved/malformed).*

## Prose-era graded outcomes (Layer-1 bootstrap tally — heterogeneous multi-target rows, treat as directional)
| TRUE-leaning | FALSE-leaning | MIXED | UNPARSEABLE | total prose rows |
|---|---|---|---|---|
| 2 | 0 | 4 | 0 | 6 |

## Instrumentation coverage (live P-claims found across research/*.md)
| Band | N claims in corpus |
|---|---|
| 80-100% | 36 |
| 60-79% | 296 |
| 40-59% | 496 |
| 20-39% | 468 |
| 0-19% | 232 |

*240 files carry P-claims. Inventory ≠ outcomes: this measures how much reasoning is instrumented, not how good it is.*

## Data-quality verdict (the honest section)
- **The central finding of the first run (2026-07-09): the harness's grades are stored as PROSE and are only ~2/6 cleanly machine-adjudicable.** The trust map cannot be better than its substrate.
- **Fix (binding from today): every GRADE appends one row to `predictions/calibration-ledger.csv`** (schema: date_graded, prediction_id, ticker, component, claimed_p, outcome TRUE/FALSE/MIXED, magnitude_delta_pct, layer_failed, notes). One prediction = N component rows. The prose grade remains the narrative record; the CSV row is the computable record.
- Backfill task: seed the CSV from the ~15 prose-era grades at the next audit (manual one-time pass; each row takes ~30s).

## Known-faculty trust adjudications (static references, outcomes-based, for session-prime)
| Faculty | Trust state | Evidence |
|---|---|---|
| Magnitude estimates in AI-supercycle regime | LOW — systematically conservative | B45 (15-name basket, tail under-modeled 5-8x) |
| Arithmetic in prose | LOW — use compute tool | #43b origin (3 catches first run, 2026-07-07) |
| Recall of regulatory/policy state | LOW — verify before framing | 2026-07-09 two-gate inversion (H200 US-license state) |
| Source attribution from social relays | LOW — always verify | 7/7 framing catches 2026-07-09 |
| Opus verification pipeline (Rule #16) | HIGH | ledger 30d: ~31 fires, 30 HIGH, 0 ZERO |
| Two-leg scan discipline (W10) | HIGH | ledger + first-week review 2026-07-03 |
