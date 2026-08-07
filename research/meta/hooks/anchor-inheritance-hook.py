#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
try:  # shared fire-log helper (house standard, fail-open)
    import sys as _sys_hfl, os as _os_hfl
    _sys_hfl.path.insert(0, _os_hfl.path.dirname(_os_hfl.path.abspath(__file__)))
    from hook_fire_log import log_fire as _log_fire
except Exception:
    def _log_fire(*_a, **_k):
        return ""
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
ANCHOR-INHERITANCE HOOK (Stop) — the N=4 escalation, built rather than promised.

WHY THIS EXISTS
  On 2026-08-07 `macro-anchor-hook` fired FOUR times on chat summaries of work
  that WAS properly anchored in its artifact. Same gap every time: the artifact
  carries the date anchor, the T1/T2/T3 tags and the tie-to-macro; the chat
  restatement carries the findings and drops the scaffolding.

  After fires 1-2 the pattern was booked in day-state with an explicit clause:
    "Escalation on N=4, and the escalation is NOT 'try harder': it is to make
     the chat restatement inherit the artifact's anchor line MECHANICALLY, the
     same way the claim-receipt hook made file-claims inherit the filesystem."

  Fire 4 landed. This is that mechanism. Writing "I will be more careful" would
  have been the hope-based fix the operator rejected on 2026-08-07:
     "there can't be hope in the harness ... it needs to function in a way where
      before any output gets put out to me, every claim has to be verified."

WHAT IT CHECKS — a RELATION, not a presence
  IF   the working tree's most recent commit wrote/updated a cross-source-log
       artifact that itself carries macro anchoring,
  AND  the assistant message is position-relevant (ticker + thesis/position
       markers) and long enough to be a real summary,
  AND  the message does NOT point at any cross-source-log artifact,
  THEN block, and HAND BACK THE EXACT ANCHOR LINE extracted from that artifact.

  The last clause is the whole design. A gate that only says "you forgot" costs
  a retry and relies on recall. A gate that returns the missing line makes
  compliance copy-paste. Enforcement should lower the cost of doing it right,
  not raise the cost of getting it wrong.

RELATION-CHECK NOTE (2026-08-05 N1 audit): the harness's standing weakness is
  that nearly every hook checks PRESENCE (a token appears) rather than RELATION
  (two artifacts agree). This one compares the MESSAGE against the COMMIT. It is
  deliberately in the scarce class.

DELIBERATELY NOT COVERED (stated so the gap stays legible):
  - Whether the anchor is CORRECT. This checks that the message carries the
    artifact's anchoring, not that the anchoring is true. Truth is a verifier's
    job and cannot be settled at a Stop gate.
  - Chat turns with no artifact behind them — nothing to inherit, correctly silent.

Exit codes: 0 pass · 2 block. Fail-open on ANY exception (house standard).
Self-test: python3 anchor-inheritance-hook.py --selftest
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = _REPO_ROOT
ARTIFACT_DIR = "research/signals/cross-source-log/"

# Message is position-relevant: a ticker-ish token AND a thesis/position marker.
TICKER = re.compile(r"\b[A-Z]{2,5}\b")
POSITION_MARKERS = re.compile(
    r"position implication|thesis|bull case|bear case|sizing|weights held|"
    r"P\(bull|P\(bear|NO ACTION|watchlist|tier\b", re.I)

# Message already points at an artifact -> satisfied.
REFERENCES_ARTIFACT = re.compile(
    r"signals/cross-source-log/[0-9]{4}-[0-9]{2}-[0-9]{2}[A-Za-z0-9_.-]*", re.I)

# The artifact carries anchoring worth inheriting.
ANCHOR_IN_ARTIFACT = re.compile(
    r"ties to macro|first-principles read|macro anchor|research-verified|"
    r"\bT1\b|\bT2\b|\bT3\b", re.I)

# Lines we can hand back as the ready-made anchor.
ANCHOR_LINE = re.compile(r"^\*\*Ties to macro.*|^\*\*Macro first-principles anchor.*", re.I | re.M)

MIN_LEN = 600  # below this it is an acknowledgement, not a summary


def in_scope() -> bool:
    return _os.getcwd().startswith(REPO_ROOT)


def _git(*args):
    return subprocess.run(["git", *args], cwd=REPO_ROOT,
                          capture_output=True, text=True, timeout=15).stdout


