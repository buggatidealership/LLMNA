#!/usr/bin/env python3
"""Blind-check compliance audit (Principle #51 verification instrument, built 2026-08-02).

WHY THIS EXISTS
---------------
Principle #51 says every detector must state what would make it stop detecting.
#51 is itself a standard with no enforcement. The direct lesson from
`macro-anchor-hook` — whose pre-registered repair criterion ("FP rate >30% ->
tighten exemptions") is UNMEASURABLE from its own log, and has sat un-adjudicable
through two scheduled reviews — is: BUILD THE TELEMETRY BEFORE THE ENFORCEMENT.

So this is a MEASUREMENT instrument, not a gate. It blocks nothing. It produces
the denominator that macro-anchor never had, so that when the #51 re-eval lands
the verdict is computed rather than argued.

WHAT IT MEASURES
----------------
1. BASELINE cohort  — every detector line in the corpus (the pre-#51 population).
                      Expected compliance ~0; this is the fresh-session audit's job,
                      NOT mine (I authored them; a self-sweep is self-correlated).
2. NEW cohort       — detectors ADDED in commits after #51 shipped. This is the
                      cohort #51 actually binds, and the only one whose compliance
                      says whether the standard is live or decorative.
3. BOILERPLATE test — distinct "goes blind if" clause texts / total. A standard
                      whose clauses all read the same is being typed, not applied.

USAGE
  python3 blind_check_audit.py                 # report to stdout
  python3 blind_check_audit.py --ledger        # also append a dated reading
  python3 blind_check_audit.py --baseline REF  # override the #51-ship commit

KNOWN LIMITS (stated, not hidden — this instrument has its own blind-check)
  - Detector patterns are regex. Detectors written as prose or inside table cells
    are NOT counted. That is the denominator-shrinkage failure mode: the ratio can
    rise because the scanner stopped seeing detectors, not because compliance rose.
    `--show-unmatched` dumps near-misses so the gap is inspectable, not silent.
  - .py FIXED 2026-08-02: the original version scanned *.md only. #51's own
    blind-check had explicitly predicted "goes blind if ... hook criteria living in
    .py docstrings" — and that blindness fired within 24 hours, when
    harness_supervisor.py shipped two compliant detectors the scanner could not see
    and the NEW cohort read a false 0/0. First live proof that a blind-check earns
    its keep: the failure was predicted in writing before it happened.
  - NEW-cohort adjacency is computed over ADDED diff lines only. A blind-check
    added in a later commit than its detector reads as non-compliant.
"""
import argparse, re, subprocess, sys, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CORPUS = REPO / "research"
SHIP_COMMIT = "0c9cad1"          # commit where Principle #51 shipped
LEDGER = CORPUS / "meta" / "blind-check-ledger.md"
LOOKAHEAD = 4                     # lines after a detector in which a blind-check counts

DETECTOR = re.compile(
    r"^\s*[-*#0-9.]*\s*\**(Falsifier|Falsifiers|Kill criterion|Retirement trigger"
    r"|Re-eval trigger|Falsification condition)\**\s*[:(]", re.I)
BLIND = re.compile(r"blind-?check\s*:", re.I)
GOES_BLIND = re.compile(r"goes blind if\s*(.+?)\s*[.·]?\s*$", re.I)
# lines that look like a detector but the strict pattern misses — denominator-shrinkage watch
NEAR_MISS = re.compile(r"\b(falsifi|kill criterion|retirement trigger|re-eval)\w*\b", re.I)

# The template/definition sites define the standard; counting them as compliant
# detectors would inflate the ratio with the standard's own documentation.
EXCLUDE = {"meta/methodology.md", "CLAUDE.md", "meta/tools/blind_check_audit.py",
           "meta/blind-check-ledger.md"}


def _rel(p):
    return str(p.relative_to(CORPUS))


def _excluded(rel):
    return any(rel == e or rel.endswith("/" + e) for e in EXCLUDE)


def scan_tree(show_unmatched=False):
    """BASELINE cohort: every detector line currently in the corpus."""
    total = compliant = 0
    clauses, unmatched = [], []
    # .py included as of 2026-08-02: #51's own blind-check predicted "goes blind if
    # ... hook criteria living in .py docstrings", and that blindness fired within
    # 24h — harness_supervisor.py carried two compliant detectors the scanner missed.
    files = sorted(CORPUS.rglob("*.md")) + sorted(CORPUS.rglob("*.py"))
    for f in files:
        rel = _rel(f)
        if _excluded(rel):
            continue
        try:
            lines = f.read_text(errors="replace").split("\n")
        except Exception:
            continue
        for i, ln in enumerate(lines):
            if DETECTOR.search(ln):
                total += 1
                window = lines[i:i + 1 + LOOKAHEAD]
                if any(BLIND.search(w) for w in window):
                    compliant += 1
                    for w in window:
                        m = GOES_BLIND.search(w)
                        if m:
                            clauses.append(m.group(1).strip().lower())
            elif show_unmatched and NEAR_MISS.search(ln) and not BLIND.search(ln):
                unmatched.append(f"{rel}:{i+1}")
    return total, compliant, clauses, unmatched


