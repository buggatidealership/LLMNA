#!/usr/bin/env python3
import os as _os
from pathlib import Path as _Path
_REPO_ROOT = _os.environ.get("CLAUDE_PROJECT_DIR") or str(_Path(__file__).resolve().parents[3])
"""
META-COUNT TRIPWIRE — Stop hook (built 2026-08-03 on the self-set schedule).

WHAT THIS IS, HONESTLY: a **TRIPWIRE**. Low false-positive, LOW RECALL. It is
NOT the fix for harness-history miscounting. It catches one narrow, high-damage
shape — a *precise* count about the harness's own recent activity, stated with
no computation in the same turn — and recomputes it from the source of record.
Items 1a (log_fire house-standard rollout) + 1b (receipts hook proper) remain
the real fix; this is the cheap backstop that fires when they have not.

ORIGIN (2026-07-20): "three times today" — two real hook fires blended with a
13-day-old priming episode into a confident false count, stated to the operator
as fact, caught only by an operator question. Codified as #43b clause 3f / B65
context-fluency, and as priming item 11.

SPEC (dual-review merged; `meta/redteam/2026-07-20-self-trust-dual-review-adjudication.md`
row "1c", and `meta/hooks/receipts-hook-spec.md` check #2 — 1c is SUBSUMED as
that hook's count-leg and joins at 08-03, gated on 2 weeks of fire-log data):
  trigger  = COUNT-WORD + HARNESS-NOUN + PAST-WINDOW token in ONE sentence.
             **NO first-person requirement** — fresh-Claude's finding was that
             FP was never the problem; RECALL was, because the first-person
             anchor missed the dominant third-person phrasing ("the hook fired
             three times today").
  action   = recompute from the SOURCE OF RECORD and block on mismatch, with
             the computed truth in the feedback.
  fail-open= source missing / unparseable / git unavailable / any exception.
  exempt   = a computing tool call in the SAME turn (the claim was computed,
             which is exactly the behaviour item 11 asks for).

PRECONDITION VERIFIED AT BUILD TIME (2026-08-03): anti-fabrication-hook entries
in meta/hook-fire-log.md span 2026-07-20 -> 2026-08-03 = 14 days, 45 entries.
The 2-week data dependency is met **exactly at the boundary**, not comfortably.

BACKTEST: `meta/tests/test_meta_count_tripwire.py` — run and its output
committed. NOTE: the previously-circulated "0 FPs across 108,883 corpus
sentences" figure is UNRECEIPTED (no script or output was ever committed; see
the adjudication artifact's own finding #3). This build REPRODUCES a backtest
rather than citing that number.

FALSIFIERS (registered at ship time):
  - >2 logged FALSE POSITIVES in 30 days  -> retire (trigger is too loose).
  - 0 catches AND 0 FPs in 90 days        -> decorative -> retire.
  - Blocks that are all self-referential (this hook discussing itself)
                                          -> exemption list is wrong, tighten.

Blind-check (Principle #51):
  distinguishes "a fabricated harness count" from "a correct harness count"
  · reads on meta/hook-fire-log.md line counts and `git rev-list --count`
  · GOES BLIND IF the claim is about a quantity with no source of record —
    agents spawned, wakes, routine firings, tokens spent. Those nouns trigger
    nothing and are allowed through by design, so the tripwire's silence is
    NOT evidence a count is correct. It covers fires and commits. Nothing else.

Testing:
  python3 meta-count-tripwire-hook.py < /dev/null   -> exit 0 (fail-open)
  python3 meta-count-tripwire-hook.py --selftest    -> fixture suite
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from hook_fire_log import log_fire
except Exception:                                        # pragma: no cover
    def log_fire(*a, **k):
        return None

HOOK = "meta-count-tripwire-hook"
FIRE_LOG = Path(_REPO_ROOT) / "research" / "meta" / "hook-fire-log.md"

NUM_WORDS = {
    "once": 1, "twice": 2, "thrice": 3,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}

# --- trigger: the count must be BOUND to the noun, not merely co-present ----
# v2 (2026-08-03, pre-ship): v1 used bag-of-features (count-word ANYWHERE +
# harness-noun ANYWHERE + window ANYWHERE in the sentence) and FAILED GATE 2 at
# 2.30 FP per 20 (gate <=1.00). Every FP had one root cause: the number was
# scavenged from elsewhere in the sentence -- "Rule #19 HIGH" -> 19, "$29.4B" ->
# 29, "20:17Z EOD fire" -> 20, "§8 B40.x discipline fires today" -> 8. v2
# requires an explicit CLAIM PHRASE in which the number sits adjacent to the
# thing being counted. Lower recall, and that is the correct trade for a
# TRIPWIRE.
_N = r"(?:(\d{1,3})|(" + "|".join(NUM_WORDS) + r"))"
_UNIT_TAIL = r"(?![\d,.:%xX]|\s*(?:bn|tn|B\b|M\b|K\b|Z\b|%|월|조|억))"
_MONEY_HEAD = r"(?<![$€£¥§#\d.,\-])"

CLAIM_PATTERNS = [
    re.compile(_MONEY_HEAD + r"\bfir(?:ed|es|ing)\s+(?:it\s+)?" + _N + _UNIT_TAIL + r"\s+times?\b", re.I),
    re.compile(_MONEY_HEAD + r"\b" + _N + _UNIT_TAIL + r"\s+(?:hook\s+)?fires\b", re.I),
    re.compile(_MONEY_HEAD + r"\b(?:committ?ed|pushed)\s+" + _N + _UNIT_TAIL + r"\s+times?\b", re.I),
    re.compile(_MONEY_HEAD + r"\b" + _N + _UNIT_TAIL + r"\s+commits?\b", re.I),
    re.compile(_MONEY_HEAD + r"\b" + _N + _UNIT_TAIL + r"\s+pushe?s\b", re.I),
    re.compile(r"\bfir(?:ed|es)\s+(once|twice|thrice)\b", re.I),
    re.compile(r"\b(?:committ?ed|pushed)\s+(once|twice|thrice)\b", re.I),
]
HARNESS_NOUN_RE = re.compile(
    r"\b(hooks?|fired?|fires|firing|commits?|committed|pushe?[sd]?|"
    r"agents?|wakes?|routines?)\b", re.I)
PAST_WINDOW_RE = re.compile(
    r"\b(today|tonight|this session|this turn|this morning|this evening|"
    r"this week|so far today|yesterday|in the last \d+\s*(?:hours?|days?))\b", re.I)

# --- exemptions (kept deliberately generous — this is a TRIPWIRE) -------
HEDGE_RE = re.compile(
    r"(~|≈|about |roughly |approximately |at least |more than |fewer than |"
    r"over |under |around |up to |or so|estimate|order of|no more than)", re.I)
META_SELF_RE = re.compile(
    r"(tripwire|selftest|backtest|fixture|falsifier|this hook|the hook itself|"
    r"meta-count|\.py\b|regex|exit code|spec\b)", re.I)
QUOTE_RE = re.compile(r"^\s*[>\"'`]|\bsaid\b|\bclaimed\b|\bwrote\b|\bper \w+\b", re.I)
# INLINE-QUOTED claim: any post-mortem discussing a past miscount quotes the bad
# sentence verbatim ("the hook fired three times today"). Caught in the pre-ship
# backtest against the dual-review artifact — the tripwire fired on the very
# incident write-up it was built from. A claim wholly inside quote marks or
# backticks is someone else's sentence, not this turn's assertion.
INLINE_QUOTED_RE = re.compile(r"[\"\u201c\u2018'`]([^\"\u201d\u2019'`]{0,200})[\"\u201d\u2019'`]")


def _inside_quotes(sentence, span_text):
    for m in INLINE_QUOTED_RE.finditer(sentence):
        if span_text.lower() in m.group(1).lower():
            return True
    return False

# noun class -> source of record
FIRE_NOUNS = re.compile(r"\b(hooks?|fired?|fires|firing)\b", re.I)
COMMIT_NOUNS = re.compile(r"\b(commits?|committed|pushe?[sd]?)\b", re.I)
# NO source of record — allowed through by design (see blind-check)
UNSOURCED_NOUNS = re.compile(r"\b(agents?|wakes?|routines?)\b", re.I)

HOOK_NAME_RE = re.compile(
    r"\b([a-z][a-z0-9-]*-hook|git-guard[a-z-]*|anti-fabrication|macro-anchor|"
    r"structural-output|session-prime|session-start|cascade-enforcement)\b", re.I)


def _sentences(text):
    for para in text.split("\n"):
        for s in re.split(r"(?<=[.!?;])\s+", para):
            s = s.strip()
            if s:
                yield s


def _extract_count(sentence):
    """Return an int iff exactly ONE claim-phrase binds a number to a counted noun."""
    found = []
    for pat in CLAIM_PATTERNS:
        for m in pat.finditer(sentence):
            g = [x for x in m.groups() if x]
            if not g:
                continue
            tok = g[0]
            if tok.isdigit():
                found.append(int(tok))
            elif tok.lower() in NUM_WORDS:
                found.append(NUM_WORDS[tok.lower()])
    uniq = set(found)
    # ambiguity -> allow (tripwire discipline: never guess which number is the claim)
    return found[0] if len(uniq) == 1 and found else None


def _window_bounds(sentence, now=None):
    now = now or datetime.now(timezone.utc)
    s = sentence.lower()
    if "yesterday" in s:
        d = (now - timedelta(days=1)).date()
        return d, d
    m = re.search(r"in the last (\d+)\s*days?", s)
    if m:
        return (now - timedelta(days=int(m.group(1)))).date(), now.date()
    if "this week" in s:
        return (now - timedelta(days=7)).date(), now.date()
    # today / tonight / this session / this morning / this turn / so far today
    return now.date(), now.date()


def _count_fires(lo, hi, hook_filter=None):
    if not FIRE_LOG.exists():
        return None                                   # fail-open: no source
    txt = FIRE_LOG.read_text(errors="replace")
    n = 0
    for line in txt.split("\n"):
        m = re.match(r"^- (\d{4}-\d{2}-\d{2})[T ][\d:]+Z?\s+(\S+)", line)
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if not (lo <= d <= hi):
            continue
        if hook_filter and hook_filter not in m.group(2):
            continue
        n += 1
    return n


def _count_commits(lo, hi):
    try:
        r = subprocess.run(
            ["git", "rev-list", "--count", "HEAD",
             f"--since={lo.isoformat()} 00:00", f"--until={hi.isoformat()} 23:59"],
            cwd=_REPO_ROOT, capture_output=True, text=True, timeout=15)
        if r.returncode != 0:
            return None                               # fail-open
        return int(r.stdout.strip())
    except Exception:
        return None


def _tool_used_this_turn(transcript_path):
    """Exemption: a computing tool call in the same turn means the number WAS
    computed — the behaviour item 11 asks for. Fail-open (True) if unreadable."""
    try:
        p = Path(transcript_path)
        if not p.exists():
            return True
        lines = p.read_text(errors="replace").strip().split("\n")
        # walk back to the previous user turn; look for tool_use in between
        for raw in reversed(lines[-400:]):
            try:
                ev = json.loads(raw)
            except Exception:
                continue
            role = (ev.get("message") or {}).get("role") or ev.get("type")
            content = json.dumps((ev.get("message") or {}).get("content", ""))
            if role == "user" and "tool_result" not in content:
                return False                          # reached the user turn, no tool seen
            if '"type":"tool_use"' in content.replace(" ", "") or "tool_use" in content:
                if re.search(r'"name"\s*:\s*"(Bash|Grep|Read|Glob)"', content):
                    return True
        return False
    except Exception:
        return True                                   # fail-open


def evaluate(text, transcript_path=None, now=None, skip_tool_exempt=False):
    """Return (verdict, detail). verdict: 'pass' | 'block'."""
    for sent in _sentences(text):
        if not (HARNESS_NOUN_RE.search(sent) and PAST_WINDOW_RE.search(sent)):
            continue
        if HEDGE_RE.search(sent) or META_SELF_RE.search(sent) or QUOTE_RE.search(sent):
            continue
        if UNSOURCED_NOUNS.search(sent) and not (
                FIRE_NOUNS.search(sent) or COMMIT_NOUNS.search(sent)):
            continue                                  # no source of record -> allow
        claimed = _extract_count(sent)
        if claimed is None:
            continue
        if any(_inside_quotes(sent, m.group(0))
               for pat in CLAIM_PATTERNS for m in pat.finditer(sent)):
            continue                                  # quoted claim -> not this turn's assertion
        lo, hi = _window_bounds(sent, now)
        if COMMIT_NOUNS.search(sent):
            truth, kind = _count_commits(lo, hi), "commits"
        elif FIRE_NOUNS.search(sent):
            hm = HOOK_NAME_RE.search(sent)
            truth = _count_fires(lo, hi, hm.group(1).lower() if hm else None)
            kind = f"fires{' (' + hm.group(1) + ')' if hm else ''}"
        else:
            continue
        if truth is None:
            continue                                  # fail-open: source missing
        if not skip_tool_exempt and transcript_path and _tool_used_this_turn(transcript_path):
            continue                                  # computed in-turn -> exempt
        if claimed != truth:
            return "block", (sent, claimed, truth, kind, lo, hi)
    return "pass", None


def main():
    if "--selftest" in sys.argv:
        return selftest()
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return 0
        payload = json.loads(raw)
    except Exception:
        return 0                                      # fail-open

    try:
        tpath = payload.get("transcript_path")
        text = ""
        if tpath and Path(tpath).exists():
            lines = Path(tpath).read_text(errors="replace").strip().split("\n")
            for raw_line in reversed(lines):
                try:
                    ev = json.loads(raw_line)
                except Exception:
                    continue
                msg = ev.get("message") or {}
                if msg.get("role") == "assistant":
                    c = msg.get("content")
                    if isinstance(c, list):
                        text = "\n".join(b.get("text", "") for b in c
                                         if isinstance(b, dict) and b.get("type") == "text")
                    elif isinstance(c, str):
                        text = c
                    break
        if not text:
            return 0

        verdict, detail = evaluate(text, tpath)
        if verdict == "block":
            sent, claimed, truth, kind, lo, hi = detail
            log_fire(HOOK, "FIRE", f"claimed={claimed} truth={truth} kind={kind}")
            print(
                f"META-COUNT TRIPWIRE: a harness-history count in this message does not "
                f"match the source of record.\n\n"
                f"  sentence : {sent[:300]}\n"
                f"  claimed  : {claimed}\n"
                f"  COMPUTED : {truth}  ({kind}, window {lo} .. {hi})\n\n"
                f"Per #43b clause 3f / B65 / priming item 11, harness-history counts are "
                f"COMPUTED, never recalled. Origin: the 2026-07-20 'three times today' "
                f"miscount, where two real fires blended with a 13-day-old priming episode.\n\n"
                f"Required: re-state using the computed number above, or run the count "
                f"yourself in this turn (a Bash/Grep/Read call in-turn exempts the claim).\n\n"
                f"This is a TRIPWIRE (low-FP, low-recall). It only covers hook FIRES "
                f"(meta/hook-fire-log.md) and COMMITS (git rev-list). Counts of agents, "
                f"wakes or routines have no source of record and pass unchecked — its "
                f"silence is not evidence a count is right.",
                file=sys.stderr)
            return 2
        return 0
    except Exception as e:                            # pragma: no cover
        log_fire(HOOK, "ERROR", str(e)[:160])
        return 0                                      # fail-open, always


def selftest():
    from datetime import date
    now = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)
    real_today = _count_fires(date(2026, 8, 3), date(2026, 8, 3))
    cases = [
        # (text, expect, label)
        (f"The hook fired {(real_today or 0) + 2} times today.", "block",
         "ORIGIN SHAPE: third-person fire count, wrong"),
        (f"The hook fired {real_today} times today.", "pass",
         "correct fire count passes"),
        ("I committed 999 times today.", "block", "wrong commit count"),
        ("The hook fired roughly three times today.", "pass", "hedged -> allow"),
        ("The tripwire fired twice today during selftest.", "pass",
         "self-referential meta -> allow"),
        ("Three agents were spawned today.", "pass",
         "no source of record for agents -> allow"),
        ("> the hook fired three times today", "pass", "quoted -> allow"),
        ("The hook fired 3 times today and 5 times yesterday.", "pass",
         "ambiguous multi-count -> allow"),
        ("Hooks are important.", "pass", "no count/window -> allow"),
        ("The cascade hook fired twice.", "pass", "no past-window token -> allow"),
    ]
    ok = 0
    for text, expect, label in cases:
        got, _ = evaluate(text, transcript_path=None, now=now, skip_tool_exempt=True)
        mark = "PASS" if got == expect else "FAIL"
        if got == expect:
            ok += 1
        print(f"  [{mark}] {label}  (expected {expect}, got {got})")
    print(f"\nselftest: {ok}/{len(cases)} passed")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
