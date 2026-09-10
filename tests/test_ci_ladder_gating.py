"""The ladder's CI gate, run against the reviewer's layouts (CB1).

`.github/workflows/ci.yml` orders the verification ladder by dependency: a red
rung stops every rung above it from running at all, so nobody can investigate a
rung 5 discrepancy while rung 1 is red. That ordering is the ladder's whole
value, and it rests on each rung job reporting honestly.

**It did not.** The job body was inline YAML, so it could not be run anywhere
but on GitHub, and its claims about which defects it catches had a corpus of
zero. The reviewer built ten layouts and five were wrong -- including
`ci_rung6_live`, which is not a hypothesis but this repository as it stood:
rung 6's own directory is empty by design, `ls A B` exits non-zero when EITHER
glob fails, and so `tests/regression` never ran while the job reported green.

`scripts/run_rung.sh` exists so the logic can be executed here. The expectation
is DECLARED per directory -- `full:` or `empty:` -- rather than inferred from
what happens to be on disk, because a directory that has been emptied and one
nobody has written yet look identical to a glob and are opposite facts.

THE CORPUS IS THE REVIEWER'S. `tests/corpus/ci_ladder_gating.txt` is test DATA
and the implementer does not edit it. Two entries require an outcome the
declared-expectation rule deliberately changes, and they are listed in
`REQUIREMENT_CHANGED` with the reason rather than quietly re-measured.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "tests" / "corpus" / "ci_ladder_gating.txt"
SCRIPT = ROOT / "scripts" / "run_rung.sh"

# Entries whose required outcome CHANGES under the declared-expectation rule,
# with the reason. Both changes are the rule getting STRICTER, which is what
# CB1 asked for; neither is a re-measurement of the reviewer's number.
#
# The corpus was written against a guard that inferred empty-versus-populated
# from disk. Under that guard "a rung with nothing in it" is a pass. Under this
# one it is a pass only when the rung DECLARES itself empty and carries the
# marker -- because an emptied rung and an unwritten one are opposite facts and
# a glob cannot tell them apart. Recorded for the reviewer to rule on.
# WHAT THE SHIPPED GATE DOES WHERE IT DOES NOT DO WHAT THE ENTRY REQUIRES,
# and in WHICH DIRECTION. The first version held only strings and its branch
# asserted `code != 0`, which was right for both entries it had and would have
# silently asserted the opposite of the truth for the conftest channels below.
# The declared outcome is written down and asserted.
REQUIREMENT_CHANGED: dict[str, tuple[str, str]] = {
    "ci_rung_genuinely_empty": (
        "fail",
        "require=pass under an inferred rule. Rung 1 is declared `full:` in the "
        "workflow, so a rung 1 holding only __init__.py now FAILS -- that is "
        "the emptied-directory case CB1 asks to redden",
    ),
    "ci_rung6_both_populated": (
        "fail",
        "require=run under an inferred rule. Rung 6's own directory is declared "
        "`empty:`, so a test appearing in it now FAILS as a stale declaration "
        "rather than being run silently",
    ),
    # R302. THE GATE DOES NOT CLOSE THESE AND NO GATE IN THIS POSITION CAN.
    # Everything `scripts/run_rung.sh` reads -- the junit report, the exit code
    # -- is written by the session the rung runs in, so a `conftest.py` in the
    # rung's own directory can write it. The first three leave a junit report
    # that is an ACCURATE record of a run that did not contain the failure.
    # The bound is review: `tests/**/conftest.py` is in the supervisor's
    # per-step diff list (`docs/SUPERVISOR.md` item 4c). These entries are here
    # so that the day one of them starts reddening, this file says so.
    "ci_rung_full_conftest_makereport_wrapper_turns_a_FAILING_test_into_a_passing_report": (
        "pass",
        "require=fail. A conftest hookwrapper on `pytest_runtest_makereport` "
        "flips the failing call report to `passed` before the junit writer "
        "sees it -- the same hook `scripts/rung_no_xpass.py` uses, in the "
        "opposite direction. The report the gate reads is green and honest "
        "about what it was handed",
    ),
    "ci_rung_full_conftest_pytest_ignore_collect_hides_the_FAILING_test_file": (
        "pass",
        "require=fail. The failing FILE is never collected, so no report of it "
        "exists to forge. Nothing in this repository records how many tests a "
        "rung is supposed to hold, which is the `.empty-by-design` argument "
        "one level down",
    ),
    "ci_rung_full_conftest_collection_modifyitems_drops_only_the_FAILING_item": (
        "pass",
        "require=fail. Assertion domain blindness in its plainest form: the "
        "collection the gate inspects cannot contain the failure",
    ),
    "ci_rung_full_conftest_pytest_sessionfinish_rewrites_the_junit_xml": (
        "pass",
        "require=fail. The one channel the old reach comment named -- and it "
        "named it as a plugin, when it works from a rung conftest",
    ),
}


def _entries() -> list[tuple[str, str, str]]:
    """`(id, layout, require)` for every corpus entry."""
    out: list[tuple[str, str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        f = dict(part.split("=", 1) for part in line.split() if "=" in part)
        out.append((f["id"], f["layout"], f["require"]))
    return out


ENTRIES = _entries()

PASSING = "def test_ok():\n    assert True\n"
FAILING = "def test_bad():\n    assert 1 == 2\n"
BROKEN = "import a_module_that_is_not_there\n\n\ndef test_ok():\n    assert True\n"
NO_PREFIX = "def check_ok():\n    assert True\n"
XFAILED = "\n".join(
    [
        "import pytest",
        "",
        "",
        '@pytest.mark.xfail(reason="the rung asserts nothing")',
        "def test_a():",
        "    assert 1 == 2",
        "",
    ]
)
SAYS_SKIPPED = "\n".join(
    [
        "def test_a():",
        '    assert True, "no case was skipped in this rung"',
        "",
    ]
)
ATEXIT_NOISE = "\n".join(
    [
        "import atexit",
        "",
        "",
        'atexit.register(lambda: print("1 skipped in 0.01s"))',
        "",
        "",
        "def test_ok():",
        "    assert True",
        "",
    ]
)
STRICT_FALSE_XPASS = "\n".join(
    [
        "import pytest",
        "",
        "",
        '@pytest.mark.xfail(strict=False, reason="explicitly non-strict")',
        "def test_a():",
        "    assert True",
        "",
    ]
)
MODULE_SKIP = "\n".join(
    [
        "import pytest",
        "",
        'pytest.skip("the whole module", allow_module_level=True)',
        "",
        "",
        "def test_a():",
        "    assert True",
        "",
    ]
)
COLLECT_IGNORE = 'collect_ignore = ["test_a.py"]\n'
XPASS_PLAIN = "\n".join(
    [
        "import pytest",
        "",
        "",
        "@pytest.mark.xfail(strict=False)",
        "def test_a():",
        "    assert True",
        "",
    ]
)
XPASS_REASON = "\n".join(
    [
        "import pytest",
        "",
        "",
        '@pytest.mark.xfail(strict=False, reason="1 passed on the reference build")',
        "def test_a():",
        "    assert True",
        "",
    ]
)
XPASS_PARAM_ID = "\n".join(
    [
        "import pytest",
        "",
        "",
        '@pytest.mark.parametrize("case", [pytest.param(1, id="3 passed")])',
        "@pytest.mark.xfail(strict=False)",
        "def test_a(case):",
        "    assert True",
        "",
    ]
)
XPASS_HEADER_CONFTEST = "\n".join(
    [
        "def pytest_report_header(config):",
        '    return "7 passed in 0.01s"',
        "",
    ]
)
XPASS_WARNING = "\n".join(
    [
        "import warnings",
        "",
        "import pytest",
        "",
        "",
        "@pytest.mark.xfail(strict=False)",
        "def test_a():",
        '    warnings.warn("3 passed in 0.01s")',
        "    assert True",
        "",
    ]
)
CLEAN_WARNS_XPASSED = "\n".join(
    [
        "import warnings",
        "",
        "",
        "def test_a():",
        '    warnings.warn("1 xpassed in 0.01s")',
        "    assert True",
        "",
    ]
)
XPASS_MODULE_PRINT = "\n".join(
    [
        "import pytest",
        "",
        'print("9 passed in 0.01s")',
        "",
        "",
        "@pytest.mark.xfail(strict=False)",
        "def test_a():",
        "    assert True",
        "",
    ]
)
TERMINAL_SUMMARY_CONFTEST = "\n".join(
    [
        "def pytest_terminal_summary(terminalreporter):",
        '    terminalreporter.write_line("5 passed in 0.01s")',
        "",
    ]
)
XPASSED = "\n".join(
    [
        "import pytest",
        "",
        "",
        '@pytest.mark.xfail(reason="expected to fail and does not")',
        "def test_a():",
        "    assert True",
        "",
    ]
)
SKIPPED = (
    "import pytest\n\n\n"
    '@pytest.mark.skip(reason="the rung asserts nothing")\n'
    "def test_a():\n    assert True\n"
)

# not-a-tolerance: the layout each entry names, built as files. This is a
# translation of the corpus's `layout=` field into a directory tree, not a
# threshold -- nothing here is compared against anything.
# ---------------------------------------------------------------------------
# R302: FOUR CHANNELS FROM A RUNG'S OWN `conftest.py`, and three controls.
#
# The gate reads pytest's junit report and pytest's exit code. Both are written
# by the same session the rung runs in, so a conftest in the rung's directory
# can write either. These are the reviewer's four, built here so the claim
# about them is a run rather than a sentence.
CONFTEST_MAKEREPORT = "\n".join(
    [
        "import pytest",
        "",
        "",
        "@pytest.hookimpl(hookwrapper=True, trylast=True)",
        "def pytest_runtest_makereport(item, call):",
        "    outcome = yield",
        "    rep = outcome.get_result()",
        "    if rep.when == 'call' and rep.failed:",
        "        rep.outcome = 'passed'",
        "        rep.longrepr = None",
    ]
)
CONFTEST_IGNORE_COLLECT = "\n".join(
    [
        "def pytest_ignore_collect(collection_path, config):",
        "    if collection_path.name == 'test_bad.py':",
        "        return True",
        "    return None",
    ]
)
CONFTEST_MODIFYITEMS_DROP_BAD = "\n".join(
    [
        "def pytest_collection_modifyitems(session, config, items):",
        "    items[:] = [i for i in items if 'bad' not in i.name]",
    ]
)
CONFTEST_MODIFYITEMS_DROP_ALL = "\n".join(
    [
        "def pytest_collection_modifyitems(session, config, items):",
        "    items[:] = []",
    ]
)
CONFTEST_SESSIONFINISH = "\n".join(
    [
        "from xml.etree import ElementTree",
        "",
        "",
        "def pytest_sessionfinish(session, exitstatus):",
        "    path = getattr(session.config.option, 'xmlpath', None)",
        "    if not path:",
        "        return",
        "    tree = ElementTree.parse(path)",
        "    for case in tree.getroot().iter('testcase'):",
        "        for kid in list(case):",
        "            if kid.tag in ('failure', 'error'):",
        "                case.remove(kid)",
        "    tree.write(path)",
        "    session.exitstatus = 0",
    ]
)
FAILING_TEST = "\n".join(["def test_a():", "    assert False"])
OK_AND_BAD = "\n".join(
    ["def test_ok():", "    assert True", "", "", "def test_bad():", "    assert False"]
)
PASSING_TEST = "\n".join(["def test_ok():", "    assert True"])
FAILING_TEST_BAD = "\n".join(["def test_bad():", "    assert False"])
XFAIL_THAT_FAILS = "\n".join(
    [
        "import pytest",
        "",
        "",
        "@pytest.mark.xfail(reason='known')",
        "def test_a():",
        "    assert False",
    ]
)

LAYOUTS: dict[str, dict[str, str | None]] = {
    "ci_rung6_live": {
        "tests/verification/rung6/__init__.py": "",
        "tests/verification/rung6/.empty-by-design": "marker",
        "tests/regression/test_golden.py": PASSING,
    },
    "ci_rung6_regression_removed": {
        "tests/verification/rung6/__init__.py": "",
        "tests/verification/rung6/.empty-by-design": "marker",
    },
    "ci_rung6_both_populated": {
        "tests/verification/rung6/__init__.py": "",
        "tests/verification/rung6/.empty-by-design": "marker",
        "tests/verification/rung6/test_r6.py": PASSING,
        "tests/regression/test_golden.py": PASSING,
    },
    "ci_rung_directory_renamed": {
        "tests/verification/rung_one/test_a.py": PASSING,
    },
    "ci_rung_genuinely_empty": {
        "tests/verification/rung1/__init__.py": "",
    },
    "ci_rung_file_collects_nothing": {
        "tests/verification/rung1/test_a.py": NO_PREFIX,
    },
    "ci_rung_file_broken_import": {
        "tests/verification/rung1/test_a.py": BROKEN,
    },
    "ci_rung_files_renamed_off_the_test_prefix": {
        "tests/verification/rung1/check_a.py": PASSING,
    },
    "ci_rung_has_a_failing_test": {
        "tests/verification/rung1/test_a.py": FAILING,
    },
    "ci_rung_tests_moved_into_a_subdirectory": {
        "tests/verification/rung1/sub/test_a.py": FAILING,
    },
    # --- the twenty-eighth verdict's twelve ---------------------------------
    "ci_rung6_stale_marker_rung_gains_a_passing_test": {
        "tests/verification/rung6/.empty-by-design": "marker",
        "tests/verification/rung6/test_r6.py": PASSING,
        "tests/regression/test_golden.py": PASSING,
    },
    "ci_rung2_stale_marker_rung_gains_a_failing_test": {
        "tests/verification/rung2/.empty-by-design": "marker",
        "tests/verification/rung2/test_a.py": FAILING,
    },
    "ci_rung_full_without_an_init_py": {
        "tests/verification/rung1/test_a.py": PASSING,
    },
    "ci_rung_conftest_raises_at_collection": {
        "tests/verification/rung1/test_a.py": PASSING,
        "tests/verification/rung1/conftest.py": BROKEN,
    },
    "ci_rung_declared_empty_but_directory_absent": {
        "tests/verification/other/keep.txt": "",
    },
    "ci_rung_path_is_a_file_not_a_directory": {
        "tests/verification/rung1": "",
    },
    "ci_rung_directory_is_a_symlink": {
        "tests/verification/real_rung/test_a.py": PASSING,
        "@symlink:tests/verification/rung1": "tests/verification/real_rung",
    },
    "ci_rung_every_test_is_skipped": {
        "tests/verification/rung1/test_a.py": SKIPPED,
    },
    "ci_rung_full_carries_a_stale_empty_by_design_marker": {
        "tests/verification/rung1/test_a.py": PASSING,
        "tests/verification/rung1/.empty-by-design": "marker",
    },
    "ci_rung_path_contains_a_space": {
        "tests/ver ification/rung1/test_a.py": PASSING,
    },
    "ci_rung6_second_dir_declared_full_collects_nothing": {
        "tests/verification/rung6/test_r6.py": PASSING,
        "tests/regression/keep.txt": "",
    },
    "ci_rung6_regression_present_but_empty": {
        "tests/verification/rung6/.empty-by-design": "marker",
        "tests/regression/keep.txt": "",
    },
    # --- the twenty-ninth verdict's seven ------------------------------------
    "ci_rung_full_every_test_is_xfail": {
        "tests/verification/rung1/test_a.py": XFAILED,
    },
    "ci_run_rung_with_no_arguments_at_all": {
        "tests/verification/rung1/test_a.py": PASSING,
    },
    "ci_argument_without_a_kind_prefix": {
        "tests/verification/rung1/test_a.py": PASSING,
    },
    "ci_passing_rung_whose_output_contains_the_word_skipped": {
        "tests/verification/rung1/test_a.py": SAYS_SKIPPED,
    },
    "ci_misspelled_kind_capital_Empty": {
        "tests/verification/rung2/.empty-by-design": "marker",
    },
    "ci_full_rung_with_a_failing_test_prints_no_OK_line": {
        "tests/verification/rung1/test_a.py": PASSING,
        "tests/verification/rung1/test_b.py": FAILING,
    },
    "ci_rung_full_xfail_marker_carries_strict_False_and_the_body_PASSES": {
        "tests/verification/rung1/test_a.py": STRICT_FALSE_XPASS,
    },
    "ci_rung_full_conftest_collect_ignore_silently_drops_a_test_file": {
        "tests/verification/rung1/test_a.py": PASSING,
        "tests/verification/rung1/conftest.py": COLLECT_IGNORE,
    },
    "ci_rung_full_module_level_pytest_skip_allow_module_level": {
        "tests/verification/rung1/test_a.py": MODULE_SKIP,
    },
    "ci_rung_full_xpass_whose_TEST_BODY_EMITS_A_WARNING_carrying_a_count_phrase": {
        "tests/verification/rung1/test_a.py": XPASS_WARNING,
    },
    "ci_rung_full_xpass_with_a_conftest_pytest_terminal_summary_writing_a_count_line": {
        "tests/verification/rung1/test_a.py": XPASS_PLAIN,
        "tests/verification/rung1/conftest.py": TERMINAL_SUMMARY_CONFTEST,
    },
    "ci_rung_full_CLEAN_rung_whose_warning_text_contains_the_word_xpassed": {
        "tests/verification/rung1/test_a.py": CLEAN_WARNS_XPASSED,
    },
    "ci_rung_full_xpass_with_a_MODULE_LEVEL_print_of_a_count_phrase_at_collection": {
        "tests/verification/rung1/test_a.py": XPASS_MODULE_PRINT,
    },
    "ci_rung_full_xpass_reason_count_phrase_WITH_the_projects_addopts_present_in_the_layout": {
        "tests/verification/rung1/test_a.py": XPASS_REASON,
    },
    "ci_rung_full_xpass_with_a_plain_strict_False_marker_and_no_free_text": {
        "tests/verification/rung1/test_a.py": XPASS_PLAIN,
    },
    "ci_rung_full_xpass_whose_xfail_REASON_string_carries_a_count_phrase": {
        "tests/verification/rung1/test_a.py": XPASS_REASON,
    },
    "ci_rung_full_xpass_whose_PARAMETRIZE_ID_carries_a_count_phrase": {
        "tests/verification/rung1/test_a.py": XPASS_PARAM_ID,
    },
    "ci_rung_full_xpass_with_a_conftest_pytest_report_header_carrying_a_count_phrase": {
        "tests/verification/rung1/test_a.py": XPASS_PLAIN,
        "tests/verification/rung1/conftest.py": XPASS_HEADER_CONFTEST,
    },
    "ci_rung_full_prints_a_counter_line_AFTER_pytests_summary": {
        "tests/verification/rung1/test_a.py": ATEXIT_NOISE,
    },
    "ci_rung_argument_path_carries_a_trailing_slash": {
        "tests/verification/rung1/test_a.py": PASSING,
    },
    "ci_rung_full_every_test_is_xfail_and_PASSES": {
        "tests/verification/rung1/test_a.py": XPASSED,
    },
    "ci_rung_declared_empty_with_its_marker_and_nothing_in_it": {
        "tests/verification/rung2/.empty-by-design": "marker",
    },
    "ci_rung6_job_as_shipped_leaves_its_own_rung_undeclared": {
        "tests/verification/rung6/test_r6.py": PASSING,
        "tests/regression/test_golden.py": PASSING,
    },
    "ci_empty_then_full_rung_fails_prints_no_OK_line": {
        "tests/verification/rung2/.empty-by-design": "marker",
        "tests/verification/rung1/test_a.py": FAILING,
    },
    "ci_rung_full_conftest_makereport_wrapper_turns_a_FAILING_test_into_a_passing_report": {
        "tests/verification/rung1/test_a.py": FAILING_TEST,
        "tests/verification/rung1/conftest.py": CONFTEST_MAKEREPORT,
    },
    "ci_rung_full_conftest_makereport_wrapper_against_the_XPASS_case_CONTROL": {
        "tests/verification/rung1/test_a.py": XPASS_PLAIN,
        "tests/verification/rung1/conftest.py": CONFTEST_MAKEREPORT,
    },
    "ci_rung_full_conftest_pytest_ignore_collect_hides_the_FAILING_test_file": {
        "tests/verification/rung1/test_ok.py": PASSING_TEST,
        "tests/verification/rung1/test_bad.py": FAILING_TEST_BAD,
        "tests/verification/rung1/conftest.py": CONFTEST_IGNORE_COLLECT,
    },
    "ci_rung_full_conftest_collection_modifyitems_drops_only_the_FAILING_item": {
        "tests/verification/rung1/test_a.py": OK_AND_BAD,
        "tests/verification/rung1/conftest.py": CONFTEST_MODIFYITEMS_DROP_BAD,
    },
    "ci_rung_full_conftest_pytest_sessionfinish_rewrites_the_junit_xml": {
        "tests/verification/rung1/test_a.py": FAILING_TEST,
        "tests/verification/rung1/conftest.py": CONFTEST_SESSIONFINISH,
    },
    "ci_rung_full_conftest_deselects_EVERY_item_CONTROL": {
        "tests/verification/rung1/test_a.py": FAILING_TEST,
        "tests/verification/rung1/conftest.py": CONFTEST_MODIFYITEMS_DROP_ALL,
    },
    "ci_rung_full_xfail_marked_test_that_genuinely_FAILS_CONTROL": {
        "tests/verification/rung1/test_a.py": XFAIL_THAT_FAILS,
    },
}

# The two entries whose job arguments are not the default pair for their rung.
SPECIAL_ARGS: dict[str, list[str]] = {
    "ci_rung_argument_path_carries_a_trailing_slash": ["full:tests/verification/rung1/"],
    "ci_rung_declared_empty_with_its_marker_and_nothing_in_it": ["empty:tests/verification/rung2"],
    # The arguments `ci.yml` carried at `fa3b070`, when rung 6's own directory
    # had been dropped from the job. Restoring `empty:` there is what makes this
    # entry fail: a test in rung 6 is now a stale declaration rather than a
    # directory nothing runs.
    "ci_rung6_job_as_shipped_leaves_its_own_rung_undeclared": [
        "empty:tests/verification/rung6",
        "full:tests/regression",
    ],
    "ci_run_rung_with_no_arguments_at_all": [],
    "ci_argument_without_a_kind_prefix": ["tests/verification/rung1"],
    "ci_misspelled_kind_capital_Empty": ["Empty:tests/verification/rung2"],
    "ci_empty_then_full_rung_fails_prints_no_OK_line": [
        "empty:tests/verification/rung2",
        "full:tests/verification/rung1",
    ],
    "ci_rung_declared_empty_but_directory_absent": ["empty:tests/verification/rung5"],
    "ci_rung_path_contains_a_space": ["full:tests/ver ification/rung1"],
    "ci_rung2_stale_marker_rung_gains_a_failing_test": ["empty:tests/verification/rung2"],
    "ci_rung6_second_dir_declared_full_collects_nothing": [
        "full:tests/verification/rung6",
        "full:tests/regression",
    ],
}

ARGS: dict[str, list[str]] = {
    "rung1": ["full:tests/verification/rung1"],
    "rung6": ["empty:tests/verification/rung6", "full:tests/regression"],
}


def _link_directory(target: Path, link: Path) -> None:
    """A directory link, by whichever mechanism this machine allows.

    NOT A SKIP AND NOT A PLATFORM GUARD (`CLAUDE.md` forbids the first). Windows
    refuses `os.symlink` without a privilege most developer accounts do not
    have -- `WinError 1314` -- while a directory JUNCTION needs none and is what
    `[ -d ]` and pytest both follow. CI runs this on Linux and takes the first
    branch; a machine that can do neither raises, and the entry goes red rather
    than quietly not being exercised.
    """
    try:
        link.symlink_to(target, target_is_directory=True)
    except OSError:
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)],
            capture_output=True,
            check=True,
        )


def _job_for(entry: str) -> list[str]:
    if entry in SPECIAL_ARGS:
        return SPECIAL_ARGS[entry]
    return ARGS["rung6"] if entry.startswith("ci_rung6") else ARGS["rung1"]


def _run(tmp: Path, entry: str) -> tuple[int, str]:
    # THE PROJECT'S PYTEST CONFIGURATION TRAVELS WITH THE LAYOUT (CG4). Without
    # it these trees had no `addopts`, so `-ra` was never in effect and the
    # flags added to counter it were untestable here: deleting them left all
    # four forged-summary layouts passing unchanged. A harness that cannot see
    # the setting under test measures nothing about it.
    tmp.mkdir(parents=True, exist_ok=True)
    (tmp / "pyproject.toml").write_text(
        (ROOT / "pyproject.toml").read_text(encoding="utf-8"), encoding="utf-8"
    )
    for rel, body in LAYOUTS[entry].items():
        if rel.startswith("@symlink:"):
            link = tmp / rel.split(":", 1)[1]
            link.parent.mkdir(parents=True, exist_ok=True)
            _link_directory(tmp / str(body), link)
            continue
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body or "", encoding="utf-8")
    out = subprocess.run(
        ["sh", str(SCRIPT), *_job_for(entry)],
        cwd=tmp,
        capture_output=True,
        text=True,
    )
    return out.returncode, out.stdout + out.stderr


def test_the_corpus_and_the_layouts_agree() -> None:
    """Meta-test: a layout this file forgot to build is a case nothing runs."""
    assert ENTRIES, f"{CORPUS} parsed to no entries; the format changed"
    named = {e[0] for e in ENTRIES}
    built = set(LAYOUTS)
    assert named == built, (
        f"in the corpus and not built here: {sorted(named - built)}; "
        f"built here and not in the corpus: {sorted(built - named)}. Every "
        "entry the reviewer wrote is run, or the count this file publishes is "
        "about a different set than the one they measured."
    )
    assert shutil.which("sh"), (
        "no POSIX shell on PATH, so the CI step body cannot be executed here "
        "and this whole file would pass without running anything"
    )


@pytest.mark.parametrize("entry, layout, require", ENTRIES, ids=[e[0] for e in ENTRIES])
def test_the_rung_job_gates_the_layout(
    entry: str, layout: str, require: str, tmp_path: Path
) -> None:
    """The shipped step body, on the layout, with the outcome the entry needs."""
    code, log = _run(tmp_path, entry)

    if entry in REQUIREMENT_CHANGED:
        # NOT SKIPPED AND NOT xfailed (`CLAUDE.md` forbids both). The entry runs
        # and its outcome is asserted -- in the DIRECTION declared above, which
        # is not always the reverse of the corpus: two of these six are cases
        # the rule made stricter, and four are cases no gate here can reach.
        declared, why = REQUIREMENT_CHANGED[entry]
        if declared == "fail":
            assert code != 0, f"{entry}: declared to FAIL and it returned 0.\n  {why}\n{log}"
        else:
            assert code == 0, (
                f"{entry}: declared to PASS -- the gate cannot reach this "
                f"channel -- and it FAILED, so something closed it and this "
                f"declaration is stale.\n  {why}\n{log}"
            )
        return

    if require == "fail":
        assert code != 0, f"{entry}: the job passed on a layout that must redden.\n{log}"
    else:
        assert code == 0, f"{entry}: the job failed on a layout that must pass.\n{log}"
        if require == "run":
            assert re.search(r"run_rung: [1-9]\d* collected", log), (
                f"{entry}: the job returned 0 without running any test. That is "
                f"the rung-6 defect exactly: green, and nothing executed. The "
                f"count comes from the script's own line, because pytest's "
                f"summary is no longer echoed -- reading it was R294.\n{log}"
            )
        else:
            assert "run_rung: OK" in log, (
                f"{entry}: the job passed without printing its success line, "
                f"so a silent pass is indistinguishable from a crash.\n{log}"
            )


def test_a_RED_rung_prints_its_count_and_its_reason(tmp_path: Path) -> None:
    """Exit 1 is not a report, and for two commits that is all there was.

    `set -e` was in force around the pytest invocation, so a failing run killed
    the script before `code=$?`: the junit reader never ran, and a red rung
    exited 1 having printed nothing at all -- no count, no reason, no name. It
    still went red, which is why nothing noticed. CI showed `Process completed
    with exit code 1` under a rung whose failure was one assertion in one file.

    Every scenario measured through that path -- the five in the step report,
    the layouts here -- was reading the shell's exit rather than the reader's,
    so this asserts the OUTPUT, not the code.
    """
    rung = tmp_path / "tests" / "verification" / "rung1"
    rung.mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text(
        (ROOT / "pyproject.toml").read_text(encoding="utf-8"), encoding="utf-8"
    )
    (rung / "test_a.py").write_text(
        "def test_ok():\n    assert True\n\n\ndef test_bad():\n    assert False\n",
        encoding="utf-8",
    )
    out = subprocess.run(
        ["sh", str(SCRIPT), "full:tests/verification/rung1"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    log = out.stdout + out.stderr
    assert out.returncode != 0, f"a rung with a failing test passed.\n{log}"
    assert "2 collected, 1 failed" in log, (
        "the rung went red without saying what it ran. The junit reader's "
        f"count line is the only thing that says the gate looked.\n{log}"
    )
    assert "is red" in log, f"no reason printed beside the exit code.\n{log}"


def test_the_changed_requirements_are_exactly_these(tmp_path: Path) -> None:
    """The rule's disagreement with the corpus, asserted rather than assumed.

    If an entry outside this list starts disagreeing, the rule moved and nobody
    said so. If one inside it stops disagreeing, the list is stale. Same idiom
    as the golden file: the disagreement is recorded, and a move fails the build.
    """
    disagreeing = set()
    for entry, _layout, require in ENTRIES:
        code, _log = _run(tmp_path / entry, entry)
        actual_fail = code != 0
        if actual_fail != (require == "fail"):
            disagreeing.add(entry)
    assert disagreeing == set(REQUIREMENT_CHANGED), (
        f"newly disagreeing: {sorted(disagreeing - set(REQUIREMENT_CHANGED))}; "
        f"no longer disagreeing: {sorted(set(REQUIREMENT_CHANGED) - disagreeing)}."
        " The rung gate's behaviour moved against the reviewer's corpus. Say "
        "which rule changed and why in the step report."
    )
