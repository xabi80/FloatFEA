"""ONE GRAVITY (directive FU0, `docs/directives/FU.md`).

The project uses FloatSim's value, `9.81 m/s^2`, read from
`floatfea.io.frames.GRAVITY_MAGNITUDE`. No other gravity literal lives in `floatfea/`
or `scripts/`.

**WHY, AND IT IS R1004.** `floatfea/io/frames.py` declares `GRAVITY_MAGNITUDE = 9.81`
and its own published frames table calls the value out explicitly -- "magnitude 9.81,
FloatSim's value, **not** 9.80665" -- while two measure scripts declared their own
`GRAVITY = 9.80665` and two further sites carried `9.81` as a bare literal. Every force
in the model consumes the frames value; the sea-state screen consumed a different one.
Measured, with each producer run at both values:

* `scripts/measure/f6_results_report.py` -- 2 of 6 published `H/lambda` figures differ
  at the printed 4 dp (`T = 10 s`: `0.1551` against `0.1550`). **No BREAKING verdict
  flips**, so the governing set does not move.
* `scripts/measure/f6a_required_section.py` -- all 6 data rows of
  `results/F6a/required_section.csv` differ, and five JSON fields move
  (`implied_root_moment_nm` `259048069.9214031` against `259136562.01954436`). **Every
  ratio is unchanged** -- `implied_root_moment_ratio` is `2.254127077030355` against
  `2.2541270770303554` -- because the ratios are `g`-independent, so no conclusion moves.

Relative size of the disagreement: `3.416e-04`. Wrong absolute numbers in two tracked
deliverables, no wrong finding. Under FR1 that is the second head -- an input accepted
and used other than as declared.

**WHY THIS TEST PARSES INSTEAD OF GREPPING.** FU0's own suggested check is
`grep 9.80665 ... returns 0`, and that check is not sufficient for the rule FU0 states:
two of the four sites carried `9.81`, the *right* value as a bare literal, which the grep
cannot see, and after the repair the surviving textual hits are all comments describing
the repair, which the grep *would* see. A float constant is found exactly by reading the
syntax tree and cannot be hidden in a comment or revealed by reformatting.
"""

from __future__ import annotations

import ast
import importlib
import math
from pathlib import Path

from floatfea.io import frames
from floatfea.loads import period_band

ROOT = Path(__file__).resolve().parents[1]
ROOTS = ("floatfea", "scripts")

# The spellings a gravity constant has actually taken in this repository, plus the two
# other common ones. EXACT EQUALITY against this tuple -- there is no window here and no
# epsilon. A detector band such as "any float in 9.7 .. 9.9" would be a tier cutoff in a
# screen, which `CLAUDE.md` treats as a tolerance under another name, and it would
# therefore belong in `floatfea/tolerances.py` with a justification. An enumerated list
# of literals needs neither.
FORBIDDEN: tuple[float, ...] = (9.81, 9.80665, 9.8, 9.807)

# The ONE module permitted to declare the value.
DECLARING = Path("floatfea/io/frames.py")

# FU0 routes half B -- `scripts/measure/f6a_required_section.py` -- to FT2.4's commit,
# together with the regeneration of `results/F6a/required_section.csv` and its cover
# note. Until that commit lands the file still declares `GRAVITY = 9.80665`.
#
# **THE EXEMPTION CANNOT OUTLIVE THE REPAIR**, which is the half that makes this a
# declaration rather than a skip: `test_every_exemption_is_STILL_NEEDED` asserts that
# each exempted file still contains a forbidden literal, so the commit that fixes half B
# turns this list red and forces its deletion. A guard that fails false is fixed or
# deleted, never extended (EK2).
EXEMPT_PENDING_FT2_4 = (Path("scripts/measure/f6a_required_section.py"),)


def _sources() -> list[Path]:
    out: list[Path] = []
    for root in ROOTS:
        out.extend(sorted((ROOT / root).rglob("*.py")))
    assert out, "no sources found; the roots moved"
    return out


