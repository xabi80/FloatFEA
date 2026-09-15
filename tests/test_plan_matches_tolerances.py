"""Every tolerance the locked plan names carries the value the code ships (BR0).

A tolerance moved in a step commit while `docs/milestones/F2.md` went on stating
the old value, and a review found it rather than the build --
`PATCH_TEST_COUNTER_HEADROOM` was re-derived from `2.0e7` to `6.0e7` and the plan
said `2.0e7` for a full round, in the round whose subject was figures outliving
the rule that produced them.

WHAT THIS MAKES IMPOSSIBLE. A tolerance can now move only together with a plan
edit, and a plan edit is a reopen with a lock Q&A and a re-lock commit. The
specific hole this closes is a two-line move: setting
`PATCH_TEST_EXACTNESS_COUNTER_DEFECT` to `1e-4` and `PATCH_TEST_COUNTER_HEADROOM`
to `3.0e9` made the whole suite green by exempting the entries it could not
detect. That is now a failing build rather than something a reviewer has to
notice.

WHAT IT DOES NOT DO, stated because a guard that is trusted past its reach is
worse than none: it does not check that the plan's PROSE is true, only that the
numbers agree. A plan sentence can still describe a value correctly and reason
about it wrongly -- `CLAUDE.md` § "Every claim carries its command" is what
covers that, and this is the mechanical half.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from floatfea import tolerances

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs" / "milestones" / "F2.md"

# `NAME = value` or `NAME` followed by `= value` inside a backticked span, which
# is how the plan writes them. The name must be a declared tolerance, so prose
# that merely mentions a constant without stating a value is not matched.
_STATED = re.compile(r"`?\b([A-Z][A-Z0-9_]{3,})\b`?\s*=\s*`?([-+0-9][0-9eE.+-]*)`?")


def _declared() -> dict[str, float]:
    return {
        n: getattr(tolerances, n)
        for n in dir(tolerances)
        if n.isupper() and isinstance(getattr(tolerances, n), float)
    }


def _stated_in_plan() -> list[tuple[int, str, str]]:
    """`(line number, name, literal)` for every tolerance the plan gives a value."""
    known = _declared()
    out: list[tuple[int, str, str]] = []
    for n, line in enumerate(PLAN.read_text(encoding="utf-8").splitlines(), 1):
        for name, literal in _STATED.findall(line):
            if name in known:
                out.append((n, name, literal))
    return out


def test_the_plan_states_at_least_one_tolerance_value() -> None:
    """Meta-test: an empty match set makes the check below vacuous.

    If the regex or the plan's formatting changes so that nothing matches, this
    file would pass while checking nothing -- which is the failure mode it exists
    to prevent, one level up.
    """
    stated = _stated_in_plan()
    assert stated, (
        "no tolerance value was found in the plan. Either the plan stopped "
        "stating them or the pattern stopped matching; both make the check "
        "below vacuous."
    )
    names = {name for _, name, _ in stated}
    assert len(names) >= 3, (
        f"only {sorted(names)} matched. The plan states more tolerances than "
        "that, so the pattern is missing most of them."
    )


@pytest.mark.parametrize(
    "line, name, literal",
    _stated_in_plan(),
    ids=lambda v: str(v) if not isinstance(v, str) else v,
)
def test_the_plan_and_the_code_agree(line: int, name: str, literal: str) -> None:
    shipped = getattr(tolerances, name)
    stated = float(literal)
    assert stated == shipped, (
        f"docs/milestones/F2.md:{line} states {name} = {literal}, and "
        f"floatfea/tolerances.py ships {shipped!r}. A tolerance moves with a "
        "plan edit or it does not move: the plan is the locked artifact, and a "
        "value that has drifted from it is a decision nobody reviewed."
    )


@pytest.mark.parametrize("name", sorted(_declared()))
def test_every_declared_tolerance_appears_in_the_plan(name: str) -> None:
    """The other direction (R161): a NEW tolerance cannot hide from the plan.

    The check above runs plan -> code, so a constant added to `tolerances.py` and
    never written into the plan was invisible to it -- and the plan is the locked
    artifact a tolerance is supposed to move with. Both directions together mean
    the set of declared tolerances and the set the plan fixes are the same set.
    """
    stated = {n for _, n, _ in _stated_in_plan()}
    assert name in stated, (
        f"{name} is declared in floatfea/tolerances.py and docs/milestones/F2.md "
        "does not state its value. A tolerance the plan does not name is one no "
        "reopen has to approve. Add it to the plan's tolerance table."
    )
