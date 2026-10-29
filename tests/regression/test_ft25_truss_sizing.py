"""FT2.5: `outputs.truss_sizing` -- the shared loop, and the truss it implies.

**THE SHAPE OF THIS WAS RULED, NOT CHOSEN.** The gate row says "truss_sizing likewise",
and the obvious reading -- re-solve the FE model at the selected TRUSS -- is not available:
the truss sizer's answer is a truss and `build_model` builds tubes. The ruling is that the
grid stays tubes, which is what `docs/milestones/R1.md` section 4 already says ("the
candidate grid is the config declared section list") as one of the three reasons R1 needs no
tolerance. So `truss_sizing` runs the SAME loop as `required_section` over the SAME grid,
and adds the truss resolution at the accepted tube's forces.

The alternative was ruled out on a measurement rather than on taste: the only truss-to-tube
bridge in the repository is `A_c h^2 / STANDIN_I`, and `STANDIN_I = 0.888` is exact for the
DECLARED section and wrong by `1.719x` at the section `required_section` actually chose
(`I_y = 1.5264` at `wall = 0.410 m`). A constant standing in for a function of the
configuration on a production path is R694 by name.

What this file holds, in order: the resolutions against their own closed-form identities,
the two geometry readings, the schema, and then the end-to-end wiring -- because FT2's
standing rule is that every repair's CALLER is held by a test.
"""

from __future__ import annotations

import math
import re
import shutil
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.run.config import ConfigError, Material, TrussOptions, load_config
from floatfea.run.pipeline import run as run_pipeline
from floatfea.run.sizing import governing_rows, size_truss
from floatfea.run.truss import (
    GEOMETRIES,
    ChordForces,
    Face,
    area_for_compression,
    area_for_tension,
    box_resolution,
    chord_buckling_length,
    enclosed_area,
    faces,
    panel_and_diagonal,
    resolve_group,
    triangle_resolution,
)

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "platform12_placeholder.yaml"
TRIMMED_STEPS = 40

# One representative beam-force set. The torsion is deliberately LARGE, for the reason
# `test_the_TORSION_term_is_what_distinguishes_the_two_shapes_vertical_face`
# records.
N, VY, VZ, T, MY, MZ = -1.0e6, 2.0e5, 3.0e5, 5.0e6, 1.9e8, 2.7e8

MATERIAL = Material(e=210e9, g=80.769230769e9, rho=7850.0, fy=355e6)
"""S355, for the cells that call a resolution directly rather than through a run."""


# ---------------------------------------------------------------------------
# The resolutions, against the identities their own derivations state
# ---------------------------------------------------------------------------
def test_the_BOX_resolution_satisfies_its_own_equilibrium_identities() -> None:
    """`sum F = N`, `sum F z = My`, `sum F y = Mz`, for four chords at `(+-b/2, +-h/2)`.

    The docstring derives `f = My/(2h)` and `g = Mz/(2b)` rather than quoting them; these
    are the three identities that derivation has to satisfy, checked exactly rather than
    through a tolerance -- the arithmetic is a handful of adds and the sums are exact.
    """
    h, b = 8.0, 3.0
    r = box_resolution(N, VY, VZ, T, MY, MZ, h, b)
    assert r.chords.keys() == {"top_+b", "top_-b", "bot_+b", "bot_-b"}
    # **EXACTLY, with no tolerance of any kind.** Measured: all three identities hold
    # at exact float equality for the box, because `N/4` and the `+-My/(2h)`,
    # `+-Mz/(2b)` pairs are exact in binary and cancel exactly.
    assert sum(r.chords.values()) == N
    # z = +h/2 for the two `top` chords, -h/2 for the two `bot`.
    moment_y = sum(
        force * (h / 2.0 if name.startswith("top") else -h / 2.0)
        for name, force in r.chords.items()
    )
    assert moment_y == MY
    # y = +b/2 for the two `+b` chords, -b/2 for the two `-b`.
    moment_z = sum(
        force * (b / 2.0 if name.endswith("+b") else -b / 2.0) for name, force in r.chords.items()
    )
    assert moment_z == MZ


def test_the_TRIANGLE_resolution_satisfies_its_own_identities_and_the_APEX_carries_no_Mz() -> None:
    """`sum F = N`, `sum M = My`, and the apex has NO `Mz` term -- it is on the centreline.

    The last is the asymmetry the docstring calls a result rather than a detail: horizontal
    bending is resisted by the bottom pair alone, on lever `b`, where the box has two
    pairs. A resolution that gave the apex an `Mz` share would be resolving a different
    truss.
    """
    h, b = 8.0, 3.0
    r = triangle_resolution(N, VY, VZ, T, MY, MZ, h, b)
    assert r.chords.keys() == {"apex", "bot_+b", "bot_-b"}

    # **THE COEFFICIENTS ARE ASSERTED EXACTLY AND THE GLOBAL SUMS ARE NOT ASSERTED.**
    # The identities `sum F = N` and `sum M = My` are exact in exact arithmetic and NOT in
    # float here: measured, `3 * (-1e6/3)` is `-999999.9999999888`, and `sum F z` is
    # `189999999.99999997`, a relative residual of `1.57e-16`. Asserting them would need a
    # round-off threshold -- a number chosen to make two quantities agree -- and it would
    # buy nothing: the defect this cell exists to catch is a WRONG COEFFICIENT, whose
    # residual is of order `My` itself. So each coefficient is checked against the
    # derivation directly, and every assertion below is one subtraction of the same
    # quantity the code added, so each holds at EXACT float equality.
    #
    # The box's identities ARE exact and are asserted as such in the cell above. The
    # difference is that `N/4` and `My/(2h)` are exact in binary where `N/3` is not.
    axial = N / 3.0
    assert r.chords["apex"] - axial == MY / h
    assert r.chords["bot_+b"] - axial - MZ / b == -MY / (2.0 * h)
    assert r.chords["bot_-b"] - axial + MZ / b == -MY / (2.0 * h)

    # THE APEX IS INDEPENDENT OF Mz: one variable moved, Mz doubled.
    doubled = triangle_resolution(N, VY, VZ, T, MY, 2.0 * MZ, h, b)
    assert doubled.chords["apex"] == r.chords["apex"]
    assert doubled.chords["bot_+b"] != r.chords["bot_+b"]


def test_the_TORSION_term_is_what_distinguishes_the_two_shapes_vertical_face() -> None:
    """The triangle's shear flow is twice the box's, because its enclosed area is half.

    **THIS CELL EXISTS BECAUSE THE PUBLISHED TABLE LOOKS LIKE A BUG AND IS NOT.** On the
    shipped deck the box and the triangle report the SAME diagonal area, which reads as a
    shared code path. It is not: the platform arms' torsion is near zero by symmetry, so
    both shapes' vertical-face shear collapses to `|Vz|/2`, which is identical by
    construction -- and the vertical face governs the diagonal. With a torsion that
    matters, the two diverge, and this is the measurement that says so.
    """
    h, b = 8.0, 3.0
    assert enclosed_area("box", h, b) == 2.0 * enclosed_area("triangle", h, b)
    box = box_resolution(N, VY, VZ, T, MY, MZ, h, b)
    tri = triangle_resolution(N, VY, VZ, T, MY, MZ, h, b)
    assert tri.face_shear["inclined"] > box.face_shear["vertical"]
    # And with NO torsion they coincide exactly, which is the deck's own case.
    box0 = box_resolution(N, VY, VZ, 0.0, MY, MZ, h, b)
    tri0 = triangle_resolution(N, VY, VZ, 0.0, MY, MZ, h, b)
    assert box0.face_shear["vertical"] == tri0.face_shear["inclined"] == abs(VZ) / 2.0


# ---------------------------------------------------------------------------
# The two readings of FI1's 45-degree panel (R801)
# ---------------------------------------------------------------------------
def test_the_two_GEOMETRY_readings_differ_in_the_direction_R801_names() -> None:
    """`per_face_45` buckles over `max(h, b)`; `uniform_panel` over `min(h, b)`.

    R801 is that the first version of the measure script took the SHORTER buckling length
    from one reading and the SHORTER diagonal from the other -- the favourable half of each.
    So the trade has to go the other way in each: the reading with the shorter chord has the
    LONGER diagonals.
    """
    h, b = 8.0, 3.0
    assert chord_buckling_length("per_face_45", h, b) == max(h, b)
    assert chord_buckling_length("uniform_panel", h, b) == min(h, b)
    vertical = faces("box", h, b)[0]
    # TWO returns, not three: `panel_and_diagonal` no longer hands back the chord buckling
    # length. That duplicate of `chord_buckling_length` is what invited R1069.
    d45, steel45 = panel_and_diagonal("per_face_45", h, b, vertical)
    du, steelu = panel_and_diagonal("uniform_panel", h, b, vertical)
    # **EXACTLY, and no tolerance.** `panel_and_diagonal` computes `panel * sqrt(2)` with
    # `panel = face.dimension = h`, and `hypot(panel, face.dimension)` with
    # `panel = min(h, b) = b` -- so each assertion below is the same float expression the
    # code evaluated, and an `approx` here would have been a tolerance standing in for an
    # identity.
    assert d45 == h * math.sqrt(2.0)
    assert du == math.hypot(b, h)
    # THE TRADE: the shorter chord costs more diagonal steel per metre.
    assert steelu > steel45


