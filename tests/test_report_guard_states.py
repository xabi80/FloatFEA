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
    return work


def _run_guard(work: Path) -> tuple[int, str]:
    out = subprocess.run(
        [sys.executable, "-m", "pytest", GUARD, "-q"],
        cwd=work,
        capture_output=True,
        text=True,
    )
    return out.returncode, out.stdout + out.stderr


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
    code, log = _run_guard(work)

    # COLLECTION IS THE THING BEING ASSERTED. A guard that cannot be collected
    # reports nothing at all, which is the failure R234 is about.
    assert "error" not in log.split("=====")[-1].lower() or "passed" in log, (
        f"{state}: the guard did not COLLECT -- it errored during import, so "
        f"nothing in the file ran and nothing was reported.\n{log[-1500:]}"
    )
    assert " passed" in log or " failed" in log, (
        f"{state}: pytest produced no pass/fail count, so the file was never "
        f"executed.\n{log[-1500:]}"
    )

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
            "test_the_parse_found_something_to_check",
            "test_the_report_carries_the_finding",
            "test_every_named_site_is_touched_or_declared",
        )
        assert any(n in log for n in named), (
            f"{state}: the guard failed, but through no named test. A failure "
            f"nobody can locate is half a report.\n{log[-1500:]}"
        )
        assert "during collection" not in log, (
            f"{state}: the guard reported through a COLLECTION error, so the "
            f"rest of the file never ran. That is R234 exactly.\n{log[-1500:]}"
        )
