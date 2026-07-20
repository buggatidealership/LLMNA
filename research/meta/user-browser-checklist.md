# USER BROWSER CHECKLIST — pending user-side actions (desktop web required)

**Created:** 2026-07-08 (user request: "save everything I must do in a browser so I can recall it tomorrow"). Delete items as done; I re-surface this at the next session start until empty.

## 1. Environment network allowlist (~2 min) — unlocks zero-token market-data scripts
1. Desktop browser → **claude.ai/code**
2. Click the **cloud icon** showing the environment name (in the environment selector when starting a task, or in a routine's edit form below Instructions)
3. **Hover the LLMNA environment → click the settings icon** on the right
4. In **"Update cloud environment"** → **Network access** dropdown → **Custom**
5. **Allowed domains**, one per line:
   stooq.com
   fred.stlouisfed.org
   api.frankfurter.app
6. Keep **"Also include default list of common package managers" CHECKED**
7. **Save changes** (applies to NEW sessions only — I test with a fetch on the next fresh session)

## 0. ⭐ FIX THE ROUTINE REPO BINDING (~2 min) — THE root-cause fix (do this one first; may be superseded if my E7 test passes — I'll update)
1. Desktop browser → **claude.ai/code/routines**
2. Open **"KR-JP morning wake"** → Edit → in the routine form find the **repository selector** → select **buggatidealership/LLMNA** → Save
3. Repeat for **"EOD synthesis"**
4. (Alternative/belt-and-braces: in the environment settings for "Analyst", update its source repo to LLMNA)
Why: your screenshots proved the spawns run in the old Health-Calculators environment — the routines' repo binding never migrated.

## 2. ~~Routine transcript look~~ ✅ DONE 2026-07-08 (user opened the run from a push notification — the screenshots WERE the diagnosis; E-series root cause found)
1. **claude.ai/code/routines** → click **"KR-JP morning wake"** or **"EOD synthesis"**
2. The routine's page lists **past runs** — open ANY one (each is a full session transcript)
3. Tell Claude what you see (screenshot or one sentence). Outcome map (my model, per the E6 artifact): empty/immediate-error = spawn-error (~P45) · work attempted but tool calls denied = allow-list-not-honored (~P30) · anything else (~P25)

## 3. Old branch deletion (~1 min) — housekeeping, blocked user-side since 2026-07-06
1. github.com → **buggatidealership/LLMNA** → Branches
2. Delete **`claude/first-test-new-repo-wxedu9`** (stale test branch; classifier blocks me from deleting it)

## 5. ⭐ NEW-SESSION ENVIRONMENT HYGIENE (~1 min) — your 2026-07-19 probe found sessions can spawn on ~11-day-stale snapshots with ZERO guards
1. When starting any new session at claude.ai/code: check the **environment selector** shows the LLMNA environment (the one whose setup script runs `research/meta/tools/setup.sh`) — your probe session ran on a stale snapshot (pre-guards, old architecture) from what looks like the old environment binding.
2. In that environment's settings, confirm the **Setup script** field contains: `bash /home/user/LLMNA/research/meta/tools/setup.sh || true`
3. If an old environment (Health-Calculators-era "Analyst" or similar) still exists in the list, consider deleting it so stale spawns can't happen — that deletion is YOURS to make (HIGH-tier by our own matrix if done agent-side).
Why: guards now self-install via the repo's project hooks (f027157) for any FRESH clone — but a container that boots an old cached snapshot predating today carries neither the guards nor the self-installer. Fresh clone from the right environment = fully guarded from turn 1.

## 6. ⭐ NEW 2026-07-20: change the GitHub DEFAULT BRANCH to main (~1 min) — confirmed cause of THREE degraded external audits
Computed 2026-07-20 (`git remote show origin`): the repo's default branch is still **`claude/first-test-new-repo-wxedu9`**, whose last commit is 2026-07-06 — while `main` is current. Every fresh clone and every external reviewer session (the 07-17 fresh-session audit, fresh-Claude round 1, tonight's K3 Swarm) lands on a 14-day-stale repo by default and reports "missing" files that exist on main.
1. github.com → **buggatidealership/LLMNA** → **Settings → General** (or the Branches page)
2. **Default branch** → switch to **`main`** → confirm
3. THEN do item 3 (delete the stale branch) — deletion is only possible after it stops being the default.

## 4. ⭐ GitHub branch protection on main (~2 min) — RECLASSIFIED REQUIRED after K3 red-team (2026-07-19): the ONLY layer that survives a server-side API bypass
**K3 finding E6:** every guard I built is client-side. An agent (or a poisoned instruction) that calls the GitHub API directly — `gh api -X DELETE .../branches/main`, `gh repo delete`, or `curl` with the repo token — bypasses ALL of them by construction, because the record lives on GitHub's servers, not on my machine. Branch protection is the only stop that runs where the record actually lives. This moved from "nice backstop" to "the one layer I genuinely cannot substitute for."
1. github.com → **buggatidealership/LLMNA** → **Settings → Branches** (or Settings → Rules → Rulesets on the new UI)
2. Add a protection rule / ruleset for branch **`main`**
3. Enable: **"Do not allow force pushes"** (blocks history rewrite) and **"Restrict deletions"** (blocks branch wipe)
4. Save. Nothing else needed — normal pushes are unaffected.
Why: my machine-side guards (pre-commit Function 4 + the new pre-push hook, both independently verified 2026-07-19) physically block destructive commits/pushes, but any client-side hook can in principle be skipped with `--no-verify`. Branch protection runs on GitHub's servers — it stops a force-push no matter what happens on my side. This is the final backstop for the CATASTROPHIC tier in `meta/destructive-change-governance.md`.