def test_at_h_EQUALS_b_the_two_readings_COINCIDE_exactly() -> None:
    """A square box has one panel dimension, so the two readings cannot differ.

    This is the control for the cell above: without it, `steelu > steel45` could be an
    artefact of a reading that is always heavier rather than of the aspect ratio.
    """
    h = b = 4.0
    assert chord_buckling_length("per_face_45", h, b) == chord_buckling_length(
        "uniform_panel", h, b
    )
    for face in faces("box", h, b):
        assert panel_and_diagonal("per_face_45", h, b, face) == panel_and_diagonal(
            "uniform_panel", h, b, face
        )


# ---------------------------------------------------------------------------
# The schema
# ---------------------------------------------------------------------------
def _sections_with(truss: object) -> dict[str, Any]:
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    block = yaml.safe_load(yaml.safe_dump(data["sections"]))
    block["truss"] = truss
    return block


GOOD = {"depths": [3.0, 8.0], "widths": [3.0], "shapes": ["box"]}


def test_FT2_5_a_declared_truss_block_is_PARSED() -> None:
    """The declared values reach `TrussOptions`, and the defaults are FI's own."""
    from floatfea.run.config import _parse_sections

    parsed = _parse_sections(_sections_with(GOOD)).truss
    assert parsed.depths == (3.0, 8.0)
    assert parsed.widths == (3.0,)
    assert parsed.shapes == ("box",)
    # not-a-tolerance: FI's own declared design parameters, in the same class as
    # `code_check.k = 2.0` and `cm = 0.85` -- options of the idealisation being applied,
    # which the run reports and another configuration may legitimately set otherwise.
    # Nothing is being allowed to DIFFER by either: both are exact equality against the
    # value `TrussOptions` declares, and the point of the cell is that the parser preserves
    # the declared default rather than inventing one.
    assert parsed.d_over_t == 24.0  # not-a-tolerance: a declared option, exact
    assert parsed.joint_allowance == 1.15  # not-a-tolerance: a declared option, exact
    # THE FLOOR IS THE DECLARED TUBE-DIAMETER MINIMUM, not the measure script's 0.02 m --
    # which the bounds check refuses, as the first run of this block discovered.
    assert parsed.diameter_search == (0.05, 6.0)
    # THE WEAKENING DIRECTION of R1071's refusal: an INT is a number and must still be
    # accepted, or declaring `d_over_t: 24` rather than `24.0` would be refused for
    # nothing. `isinstance(True, int)` is why the bool test has to come first.
    from floatfea.run.config import _parse_truss as _pt

    widened = _pt({**GOOD, "d_over_t": 24, "joint_allowance": 1}, "sections.truss")
    assert widened.d_over_t == 24.0  # not-a-tolerance: a declared option, exact
    assert widened.joint_allowance == 1.0


@pytest.mark.parametrize(
    "truss, needle",
    [
        pytest.param({**GOOD, "depths": []}, "no `(h, b)` grid", id="no_depths"),
        pytest.param({**GOOD, "widths": []}, "no `(h, b)` grid", id="no_widths"),
        pytest.param({**GOOD, "depths": [0.0]}, "must be positive", id="a_zero_depth"),
        pytest.param({**GOOD, "widths": [-3.0]}, "must be positive", id="a_negative_width"),
        pytest.param({**GOOD, "shapes": ["hexagon"]}, "not a label", id="an_unknown_shape"),
        pytest.param({**GOOD, "shapes": []}, "no cross-section", id="no_shapes"),
        pytest.param({**GOOD, "d_over_t": 2.0}, "has no bore", id="a_solid_chord"),
        pytest.param(
            {**GOOD, "joint_allowance": 0.9}, "REMOVES steel", id="an_allowance_below_one"
        ),
        # R1071: `_floats` refused a bool and a string for the LISTS twenty lines away and
        # these two scalars did not. YAML turns `yes` into `True`, `float(True)` is `1.0`,
        # and `validate`'s `< 1.0` passes it -- so every `steel/m` figure would publish
        # with NO joint allowance -- chord AND diagonal steel 13% low against the
        # declared 1.15 (L11).
        pytest.param(
            {**GOOD, "joint_allowance": True}, "is not a number", id="an_allowance_of_yes"
        ),
        pytest.param(
            {**GOOD, "joint_allowance": "1.15"}, "is not a number", id="an_allowance_as_text"
        ),
        pytest.param({**GOOD, "d_over_t": True}, "is not a number", id="a_D_over_t_of_yes"),
        pytest.param({**GOOD, "d_over_t": "24"}, "is not a number", id="a_D_over_t_as_text"),
        pytest.param(
            {**GOOD, "diameter_search": [6.0, 0.05]},
            "not an increasing bracket",
            id="a_reversed_bracket",
        ),
        pytest.param(
            {**GOOD, "diameter_search": [0.01, 6.0]},
            "outside the admissible range",
            id="a_bracket_below_the_tube_domain",
        ),
        pytest.param({**GOOD, "depths": 3.0}, "expected a list", id="a_scalar_depth_list"),
        pytest.param({**GOOD, "nonsense": 1}, "unrecognised field", id="an_unknown_key"),
        pytest.param(7, "expected a mapping", id="a_scalar_block"),
    ],
)
def test_FT2_5_the_truss_block_is_REFUSED_by_name(truss: object, needle: str) -> None:
    """Each of these would otherwise reach the resolution or the sizing.

    `a_bracket_below_the_tube_domain` is the one worth reading: a chord IS a tube, so every
    value in `diameter_search` goes through the same `_checked` bound a declared `d_outer`
    goes through. It cannot be admissible here and refused as a section.
    """
    from floatfea.run.config import _parse_sections

    with pytest.raises(ConfigError) as caught:
        _parse_sections(_sections_with(truss))
    assert needle in str(caught.value), str(caught.value)


def test_FT2_5_a_configuration_with_NO_truss_block_still_LOADS() -> None:
    """The weakening direction: every configuration written before FT2.5 must still load.

    `TrussOptions`' default has EMPTY grids, which `validate` refuses -- so the default is
    constructed unvalidated when the block is absent and validated only when declared.
    Without that, the shipped example would stop loading.
    """
    cfg = load_config(EXAMPLE)
    assert cfg.sections.truss.depths == ()
    assert cfg.outputs.truss_sizing is False


# ---------------------------------------------------------------------------
# End to end
# ---------------------------------------------------------------------------
def _fixture(
    tmp_path: Path,
    *,
    candidates: dict[str, list[dict[str, float]]] | None = None,
    truss: dict[str, Any] | None = None,
    truss_sizing: bool = True,
    required_section: bool = False,
) -> tuple[Path, Path]:
    """The shipped example with `lam` AND `times` trimmed. See FT2.4's fixture for why."""
    data: dict[str, Any] = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    src = (EXAMPLE.parent / data["load_cases"]["npz"]).resolve()
    local = tmp_path / "data"
    local.mkdir(exist_ok=True)
    shutil.copy2(src, local / src.name)
    shutil.copy2(src.with_suffix(".provenance.json"), local / f"{src.stem}.provenance.json")
    npz = local / src.name
    raw = np.load(npz, allow_pickle=False)
    trim = ("/lam", "/times")
    np.savez(
        npz,
        **{k: (raw[k][:TRIMMED_STEPS] if k.endswith(trim) else raw[k]) for k in raw.files},
    )
    data["load_cases"]["npz"] = str(npz)
    data["sections"]["candidates"] = candidates or {
        "platform": [{"d_outer": 2.5, "wall": 0.18}, {"d_outer": 2.5, "wall": 0.41}]
    }
    data["sections"]["truss"] = truss or GOOD
    out_dir = tmp_path / "out"
    data["outputs"]["directory"] = str(out_dir)
    data["outputs"]["truss_sizing"] = truss_sizing
    data["outputs"]["required_section"] = required_section
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path, out_dir


