#!/usr/bin/env python3
"""
calibration_curve.py — the TRUST MAP generator (compute-layer item (a), built 2026-07-09).

Two-layer design (decided at build time after inspecting the data):
  LAYER 1 (bootstrap, brittle by nature): best-effort parse of the PROSE-era records —
    grading-log.md Graded rows + P~X% claims across research/. Unparseable rows are
    COUNTED AND REPORTED, never silently dropped (#43b: the mismatch is information).
  LAYER 2 (durable): predictions/calibration-ledger.csv — machine-readable, one row per
    graded component, appended AT GRADE TIME going forward. The prose was the bug;
    structured logging is the fix. Future runs compute the curve from the CSV.

Output: research/meta/trust-map.md (GENERATED — do not hand-edit; regenerate via
  python3 research/meta/scripts/calibration_curve.py)

Trust-map sections: P-band calibration table | outcome tally | claim inventory by hedge
type | data-quality report (unparseable/unresolved counts) | known-faculty trust notes
(static references to B-series adjudications, included for session-prime consumption).
"""
import re, csv, datetime, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]  # .../research
LEDGER = ROOT / "predictions" / "calibration-ledger.csv"
OUT = ROOT / "meta" / "trust-map.md"
TODAY = datetime.date.today().isoformat()

BANDS = [(80, 101, "80-100%"), (60, 80, "60-79%"), (40, 60, "40-59%"), (20, 40, "20-39%"), (0, 20, "0-19%")]

def band_of(p):
    for lo, hi, name in BANDS:
        if lo <= p < hi:
            return name
    return None

# ---------- Layer 2: the durable CSV ----------
LEDGER_HEADER = ["date_graded", "prediction_id", "ticker", "component", "claimed_p",
                 "outcome", "magnitude_delta_pct", "layer_failed", "notes"]

def read_ledger():
    rows = []
    if LEDGER.exists():
        with open(LEDGER) as f:
            rows = [r for r in csv.DictReader(f)]
    return rows

# ---------- Layer 1: prose-era bootstrap ----------
OUTCOME_PATTERNS = {
    "TRUE":  re.compile(r"\b(RIGHT direction|CLEAN HIT|band-hit|HIT\b|BEAT.*predicted|directional HIT|H1 FIRED)", re.I),
    "FALSE": re.compile(r"\b(WRONG DIRECTION|band-miss|MISS\b|FALSIFIED)", re.I),
    "MIXED": re.compile(r"\b(PARTIAL|CONFOUNDED|MIXED|REFINE)", re.I),
}

def parse_graded_rows():
    """Best-effort tally of graded prose rows. Multi-target rows counted as MIXED unless clean."""
    gl = (ROOT / "predictions" / "grading-log.md").read_text()
    graded_section = gl.split("## Graded", 1)[-1]
    rows = [l for l in graded_section.splitlines() if l.startswith("|") and "---" not in l and "Prediction file" not in l]
    tally = {"TRUE": 0, "FALSE": 0, "MIXED": 0, "UNPARSEABLE": 0}
    for r in rows:
        hits = {k: bool(p.search(r)) for k, p in OUTCOME_PATTERNS.items()}
        if hits["MIXED"] or (hits["TRUE"] and hits["FALSE"]):
            tally["MIXED"] += 1
        elif hits["TRUE"]:
            tally["TRUE"] += 1
        elif hits["FALSE"]:
            tally["FALSE"] += 1
        else:
            tally["UNPARSEABLE"] += 1
    return tally, len(rows)

P_CLAIM = re.compile(r"P[~=(]\s*(?:bull|bear|beat|raise|FY-raise)?\s*[)~=]?\s*(\d{1,2})\s*%")

def claim_inventory():
    """Count live P-claims across research/ by band (inventory = instrumentation coverage, not outcomes)."""
    counts = {name: 0 for _, _, name in BANDS}
    files = 0
    for p in ROOT.rglob("*.md"):
        if "trust-map" in p.name:
            continue
        try:
            t = p.read_text()
        except Exception:
            continue
        found = P_CLAIM.findall(t)
        if found:
            files += 1
        for v in found:
            b = band_of(int(v))
            if b:
                counts[b] += 1
    return counts, files

def compute_curve(ledger_rows):
    curve = {name: {"n": 0, "true": 0} for _, _, name in BANDS}
    skipped = 0
    for r in ledger_rows:
        try:
            p = float(r["claimed_p"])
        except (ValueError, KeyError):
            skipped += 1
            continue
        b = band_of(p)
        if not b or r.get("outcome") not in ("TRUE", "FALSE"):
            skipped += 1
            continue
        curve[b]["n"] += 1
        curve[b]["true"] += (r["outcome"] == "TRUE")
    return curve, skipped

