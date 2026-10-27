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
import importlib.util
import math
import sys
from pathlib import Path
from types import ModuleType

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
# **R1014: THE EXACT HITS, NOT MERELY "SOME".** The reverse guard below asserted that an
# exempted file still carried a forbidden literal AT ALL, so a PARTIAL repair of half B --
# `9.80665` corrected to `9.81`, still a bare literal -- kept the exemption alive and left
# the leftover unscanned. Measured, three arms: shipped `[(52, 9.80665)]` green, partial
# `[(52, 9.81)]` ALSO green, full repair `[]` red. Declaring the line and the value makes
# the middle arm red too, which is the arm that matters.
EXEMPT_PENDING_FT2_4: dict[Path, list[tuple[int, float]]] = {
    Path("scripts/measure/f6a_required_section.py"): [(52, 9.80665)],
}


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
    for rel, declared in EXEMPT_PENDING_FT2_4.items():
        hits = _gravity_literals(ROOT / rel)
        assert hits == declared, (
            f"{rel.as_posix()} is exempted from FU0 for {declared} and its gravity "
            f"literals are now {hits}. EITHER the repair landed, in which case the "
            f"exemption is stale and gets deleted from `EXEMPT_PENDING_FT2_4` (EK2), OR "
            f"the literal moved or changed value, in which case the exemption no longer "
            f"describes what it is covering and the new state is unscanned. A guard that "
            f"accepts 'some literal, somewhere' accepts a PARTIAL repair."
        )


def test_the_declaring_module_declares_FLOATSIMS_value_and_not_the_standard_one() -> None:
    """9.81, not 9.80665. The frames table publishes this distinction explicitly."""
    # not-a-tolerance: FloatSim's own gravity, the quantity this whole file exists to
    # keep single-sourced. Exact equality against the value directive FU0 names; nothing
    # is being allowed to differ by it, and a window here would be the detector band the
    # `FORBIDDEN` comment above refuses for the same reason.
    assert frames.GRAVITY_MAGNITUDE == 9.81  # not-a-tolerance: FloatSim's declared g
    assert frames.GRAVITY_VECTOR == (0.0, 0.0, -9.81)


def _period_band_loaded_fresh(under_name: str) -> ModuleType:
    """A SECOND module object from `period_band.py`'s own file, left out of `sys.modules`.

    **WHY NOT `importlib.reload`, WHICH IS WHAT THIS CELL USED TO DO -- R1018.** `reload`
    re-executes the module in its EXISTING namespace and leaves the new objects bound in
    `sys.modules`, so every name already imported elsewhere in the process goes on
    pointing at the PRE-reload objects while the module globals hold post-reload ones.
    `Admissibility.may_govern` resolves `Admissibility` through those globals, so for the
    old class -- the one `tests/unit/test_period_band.py` imported at collection -- it
    compared a member of the old class against the new class's `IN_BAND` and returned
    `False` for every member. Fourteen of that file's twenty-eight cells went red, with
    the message `assert False is (<Admissibility.IN_BAND> is <Admissibility.IN_BAND>)` --
    two objects that print identically and are not identical.

    It was invisible to every measurement this commit took: the two files alone give
    `28 passed`, and CI runs `pytest tests/unit` in a different process from the root
    `tests/test_*.py` files, so no job there runs them together. Only a whole-suite run
    sees it, and the reviewer's did.

    `spec_from_file_location` + `module_from_spec` + `exec_module` gives a module object
    that executes `period_band.py` from source, binding whatever `frames.GRAVITY_MAGNITUDE`
    is at that moment, and NOTHING in `sys.modules` is replaced -- which is the whole
    property the repair needs. The assertion below keeps that property honest.
    """
    spec = importlib.util.spec_from_file_location(under_name, Path(period_band.__file__))
    assert spec is not None and spec.loader is not None
    fresh = importlib.util.module_from_spec(spec)
    # **THE `sys.modules` ENTRY IS REQUIRED AND IT IS NOT THE ONE R1018 IS ABOUT.**
    # `period_band` declares `CaseBand` as a dataclass, and `dataclasses._process_class`
    # resolves annotations through `sys.modules.get(cls.__module__).__dict__`; without an
    # entry under THIS name that is `None.__dict__` --
    # `AttributeError: 'NoneType' object has no attribute '__dict__'`, measured. So the
    # entry goes in under the PROBE's name, which `floatfea.loads.period_band` is not, and
    # comes out again in `finally`. The live module is never rebound, which is the one
    # thing `importlib.reload` could not avoid.
    sys.modules[under_name] = fresh
    try:
        spec.loader.exec_module(fresh)
    finally:
        del sys.modules[under_name]
    return fresh


def test_the_SCREENS_wavelength_reads_the_FRAMES_value() -> None:
    """FU0's second clause: a patched frames value moves the screen's `lambda`.

    `period_band` binds `GRAVITY_MAGNITUDE` at import, which is the idiom every other
    consumer uses (`floatfea/loads/selfweight.py`, `floatfea/solve/static.py`), so the
    dependency is proved by EXECUTING the module's source against a patched frames rather
    than by patching an attribute the function never re-reads. A test that patched
    `period_band.GRAVITY_MAGNITUDE` and passed would prove nothing about where the value
    comes from.
    """
    period_s = 10.0
    before = period_band.deep_water_wavelength(period_s)
    original = frames.GRAVITY_MAGNITUDE
    live = sys.modules["floatfea.loads.period_band"]
    try:
        # A value nothing could arrive at by accident.
        frames.GRAVITY_MAGNITUDE = 1.0  # type: ignore[misc]
        probe = _period_band_loaded_fresh("_period_band_at_patched_gravity")
        after = probe.deep_water_wavelength(period_s)
    finally:
        frames.GRAVITY_MAGNITUDE = original  # type: ignore[misc]

    # **THE PROPERTY R1018 COST FOURTEEN CELLS, ASSERTED RATHER THAN ARGUED.** The module
    # every other test holds is the same OBJECT it was before this cell ran, and the probe
    # is a different one that never entered `sys.modules`.
    assert sys.modules["floatfea.loads.period_band"] is live
    assert sys.modules["floatfea.loads.period_band"] is period_band
    assert probe is not period_band
    assert "_period_band_at_patched_gravity" not in sys.modules
    assert probe.Admissibility is not period_band.Admissibility, (
        "the probe did not re-execute the module source, so the two assertions below "
        "would be comparing one module against itself"
    )

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
    # And the restore worked -- of the VALUE, which is all a restore can be once nothing
    # is reloaded. The four assertions above are what says no later test inherits a
    # patched MODULE, and the sentence that used to stand here claimed the second from a
    # measurement of the first. That was R1018's cover.
    assert period_band.deep_water_wavelength(period_s) == before