def test_END_TO_END_truss_sizing_writes_its_artifact_and_DISCLAIMS_the_U(tmp_path) -> None:
    """The artifact, and condition 1 of the ruling: the `U` is the TUBE's, said up front.

    A reader must not be able to read `U = 0.99` as a statement about the truss. FT2.4's
    artifacts label two configurations of the same representation; this labels two
    REPRESENTATIONS, which is a stronger claim to have to disclaim -- so the disclaimer is
    the first section of the file and the cell asserts it is.
    """
    from floatfea import cli

    path, out_dir = _fixture(tmp_path)
    assert cli.main(["run", str(path)]) == 0
    assert sorted(p.name for p in out_dir.glob("*")) == [
        "member_forces.csv",
        "report.md",
        "truss_sizing.md",
        "utilisation.csv",
    ]
    text = (out_dir / "truss_sizing.md").read_text(encoding="utf-8")
    head = text.split("## The tube the loop accepted")[0]
    assert "READ THIS BEFORE ANY NUMBER BELOW" in head, head
    assert "evaluated on the TUBE, not on the truss" in head, head
    assert "never" in head and "re-solved**" in head, head
    assert "That is the tube's utilisation." in head, head
    # The loop ran and reported BOTH max U values, which is FM0's own requirement.
    assert "fixed-force max U" in text and "re-solved max U" in text, text
    assert "**1 re-solve(s).**" in text, text
    # Both readings published (R801), and the declared parameters stated.
    for geometry in GEOMETRIES:
        assert geometry in text, geometry
    assert "`D/t = 24`" in text, text
    # **R1074: the governing-face sentence must describe THIS run's cells**, not a figure
    # carried from another deck. The arm for it did not redden until this assertion
    # existed -- nothing read that sentence.
    # **THE COUNT IS PER CANDIDATE GROUP, and the formula here was group-blind.** It
    # multiplied depths x widths x shapes x readings and was green only because this
    # fixture declares ONE group; at two groups the artifact says 16 and the formula gave
    # 8. It is derived from the report's own structure now, which is what the sentence is
    # derived from.
    cfg = load_config(path)
    per_group = (
        len(cfg.sections.truss.depths)
        * len(cfg.sections.truss.widths)
        * len(cfg.sections.truss.shapes)
        * len(GEOMETRIES)
    )
    expected_cells = per_group * len(cfg.sections.candidates)
    assert f"Of the {expected_cells} cells in the tables above" in text, text
    assert "60 declared cells" not in text, "a figure from another deck is published here"
    # **AND THE FACE NAMES ARE READ, which is what nothing did (R1078).** A triangle has
    # no vertical face; if the sentence says one governs, the count is conflating shapes.
    # The GENERATED COUNT, not the whole document: the explanatory prose names the
    # inclined face wherever it describes the mechanism, and should.
    if "triangle" not in cfg.sections.truss.shapes:
        assert "governed by the inclined face" not in text, (
            "a box-only configuration reports an inclined face governing, which is the "
            "shear-key conflation R1078 was about"
        )
    assert "governed by the" in text, text


def test_END_TO_END_the_truss_is_resolved_at_the_ACCEPTED_forces_not_the_BASELINE(
    tmp_path,
) -> None:
    """Condition 2 of the ruling, held by a bitwise discrimination.

    **THE DISCRIMINATION IS REAL BUT IT IS SMALL, AND SAYING SO IS THE POINT.** Measured on
    this deck: of the 12 governing-basis rows of the platform group, **zero are
    bit-identical** between the baseline solve and the accepted one, and the largest
    relative component move is `3.5` -- on a quantity that is near zero by symmetry. The
    published chord area moves only `1.7e-14`, because it is driven by the moment terms. So
    this cell detects the PLUMBING rather than a visible defect, and it is taken because it
    is free: a truss resolved from baseline forces is sized for loads the structure does not
    carry at the section the loop chose, and the gap is bounded nowhere.
    """
    path, _out = _fixture(tmp_path, truss={"depths": [8.0], "widths": [3.0], "shapes": ["box"]})
    cfg = load_config(path)
    baseline = run_pipeline(cfg)
    report = size_truss(cfg, baseline)

    from_baseline = governing_rows(cfg, baseline, "platform")
    from_accepted = governing_rows(cfg, report.sizing.final, "platform")
    assert [label for label, _v in from_baseline] == [label for label, _v in from_accepted]
    # NON-VACUITY: the two force sets genuinely differ, so the assertion below can fail.
    # `strict=True` and not ruff's suggested `strict=False`: a length mismatch must fail
    # loudly, because a silently truncated zip makes this very assertion vacuous.
    assert all(b != a for (_lb, b), (_la, a) in zip(from_baseline, from_accepted, strict=True))

    expected = resolve_group("platform", from_accepted, cfg.sections.truss, cfg.sections.material)
    wrong = resolve_group("platform", from_baseline, cfg.sections.truss, cfg.sections.material)
    (published,) = report.trusses
    for cell, good, bad in zip(published.cells, expected.cells, wrong.cells, strict=True):
        assert cell.chord_area == good.chord_area, (cell, good)
        assert cell.chord_area != bad.chord_area, (
            "the published chord area is bit-identical to the one the BASELINE forces give, "
            "so this cell cannot tell which force set was used"
        )


def test_END_TO_END_BOTH_analyses_set_is_REFUSED_and_writes_nothing(tmp_path, capsys) -> None:
    """They are one loop over one grid; running both solves the model twice for one answer.

    Refused before any output is written, so nothing on disk describes a run that did not
    happen (R809).
    """
    from floatfea import cli

    path, out_dir = _fixture(tmp_path, required_section=True, truss_sizing=True)
    assert cli.main(["run", str(path)]) == 2
    message = capsys.readouterr().err
    assert "both set" in message, message
    assert "solves the model twice" in message, message
    assert not out_dir.exists() or sorted(out_dir.glob("*")) == [], list(out_dir.glob("*"))


def test_END_TO_END_a_demand_outside_the_declared_BRACKET_is_REFUSED(tmp_path, capsys) -> None:
    """The compression sizing refuses rather than extrapolating, and names what to widen.

    A 0.1 m upper bound cannot carry the platform arm's chord force over any panel. The
    refusal has to say which declared value to change, because "no tube up to D = 0.1 m"
    with no pointer is a message a reader cannot act on.
    """
    from floatfea import cli

    path, out_dir = _fixture(
        tmp_path,
        truss={**GOOD, "diameter_search": [0.05, 0.1]},
    )
    # `cli.main` CATCHES `ConfigError` and returns 2 with the message on stderr, which
    # is what a user sees: a message rather than a traceback.
    assert cli.main(["run", str(path)]) == 2
    message = capsys.readouterr().err
    assert "Refused, not extrapolated" in message, message
    assert "sections.truss.diameter_search" in message, message
    assert not out_dir.exists() or sorted(out_dir.glob("*")) == [], list(out_dir.glob("*"))


def test_a_force_row_with_the_WRONG_COMPONENT_COUNT_is_REFUSED_by_name() -> None:
    """The six components are counted, not unpacked blind.

    **THIS CELL EXISTS BECAUSE THE REVERT ARM FOR THAT GUARD DID NOT REDDEN.** I predicted
    it would not -- nothing else in the suite feeds a short row -- and a guard nothing
    exercises is a guard nobody has seen refuse, which is R1060's lesson at a smaller
    scale. So the choice was a cell or a deletion (EK2), and a cell is one line.

    The defect it stops is specific: `Row.values` is a `tuple[float, ...]` as far as the
    type says, and the resolutions take exactly `(N, Vy, Vz, T, My, Mz)`. A row of five
    would shift every argument one place -- `My` arriving where `T` belongs -- and produce
    a perfectly plausible truss from the wrong moment.
    """
    short = [("platform:hub1_arm ROOT", (1.0, 2.0, 3.0, 4.0, 5.0))]
    with pytest.raises(ConfigError) as caught:
        resolve_group("platform", short, load_config(EXAMPLE).sections.truss, MATERIAL)
    message = str(caught.value)
    assert "carries 5 force components where the resolutions take six" in message, message
    assert "shift every argument one place" in message, message


