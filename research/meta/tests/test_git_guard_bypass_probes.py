#!/usr/bin/env python3
"""git-guard probe harness. Payloads assembled from fragments; run via
`python3 gg_probe.py` only (never inline in a shell cmd — the live guard scans cmds)."""
import json, os, subprocess, sys
ENV = dict(os.environ, LLMNA_PROBE="1")  # probe-tag fires (07-23, G-28)
HOOK = os.path.join(os.environ.get("CLAUDE_PROJECT_DIR") or "/home/user/LLMNA",
                    "research", "meta", "hooks", "git-guard-pretooluse.py")

def run(cmd):
    p = json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}})
    return subprocess.run([sys.executable, HOOK], input=p, capture_output=True, text=True, env=ENV).returncode

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
    # redirect data-span fixes (07-23 audit): heredoc/quoted prose w/ ">" +
    # protected filename = FP resolved; real redirect targets still block
    ("FP heredoc msg-file w/ protected name",
     "cat > /tmp/s/m.txt << 'E'\ngrade 9/9 > baseline; grading-log row\nE", 0),
    ("FP commit -m w/ > + protected name", C + '-m "0.10 > base, grading-log row"', 0),
    ("TP real truncation of protected",  "echo x > research/meta/methodology.md", 2),
    ("TP sh -c redirect onto protected", 'bash -c "echo x > CLAUDE.md"', 2),
]
fails = 0
for label, cmd, exp in CASES:
    got = run(cmd)
    ok = (got == exp)
    fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp}")
print(f"\n{'ALL PASS' if fails==0 else str(fails)+' MISMATCH'}")
sys.exit(fails)
