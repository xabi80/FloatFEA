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

# `block` is defined HERE, above its first use, and that is the whole of the change
# to it. The refusals FH0 adds below run BEFORE the point it used to be defined at,
# and bash resolves a function at CALL time -- so an earlier call printed
# `block: command not found` and, with `set -u` but no `set -e`, the script CARRIED
# ON PAST THE REFUSAL. A guard that cannot refuse is worse than one that is absent.
block() {
  printf '{"decision":"block","reason":%s}\n' "$(printf '%s' "$1" | "$PY_BIN" -c 'import json,sys;print(json.dumps(sys.stdin.read()))')"
  exit 0
}


# THE ACTIVE STEP COMES FROM THE PLAN'S MARKER, NOT FROM SORTING PATHS (FH0).
#
# It used to rank `docs/reports/F*/step-*.md` with
#     m=$3; sub(/^F/,"",m); printf "%03d %03d", m+0, s+0
# and take the last. `m+0` on a SUFFIXED milestone takes its integer part, so `6a`
# became `6`:
#
#     006 001 docs/reports/F6/step-1.md
#     006 001 docs/reports/F6a/step-1.md      <-- collides with F6 step 1
#     006 002 docs/reports/F6/step-2.md       <-- and loses on 2 > 1
#
# so the whole of F6a was gated against F6 step 2's verdict and its reviewed commit.
# The comparison base was a commit in the past, `floatfea`/`tests` had differed from
# it since F6a's first step commit, and NO commit and NO verdict could clear it -- a
# verdict written into F6a's review file does not touch the file the ranking picked.
# Three interim checks were forced by it, all three PASS.
#
# This is EC0 a second time, one notch less visible: EC0 ranked every report at
# milestone `000`, and this ranked a suffixed milestone at its base.
#
# AND EC0's LOUD-FAILURE GUARD COULD NOT SEE IT, which is the part worth keeping.
# `if (m !~ /^[0-9]/)` asks whether the field STARTS with a digit, and `6a` does;
# the defect was that it is not WHOLLY a digit after the documented suffix. EC0's
# own comment says why that survives: "printing `000` for it is what let the defect
# survive: the ranking stayed plausible."
#
# So the milestone and the step are read from the one place that already decides
# them: the `<!-- step-under-execution: N -->` marker. That is the resolver
# `tests/test_report_carried.py::_active_plan` uses, and
# `test_the_plan_names_the_step_under_execution` holds it to EXACTLY ONE plan, so
# the milestone cannot advance without the previous plan's marker being retired.
#
# THE PATTERN IS STRICT AND THAT IS LOAD-BEARING. A retired marker reads
# `<!-- step-under-execution: moved to F3 at step 1 (DY8c) -->`, so requiring
# `[0-9]+` between the colon and `-->` is what separates the live marker from the
# four retired ones and from prose naming it. A loose grep for the phrase finds
# five files; this finds one.
marker_re='<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->'
plans=$(grep -lE "$marker_re" docs/milestones/F*.md 2>/dev/null || true)
plan_count=$(printf '%s' "$plans" | grep -c . || true)

# A TIE IS REFUSED, NEVER BROKEN BY PATH STRING (FH0). The old ranking resolved a
# collision with `sort | tail -1` -- alphabetically -- so which milestone this hook
# gated was an accident of spelling. Two live markers is the state `_active_plan`'s
# docstring calls impossible by construction; if it happens, the answer is not to
# pick one of them.
if [ "$plan_count" -ne 1 ]; then
  block "require-verdict: $plan_count plans carry a live step-under-execution marker$([ -n "$plans" ] && printf ' (%s)' "$(printf '%s' "$plans" | tr '\n' ' ')"). EXACTLY ONE must. With none, nothing is under execution and this hook has no report to read. With two, the milestone advanced without the previous plan's marker being retired -- and the ranking this replaced would have silently picked whichever path sorted last (FH0). Retire the stale marker, or add the missing one."
fi

milestone=$(basename "$plans" .md)
step=$(grep -oE "$marker_re" "$plans" | head -1 | grep -oE '[0-9]+')