def test_R1069_the_DIAGONAL_FORCE_is_V_L_over_d_from_STATICS(tmp_path) -> None:
    """The assertion that was missing, and whose absence let a wrong formula ship.

    **NO CELL IN THIS FILE ASSERTED AN ABSOLUTE DIAGONAL FORCE.** The R801 pair asserts the
    TRADE between the two readings and the lengths; nothing pinned the force, so a wrong
    force ratio passed everything. It shipped in `739364a` and reached
    `truss_sizing.md`'s diagonal area, its steel-per-metre and therefore the cell it
    RECOMMENDS.

    **THE IDENTITY, derived rather than quoted.** One braced panel as a pin-jointed free
    body: chords at `(0,0)-(p,0)` and `(0,d)-(p,d)`, diagonal across. A cut perpendicular to
    the truss axis crosses both chords and the diagonal; the chords are parallel to the axis
    so their transverse component is ZERO, and the diagonal alone carries the shear:

        F_d * (d / L) = V        =>      F_d = V * L / d = V / sin(theta)

    **AND THE CELL ASSERTS THE WRONG FORMULA DIFFERS, which is what makes it non-vacuous
    and is why it is driven at `h != b`.** `V L / d` and `V L / p` coincide exactly when
    `p == d` -- which is `per_face_45` by construction. My own first-principles check agreed
    with the wrong formula for precisely that reason, and
    `test_at_h_EQUALS_b_the_two_readings_COINCIDE_exactly` sits where every candidate
    denominator agrees. A cell that cannot separate them proves nothing.
    """
    h, b = 8.0, 3.0
    shear = 8.33e5
    rows = [("probe ROOT", (0.0, 0.0, shear, 0.0, 0.0, 0.0))]
    truss = TrussOptions(depths=(h,), widths=(b,), shapes=("box",))
    group = resolve_group("platform", rows, truss, MATERIAL)

    for cell in group.cells:
        # The vertical faces take `Vz`, so with `Vy = T = 0` the vertical face governs and
        # its own shear is `|Vz| / 2` -- which `test_the_TORSION_term...` pins separately.
        vertical = faces("box", h, b)[0]
        length, steel_factor = panel_and_diagonal(cell.geometry, h, b, vertical)
        statics = (shear / 2.0) * length / vertical.dimension
        wrong = (shear / 2.0) * steel_factor
        assert cell.diagonal_force == statics, (cell.geometry, cell.diagonal_force, statics)
        # NON-VACUITY: at `h != b` the two candidate formulas MUST differ under
        # `uniform_panel`, or this cell could not have caught R1069.
        if cell.geometry == "uniform_panel":
            assert statics != wrong, (
                "the statics force and `V * steel_factor` agree at this geometry, so this "
                "cell cannot tell them apart and would have passed on R1069"
            )


def test_R1069_a_NEARLY_TRANSVERSE_diagonal_carries_NEARLY_ALL_the_shear() -> None:
    """The control that needs no algebra, and it is the one that settles the formula.

    As a diagonal becomes transverse its force must approach `V`, because it is carrying
    the shear almost directly. At `p = 1, d = 50` statics gives `F/V = 1.0002`; the ratio
    `L/p` gives `50.01`. **A ratio that grows without bound as a member becomes more
    transverse is not a force ratio** -- it is the steel-per-unit-length ratio, which is a
    different quantity with the same two symbols in it.
    """
    p, d = 1.0, 50.0
    length = math.hypot(p, d)
    # **STATED AS INEQUALITIES IN THE SYMBOLS, so there is no magnitude literal to be a
    # threshold.** `sqrt(1 + x^2) - 1 < x` for `x > 0`, with `x = p/d`: the statics ratio is
    # within `p/d` of ONE, i.e. a nearly transverse diagonal carries nearly all of `V`.
    assert length / d - 1.0 < p / d
    # And `L/p` exceeds `d/p` outright, because `L > d`. At this aspect ratio that is
    # `50.01` against `1.0002` -- a ratio that grows without bound as a member becomes
    # transverse, which is what disqualifies it as a force ratio.
    assert length / p > d / p


def test_R1069_the_CHORD_resolutions_match_FIRST_PRINCIPLES(tmp_path) -> None:
    """The chord half, checked from the coordinates and not from its own derivations.

    **THIS WAS A SCRATCHPAD SCRIPT AND IS NOW A CELL, and the reviewer's reason for
    requiring that is the right one:** landing the measurement one commit after the thing
    it would have caught is the wrong order. The chord half is the half that was already
    correct -- every coefficient in both docstrings is right -- and this is what says so
    reproducibly rather than in a message.

    It reads NO coefficient. It builds the chord COORDINATES, computes the centroid and
    both second moments by summation over them, applies `F_i = N/n + A_c My (z_i - zbar) /
    I_yy + A_c Mz (y_i - ybar) / I_zz`, and compares.
    """
    h, b = 8.0, 3.0
    n, vy, vz, t, my, mz = -1.0e6, 2.0e5, 3.0e5, 0.0, 1.9e8, 2.7e8

    def first_principles(positions: dict[str, tuple[float, float]]) -> dict[str, float]:
        count = len(positions)
        zbar = sum(z for _y, z in positions.values()) / count
        ybar = sum(y for y, _z in positions.values()) / count
        i_yy = sum((z - zbar) ** 2 for _y, z in positions.values())
        i_zz = sum((y - ybar) ** 2 for y, _z in positions.values())
        return {
            name: n / count + my * (z - zbar) / i_yy + mz * (y - ybar) / i_zz
            for name, (y, z) in positions.items()
        }

    box = first_principles(
        {
            "top_+b": (+b / 2.0, +h / 2.0),
            "top_-b": (-b / 2.0, +h / 2.0),
            "bot_+b": (+b / 2.0, -h / 2.0),
            "bot_-b": (-b / 2.0, -h / 2.0),
        }
    )
    got = box_resolution(n, vy, vz, t, my, mz, h, b).chords
    assert got.keys() == box.keys()
    for name in sorted(got):
        # EXACT for the box: `N/4` and the `+-My/(2h)`, `+-Mz/(2b)` pairs are exact in
        # binary.
        assert got[name] == box[name], (name, got[name], box[name])

    tri_positions = {"apex": (0.0, h), "bot_+b": (+b / 2.0, 0.0), "bot_-b": (-b / 2.0, 0.0)}
    tri = first_principles(tri_positions)
    got = triangle_resolution(n, vy, vz, t, my, mz, h, b).chords
    assert got.keys() == tri.keys()
    for name in sorted(got):
        assert got[name] == tri[name], (name, got[name], tri[name])

    # AND THE THREE SECTION PROPERTIES THE DOCSTRING CLAIMS, by summation over the same
    # coordinates -- so `(2/3) A_c h^2` is a measurement here and not a sentence.
    zbar = sum(z for _y, z in tri_positions.values()) / 3.0
    assert zbar == h / 3.0
    # not-a-tolerance: a round-off floor on an algebraic identity, NOT a threshold two
    # quantities are allowed to differ by. Measured: the sum is `42.66666666666667` and
    # `(2/3)h^2` is `42.666666666666664` -- one ulp apart, because `zbar = 8/3` is inexact
    # in binary. The defect it must catch is a wrong coefficient (`1/2`, `3/4`), which is
    # `10.7` or `5.3` away from this value -- thirteen orders of magnitude above the floor.
    i_yy = sum((z - zbar) ** 2 for _y, z in tri_positions.values())
    two_thirds = 2.0 / 3.0 * h * h
    assert i_yy == pytest.approx(two_thirds, abs=1e-12)  # not-a-tolerance: round-off floor
    assert sum((y - 0.0) ** 2 for y, _z in tri_positions.values()) == b * b / 2.0


def test_L3_the_JOINT_ALLOWANCE_scales_CHORD_AND_DIAGONAL_steel_both() -> None:
    """The allowance was on the chords alone; the source applies it to both.

    **AND THIS CELL EXISTS BECAUSE THE REPAIR WAS HELD BY NOTHING.** No cell asserts
    `steel_area_per_m` absolutely, so moving the allowance from one term to two changed a
    published number with the whole suite green -- the same shape as the revert arm that
    measured a prediction instead of a guard.

    The assertion is a PROPORTIONALITY, which is what distinguishes the two placements
    without pinning a magnitude: if the allowance multiplies chord AND diagonal steel then
    the total scales by it exactly, and if it multiplies the chords alone then the ratio is
    strictly smaller because the diagonal term does not move. `scripts/measure/f6b_truss_sizing.py`
    has `line_mass = (chord_steel + diagonal_steel) * RHO_STEEL * JOINT_ALLOWANCE`.
    """
    h, b = 8.0, 3.0
    rows = [("probe ROOT", (-1.0e6, 2.0e5, 3.0e5, 0.0, 1.9e8, 2.7e8))]
    plain = resolve_group(
        "platform",
        rows,
        TrussOptions(depths=(h,), widths=(b,), shapes=("box",), joint_allowance=1.0),
        MATERIAL,
    )
    allowed = resolve_group(
        "platform",
        rows,
        TrussOptions(depths=(h,), widths=(b,), shapes=("box",), joint_allowance=1.15),
        MATERIAL,
    )
    assert len(plain.cells) == len(allowed.cells) and plain.cells
    for a, b_ in zip(plain.cells, allowed.cells, strict=True):
        # Exact, because the allowance is the only factor that moved and it multiplies the
        # whole sum. `1.15` is a declared option, not a tolerance.
        assert b_.steel_area_per_m == a.steel_area_per_m * 1.15, (a.geometry, a, b_)
        # NON-VACUITY: the diagonal term is a real share of the total, so a chord-only
        # allowance would give a ratio strictly below 1.15 and this cell would fail.
        assert a.diagonal_area > 0.0, a


