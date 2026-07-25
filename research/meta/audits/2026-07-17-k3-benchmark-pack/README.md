# LLMNA Benchmark-Audit — Reproducibility Pack (Frozen Baseline)

**Audited commit (REQUIRED checkout to reproduce the frozen numbers):**
`d816abf1664d23a50a1927b8a6f3365c8a6939e7` — main, 2026-07-17T22:05:42Z, 1230 commits.
The repository itself is NOT included in this pack (the resident session has it); run against a checkout pinned to this commit. `reproduce.py` prints a MATCH/MISMATCH line against it at STEP 0.

**Auditor:** external cross-family reviewer (Kimi K3), 2026-07-18
**Null hypothesis:** this system has no predictive edge beyond cheap baselines.
**Determinism:** `reproduce.py` regenerates every headline number and every CSV byte-identically, offline, from any working directory. Verified 2026-07-18 (all four CSVs diff-identical).

## Usage (no network, two arguments)

```bash
git clone https://github.com/buggatidealership/LLMNA.git && cd LLMNA && git checkout d816abf1664d23a50a1927b8a6f3365c8a6939e7 && cd ..
python3 reproduce.py --repo ./LLMNA --pack .
# regenerated CSVs land in ./audit-repro-out/ — diff against the frozen ones here; all four must be identical
```

Receipt verification = run the two lines above + compare the four headline lines against `MANIFEST.txt` §EXPECTED-OUTPUTS.

## Manifest

| file | content |
|---|---|
| `reproduce.py` | STEP 0 + registration integrity + Tests 1–3 compute; path-independent, offline, seeded bootstraps (42/7) |
| `test1_binary_rows.csv` | 51 probability rows: 41 included binary + 10 excluded MIXED, inclusion decisions + `parrot_row` flag (20 rows = consensus-parrot subset; rule: `consensus\|guide\|whisper\|beat` on component) |
| `test2_point_estimates.csv` | 28 point rows: 20 street-sourced head-to-head + 8 UNSOURCED-STREET, with actual/repo/street/source/verdict/delta |
| `test3_trade_windows.csv` | 11 trade windows: entry/exit dates+prices, returns vs SOXX/QQQ, truncation flags |
| `test4_selection_integrity.md` | registration-ratio evidence (83% confirmed / 71% incl-ambiguous) |
| `test5_overrides.csv` | 5 human-vs-harness override events with prices and ex-post verdicts |
| `registration_integrity.csv` | all 28 prediction artifacts: first-commit vs event date + post-registration edit assessments |
| `prices/*.csv` | 16 frozen daily-close series (Yahoo Finance, fetched 2026-07-18, range 2026-05-15→07-18) |
| `MANIFEST.txt` | SHA-256 of every file + expected headline outputs |

## Verdicts (as reported)

1. **Calibration:** Brier 0.1978 vs coin 0.2500 / base-rate 0.1844 / parrot 0.1000 (system 0.1377 on parrot rows). Bootstrap P(better): 0.964 / 0.359 / 0.078. Under-confident in every populated bucket. **RECORD TOO YOUNG, null-favored.**
2. **Point estimates:** 12W/7L/1T of 20 sourced rows; mean Δ +1.03pp (CI [+0.05,+1.99], P=0.98). **NULL REJECTED (weak, small-n).**
3. **Economic value:** −3.63% vs SOXX −1.25% / QQQ −2.26%; 3/11 beat SOXX; coverage 11/22 registration artifacts (50%) → no extrapolation. **NULL CONFIRMED.**
4. **Selection integrity:** 10/12 prints registered (83%); misses inside the registered set; NTAP skip + DELL post-hoc + Samsung duplicate-registration flagged.
5. **Research vs realized book:** exposure-reducing overrides 4/4 vindicated (MRVL −29.3%, SNDK −33.3%, SKH −15.8%, NBIS −17.6% since exits); SKHY override −11.2% underwater. PF-1 doctrine falsified as written by this window.

## Corrections to the audit prose (found while freezing)

- "26 prediction artifacts" → exact count **28** (22 registration + 6 GRADE files). Coverage restated: 11/22 registration artifacts (50%) cleanly tradeable. Verdicts unchanged.
- Prose bootstrap P (0.966/0.359/0.079) vs script (0.964/0.359/0.078): ±0.002 RNG-layout jitter; script is the deterministic reference.

## Next quarter

1. Checkout the new HEAD; rerun `reproduce.py` (it prints MATCH/MISMATCH vs the baseline commit).
2. Keep frozen `prices/` for baseline windows; add series only for new trades.
3. Same inclusion rules (binary-only primary, MIXED=0.5 sensitivity; |est−act|/act; street from repo files; LONG-at-registration-close→+30d; equal weight; SOXX/QQQ matched windows).
4. Null stays the default position. Always.
