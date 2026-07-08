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
