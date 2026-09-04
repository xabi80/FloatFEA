#!/usr/bin/env bash
# Stop hook: the implementer may not end its turn while the newest step report
# has no supervisor verdict, or while the newest verdict is HOLD/STOP and a
# later step report exists.
#
# Input: hook JSON on stdin. Output: JSON {"decision":"block","reason":...}
# to block, or nothing to allow. Honours stop_hook_active to avoid loops.

set -u
input=$(cat)

# python3 does not exist on every machine this repo is worked on (Windows/Git
# Bash has `python`). Both hooks FAIL OPEN when the interpreter is missing --
# protect-reviews resolves an empty path and allows the edit; require-verdict
# emits invalid JSON and the stop is allowed. Resolve once, loudly.
PY_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PY_BIN" ]; then
  printf '{"decision":"block","reason":"No python interpreter found; the gating hooks cannot run and would otherwise FAIL OPEN. Install python or fix PATH."}
'
  exit 0
fi


# If we are already inside a stop-hook continuation, allow the stop so the
# hook cannot recurse forever.
if printf '%s' "$input" | grep -q '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi

root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$root" || exit 0

# Newest report by (milestone, step) — sort numerically on the step number.
report=$(ls docs/reports/F*/step-*.md 2>/dev/null \
  | awk -F'[/-]' '{ m=$2; sub(/^F/,"",m); s=$NF; sub(/\.md$/,"",s); printf "%03d %03d %s\n", m, s, $0 }' \
  | sort | tail -1 | awk '{print $3}')
[ -z "$report" ] && exit 0   # no reports yet: gating not active

review=${report/docs\/reports/docs\/reviews}

# Any earlier step still on HOLD/STOP while a later report exists is a
# violation regardless of what the newest review says.
stepnum() { local s=${1##*step-}; echo "${s%.md}"; }
for r in $(ls docs/reviews/F*/step-*.md 2>/dev/null); do
  [ "$r" = "$review" ] && continue
  v=$(grep -m1 -E '^Verdict:' "$r" | awk '{print $2}')
  if [ "$v" = "HOLD" ] || [ "$v" = "STOP" ]; then
    # Same milestone, and the newest report is a later step than the held one.
    if [ "$(dirname "$r")" = "$(dirname "$review")" ] && [ "$(stepnum "$report")" -gt "$(stepnum "$r")" ]; then
      printf '{"decision":"block","reason":"%s"}\n' \
        "$r is $v and a later step report exists ($report). The held step must reach PASS before any later step is worked. Answer the HOLD items, re-invoke the gating-supervisor on that step, and do not proceed until it passes."
      exit 0
    fi
  fi
done

block() {
  printf '{"decision":"block","reason":%s}\n' "$(printf '%s' "$1" | "$PY_BIN" -c 'import json,sys;print(json.dumps(sys.stdin.read()))')"
  exit 0
}

if [ ! -f "$review" ]; then
  block "Step report $report has no supervisor verdict at $review. Invoke the gating-supervisor subagent on this step before ending the turn. Do not write the verdict yourself."
fi

# Report or code changed since the verdict's reviewed commit: the step was
# reworked after review. Uses git, not mtimes, so a fresh clone cannot trip it.
#
# tests/corpus/ is EXCLUDED because it is the reviewer's, not the implementer's
# (BE3): the supervisor commits its adversarial corpus after the commit it
# reviewed, so counting it as implementer rework made every review that opened a
# corpus demand a re-review of itself. docs/reviews/ is exempt for the same
# reason and was never in this list. The exclusion does not widen what the
# implementer can change unseen -- protect-reviews.sh denies it those paths --
# but note the KNOWN LIMITATION both hooks share: they see Write|Edit|MultiEdit,
# not a shell redirect through Bash.
reviewed=$(grep -m1 -E '^Reviewed commit:' "$review" | awk '{print $3}')
if [ -n "$reviewed" ] && git cat-file -e "$reviewed" 2>/dev/null; then
  if ! git diff --quiet "$reviewed" -- "$report" floatfea tests ':(exclude)tests/corpus' 2>/dev/null; then
    block "floatfea/, tests/, or $report changed since the verdict at $reviewed. Re-invoke the gating-supervisor so the verdict covers the current state."
  fi
fi

verdict=$(grep -m1 -E '^Verdict:' "$review" | awk '{print $2}')
case "$verdict" in
  PASS) exit 0 ;;
  HOLD|STOP)
    # A HOLD/STOP on the newest report is fine to stop on — the implementer
    # must now answer it. What is not fine is a later report existing while
    # an earlier one holds; that is caught because the newest report is the
    # one with the HOLD. Nothing further to check.
    exit 0 ;;
  *)
    block "$review carries no recognisable Verdict line (PASS|HOLD|STOP). Re-invoke the gating-supervisor." ;;
esac
