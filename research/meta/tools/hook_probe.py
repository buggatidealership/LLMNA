#!/usr/bin/env python3
"""
HOOK EXECUTION PROBE HARNESS — born 2026-08-05 (condition N3).

WHY THIS EXISTS
---------------
`meta/hook-fire-log.md` records fires. It CANNOT distinguish:
  (a) a hook that is dead and can never fire, from
  (b) a hook that is alive but whose trigger is rare.
Both read as "no log". On 2026-08-05 four hooks showed NO-LOG and at least two
of them provably run every turn, so the log is not evidence of health either way.

`session-prime-cascade-hook` was dead-on-arrival for two months because its
regex required an ID-dash adjacency no real header has. Zero fires looked
identical to zero triggers. That is the failure this harness exists to make
impossible.

WHAT IT DOES
------------
For every Stop hook it builds a synthetic transcript containing a POSITIVE
fixture (text that SHOULD trip the hook) and a NEGATIVE fixture (text that
should sail through), feeds each through the hook's real stdin contract, and
records the exit code.

  exit 2 = hook blocked the message
  exit 0 = hook passed it

VERDICTS (this is the falsifiable part — every hook lands in exactly one)
  LIVE            positive fires AND negative passes   -> the hook works
  DEAD-SUSPECT    positive does NOT fire AND zero fires ever logged -> likely dead
  FIXTURE-UNMATCHED positive does NOT fire BUT the log proves it has fired
                  -> THE FIXTURE IS WRONG, not the hook
  OVER-FIRES      negative fires                       -> false-positive generator
  BROKEN          non-0/2 exit, or an exception        -> crashes
  UNPROBEABLE     trigger depends on git/repo state, not message text

UNPROBEABLE IS NOT A PASS. It means this harness cannot adjudicate the hook and
a state-based fixture is still owed. Reported separately so it can never be
quietly counted as healthy.

USAGE
  python3 research/meta/tools/hook_probe.py            # probe all
  python3 research/meta/tools/hook_probe.py --json     # machine-readable
  python3 research/meta/tools/hook_probe.py --hook structural-output-hook
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HOOKS = REPO / "research" / "meta" / "hooks"

# Each entry: (positive_fixture, negative_fixture)
# positive = MUST trip the hook. negative = MUST NOT.
# Fixtures are written against each hook's documented trigger, not guessed.
FIXTURES = {
    "anti-fabrication-hook": (
        # NOTE: the currency regex REQUIRES a unit suffix. "$47,318,000,000"
        # does NOT match; "$47.3 billion" does. The first fixture written here
        # used the former and produced a false DEAD verdict on a hook that had
        # fired 62 times in 30 days. Kept as a comment because the near-miss is
        # the whole reason this harness carries a calibration set.
        "The company reported revenue of $47.3 billion for the quarter and "
        "capacity reached 91.7 GW across the fleet.",
        "Nothing numeric here — a plain narrative sentence about the market.",
    ),
    "bottoms-up-hook": (
        "WORKFLOW: PREDICT. I forecast revenue will reach $88 billion in 2029, "
        "implying 34% growth off the current base.",
        "A short factual restatement with no forward projection of any kind.",
    ),
    "nth-order-cascade-hook": (
        "NVDA thesis: the HBM shortage causes memory prices to rise, which "
        "drives margin expansion for the beneficiary names in this portfolio.",
        "A neutral note about file organisation in the repository.",
    ),
    "bypass-route-hook": (
        "The binding constraint is advanced packaging capacity; supply is tight "
        "and the shortage is capacity-limited through 2027 for this thesis.",
        "A neutral note about file organisation in the repository.",
    ),
    "antifragility-mn-hook": (
        "P(bull case): 65%. P(bear case): 20%. Tier: Core. Position target 10%.",
        "A neutral note about file organisation in the repository.",
    ),
    "analyst-pt-context-hook": (
        "The stock is trading above analyst PT — the average PT of $261 sits "
        "below the current price, so the thesis looks stretched here.",
        "A neutral note about file organisation in the repository.",
    ),
    "reasoning-tagging-hook": (
        "I put the odds of the guide being raised at P~78% and the reaction "
        "turning negative at P~55%.",
        "A neutral note about file organisation in the repository.",
    ),
    "macro-anchor-hook": (
        "NVDA thesis update. Bull case: demand strengthens through 2027 and the "
        "bear case weakens materially. Sizing this position higher is warranted. "
        "Position implication: HOLD — no size change — thesis intact.",
        "A neutral note about file organisation in the repository.",
    ),
    "segment-trajectory-hook": (
        "AI is only 4% of revenue for this name, which is too small to drive "
        "the thesis, so it goes to Tier 3 and we skip it.",
        "A neutral note about file organisation in the repository.",
    ),
    "structural-output-hook": (
        ("This is a long analytical response about the NVDA thesis and the "
         "probability of the bull scenario resolving in our favour. " * 12),
        "Short ack.",
    ),
    "borrowed-vs-firstprinciples-hook": (
        "Per the SemiAnalysis note, consensus is that HBM tightness persists "
        "into 2027. Analysts say the NVDA thesis holds. According to the report, "
        "the bull case is intact and sizing should increase.",
        "A neutral note about file organisation in the repository.",
    ),
    "llm-native-reasoning-hook": (
        "On balance, weighing the pros and cons, my view is that the NVDA thesis "
        "remains intact and the stock should outperform. The most likely outcome "
        "is continued strength; I expect the bull case to play out as described.",
        "A neutral note about file organisation in the repository.",
    ),
    "meta-count-tripwire-hook": (
        "The hook fired 3 times today and I have made 7 commits this session. "
        "There are 19 Critical Rules and 21 hooks in the harness right now.",
        "A neutral note about file organisation in the repository.",
    ),
}

# ---------------------------------------------------------------------------
# FIXTURE PRE-FLIGHT — added after the harness produced THREE false DEAD
# verdicts in a row on hooks with 62 and 115 fires in 30 days.
#   miss 1: "$47,318,000,000" — the currency regex REQUIRES a unit suffix
#   miss 4: the PAD TEXT ITSELF contained the word "hooks", which several
#           hooks treat as a meta-discussion EXEMPTION — the filler disarmed
#           the very hooks it was meant to reach. Pad text must be plain
#           market prose containing NO harness vocabulary.
#   miss 2/3: fixtures under 200 chars — several hooks `sys.exit(0)` on
#             `len(text) < 200`, treating short messages as acknowledgements,
#             so the scan never runs and the hook looks dead.
# A probe whose fixtures are invalid is worse than no probe: it manufactures
# confident false negatives about the very layer it exists to audit.
# 900, not 200: hooks apply DIFFERENT length gates (anti-fabrication 200,
# macro-anchor and structural-output 800). The floor must clear the HIGHEST
# gate or the tallest-gated hooks silently report DEAD. Miss 5 of 5.
MIN_FIXTURE_CHARS = 900
_PAD = (" The quarter showed continued expansion across the memory and packaging "
        "segments, with order books extending into the following year and lead "
        "times remaining elevated versus the prior comparable period. Management "
        "commentary described broad-based demand across regions and end markets.")


def _validate_and_pad(fixtures):
    """Positive fixtures MUST clear the length gate. Pad deterministically."""
    fixed = {}
    for name, (pos, neg) in fixtures.items():
        while len(pos) < MIN_FIXTURE_CHARS:
            pos = pos + _PAD
        fixed[name] = (pos, neg)
    return fixed


# Trigger depends on repo/git state or the USER message, not the assistant text.
# A text fixture cannot adjudicate these. Named explicitly so they are never
# silently counted as healthy.
FIXTURES = _validate_and_pad(FIXTURES)

STATE_BASED = {
    "cascade-enforcement-hook": "needs modified thesis files in the working tree",
    "signal-ingest-cascade-hook": "needs a cascade-worthy USER message + session file state",
    "session-prime-cascade-hook": "needs a git diff adding a new codification ID",
    "git-guard-pretooluse": "PreToolUse contract, not Stop; probed by test_git_guard_*.py",
}

# Not enforcement objects.
NON_ENFORCEMENT = {
    "session-start-hook": "informational briefing, always exit 0 by design",
    "session-prime-hook": "SessionStart injection, no block path",
    "llm-native-priming-hook": "UserPromptSubmit injection, no block path",
    "hook_fire_log": "shared library, not a hook",
}


def run_hook(hook_name: str, assistant_text: str, timeout: int = 25):
    """Feed a synthetic transcript through the hook's real stdin contract."""
    path = HOOKS / f"{hook_name}.py"
    if not path.exists():
        return None, f"missing script: {path}"
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as tf:
        tf.write(json.dumps({
            "type": "assistant",
            "message": {"role": "assistant",
                        "content": [{"type": "text", "text": assistant_text}]},
        }) + "\n")
        transcript = tf.name
    payload = json.dumps({
        "transcript_path": transcript,
        "hook_event_name": "Stop",
        "stop_hook_active": False,
        "cwd": str(REPO),
    })
    env = dict(os.environ, CLAUDE_PROJECT_DIR=str(REPO))
    # NOTE: cwd=REPO is REQUIRED — hooks self-gate to the research repo and
    # exit 0 anywhere else. Probing from /tmp would report every hook DEAD.
    try:
        p = subprocess.run([sys.executable, str(path)], input=payload, text=True,
                           capture_output=True, timeout=timeout, cwd=str(REPO), env=env)
        return p.returncode, (p.stderr or "")[:200]
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:  # pragma: no cover
        return None, f"{type(e).__name__}: {e}"
    finally:
        try:
            os.unlink(transcript)
        except OSError:
            pass


