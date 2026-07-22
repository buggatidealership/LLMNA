#!/usr/bin/env python3
"""git-guard probe harness. Payloads assembled from fragments; run via
`python3 gg_probe.py` only (never inline in a shell cmd — the live guard scans cmds).

2026-07-22 rework: K3-ORACLE section added — the EXACT external payloads from
`meta/redteam/2026-07-22-K3-deep-dive-review-adjudication.md` (Q3-1, Q3-2a-d),
permanent fixtures per the commission ("oracle-backed, not self-authored probes").
Path resolution made CLAUDE_PROJECT_DIR-relative (same class as the tier-gate
fixture's hardcoded-path defect)."""
import json, os, subprocess, sys
from pathlib import Path
_REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
HOOK = os.path.join(_REPO, "research", "meta", "hooks", "git-guard-pretooluse.py")

# isolate git-guard BLOCK telemetry into a temp root so this test never writes to
# the real hook-fire-log (rework-6: no test pollutes the committed log). The
# guard's block matchers are REPO-independent (relative research/ + CLAUDE.md
# patterns and hardcoded tokens), so blocking behavior is unchanged.
import tempfile as _tf
_SBOX = _tf.mkdtemp(prefix="gg-test-")
os.makedirs(os.path.join(_SBOX, "research", "meta"), exist_ok=True)
_ENV = dict(os.environ, CLAUDE_PROJECT_DIR=_SBOX)

def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True,
                          text=True, env=_ENV).returncode

RM = "rm " + "-rf "
C = "git " + "commit "
CASES = [
    # holes that must now BLOCK (2)
    ("HOLE#1a rm env-var root", RM + "$CLAUDE_PROJECT_DIR", 2),
    ("HOLE#1b rm tilde repo",   RM + "~/LLMNA", 2),
    ("HOLE#2  commit short-n",  C + "-n -m x", 2),
    ("HOLE#2b commit bundled",  C + "-nm x", 2),
    ("HOLE#2c commit -a -n",    C + "-a -n -m x", 2),
    # must STILL block (regression controls)
    ("CTRL resolved-root rm",   RM + "/home/user/LLMNA/research", 2),
    ("CTRL bare-dot rm",        RM + ".", 2),
    ("CTRL long-flag rm",       "rm " + "--recursive --force research/", 2),
    ("CTRL --no-verify commit", C + "--no-verify -m x", 2),
    # must STILL pass (over-block / message-FP controls)
    ("BENIGN scratch rm",       RM + "/tmp/scratch/foo", 0),
    ("BENIGN normal commit",    C + "-m x", 0),
    ("BENIGN push dry-run -n",  "git " + "push -n origin main", 0),
    ("BENIGN git status",       "git status --short", 0),
    ("BENIGN rm single file",   "rm " + "research/meta/todo.md.bak", 0),
    ("FP msg says dash-n",      C + '-m "close the ' + "-n" + ' bypass hole"', 0),
    ("FP msg says commit-n",    C + '-m "fix git ' + "commit -n" + ' path"', 0),
    ("FP msg head-n in text",   C + '-m "use head ' + "-n" + ' 5 here"', 0),
    # ---- K3 ORACLE PAYLOADS (verbatim from the 2026-07-22 adjudication; all
    # ---- were confirmed exit-0 holes pre-rework; permanent fixtures) ----
    ("K3 Q3-1 commit -m then -n",  C + '-m "x" ' + "-n", 2),
    ("K3 Q3-2a rm tilde trailing/", RM + "~/LLMNA/", 2),
    ("K3 Q3-2b rm bare home",       RM + "~/", 2),
    ("K3 Q3-2c rm HOME-var repo",   RM + "$HOME/LLMNA", 2),
    ("K3 Q3-2d rm tilde no-slash (was already blocking)", RM + "~/LLMNA", 2),
    # boundary controls for the new bare-home token: sibling home subpaths pass
    ("CTRL rm home sibling dir",    RM + "~/scratch-notes", 0),
    ("CTRL git -C repo commit -n",  "git -C /home/user/LLMNA commit -nm x", 2),
]
fails = 0
for label, cmd, exp in CASES:
    got = run(cmd)
    ok = (got == exp)
    fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp}")
print(f"\n{'ALL PASS' if fails==0 else str(fails)+' MISMATCH'}")
sys.exit(fails)