def scan_new(baseline):
    """NEW cohort: detectors added in commits after #51 shipped."""
    try:
        diff = subprocess.run(
            # covers .md and .py alike — the diff is path-scoped, not extension-scoped
            ["git", "diff", f"{baseline}..HEAD", "--unified=0", "--", "research/"],
            cwd=REPO, capture_output=True, text=True, timeout=60).stdout
    except Exception as e:
        return None, None, [], f"git diff failed: {e}"

    added = [l[1:] for l in diff.split("\n")
             if l.startswith("+") and not l.startswith("+++")]
    total = compliant = 0
    clauses = []
    for i, ln in enumerate(added):
        if DETECTOR.search(ln):
            total += 1
            window = added[i:i + 1 + LOOKAHEAD]
            if any(BLIND.search(w) for w in window):
                compliant += 1
                for w in window:
                    m = GOES_BLIND.search(w)
                    if m:
                        clauses.append(m.group(1).strip().lower())
    return total, compliant, clauses, None


def pct(n, d):
    return "n/a" if not d else f"{100.0 * n / d:.1f}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", action="store_true")
    ap.add_argument("--baseline", default=SHIP_COMMIT)
    ap.add_argument("--show-unmatched", action="store_true")
    a = ap.parse_args()

    b_tot, b_ok, b_cl, unmatched = scan_tree(a.show_unmatched)
    n_tot, n_ok, n_cl, err = scan_new(a.baseline)

    distinct = len(set(n_cl)) if n_cl else 0
    boiler = "n/a" if not n_cl else f"{distinct}/{len(n_cl)} distinct"

    print("BLIND-CHECK COMPLIANCE (Principle #51) — computed, not recalled")
    print(f"  baseline ref            : {a.baseline} (#51 ship commit)")
    print(f"  BASELINE cohort         : {b_ok}/{b_tot} compliant  ({pct(b_ok, b_tot)})")
    print(f"                            -> the fresh-session audit's scope, NOT self-swept")
    if err:
        print(f"  NEW cohort              : ERROR {err}")
    else:
        print(f"  NEW cohort (post-#51)   : {n_ok}/{n_tot} compliant  ({pct(n_ok, n_tot)})")
        print(f"                            -> the ONLY cohort #51 binds")
        print(f"  boilerplate test        : {boiler} 'goes blind if' clauses")
    if a.show_unmatched:
        print(f"  scanner near-misses     : {len(unmatched)} "
              f"(denominator-shrinkage watch; first 10 below)")
        for u in unmatched[:10]:
            print(f"      {u}")

    print()
    print("  PRE-REGISTERED THRESHOLDS (set 2026-08-02, BEFORE the data existed):")
    print("    re-eval 2026-08-24 monthly audit.")
    print("    NEW-cohort compliance >=80% AND distinct-clause ratio >=0.5 -> #51 is live, keep unhooked.")
    print("    NEW-cohort compliance  <80%                                 -> #51 is not self-enforcing:")
    print("                                                                   hook it or retire it. No third option.")
    print("    distinct-clause ratio  <0.5                                 -> clauses are boilerplate -> decorative.")
    print("    NEW cohort N<5 at re-eval                                   -> sample too small; ONE extension to")
    print("                                                                   2026-09-24, then decide on whatever N exists.")

    if a.ledger:
        today = datetime.date.today().isoformat()
        row = (f"| {today} | {a.baseline} | {b_ok}/{b_tot} ({pct(b_ok, b_tot)}) | "
               f"{n_ok}/{n_tot} ({pct(n_ok, n_tot)}) | {boiler} |\n")
        if not LEDGER.exists():
            LEDGER.write_text(
                "# Blind-check compliance ledger (Principle #51)\n\n"
                "Append-only dated readings from `meta/tools/blind_check_audit.py`.\n"
                "A MISSING reading is itself a finding — the gap in the date column is the\n"
                "evidence that the re-eval did not happen.\n\n"
                "| date | baseline ref | baseline cohort | NEW cohort (post-#51) | boilerplate test |\n"
                "|---|---|---|---|---|\n")
        with LEDGER.open("a") as fh:
            fh.write(row)
        print(f"\n  ledger appended -> {_rel(LEDGER)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