# THE MILESTONE LABEL IS WHOLLY NUMERIC AFTER ITS ONE OPTIONAL SUFFIX LETTER (FH0).
# EC0's guard with the hole closed: not "starts with a digit" but "a digit run, then
# at most one lowercase letter, and nothing else". `F6` and `F6a` pass; `F6ab`,
# `Freports` and `F6-draft` are refused rather than ranked plausibly.
case "$milestone" in
  F*) m_body=${milestone#F} ;;
  *)  m_body="" ;;
esac
if ! printf '%s' "$m_body" | grep -qE '^[0-9]+[a-z]?$'; then
  block "require-verdict: cannot read a milestone label from $plans (got '$milestone'). A label is F<digits> with at most one lowercase suffix letter -- F6, F6a. EC0's guard asked only whether the field STARTS with a digit, which is how F6a passed it while ranking as 6 (FH0)."
fi
if [ -z "$step" ]; then
  block "require-verdict: $plans carries a step-under-execution marker with no readable step number. The marker is the single source for which step is under execution (FH0)."
fi

report="docs/reports/$milestone/step-$step.md"
if [ ! -f "$report" ]; then
  block "require-verdict: $plans says step $step of $milestone is under execution and $report does not exist. The marker is advanced in the commit that adds the next step's report, never before it."
fi

review=${report/docs\/reports/docs\/reviews}

