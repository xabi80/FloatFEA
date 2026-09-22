"""Q8's third local class, and the two constants it declares (CH0, R303).

A canonical file is produced on one machine and read on every other, and the
question this file answers is what a machine that is NOT the canonical one
asserts about it. Q8's first two classes were written for physical channels --
exact for arithmetic only, `2` ULP through a transcendental. Neither reaches
`clean_worst_ratio`, which moved **7.3%** between the canonical render and a
laptop one at a byte-identical winning entry: the figure is an out-of-balance
of a field that is exact in exact arithmetic, divided by a ceiling, so the
numerator IS round-off and two BLAS kernels differ in their last bits by `O(1)`
factors.

The third class asserts the **decision** rather than the value, and this file
runs it against injected pairs rather than against whatever this machine
renders today -- which is the only way the counters can be run at all, since a
real render disagrees with the canonical one in exactly the ways that are
allowed.

WHAT IS ASSERTED HERE
  1. every row that is NOT floor-class must agree exactly, on any machine, so
     staleness is still caught off the canonical runner;
  2. a floor-class figure may move by up to `FIGURE_FLOOR_CLASS_SPREAD` and no
     further, and `FIGURE_FLOOR_CLASS_SPREAD_COUNTER_DEFECT` is the injected
     move that must be refused;
  3. the decision must hold, and its margin must exceed the spread bound, so a
     figure whose decision the platform alone could flip is a finding;
  4. the stamp must be present and must name the canonical environment;
  5. the tie window names the entries that swap and excludes the next one,
     `FIGURE_ARGMIN_TIE_WINDOW_COUNTER_DEFECT`.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pytest

from floatfea.tolerances import (
    FIGURE_ARGMIN_TIE_WINDOW,
    FIGURE_ARGMIN_TIE_WINDOW_COUNTER_DEFECT,
    FIGURE_FLOOR_CLASS_SPREAD,
    FIGURE_FLOOR_CLASS_SPREAD_COUNTER_DEFECT,
    RIGID_MODE_BOUND,
)

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "docs" / "milestones" / "F2_figures.md"
PLAN = ROOT / "docs" / "milestones" / "F2.md"


def _regen():
    spec = importlib.util.spec_from_file_location(
        "regen_figures", ROOT / "scripts" / "regen_figures.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


R = _regen()

# A canonical file in miniature: the stamp, one exact row, and one row of each
# floor-class kind. Written here rather than taken from the repository so the
# injected pairs below differ in ONE cell.
CANON = {
    "stamp_platform": "linux",
    "stamp_python": "3.13.7",
    "stamp_numpy": "2.4.0",
    "stamp_scipy": "1.16.0",
    "stamp_openblas_coretype": "Haswell",
    "corpus_entries": "187",
    "clean_worst_ratio": "0.2564x",
    # THE TWO SURVIVING FLOOR-CLASS ROWS (DB1). Every row this fixture used
    # to carry a decision on -- `clean_worst_ratio`, `counter_headroom_room`,
    # `detection_edge` -- is a worst over a corpus or a ratio to one, so DB1
    # withdraws it and `floor_class()` reports it as `words`, which decides
    # nothing. These two are taken on the shipped frame, decide against a
    # named constant, and are what the cases below now move. The values are
    # the canonical render's.
    "rigid_mode_residual": "7.8658e-17",
    "rigid_mode_counter_seventh": "1.2445e+02",
    "rigid_body_mode_ratio": "1.1986e-14",
    "rigid_body_counter_loss": "7.4709e-12",
    "counter_headroom_room": "2.19x",
    "detection_edge": "3.6425e-14",
    "counter_defect_over_edge": "2.745e+07x",
    "counter_defect_boundary": "2.183e-06 passes, 2.188e-06 fails",
}


def _file(rows: dict[str, str]) -> str:
    head = "# F2 figures\n\n| name | value |\n|---|---|\n"
    return head + "".join(f"| `{k}` | {v} |\n" for k, v in rows.items())


def _with(**changes: str) -> str:
    rows = dict(CANON)
    rows.update(changes)
    return _file(rows)


def _scaled(name: str, factor: float) -> str:
    """The canonical file with one floor-class figure moved by `factor`."""
    value = CANON[name]
    number = R._number(value)
    assert number is not None
    suffix = value[len(re.match(r"\s*-?[\d.eE+-]+", value).group(0)) :]
    return _with(**{name: f"{number * factor:.6g}{suffix}"})


def _with_mark(name: str, kind: str, ceiling: str | None, log: bool):
    """Add one synthetic mark to the generator's table, and take it away after.

    `floor_class()` renders on first call, so this forces the render before
    touching `_MARKS` -- otherwise the render would run inside the test and
    overwrite the injected row.
    """
    R.floor_class()
    R._MARKS[name] = (kind, ceiling, log)
    return name


def test_a_LOG_VALUED_row_is_compared_as_a_RATIO_whatever_it_is_CALLED() -> None:
    """R418's mechanism, not R418's row.

    `as_ratio` read the suffix `_orders` off the figure's NAME, and the commit
    that introduced that rule renamed a log-valued row to end in `_decided`.
    The row kept its meaning, lost the suffix, and was silently compared by
    the wrong rule -- its guard's sensitivity reduced by roughly its own
    magnitude. The flag is declared beside the value now.

    THE TWO RULES DISAGREE ON THIS PAIR AND THAT IS THE POINT: `1.0` against
    `1.3` is `10**0.3 = 2.0x` as a ratio of the underlying quantities, over
    the declared spread, and `1.3x` as a quotient of logarithms, under it.
    """
    name = _with_mark("a_log_row_named_anything", "derived", None, True)
    try:
        canon = dict(CANON)
        canon[name] = "1.000"
        moved = dict(canon)
        moved[name] = "1.300"
        code, lines = R.compare(_file(canon), _file(moved))
        assert code != 0, (
            "a log-valued row moved by 0.3 ORDERS -- a factor of 2.0 in the "
            "quantity the spread is declared on -- and the check passed it. "
            "That is R418: the rule was reached by the name and this name "
            "does not end in `_orders`.\n" + "\n".join(lines)
        )
        # And the same pair under the OTHER class is allowed, so the failure
        # above is the log flag and not the numbers.
        R._MARKS[name] = ("derived", None, False)
        code, lines = R.compare(_file(canon), _file(moved))
        assert code == 0, (
            "1.000 against 1.300 is 1.3x as a plain ratio, under the declared "
            "spread. If this fails, the test above proves nothing about the "
            "flag.\n" + "\n".join(lines)
        )
    finally:
        R._MARKS.pop(name, None)


def test_the_SHIPPED_log_rows_declare_themselves() -> None:
    """The flag is not dead code: the retired parametrisation still uses it.

    `rigid_mode_seventh_orders` is generated because revision 21 of the step
    report cites it by name, and it is `log10` of a ratio. If it ever stops
    being marked, the row above stops being the only thing that exercises the
    branch -- and this says so rather than leaving the branch untested by
    accident.
    """
    marked = {n for n, (_k, _c, log) in R.floor_class().items() if log}
    # ONE ROW, NOT TWO, SINCE DB1. `rigid_mode_seventh_orders_smallest_decided`
    # was the second and it is a corpus-derived figure -- `log10` of a ratio
    # taken at the smallest DECIDED entry, which moves whenever the corpus
    # grows -- so DB1 withdraws it and `floor_class()` reports a withdrawn row
    # as `words`. The branch is still exercised by the row that remains, which
    # is what this test exists to say; if that one ever goes too, the flag
    # becomes dead code and this assertion is what notices.
    assert marked == {"rigid_mode_seventh_orders"}, (
        f"the log-valued rows are {sorted(marked)}. Every one of them carries "
        "`log10` of a ratio and is compared as a ratio; a row that is log-"
        "valued and unmarked is compared by the wrong rule, silently."
    )


def test_the_control_agrees_with_itself() -> None:
    """A check that refuses everything is not a check."""
    code, lines = R.compare(_file(CANON), _file(CANON))
    assert code == 0, "\n".join(lines)


@pytest.mark.parametrize(
    "factor, must_fail",
    [
        (1.0, False),
        (1.078, False),
        (1.336, False),
        (FIGURE_FLOOR_CLASS_SPREAD_COUNTER_DEFECT, True),
        (3.0, True),
    ],
)
def test_a_floor_class_figure_may_move_only_so_far(factor: float, must_fail: bool) -> None:
    """`rigid_body_mode_ratio` is `1.336x` between two real machines.

    The counter is `FIGURE_FLOOR_CLASS_SPREAD_COUNTER_DEFECT`, which is above
    the bound and not on it: a counter sitting exactly at the ceiling tests the
    comparison operator.
    """
    code, lines = R.compare(_file(CANON), _scaled("rigid_body_mode_ratio", factor))
    assert (code != 0) == must_fail, f"factor {factor}:\n" + "\n".join(lines)


def test_a_row_that_is_not_floor_class_must_agree_EXACTLY() -> None:
    """The class is a licence for nine rows, not for the file.

    Every count, every `margin_*`, every `below_ceiling_*` was byte-identical
    on the two machines that produced the measurement, so staleness in any of
    them is still caught on a laptop.
    """
    code, lines = R.compare(_file(CANON), _with(corpus_entries="188"))
    assert code != 0, "\n".join(lines)
    assert any("corpus_entries" in line for line in lines)


def test_the_DECISION_moving_is_a_failure_however_small_the_move() -> None:
    """A figure that crosses its ceiling is a failure whatever the distance.

    THE VEHICLE CHANGED AT DB1 AND THE ASSERTION DID NOT. This read
    `clean_worst_ratio` at `1.02x` against the patch-test ceiling;
    `clean_worst_ratio` is a worst-over-corpus value, so DB1 withdraws it and
    `floor_class()` reports it as `words` -- which is not a class that decides
    anything, so the case stopped testing what it was written for.
    `rigid_mode_residual` is floor-class `below RIGID_MODE_EXACTNESS`, survives
    DB1 because it is taken on the shipped frame, and carries the same
    decision. The point of the case is unchanged: the decision, not the
    distance, is what the third class asserts.
    """
    code, lines = R.compare(_file(CANON), _with(rigid_mode_residual="1e-9"))
    assert code != 0, "\n".join(lines)
    assert any("DECISION MOVED" in line or "margin" in line for line in lines)


def test_a_margin_thinner_than_the_spread_is_a_finding() -> None:
    """The bracket, as an assertion.

    `1.336 < FIGURE_FLOOR_CLASS_SPREAD < 2.19` is what makes the class safe: a
    spread inside the bound cannot carry a decision across a ceiling. If a
    figure's own margin ever drops below the bound, that reasoning stops
    holding for it, and this is where that is noticed.
    """
    # THE VEHICLE CHANGED AT DB1, LIKE THE CASE ABOVE. `counter_headroom_room`
    # is a ratio to a minimum over the corpus, so it is withdrawn and reports
    # as `words`. `rigid_mode_counter_seventh` is floor-class
    # `below RIGID_MODE_BOUND`, is taken on the shipped frame, and is the
    # counter whose margin this reasoning is actually about.
    # A MARGIN, NOT A VALUE. `counter_headroom_room` WAS the margin, so the
    # old case wrote the thin number straight in. `rigid_mode_counter_seventh`
    # is a `lambda_7` in units of `||K_hat||*eps`, and its margin against
    # `RIGID_MODE_BOUND` is `bound / value` -- so the thin case is the value
    # that puts THE MARGIN just inside the spread, not the spread itself.
    thin = f"{RIGID_MODE_BOUND / (FIGURE_FLOOR_CLASS_SPREAD * 0.9):.4e}"
    code, lines = R.compare(_file(CANON), _with(rigid_mode_counter_seventh=thin))
    assert code != 0, "\n".join(lines)
    assert any("under the declared spread" in line for line in lines)


@pytest.mark.parametrize(
    "changes, why",
    [
        ({"stamp_openblas_coretype": "unset"}, "a render with no kernel pin"),
        ({"stamp_openblas_coretype": "Zen"}, "a render on a different kernel"),
        ({"stamp_python": "3.12.8"}, "a render on an interpreter the plan does not pin"),
    ],
)
def test_the_committed_stamp_must_name_the_canonical_environment(
    changes: dict[str, str], why: str
) -> None:
    """CH5. The stamp is what stops a laptop render being committed again."""
    code, lines = R.compare(_file({**CANON, **changes}), _file(CANON))
    assert code != 0, f"{why}:\n" + "\n".join(lines)


def test_a_file_with_no_stamp_at_all_is_refused() -> None:
    rows = {k: v for k, v in CANON.items() if not k.startswith("stamp_")}
    code, lines = R.compare(_file(rows), _file(rows))
    assert code != 0, "\n".join(lines)
    assert any("NO environment stamp" in line for line in lines)


def test_the_pass_fail_words_are_the_decision_for_the_boundary_row() -> None:
    """`counter_defect_boundary` is two numbers and two words.

    The numbers are floor-class and move; the words are the decision and do
    not. A row reading `fails, fails` is the counter-defect size becoming
    inadmissible, which is a finding on any machine.
    """
    code, lines = R.compare(
        _file(CANON), _with(counter_defect_boundary="2.183e-06 fails, 2.188e-06 fails")
    )
    assert code != 0, "\n".join(lines)


def test_the_numbers_beside_the_words_get_their_spread_too() -> None:
    """R311(c). The plan says the spread is printed beside the value either way.

    The `words` branch returned before any number was read, so
    `counter_defect_boundary` -- two probe sizes and two words -- was the one
    floor-class row with no spread beside it, and a row nine orders of
    magnitude out passed with no complaint.
    """
    moved = _with(counter_defect_boundary="1e-99 passes, 1e+99 fails")
    code, lines = R.compare(_file(CANON), moved)
    assert code != 0, "\n".join(lines)
    row = next(ln for ln in lines if "counter_defect_boundary" in ln)
    assert (
        "x" in row.split()[-1] or "OVER" in row
    ), f"no spread printed beside the boundary row: {row!r}"


def test_the_decision_words_are_compared_whole() -> None:
    """R313. `re.sub` over `[-+0-9.eE]` deleted the `e` out of `passes`."""
    code, lines = R.compare(
        _file(CANON), _with(counter_defect_boundary="2.183e-06 passees, 2.188e-06 fails")
    )
    assert code != 0, (
        "`passees` compared equal to `passes`, which is the character class "
        "eating the letter rather than the words being read.\n" + "\n".join(lines)
    )


def test_the_floor_class_is_what_the_GENERATOR_marks() -> None:
    """CI3/R312. Membership is a property of how a figure is computed.

    The hand-written map had nine members while the round's nine movers were a
    different nine, and nothing said so. The marks are now made at the line
    that builds each row, so a figure added without a mark is exact-compared
    by default -- the safe direction -- and one that is marked says so where
    it is produced.
    """
    marks = R.floor_class()
    assert marks, "the generator marked no figure floor-class at all"
    assert "clean_worst_ratio" in marks and "detection_edge_at" not in marks, (
        "the class is upside down: `clean_worst_ratio` is a round-off "
        "magnitude and `detection_edge_at` is a NAME, which no tolerance on a "
        "value can bound."
    )
    for name, (kind, ceiling, _log) in marks.items():
        assert kind in ("below", "above", "derived", "words"), (name, kind)
        if kind in ("below", "above") and ceiling is not None:
            assert hasattr(__import__("floatfea.tolerances", fromlist=["x"]), ceiling), (
                f"{name} is marked against `{ceiling}`, which is not a " "declared tolerance."
            )


# ------------------------------------------------------------- the tie window


def test_the_tie_window_names_the_entries_that_swap_and_excludes_the_next() -> None:
    """CH0's second constant, run against the measured positions.

    The two entries that swap between machines are `1.0041x` apart and the next
    is at `FIGURE_ARGMIN_TIE_WINDOW_COUNTER_DEFECT`. The window has to be above
    the first and below the second, and this asserts both directions.
    """
    base = 3.627517e-14
    edges = [
        (base, "ci_plateau"),
        (base * 1.004125, "ch_edgemin"),
        (base * FIGURE_ARGMIN_TIE_WINDOW_COUNTER_DEFECT, "the_next_one"),
        (base * 1.5, "far_away"),
    ]
    named = R.tie_set(edges, FIGURE_ARGMIN_TIE_WINDOW)
    assert named == ["ch_edgemin", "ci_plateau"], named
    assert "the_next_one" not in named, (
        "the window reaches the first entry it has to exclude, so a change in "
        "the corpus one third as large as the platform spread would change the "
        "published set."
    )


def test_the_tie_set_is_stable_under_a_flip() -> None:
    """The whole point of shape 2: a flip inside the set changes no byte."""
    base = 3.627517e-14
    a = [(base, "ci_plateau"), (base * 1.004125, "ch_edgemin")]
    b = [(base, "ch_edgemin"), (base * 1.004125, "ci_plateau")]
    assert R.tie_set(a, FIGURE_ARGMIN_TIE_WINDOW) == R.tie_set(b, FIGURE_ARGMIN_TIE_WINDOW)


# ------------------------------------------------- the bracket, in the plan


def test_the_spread_bound_is_bracketed_by_its_own_measurements() -> None:
    """`largest measured spread < FIGURE_FLOOR_CLASS_SPREAD < smallest margin`.

    Both halves come from files rather than from this test: the spreads from
    Q8's own table in the plan, the margin from the committed figures. When
    either side moves -- a new machine with a wider spread, or a figure whose
    headroom shrinks -- the bracket closes and this goes red, which is the
    property the tolerance comment claims.
    """
    plan = PLAN.read_text(encoding="utf-8", errors="replace")
    block = plan[plan.index("A third class: the figure IS a round-off magnitude") :]
    block = block[: block.index("| channel class |")]
    # THE LAST COLUMN ONLY. The table is `| figure | CI | laptop | spread |`
    # and the value columns carry an `x` too, so a pattern over the whole row
    # read `0.2564x` -- a VALUE -- as a spread and the bracket compared the
    # bound against the wrong quantity.
    spreads = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[3].startswith("`") and cells[3].endswith("x`"):
            spreads.append(float(cells[3].strip("`").rstrip("x")))
    assert len(spreads) >= 5, f"the plan's spread table parsed to {spreads}"
    assert max(spreads) < FIGURE_FLOOR_CLASS_SPREAD, (
        f"the largest measured spread is {max(spreads)}x and the bound is "
        f"{FIGURE_FLOOR_CLASS_SPREAD}x. A bound below its own measurement is "
        "a bound that reddens on the machine it was measured from."
    )
    figures = R._values(FIGURES.read_text(encoding="utf-8", errors="replace"))
    margins = []
    for name, (kind, _ceil, _log) in R.floor_class().items():
        if kind in ("derived", "words") or name not in figures:
            continue
        value = R._number(figures[name])
        assert value is not None and value > 0, f"{name} is {figures[name]!r}"
        ceiling = R._ceiling(name)
        margins.append(ceiling / value if kind == "below" else value / ceiling)
    assert margins, "no floor-class margin could be measured from the committed figures"
    assert min(margins) > FIGURE_FLOOR_CLASS_SPREAD, (
        f"the smallest floor-class margin is {min(margins):.4g}x and the "
        f"spread bound is {FIGURE_FLOOR_CLASS_SPREAD}x. With the bound above "
        "the margin, a platform disagreement inside the bound could carry a "
        "decision across its ceiling, which is the reasoning the class rests "
        "on."
    )
