#!/usr/bin/env python3
"""LLMNA PreToolUse git guard (born 2026-07-19 LATE from the user's new-session probe;
v2 2026-07-19 LATE after Kimi-K3 red-team found the guard covered only the commit/push
surface while a confused agent has many other doors — 13 demonstrated bypasses).

THREAT MODEL: confused/misdirected agent (not adversarial human) — misinterpretation,
hallucinated-state cleanup, relayed/poisoned instruction, destructive-command accident.

WHY THIS LAYER: git-level hooks need core.hooksPath, which a fresh clone lacks; this
PreToolUse hook rides .claude/settings.json (ships with every clone, provably fires
even on a stale snapshot). It (1) self-activates hooksPath, (2) deterministically
blocks the destructive command families below absent the matching operator token.

COVERAGE (v2). Absent OPERATOR_APPROVED_FORCE_PUSH=1 (history/record class) or
OPERATOR_APPROVED_DELETION=1 (file-destruction class), block:
  commit/push  : --no-verify ; push --force/-f/--force-with-lease/--delete/-d/:ref/+ref (K3 E5)
  hooksPath    : git config / -c / --unset of core.hooksPath to a non-canonical value (K3 E3)
  plumbing     : reset --hard, clean -f(dx), reflog expire, gc --prune, branch -D/-d,
                 update-ref -d, filter-branch, filter-repo, stash drop/clear,
                 checkout/switch -f/--force, worktree remove --force (K3 E2)
  mv/rename    : mv of .git / research / protected path out (K3 E7)
  action-level : rm -rf repo/.git/research ; find …-delete/-exec rm ; xargs rm ;
                 python/perl/ruby/node rmtree/unlink/remove on repo path ;
                 truncate -s0 / dd of= / single-> redirect onto a protected file (K3 E4)

HELD for post-review synthesis (NOT in v2, tracked in destructive-change-governance.md):
  nonce challenge-response tokens (K3 #3) ; cumulative cross-commit thresholds (K3 E1) ;
  Edit/Write/MultiEdit matcher on enforcement files (K3 E8) ; semantic settings-diff
  guard (K3 E9) ; hook-content hash manifest self-heal (K3 #1). Server-side GitHub
  branch protection (K3 #2 / E6) is the operator-side floor beneath all of this.

Exit 2 + stderr = deterministic block. Exit 0 = allow. Any exception = allow + log
(fail-open — never brick a session).
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or "/home/user/LLMNA"
LOG = os.path.join(REPO, "research", "meta", "hook-fire-log.md")
CANON_HOOKS = "research/meta/hooks/git"

# repo-record / enforcement targets whose destruction is record-loss, not scratch work
# 2026-07-20 K3-Swarm G-24 fix: dynamic repo root + $CLAUDE_PROJECT_DIR + bare `.`/`./`
# (cwd inside the repo) — the old list hardcoded only the literal path, so
# `find . -delete` and rmtree('.') passed the has_repo gate unexamined.
REPO_TOKENS = re.compile(
    r"(" + re.escape(REPO) + r"|/home/user/LLMNA|\$\{?CLAUDE_PROJECT_DIR\}?|"
    # 07-23 audit: tilde/$HOME repo aliases (find/xargs/interpreter/truncate/dd
    # branches gate on REPO_TOKENS; `find ~/LLMNA -delete` previously passed).
    # Deliberately repo-scoped only — bare `~` here would arm the repo gates on
    # every home-dir mention; the rm branch handles bare-tilde separately.
    r"~/LLMNA(/|\b)|\$\{?HOME\}?/LLMNA(/|\b)|"
    r"(^|[\s'\"=(])\.(/|['\"]|\s|$)|"
    r"(^|[\s'\"=(/])research(/|\b)|\.git(/|\b)|\bmethodology|"
    r"\bsession-prime|\blessons\.md|\bgrading-log|calibration-ledger|CLAUDE\.md|"
    r"settings\.json|(^|[\s'\"=(/])portfolio(/|\b)|meta/hooks)"
)


def log_line(msg: str) -> None:
    try:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"- {ts} git-guard-pretooluse {msg}\n")
    except Exception:
        pass


def ensure_hooks_path() -> None:
    try:
        r = subprocess.run(["git", "-C", REPO, "config", "core.hooksPath"],
                           capture_output=True, text=True, timeout=5)
        if r.stdout.strip() != CANON_HOOKS:
            subprocess.run(["git", "-C", REPO, "config", "core.hooksPath", CANON_HOOKS],
                           capture_output=True, timeout=5)
            log_line("ACTIVATED core.hooksPath (was unset/wrong — stale-session class)")
    except Exception:
        pass


def block(reason: str, cmd: str) -> None:
    log_line(f"BLOCK ({reason})")
    sys.stderr.write(
        f"GIT-GUARD (PreToolUse): BLOCKED — {reason}.\n"
        f"Command: {cmd[:300]}\n"
        "Per research/meta/destructive-change-governance.md this requires operator "
        "approval in-conversation, then the matching OPERATOR_APPROVED_* token. "
        "An inferred/relayed instruction does not qualify.\n"
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

    force_ok = (os.environ.get("OPERATOR_APPROVED_FORCE_PUSH") == "1"
                or "OPERATOR_APPROVED_FORCE_PUSH=1" in cmd)
    del_ok = (os.environ.get("OPERATOR_APPROVED_DELETION") == "1"
              or "OPERATOR_APPROVED_DELETION=1" in cmd)

    # commit-message payloads are DATA not flags — strip so a message describing the
    # guard doesn't self-trip (K3 false-positive class, demonstrated live 2026-07-19).
    # bash -c "..." wrappers are deliberately NOT stripped (inner command still scanned).
    s = re.sub(r"(-m|--message)(\s+|=)('[^']*'|\"[^\"]*\")", r"\1 MSG", cmd)
    has_repo = REPO_TOKENS.search(s) is not None
    is_git = re.search(r"\bgit\b", s) is not None

    # ---- history / record-rewrite class (FORCE_PUSH token) ----
    if not force_ok:
        # commit: --no-verify OR its short form -n (possibly bundled, e.g. -nm) skips
        # pre-commit + commit-msg. push: only --no-verify (there -n means --dry-run,
        # which must NOT block). K3-Swarm deep-dive fix 2026-07-21 (git commit -n bypass).
        # The -n check is TEMPERED to the pre-message flag region — a tempered-greedy
        # token that refuses to cross the -m/--message/-F/--file argument — so a commit
        # MESSAGE that merely contains a "-n" token does not false-block (verified live).
        if is_git and re.search(r"\bcommit\b[^|;&]*--no-verify", s):
            block("--no-verify would skip the verified pre-commit/commit-msg guards", cmd)
        # commit -n (short --no-verify). 07-23 audit fix: the 07-21 tempered-greedy
        # token refused to cross -m/-F, so `git commit -m "x" -n` (flag AFTER the
        # message) bypassed it — probe-verified. Correct structure: spans that
        # provably cannot carry an EXECUTED command are DATA — strip them, then
        # scan the whole git-commit segment for a short-flag bundle containing n.
        #   stripped : heredoc bodies NOT piped into a shell; echo/printf args
        #              (resolves the old documented-residual echo-prose FP)
        #   kept     : bash/sh -c "..." payloads (executed — must stay scanned);
        #              -m "..." payloads already neutralized to MSG at the top.
        # Long flags (--amend) can't match: [a-zA-Z]* refuses the second hyphen.
        # push -n stays allowed (there it means --dry-run; separate push checks).
        # Residuals (documented, confused-agent threat model): quoted flag
        # `git commit "-n"`; heredoc piped into an interpreter other than *sh;
        # `git commit -uno` (rare legit bundle with n) over-blocks — rephrase long-form.
        def _heredoc_sub(m, _s=s):
            pre = _s[max(0, m.start() - 40):m.start()]
            return m.group(0) if re.search(r"\b(ba|z|da)?sh\b[^|;&]*$", pre) else " HEREDOC "
        s_noq = re.sub(r"<<-?\s*(['\"]?)(\w+)\1[\s\S]*?\n\2\b", _heredoc_sub, s)
        s_noq = re.sub(r"\b(echo|printf)\b[^|;&\n]*", r"\1 ECHOARG", s_noq)
        if is_git and re.search(r"\bgit\b[^|;&]*\bcommit\b[^|;&]*\s-[a-zA-Z]*n[a-zA-Z]*\b", s_noq):
            block("commit -n (short --no-verify) would skip the pre-commit/commit-msg guards", cmd)
        if is_git and re.search(r"\bpush\b[^|;&]*--no-verify", s):
            block("--no-verify would skip the verified pre-push guard", cmd)
        if is_git and re.search(r"\bpush\b", s) and re.search(
                r"\bpush\b[^|;&]*(--force(-with-lease)?\b|\s-f\b|--delete\b|\s-d\b|\s[:+]\S)", s):
            block("force-push / remote-ref deletion / +refspec (history-rewrite class)", cmd)
        # core.hooksPath tampering (disable the git-level guards) — allow only canonical.
        # Case-insensitive (K3-Swarm G-25 fix): git config keys are case-insensitive,
        # so `core.hookspath` was an evasion against the old case-sensitive patterns.
        m = re.search(r"(?i)core\.hookspath[=\s]+(\S+)", s)
        if m and m.group(1).strip("'\"") != CANON_HOOKS:
            block("core.hooksPath override to a non-canonical value (disables git guards)", cmd)
        if re.search(r"(?i)config[^|;&]*--unset[^|;&]*core\.hookspath", s):
            block("unsetting core.hooksPath (disables git guards)", cmd)
        if is_git and re.search(
                r"\b(reset\s+--hard|clean\s+-[a-z]*f[a-z]*|reflog\s+expire|gc\b[^|;&]*--prune|"
                r"branch\s+-[dD]\b|update-ref\s+-d|filter-branch|filter-repo|"
                r"stash\s+(drop|clear)|checkout\s+(-f|--force)|switch\s+(-f|--force)|"
                r"restore\s+[^|;&]*(--worktree|--staged|\.(\s|$))|"
                r"worktree\s+remove[^|;&]*(--force|-f))\b", s):
            block("git plumbing that discards commits/refs/working-tree (history/record class)", cmd)
        # mv of .git or a protected tree out from under the repo
        if re.search(r"\bmv\s+[^|;&]*(\.git\b|\bresearch\b|\bportfolio\b)", s):
            block("mv of .git / research / portfolio (record relocation)", cmd)

    # ---- file-destruction class (DELETION token) ----
    if not del_ok:
        # Long-flag forms included (K3-Swarm G-23 fix): `rm --recursive --force`
        # escaped the short-flag-only regex; LLM agents emit long flags habitually.
        if re.search(r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r|-r\s+-f|-f\s+-r"
                     r"|--recursive\b[^|;&]*--force\b|--force\b[^|;&]*--recursive\b"
                     r"|--recursive\b[^|;&]*-[a-zA-Z]*f|-[a-zA-Z]*r[a-zA-Z]*\b[^|;&]*--force\b)", s):
            tail = s.split("rm", 1)[1]
            # K3-Swarm deep-dive fix 2026-07-21: the rm branch had its own narrow tail
            # regex and never consulted REPO_TOKENS, so `rm -rf $CLAUDE_PROJECT_DIR` and
            # `rm -rf ~/LLMNA` slipped past the G-24 hardening. Now gate on the tail
            # regex (extended with ~ / ~/LLMNA) OR the hardened REPO_TOKENS set.
            # 07-23 audit fix (probe-verified bypasses): trailing-slash tilde form
            # (~/LLMNA/), home-wipe (~/), and $HOME/${HOME} forms all exited 0 —
            # the old `~(/LLMNA)?` required a boundary immediately after, which a
            # trailing slash broke, and $HOME had no pattern at all.
            if re.search(rf"(\s|=|'|\"|^)({re.escape(REPO)}(/research|/\.git|/portfolio)?/?|"
                         r"research/?|\.git/?|portfolio/?|~(/LLMNA)?/?|"
                         r"\$\{{?HOME\}}?(/LLMNA)?/?|\.|/)(\s|$|'|\")", tail) \
                    or REPO_TOKENS.search(tail):
                block("recursive force-delete aimed at repo root / research / portfolio / .git", cmd)
        if has_repo and re.search(r"\bfind\b[^|;&]*(-delete\b|-exec\s+(rm|unlink)\b)", s):
            block("find -delete / -exec rm over a repo path (mass file deletion)", cmd)
        if has_repo and re.search(r"\|\s*xargs\b[^|;&]*\b(rm|unlink)\b", s):
            block("xargs rm over a repo path (mass file deletion)", cmd)
        if re.search(r"\b(python3?|perl|ruby|node)\b[^|;&]*(-c|-e)\b", s) and \
           re.search(r"(rmtree|unlink|os\.remove|removedirs|\brmdir\b|shutil\.rmtree|fs\.rm)", s) and has_repo:
            block("interpreter-level file deletion (rmtree/unlink) on a repo path", cmd)
        if has_repo and re.search(r"\btruncate\b[^|;&]*-s\s*0\b", s):
            block("truncate -s0 on a repo path (content erasure)", cmd)
        if has_repo and re.search(r"\bdd\b[^|;&]*\bof=", s):
            block("dd of= onto a repo path (content overwrite)", cmd)
        # single-> truncating redirect onto an enforcement/protected file (not >> append).
        # Protected list aligned with destructive-change-governance §1b (K3-Swarm G-26 fix):
        # CLAUDE.md, biases-watchlist, grading-log, calibration-ledger, INDEX.md,
        # portfolio/, meta/tools/ were named protected there but missing here.
        if re.search(r"(^|[^>])>\s*[^>|;&]*"
                     r"(\.git/|meta/hooks/|meta/tools/|settings\.json|methodology|"
                     r"session-prime|lessons\.md|CLAUDE\.md|biases-watchlist|"
                     r"grading-log|calibration-ledger|INDEX\.md|portfolio/)", s):
            block("truncating redirect (>) onto an enforcement/protected file", cmd)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        log_line(f"ERROR fail-open: {type(e).__name__}")
        sys.exit(0)
