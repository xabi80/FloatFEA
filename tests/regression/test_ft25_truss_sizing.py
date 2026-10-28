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
import shutil
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.run.config import ConfigError, Material, load_config
from floatfea.run.pipeline import run as run_pipeline
from floatfea.run.sizing import governing_rows, size_truss
from floatfea.run.truss import (
    GEOMETRIES,
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
    assert tri.face_shear["vertical"] > box.face_shear["vertical"]
    # And with NO torsion they coincide exactly, which is the deck's own case.
    box0 = box_resolution(N, VY, VZ, 0.0, MY, MZ, h, b)
    tri0 = triangle_resolution(N, VY, VZ, 0.0, MY, MZ, h, b)
    assert box0.face_shear["vertical"] == tri0.face_shear["vertical"] == abs(VZ) / 2.0


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
    _p45, d45, steel45 = panel_and_diagonal("per_face_45", h, b, vertical)
    _pu, du, steelu = panel_and_diagonal("uniform_panel", h, b, vertical)
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
