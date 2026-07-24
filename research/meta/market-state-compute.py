#!/usr/bin/env python3
"""MARKET-STATE compute (spec: sector/market-state-function-spec.md, P1).

Input: CSV lines on stdin or a file arg — name,cohort,day_pct[,source_tier]
Output: computed state vector — per-cohort means, cross-cohort dispersion,
breadth, divergence flags. NO narration; interpretation happens downstream.
Hybrid sourcing (user decision 2026-07-08): pull-agent tape + user screenshots.
#43b: every number here is computed, never eyeballed.
"""
import csv, statistics, sys
from collections import defaultdict

def main() -> None:
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    rows = [r for r in csv.reader(src) if r and not r[0].startswith("#")]
    cohorts = defaultdict(list)
    for r in rows:
        name, cohort, pct = r[0].strip(), r[1].strip(), float(r[2])
        cohorts[cohort].append((name, pct))

    print(f"{'cohort':<18}{'n':>3}{'mean%':>8}{'min':>8}{'max':>8}  members")
    means = {}
    for c, members in sorted(cohorts.items()):
        vals = [p for _, p in members]
        means[c] = statistics.mean(vals)
        lo, hi = min(members, key=lambda m: m[1]), max(members, key=lambda m: m[1])
        print(f"{c:<18}{len(vals):>3}{means[c]:>8.2f}{lo[1]:>8.2f}{hi[1]:>8.2f}  "
              f"low={lo[0]} high={hi[0]}")

    all_vals = [p for ms in cohorts.values() for _, p in ms]
    up = sum(1 for v in all_vals if v > 0)
    print(f"\nbreadth: {up}/{len(all_vals)} up ({up/len(all_vals):.0%})")
    if len(means) >= 2:
        spread = max(means.values()) - min(means.values())
        top = max(means, key=means.get); bot = min(means, key=means.get)
        print(f"cross-cohort dispersion: {spread:.2f}pp ({top} {means[top]:+.2f} vs {bot} {means[bot]:+.2f})")
        # divergence flag: any cohort mean opposite-signed vs the all-name mean by >1.5pp
        overall = statistics.mean(all_vals)
        for c, m in sorted(means.items()):
            if overall != 0 and (m > 0) != (overall > 0) and abs(m - overall) > 1.5:
                print(f"DIVERGENCE FLAG: {c} ({m:+.2f}) opposite-signed vs tape mean ({overall:+.2f})")

if __name__ == "__main__":
    main()
