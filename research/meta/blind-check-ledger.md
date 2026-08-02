# Blind-check compliance ledger (Principle #51)

Append-only dated readings from `meta/tools/blind_check_audit.py`.
A MISSING reading is itself a finding — the gap in the date column is the
evidence that the re-eval did not happen.

| date | baseline ref | baseline cohort | NEW cohort (post-#51) | boilerplate test |
|---|---|---|---|---|
| 2026-08-02 | 0c9cad1 | 0/155 (0.0%) | 0/0 (n/a) | n/a |
| 2026-08-02 | 0c9cad1 | 2/160 (1.2%) | 0/0 (n/a) | n/a |