def test_R1069_the_DIAGONAL_is_sized_at_ITS_OWN_length_not_the_chords() -> None:
    """The second half of R1069, and it had no cell until this arm failed to redden.

    **I PREDICTED THAT ARM WOULD NOT FIRE AND IT DID NOT, WHICH MEANS IT WAS MEASURING THE
    PREDICTION.** Reverting the compression length from the diagonal's own length back to
    the chord buckling length left the whole suite green: nothing asserted the diagonal
    AREA absolutely, only its force. Same shape as the arm that caught me last commit, so
    the same answer (EK2): a cell, not a note.

    The discrimination is real and it is at `h != b` for the same reason as the force: at
    `h = 8, b = 3` under `uniform_panel` the diagonal is `hypot(3, 8) = 8.544 m` long while
    the chord's buckling length is `min(8, 3) = 3 m`, so a diagonal sized at the chord's
    length comes out far too small -- unconservative, and in a published area.
    """
    h, b = 8.0, 3.0
    shear = 8.33e5
    rows = [("probe ROOT", (0.0, 0.0, shear, 0.0, 0.0, 0.0))]
    truss = TrussOptions(depths=(h,), widths=(b,), shapes=("box",))
    group = resolve_group("platform", rows, truss, MATERIAL)
    vertical = faces("box", h, b)[0]

    for cell in group.cells:
        length, _steel = panel_and_diagonal(cell.geometry, h, b, vertical)
        force = (shear / 2.0) * length / vertical.dimension
        right, _branch = area_for_compression(-force, length, truss, MATERIAL)
        right = max(right, area_for_tension(force, MATERIAL))
        assert cell.diagonal_area == right, (cell.geometry, cell.diagonal_area, right)
        # NON-VACUITY: sizing at the CHORD's buckling length must give a different area,
        # or this cell cannot tell the two apart.
        buckling = chord_buckling_length(cell.geometry, h, b)
        if buckling != length:
            wrong, _b2 = area_for_compression(-force, buckling, truss, MATERIAL)
            wrong = max(wrong, area_for_tension(force, MATERIAL))
            assert right != wrong, (
                f"at {cell.geometry} the diagonal length {length} and the chord buckling "
                f"length {buckling} give the same area, so this cell cannot discriminate"
            )


@pytest.mark.parametrize(
    "truss_value, needle",
    [
        pytest.param(float("nan"), "must be finite", id="a_nan_allowance"),
        pytest.param(float("inf"), "must be finite", id="an_inf_allowance"),
    ],
)
def test_L8_a_NON_FINITE_declared_parameter_is_REFUSED(truss_value, needle: str) -> None:
    """`_checked` in the same module refuses NaN; these two scalars did not.

    The loud half is harmless -- a `nan` allowance prints as `nan` in every `steel/m`
    figure. **The quiet half is `lightest()`**, whose `min` over a grid containing `nan`
    returns a cell that is not the minimum, because every comparison with `nan` is False.
    """
    from floatfea.run.config import _parse_truss

    # BOTH scalars, because the code closes both and the cell covered one (L15).
    for key in ("joint_allowance", "d_over_t"):
        with pytest.raises(ConfigError) as caught:
            _parse_truss({**GOOD, key: truss_value}, "sections.truss")
        assert needle in str(caught.value), (key, str(caught.value))
    # AND the grid, which L18 closed in a different door.
    with pytest.raises(ConfigError) as caught:
        _parse_truss({**GOOD, "depths": [truss_value, 8.0]}, "sections.truss")
    assert "must be finite" in str(caught.value), str(caught.value)


def test_R1072_the_TRIANGLE_shear_allocation_does_NOT_close_and_the_BOX_does() -> None:
    """The idealisation's error, pinned as a measurement so it cannot drift unrecorded.

    **THIS CELL DOES NOT ASSERT THE ALLOCATION IS RIGHT. IT ASSERTS WHAT IT IS.** Each of
    the triangle's two inclined faces is allocated `|Vz|/2`, as though it were vertical. It
    is not: for its VERTICAL component to be `|Vz|/2`, an inclined face of length
    `Lf = hypot(h, b/2)` must carry `|Vz| Lf / (2h)` in plane. So the allocation is short
    by exactly `Lf/h`, and the torsion share is short by the same factor -- `q h` where
    Bredt gives `q Lf`.

    **THE BOX IS THE CONTROL AND IT CLOSES EXACTLY**, because its faces really are
    vertical, so `Lf = h` and the factor is one.

    The idealisation is inherited verbatim from `scripts/measure/f6b_truss_sizing.py` and
    is already published in `results/F6b/truss_sizing.md`; FI1 (`docs/milestones/F6b.md`)
    says shear goes to the VERTICAL faces and a triangle has none, so nothing declares it.
    **It is escalated rather than repaired** -- making it close in `floatfea/` alone would
    put two answers for one quantity in this repository. This cell is what stops the gap
    being rediscovered instead of ruled on.
    """
    for h, b in ((8.0, 3.0), (3.0, 8.0), (2.0, 8.0)):
        lf = math.hypot(h, b / 2.0)
        box = box_resolution(0.0, 0.0, 1.0, 0.0, 0.0, 0.0, h, b)
        tri = triangle_resolution(0.0, 0.0, 1.0, 0.0, 0.0, 0.0, h, b)
        # Both shapes allocate `|Vz|/2` to each of two faces, so both SUM to Vz = 1.
        assert box.face_shear["vertical"] * 2 == 1.0
        assert tri.face_shear["inclined"] * 2 == 1.0
        # THE TRIANGLE: in-plane equilibrium needs `Lf/h` times as much, and `Lf > h`
        # strictly whenever `b > 0` -- so the shortfall is never zero and never favourable.
        # (Three assertions here used to be arithmetic about Python rather than about
        # `floatfea` -- `math.hypot(h, 0.0) == h` and a restatement of `2*(Lf/(2h))` --
        # and they are gone (L14).)
        assert lf > h
        in_plane = 2.0 * (1.0 * lf / (2.0 * h))
        assert tri.face_shear["inclined"] * 2 < in_plane

        # **THE TORSION HALF, which the published claim asserts and no cell covered (L14):
        # the module's share is `q h` where Bredt gives `q Lf`, short by the same factor.**
        # Driven with `T = 1` and `Vy = Vz = 0`, so the torsion term is the whole shear.
        tri_t = triangle_resolution(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, h, b)
        # **`q` IS DERIVED HERE, NOT FROM `enclosed_area` (L21).** Taking it from the code
        # under test made this cell survive a mutation of that function's triangle branch.
        # Bredt: `q = T / (2 A_enc)`, and a triangle's enclosed area is `b h / 2`.
        q = 1.0 / (2.0 * (0.5 * b * h))
        # **EXACTLY, and no tolerance.** With `Vz = 0` the module's share is `abs(q*h)`
        # from the same expression computed here, so equality is exact -- and it is the
        # `h` rather than the `Lf` that this pins, which is the whole finding.
        assert tri_t.face_shear["inclined"] == q * h
        # (An assertion here that `q * lf > ...` reduced, given the line above, to `lf > h`
        # -- already asserted a few lines up. It was the L14 defect reintroduced by the L14
        # repair, and it is gone rather than restated (L21).)