def recent_anchored_artifacts():
    """Cross-source-log artifacts touched by HEAD that carry anchoring."""
    out = []
    try:
        files = [f for f in _git("show", "--name-only", "--pretty=format:", "HEAD").split("\n")
                 if f.strip().startswith(ARTIFACT_DIR)]
        for f in files:
            p = Path(REPO_ROOT) / f
            if not p.exists():
                continue
            body = p.read_text(encoding="utf-8", errors="replace")
            if ANCHOR_IN_ARTIFACT.search(body):
                m = ANCHOR_LINE.search(body)
                out.append((f, m.group(0).strip() if m else ""))
    except Exception:
        return []
    return out


def evaluate(text: str, artifacts):
    """Returns list of (path, anchor_line) that the message failed to inherit."""
    if len(text) < MIN_LEN:
        return []
    if not artifacts:
        return []
    if not (TICKER.search(text) and POSITION_MARKERS.search(text)):
        return []
    if REFERENCES_ARTIFACT.search(text):
        return []
    return artifacts


def build_message(missing):
    out = ["ANCHOR-INHERITANCE HOOK: this turn committed an ANCHORED artifact, but the",
           "message summarising it does not point at the artifact.",
           "",
           "This is the N=4 escalation registered on 2026-08-07 after macro-anchor-hook",
           "fired three times on the same gap. The artifact is anchored; the summary is not.",
           "",
           "PASTE ONE OF THESE — the line already exists, it just did not travel:", ""]
    for path, anchor in missing:
        out.append(f"  artifact: `{path}`")
        if anchor:
            out.append(f"  its anchor line: {anchor[:300]}")
        out.append("")
    out += ["Satisfied by naming the artifact path in the message (option (e) of",
            "Critical Rule #15), which also satisfies macro-anchor-hook.",
            "",
            "Not a style rule: a summary that cannot be traced to its evidence is the",
            "same defect as L57 — a claim whose backing exists but never travels with it."]
    return "\n".join(out)


def selftest() -> int:
    A = [("research/signals/cross-source-log/2026-08-07-x.md", "**Ties to macro:** demand-side, no constraint change.")]
    long = "x " * 400
    cases = [
        (long + " TWLO thesis. Position implication: NO ACTION.", A, True,
         "anchored artifact + position summary, no path -> block"),
        (long + " TWLO thesis. Position implication: NO ACTION. See `research/signals/cross-source-log/2026-08-07-x.md`.",
         A, False, "path present -> pass"),
        (long + " TWLO thesis. Position implication: NO ACTION.", [], False,
         "no artifact committed -> pass"),
        ("Short ack.", A, False, "too short -> pass"),
        (long + " general chatter with no position content at all.", A, False,
         "not position-relevant -> pass"),
    ]
    ok = True
    for text, arts, want, label in cases:
        got = bool(evaluate(text, arts))
        status = "PASS" if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"  [{status}] {label}  (blocked={got}, expected={want})")
    print("\nSELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if not in_scope():
        sys.exit(0)
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    if data.get("stop_hook_active") is True:
        sys.exit(0)
    tp = data.get("transcript_path", "")
    if not tp or not Path(tp).exists():
        sys.exit(0)
    try:
        text = ""
        for line in reversed(open(tp).readlines()):
            try:
                e = json.loads(line)
            except Exception:
                continue
            msg = e.get("message") or e
            if (msg.get("role") or e.get("role")) != "assistant":
                continue
            c = msg.get("content")
            if isinstance(c, str):
                text = c
                break
            if isinstance(c, list):
                parts = [x.get("text", "") for x in c
                         if isinstance(x, dict) and x.get("type") == "text"]
                if parts:
                    text = "\n".join(parts)
                    break
        if not text or "anchor-inheritance-hook" in text:
            sys.exit(0)
        missing = evaluate(text, recent_anchored_artifacts())
        if not missing:
            sys.exit(0)
        _log_fire("anchor-inheritance-hook", f"FIRE (artifact anchored, summary unlinked; n={len(missing)})")
        print(build_message(missing), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # FAIL OPEN
        try:
            _log_fire("anchor-inheritance-hook", f"ERROR (failed open): {exc}")
        except Exception:
            pass
        sys.exit(0)


if __name__ == "__main__":
    main()