def _gravity_literals(path: Path) -> list[tuple[int, float]]:
    """Every float constant in `path` equal to one of `FORBIDDEN`, with its line."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: list[tuple[int, float]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue
        value = node.value
        # `isinstance(True, int)` is True, so booleans are excluded explicitly.
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            continue
        if any(float(value) == f for f in FORBIDDEN):
            found.append((node.lineno, float(value)))
    return found


def test_NO_gravity_literal_outside_the_declaring_module() -> None:
    """FU0: `floatfea.io.frames` is the single source and nothing else spells it out."""
    offenders: dict[str, list[tuple[int, float]]] = {}
    for path in _sources():
        rel = path.relative_to(ROOT)
        if rel == DECLARING or rel in EXEMPT_PENDING_FT2_4:
            continue
        hits = _gravity_literals(path)
        if hits:
            offenders[rel.as_posix()] = hits
    assert not offenders, (
        "a gravity literal lives outside `floatfea/io/frames.py` (FU0). Read the value "
        "from `floatfea.io.frames.GRAVITY_MAGNITUDE`, or -- for the sea-state screen -- "
        f"call `floatfea.loads.period_band`, which already does: {offenders}"
    )


def test_every_exemption_is_STILL_NEEDED() -> None:
    """An exemption whose file no longer offends is deleted, not carried (EK2).

    This is what stops `EXEMPT_PENDING_FT2_4` becoming a permanent hole. When FT2.4
    repairs half B this test fails, and the only repair for it is removing the entry.
    """
    for rel in EXEMPT_PENDING_FT2_4:
        hits = _gravity_literals(ROOT / rel)
        assert hits, (
            f"{rel.as_posix()} is exempted from FU0 but carries no gravity literal any "
            "more. The exemption is stale: delete it from `EXEMPT_PENDING_FT2_4`."
        )


def test_the_declaring_module_declares_FLOATSIMS_value_and_not_the_standard_one() -> None:
    """9.81, not 9.80665. The frames table publishes this distinction explicitly."""
    assert frames.GRAVITY_MAGNITUDE == 9.81
    assert frames.GRAVITY_VECTOR == (0.0, 0.0, -9.81)


def test_the_SCREENS_wavelength_reads_the_FRAMES_value() -> None:
    """FU0's second clause: a patched frames value moves the screen's `lambda`.

    `period_band` binds `GRAVITY_MAGNITUDE` at import, which is the idiom every other
    consumer uses (`floatfea/loads/selfweight.py`, `floatfea/solve/static.py`), so the
    dependency is proved by reloading the module against a patched frames rather than by
    patching an attribute the function never re-reads. A test that patched
    `period_band.GRAVITY_MAGNITUDE` and passed would prove nothing about where the value
    comes from.
    """
    period_s = 10.0
    before = period_band.deep_water_wavelength(period_s)
    original = frames.GRAVITY_MAGNITUDE
    try:
        # A value nothing could arrive at by accident.
        frames.GRAVITY_MAGNITUDE = 1.0  # type: ignore[misc]
        reloaded = importlib.reload(period_band)
        after = reloaded.deep_water_wavelength(period_s)
    finally:
        frames.GRAVITY_MAGNITUDE = original  # type: ignore[misc]
        importlib.reload(period_band)

    # **BOTH ASSERTIONS ARE BIT-EXACT, AND THE FORM MATTERS.** The first version of this
    # compared `after` with `before / 9.81` and failed by 2 ulp -- `15.915494309189533`
    # against `15.915494309189535` -- because dividing the result is not the same
    # floating-point operation as multiplying by a different `g`. The repair is to assert
    # the thing that is exactly true, which is the function's own expression evaluated at
    # each `g`, NOT to introduce a comparison epsilon. An epsilon here would have been a
    # tolerance living outside `floatfea/tolerances.py` to rescue a test, which is the
    # one thing `CLAUDE.md` forbids outright.
    assert after == 1.0 * period_s * period_s / (2.0 * math.pi), (
        f"patching the frames gravity to 1.0 left the screen's wavelength at {after}; "
        f"the screen is not reading the single source"
    )
    assert before == 9.81 * period_s * period_s / (2.0 * math.pi)
    # And the restore worked, so no later test inherits a patched module.
    assert period_band.deep_water_wavelength(period_s) == before
