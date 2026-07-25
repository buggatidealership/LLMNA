#!/bin/bash
# LLMNA environment setup script (built 2026-07-16).
# Lives in git; the cloud environment's "Setup script" field contains ONLY:
#   bash /home/user/LLMNA/research/meta/tools/setup.sh || true
# Runs at container start, before Claude Code launches.
# NEVER-ECHO: prints/writes presence booleans and lengths only — never key values.
# Must NEVER fail the boot: every step is best-effort (|| true), output to /tmp only
# (writing into the repo would dirty the tree and trip the git-check Stop hook).

OUT=/tmp/llmna-boot-status.txt
{
  echo "LLMNA boot status — $(date -u +%Y-%m-%dT%H:%M:%SZ) — host $(hostname)"
  echo "--- env keys (presence only) ---"
  for k in FINNHUB_API_KEY EODHD_API_TOKEN FRED_API_KEY DART_API_KEY \
           EDINET_API_KEY FMP_API_KEY ALPHAVANTAGE_API_KEY ECOS_API_KEY; do
    v="${!k}"
    if [ -n "$v" ]; then echo "$k: PRESENT(len=${#v})"; else echo "$k: absent"; fi
  done
  echo "--- keyless reachability (no tokens involved) ---"
  for url in "https://data.sec.gov/submissions/CIK0001046179.json" \
             "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"; do
    code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 8 \
           -H "User-Agent: LLMNA-personal-research alistairjdb@gmail.com" "$url" || echo "ERR")
    echo "${url%%/v1*}: HTTP $code"
  done
  echo "--- repo ---"
  cd /home/user/LLMNA 2>/dev/null && echo "HEAD: $(git rev-parse --short HEAD 2>/dev/null) ($(git log -1 --format=%cd --date=format:%Y-%m-%d 2>/dev/null))"
  # Snapshot-currency guard (added 2026-07-17 after a fresh-session audit ran on an
  # 11-day-stale container clone, 393 commits behind, and mistook it for reality):
  git fetch origin main --quiet 2>/dev/null || true
  BEHIND=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "?")
  echo "BEHIND origin/main: ${BEHIND} commits $( [ "${BEHIND}" != "0" ] && echo '<<< STALE CLONE — git pull BEFORE trusting any repo state' )"
} > "$OUT" 2>&1 || true
# Diff-before-commit + secrets-scan pre-commit hook (binding, user directive 2026-07-16):
cd /home/user/LLMNA 2>/dev/null && git config core.hooksPath research/meta/hooks/git || true

exit 0
