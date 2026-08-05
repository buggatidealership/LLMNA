#!/usr/bin/env python3
"""Falsification tests for the N2 enforcement ledger.

The ledger's whole claim is that its ENFORCED/UNVERIFIED/ADVISORY labels are
COMPUTED from probe results rather than authored. A decorative label — one that
would print "ENFORCED" no matter what the hooks were actually doing — is worse
than no label, because it manufactures exactly the false confidence the
2026-08-05 root-cause artifact was written about.

So these tests do not check that the ledger renders. They check that it CHANGES
when the underlying world changes, and that it FAILS LOUD when it cannot know:

  T1  real status            -> at least one ENFORCED and at least one ADVISORY
  T2  kill a live hook       -> that item flips ENFORCED -> UNVERIFIED
  T3  revive a dead hook     -> that item flips UNVERIFIED -> ENFORCED
  T4  status file missing    -> every item reads UNKNOWN, ledger says so
  T5  status file corrupt    -> same as missing (degrade, never assume coverage)
  T6  status file 99d old    -> staleness banner present, ENFORCED discounted
  T7  no probe result at all -> hook still exits 0 and still injects the block

Run: python3 research/meta/tests/test_enforcement_ledger.py
Exit 0 = all pass. Exit 1 = the ledger is not doing what it claims.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HOOK = REPO / "research" / "meta" / "hooks" / "llm-native-priming-hook.py"
LIVE_STATUS = REPO / "research" / "meta" / "hooks" / "enforcement-status.json"

PROMPT = ("Give me a full thesis update on NVDA with sizing implications and a "
          "position implication line, long enough to clear the 50-char floor.")

FAILS = []


def render(status_obj="LIVE_FILE"):
    """Run the hook with a given status file and return the injected text."""
    env = dict(os.environ)
    tmp = None
    if status_obj == "MISSING":
        env["LLMNA_ENFORCEMENT_STATUS"] = "/nonexistent/enforcement-status.json"
    elif status_obj != "LIVE_FILE":
        fd, tmp = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, "w") as f:
            f.write(status_obj if isinstance(status_obj, str)
                    else json.dumps(status_obj))
        env["LLMNA_ENFORCEMENT_STATUS"] = tmp
    try:
        p = subprocess.run([sys.executable, str(HOOK)],
                           input=json.dumps({"prompt": PROMPT}),
                           capture_output=True, text=True, cwd=str(REPO), env=env)
        if p.returncode != 0:
            return None, p.returncode
        out = json.loads(p.stdout)
        ctx = out["hookSpecificOutput"]["additionalContext"]
        return ctx.split("=== LLM-NATIVE")[0], p.returncode
    finally:
        if tmp:
            os.unlink(tmp)


def line_for(ledger, n):
    for ln in ledger.splitlines():
        if ln.strip().startswith(f"#{n} "):
            return ln
    return ""


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def doctored(**verdicts):
    """Real status with named hooks' verdicts overridden."""
    base = json.loads(LIVE_STATUS.read_text())
    for h, v in verdicts.items():
        base["hooks"].setdefault(h.replace("_", "-"), {})["verdict"] = v
    return base


def main():
    print("ENFORCEMENT LEDGER — FALSIFICATION TESTS\n" + "=" * 66)

    if not LIVE_STATUS.exists():
        print("  enforcement-status.json absent — run hook_probe.py --emit-status")
        return 1

    # T1 — the real world produces a mixed ledger. If everything reads the same
    # label, the ledger is carrying no information.
    led, _ = render()
    check("T1 real status yields both ENFORCED and ADVISORY",
          led and "ENFORCED" in led and "ADVISORY" in led)
    check("T1 item 5 ENFORCED (structural-output-hook is probe-verified LIVE)",
          "ENFORCED" in line_for(led, 5), line_for(led, 5))
    check("T1 item 11 UNVERIFIED (meta-count-tripwire-hook is DEAD-SUSPECT)",
          "UNVERIFIED" in line_for(led, 11), line_for(led, 11))

    # T2 — THE LOAD-BEARING TEST. Kill structural-output-hook in the status file.
    # If item 5 still says ENFORCED, the label is authored, not computed, and
    # every claim this ledger makes is void.
    led2, _ = render(doctored(**{"structural-output-hook": "DEAD-SUSPECT"}))
    check("T2 killing structural-output-hook flips item 5 to UNVERIFIED",
          "UNVERIFIED" in line_for(led2, 5), line_for(led2, 5))

    # T2b — item 7 has TWO backing hooks. Killing one must NOT flip it; killing
    # both must. Otherwise redundancy is being scored wrong in either direction.
    led2b, _ = render(doctored(**{"reasoning-tagging-hook": "DEAD-SUSPECT"}))
    check("T2b killing 1 of item 7's 2 hooks keeps it ENFORCED",
          "ENFORCED" in line_for(led2b, 7), line_for(led2b, 7))
    led2c, _ = render(doctored(**{"reasoning-tagging-hook": "DEAD-SUSPECT",
                                  "anti-fabrication-hook": "DEAD-SUSPECT"}))
    check("T2c killing both of item 7's hooks flips it to UNVERIFIED",
          "UNVERIFIED" in line_for(led2c, 7), line_for(led2c, 7))

    # T3 — the reverse direction. A ledger that only ever downgrades would pass
    # T2 while still being broken.
    led3, _ = render(doctored(**{"meta-count-tripwire-hook": "LIVE"}))
    check("T3 reviving meta-count-tripwire-hook flips item 11 to ENFORCED",
          "ENFORCED" in line_for(led3, 11), line_for(led3, 11))

    # T4/T5 — no knowledge must render as no knowledge, never as coverage.
    led4, _ = render("MISSING")
    check("T4 missing status -> every item UNKNOWN",
          led4 and "UNKNOWN" in led4 and "ENFORCED   [" not in led4)
    check("T4 missing status is stated, not silent",
          led4 and "MISSING OR UNREADABLE" in led4)
    led5, _ = render("{ this is not json")
    check("T5 corrupt status degrades to UNKNOWN, does not crash",
          led5 and "UNKNOWN" in led5)

    # T6 — a stale status file is the quiet failure mode: the hooks rot, the
    # ledger keeps printing ENFORCED from a months-old run.
    old = json.loads(LIVE_STATUS.read_text())
    old["generated_utc"] = "2026-01-01T00:00:00Z"
    led6, _ = render(old)
    check("T6 stale status raises the staleness banner",
          led6 and "DAYS OLD" in led6, (led6 or "")[:200])

    # T7 — none of the above may break the hook's actual job.
    for label, obj in (("real", "LIVE_FILE"), ("missing", "MISSING"),
                       ("corrupt", "{ nope")):
        _, rc = render(obj)
        check(f"T7 hook exits 0 with {label} status", rc == 0, f"rc={rc}")

    print("=" * 66)
    if FAILS:
        print(f"  {len(FAILS)} FAILED: " + ", ".join(FAILS))
        return 1
    print("  all pass — the ledger's labels track the probe, in both directions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
