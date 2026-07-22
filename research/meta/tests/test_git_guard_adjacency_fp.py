#!/usr/bin/env python3
"""Extra probe for the git-commit-adjacency tightening.
FP reduced from 'any commit -n in text' to 'only literal git-commit-n adjacency'."""
import json, os, subprocess, sys, tempfile
from pathlib import Path
_REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
HOOK = os.path.join(_REPO, "research", "meta", "hooks", "git-guard-pretooluse.py")
_SBOX = tempfile.mkdtemp(prefix="gg-test-")
os.makedirs(os.path.join(_SBOX, "research", "meta"), exist_ok=True)
_ENV = dict(os.environ, CLAUDE_PROJECT_DIR=_SBOX)  # isolate BLOCK telemetry (rework-6)
def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True,
                          text=True, env=_ENV).returncode
C = "git " + "commit "
cases = [
    # prose WITHOUT git-commit adjacency -> now PASS (the fix)
    ("prose 'commit -n' no-git-adj", 'echo ' + '"the commit -n flag skips hooks"', 0),
    ("prose git-guard: commit -n",   'cat f << E\n' + "guard note: commit -n bypass\nE", 0),
    ("prose 'commit' then later -n",  'echo ' + '"commit stuff" && ls -n', 0),
    # real invocations -> BLOCK
    ("REAL git commit -n",       C + "-n -m x", 2),
    ("REAL git commit -nm",      C + "-nm x", 2),
    # benign real commit -> PASS
    ("BENIGN git commit -m",     C + "-m x", 0),
    ("BENIGN msg mentions -n",   C + '-m "close -n hole"', 0),
    # DOCUMENTED RESIDUAL: literal 'git commit -n' in prose still blocks (can't disambiguate)
    ("RESIDUAL literal git-commit-n in prose", 'echo ' + '"run git ' + "commit -n" + ' to skip"', 2),
]
f = 0
for label, cmd, exp in cases:
    got = run(cmd); ok = got == exp; f += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp}")
print("ALL PASS" if f == 0 else f"{f} MISMATCH")
sys.exit(f)
