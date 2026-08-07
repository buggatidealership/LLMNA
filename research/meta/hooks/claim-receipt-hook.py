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
CLAIM-RECEIPT HOOK (Stop) — Phase 1 of the receipts layer.

Operator directive 2026-08-07 verbatim-adjacent:
  "There can't be hope in the harness when it comes to [behaviour] that needs
   to happen every single time a certain condition [is met]... you write this
   down, you're hoping that you pull another session, realize it, and do it.
   ...before any output gets put out to me, every claim that you're about to
   make in the output has to be verified."

WHY THIS EXISTS — the L57 case (2026-08-07):
  L57 was cited in session-prime.md, force-injected into every cold session,
  and graded against on 08-06 — while having NO entry in lessons.md and never
  having had one (`git log -S"L57"` empty). It was a CLAIM with no artifact.
  Nothing checked it because nothing could: the only record was my own word.

  The prior write-up concluded "where no postcondition can be defined, the
  claim must not be made in that form." The operator rejected that, correctly:
  a rule in a file is a PROMISE, enforced by hope that a future session reads
  and complies. This hook is the non-hope version. Where a claim class cannot
  be verified, the GATE REFUSES THE CLAIM rather than a document asking nicely.

DESIGN PRINCIPLE:
  A receipt must be a BY-PRODUCT OF THE ACT, not a statement by the actor.
  Each class below pairs a claim pattern with a repo-observable postcondition
  that exists independently of what the message says.

CLASSES ENFORCED (Phase 1 — all three fully deterministic, no judgement):
  C1 ID-CODIFICATION  "L60 codified" / "codified B67" / "TC-20 registered"
                      -> that ID must be present in its canonical file ON DISK.
                      This is exactly the L57 hole.
  C2 FILE-WRITE       "written to `path`" / "artifact: `path`"
                      -> that path must exist ON DISK.
  C3 COMMIT-PUSH      "committed and pushed" / "pushed to origin"
                      -> working tree clean AND HEAD == origin/<branch>.
                      The say-do gap in its purest form.

DELIBERATELY NOT ENFORCED IN PHASE 1 (stated so the gap is legible, per the
enforcement-ledger discipline — an unstated gap is the thing that produced L57):
  - "cascaded to N theses"  -> needs same-commit diff inspection; Phase 2.
  - "verified" / "the verifier returned X" -> needs transcript agent-result
    correlation; Phase 2.
  - Any claim about the outside world (was the number right?) -> NOT
    mechanically checkable at a Stop gate at all; that is a verifier-agent
    job and carries latency this gate cannot absorb. Naming the boundary
    rather than implying total coverage.

EXEMPTIONS (false-positive control — this hook sees every message):
  - Hedged/forward claims: "(to be created)", "(when written)", "will write",
    "not yet written", "planned", "Phase N", "never written", "must be".
  - Placeholder/abbreviated paths: contains "...", "XX", "path/to", "{".
  - Self-reference: messages discussing THIS hook by filename.

Exit codes:
  0 — pass (no unhedged claim, or every claim's postcondition holds)
  2 — block (a claim was made whose receipt does not exist)

Fail-open on ANY exception (house standard): a broken gate must not wedge the
session. Failures are logged, not silent.

Self-test: python3 claim-receipt-hook.py --selftest
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = _REPO_ROOT

CANONICAL = {
    "L":  "research/predictions/lessons.md",
    "B":  "research/meta/biases-watchlist.md",
    "TC": "research/signals/triangulation.md",
    "PC": "research/meta/cross-domain-pattern-register.md",
}

# C1 — an ID asserted as codified/registered/added, in either word order.
_CODIFY_VERB = r"(?:codified|registered|added|shipped|written|booked)"
C1_PATTERNS = [
    re.compile(rf"\b(L|B|TC|PC)[- ]?(\d+)\b[^.\n]{{0,60}}?\b{_CODIFY_VERB}\b", re.I),
    re.compile(rf"\b{_CODIFY_VERB}\b[^.\n]{{0,40}}?\b(L|B|TC|PC)[- ]?(\d+)\b", re.I),
]

# C2 — a file asserted as written, in backticks.
C2_PATTERN = re.compile(
    r"(?:written to|wrote|artifact:|created|new file:)\s*`([A-Za-z0-9_./-]+\.(?:md|py|json))`",
    re.I,
)

# C3 — a commit/push asserted.
C3_PATTERN = re.compile(r"\b(?:committed and pushed|pushed to origin|commit(?:ted)? \+ push(?:ed)?)\b", re.I)

HEDGES = [
    r"\(to be created\)", r"\(when written\)", r"\(never written\)", r"\(not yet",
    r"\bwill (?:write|create|be (?:written|created|codified|registered|added|shipped|booked))\b",
    r"\bnot yet (?:written|created|codified|registered)\b", r"\bto be (?:codified|registered|added)\b",
    r"\bplanned\b", r"\bPhase \d\b", r"\bmust be (?:written|created)\b",
    r"\bwould (?:write|be)\b", r"\bproposed\b", r"\bif written\b",
]
PLACEHOLDER = ("...", "…", "XX", "path/to", "{", "<")


def in_scope() -> bool:
    import os
    return os.getcwd().startswith(REPO_ROOT)


def _read(rel: str) -> str:
    try:
        return (Path(REPO_ROOT) / rel).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def _hedged_near(text: str, idx: int, window: int = 260) -> bool:
    """A claim is exempt if a hedge sits in the same neighbourhood."""
    seg = text[max(0, idx - window): idx + window]
    return any(re.search(h, seg, re.I) for h in HEDGES)


def check_c1(text: str):
    """ID asserted as codified -> must be present in its canonical file."""
    bad = []
    seen = set()
    for pat in C1_PATTERNS:
        for m in pat.finditer(text):
            ns, num = m.group(1).upper(), m.group(2)
            key = f"{ns}{num}"
            if key in seen:
                continue
            seen.add(key)
            if _hedged_near(text, m.start()):
                continue
            body = _read(CANONICAL[ns])
            if not body:
                continue  # canonical file unreadable -> fail open on this item
            token = rf"\b{ns}-?{num}\b" if ns in ("TC", "PC") else rf"\b{ns}{num}\b"
            if not re.search(token, body):
                bad.append((key, CANONICAL[ns]))
    return bad


def check_c2(text: str):
    """File asserted as written -> must exist."""
    bad = []
    for m in C2_PATTERN.finditer(text):
        p = m.group(1)
        if any(t in p for t in PLACEHOLDER):
            continue
        if _hedged_near(text, m.start()):
            continue
        root = Path(REPO_ROOT)
        if any((root / c).exists() for c in (p, f"research/{p}", f"research/meta/{p}")):
            continue
        # bare filename anywhere in the repo also counts as resolved
        name = Path(p).name
        try:
            if next(root.rglob(name), None) is not None:
                continue
        except Exception:
            continue
        bad.append(p)
    return bad


def check_c3(text: str):
    """Commit+push asserted -> tree clean AND HEAD == its upstream."""
    if not C3_PATTERN.search(text):
        return None
    m = C3_PATTERN.search(text)
    if m and _hedged_near(text, m.start()):
        return None
    try:
        st = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT,
                            capture_output=True, text=True, timeout=15)
        dirty = [l for l in st.stdout.splitlines() if l.strip()]
        rev = subprocess.run(["git", "rev-parse", "HEAD", "@{u}"], cwd=REPO_ROOT,
                             capture_output=True, text=True, timeout=15)
        parts = rev.stdout.split()
        if rev.returncode != 0 or len(parts) < 2:
            return None  # no upstream -> cannot verify -> fail open
        if parts[0] != parts[1]:
            return "HEAD does not match its upstream — the push did not land"
        if dirty:
            return f"{len(dirty)} uncommitted change(s) remain: " + ", ".join(d[3:] for d in dirty[:4])
    except Exception:
        return None
    return None