def test_R1072_a_TRIANGLE_diagonal_force_is_pinned_ABSOLUTELY_at_h_not_b() -> None:
    """The cell the ruling requires either way: a triangle force, absolutely, at `h != b`.

    Every other force cell in this file uses `shapes=("box",)`. The chord channel has three
    equilibrium identities holding it; the shear channel had none for the triangle, which is
    how R1072's allocation went unexamined through two commits and one review.

    What is pinned is the force the SHIPPED allocation produces -- `|Vz|/2` on the inclined
    face, times `L/d` -- so that if the allocation is ever changed, this cell fails and the
    change cannot be silent. It is a statement about the code, not an endorsement of it;
    `test_R1072_the_TRIANGLE_shear_allocation_does_NOT_close_and_the_BOX_does` is the one
    that records the gap.
    """
    # **`h=8, b=3` AND NOT `h=3, b=8` (L13).** At `h=3, b=8` the inclined face's own
    # dimension is `h = 3` and `min(h, b)` is also `3`, so the two readings give the SAME
    # panel and the SAME diagonal -- `707106.7811865476` against `...75`. A cell there
    # cannot tell them apart, and mutating `panel * sqrt(2)` to `panel * 2.0` left both
    # R1072 cells green. At `h=8, b=3` the panels are `8` and `3` and they separate.
    h, b = 8.0, 3.0
    shear = 1.0e6
    rows = [("probe ROOT", (0.0, 0.0, shear, 0.0, 0.0, 0.0))]
    truss = TrussOptions(depths=(h,), widths=(b,), shapes=("triangle",))
    group = resolve_group("platform", rows, truss, MATERIAL)
    inclined = faces("triangle", h, b)[0]
    assert inclined.shear_key == "inclined" and inclined.dimension == h

    for cell in group.cells:
        # **THE LENGTH IS DERIVED HERE, NOT TAKEN FROM `panel_and_diagonal` (L13).** The
        # first version of this cell read `length` from that function and then asserted
        # the force against it -- so a mutation of the function moved BOTH sides and the
        # assertion was tautological. Mutating `panel * sqrt(2)` to `panel * 2.0` left it
        # green, which is what L13 measured; relocating the geometry did not fix it,
        # because the geometry was never the problem.
        panel = inclined.dimension if cell.geometry == "per_face_45" else min(h, b)
        length = (
            panel * math.sqrt(2.0)
            if cell.geometry == "per_face_45"
            else math.hypot(panel, inclined.dimension)
        )
        expected = (shear / 2.0) * length / inclined.dimension
        assert cell.diagonal_force == expected, (cell.geometry, cell.diagonal_force)
        # The inclined face governs here: `Vy = T = 0`, so the bottom face carries nothing.
        assert cell.diagonal_face == "inclined", cell.diagonal_face


def test_R1076_the_bullet_PUBLISHES_NO_AREA_FACTOR_in_either_shape_it_took(tmp_path) -> None:
    """The area-factor bullet states the mechanism and quantifies nothing.

    **THE ARM FOR R1076 DID NOT REDDEN UNTIL THIS CELL EXISTED.** Republishing a single
    bound -- `IS 1.89083 EVERYWHERE, A SINGLE BOUND` in place of the sentence that says it
    is not published -- left the whole suite green, which is R1074's finding again one
    bullet over: a figure REMOVED because it could not be true is as silently restorable as
    a figure nothing reads.

    The two needles are the two shapes the six retired versions actually took, so this is a
    check derived from the history rather than a guess at the next one: a markdown TABLE of
    area columns (versions 4 and 5) and an `N.NNNNx` MULTIPLIER (versions 1, 2, 3 and 6).
    What it cannot see is a third shape, and it says so rather than implying coverage.
    """
    from floatfea import cli

    path, out_dir = _fixture(tmp_path)
    assert cli.main(["run", str(path)]) == 0
    text = (out_dir / "truss_sizing.md").read_text(encoding="utf-8")

    # The positive half: the sentence a republication would have to displace.
    assert "THE FACTOR ON THE AREA IS NOT PUBLISHED HERE" in text
    assert "unconservative by an amount this tool does not bound" in text

    # The negative half, over the bullet's own span rather than the whole document: the
    # tables above legitimately carry both `|` rows and multipliers.
    start = text.index("THE FACTOR ON THE AREA IS NOT PUBLISHED HERE")
    bullet = text[start : text.index("FI1 DECLARES NOTHING HERE", start)]
    assert "|" not in bullet, bullet
    assert re.search("[0-9][.][0-9]+x", bullet) is None, bullet

    # **AND THE FORCE FACTOR CARRIES ITS CORRECTION AND ITS READING.** R1076's condition
    # asked for both and the first repair of it still said "EXACTLY" unqualified. The two
    # figures are DERIVED here from the resolver, so a change to the resolution moves the
    # assertion and not only the prose.
    assert "UNDER THE ALLOCATION-ALONE CORRECTION" in text
    h, b = 3.0, 8.0
    lf = math.hypot(h, b / 2.0)
    shipped = Face(2, h, "inclined")
    widened = Face(2, lf, "inclined")
    len0, _ = panel_and_diagonal("uniform_panel", h, b, shipped)
    len1, _ = panel_and_diagonal("uniform_panel", h, b, widened)
    # One unit of shipped face shear becomes `Lf/h` units under the corrected allocation.
    two_edit = ((lf / h) * len1 / widened.dimension) / (len0 / shipped.dimension)
    assert f"`{two_edit:.5f}`" in text, (two_edit, text)
    assert f"`{lf / h:.5f}`" in text, (lf / h, text)
    assert two_edit < lf / h, (two_edit, lf / h)


def _cell_at(shape: str, h: float, b: float, geometry: str, steel: float, face: str = ""):
    """A `TrussCell` carrying the four fields `_margin` reads, its steel, and its face.

    **R1087: THE FACE IS THE FIFTH FIELD AND IT IS A PARAMETER NOW.** This helper hard-set
    `diagonal_face="bottom"` while its docstring declared four fields, so `_governing_faces`
    read a fifth the docstring did not mention -- and `bottom` is a TRIANGLE's key, so
    every `box` cell it built was a box governed by a face a box does not have. That is
    R1078's conflation reproduced inside the fixture written to check R1078's repair.
    The default is empty, which is `_cell`'s own value when no face governs.
    """
    from floatfea.run.truss import TrussCell

    return TrussCell(
        shape=shape,
        depth=h,
        width=b,
        geometry=geometry,
        chord_area=0.0,
        chord_force=0.0,
        chord_station="ROOT",
        chord_branch="tension",
        chord_buckling_length=1.0,
        diagonal_area=0.0,
        diagonal_force=0.0,
        diagonal_face=face,
        steel_area_per_m=steel,
    )


def test_R1077_the_MARGIN_says_what_it_is_OVER_in_all_four_states() -> None:
    """`_margin`'s runner-up is named, and each branch has its own state.

    **THE DEFECT THIS HOLDS WAS FOUND AT THE VERDICT'S OWN NAMED CONFIGURATION AND WAS NOT
    WHAT THE CONFIGURATION PREDICTED.** A grid of one declared `(shape, h, b)` does not
    give one cell -- it gives one PER READING -- so `_margin` was comparing the two readings
    of the winner and the sentence called the loser "the next declared cell". The predicted
    `0.00%` never appears; the published figure was `0.39%` at a grid holding one entry.

    Four states because the function has four answers, and a decision rule with a branch no
    state reaches is a rule nothing holds in place.
    """
    from floatfea import cli

    class _Group:
        def __init__(self, cells):
            self.cells = cells

    # (1) NO cell resolved. The old `< 2` test answered "the only declared cell" here.
    assert "no cell resolved" in cli._margin(_Group([]))

    # (2) Exactly one cell.
    one = [_cell_at("box", 8.0, 3.0, "per_face_45", 1.0)]
    assert "the only cell that resolved" in cli._margin(_Group(one))

    # (3) Two READINGS of the same declared cell -- the state that produced the defect.
    # The expected percentage is DERIVED from the two steels this cell declares. Folding
    # it to a constant made it a bare `0.25` that the tolerance guard could not tell from
    # a threshold, and it was right: a number with no visible provenance in a comparison
    # is a threshold whatever the author meant.
    best_steel, next_steel = 1.0, 1.25
    same = [
        _cell_at("box", 8.0, 3.0, "per_face_45", best_steel),
        _cell_at("box", 8.0, 3.0, "uniform_panel", next_steel),
    ]
    got = cli._margin(_Group(same))
    assert "the OTHER READING (`uniform_panel`) of the same `box` cell" in got, got
    assert "next cell" not in got, got
    gap_pct = (next_steel - best_steel) / best_steel * 100.0
    assert f"{gap_pct:.2f}%" in got, got

    # (4) A genuinely different declared cell wins the runner-up slot.
    other = [
        _cell_at("box", 8.0, 3.0, "per_face_45", 1.0),
        _cell_at("triangle", 2.0, 11.0, "uniform_panel", 1.5),
        _cell_at("box", 8.0, 3.0, "uniform_panel", 4.0),
    ]
    got = cli._margin(_Group(other))
    assert "the next cell (`triangle`, `h = 2 m`, `b = 11 m`, `uniform_panel`)" in got, got
    assert "OTHER READING" not in got, got

    # (5) And the zero-steel guard still has its own message rather than a division.
    free = [
        _cell_at("box", 8.0, 3.0, "per_face_45", 0.0),
        _cell_at("box", 8.0, 3.0, "uniform_panel", 1.0),
    ]
    assert "needs no steel at all" in cli._margin(_Group(free))

    # (6) **A DUPLICATE IS NOT THE OTHER READING (R1082).** `same_hb` alone put
    # `per_face_45` ahead of "the OTHER READING (`per_face_45`)" -- the winner's own
    # reading named as its runner-up, at `0.00%`. Three states on one axis, not two.
    twice = [
        _cell_at("box", 3.0, 3.0, "per_face_45", 1.0),
        _cell_at("box", 3.0, 3.0, "per_face_45", 1.0),
        _cell_at("box", 3.0, 3.0, "uniform_panel", 2.0),
    ]
    got = cli._margin(_Group(twice))
    assert "an IDENTICAL cell (`box`, `h = 3 m`, `b = 3 m`, `per_face_45`)" in got, got
    assert "OTHER READING" not in got, got
    assert "declares " in got and "more than once" in got, got

    # L36, in passing: `_governing_faces` published "1 are governed by the horizontal
    # face". Both branches of the agreement, since a fix for one can break the other.
    class _Report:
        def __init__(self, cells):
            self.trusses = [_Group(cells)]

    # A BOX's faces are vertical and horizontal (R1078/R1087): `bottom` is a triangle's.
    one = _cell_at("box", 3.0, 3.0, "per_face_45", 1.0, face="vertical")
    two = _cell_at("box", 8.0, 3.0, "uniform_panel", 1.0, face="vertical")
    assert cli._governing_faces(_Report([one])) == "1 is governed by the vertical face"
    assert "2 are governed by the vertical face" in cli._governing_faces(_Report([one, two]))

    # **L46, pre-existing: a cell with NO governing face was published as being governed
    # by a face called `(none)`.** `_cell` leaves the field empty when every face carries
    # zero shear. Both agreements again.
    #
    # **R1086: "the invented face name is forbidden" was what this comment used to say,
    # and NOTHING forbids it -- nor can anything, because the shipped sentence QUOTES the
    # retired wording.** The outcome is held by the positive needle below, which is a
    # weaker guarantee than the comment claimed, and the comment now says so.
    import dataclasses

    blank = dataclasses.replace(one, diagonal_face="")
    got = cli._governing_faces(_Report([blank]))
    assert "(none)" not in got, got
    assert "1 has no governing face at all" in got, got
    got_two = cli._governing_faces(_Report([blank, dataclasses.replace(two, diagonal_face="")]))
    assert "2 have no governing face at all" in got_two, got_two
    # **AND THE MIXED REPORT, WHERE THE CAUSAL PHRASE WAS FALSE OF THE NAMED FACE
    # (R1085).** As a trailing comma phrase, "every face carrying zero shear" read as a
    # statement about the vertical-governed cell too. It is parenthesised into its own
    # clause now, and the whole string is pinned rather than two fragments of it.
    mixed = cli._governing_faces(_Report([one, blank]))
    assert mixed == (
        "1 is governed by the vertical face, 1 has no governing face at all"
        " (every face of that cell carrying zero shear)"
    ), mixed
    assert "zero shear)" in mixed and not mixed.endswith("zero shear"), mixed
    # **R1089: THE THIRD AGREEMENT PAIR, whose plural branch nothing reached.** R1085's
    # repair introduced `that cell` / `those cells`, and only the singular was asserted --
    # the same gap L36 was, one clause over. Two blanks reach the plural.
    both_blank = cli._governing_faces(_Report([blank, dataclasses.replace(two, diagonal_face="")]))
    assert "every face of those cells carrying zero shear" in both_blank, both_blank
    assert "that cell" not in both_blank, both_blank


