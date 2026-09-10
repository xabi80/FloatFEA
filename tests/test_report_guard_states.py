"""The carry guard's inputs, run as the states that actually occur (R234).

`tests/test_report_carried.py` reads a report and a verdict at MODULE scope, so
whatever it cannot read it cannot report -- it dies during collection and takes
the suite with it. That is what CB2 shipped: at every legitimate step boundary,
where the report is committed and the verdict is written afterwards, `pytest -q`
gave `1 error` and ran **zero** of 1589 tests. Item 1b made a boundary red; this
made it silent.

A guard whose failure mode is "no tests ran" is worse than one that is wrong,
because a wrong answer is still an answer. This file runs the guard against each
state the reviewer enumerated and requires the outcome to be one of three:

    green        the state is normal and every assertion passes
    named_fail   the state is a defect and a NAMED test carries the message,
                 with the rest of the file still collected and run
    ignored      the state is not a step at all and the guard steps over it

**`named_fail` is the whole point.** It is not enough that the guard notices;
it has to notice without preventing anything else from running.

THE CORPUS IS THE REVIEWER'S. `tests/corpus/report_guard_states.txt` is test
DATA and the implementer does not edit it.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple
from xml.etree import ElementTree

import pytest

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "tests" / "corpus" / "report_guard_states.txt"
GUARD = "tests/test_report_carried.py"

# How each state is built, relative to a COPY of the repository. A state is a
# mutation of `docs/reports/F2/` or `docs/reviews/F2/` and nothing else.
STATES: dict[str, list[tuple[str, str]]] = {
    "baseline": [],
    "newest_report_has_no_verdict_yet": [("copy_report", "6")],
    "newest_verdict_file_present_but_empty": [("copy_report", "6"), ("empty_verdict", "6")],
    "two_digit_step_number": [("copy_report", "10"), ("copy_verdict", "10")],
    "non_numeric_step_suffix": [("copy_report", "5b")],
    "reports_directory_renamed_away": [("rename_reports", "")],
    # --- the twenty-ninth verdict's eleven ---------------------------------
    "superscript_digit_step_number": [("report_named", "step-\N{SUPERSCRIPT ONE}.md")],
    "shallow_clone_depth_1": [("shallow", "")],
    "reviews_directory_renamed_away": [("rename_reviews", "")],
    "answers_header_names_a_sha_that_is_not_a_commit": [("bad_answers_sha", "deadbee")],
    "two_reports_ahead_of_the_newest_verdict": [
        ("copy_report", "6"),
        ("copy_report", "7"),
    ],
    "report_file_is_a_directory": [("report_dir", "6"), ("copy_verdict", "6")],
    "verdict_file_is_a_directory": [("copy_report", "6"), ("verdict_dir", "6")],
    "draft_suffix_beside_a_step_report": [("report_named", "step-6-draft.md")],
    "step_number_is_the_empty_string": [("report_named", "step-.md")],
    "two_digit_step_number_discriminating": [
        ("copy_report", "10"),
        ("copy_verdict", "10"),
        ("append_finding", "10"),
    ],
    "verdict_amended_after_the_commit_the_report_answers": [("append_finding", "5")],
    # --- the thirtieth verdict's four --------------------------------------
    "shallow_clone_depth_1_reports_one_diagnosis_not_sixteen": [("shallow", "")],
    "zero_padded_step_number": [("report_named", "step-06.md")],
    "zero_padded_step_number_beside_the_unpadded_one": [
        ("report_named", "step-06.md"),
        ("copy_report", "6"),
        ("copy_verdict", "6"),
    ],
    "answers_header_names_an_older_verdict_commit": [("older_answers_sha", "")],
}


def _entries() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        f = dict(p.split("=", 1) for p in line.split() if "=" in p and not p.startswith("src="))
        out.append((f["id"], f["require"]))
    return out


ENTRIES = _entries()

# States whose required outcome CHANGES under the repaired guard, with the
# reason. Recorded rather than forced: the reviewer's `require` was measured
# against the version that died at module scope, and a state that only failed
# because the guard could not be imported is not a state that should fail.
# Each entry maps to the outcome the REPAIRED guard produces, so the direction
# is asserted rather than merely excused. A bare string here silently indexed to
# its first character and asserted the right thing by accident.
REQUIREMENT_CHANGED: dict[str, tuple[str, str]] = {
    "shallow_clone_depth_1": (
        "named_fail",
        "require=green. A guard that cannot see the diff and says nothing is "
        "the defect R243 names, so the repaired guard reports a NAMED failure "
        "instead of passing. `fetch-depth: 0` removes the state from CI; it "
        "does not make the state harmless where it occurs",
    ),
    "two_digit_step_number": (
        "green",
        "require=named_fail, measured against CB2's guard. A step-10 report and "
        "a step-10 verdict are a COHERENT pair -- `int(stem.split('-')[1])` "
        "reads `10` correctly and the carry comparison resolves -- so the "
        "repaired guard is green. The failure the reviewer measured was the "
        "module-scope read, not the two-digit number",
    ),
}


# CE2: AN ABLATION ASSERTS THE DIAGNOSIS, NOT THE FAILURE.
#
# `assert code != 0` was satisfied both by the repair and by its absence: with
# the return-code branch removed, the shallow clone still exits non-zero -- with
# SIXTEEN site failures instead of one named diagnosis. The test could not tell
# the two apart, which was the whole content of R243.
#
# `{state: (must fail, must NOT fail)}`. The second half is what makes the
# assertion an ablation: removing the branch turns the deferring tests red, and
# that is a different set.
DIAGNOSIS: dict[str, tuple[str, str]] = {
    "shallow_clone_depth_1_reports_one_diagnosis_not_sixteen": (
        "test_the_diff_the_site_check_needs_is_available",
        "test_every_named_site_is_touched_or_declared",
    ),
    "shallow_clone_depth_1": (
        "test_the_diff_the_site_check_needs_is_available",
        "test_every_named_site_is_touched_or_declared",
    ),
    "newest_report_has_no_verdict_yet": (
        "test_the_guard_reads_the_step_being_worked_on",
        "test_the_report_names_the_verdict_it_answers",
    ),
    "answers_header_names_a_sha_that_is_not_a_commit": (
        "test_the_report_names_the_verdict_it_answers",
        "test_the_diff_the_site_check_needs_is_available",
    ),
}


def _force_remove(func, path, exc):  # noqa: ANN001 - shutil's handler signature
    """Clear the read-only bit and retry. Git packs arrive read-only."""
    import os
    import stat

    os.chmod(path, stat.S_IWRITE)
    func(path)


def _build(tmp: Path, state: str) -> Path:
    """A repository copy with the state applied. Only `docs/` is mutated."""
    work = tmp / "repo"
    work.mkdir(parents=True, exist_ok=True)
    # `.git` IS PART OF THE INPUT. `_changed_lines()` runs `git diff` against the
    # reviewed commit, so a copy without it gives an empty touched-set and every
    # site check fails for a reason that is the harness, not the guard.
    for rel in (".git", "tests", "docs", "floatfea", "scripts", "pyproject.toml"):
        src = ROOT / rel
        dst = work / rel
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
    reports, reviews = work / "docs/reports/F2", work / "docs/reviews/F2"
    for action, arg in STATES[state]:
        if action == "copy_report":
            shutil.copy2(reports / "step-5.md", reports / f"step-{arg}.md")
        elif action == "copy_verdict":
            shutil.copy2(reviews / "step-5.md", reviews / f"step-{arg}.md")
        elif action == "empty_verdict":
            (reviews / f"step-{arg}.md").write_text("", encoding="utf-8")
        elif action == "rename_reports":
            reports.rename(reports.parent / "F2_moved")
        elif action == "rename_reviews":
            reviews.rename(reviews.parent / "F2_moved")
        elif action == "report_named":
            shutil.copy2(reports / "step-5.md", reports / arg)
        elif action == "report_dir":
            (reports / f"step-{arg}.md").mkdir()
        elif action == "verdict_dir":
            (reviews / f"step-{arg}.md").mkdir()
        elif action == "bad_answers_sha":
            text = (reports / "step-5.md").read_text(encoding="utf-8", errors="replace")
            head = text.rindex("Answers: verdict")
            end = text.index("\n", head)
            (reports / "step-5.md").write_text(
                text[:head] + f"Answers: verdict 28 @ {arg}" + text[end:],
                encoding="utf-8",
            )
        elif action == "append_finding":
            # A finding the report cannot possibly carry, appended to the
            # WORKING COPY of the verdict. The guard reads the verdict from git
            # at the answered sha, so this must change nothing -- and if it
            # does, the guard is reading the working copy instead.
            v = reviews / f"step-{arg}.md"
            v.write_text(
                v.read_text(encoding="utf-8", errors="replace")
                + "\n**R999. (BLOCKING) planted by the harness.**\n",
                encoding="utf-8",
            )
        elif action == "older_answers_sha":
            # A real commit, but not the newest verdict's. Item 1b is the
            # reviewer's to check by eye; this asks whether the guard says
            # anything at all when the header points backwards.
            older = subprocess.run(
                ["git", "-C", str(work), "rev-list", "-n", "1", "HEAD~4"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            text = (reports / "step-5.md").read_text(encoding="utf-8", errors="replace")
            head = text.rindex("Answers: verdict")
            end = text.index(chr(10), head)
            (reports / "step-5.md").write_text(
                text[:head] + f"Answers: verdict 28 @ {older}" + text[end:],
                encoding="utf-8",
            )
        elif action == "shallow":
            # A REAL SHALLOW CLONE, not `fetch --depth 1` on a full one. The
            # first version ran the fetch against `origin` and changed nothing,
            # so the state passed without ever being built -- the harness
            # equivalent of the defect it is here to catch. `--no-local` forces
            # the transport that honours the depth for a file URL.
            shallow = tmp / "shallow"
            subprocess.run(
                ["git", "clone", "--depth", "1", "--no-local", ROOT.as_uri(), str(shallow)],
                capture_output=True,
                check=True,
            )
            # `rmtree` on a copied `.git` hits read-only pack files on
            # Windows, so the handler clears the bit rather than the harness
            # reporting a permission error as a guard failure.
            #
            # `onerror=`, NOT `onexc=` (CE0). `onexc` arrived in 3.12; the
            # project pins 3.11 and the runner has it, so the one state that
            # measures the shallow-clone repair was the one state that could not
            # run where the shallow clone was found. The handler ignores its
            # third argument, so it fits either signature.
            shutil.rmtree(work / ".git", onerror=_force_remove)
            shutil.move(str(shallow / ".git"), str(work / ".git"))
    return work


class Outcome(NamedTuple):
    """What the nested run did, read from pytest itself rather than its prose."""

    code: int
    collected: int
    failed: int
    errors: int
    names: tuple[str, ...]
    log: str

    @property
    def collection_failed(self) -> bool:
        """Nothing ran. `pytest` exit 2 is a usage or collection error, and a
        junit report with no test cases says the same thing from the other
        side."""
        return self.code == 2 or self.collected == 0

    @property
    def everything_failed(self) -> bool:
        return self.collected > 0 and self.failed + self.errors == self.collected


def _run_guard(work: Path) -> Outcome:
    """Run the guard in `work` and read the result from the junit report.

    NOT FROM THE TEXT (CC4). The first version searched stdout for the word
    "error", so on CI it announced that a nested run had not collected while
    that run's own summary read `5 failed in 0.05s`. Its mirror was worse:
    `or "passed" in log` disabled the check outright as soon as anything passed.
    A substring cannot separate "nothing ran" from "everything failed", and
    those are the two states this file exists to tell apart.
    """
    report = work / "junit.xml"
    out = subprocess.run(
        [sys.executable, "-m", "pytest", GUARD, "-q", f"--junit-xml={report}"],
        cwd=work,
        capture_output=True,
        text=True,
    )
    collected = failed = errors = 0
    names: list[str] = []
    if report.is_file():
        root = ElementTree.parse(report).getroot()
        for case in root.iter("testcase"):
            collected += 1
            bad = False
            for child in case:
                if child.tag == "failure":
                    failed += 1
                    bad = True
                elif child.tag == "error":
                    errors += 1
                    bad = True
            if bad:
                names.append(case.get("name", ""))
    return Outcome(out.returncode, collected, failed, errors, tuple(names), out.stdout + out.stderr)


def _assert_diagnosis(state: str, got: Outcome, log: str) -> None:
    """The ablation: the named diagnosis fails and its dependants do not."""
    must, must_not = DIAGNOSIS[state]
    assert any(must in n for n in got.names), (
        f"{state}: the guard failed, but `{must}` -- the test that carries the "
        f"diagnosis -- is not among {list(got.names)[:6]}. A failure that does "
        "not name its cause is not an ablation.\n" + log[-1200:]
    )
    assert not any(must_not in n for n in got.names), (
        f"{state}: `{must_not}` failed too. That is the SHAPE the repair "
        "removes -- one diagnosis rather than a cascade -- so its presence "
        "means the branch under test is not doing the work.\n" + log[-1200:]
    )


def test_the_corpus_and_the_states_agree() -> None:
    """Meta-test: a state this file forgot to build is a state nothing runs."""
    assert ENTRIES, f"{CORPUS} parsed to no entries; the format changed"
    named = {e[0] for e in ENTRIES}
    assert named == set(STATES), (
        f"in the corpus and not built: {sorted(named - set(STATES))}; "
        f"built and not in the corpus: {sorted(set(STATES) - named)}"
    )


@pytest.mark.parametrize("state, require", ENTRIES, ids=[e[0] for e in ENTRIES])
def test_the_guard_survives_the_state(state: str, require: str, tmp_path: Path) -> None:
    work = _build(tmp_path, state)
    got = _run_guard(work)
    code, log = got.code, got.log

    # TWO SEPARATE ASSERTIONS, because they are two different failures (CC4).
    assert not got.collection_failed, (
        f"{state}: the guard did not COLLECT -- exit {got.code}, "
        f"{got.collected} test cases in the junit report. Nothing in the file "
        f"ran and nothing was reported, which is R234.\n{log[-1500:]}"
    )
    assert not got.everything_failed, (
        f"{state}: every one of {got.collected} tests failed. A guard that "
        "fails wholesale is reporting the state of its own inputs, not of the "
        f"repository.\n{log[-1500:]}"
    )

    if state in REQUIREMENT_CHANGED:
        # NOT skipped and NOT xfailed. The state runs and its outcome is
        # asserted, in the direction the repair produces.
        if REQUIREMENT_CHANGED[state][0] == "green":
            assert code == 0, (
                f"{state}: the repaired guard is expected to be GREEN here and "
                f"it failed.\n{log[-1500:]}"
            )
        else:
            assert code != 0, (
                f"{state}: the repaired guard is expected to REPORT here and it "
                f"passed.\n{log[-1500:]}"
            )
        return

    if require == "green":
        assert code == 0, f"{state}: expected a clean run.\n{log[-1500:]}"
    elif require == "ignored":
        assert code == 0, (
            f"{state}: a file that is not a numbered step must be stepped over, "
            f"not reacted to.\n{log[-1500:]}"
        )
    else:
        assert code != 0, f"{state}: this state is a defect and must fail.\n{log[-1500:]}"
        named = (
            "test_the_guard_reads_the_step_being_worked_on",
            "test_the_report_names_the_verdict_it_answers",
            "test_the_diff_the_site_check_needs_is_available",
            "test_the_parse_found_something_to_check",
            "test_the_report_carries_the_finding",
            "test_every_named_site_is_touched_or_declared",
        )
        if state in DIAGNOSIS:
            _assert_diagnosis(state, got, log)

        assert any(any(n in got_name for n in named) for got_name in got.names), (
            f"{state}: the guard failed through {list(got.names)[:4]}, none of "
            "which is a named reporter. A failure nobody can locate is half a "
            f"report.\n{log[-1500:]}"
        )
