#!/usr/bin/env python3
"""ACTIVATION-CHAIN test (rework-item-1, L38: component-green != system-green).

The branch's original failure: two hooks passed `python3 hook.py --selftest`
(the COMPONENT) but shipped git mode 100644, so when settings.json fired them by
BARE PATH they exited 126 (Permission denied) and enforced nothing. A selftest
can never catch this — only invoking the hook the way the harness invokes it can.

This test asserts the two things a selftest cannot:
  (A) EVERY hook wired in .claude/settings.json that points at a repo .py/.sh is
      committed EXECUTABLE (git mode 100755). Checks the COMMITTED mode via
      `git ls-files -s` — not the local fs mode — because the bug was in what
      shipped, not what sat in one working tree.
  (B) The two new hooks actually RUN when invoked by bare path (returncode != 126)
      and behave correctly on a real event fed on stdin.

Run: python3 research/meta/tests/test_hook_activation_chain.py  (exit = #fails)
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[3])
SETTINGS = REPO / ".claude" / "settings.json"

fails = 0


def check(label, cond):
    global fails
    print(("OK  " if cond else "XX  ") + label)
    fails += 0 if cond else 1


def git_mode(relpath: str) -> str:
    r = subprocess.run(["git", "-C", str(REPO), "ls-files", "-s", relpath],
                       capture_output=True, text=True)
    return r.stdout.split()[0] if r.stdout.strip() else ""


# ---- (A) every wired repo-script hook is committed executable ----
settings = json.loads(SETTINGS.read_text())
wired = []
for event, groups in settings.get("hooks", {}).items():
    for g in groups:
        for h in g.get("hooks", []):
            cmd = h.get("command", "")
            # match a repo-relative path to a .py/.sh hook script inside the command
            for tok in cmd.replace('"', " ").split():
                if "research/meta/hooks/" in tok and tok.rstrip(".").endswith((".py", ".sh")):
                    rel = tok[tok.index("research/meta/hooks/"):]
                    wired.append((event, rel))

check("found wired script hooks in settings.json", len(wired) >= 2)
for event, rel in wired:
    mode = git_mode(rel)
    # executable bit set for owner => mode like 100755 / 100775 (third-from-last digit odd/>=1)
    execbit = bool(mode) and mode.startswith("100") and int(mode[-3]) % 2 == 1
    check(f"[{event}] {rel} committed executable (mode={mode or 'MISSING'})", execbit)


# ---- (B) new hooks RUN by bare path (not 126) + behave ----
env = dict(os.environ, CLAUDE_PROJECT_DIR=str(REPO), LLMNA_HOOK_TEST="1")

def fire_bare(rel, stdin, cwd=None):
    """Invoke exactly as settings.json does: the bare path is the argv[0]."""
    path = str(REPO / rel)
    return subprocess.run([path], input=stdin, capture_output=True, text=True,
                          env=env, cwd=cwd or str(REPO))

# receipts-hook: build a transcript with a fabricated file-claim -> must BLOCK (exit 2)
with tempfile.TemporaryDirectory() as td:
    tpath = os.path.join(td, "t.jsonl")
    fab = "Created `research/meta/zzz-nonexistent-activation-probe.md` for the ledger."
    Path(tpath).write_text(json.dumps({"type": "assistant",
        "message": {"role": "assistant", "content": [{"type": "text", "text": fab}]}}) + "\n")
    r = fire_bare("research/meta/hooks/receipts-hook.py",
                  json.dumps({"stop_hook_active": False, "transcript_path": tpath}))
    check("receipts-hook runs by bare path (not 126)", r.returncode != 126)
    check("receipts-hook BLOCKS a fabricated file-claim via activation chain (exit 2)",
          r.returncode == 2)

# receipts-hook: empty transcript -> runs, no claim, exit 0
r = fire_bare("research/meta/hooks/receipts-hook.py",
              json.dumps({"stop_hook_active": False, "transcript_path": "/nonexistent"}))
check("receipts-hook clean input runs by bare path, exit 0", r.returncode == 0)

# promise-heartbeat: SessionStart event -> runs, exit 0
r = fire_bare("research/meta/hooks/promise-heartbeat.py",
              json.dumps({"hook_event_name": "SessionStart", "source": "startup"}))
check("promise-heartbeat runs by bare path (not 126)", r.returncode != 126)
check("promise-heartbeat exits 0 via activation chain", r.returncode == 0)

print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
