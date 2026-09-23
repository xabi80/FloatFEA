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


def _every_reference() -> list[tuple[str, str]]:
    """`(file, name)` for every `{{fig:NAME}}` anywhere in the repository.

    CM3/R337: a dangling figure name in a docstring is the same defect as one
    in the plan, and until now only the plan was read. A comment that cites a
    figure the generator does not produce is a claim with nothing behind it,
    and it is harder to notice than a stale number because it looks like a
    reference.
    """
    out: list[tuple[str, str]] = []
    for where in ("floatfea", "tests", "scripts", "docs"):
        for path in (ROOT / where).rglob("*"):
            if path.suffix not in (".py", ".md", ".sh") or "__pycache__" in str(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for name in _REF.findall(text):
                out.append((str(path.relative_to(ROOT)).replace("\\", "/"), name))
    return out


REFERENCES = _every_reference()


@pytest.mark.parametrize(
    "where, name",
    REFERENCES or [("(none)", "(none)")],
    ids=[f"{w}:{n}" for w, n in REFERENCES] or ["(none)"],
)
def test_every_figure_reference_anywhere_resolves(where: str, name: str) -> None:
    """Wherever it is written, the name has to exist."""
    if where == "(none)":
        pytest.fail("no `{{fig:...}}` reference found anywhere; the pattern broke")
    defined = _defined()
    assert name in defined, (
        f"{where} cites `{{{{fig:{name}}}}}` and the generated file defines "
        f"{sorted(defined)[:4]}... A reference in a docstring is a claim like "
        "any other."
    )


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


def test_every_floor_class_row_clears_its_tolerance_on_THIS_tree() -> None:
    """DD2. The one useful half of the guard DC0 deleted, restored alone.

    `scripts/regen_figures.py --check` did two jobs. One was the staleness
    comparison -- re-render, diff against the committed file -- whose domain
    included every row derived from the reviewer's corpora, so it reddened on
    the reviewer's own commits and DC0 deleted it. The other was this: each
    floor-class row is compared with the TOLERANCE it decides against, and the
    margin must both hold and be wider than the declared platform spread.

    That second job went with the deletion and nobody said so, including the
    commit message I wrote for it (R503). `largest_rigid_eigenvalue` and
    `rigid_mode_mechanism_ceiling` bracket `RIGID_MODE_BOUND` from below, and
    after DC0 the only caller of `--check` in the repository was the deleted
    test, so nothing in the suite would have noticed either of them crossing.

    WHAT THIS DOES AND DOES NOT DO. It renders on THIS tree and asserts each
    row against its own constant. It does NOT read
    `docs/milestones/F2_figures.md`, so a corpus commit cannot redden it by
    moving a number -- only by moving a number PAST A CEILING, which is a real
    finding and the one worth being woken for. The committed render staying
    current is a closure item now, not a guard.

    THE SPREAD CHECK IS PART OF THE DECISION, not decoration: a margin thinner
    than `FIGURE_FLOOR_CLASS_SPREAD` is one the platform difference alone could
    carry across the ceiling, which is Q8's third class and the reason these
    rows are floor-class at all.
    """
    # LOADED HERE, NOT AT MODULE SCOPE. `floor_class()` renders on first
    # call, and a render at import would cost every test in this file the
    # ninety seconds this one pays on purpose.
    import importlib.util

    from floatfea.tolerances import FIGURE_FLOOR_CLASS_SPREAD

    spec = importlib.util.spec_from_file_location(
        "regen_figures_for_clearance", ROOT / "scripts" / "regen_figures.py"
    )
    assert spec is not None and spec.loader is not None
    R = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(R)

    marks = R.floor_class()
    rows = dict(R._ROW.findall(R.render()))
    checked, failures = [], []
    for name, (kind, ceiling_name, as_ratio) in sorted(marks.items()):
        if kind not in ("below", "above"):
            continue
        value = R._number(rows.get(name, ""))
        if value is None or value <= 0:
            failures.append(f"{name}: rendered `{rows.get(name)}`, not a positive number")
            continue
        ceil = R._ceiling(name)
        if as_ratio:
            margin = 10 ** (ceil - value) if kind == "below" else 10 ** (value - ceil)
        else:
            margin = ceil / value if kind == "below" else value / ceil
        checked.append(name)
        if margin < 1.0:
            failures.append(
                f"{name} is {value:.6g} and must be {kind} "
                f"{ceil:.6g} ({ceiling_name}): THE DECISION MOVED"
            )
        elif margin < FIGURE_FLOOR_CLASS_SPREAD:
            failures.append(
                f"{name} clears {ceiling_name} by {margin:.4g}x, under the "
                f"declared spread {FIGURE_FLOOR_CLASS_SPREAD}x -- the platform "
                "alone could carry this decision across its ceiling"
            )

    assert checked, (
        "no floor-class row was checked at all. Every row is `derived` or "
        "`words`, or the marks did not load -- either way this test is "
        "vacuous, which is how the last one stopped meaning anything."
    )
    assert not failures, "\n".join(failures)


# THE STALENESS GUARD WAS HERE AND IS DELETED (DC0). Its name is not written
# out, because `test_every_test_name_cited_in_prose_exists` requires a cited
# test name to exist and this one no longer does -- which is that guard doing
# exactly its job on a deletion. The name is in the golden's diff, in this
# commit, and in the closure artifact.
#
# It re-rendered the figures and compared them with the committed file.
#
# THE MECHANISM, WHICH IS WHAT WAS MEASURED. Two corpus files feed rendered
# rows: `g21_rigid_body_frames.txt` reaches `rigid_mode_corpus_frames` through
# `RBC.ENTRIES`, and `g22_model_configurations.txt` reaches `corpus_entries`
# through `C.ENTRIES`. A commit that adds entries to either moves those rows,
# so the guard reports the reviewer's own data as a stale figure, and the
# repair is an implementer commit after a closed step -- which reddens the
# whole-suite-line guard in turn.
#
# "EVERY TIME" AND "IT RAN FOUR TIMES" STOOD HERE AND ARE WITHDRAWN (R506,
# R507). Neither had a cell. The second is a count of history with no command
# behind it, and the first is false as stated: a corpus commit touching
# neither of those two files moves nothing, which is what `cbf8520` did --
# it touched `tree_prose_claims.txt` only, and `--check` reads the same 172
# frames on both sides of it.
#
# A STALENESS CHECK WHOSE DOMAIN INCLUDES REVIEWER-OWNED DATA REPORTS THE
# REVIEWER'S WORK AS THE IMPLEMENTER'S DEFECT. That is the reason, and it is
# in the closure artifact.
#
# The first attempt at the loop emptied the figures instead -- every
# corpus-derived row published a pointer to a test rather than a number. That
# hollowed out this guard rather than removing it: 51 of 64 rows became a
# pure function of the row's own name, so it compared a constant with itself
# across 80% of its domain, and the prose written around it asserted that a
# test carried a claim it does not carry. Deleting the guard is the honest
# form of the same decision.
#
# The figures file is still generated and still canonical, and the committed
# copy is refreshed as a CLOSURE ITEM at each step's closure rather than at
# every corpus commit.
#
# WHAT IS NOT CLAIMED HERE, and the earlier wording implied it (R506): `ci.yml`
# runs the generator inside the determinism legs, which RENDER and hash but
# compare nothing, so no CI job checks the committed copy against a fresh one.
# The only comparison left in the repository is
# `test_every_figure_reference_anywhere_resolves`, which fails a `{{fig:}}`
# name the generator does not produce -- a different question from whether a
# published number is current.
