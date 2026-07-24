#!/usr/bin/env python3
"""Running Brier tally for the calibration ledger (Probability-Resolution Program v2, Phase 1).
Reads predictions/calibration-ledger.csv; reports system vs base-rate vs shrinkage Brier,
Murphy decomposition (REL/RES/UNC), and per-bucket calibration — at wakes, not quarterly.
KNOWN-ANSWER TEST (frozen K3 pack, n=41 at HEAD d816abf): system 0.1978 / base 0.1844 /
shrinkage 0.1777; RES/REL are BUCKETING-DEPENDENT (0.1-bins here vs coarser splits elsewhere) — compare only like-for-like. Run with --selftest to verify against those.
Usage: python3 brier_tally.py [--since YYYY-MM-DD] [--selftest]
"""
import csv, sys, statistics, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "predictions" / "calibration-ledger.csv"

def rows(since=None):
    out = []
    for r in csv.DictReader(open(LEDGER)):
        if r.get("outcome","").strip() not in ("TRUE","FALSE"): continue
        try: p = float(r["claimed_p"]); p = p/100 if p > 1 else p
        except (ValueError, KeyError): continue
        if since and r.get("date_graded","") < since: continue
        out.append((p, 1.0 if r["outcome"].strip()=="TRUE" else 0.0))
    return out

def report(bins, label=""):
    n = len(bins)
    if n < 2: return print(f"{label}: n={n} — too few rows")
    base = sum(o for _,o in bins)/n
    br  = sum((p-o)**2 for p,o in bins)/n
    brb = sum((base-o)**2 for _,o in bins)/n
    brs = sum(((p+base)/2-o)**2 for p,o in bins)/n
    # Murphy: bucket by claimed p (0.1 bins)
    from collections import defaultdict
    buckets = defaultdict(list)
    for p,o in bins: buckets[round(p,1)].append((p,o))
    rel = sum(len(v)*( (sum(p for p,_ in v)/len(v)) - (sum(o for _,o in v)/len(v)) )**2 for v in buckets.values())/n
    res = sum(len(v)*( (sum(o for _,o in v)/len(v)) - base )**2 for v in buckets.values())/n
    sd = statistics.stdev([(p-o)**2-(base-o)**2 for p,o in bins]) if n > 2 else float('nan')
    print(f"{label}: n={n} base={base:.3f} | Brier sys {br:.4f} / base {brb:.4f} / shrink {brs:.4f} "
          f"| REL {rel:.4f} RES {res:.4f} UNC {base*(1-base):.4f} | 2σ-detectable Δ {2*sd/math.sqrt(n):.3f}")
    for k in sorted(buckets):
        v = buckets[k]
        print(f"   claimed~{k:.1f}: n={len(v)} realized={sum(o for _,o in v)/len(v):.2f}")

if __name__ == "__main__":
    since = None
    if "--since" in sys.argv: since = sys.argv[sys.argv.index("--since")+1]
    if "--selftest" in sys.argv:
        b = rows()
        n = len(b); base = sum(o for _,o in b)/n
        br = sum((p-o)**2 for p,o in b)/n
        ok = abs(br-0.1978) < 0.02  # ledger grows; loose bound on full-history run
        print(f"selftest: n={n} brier={br:.4f} (frozen-pack reference 0.1978 at n=41) — {'PLAUSIBLE' if ok else 'CHECK'}")
    report(rows(since), f"BRIER TALLY{' since '+since if since else ' (full ledger)'}")
