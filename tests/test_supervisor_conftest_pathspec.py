"""The reviewer's conftest pathspec matches the conftests that exist (CI0, R310).

R302's answer was that no gate can outrank code that writes the record it
reads, so **review is the bound** -- and the bound was written into both
instruction files as a pathspec:

    git diff <prev>..<this> -- 'tests/**/conftest.py'

which matches **nothing**. Git's default pathspec glob will not let a double
star stand for zero directories, so the pattern means "depth two or more", and
the only conftest in this repository is `tests/conftest.py` at depth one --
where it applies to every rung at once and already implements
`pytest_collection_modifyitems`, one of the channels the item exists for.

An instruction that returns the empty set is an empty parameter set in prose.
This file is the negative control the instruction did not have: it runs the
pathspec the reviewer is told to run and requires it to name every conftest
that is tracked.

WHAT IT DOES NOT DO: it cannot make anyone read the diff. It makes the command
in the instruction return the files it claims to be about, so that the reading
has something in front of it.
"""

from __future__ import annotations

import re
import shlex
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS = (
    ROOT / "docs" / "SUPERVISOR.md",
    ROOT / ".claude" / "agents" / "gating-supervisor.md",
)

# The item-4c line in either file: everything after `--` up to the end of the
# backticked command.
_PATHSPEC = re.compile(r"`git diff [^`]*?--\s+([^`]*conftest\.py[^`]*)`")


def _tracked_conftests() -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "*conftest.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return {line.strip() for line in out.stdout.splitlines() if line.strip()}


def _matched_by(pathspec: list[str]) -> set[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", *pathspec],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return {line.strip() for line in out.stdout.splitlines() if line.strip()}


def test_there_are_conftests_to_find() -> None:
    """A repository with no conftest makes every assertion below vacuous."""
    found = _tracked_conftests()
    assert found, (
        "no tracked `conftest.py` anywhere. If that is true the channel R302 "
        "is about does not exist here, and this file is measuring nothing -- "
        "which is worth knowing either way."
    )


@pytest.mark.parametrize("path", INSTRUCTIONS, ids=lambda p: p.name)
def test_the_instruction_pathspec_names_every_conftest(path: Path) -> None:
    """The command the reviewer is told to run, run."""
    text = path.read_text(encoding="utf-8", errors="replace")
    specs = _PATHSPEC.findall(text)
    assert specs, (
        f"{path.name} carries no `git diff ... conftest.py` command in its "
        "item 4c. The bound R302 names is that command; without it the item "
        "has no answer at all."
    )
    for raw in specs:
        pathspec = shlex.split(raw)
        matched = _matched_by(pathspec)
        missing = _tracked_conftests() - matched
        assert not missing, (
            f"{path.name}'s pathspec {pathspec} does not match {sorted(missing)}.\n"
            "Git will not let `**` stand for zero directories, so "
            "`tests/**/conftest.py` means depth two or more and misses "
            "`tests/conftest.py` -- the one that exists, and the one that "
            "applies to every rung. List both paths."
        )


def test_the_pattern_that_failed_is_still_the_one_that_fails() -> None:
    """The measurement behind this file, kept as a run rather than a memory.

    If a future git makes `**` match zero directories, this goes red and the
    instruction can be simplified. Until then the reason for listing two paths
    is a property of the tool, not a preference, and it is asserted rather
    than remembered.
    """
    if not any(p.count("/") == 1 for p in _tracked_conftests()):
        pytest.fail(
            "no depth-one conftest is tracked any more, so the case this file "
            "was written for cannot be measured. Re-read the instruction: the "
            "two-path form may no longer be needed."
        )
    assert not _matched_by(["tests/**/conftest.py"]) & {"tests/conftest.py"}, (
        "`tests/**/conftest.py` now matches `tests/conftest.py`. Git's "
        "behaviour changed; the instruction may drop the second path."
    )