PROBE_OPEN = "<!-- PROBE-RUN-BEGIN -->"
PROBE_CLOSE = "<!-- PROBE-RUN-END -->"


def _fence(marker):
    """Fence probe-induced fires so they never pollute the audit baseline.

    DISCOVERED THE HARD WAY 2026-08-05: running this harness made the hooks
    log real fires. macro-anchor went 115 -> 173 and structural-output
    129 -> 182 across a handful of probe runs. An instrument that inflates the
    telemetry it reads will, given enough runs, make every hook look busy and
    healthy — the exact false-confidence failure this harness was built to
    expose, reproduced by the harness itself."""
    log = REPO / "research" / "meta" / "hook-fire-log.md"
    try:
        with open(log, "a") as f:
            f.write(f"{marker}\n")
    except OSError:
        pass


def fire_history():
    """Fires per hook from meta/hook-fire-log.md. A hook with logged fires has
    PROVEN it can fire — so a failing fixture means the FIXTURE is wrong, not
    the hook. Without this the probe conflates 'my test is bad' with 'the hook
    is dead', which is exactly the false-negative class it exists to kill."""
    import re as _re, collections
    log = REPO / "research" / "meta" / "hook-fire-log.md"
    c = collections.Counter()
    if not log.exists():
        return c
    pat = _re.compile(r"^- \d{4}-\d{2}-\d{2} [\d:]+Z ([a-z0-9\-_]+) ")
    # DEPTH, not a boolean. The retroactive fence inserted on 2026-08-05
    # spans probe runs that had already written their OWN fences inside it,
    # so the markers nest. A boolean would clear on the first inner CLOSE and
    # readmit the remaining probe fires as real — the same class of silent
    # miscount this probe exists to detect, one level down in the reader.
    depth = 0
    for ln in log.read_text(errors="replace").splitlines():
        if ln.strip() == PROBE_OPEN:
            depth += 1
            continue
        if ln.strip() == PROBE_CLOSE:
            depth = max(0, depth - 1)
            continue
        if depth:             # probe-induced, NOT a real catch
            continue
        mm = pat.match(ln)
        if mm and "smoke-test" not in ln:
            c[mm.group(1)] += 1
    return c


