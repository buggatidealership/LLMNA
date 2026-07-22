# Guard Exit-Path Inventory + Room-Independence Map

**Born:** 2026-07-22 (accounting-layer commission item 6; K3 theme 6 "guards
only in some rooms" + Q5 "8 exit paths never inventoried"). Companion to
`destructive-change-governance.md` (the WHAT) — this file is the WHERE/WHEN
each guard exits, and which rooms it is absent from.

Purpose: the enforcement layer was reviewed (K3 07-22: "the locks mostly
work"); this is the ACCOUNTING of the locks — every exit path named so a
silent nap or a headless-absence can't hide in an un-enumerated branch.

---

## A. PreToolUse git-guard (`git-guard-pretooluse.py`) — command-time guard

Scans every Bash command; blocks destructive families absent the operator token.
Exit paths (verified 2026-07-22 by grep + selftest):

| # | Line | Exit | Trigger | Fail direction |
|---|---|---|---|---|
| 1 | ~105 | **2** | any of 16 `block()` call sites matched (commit -n, force-push, rm-boundary, hooksPath tamper, plumbing, mv, find/xargs/interpreter delete, truncate, dd, redirect) | BLOCK (safe) |
| 2 | ~115 | 0 | `tool_name` not in (None, Bash) | allow non-Bash |
| 3 | ~120 | 0 | empty command string | allow |
| 4 | ~221 | 0 | end of `main()` — nothing matched | allow (default) |
| 5 | ~231 | 0 | exception handler (fail-open) — logs `ERROR fail-open` | allow + log |

Room-independence: ✅ rides `.claude/settings.json` (ships with every clone),
self-activates `core.hooksPath`. Fires from turn 1 on a fresh/headless container.
Scans commands regardless of cwd (destructive commands anywhere are caught).

Residual (documented, not silent): exit #5 fail-open means a malformed-input
crash ALLOWS the command — correct for availability (never brick a session) but
it is an allow-path; the `ERROR fail-open` log line is the receipt that it
happened. `git -C <path> commit -n` from OUTSIDE via a wrapper is covered by the
`-C\s+\S+` clause added 2026-07-22.

## B. Stop commit+push gate (`stop-hook-git-check.sh`) — the record gate

⚠️ **ROOM-DEPENDENCE (K3 theme 6, load-bearing):** the LIVE copy runs from the
environment launcher (`~/.claude/`), NOT from the repo. The repo copy is a
NON-EXECUTED snapshot (header says so). Therefore this gate's presence depends
on the launcher config — in a headless/cron room where the launcher differs, it
may be ABSENT, and NO repo-side equivalent enforces commit+push. This is the
single biggest room-dependence in the stack and CANNOT be fixed from the repo
(a repo-side duplicate would double-fire against the environment one). Tracked
as a promise; the honest state is: **on web/cron, verify the commit+push gate
exists rather than assuming it.**

The 8 exit paths (K3 Q5 — now inventoried):

| # | Line | Exit | Trigger | Fail direction |
|---|---|---|---|---|
| 1 | 16 | 0 | `stop_hook_active == true` | **NAP** (post-block window) |
| 2 | 21 | 0 | not a git repo | allow |
| 3 | 30 | 0 | no remote configured | allow |
| 4 | 36 | **2** | uncommitted (staged or unstaged) changes | BLOCK |
| 5 | 43 | **2** | untracked files present | BLOCK |
| 6 | 66 | **2** | commit(s) GitHub will show Unverified (signature/committer) | BLOCK |
| 7 | 77 | **2** | unpushed commit(s) | BLOCK |
| 8 | 81 | 0 | clean tree, pushed, signed | allow (pass) |

**Exit #1 is the post-block nap window** (K3 theme 6): after ANY Stop hook
blocks, the harness sets `stop_hook_active` on the NEXT Stop, so this gate
naps — a one-turn window where uncommitted work is not caught. Repo-side we
CANNOT change the environment copy. Mitigations in place / planned:
- The PreToolUse git-guard (room-independent) still blocks destructive git ops
  during the nap — deletion/force-push cannot slip through the window.
- Accounting-layer hooks I own now use a CONTENT-SCOPED recursion guard instead
  of a blanket nap (see §C) — the pattern that closes the window.
- Promise registered (07-24) to evaluate a reviewed repo-side commit+push
  backstop with the content-scoped guard (double-fire risk needs review first).

## C. Stop analytical hooks — nap behavior (inventoried 2026-07-22)

All 15 analytical Stop hooks blanket-nap on `stop_hook_active` (`if
stop_hook_active: exit 0`) — the standard infinite-Stop-loop guard. This is the
same nap window as §B#1 but for reasoning-quality gates (lower stakes than the
record gate). Only `receipts-hook.py` (6 refs) now uses the **content-scoped
guard**: it naps ONLY if THIS exact message already blocked here (a real loop),
and RE-ENFORCES on any changed message — closing the window while staying
loop-safe. Selftest cases 14-16 pin this behavior.

Propagation decision (B47 review-discipline): the content-scoped guard is NOT
blanket-applied to the other 15 this session — an unreviewed 15-hook refactor is
exactly the "builder's blind spots ship inside every patch" risk the commission
warns about. `receipts-hook` is the reference implementation; propagation to the
integrity-critical hooks (anti-fabrication first) is a registered, reviewable
follow-up.

| Hook | Nap style |
|---|---|
| receipts-hook.py | **content-scoped** (closes window) |
| anti-fabrication, cascade, session-prime-cascade, segment-trajectory, nth-order, bypass-route, bottoms-up, antifragility, analyst-pt, signal-ingest, reasoning-tagging, llm-native-reasoning, structural-output, macro-anchor, borrowed-vs-firstprinciples | blanket nap (standard loop guard) |
| llm-native-priming (UserPromptSubmit), session-prime, promise-heartbeat (SessionStart) | n/a — not Stop hooks; no nap |

## D. Redirect over-block FP (fixed 2026-07-22, this item)

The git-guard truncating-redirect check false-blocked a heredoc commit message
that merely NAMED a protected file after `cat > /tmp/msg.txt` (reproduced LIVE
2× this session). Fix: anchor the protected match to the immediate redirect
TARGET token, not to prose downstream of the `>`. Pinned by
`tests/test_git_guard_redirect_fp.py` (5 FP-pass + 5 real-catch-block).
