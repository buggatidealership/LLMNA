#!/usr/bin/env python3
"""LLMNA PreToolUse git guard (born 2026-07-19 LATE, from the user's new-session probe).

WHY THIS EXISTS (the probe finding): a fresh session on a stale clone had NO git hooks
active — .git/hooks empty, core.hooksPath unset — because git-level hook activation
depended on the ENVIRONMENT's setup-script field (user-side, invisible to the repo).
The project hook layer (.claude/settings.json), by contrast, provably ran even in that
stale session. So this guard lives at the layer that actually travels with the clone.

TWO FUNCTIONS, both fail-open (never brick a session; log instead):
  1. SELF-ACTIVATION: before any Bash command runs, idempotently set
     core.hooksPath -> research/meta/hooks/git. Closes the "guards exist in the repo
     but nothing installed them" gap for every session whose clone carries this file.
  2. COMMAND SCREEN (CATASTROPHIC tier, destructive-change-governance.md):
     block, absent the operator token, any Bash command containing:
       - `--no-verify` on git commit/push  (the documented client-hook bypass)
       - `git push` with --force / --force-with-lease / -f / --delete / -d / :refspec
       - `rm -rf`-class recursive deletion aimed at the repo root, .git, or research/
     Token = OPERATOR_APPROVED_FORCE_PUSH=1 (push/no-verify class) or
     OPERATOR_APPROVED_DELETION=1 (rm class), set ONLY after explicit operator
     approval in-conversation — same honesty contract as the git-level guards.

Exit 2 + stderr = deterministic block (Claude Code PreToolUse contract).
Exit 0 = allow. Any internal exception = allow + log (fail-open by design).
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or "/home/user/LLMNA"
LOG = os.path.join(REPO, "research", "meta", "hook-fire-log.md")


def log_line(msg: str) -> None:
    try:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"- {ts} git-guard-pretooluse {msg}\n")
    except Exception:
        pass


def ensure_hooks_path() -> None:
    """Idempotent self-activation of the version-controlled git hooks."""
    try:
        r = subprocess.run(
            ["git", "-C", REPO, "config", "core.hooksPath"],
            capture_output=True, text=True, timeout=5,
        )
        if r.stdout.strip() != "research/meta/hooks/git":
            subprocess.run(
                ["git", "-C", REPO, "config", "core.hooksPath", "research/meta/hooks/git"],
                capture_output=True, timeout=5,
            )
            log_line("ACTIVATED core.hooksPath (was unset/wrong — stale-session class)")
    except Exception:
        pass


def block(reason: str, cmd: str) -> None:
    log_line(f"BLOCK ({reason})")
    sys.stderr.write(
        f"GIT-GUARD (PreToolUse, CATASTROPHIC tier): BLOCKED — {reason}.\n"
        f"Command: {cmd[:300]}\n"
        "Per research/meta/destructive-change-governance.md this requires explicit "
        "verbatim operator instruction naming the action, then the matching "
        "OPERATOR_APPROVED_* token. An inferred/relayed instruction does not qualify.\n"
    )
    sys.exit(2)


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        data = {}
    if data.get("tool_name") not in (None, "Bash"):
        sys.exit(0)
    cmd = (data.get("tool_input") or {}).get("command", "") or ""

    ensure_hooks_path()
    if not cmd:
        sys.exit(0)

    force_ok = (
        os.environ.get("OPERATOR_APPROVED_FORCE_PUSH") == "1"
        or "OPERATOR_APPROVED_FORCE_PUSH=1" in cmd
    )
    del_ok = (
        os.environ.get("OPERATOR_APPROVED_DELETION") == "1"
        or "OPERATOR_APPROVED_DELETION=1" in cmd
    )

    # Commit-message text is data, not flags: strip -m "..." payloads before screening
    # (first false positive 2026-07-19: a harness-meta commit MESSAGE mentioning
    # "--no-verify" tripped the flag pattern). bash -c "..." wrappers are NOT stripped.
    scan = re.sub(r"(-m|--message)(\s+|=)('[^']*'|\"[^\"]*\")", r"\1 MSG", cmd)

    is_git = re.search(r"\bgit\b", scan) is not None
    if is_git and re.search(r"(commit|push)\b[^|;&]*--no-verify", scan) and not force_ok:
        block("--no-verify would skip the verified pre-commit/pre-push guards", cmd)

    if is_git and re.search(r"\bpush\b", scan) and not force_ok:
        if re.search(r"\bpush\b[^|;&]*(--force(-with-lease)?\b|\s-f\b|--delete\b|\s-d\b|\s:\S)", scan):
            block("force-push / remote-ref deletion (history-rewrite class)", cmd)

    if not del_ok and re.search(r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r|-r\s+-f|-f\s+-r)\b", scan):
        targets = rf"(\s|=|'|\"|^)({re.escape(REPO)}(/research|/\.git)?/?|research/?|\.git/?|\.|/)(\s|$|'|\")"
        if re.search(targets, scan.split("rm", 1)[1]):
            block("recursive force-delete aimed at repo root / research/ / .git", cmd)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # fail-open: never brick the session
        log_line(f"ERROR fail-open: {type(e).__name__}")
        sys.exit(0)