# Any earlier step still on HOLD/STOP while a later report exists is a
# violation regardless of what the newest review says.
stepnum() { local s=${1##*step-}; echo "${s%.md}"; }

# DD1/DE1: A STEP'S DISPOSITION IS ITS CLOSURE VERDICT, NOT THE FILE'S LAST
# LINE. A verdict file accumulates every verdict written on that step, and
# once a step has closed, later verdicts in the same file are about the state
# of the TREE -- they do not reopen the step. Reading only the header made
# this hook refuse every turn after step 5 closed at verdict 53: two
# tree-rounds were written into its file, the header read HOLD, and the
# refusal had no exit, because a verdict on step 5 could not clear a step-6
# report and a verdict on step 6 was what the refusal was preventing. It cost
# two verdicts, neither about the work, and `CLAUDE.md` § Step gating calls
# that a guard failing false.
#
# So a step counts as closed when ANY verdict in its file is a PASS.
# `grep -c` over `^Verdict: *PASS` rather than the first line only.
closed_by_a_pass() { grep -cE '^Verdict: *PASS' "$1" 2>/dev/null | grep -qv '^0$'; }

for r in $(ls docs/reviews/F*/step-*.md 2>/dev/null); do
  [ "$r" = "$review" ] && continue
  v=$(grep -m1 -E '^Verdict:' "$r" | awk '{print $2}')
  if closed_by_a_pass "$r"; then
    continue
  fi
  if [ "$v" = "HOLD" ] || [ "$v" = "STOP" ]; then
    # Same milestone, and the newest report is a later step than the held one.
    if [ "$(dirname "$r")" = "$(dirname "$review")" ] && [ "$(stepnum "$report")" -gt "$(stepnum "$r")" ]; then
      printf '{"decision":"block","reason":"%s"}\n' \
        "$r is $v and a later step report exists ($report). The held step must reach PASS before any later step is worked. Answer the HOLD items, re-invoke the gating-supervisor on that step, and do not proceed until it passes."
      exit 0
    fi
  fi
done

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
# THE REVIEWED COMMIT IS CHOSEN BY ANCESTRY, NOT BY FILE ORDER (FH0).
#
# This was `grep -m1`, and `-m1` was CORRECT for the convention: `write_verdict.py`
# PREPENDS, so a verdict file is newest-first (DY6), and C105 recorded `re.search`
# as right for the same reason. Measured in F6 step 2's file, which carries eight
# distinct reviewed commits across 3431 lines: the first is `bf5fdf0`, and
# `bf5fdf0` is the one every other listed commit is an ancestor of. **So `-m1`
# returned the NEWEST, and an earlier claim of mine that it returned the oldest
# (R798) was wrong and is withdrawn.**
#
# It is replaced anyway, because it depended on file ORDER in a file whose order is
# a convention one generator holds in place. Ancestry does not depend on it: the
# newest reviewed commit is the one every other listed commit is an ancestor of. If
# no single such commit exists -- a rebase, a cherry-pick, two branches' verdicts in
# one file -- the hook REFUSES, for the same reason a tie above is refused.
pick_reviewed() {
  local file=$1 shas sha other ok found=""
  shas=$(grep -E '^Reviewed commit:' "$file" | awk '{print $3}' | awk 'NF' | sort -u)
  if [ -z "$shas" ]; then
    REVIEWED_PICK=""
    REVIEWED_WHY="no 'Reviewed commit:' line"
    return 1
  fi
  for sha in $shas; do
    git cat-file -e "$sha" 2>/dev/null || continue
    ok=1
    for other in $shas; do
      [ "$other" = "$sha" ] && continue
      git cat-file -e "$other" 2>/dev/null || continue
      git merge-base --is-ancestor "$other" "$sha" 2>/dev/null || { ok=0; break; }
    done
    if [ "$ok" = 1 ]; then
      if [ -n "$found" ]; then
        REVIEWED_PICK=""
        REVIEWED_WHY="two commits ($found and $sha) each have every other listed commit as an ancestor"
        return 1
      fi
      found=$sha
    fi
  done
  if [ -z "$found" ]; then
    REVIEWED_PICK=""
    REVIEWED_WHY="no single commit among [$(printf '%s' "$shas" | tr '\n' ' ')] has every other as an ancestor"
    return 1
  fi
  REVIEWED_PICK=$found
  REVIEWED_WHY="every other listed commit is its ancestor"
  return 0
}

REVIEWED_PICK=""
REVIEWED_WHY=""
if pick_reviewed "$review"; then
  reviewed=$REVIEWED_PICK
elif [ "$REVIEWED_WHY" = "no 'Reviewed commit:' line" ]; then
  # Unchanged behaviour: an empty `reviewed` skips the comparison below, exactly as
  # a missing line did before. A verdict with no reviewed commit is the reviewer's
  # own defect and `write_verdict.py` stamps it, so this hook does not duplicate it.
  reviewed=""
else
  block "require-verdict: cannot choose the reviewed commit in $review -- $REVIEWED_WHY. The newest reviewed commit is the one every other listed commit is an ancestor of; with no single such commit this hook refuses rather than taking one by file order (FH0)."
fi

# EVERY FINDING IN THE NEWEST VERDICT IS CARRIED BY THE NEWEST REPORT (BS0).
# Twice in three rounds the report's `Carried` section dropped a whole verdict's
# findings -- eleven items once, five of them blocking or STOP-class, four
# untouched in the repository -- and both times a review caught it rather than
# the build. CLAUDE.md's dependency-list rule is the point of the arrangement;
# this makes it mechanical.
#
# PLACED BEFORE THE DIRTY-TREE BRANCH, because it was placed after it and could
# therefore never run (R153): that branch blocks and exits whenever the report or
# `floatfea`/`tests` differs from the reviewed commit, and the report is inside
# its pathspec, so the two conditions were mutually exclusive. The evidence for
# "this is now a build failure" was a manual invocation.
#
# AND THE REAL GUARD IS NOW A TEST, `tests/test_report_carried.py`. Five hook
# defects in this milestone say the hook is the wrong home for anything that must
# run; the supervisor runs pytest, so an incomplete Carried is red inside the
# verdict that reads it. This call stays as a fast local signal, not as the
# mechanism.
#
# It runs only when the report is NEWER than the verdict it must carry, i.e.
# after the implementer has answered. Before that the report legitimately
# predates the findings and carrying them is impossible.
#
# WHAT IT CANNOT CHECK: whether the status written beside each carried item is
# true. A report can carry R142 and lie about it. That half is the reviewer's.
if [ -n "$reviewed" ] && git cat-file -e "$reviewed" 2>/dev/null; then
  if git diff --quiet "$reviewed" -- "$report" 2>/dev/null; then
    : # report unchanged since the reviewed commit: nothing to carry yet
  elif command -v python >/dev/null 2>&1 || command -v python3 >/dev/null 2>&1; then
    PY_BIN=$(command -v python3 || command -v python)
    if ! carried=$("$PY_BIN" "scripts/check_carried.py" --verdict "$review" --report "$report" 2>&1); then
      block "$carried  -- CLAUDE.md requires the next report's Carried section to list every open item, and BS0 makes that a build failure rather than a review finding."
    fi
  fi
fi

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