def build_message(c1, c2, c3):
    out = ["CLAIM-RECEIPT HOOK: your message asserts something whose receipt does not exist.",
           "", "A claim is only allowed if the artifact it names can be observed independently", "of the claim itself.", ""]
    if c1:
        out.append("UNBACKED CODIFICATION CLAIM(S) — the ID is not in its canonical file:")
        for key, path in c1:
            out.append(f"  - {key} asserted as codified, but absent from {path}")
        out += ["", "  This is the L57 failure exactly: an ID that lives in a summary or in prose",
                "  while the canonical entry was never written.",
                "  FIX: write the canonical entry now, or state the claim as pending.", ""]
    if c2:
        out.append("UNBACKED FILE-WRITE CLAIM(S) — the path does not exist:")
        for p in c2:
            out.append(f"  - {p}")
        out += ["", "  FIX: write the file, correct the path, or mark it '(to be created)'.", ""]
    if c3:
        out += ["UNBACKED COMMIT/PUSH CLAIM:", f"  - {c3}", "",
                "  FIX: actually commit and push, then restate.", ""]
    out += ["Exemptions that pass cleanly: '(to be created)', '(when written)',",
            "'not yet written', 'planned', 'Phase N'. Saying a thing is UNDONE is",
            "always allowed. Only asserting it is DONE requires the receipt."]
    return "\n".join(out)


def run(text: str):
    c1, c2, c3 = check_c1(text), check_c2(text), check_c3(text)
    return c1, c2, c3


def selftest() -> int:
    cases = [
        # (text, should_block, label)
        ("L60 codified today and it holds.", False, "L60 exists -> pass"),
        ("L999 codified today.", True, "L999 absent -> block"),
        ("L999 will be codified later.", False, "hedged -> pass"),
        ("A new lesson L998 is proposed, not yet written.", False, "hedged 'not yet written' -> pass"),
        ("Artifact: `research/meta/day-state.md`", False, "existing file -> pass"),
        ("Artifact: `research/meta/definitely-not-here.md`", True, "missing file -> block"),
        ("See `meta/foo-plan.md` (to be created)", False, "explicit hedge -> pass"),
        ("Referenced `signals/...-abbrev.md` in passing", False, "placeholder -> pass"),
        ("Nothing asserted here at all.", False, "no claim -> pass"),
    ]
    ok = True
    for text, want, label in cases:
        c1, c2, c3 = run(text)
        got = bool(c1 or c2 or c3)
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
                parts = [x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text"]
                if parts:
                    text = "\n".join(parts)
                    break
        if not text:
            sys.exit(0)
        # never fire on messages about this hook itself
        if "claim-receipt-hook" in text:
            sys.exit(0)
        c1, c2, c3 = run(text)
        if not (c1 or c2 or c3):
            sys.exit(0)
        _log_fire("claim-receipt-hook", f"FIRE c1={len(c1)} c2={len(c2)} c3={bool(c3)}")
        print(build_message(c1, c2, c3), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # FAIL OPEN — a broken gate must not wedge the session
        try:
            _log_fire("claim-receipt-hook", f"ERROR (failed open): {exc}")
        except Exception:
            pass
        sys.exit(0)


if __name__ == "__main__":
    main()
