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
REQUIREMENT_CHANGED: dict[str, str] = {
    "ci_rung_genuinely_empty": (
        "require=pass under an inferred rule. Rung 1 is declared `full:` in the "
        "workflow, so a rung 1 holding only __init__.py now FAILS -- that is "
        "the emptied-directory case CB1 asks to redden"
    ),
    "ci_rung6_both_populated": (
        "require=run under an inferred rule. Rung 6's own directory is declared "
        "`empty:`, so a test appearing in it now FAILS as a stale declaration "
        "rather than being run silently"
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
        # and its outcome is asserted -- against the requirement this rule
        # changes it to, with the change itself declared above.
        assert code != 0, (
            f"{entry}: the declared-expectation rule is supposed to make this "
            f"FAIL and it returned 0.\n{log}"
        )
        return

    if require == "fail":
        assert code != 0, f"{entry}: the job passed on a layout that must redden.\n{log}"
    else:
        assert code == 0, f"{entry}: the job failed on a layout that must pass.\n{log}"
        if require == "run":
            assert "passed" in log, (
                f"{entry}: the job returned 0 without running any test. That is "
                f"the rung-6 defect exactly: green, and nothing executed.\n{log}"
            )
        else:
            assert "run_rung: OK" in log, (
                f"{entry}: the job passed without printing its success line, "
                f"so a silent pass is indistinguishable from a crash.\n{log}"
            )


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
