"""The plan's moving numbers are generated, and are not stale (BT0).

Hand-typed figures in `docs/milestones/F2.md` moved **eight times** across this
milestone, and three review rounds running found one describing the repository as
it was a commit earlier. The plan is a locked artifact; a number inside it that
nothing regenerates is a claim with no owner.

So the numbers that move are produced by `scripts/regen_figures.py` into
`docs/milestones/F2_figures.md` and referenced from the plan as `{{fig:NAME}}`.
This asserts both halves: every referenced name exists, and the generated file is
what a fresh run produces.

SCOPE, and it is deliberately narrow: the figures that move, not the whole plan.
A generated file that owns every number becomes a second source of truth nobody
reads. The prose around these figures is still prose, and `CLAUDE.md`'s
claim-carries-its-command rule is what covers it.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs" / "milestones" / "F2.md"
FIGURES = ROOT / "docs" / "milestones" / "F2_figures.md"

_REF = re.compile(r"\{\{fig:([a-z0-9_]+)\}\}")
_ROW = re.compile(r"^\| `([a-z0-9_]+)` \| (.+?) \|$", re.MULTILINE)


def _defined() -> dict[str, str]:
    return dict(_ROW.findall(FIGURES.read_text(encoding="utf-8")))


def _referenced() -> list[str]:
    return sorted(set(_REF.findall(PLAN.read_text(encoding="utf-8"))))


def test_the_plan_references_generated_figures_at_all() -> None:
    """Meta-test: zero references makes every check below vacuous."""
    refs = _referenced()
    assert refs, (
        "the plan references no generated figure. Either the references were "
        "removed or the pattern stopped matching, and both make this file a "
        "test of nothing."
    )
    assert len(refs) >= 5, f"only {refs} referenced; the set is larger than that"


@pytest.mark.parametrize("name", _referenced())
def test_every_referenced_figure_exists(name: str) -> None:
    defined = _defined()
    assert name in defined, (
        f"the plan references {{{{fig:{name}}}}} and "
        f"docs/milestones/F2_figures.md does not define it. Run "
        "`python scripts/regen_figures.py`."
    )


def test_the_generated_figures_are_not_stale() -> None:
    """The file is what a fresh run produces, or the plan is quoting the past."""
    out = subprocess.run(
        [sys.executable, "scripts/regen_figures.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert out.returncode == 0, (
        f"{out.stdout}{out.stderr}\ndocs/milestones/F2_figures.md is not what "
        "`scripts/regen_figures.py` produces at this commit. Regenerate it and "
        "say in the step report which figures moved and why -- that is the "
        "whole point of generating them."
    )
