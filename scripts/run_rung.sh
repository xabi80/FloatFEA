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

    # THE OUTCOME IS READ FROM THE JUNIT REPORT AND THE EXIT CODE, NEVER FROM
    # STDOUT (CG4). Every version that parsed the terminal output was defeated
    # by text some other part of the process controls, and each fix moved the
    # forgery one step earlier:
    #
    #   tail -1        an `atexit` hook printing after the summary
    #   head -1        `-ra`'s short summary, carrying an xfail `reason=` or a
    #                  parametrize id, printed BEFORE the count line
    #   --no-header    a conftest `pytest_report_header`
    #   and still:     `warnings.warn("3 passed in 0.01s")`, and a conftest
    #                  `pytest_terminal_summary`
    #
    # There is no last position in that list. A clean rung whose test merely
    # WARNS the word was reddened by the same rule, which is the mirror defect.
    # `--junit-xml` is pytest's own structured account of what it did, and a
    # test cannot write another test's element.
    # `-p rung_no_xpass` turns an unexpected pass into a FAILING report entry,
    # which is the only structured signal for it: a marker's explicit
    # `strict=False` overrides the project's `xfail_strict`, and pytest's junit
    # records such a case as a plain pass. See `scripts/rung_no_xpass.py`.
    #
    # THE REACH, so the gate is not trusted past it. Two inputs are read and no
    # others: the junit report and pytest's exit code. Nothing a test, a
    # conftest, a plugin or an `atexit` hook PRINTS is read at all -- which is
    # why a module-level `print("1 passed")` is no longer caught here and no
    # longer needs to be: it is not a forgery of anything this reads.
    #
    # WHAT THIS GATE CANNOT DO, STATED AS A PROPERTY RATHER THAN AS A LIST.
    # Everything it reads is writable from a rung's own `conftest.py`. The
    # previous version of this comment enumerated three producers and called
    # them "edits to the harness"; the reviewer measured four channels and
    # three were unlisted:
    #
    #   pytest_runtest_makereport      a hookwrapper flipping a failing report
    #                                  to passing -- the same hook the repair
    #                                  in rung_no_xpass.py uses, in reverse
    #   pytest_ignore_collect          the failing file never collected
    #   pytest_collection_modifyitems  the failing item dropped from the run
    #   pytest_sessionfinish           the XML rewritten after pytest wrote it
    #
    # The first three leave a green junit report that is an accurate record of
    # a run that did not include the failure. NO GATE CLOSES THIS: a gate that
    # reads a record cannot outrank code that writes the record, and the same
    # is true of any replacement for this script.
    #
    # TWO RECORDS OF ONE RUN, AND THEY MUST AGREE (CI0). `-p rung_no_xpass`
    # tallies the session independently and writes `$RUNG_TALLY`; the reader
    # below compares that tally with the junit XML on collected, failed and
    # skipped, and a disagreement reddens the rung. A conftest that drops a
    # failing item now has to defeat both records consistently instead of one.
    # THAT IS A COST, NOT A WALL: both are written inside the same session and
    # a conftest can reach both.
    #
    # WHAT PROTECTS A RUNG IS THEN REVIEW OF ITS CONFTEST -- the LAST bound,
    # not the whole of the answer. `docs/SUPERVISOR.md` item 4c and
    # `.claude/agents/gating-supervisor.md` item 4c diff
    # `tests/conftest.py 'tests/**/conftest.py'` at every step, beside
    # `floatfea/tolerances.py`. BOTH PATHS, because the double star alone
    # matches nothing: git will not let it stand for zero directories, and the
    # only conftest in this repository is at depth one -- where it applies to
    # every rung at once.
    # `set +e` AROUND THE RUN. With `set -e` in force a failing pytest
    # killed the script on the spot: `code=$?` never ran, the junit reader
    # below never ran, and a red rung exited 1 having printed NOTHING --
    # no count, no reason, no name. It still went red, so it looked like a
    # working gate; what was lost was everything that says WHICH test
    # failed, and every `exit 1` measured through this path was measuring
    # the shell rather than the reader it was supposed to be measuring.
    tally=$(mktemp)
    set +e
    RUNG_TALLY="$tally" \
    PYTHONPATH="$(cd "$(dirname "$0")" && pwd)${PYTHONPATH:+:$PYTHONPATH}" \
        python -m pytest "$@" -q -p rung_no_xpass -o xfail_strict=true \
        --junit-xml="$report" >/dev/null 2>&1
    code=$?
    python - "$report" "$code" "$*" "$tally" <<'PY'
