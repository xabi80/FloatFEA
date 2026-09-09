#!/usr/bin/env sh
# Run one rung of the verification ladder, with its expectation DECLARED.
#
# Usage:  run_rung.sh full:tests/verification/rung1
#         run_rung.sh empty:tests/verification/rung6 full:tests/regression
#
# WHY THIS IS A SCRIPT AND NOT INLINE YAML. The inline version could not be run
# anywhere but on GitHub, so its claims about what it catches had a corpus of
# zero -- and when the reviewer built layouts, half of them were wrong.
# `tests/test_ci_ladder_gating.py` runs this file against all of them, and that
# file is executed by the `guards` job, so the claim is checked where it is made.
#
# WHAT WENT WRONG WITH THE VERSIONS THIS REPLACES.
#   * The first decided empty-versus-populated from a shell glob. `ls A B` exits
#     non-zero when EITHER glob fails, and rung 6's own directory is empty by
#     design -- so `tests/regression` NEVER RAN and the job reported green. A
#     renamed rung went from exit 4 to exit 0, and a failing test one directory
#     down passed silently.
#   * The second declared the expectation but still let four states through: a
#     `full:` directory carrying a stale `.empty-by-design` marker, a rung whose
#     every test is skipped, a path containing a space, and a success line
#     printed for a rung that had already failed.
#
# A glob that matches nothing is indistinguishable, to a guard, from a directory
# that is not there. The expectation is declared here instead, so an emptied or
# renamed directory contradicts the declaration and reddens.
set -eu

STATUS=0
RUN_COUNT=0
set -- "$@" --end--

fail() {
    echo "run_rung: FAIL -- $1" >&2
    STATUS=1
}

# Positional parameters carry the directories to run, so a path containing a
# space survives. `$RUN_DIRS` as a string did not: the shell re-split it and the
# rung silently ran two directories that do not exist.
while [ "$1" != "--end--" ]; do
    arg=$1
    shift
    kind=${arg%%:*}
    dir=${arg#*:}

    if [ ! -d "$dir" ]; then
        fail "$dir is not a directory. A rung path that is renamed, removed, or
        replaced by a file is a defect, not an empty rung."
        continue
    fi

    marker="$dir/.empty-by-design"

    # `--collect-only` separates "there are no tests" from "the tests failed",
    # which is the distinction pytest's exit code 5 collapses into one value
    # with several real defects.
    set +e
    python -m pytest "$dir" -q --collect-only >/dev/null 2>&1
    collect=$?
    set -e

    case "$collect" in
        0) count=some ;;
        5) count=none ;;
        *) fail "$dir: collection itself errored (pytest exit $collect) -- a
        broken import, a conftest that raises, or a collection error. Never an
        empty rung."
           continue ;;
    esac

    if [ "$kind" = "empty" ]; then
        if [ ! -f "$marker" ]; then
            fail "$dir is declared empty and carries no .empty-by-design marker.
        The marker is what separates a rung nobody has written yet from one
        whose tests have gone missing."
            continue
        fi
        if [ "$count" != "none" ]; then
            fail "$dir is declared empty and collects tests. The declaration is
        stale: delete the marker and change empty: to full: in the same commit."
        fi
    else
        if [ -f "$marker" ]; then
            fail "$dir is declared full and still carries .empty-by-design. Two
        declarations that contradict each other are worse than either, because
        whichever is read first looks authoritative."
            continue
        fi
        if [ "$count" = "none" ]; then
            fail "$dir is declared full and collects nothing. Exit 5 is a
        failure here: a renamed file, a lost test prefix, or tests moved
        elsewhere all look exactly like this."
            continue
        fi
        set -- "$@" "$dir"
        RUN_COUNT=$((RUN_COUNT + 1))
    fi
done
shift  # drop --end--

[ "$STATUS" -eq 0 ] || exit 1

if [ "$RUN_COUNT" -gt 0 ]; then
    out=$(python -m pytest "$@" -q 2>&1) || {
        echo "$out"
        exit 1
    }
    echo "$out"
    # A RUNG WHOSE TESTS ARE ALL SKIPPED IS NOT A RUNG THAT PASSED. `CLAUDE.md`
    # forbids a skip outright, and pytest exits 0 for a run that skipped
    # everything -- so without this the ladder reports green on a rung that
    # asserted nothing.
    case "$out" in
        *skipped*) fail "a test in $* was skipped. CLAUDE.md: never skip a test
        to get a green build -- report the failure instead."
                   exit 1 ;;
    esac
fi

# PRINTED ONLY AFTER EVERY CHECK HAS PASSED, and only for what was actually
# declared empty. The previous version printed its success line inside the loop,
# so a rung that failed later still announced that it had nothing to run.
echo "run_rung: OK -- $RUN_COUNT director(y|ies) ran"
