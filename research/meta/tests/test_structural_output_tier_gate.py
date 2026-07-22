#!/usr/bin/env python3
"""structural-output-hook probe battery: tier-check-before-size-gate (G-27) +
PI-casing (K3 Q3-4 rework) + joint-state hyphen fix (case-4 adjudication).

2026-07-22 rework of the born-red fixture:
- HOOK path now CLAUDE_PROJECT_DIR-relative (was hardcoded /home/user/LLMNA —
  broke on any other checkout root).
- case 4 ("long w/ H1/H2 markers") ADJUDICATED: exp=0 was RIGHT; the hook
  over-fired because its joint-state regex rejected the hyphenated
  "joint-state matrix" spelling its own feedback text demands. Hook fixed;
  fixture expectation unchanged.
- PI casing fixtures added (K3 Q3-3: matcher had no re.IGNORECASE, lowercase
  reopened G-27). PROVENANCE: K3's exact 6 spellings were never committed to
  the repo; reconstructing them from recall and labeling them verbatim would
  be the B65 recall-as-receipt failure. The 6 below are FRESHLY AUTHORED
  2026-07-22 to span the case space (canonical / lower / UPPER / Title /
  mixed / bold-wrapped lower). If K3's originals surface later, reconcile.
"""
import json, subprocess, sys, tempfile, os
from pathlib import Path

_REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
HOOK = os.path.join(_REPO, "research", "meta", "hooks", "structural-output-hook.py")


def run(assistant_text):
    # build a minimal one-line JSONL transcript with a single assistant message
    fd, path = tempfile.mkstemp(suffix=".jsonl")
    with os.fdopen(fd, "w") as f:
        f.write(json.dumps({"type": "assistant",
                            "message": {"role": "assistant",
                                        "content": [{"type": "text", "text": assistant_text}]}}) + "\n")
    payload = json.dumps({"transcript_path": path, "stop_hook_active": False})
    # LLMNA_HOOK_TEST=1 -> the hook tags any fire it logs with [probe] so
    # structural-output-metric.py excludes it (channel-B probe-pollution guard).
    env = dict(os.environ, LLMNA_HOOK_TEST="1")
    r = subprocess.run([sys.executable, HOOK], input=payload, capture_output=True,
                       text=True, cwd=_REPO, env=env)
    os.unlink(path)
    return r.returncode

PI_CANON = "Position implication"  # assembled to avoid tripping any scanner on this file's text
TIER = "\U0001F7E2"  # green circle tier marker
SHORT = "x" * 100    # well under 800 chars

# 6 casing spellings (freshly authored, see docstring provenance note)
CASINGS = [
    ("canonical",     PI_CANON + ":"),
    ("all-lower",     PI_CANON.lower() + ":"),
    ("ALL-UPPER",     PI_CANON.upper() + ":"),
    ("Title Case",    "Position Implication:"),
    ("mixed",         "pOsItion imPlication:"),
    ("bold lower",    "**" + PI_CANON.lower() + ":**"),
]

cases = [
    # short message + untiered PI -> must BLOCK (the G-27 fix)
    ("short + untiered PI (THE FIX)", f"{SHORT}\n**{PI_CANON}:** HOLD SMCI at watchlist.", 2),
    # short message + TIERED PI -> must pass
    ("short + tiered PI", f"{SHORT}\n**{PI_CANON}:** HOLD — {TIER} T1 confirmed.", 0),
    # short message, no PI -> pass (not analytical enough)
    ("short, no PI", f"{SHORT} just a status note.", 0),
    # long analytical message w/ structural markers + no PI -> pass
    # (case-4: exp=0 ADJUDICATED CORRECT — hyphenated joint-state now credited)
    ("long w/ H1/H2 markers", ("H1 (P=60%) ... H2 (P=30%) ... joint-state matrix ... " + "y"*850), 0),
]
# every casing, untiered -> BLOCK; every casing, tiered -> pass
for label, spelling in CASINGS:
    cases.append((f"untiered PI casing [{label}]",
                  f"{SHORT}\n{spelling} TRIM to 10% — drifted above target.", 2))
    cases.append((f"tiered PI casing [{label}]",
                  f"{SHORT}\n{spelling} TRIM to 10% {TIER} — per T1 receipt.", 0))

fails = 0
for label, txt, exp in cases:
    got = run(txt); ok = (got == exp); fails += (0 if ok else 1)
    print(f"{'OK ' if ok else 'XX '}{label}: got={got} exp={exp} (len={len(txt)})")
print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
sys.exit(fails)
