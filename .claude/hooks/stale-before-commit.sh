#!/usr/bin/env bash
# PreToolUse hook: refuse a `git commit` whose staged diff changes a measured
# value and leaves the old one written somewhere (CY2, R465).
#
# `scripts/precommit_stale.py` was written at CX1 on the reviewer's own
# suggestion and wired to nothing -- a grep over `.github/`, `.claude/` and
# every script found only its own test. A tool wired to nothing is the species
# it exists to catch, so this is the wiring.
#
# It FAILS OPEN when python is missing, like the two hooks beside it, and says
# so loudly rather than silently allowing.

set -u
input=$(cat)

# Only `git commit`. A `git commit --amend` is one too; anything else passes.
if ! printf '%s' "$input" | grep -qE '"command"[[:space:]]*:[[:space:]]*"[^"]*git commit'; then
  exit 0
fi

PY_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PY_BIN" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"No python interpreter found; the staleness check cannot run and would otherwise FAIL OPEN."}}\n'
  exit 0
fi

root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root" || exit 0

out=$("$PY_BIN" scripts/precommit_stale.py 2>&1)
code=$?
if [ "$code" -eq 0 ]; then
  exit 0
fi

# The survivors are reported, not decided: every one needs a look, and the
# measured false rate on a real round was four in five. The reason carries the
# whole list so the decision is made against the lines rather than the count.
reason=$(printf '%s' "$out" | "$PY_BIN" -c 'import json,sys;print(json.dumps(sys.stdin.read()))')
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":%s}}\n' "$reason"
exit 0