def verdict(pos_rc, neg_rc):
    if pos_rc is None or neg_rc is None:
        return "BROKEN"
    if pos_rc not in (0, 2) or neg_rc not in (0, 2):
        return "BROKEN"
    if pos_rc == 2 and neg_rc == 0:
        return "LIVE"
    if pos_rc == 0:
        return "DEAD"
    if neg_rc == 2:
        return "OVER-FIRES"
    return "BROKEN"


# CALIBRATION SET — hooks with INDEPENDENT evidence of being alive (they fired
# at this session on 2026-08-05, and meta/hook-fire-log.md records the counts).
# If the probe calls any of these DEAD, THE PROBE IS WRONG, not the hook.
# This exists because the first run of this harness reported anti-fabrication
# (62 fires/30d) and macro-anchor (115 fires/30d) as DEAD on bad fixtures.
CALIBRATION_LIVE = {
    "anti-fabrication-hook", "macro-anchor-hook", "bottoms-up-hook",
    "nth-order-cascade-hook", "reasoning-tagging-hook", "structural-output-hook",
}


def main():
    global FIRES
    FIRES = fire_history()   # read BEFORE fencing, so this run is excluded
    _fence(PROBE_OPEN)
    only = None
    if "--hook" in sys.argv:
        only = sys.argv[sys.argv.index("--hook") + 1]
    results = {}

    for name, (pos, neg) in sorted(FIXTURES.items()):
        if only and name != only:
            continue
        pos_rc, pos_err = run_hook(name, pos)
        neg_rc, neg_err = run_hook(name, neg)
        v = verdict(pos_rc, neg_rc)
        fires = FIRES.get(name, 0)
        # A hook with logged fires has proven it CAN fire. If our fixture fails
        # to trip it, the fixture is at fault — never report that as DEAD.
        if v == "DEAD" and fires > 0:
            v = "FIXTURE-UNMATCHED"
        elif v == "DEAD" and fires == 0:
            v = "DEAD-SUSPECT"
        results[name] = {
            "verdict": v, "fires_logged": fires,
            "positive_exit": pos_rc, "negative_exit": neg_rc,
            "err": (pos_err or neg_err or "").strip()[:120],
        }
    for name, why in sorted(STATE_BASED.items()):
        if only and name != only:
            continue
        results[name] = {"verdict": "UNPROBEABLE", "reason": why}

    _fence(PROBE_CLOSE)

    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
        return 0

    # Calibration check BEFORE reporting anything.
    miscalled = [n for n in CALIBRATION_LIVE
                 if results.get(n, {}).get("verdict") in ("DEAD-SUSPECT", "FIXTURE-UNMATCHED")]
    if miscalled:
        print("=" * 74)
        print("  PROBE SELF-TEST FAILED — these hooks have independent evidence")
        print("  of being alive but the probe called them DEAD:")
        for n in sorted(miscalled):
            print(f"    - {n}")
        print("  => THE FIXTURES ARE WRONG, NOT THE HOOKS. Fix before trusting")
        print("     any DEAD verdict in this run.")
        print("=" * 74 + "\n")

    order = {"DEAD-SUSPECT": 0, "OVER-FIRES": 1, "BROKEN": 2,
             "FIXTURE-UNMATCHED": 3, "UNPROBEABLE": 4, "LIVE": 5}
    print(f"HOOK EXECUTION PROBE — {len(results)} hooks\n" + "=" * 74)
    for name, r in sorted(results.items(), key=lambda kv: (order[kv[1]["verdict"]], kv[0])):
        v = r["verdict"]
        mark = {"LIVE": "OK  ", "DEAD-SUSPECT": "DEAD", "OVER-FIRES": "OVER",
                "BROKEN": "BRK ", "UNPROBEABLE": "??? ",
                "FIXTURE-UNMATCHED": "FIX "}[v]
        extra = r.get("reason") or (f"pos={r.get('positive_exit')} neg={r.get('negative_exit')} "
                                    f"fires={r.get('fires_logged')}"
                                    if "positive_exit" in r else "")
        print(f"  [{mark}] {name:34} {v:12} {extra}")
        if r.get("err"):
            print(f"         stderr: {r['err']}")
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print("=" * 74)
    print("  " + " · ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("\n  UNPROBEABLE is NOT a pass — a state-based fixture is still owed.")
    # Non-zero exit if anything is DEAD or BROKEN, so this can gate CI later.
    if miscalled:
        return 2  # probe itself is untrustworthy this run
    return 1 if (counts.get("DEAD-SUSPECT") or counts.get("BROKEN")) else 0


if __name__ == "__main__":
    sys.exit(main())