import sys
from xml.etree import ElementTree

report, code, where = sys.argv[1], int(sys.argv[2]), sys.argv[3]
tally = sys.argv[4] if len(sys.argv) > 4 else ""
try:
    root = ElementTree.parse(report).getroot()
except Exception as exc:
    sys.exit(f"run_rung: FAIL -- {where} produced no readable junit report ({exc}); "
             f"pytest exited {code} and nothing describes what it did.")

cases = list(root.iter("testcase"))
if not cases:
    sys.exit(f"run_rung: FAIL -- {where} collected nothing. Exit {code}. A rung "
             "that reports a result about no tests is the failure this reads for.")

bad = {"failure": 0, "error": 0, "skipped": 0}
for case in cases:
    for child in case:
        if child.tag in bad:
            bad[child.tag] += 1

print(f"run_rung: {len(cases)} collected, "
      f"{bad['failure']} failed, {bad['error']} errored, {bad['skipped']} skipped")

# THE NAMES, FROM THE REPORT THAT ALREADY HOLDS THEM (R311d). The repair that
# restored the count and the reason did not restore a name, and a rung that
# says "13 failed" sends the reader to the log the gate exists to replace.
for case in cases:
    for child in case:
        if child.tag in ("failure", "error", "skipped"):
            who = f"{case.get('classname', '')}::{case.get('name', '')}".strip(":")
            print(f"run_rung:   {child.tag}  {who}")

# TWO RECORDS, CROSS-CHECKED (CI0). The junit XML and the plugin's own tally
# are written by the same session, so a conftest can reach both -- but it has
# to reach both CONSISTENTLY, and one rewritten hook now reddens here.
if tally:
    try:
        seen = open(tally, encoding="utf-8").read().split()
    except OSError:
        seen = []
    if len(seen) != 3:
        sys.exit(f"run_rung: FAIL -- {where}: the plugin wrote no tally. "
                 "`-p rung_no_xpass` did not load, or something unloaded it, "
                 "and the cross-check that makes one forged record insufficient "
                 "is not running.")
    mine = (len(cases), bad["failure"] + bad["error"], bad["skipped"])
    theirs = tuple(int(x) for x in seen)
    if mine != theirs:
        sys.exit(f"run_rung: FAIL -- {where}: the two records of this run "
                 f"disagree. junit says {mine} (collected, failed, skipped) and "
                 f"the plugin tallied {theirs}. One of them was written by "
                 "something other than the run.")

if bad["skipped"]:
    sys.exit(f"run_rung: FAIL -- {bad['skipped']} skipped in {where}. CLAUDE.md: "
             "never skip a test to get a green build. Report the failure instead.")
if bad["failure"] or bad["error"]:
    sys.exit(f"run_rung: FAIL -- {where} is red.")
if code != 0:
    sys.exit(f"run_rung: FAIL -- pytest exited {code} with no failing case. An "
             "unexpected pass under `xfail_strict` lands here, and so does a "
             "usage error; either way the rung did not pass.")
PY
    verdict=$?
    set -e
    [ "$verdict" -eq 0 ] || exit 1
fi

# PRINTED ONLY AFTER EVERY CHECK HAS PASSED, and only for what was actually
# declared empty. The previous version printed its success line inside the loop,
# so a rung that failed later still announced that it had nothing to run.
echo "run_rung: OK -- $RUN_COUNT director(y|ies) ran"
