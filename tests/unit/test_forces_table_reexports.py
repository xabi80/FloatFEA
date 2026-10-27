"""The re-exports two by-path consumers depend on, asserted rather than commented (FL1).

**THIS TEST EXISTS BECAUSE A LINT AUTOFIX ALREADY BROKE IT ONCE, IN THE SAME SESSION
THAT WROTE THE COMMENT WARNING ABOUT IT.** FL1 moved the member-force core out of
`scripts/measure/member_forces_table.py` into `floatfea/post/forces_table.py`. Two
scripts -- `f6a_premise_check.py` and `f6_results_report.py` -- load that script BY PATH
through `importlib` and reach for these names as attributes of the loaded module, so
after the move they resolve only because the script imports them back into its own
namespace.

`ruff` reads them as unused, because within that file they are. The import block carries
`# noqa: F401` for exactly that reason, and the first attempt to say so in a comment was
undone two commands later: an import-sort autofix merged two blocks and dropped four of
the names, leaving `_joint_wiring`, `_lam_full_scale`, `_net_field` and `_station_values`
unresolvable. Nothing was red. The consumers fail with an `AttributeError` at the far end
of an `importlib` load, with nothing in either file to point at.

A comment cannot survive a tool that rewrites the lines it describes. This can.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "measure" / "member_forces_table.py"

# The eight attributes the two consumers actually reach for.
#
# This list is a claim about the repository, and under CW0 such a claim is a test, a
# triple, or deleted. It is A TEST: the second test function below greps both consumers
# for their `MFT` attribute lookups and fails if they ask for anything this tuple does
# not list.
#
# It was briefly written here as a `claim:`/`cmd:` comment instead, and
# `tests/test_tree_prose_consistent.py` rejected it on sight for two good reasons: the
# `cmd:` wrapped onto a second line, which that parser forbids because a wrapping command
# swallows whatever follows it, and the command was a shell pipeline the triple runner
# cannot execute -- so nothing would ever have checked it. A triple whose command cannot
# run is exactly what CW0 calls not a triple.
CONSUMED = (
    # `FROUDE_LAMBDA` WAS HERE AND IS NOT A RE-EXPORT ANY MORE (R906). FN0 threaded the
    # Froude scale out of `floatfea.post.forces_table`, so `f6a_premise_check.py` had to
    # state a scale when calling `_lam_full_scale` and reached for the nearest declared
    # one, `MFT.FROUDE_LAMBDA` -- and this list is what noticed, on the first whole-suite
    # run after that change.
    #
    # R902 then deleted that constant, because a module literal standing in for a
    # recorded input is R805/FN0's own defect. So the consumer now reads the scale from
    # the npz through `exported_froude_lambda`, and this entry asserted the existence of
    # a symbol a guard added in the SAME COMMIT asserts is absent -- two guards claiming
    # opposite things, with CI's `unit tests` red and `guards and meta-tests` skipped
    # behind it. The entry is removed rather than the newer guard relaxed: the scale
    # belongs to the file, not to a sibling script's namespace.
    #
    # R947 ADDED A NINTH NAME, AND THIS LIST IS WHY THAT IS SAFE.
    # `f6_results_report.py` had re-implemented the published-factor format inline; the
    # repair was to call the one definition, which made the consumer reach for one more
    # attribute. That is exactly the drift this list exists to catch -- it caught R906
    # the same way, on the first whole-suite run after the change -- so the name is
    # DECLARED rather than the call avoided.
    "_factor_text",
    "_joint_wiring",
    "_lam_full_scale",
    "_net_field",
    "_static_rows",
    "_station_values",
    "_stresses",
    "map_joint_reactions",
    "solve_inertia_relief",
)


def _load_by_path() -> object:
    """Load the script the way its two consumers do, not by package import.

    The route is the subject: a package import would not reproduce the `sys.path`
    arrangement those scripts rely on, and it is the by-path attribute lookup that
    broke.
    """
    for entry in (str(ROOT), str(ROOT / "scripts")):
        if entry not in sys.path:
            sys.path.insert(0, entry)
    spec = importlib.util.spec_from_file_location("member_forces_table", SCRIPT)
    assert spec is not None and spec.loader is not None, SCRIPT
    module = importlib.util.module_from_spec(spec)
    sys.modules["member_forces_table"] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("name", CONSUMED)
def test_the_by_path_consumers_can_still_reach_every_name(name: str) -> None:
    """Each name resolves on the module as loaded by path.

    Parametrised one name per case ON PURPOSE (EG3(i)'s discipline applied to a test
    rather than to a verdict): a single assertion over the tuple reports the first
    missing name and hides the rest, and the autofix that caused this dropped FOUR.
    """
    module = _load_by_path()
    assert hasattr(module, name), (
        f"`member_forces_table.{name}` does not resolve. Two scripts load that file by "
        f"path and read this attribute; before FL1's move it was defined there, and it "
        f"now resolves only via the `# noqa: F401` re-export block. If a lint autofix "
        f"removed it as unused, restore it to that block rather than deleting this case."
    )


def test_the_names_this_test_guards_are_the_ones_the_consumers_ASK_FOR() -> None:
    """The guarded list is read off the consumers, so it cannot drift from them.

    Without this, `CONSUMED` is a list someone typed once. A consumer that starts
    reaching for a ninth attribute would be unprotected, and the failure mode is the
    same `AttributeError` this file exists to prevent.
    """
    import re

    asked: set[str] = set()
    for rel in ("f6a_premise_check.py", "f6_results_report.py"):
        text = (ROOT / "scripts" / "measure" / rel).read_text(encoding="utf-8")
        asked.update(re.findall(r"MFT\.([A-Za-z_][A-Za-z0-9_]*)", text))

    assert asked, (
        "no `MFT.<name>` lookups found in either consumer. Either they stopped loading "
        "the script by path -- in which case this whole file can go -- or the pattern "
        "this test greps for no longer matches how they do it."
    )
    unguarded = sorted(asked - set(CONSUMED))
    assert not unguarded, (
        f"the consumers reach for {unguarded}, which `CONSUMED` does not list, so those "
        f"attributes are unprotected. Add them to `CONSUMED`."
    )


def test_R1025_the_GENERATORS_CATEGORY_MOVES_WITH_THE_LIBRARYS_LIMIT(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """R1010's rewrite, held by a test rather than by a grid.

    R1010 replaced `if s > 1.0 / 7.0` and `period_full_s < lo` in this generator with
    reads of `_case.verdict`. Both copies were the same float as the library's, so nothing
    moved -- which is why a 160000-point equivalence grid could show the rewrite changed no
    published number and could NOT show the rewrite was load-bearing. What a second copy
    costs is the NEXT edit to either constant: the library's verdict moves and the
    published column does not.

    So the library's limit is moved, and the generator's category has to move with it. A
    copy of the literal would leave `category` where it was. ONE VARIABLE: the limit; the
    wavelength and the steepness are asserted unchanged, so the physics is held fixed and
    only the DECISION moves (BG0).
    """
    from floatfea.loads import period_band as PB

    module = _load_by_path()
    h_full, period = 24.2, 14.0
    # The INJECTED limit. It is declared here rather than written twice, because the
    # assertion below and the patch have to be the same number or the cell proves nothing
    # (C131's shape: one value written twice with a comment hoping they stay equal).
    _PATCHED_LIMIT = 0.05

    lam, s, _where, category = module.steepness(period, h_full)  # type: ignore[attr-defined]
    assert category == "in", (category, s)
    # NON-VACUOUS in both directions: the real limit does not call this case breaking, and
    # the patched one must. Without the second assertion the patch could be a no-op.
    assert s < PB.BREAKING_STEEPNESS_LIMIT, (s, PB.BREAKING_STEEPNESS_LIMIT)
    # not-a-tolerance: `_PATCHED_LIMIT` is the INJECTED limit this cell sets two lines
    # below -- an input to the experiment, chosen so that it sits between the real limit
    # and this case's steepness, which is what makes the category move. Nothing is
    # compared for agreement against it and loosening it cannot turn a red green: a value
    # above `s` makes the cell fail at `category2 == "breaking"`, and a value above the
    # real limit makes it fail here.
    assert (
        # not-a-tolerance: `_PATCHED_LIMIT` is the INJECTED limit this cell sets two lines
        # below, chosen to sit between the real limit and this case's steepness so the
        # category has to move. It is an input to the experiment: a value above `s` makes
        # the cell fail at `category2 == "breaking"`, and one above the real limit makes
        # it fail here, so loosening it cannot turn a red green.
        #
        # MARKED rather than left to the guard's blind spot: a FUNCTION-LOCAL name holding
        # a literal is not resolved by `tests/test_no_tolerance_literals.py` (a
        # MODULE-LEVEL one is -- measured, see the commit message), so this comparison was
        # silently exempt. Relying on that would be working around the guard.
        s
        > _PATCHED_LIMIT
    ), s

    monkeypatch.setattr(PB, "BREAKING_STEEPNESS_LIMIT", _PATCHED_LIMIT)
    lam2, s2, where2, category2 = module.steepness(period, h_full)  # type: ignore[attr-defined]
    assert (lam2, s2) == (lam, s), ((lam2, s2), (lam, s))
    assert category2 == "breaking", (category2, s2)
    assert "BREAKING" in where2, where2
