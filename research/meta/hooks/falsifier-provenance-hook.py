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
FALSIFIER-PROVENANCE — the harness's first RELATION check (added 2026-08-05).

Enforces Critical Rule #8: never sell on a macro headwind without a written
thesis falsifier firing. Postcondition form (N1, per
meta/redteam/2026-08-05-N1-postconditions-presence-vs-relation.md #8):

    every EXIT/TRIM names a falsifier that is LITERALLY PRESENT in that
    ticker's companies/{TICKER}/thesis.md falsifier block

WHY THIS ONE, AND WHY IT IS DIFFERENT FROM EVERY OTHER HOOK HERE

The N1 audit classified all 24 Critical-Rule clauses as PRESENCE (a token
appears in the output) or RELATION (two things in the output agree). It then
crossed that against the N3 probe and found:

    PRESENCE clauses with a probe-verified hook :  3
    RELATION clauses with a probe-verified hook :  0

Every hook the harness can prove is running checks that a token EXISTS. Not one
checks that two things AGREE. And all eight errors of 2026-08-05 were produced
with every required token present and a false relation underneath — the numbers
were cited, the claims were tagged, the cascades carried their order markers.
Citation is a presence property; comparability is a relation property; the
enforcement layer only had instruments for the first.

This hook closes exactly one relation, on the highest-stakes line the harness
produces: the one that moves real money out of a position.

WHY NOT #12 (the two-dates check), which the audit ranked FIRST

Because a relation check needs BOTH OPERANDS TO EXIST before it can compare
them, and a corpus backtest killed it: of 473 cross-source-log files, 247 name
an aggregator-class source and 244 of those (99%) record no separate date for
the underlying primary claim. The check would fire on essentially everything —
a wall, not a check — and would degrade into a presence demand for a convention
nobody follows. That is a real ordering constraint the N1 artifact missed:
   PRESENCE OF BOTH OPERANDS IS A PREREQUISITE FOR RELATION CHECKING.
Presence checks are not worthless. They are the floor a relation check stands
on. #12 needs a convention first; #8 does not, because both of its operands are
already written down.

WHAT IT DETECTS

  TRIGGER: an assistant message containing a Position implication line whose
  action is EXIT or TRIM, for a ticker with a companies/{TICKER}/thesis.md.

  PASS: the message names a falsifier, and enough of the named falsifier's
  distinctive words appear in that thesis's falsifier block for the reference
  to be real.

  FIRE: the message says EXIT or TRIM and either names no falsifier at all, or
  names one whose language does not appear in the thesis it claims to come
  from. The second case is the interesting one — a fabricated citation, in the
  position layer rather than the number layer.

FALSE-POSITIVE CONTROL. The trigger population is deliberately narrow: 15
EXIT/TRIM lines across 825 position-implication lines in 94 thesis files at
build time. Rare by construction. HOLD, NO ACTION and ENTER never trigger it —
Rule #8 is about exits.

BLIND-CHECK (Principle #51). Distinguishes a falsifier grounded in the thesis
from one invented at exit time · reads on word overlap between the cited
falsifier and the thesis falsifier block · GOES BLIND IF exits stop being
written as Position implication lines (a prose exit, an exit stated only in
portfolio/changes.md, or an exit the operator makes without my writing one) —
in which case it reads clean forever while the discipline rots. It is a check
on my own output, so it cannot see any decision that never passed through it.

RETIREMENT. If this fires zero times in 90 days it is not automatically inert:
the trigger population is genuinely rare, so a zero-fire quarter is consistent
with a quarter of no exits. Retire only if it fires zero times ACROSS A QUARTER
CONTAINING >=3 EXIT/TRIM lines — that would mean the discipline is being met
without it, or the detector cannot see.

Scope: only inside the research OS repo. Exit 0 outside.
"""

import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = _REPO_ROOT
COMPANIES = Path(REPO_ROOT) / "research" / "companies"

# The exit-class Position implication line. HOLD/NO ACTION/ENTER are out of
# scope — Critical Rule #8 governs selling.
EXIT_LINE = re.compile(
    r"Position implication:\s*\**\s*(EXIT|TRIM)\b(?P<rest>[^\n]*)", re.I)

# A ticker mentioned anywhere in the message that we actually hold a thesis for.
TICKER = re.compile(r"\b([A-Z]{2,5})\b")

# The message claims a falsifier fired.
FALSIFIER_CLAIM = re.compile(
    r"falsifier[^.\n]{0,160}|fires?\s+falsifier|falsif(?:ies|ied|ication)"
    r"[^.\n]{0,160}", re.I)

# Meta-discussion exemption. This hook, its own documentation, and the audit
# artifacts all quote Position implication lines; they must not trip it.
# NOTE: deliberately does NOT include the bare word "hook" — during the probe
# build on 2026-08-05 a padding string containing "hooks" silently disarmed
# seven hooks at once. Exemptions here are anchored to file paths and IDs.
META = re.compile(
    r"falsifier-provenance-hook|meta/redteam/|meta/hooks/|\.py\b|"
    r"postcondition_audit|hook_probe|N1-postconditions", re.I)

MIN_OVERLAP = 3   # distinctive words the cited falsifier must share with the thesis


def in_scope() -> bool:
    return os.getcwd().startswith(REPO_ROOT)


def get_last_assistant_message(transcript_path: str) -> str:
    try:
        with open(transcript_path) as f:
            lines = f.readlines()
    except (FileNotFoundError, PermissionError):
        return ""
    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = entry.get("message") or entry
        if (msg.get("role") or entry.get("role")) != "assistant":
            continue
        content = msg.get("content")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = [c.get("text", "") for c in content
                     if isinstance(c, dict) and c.get("type") == "text"]
            if parts:
                return "\n".join(parts)
    return ""


STOP = set("""the a an and or of to in for on with is are was were be been it its
this that these those at as by from not no than then when if which what who how
would could should will may might must can thesis falsifier falsifiers position
implication case bull bear base tier target price stock name company""".split())


def distinctive(text):
    """Content words, lowercased, stopwords and pure numbers dropped."""
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in STOP}


def thesis_falsifier_block(ticker):
    """The falsifier section of a thesis, or None if the thesis has none."""
    f = COMPANIES / ticker / "thesis.md"
    if not f.exists():
        return None
    try:
        t = f.read_text(errors="replace")
    except OSError:
        return None
    m = re.search(r"^#+\s*Falsifiers?\b(.*?)(?=^#+\s|\Z)", t,
                  re.M | re.S | re.I)
    return m.group(1) if m else None


def main():
    if not in_scope():
        sys.exit(0)
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    text = get_last_assistant_message(data.get("transcript_path", "") or "")
    if not text:
        sys.exit(0)
    if META.search(text):
        sys.exit(0)

    exits = list(EXIT_LINE.finditer(text))
    if not exits:
        sys.exit(0)

    # Which held names does this message actually talk about?
    known = {t for t in TICKER.findall(text)
             if (COMPANIES / t / "thesis.md").exists()}
    if not known:
        sys.exit(0)

    claims = " ".join(m.group(0) for m in FALSIFIER_CLAIM.finditer(text))
    action = exits[0].group(1).upper()

    if not claims.strip():
        reason = (f"{action} stated with NO falsifier named at all. Critical "
                  f"Rule #8: sell only when a WRITTEN thesis falsifier fires.")
    else:
        cited = distinctive(claims)
        best, best_n = None, -1
        for t in sorted(known):
            block = thesis_falsifier_block(t)
            if block is None:
                continue
            n = len(cited & distinctive(block))
            if n > best_n:
                best, best_n = t, n
        if best is None:
            reason = (f"{action} stated for {', '.join(sorted(known))}, but no "
                      f"thesis carries a Falsifiers section to have fired.")
        elif best_n >= MIN_OVERLAP:
            sys.exit(0)   # the relation holds — the cited falsifier is really there
        else:
            reason = (f"{action} names a falsifier, but its language does not "
                      f"appear in {best}'s thesis falsifier block "
                      f"(overlap {best_n} < {MIN_OVERLAP} distinctive words). "
                      f"The falsifier may have been composed at exit time "
                      f"rather than fired.")

    msg = [
        "FALSIFIER-PROVENANCE HOOK (RELATION check): exit-class position",
        "implication without a grounded falsifier.",
        "",
        f"  {reason}",
        "",
        "This is not a presence check. It is not asking you to mention a",
        "falsifier — it is asking that the falsifier you name be one that is",
        "LITERALLY WRITTEN in that ticker's thesis.md Falsifiers block, from",
        "before this decision. A falsifier composed at exit time is a",
        "rationalisation with a citation format.",
        "",
        "Required action, one of:",
        "  - quote the thesis falsifier that fired, by its number, in the",
        "    same words the thesis uses",
        "  - if no written falsifier fired, say so and DO NOT exit on macro",
        "    (Critical Rule #8) — or amend the thesis first, in this commit,",
        "    and exit on the amended falsifier",
        "",
        "See: research/CLAUDE.md Critical Rule #8 · B9 (emotional risk-",
        "management as prudence) · meta/redteam/2026-08-05-N1-postconditions-",
        "presence-vs-relation.md #8",
    ]
    print("\n".join(msg), file=sys.stderr)
    _log_fire("falsifier-provenance-hook", "FIRE",
              detail=f"Rule#8 {action} without grounded falsifier")
    sys.exit(2)


if __name__ == "__main__":
    main()
