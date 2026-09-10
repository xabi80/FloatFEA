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

# AT LEAST ONE ARGUMENT. With none the loop never runs and the script printed
# `OK -- 0 director(y|ies) ran`: a job wired to nothing announced success.
if [ "$#" -eq 0 ]; then
    echo "run_rung: FAIL -- no arguments. A rung job that names no directory" >&2
    echo "        runs nothing and must not report success." >&2
    exit 1
fi

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

    # THE PREFIX IS EXACT. `${arg%%:*}` returns the whole string when there is
    # no colon, so a bare path ran as `full:` and a capitalised `Empty:` fell
    # through the `empty` branch into `full` -- a declaration the script did not
    # understand became the permissive one.
    case "$kind" in
        full|empty) ;;
        *) fail "\`$arg\` has no \`full:\` or \`empty:\` prefix. An argument the
        script does not understand must not default to the permissive reading."
           continue ;;
    esac

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
    report=$(mktemp)
    # `xfail_strict`: an XPASS is a failure here. A rung whose only test is
    # marked xfail and then passes exits 0 by default, and the junit report
    # records it as a pass -- so the rung reported success while asserting the
    # opposite of what it says.
    out=$(python -m pytest "$@" -q -o xfail_strict=true --junit-xml="$report" 2>&1) || {
        echo "$out"
        exit 1
    }
    echo "$out"
    # A RUNG WHOSE TESTS ARE ALL SKIPPED IS NOT A RUNG THAT PASSED. `CLAUDE.md`
    # forbids a skip and an xfail in the same sentence, and pytest exits 0 for a
    # run that did either to everything -- so without this the ladder reports
    # green on a rung that asserted nothing.
    #
    # READ FROM THE SUMMARY LINE ONLY. Grepping the whole output matched a
    # PASSING test whose own diagnostic contained the word, and reddened a rung
    # that had skipped nothing.
    # READ FROM PYTEST'S OWN REPORT, not from the tail of stdout. Anything the
    # process prints after the summary -- an `atexit` hook, a plugin, a
    # subprocess -- became the line `tail -1` picked, so a rung that skipped
    # nothing could be reddened by a string, and one that skipped everything
    # could hide behind a later line.
    if grep -qE '(skipped|xfail)="[1-9]' "$report" 2>/dev/null; then
        fail "$(grep -oE '(skipped|xfail[a-z]*)=\"[0-9]+\"' "$report" | tr '
' ' ')
        -- a test in $* was skipped or xfailed. CLAUDE.md: never skip a test or
        mark it xfail to get a green build. Report the failure instead."
        exit 1
    fi
fi

# PRINTED ONLY AFTER EVERY CHECK HAS PASSED, and only for what was actually
# declared empty. The previous version printed its success line inside the loop,
# so a rung that failed later still announced that it had nothing to run.
echo "run_rung: OK -- $RUN_COUNT director(y|ies) ran"