def main():
    if not LEDGER.exists():
        with open(LEDGER, "w", newline="") as f:
            csv.writer(f).writerow(LEDGER_HEADER)
    ledger_rows = read_ledger()
    curve, skipped = compute_curve(ledger_rows)
    tally, n_prose = parse_graded_rows()
    inv, n_files = claim_inventory()

    lines = [
        f"# TRUST MAP — generated {TODAY} by `meta/scripts/calibration_curve.py` (DO NOT HAND-EDIT)",
        "",
        "**Regenerate:** `python3 research/meta/scripts/calibration_curve.py` | Feed the summary into session-prime at each monthly audit.",
        "",
        "## P-band calibration curve (from calibration-ledger.csv — the computable record)",
        "| Band | N graded | N TRUE | Hit rate | Calibration read |",
        "|---|---|---|---|---|",
    ]
    for _, _, name in BANDS:
        c = curve[name]
        if c["n"]:
            hr = c["true"] / c["n"] * 100
            mid = (int(name.split("-")[0]) + int(name.split("-")[1].rstrip("%"))) / 2
            read = "overconfident" if hr < mid - 15 else "underconfident" if hr > mid + 15 else "in-band"
            lines.append(f"| {name} | {c['n']} | {c['true']} | {hr:.0f}% | {read} |")
        else:
            lines.append(f"| {name} | 0 | 0 | n/a | NO STRUCTURED DATA YET |")
    lines += [
        f"\n*Ledger rows: {len(ledger_rows)} total, {skipped} skipped (unresolved/malformed).*",
        "",
        "## Prose-era graded outcomes (Layer-1 bootstrap tally — heterogeneous multi-target rows, treat as directional)",
        f"| TRUE-leaning | FALSE-leaning | MIXED | UNPARSEABLE | total prose rows |",
        f"|---|---|---|---|---|",
        f"| {tally['TRUE']} | {tally['FALSE']} | {tally['MIXED']} | {tally['UNPARSEABLE']} | {n_prose} |",
        "",
        "## Instrumentation coverage (live P-claims found across research/*.md)",
        "| Band | N claims in corpus |", "|---|---|",
    ]
    for _, _, name in BANDS:
        lines.append(f"| {name} | {inv[name]} |")
    lines += [
        f"\n*{n_files} files carry P-claims. Inventory ≠ outcomes: this measures how much reasoning is instrumented, not how good it is.*",
        "",
        "## Data-quality verdict (the honest section)",
        f"- **The central finding of the first run ({TODAY}): the harness's grades are stored as PROSE and are only "
        f"~{(tally['TRUE']+tally['FALSE'])}/{n_prose} cleanly machine-adjudicable.** The trust map cannot be better than its substrate.",
        "- **Fix (binding from today): every GRADE appends one row to `predictions/calibration-ledger.csv`** "
        "(schema: date_graded, prediction_id, ticker, component, claimed_p, outcome TRUE/FALSE/MIXED, magnitude_delta_pct, layer_failed, notes). "
        "One prediction = N component rows. The prose grade remains the narrative record; the CSV row is the computable record.",
        "- Backfill task: seed the CSV from the ~15 prose-era grades at the next audit (manual one-time pass; each row takes ~30s).",
        "",
        "## Known-faculty trust adjudications (static references, outcomes-based, for session-prime)",
        "| Faculty | Trust state | Evidence |",
        "|---|---|---|",
        "| Magnitude estimates in AI-supercycle regime | LOW — systematically conservative | B45 (15-name basket, tail under-modeled 5-8x) |",
        "| Arithmetic in prose | LOW — use compute tool | #43b origin (3 catches first run, 2026-07-07) |",
        "| Recall of regulatory/policy state | LOW — verify before framing | 2026-07-09 two-gate inversion (H200 US-license state) |",
        "| Source attribution from social relays | LOW — always verify | 7/7 framing catches 2026-07-09 |",
        "| Opus verification pipeline (Rule #16) | HIGH | ledger 30d: ~31 fires, 30 HIGH, 0 ZERO |",
        "| Two-leg scan discipline (W10) | HIGH | ledger + first-week review 2026-07-03 |",
    ]
    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} | ledger rows={len(ledger_rows)} | prose rows={n_prose} (unparseable={tally['UNPARSEABLE']}) | claims={sum(inv.values())} in {n_files} files")

if __name__ == "__main__":
    sys.exit(main())