@pytest.mark.parametrize(
    "key, grid, needle",
    [
        ("depths", [3.0, 3.0], "depths[1] repeats 3.0, already declared at index 0"),
        ("widths", [8.0, 2.0, 8.0], "widths[2] repeats 8.0, already declared at index 0"),
        ("shapes", ["box", "box"], "shapes[1] repeats 'box', already declared at index 0"),
    ],
)
def test_R1082_a_REPEATED_grid_entry_is_refused_on_every_axis(tmp_path, key, grid, needle) -> None:
    """A repeated depth, width or shape is refused at parse, as a repeated heading is.

    **THE CONFIGURATION WAS ADMISSIBLE AND IT PRODUCED A FALSE SENTENCE.** At
    `depths: [3.0, 3.0]` the artifact published a `per_face_45` winner as being ahead of
    "the OTHER READING (`per_face_45`)" by `0.00%`, while the real margin over the other
    reading at that cell was non-zero. `_parse_headings` in the same module already
    refuses a repeat and gives the reason -- nothing about the answer changes and
    everything about what the run claims to have swept does. This closes the other three
    axes of the same grid.
    """
    truss = dict(GOOD)
    truss[key] = grid
    path, out_dir = _fixture(tmp_path, truss=truss)
    with pytest.raises(ConfigError) as excinfo:
        load_config(path)
    assert needle in str(excinfo.value), str(excinfo.value)
    assert "R1082" in str(excinfo.value), str(excinfo.value)
    # Refused at parse, so nothing is written -- the artifact never existed to be wrong.
    assert not out_dir.exists() or not list(out_dir.glob("*"))


def test_R1080_the_bullet_does_NOT_bound_the_error_BY_THE_GOVERNING_FACE(tmp_path) -> None:
    """The reach of the inclined-face defect is stated structurally, not by the face count.

    **THE RETIRED SENTENCE WAS CIRCULAR AND THAT IS WHY IT IS GONE (R1080).** It told a
    reader the error "cannot reach `diag A` at all" wherever a box's vertical or a
    triangle's bottom face governs -- but the governing face is chosen by comparing face
    shears the defect understates, so the attribution printed in the tables is computed
    under the defect and cannot delimit it.

    The replacement is structural and therefore true at every configuration, which is the
    property the old one lacked: `steel/m` SUMS the faces' diagonal steel so it moves on
    every triangle cell with a non-zero inclined-face shear, whichever face governs, while
    `diag A` is a MAXIMUM so it moves only where the corrected inclined face overtakes the
    bottom one. Measured over a 36-point `(h, b)` grid at four load mixes: `steel/m` moved
    on 288 of 288 cells and `diag A` on 155 of them -- including one load mix where
    `diag A` moved on 0 of 72 while `steel/m` moved on all 72, which is precisely the case
    the retired sentence told a reader was safe.
    """
    from floatfea import cli

    path, out_dir = _fixture(tmp_path)
    assert cli.main(["run", str(path)]) == 0
    text = (out_dir / "truss_sizing.md").read_text(encoding="utf-8")

    # The circular claim is gone, in both of the forms it took.
    assert "cannot reach `diag A` at all" not in text, text
    assert "WHETHER IT REACHES A PUBLISHED NUMBER DEPENDS ON WHICH FACE GOVERNS" not in text

    # And the structural statement is present, with the mechanism that makes it general.
    assert "SUMS the faces' diagonal steel" in text, text
    assert "MAXIMUM over" in text, text
    # **AND THE QUANTIFIER, which an earlier version of this bullet got wrong.** It said
    # the sum rises on every cell with a non-zero inclined-face shear. It does not: below
    # the smallest declared tube the sizing returns the bracket floor for both demands.
    # **THE NEEDLE SPANS THE CLAUSE, NOT A FRAGMENT OF IT.** A first version asserted only
    # `SMALLEST DECLARED TUBE ALREADY COVERS`, which lives on the source line AFTER the one
    # carrying the quantifier -- so the arm that replaced the quantifier left it green. A
    # needle whose domain cannot contain the failure is not a needle.
    assert (
        "raises the sum WHEREVER THOSE FACES MUST CARRY IN PLANE MORE THAN THE SMALLEST"
        " DECLARED TUBE ALREADY COVERS" in text
    ), text
    assert "whose inclined-face shear is non-zero" not in text, text
    assert "a function of a DECLARED input" in text, text
    # L45: `LOW, never high` was false in its first half -- at a floor-pinned cell the
    # published figure is EXACT, not low. Three needles are asserted now -- the one-way
    # half, the correction it holds under, and the floor clause -- which is more than the
    # "only the one-way half" an earlier version of this comment claimed (R1090).
    # **NOTHING FORBIDS THE RETIRED WORDING AND NOTHING CAN (R1086, R1090).** An earlier
    # version of this comment said it was forbidden. There is no `not in` assertion for
    # it here and none is possible, because the shipped sentence QUOTES `LOW, never high`
    # in the course of correcting it -- the same reason the sibling note a hundred lines
    # above gives for the invented face name. The three positives below are the whole
    # guarantee: if the sentence regresses to the bare claim they go red, which is a
    # weaker thing than forbidding the words and is the true one.
    # **AND THE DIRECTION CLAIM NAMES WHICH CORRECTION IT HOLDS UNDER (R1088).** "no
    # triangle figure is ever HIGH" is false under the BRACED LENGTH ALONE, which is one
    # of the three corrections the same bullet enumerates -- so the unqualified sentence
    # was true of two of three and read as true of all three.
    assert (
        "no triangle figure in these tables is ever HIGH UNDER THE ALLOCATION CORRECTION"
        " APPLIED ALONE" in text
    ), text
    assert "Under the BRACED LENGTH ALONE a `diag A` can come out HIGH" in text, text
    # **AND THE `EXACT` CLAIM IS PINNED TO THE ALLOCATION ALONE (R1092).** An earlier
    # version extended it to the two-edit correction, where it is false: the bracket floor
    # pins the AREA and nothing pins the STEEL, because the second edit lengthens the
    # diagonals. Both the narrowing and the reason are asserted, so neither can drift back.
    assert (
        "UNDER THE ALLOCATION ALONE it is low where the defect surfaces and EXACT where"
        " the bracket floor absorbs the whole of it" in text
    ), text
    assert "DOES NOT EXTEND TO THE TWO-EDIT CORRECTION" in text, text
    assert "the floor pins the AREA and nothing pins the STEEL" in text, text
    # R1091: the allocation is two terms, and the bullet says it does not speak for a
    # correction that moves only one of them.
    assert "the allocation is itself TWO terms" in text, text
    assert "does not enumerate and does not speak for" in text, text
    # The face count survives as a description, explicitly disclaimed as a bound.
    assert "NOT as a" in text and "bound on the error" in text, text


