#!/usr/bin/env sh
# Run one rung of the verification ladder, with its expectation DECLARED (CB1).
#
# Usage:  run_rung.sh full:tests/verification/rung1
#         run_rung.sh empty:tests/verification/rung6 full:tests/regression
#
# WHY THIS IS A SCRIPT AND NOT INLINE YAML. The inline version could not be run
# anywhere but on GitHub, so its claims about what it catches had a corpus of
# zero -- and when the reviewer built ten layouts, five of them were wrong.
# `tests/test_ci_ladder_gating.py` runs this file against all ten.
#
# WHAT WENT WRONG WITH THE VERSION THIS REPLACES. It decided empty-versus-
# populated from a shell glob, so:
#   * `ls A B` exits non-zero when EITHER glob fails, and rung 6's own rung
#     directory is empty by design -- so `tests/regression` NEVER RAN and the
#     job reported green;
#   * a renamed rung directory went from exit 4 to exit 0, and a failing test
#     one directory down reported green.
# A glob that matches nothing is indistinguishable, to that guard, from a
# directory that is not there. The expectation is declared here instead, so an
# emptied or renamed directory contradicts the declaration and reddens.
set -eu

RUN_DIRS=""
STATUS=0

fail() {
    echo "run_rung: FAIL -- $1" >&2
    STATUS=1
}

for arg in "$@"; do
    kind=${arg%%:*}
    dir=${arg#*:}

    if [ ! -d "$dir" ]; then
        fail "$dir does not exist. A rung directory that is renamed or removed is
        a defect, not an empty rung."
        continue
    fi

    # `--collect-only` separates "there are no tests" from "the tests failed",
    # which is the distinction pytest's exit code 5 collapses into the same
    # value as several real defects.
    set +e
    python -m pytest "$dir" -q --collect-only >/dev/null 2>&1
    collect=$?
    set -e

    case "$collect" in
        0) count=some ;;
        5) count=none ;;
        *) fail "$dir: collection itself errored (pytest exit $collect) -- a
        broken import or a collection error, never an empty rung."
           continue ;;
    esac

    if [ "$kind" = "empty" ]; then
        if [ ! -f "$dir/.empty-by-design" ]; then
            fail "$dir is declared empty and carries no .empty-by-design marker.
        The marker is what separates a rung nobody has written yet from one
        whose tests have gone missing."
            continue
        fi
        if [ "$count" != "none" ]; then
            fail "$dir is declared empty and collects tests. Remove the
        .empty-by-design marker and declare it full."
        fi
        echo "run_rung: $dir -- empty by design, nothing to run"
    else
        if [ "$count" = "none" ]; then
            fail "$dir is declared full and collects nothing. Exit 5 is a
        failure here: a renamed file, a lost test prefix, or tests moved
        elsewhere all look like this."
            continue
        fi
        RUN_DIRS="$RUN_DIRS $dir"
    fi
done

[ "$STATUS" -eq 0 ] || exit 1

if [ -n "$RUN_DIRS" ]; then
    # shellcheck disable=SC2086
    python -m pytest $RUN_DIRS -q
fi
