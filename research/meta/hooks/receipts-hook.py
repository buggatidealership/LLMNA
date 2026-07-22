#!/usr/bin/env python3
"""LLMNA RECEIPTS HOOK (Stop) — say–do gap enforcement, Phase 1.

Built 2026-07-22 per `meta/hooks/receipts-hook-spec.md` (K3 proposal adjudicated
2026-07-20) under the fresh-session accounting-layer commission
(`meta/redteam/2026-07-22-K3-harness-state-opinion-and-fresh-session-commission.md`,
theme 1 — "referee grades its own homework").

PRINCIPLE (spec §top): no action-claim may be emitted that isn't constructible
from a same-turn receipt — this hook RE-DERIVES the claimed state itself;
pasted receipts don't count. A narration that skipped the post-action read is
exactly the class this catches.

PHASE-1 CHECKS (spec adjudication table):
  1-amended  CLAIM ACCURACY on git state: a commit SHA stated in the final
             assistant message must exist in this repository
             (`git cat-file -e <sha>^{commit}`); a past-tense "pushed" claim
             must match `@{u}` sync (rev-list @{u}..HEAD == 0). Push-STATE
             enforcement stays where it lives (stop-hook-git-check);
             this hook only verifies the CLAIM matches reality.
  3          FILE CLAIMS: "Created/Updated/Wrote `path`" → the path must exist
             in the working tree. Globs / hedged / historical narration skipped.
  4 (cheap)  ENVIRONMENT CLAIMS: "sentinel touched/armed" → the named sentinel
             file must exist.

THREE-VALUED VERDICTS (house standard): PASS (verified true — silent),
FAIL (verified false — exit 2 + stderr, logged to hook-fire-log),
UNVERIFIABLE (cannot re-derive — exit 0, never blocks; Phase-3 sampled lane
owns the semantic tail).

FP DISCIPLINE (spec precondition): the extraction patterns below were
corpus-backtested over every research/**/*.md file before wiring
(`--backtest`; receipt in the shipping commit). Live FP ladder per spec
falsifiers: >2 FP/week → narrow the verb-pattern.

COUNT-LEG (1c recompute-and-compare) joins 2026-08-03 — NOT implemented here
(data dependency on 2 weeks of anti-fab fire-log, unchanged).

Fail-open: any exception → exit 0 + log. Recursion guard: stop_hook_active
→ exit 0 (post-block-nap window is tracked separately — commission item 6).

Modes: (no args) = live Stop hook; --selftest = fixture battery (exit = #fails);
--backtest = corpus FP sweep over research/**/*.md (exit 0, prints counts).
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = os.environ.get("CLAUDE_PROJECT_DIR") or str(Path(__file__).resolve().parents[3])
LOG = os.path.join(REPO, "research", "meta", "hook-fire-log.md")
STATE = os.path.join(REPO, "research", "meta", ".receipts-hook-state.json")  # gitignored


def _content_hash(text: str) -> str:
    import hashlib
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16]


def _blocked_before(text: str) -> bool:
    """True iff THIS exact message already produced a receipts block."""
    try:
        if not os.path.exists(STATE):
            return False
        return _content_hash(text) in json.load(open(STATE)).get("blocked", [])
    except Exception:
        return False


def _remember_block(text: str) -> None:
    try:
        seen = json.load(open(STATE)).get("blocked", []) if os.path.exists(STATE) else []
        h = _content_hash(text)
        if h not in seen:
            with open(STATE, "w") as f:
                json.dump({"blocked": (seen + [h])[-8:]}, f)
    except Exception:
        pass

# SHA action-claim: past-tense verb IMMEDIATELY adjacent to the hex token
# ("Committed abc1234", "committed as abc1234", "commit: abc1234").
# Citation/appositive forms — "(commit 4c049f48)", "per dcdd60a9 commit" — are
# deliberately NOT checked: the corpus backtest (2026-07-22, 755 files) showed
# ~50 legitimate citations of pre-history-rewrite SHAs that no longer resolve
# (known condition, DURABLE-ACTIVATION.md G-40 note). Claim-accuracy scope is
# the assistant's OWN same-turn "I committed X" claims, per spec check 1-amended.
# Token must contain >=1 digit AND >=1 [a-f] letter: kills pure-digit
# timestamp/ID tokens (e.g. 20260622000299) at the cost of skipping the rare
# all-digit real SHA — conservative direction (skip = UNVERIFIABLE, never FP).
SHA_CLAIM = re.compile(
    r"(?i)\b(?:committed|commit(?:\s+hash)?:|sha:)\s*(?:as\s+|at\s+|in\s+)?"
    r"[`(\[]{0,2}((?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40})\b")

# past-tense push claim; negative forms excluded in code below
PUSHED_CLAIM = re.compile(r"(?<![a-zA-Z])[Pp]ushed\b")
PUSH_NEGATORS = re.compile(
    r"(?i)\b(not|isn't|aren't|will be|to be|please|must be|should be|un)\s*pushed"
    r"|\bunpushed\b|\bpushed\s+(?:back|for|out|to\s+(?:next|later|2\d{3}))")

# file-claim line: action verb + backticked repo-relative path
FILE_VERB = re.compile(r"(?i)\b(created|updated|wrote|rewrote|added|saved|appended)\b")
BACKTICK_PATH = re.compile(
    r"`((?:research|\.claude|predictions|meta|companies|sector|signals|"
    r"portfolio|watchlist|wiki)/[\w./-]+\.(?:md|py|json|sh|yml|jsonl))`")
# historical / future / negated narration — not a this-turn action claim
CLAIM_HEDGES = re.compile(
    r"(?i)\b(previously|was (?:created|updated|added|written)|had been|will be|"
    r"to be (?:created|updated|added|written)|planned|pending|historical|retired|"
    r"deleted|removed|renamed|instead of|rather than|would|should|could|may|might|"
    r"if\b|not yet|never)\b")

SENTINEL_CLAIM = re.compile(r"(?i)\b(?:touched|armed|re-armed)\b[^\n`]{0,60}`?(~/[.\w-]+|/[\w./-]+sentinel[\w.-]*)`?")


def log_line(msg: str) -> None:
    try:
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"- {ts} receipts-hook {msg}\n")
    except Exception:
        pass


def git(*args, cwd=None):
    return subprocess.run(["git", "-C", cwd or REPO, *args],
                          capture_output=True, text=True, timeout=10)


def load_last_assistant_message(data: dict) -> str:
    transcript_path = data.get("transcript_path")
    if not transcript_path or not Path(transcript_path).exists():
        return ""
    last = ""
    try:
        with open(transcript_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                msg = obj.get("message", {})
                if msg.get("role") != "assistant":
                    continue
                content = msg.get("content", [])
                if isinstance(content, list):
                    text = "\n".join(c.get("text", "") for c in content
                                     if isinstance(c, dict) and c.get("type") == "text")
                else:
                    text = str(content)
                if text:
                    last = text
    except Exception:
        return ""
    return last


def extract_claims(text: str, repo: str):
    """Return (fails, unverifiable) lists of (kind, detail) claim verdicts.

    Only lines that make an action claim are examined; quoted lines (>) and
    hedged/historical narration are skipped. Verification is a RE-DERIVATION
    against git / the filesystem, never a string-trust of the message.
    """
    fails, unver = [], []
    seen_shas, seen_paths = set(), set()
    push_claimed = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(">"):
            continue
        hedged = CLAIM_HEDGES.search(line) is not None

        # ---- check 1-amended: SHA existence ----
        if not hedged:
            for tok in SHA_CLAIM.findall(line):
                if tok in seen_shas:
                    continue
                seen_shas.add(tok)
                r = git("cat-file", "-e", f"{tok}^{{commit}}", cwd=repo)
                if r.returncode != 0:
                    # Repo-grounding pass (Critical Rule #7d, same rule as the
                    # anti-fabrication hook): a SHA that exists as an exact
                    # string in the COMMITTED corpus is a restatement of logged
                    # history (pre-rewrite SHAs, G-40 class) — UNVERIFIABLE,
                    # not a fabrication. A fabricated SHA exists nowhere.
                    g = git("grep", "-qF", tok, "HEAD", "--", "research/", cwd=repo)
                    if g.returncode == 0:
                        unver.append(("sha", f"`{tok}` not in object DB but grounded in committed corpus (historical restatement)"))
                    else:
                        fails.append(("sha", f"claimed commit `{tok}` does not exist in this repository"))

        # ---- check 1-amended: push-sync claim ----
        if (not hedged and PUSHED_CLAIM.search(line)
                and not PUSH_NEGATORS.search(line)):
            push_claimed = True

        # ---- check 3: file claims ----
        # Proximity rule: the action verb must appear within 60 chars BEFORE the
        # backticked path on the same line — long lines that happen to contain
        # both a verb and a distant reference path are citations, not claims.
        if not hedged and FILE_VERB.search(line):
            for pm in BACKTICK_PATH.finditer(line):
                p = pm.group(1)
                vprox = FILE_VERB.search(line[max(0, pm.start() - 60):pm.start()])
                if vprox is None:
                    continue
                if p in seen_paths or any(ch in p for ch in "*?{") or ".." in p:
                    continue
                seen_paths.add(p)
                cand = [os.path.join(repo, p)]
                if not p.startswith(("research/", ".claude/")):
                    cand.append(os.path.join(repo, "research", p))
                if not any(os.path.exists(c) for c in cand):
                    fails.append(("file", f"claimed file `{p}` does not exist in the working tree"))

        # ---- check 4: sentinel claims (cheap environment receipts) ----
        if not hedged:
            m = SENTINEL_CLAIM.search(line)
            if m:
                sp = os.path.expanduser(m.group(1))
                if not os.path.exists(sp):
                    fails.append(("sentinel", f"claimed sentinel `{m.group(1)}` does not exist"))

    if push_claimed:
        up = git("rev-parse", "--abbrev-ref", "@{u}", cwd=repo)
        if up.returncode != 0:
            unver.append(("push", "pushed-claim: no upstream configured — cannot re-derive"))
        else:
            ahead = git("rev-list", "@{u}..HEAD", "--count", cwd=repo)
            if ahead.returncode == 0 and ahead.stdout.strip().isdigit() \
                    and int(ahead.stdout.strip()) > 0:
                fails.append(("push", f"message claims 'pushed' but HEAD is "
                                      f"{ahead.stdout.strip()} commit(s) ahead of {up.stdout.strip()}"))
    return fails, unver


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        sys.exit(0)
    if not os.getcwd().startswith(REPO):
        sys.exit(0)

    text = load_last_assistant_message(data)
    if not text:
        sys.exit(0)

    # Content-scoped recursion guard (commission item 6, K3 theme 6 "guards take
    # one nap after any alarm"). The harness sets stop_hook_active after ANY hook
    # blocks; a BLANKET exit-0 here would nap through a FRESH false claim in the
    # very next message — the enforcement-free post-block window. Nap ONLY if THIS
    # exact message already blocked HERE (a real loop the agent can't satisfy); a
    # changed message re-enforces. Loop-safety preserved: identical re-sends nap.
    if data.get("stop_hook_active") and _blocked_before(text):
        sys.exit(0)

    fails, _unver = extract_claims(text, REPO)
    if not fails:
        sys.exit(0)

    _remember_block(text)
    log_line("FIRE (" + "; ".join(f"{k}:{d[:80]}" for k, d in fails) + ")")
    sys.stderr.write(
        "RECEIPTS HOOK (say–do gap, spec: meta/hooks/receipts-hook-spec.md): "
        "the final message makes action-claims that FAIL re-derivation:\n")
    for kind, detail in fails:
        sys.stderr.write(f"  - [{kind}] {detail}\n")
    sys.stderr.write(
        "\nA claim of done/committed/pushed/created must be constructible from a "
        "same-turn receipt. Re-check the actual state (git log -1 / git status / "
        "ls the path), perform the missing action or correct the claim, then restate.\n")
    sys.exit(2)


# ---------------------------------------------------------------- selftest
def _selftest() -> int:
    import tempfile
    fails = 0

    def check(label, cond):
        nonlocal fails
        print(("OK  " if cond else "XX  ") + label)
        fails += 0 if cond else 1

    with tempfile.TemporaryDirectory() as td:
        repo = os.path.join(td, "r")
        os.makedirs(os.path.join(repo, "research", "meta"))
        subprocess.run(["git", "init", "-q", repo], check=True)
        subprocess.run(["git", "-C", repo, "config", "user.email", "t@t"], check=True)
        subprocess.run(["git", "-C", repo, "config", "user.name", "t"], check=True)
        f = os.path.join(repo, "research", "meta", "real.md")
        open(f, "w").write("x\n")
        subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
        subprocess.run(["git", "-C", repo, "commit", "-qm", "seed"], check=True)
        sha = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"],
                             capture_output=True, text=True).stdout.strip()

        # 1. real SHA claim → PASS
        fl, _ = extract_claims(f"Committed {sha[:9]} with the fix.", repo)
        check("real SHA passes", fl == [])
        # 2. fabricated SHA claim → FAIL
        fl, _ = extract_claims("Committed 1a2b3c4d5e and pushed nothing else.", repo)
        check("fabricated SHA fails", any(k == "sha" for k, _ in fl))
        # 3. hex-free prose → no claim
        fl, _ = extract_claims("The commit message describes the fix.", repo)
        check("prose without hex is silent", fl == [])
        # 4. existing-file claim → PASS
        fl, _ = extract_claims("Updated `research/meta/real.md` with the entry.", repo)
        check("existing file passes", fl == [])
        # 5. missing-file claim → FAIL
        fl, _ = extract_claims("Created `research/meta/ghost.md` for the ledger.", repo)
        check("missing file fails", any(k == "file" for k, _ in fl))
        # 6. hedged narration → skipped
        fl, _ = extract_claims("Previously created `research/meta/ghost.md` (since retired).", repo)
        check("hedged/historical narration skipped", fl == [])
        # 7. quoted line → skipped
        fl, _ = extract_claims("> Created `research/meta/ghost.md`", repo)
        check("quoted line skipped", fl == [])
        # 8. pushed claim, no upstream → UNVERIFIABLE (no fail)
        fl, uv = extract_claims("Committed and pushed the receipts layer.", repo)
        check("pushed w/o upstream = unverifiable, no block",
              fl == [] and any(k == "push" for k, _ in uv))
        # 9. pushed claim with upstream, ahead → FAIL
        up = os.path.join(td, "up.git")
        subprocess.run(["git", "init", "-q", "--bare", up], check=True)
        subprocess.run(["git", "-C", repo, "remote", "add", "origin", up], check=True)
        subprocess.run(["git", "-C", repo, "push", "-qu", "origin", "HEAD"],
                       check=True, capture_output=True)
        open(f, "a").write("y\n")
        subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
        subprocess.run(["git", "-C", repo, "commit", "-qm", "ahead"], check=True)
        fl, _ = extract_claims("Committed and pushed the receipts layer.", repo)
        check("pushed-claim while ahead fails", any(k == "push" for k, _ in fl))
        # 10. pushed claim after real push → PASS
        subprocess.run(["git", "-C", repo, "push", "-q"], check=True, capture_output=True)
        fl, _ = extract_claims("Committed and pushed the receipts layer.", repo)
        check("pushed-claim when synced passes", fl == [])
        # 11. negated push forms → no claim
        fl, _ = extract_claims("These are not pushed yet; please push later.", repo)
        check("negated push forms skipped", fl == [])
        # 12. hook process: garbage stdin → exit 0 (fail-open)
        r = subprocess.run([sys.executable, __file__], input="{not json",
                           capture_output=True, text=True)
        check("garbage stdin exits 0", r.returncode == 0)
        # 13. stop_hook_active with empty/no transcript → exit 0 (no text to judge)
        r = subprocess.run([sys.executable, __file__],
                           input=json.dumps({"stop_hook_active": True}),
                           capture_output=True, text=True)
        check("stop_hook_active + no transcript exits 0", r.returncode == 0)

        # 14. content-scoped recursion guard (item 6 nap-window fix): the helpers
        # read the module-global STATE; point it at a temp file for the test.
        import tempfile as _tf
        real_state = STATE
        with _tf.TemporaryDirectory() as td2:
            globals()["STATE"] = os.path.join(td2, "state.json")
            msg_a = "Created `research/meta/ghost.md` for the ledger."
            msg_b = "Created `research/meta/other-ghost.md` for the ledger."
            check("fresh message not blocked-before", not _blocked_before(msg_a))
            _remember_block(msg_a)
            check("remembered message IS blocked-before (loop → nap)", _blocked_before(msg_a))
            check("DIFFERENT message NOT blocked-before (fresh → re-enforce)",
                  not _blocked_before(msg_b))
        globals()["STATE"] = real_state

    print("ALL PASS" if fails == 0 else f"{fails} MISMATCH")
    return fails


def _backtest() -> None:
    """Corpus FP sweep: every research/**/*.md treated as a candidate message.

    Historical documents legitimately narrate created/updated files and cite
    SHAs; any FAIL here is a false positive the live hook must not produce.
    """
    root = Path(REPO) / "research"
    total_files = 0
    fp_files = []
    for p in sorted(root.rglob("*.md")):
        total_files += 1
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fl, _ = extract_claims(text, REPO)
        if fl:
            fp_files.append((str(p.relative_to(REPO)), fl))
    print(f"backtest: {total_files} files scanned, {len(fp_files)} with FAIL verdicts")
    for name, fl in fp_files:
        for k, d in fl:
            print(f"  FP? {name}: [{k}] {d}")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(_selftest())
    if "--backtest" in sys.argv:
        _backtest()
        sys.exit(0)
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        log_line(f"ERROR fail-open: {type(e).__name__}")
        sys.exit(0)
