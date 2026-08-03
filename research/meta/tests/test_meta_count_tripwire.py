#!/usr/bin/env python3
"""PRE-SHIP BACKTEST for meta-count-tripwire-hook.py (built + run 2026-08-03).

WHY THIS FILE EXISTS RATHER THAN A CITATION: the dual-review adjudication
(`meta/redteam/2026-07-20-self-trust-dual-review-adjudication.md`, finding #3)
established that the circulated figure "0 false positives across 108,883 corpus
sentences" is **UNRECEIPTED** — no script, corpus dump, or output was ever
committed, and the number's only occurrences in the repo are its own
restatements. The spec therefore requires the pre-ship backtest to REPRODUCE a
result, not cite that one. This script is that reproduction, and its output is
committed alongside it.

GATE (from the build spec):
  1. MUST catch the origin trigger sentence ("three times today" shape).
  2. AT MOST 1 false positive per 20 legit replayed meta-statements harvested
     from real committed corpus text.

REPLAY FIDELITY — the one methodological choice that matters here:
  A corpus sentence saying "the hook fired twice today" inside a 2026-07-31
  artifact means *2026-07-31*, not the day the backtest runs. Replaying it
  against today's window would manufacture mismatches that the live hook would
  never produce. So each harvested sentence is replayed with **its own file's
  date as `now`**, recovered from the dated filename. Sentences from undated
  files are still harvested but flagged, because their window is unrecoverable
  and any verdict on them is uninterpretable.

Usage: python3 test_meta_count_tripwire.py [-v]
"""
import importlib.util
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
RESEARCH = REPO / "research"
HOOK_PATH = RESEARCH / "meta" / "hooks" / "meta-count-tripwire-hook.py"

spec = importlib.util.spec_from_file_location("tripwire", HOOK_PATH)
tw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tw)

DATE_IN_NAME = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def harvest():
    """Every committed corpus sentence carrying harness-noun + past-window.

    That is the hook's *candidate* population — the set it could possibly fire
    on. Anything outside it is irrelevant to an FP rate, so counting the whole
    corpus as a denominator (as the unreceipted 108,883 figure did) would
    flatter the result by ~3 orders of magnitude.
    """
    out = []
    for f in sorted(RESEARCH.rglob("*.md")):
        rel = str(f.relative_to(RESEARCH))
        if rel.startswith("meta/hooks/") or rel.startswith("meta/tests/"):
            continue                                  # the hook's own docs
        m = DATE_IN_NAME.search(f.name)
        ref = (datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                        12, 0, tzinfo=timezone.utc) if m else None)
        try:
            text = f.read_text(errors="replace")
        except Exception:
            continue
        for sent in tw._sentences(text):
            if tw.HARNESS_NOUN_RE.search(sent) and tw.PAST_WINDOW_RE.search(sent):
                out.append((rel, sent, ref))
    return out


def main():
    verbose = "-v" in sys.argv
    print("=" * 74)
    print("META-COUNT TRIPWIRE — PRE-SHIP BACKTEST (reproduced, not cited)")
    print("=" * 74)

    # ---- GATE 1: must catch the origin shape -------------------------------
    now = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)
    from datetime import date
    truth_today = tw._count_fires(date(2026, 8, 3), date(2026, 8, 3))
    origin = f"The hook fired {(truth_today or 0) + 2} times today."
    v1, d1 = tw.evaluate(origin, None, now=now, skip_tool_exempt=True)
    print(f"\nGATE 1 — origin trigger shape must be CAUGHT")
    print(f"  fixture : {origin!r}")
    print(f"  today's true fire count (computed) : {truth_today}")
    print(f"  verdict : {v1}   -> {'PASS' if v1 == 'block' else 'FAIL'}")
    print(f"  NOTE: the ORIGINAL 2026-07-20 sentence was never committed verbatim")
    print(f"        (the adjudication records the claim, not the string). This is the")
    print(f"        canonical SHAPE — third person, precise count, past window, no")
    print(f"        in-turn computation — not a byte-exact replay of the incident.")
    gate1 = (v1 == "block")

    # ---- GATE 2: FP rate on real committed meta-statements -----------------
    cands = harvest()
    dated = [c for c in cands if c[2] is not None]
    undated = [c for c in cands if c[2] is None]
    blocks = []
    for rel, sent, ref in dated:
        v, d = tw.evaluate(sent, None, now=ref, skip_tool_exempt=True)
        if v == "block":
            blocks.append((rel, sent, d))

    print(f"\nGATE 2 — false positives on REAL committed meta-statements")
    print(f"  candidate population (harness-noun + past-window in one sentence):")
    print(f"    total harvested        : {len(cands)}")
    print(f"    dated (replayable)     : {len(dated)}")
    print(f"    undated (window unrecoverable, EXCLUDED from the rate) : {len(undated)}")
    print(f"  blocks on dated candidates : {len(blocks)}")
    if dated:
        rate = len(blocks) / len(dated) * 20
        print(f"  FP rate                    : {len(blocks)}/{len(dated)}"
              f"  = {rate:.2f} per 20  (gate: <= 1.00 per 20)")
        gate2 = rate <= 1.0
    else:
        rate, gate2 = 0.0, False
        print("  no dated candidates -> gate cannot be evaluated")

    if blocks and verbose:
        print("\n  blocked sentences (inspect these — each is a candidate FP):")
        for rel, sent, d in blocks[:25]:
            print(f"    - {rel}\n      {sent[:150]}")
            if d:
                print(f"      claimed={d[1]} computed={d[2]} kind={d[3]} window={d[4]}..{d[5]}")

    print("\n" + "=" * 74)
    print(f"GATE 1 (catches origin shape) : {'PASS' if gate1 else 'FAIL'}")
    print(f"GATE 2 (<=1 FP per 20)        : {'PASS' if gate2 else 'FAIL'}")
    print(f"SHIP DECISION                 : "
          f"{'CLEARED' if (gate1 and gate2) else 'BLOCKED — do not wire'}")
    print("=" * 74)
    return 0 if (gate1 and gate2) else 1


if __name__ == "__main__":
    sys.exit(main())