def test_R1081_the_artifact_does_not_claim_the_winner_is_LOAD_INDEPENDENT(tmp_path) -> None:
    """The argmin is a property of this run's loads, and the artifact says so.

    **THE R1077 REPAIR REMOVED THE LITERALS AND THE QUALIFIER WITH THEM (R1081).** The
    sentence had read that the torsion does not decide the winner "on this deck", which
    was true and measured; stripped of its qualifier it became a universal claim that is
    false -- torsion moved as the single variable flips both the winning shape and the
    winning reading. The artifact now states the dependence rather than denying it, and
    attaches no figure, because any figure here is a fact about one deck emitted by a
    generator that runs for all of them.
    """
    from floatfea import cli

    path, out_dir = _fixture(tmp_path)
    assert cli.main(["run", str(path)]) == 0
    text = (out_dir / "truss_sizing.md").read_text(encoding="utf-8")

    assert "WHICH CELL WINS CAN DEPEND ON THE LOAD" in text, text
    assert "named the torsion as what decides" not in text, text
    assert "property of THIS run's loads" in text, text
    # **R1083: NONE OF THE THREE ASSERTIONS ABOVE IS L43's REPAIR, AND MY ARM FOR IT
    # REDDENED FOR THE WRONG REASON.** All three predate L43 and survive its reversion;
    # the arm's mutation happened to delete `property of THIS run's loads` as well, so
    # `1 failed` was a true observation about a mutation that was not L43's. L43 changed
    # two clauses and these are the two:
    assert "can flip both the winning SHAPE and the winning READING" in text, text
    assert "is not guaranteed to carry over to another deck or another heading" in text, text
    assert "carries over to neither" not in text, text


def test_R1082_a_NEAR_duplicate_is_ACCEPTED_because_the_comparison_is_EXACT(tmp_path) -> None:
    """`[3.0, 3.0000001]` are two declared depths and both are kept.

    **THIS IS EH4's WEAKENING DIRECTION ON THE REFUSAL THE SAME COMMIT ADDED**, and it is
    the half a new rule does not get checked on by default: the repeat refusal was added
    because a repeat produced a false sentence, so every arm of it points at refusing
    MORE. The question this asks is what the rule refuses that nobody asked it to.

    The comparison is exact float equality and it stays that way. Reaching for `isclose`
    here would put a comparison epsilon in `config.py` under another name -- a "near
    duplicate" threshold is a tolerance, which `CLAUDE.md` forbids outright, and it would
    refuse a grid a user is entitled to declare. Two depths a tenth of a micron apart are
    a strange thing to sweep and they are not this parser's business to forbid.
    """
    truss = dict(GOOD)
    truss["depths"] = [3.0, 3.0000001]
    path, _out_dir = _fixture(tmp_path, truss=truss)
    cfg = load_config(path)
    assert cfg.sections.truss.depths == (3.0, 3.0000001), cfg.sections.truss.depths
    # Both survive as distinct declared depths: the grid is two deep, not one.
    assert len(set(cfg.sections.truss.depths)) == 2

    # And the exact duplicate of one of them is still refused, so widening to accept the
    # near-duplicate did not cost the refusal -- both directions hold at once.
    truss["depths"] = [3.0, 3.0000001, 3.0]
    again = tmp_path / "again"
    again.mkdir()
    path2, _ = _fixture(again, truss=truss)
    with pytest.raises(ConfigError) as caught:
        load_config(path2)
    assert "repeats 3.0, already declared at index 0" in str(caught.value), str(caught.value)


def test_R1080_the_defect_does_NOT_move_steel_per_m_BELOW_the_bracket_FLOOR() -> None:
    """The exception to R1080's reach, as arithmetic rather than as a sentence.

    **MY OWN BULLET CLAIMED THE SUM RISES ON EVERY CELL WITH A NON-ZERO INCLINED-FACE
    SHEAR, AND THAT IS FALSE.** `area_for_compression` bisects inside
    `sections.truss.diameter_search` and the smallest declared tube already carries a small
    demand, so the shipped and the corrected allocations return the SAME floor area and the
    published `steel/m` is byte-identical. My first probe missed it because every load I
    chose was large; the boundary has to be solved, not sampled.

    The cell pins both sides of that boundary at one `(h, b)` with one variable moved -- the
    inclined-face allocation -- so the exception is a property of the resolution and not of
    a published sentence. It carries no threshold of its own: the two loads are far either
    side of a boundary this test never names, and the assertions are equality and
    inequality of published figures.
    """
    import math

    import floatfea.run.truss as truss_mod

    original = truss_mod.RESOLVERS["triangle"]

    def corrected(n, vy, vz, t, my, mz, h, b):
        cf = original(n, vy, vz, t, my, mz, h, b)
        lf = math.hypot(h, b / 2.0)
        shears = dict(cf.face_shear)
        shears["inclined"] = shears["inclined"] * (lf / h)
        return ChordForces(cf.chords, shears)

    def resolve(vz, fixed):
        truss_mod.RESOLVERS["triangle"] = corrected if fixed else original
        try:
            group = resolve_group(
                "probe",
                [("probe", (0.0, 3.0e6, vz, 0.0, 1.0e8, 0.0))],
                TrussOptions(depths=(3.0,), widths=(8.0,), shapes=("triangle",)),
                MATERIAL,
            )
            return {c.geometry: c for c in group.cells}
        finally:
            truss_mod.RESOLVERS["triangle"] = original

    # The one variable really did move, measured at the RESOLUTION rather than at the
    # reported `diagonal_force` -- which names the GOVERNING face, the bottom one here, and
    # is therefore identical under a correction to the inclined face. That identity is the
    # finding R1080 is about, so the cell must not rest on it.
    row = (0.0, 3.0e6, 1.0e3, 0.0, 1.0e8, 0.0)
    assert (
        corrected(*row, 3.0, 8.0).face_shear["inclined"]
        > original(*row, 3.0, 8.0).face_shear["inclined"]
    )

    # BELOW the floor: that larger inclined shear does NOT move the published figure.
    small_shipped, small_fixed = resolve(1.0e3, False), resolve(1.0e3, True)
    for geometry, shipped in small_shipped.items():
        fixed = small_fixed[geometry]
        assert fixed.steel_area_per_m == shipped.steel_area_per_m, (
            geometry,
            shipped.steel_area_per_m,
            fixed.steel_area_per_m,
        )

    # ABOVE it: the same one-variable change does move the published figure, and UP.
    big_shipped, big_fixed = resolve(1.0e6, False), resolve(1.0e6, True)
    for geometry, shipped in big_shipped.items():
        fixed = big_fixed[geometry]
        assert fixed.steel_area_per_m > shipped.steel_area_per_m, geometry

    # And the control: the box has no inclined face, so the same patch cannot reach it.
    box_a = resolve_group(
        "probe",
        [("probe", (0.0, 3.0e6, 1.0e6, 0.0, 1.0e8, 0.0))],
        TrussOptions(depths=(3.0,), widths=(8.0,), shapes=("box",)),
        MATERIAL,
    )
    truss_mod.RESOLVERS["triangle"] = corrected
    try:
        box_b = resolve_group(
            "probe",
            [("probe", (0.0, 3.0e6, 1.0e6, 0.0, 1.0e8, 0.0))],
            TrussOptions(depths=(3.0,), widths=(8.0,), shapes=("box",)),
            MATERIAL,
        )
    finally:
        truss_mod.RESOLVERS["triangle"] = original
    for a, b in zip(box_a.cells, box_b.cells, strict=True):
        assert a.steel_area_per_m == b.steel_area_per_m, (a.geometry, a.shape)
