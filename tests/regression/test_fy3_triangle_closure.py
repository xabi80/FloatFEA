"""FY3: the triangle's faces CLOSE against the applied load, and the box is untouched.

**WHAT THIS CLOSES (R1072).** An apex-up triangle has two inclined walls and a bottom wall,
and each resists shear IN ITS OWN PLANE. The module gave each inclined face the VERTICAL
PROJECTION of both its shear and its shear flow -- `|Vz|/2` and `q*h` -- so the faces did
not carry the applied load between them. Over the example's declared grid the recovered
fraction of `Vz` ran from `0.982872` down to `0.447214`, and of `Mx/T` from `0.988581` to
`0.631476`, while the box closed at `1.000000` at every aspect ratio.

The consequence was UNCONSERVATIVE and reached a published column: triangular `diag A` in
`truss_sizing.md` low by up to `2.3792x`. `docs/milestones/F6b.md` declares nothing about an
inclined face -- FI1 sends `Vz` to the VERTICAL faces and a triangle has none -- so this was
an unexamined carry-over from `scripts/measure/f6b_truss_sizing.py`, not a declared
idealisation.

**THE CLOSURE IS MEASURED FROM THE MODULE'S OWN WALL MAGNITUDES, WITH THEIR REAL LEVERS.**
That is the whole of SR-3 and it is why these cells can fail. The first version of this
measurement computed the recovered torque as `2 * A_enc * q`, which is Bredt's identity:
`1.000000` whatever the module does. A check that cannot fail is the R434 shape this
repository keeps a guard and a control file for. Here each wall's force is the module's own
`face_shear` value, resolved along that wall's unit direction, and the moment is taken about
a point with that wall's real lever -- so a wrong magnitude moves the answer.

**WHY A REGRESSION FILE AND NOT A UNIT ONE.** These are pure arithmetic and run in
milliseconds, but what they protect is a PUBLISHED deliverable's column, and
`tests/regression/` is what rung 6 runs over the published artifacts.
"""

from __future__ import annotations

import math
from pathlib import Path

import pytest

from floatfea.run.config import load_config
from floatfea.run.truss import (
    RESOLVERS,
    TrussOptions,
    enclosed_area,
    inclined_face_length,
    resolve_group,
)
from floatfea.tolerances import TRUSS_FACE_CLOSURE_RELATIVE, TRUSS_FACE_CLOSURE_RELATIVE_COUNTER

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"

# the example's own commented `truss:` block -- the grid `truss_sizing.md` is published over
DEPTHS = (3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
WIDTHS = (3.0, 4.0, 5.0, 6.0, 8.0)
GRID = tuple((h, b) for h in DEPTHS for b in WIDTHS)

# and two cells outside it, because a bound that holds only where it was fitted is not a
# bound: `(1.5, 11.0)` is the widest aspect ratio any verdict has probed, `Lf/h = 3.8`.
OFF_GRID = ((2.0, 8.0), (1.5, 11.0))


def _triangle_walls(
    h: float, b: float
) -> tuple[tuple[str, tuple[float, float], tuple[float, float]], ...]:
    """Each wall of an apex-up triangle: its key, a point on it, its unit direction.

    Bottom chords at `(-b/2, 0)` and `(+b/2, 0)`, apex at `(0, h)`, which is the geometry
    `triangle_resolution` documents and resolves its chord forces on.
    """
    lf = inclined_face_length(h, b)
    return (
        ("inclined", (b / 2.0, 0.0), (-b / 2.0 / lf, h / lf)),
        ("inclined", (0.0, h), (-b / 2.0 / lf, -h / lf)),
        ("bottom", (0.0, 0.0), (1.0, 0.0)),
    )


def _vertical_closure(shape: str, h: float, b: float, scale: float = 1.0) -> float:
    """The faces' own VERTICAL components, summed, against an applied `Vz` of 1."""
    forces = RESOLVERS[shape](0.0, 0.0, 1.0, 0.0, 0.0, 0.0, h, b)
    if shape == "box":
        return 2.0 * forces.face_shear["vertical"]
    lf = inclined_face_length(h, b)
    return 2.0 * forces.face_shear["inclined"] * scale * h / lf


def _torque_closure(shape: str, h: float, b: float, scale: float = 1.0) -> float:
    """The MOMENT of the module's own wall forces about the origin, against `T` of 1.

    For the box the walls are at `+-b/2` and `+-h/2` from the centroid and the levers are
    those; for the triangle the bottom wall passes through the origin and contributes
    nothing, so the two inclined walls must supply all of `T` on their own levers.
    """
    forces = RESOLVERS[shape](0.0, 0.0, 0.0, 1.0, 0.0, 0.0, h, b)
    if shape == "box":
        return (
            2.0 * forces.face_shear["vertical"] * 0.5 * b
            + 2.0 * forces.face_shear["horizontal"] * 0.5 * h
        )
    moment = 0.0
    for key, (rx, ry), (ex, ey) in _triangle_walls(h, b):
        magnitude = forces.face_shear[key] * (scale if key == "inclined" else 1.0)
        moment += rx * (magnitude * ey) - ry * (magnitude * ex)
    return moment


@pytest.mark.parametrize("shape", ["triangle", "box"])
@pytest.mark.parametrize(("h", "b"), GRID + OFF_GRID, ids=lambda v: f"{v:g}")
def test_FY3_the_faces_CLOSE_against_the_applied_shear_and_torque(
    shape: str, h: float, b: float
) -> None:
    """Both channels, both shapes, every declared cell and two beyond the grid.

    **THE BOX IS HERE AS THE CONTROL, not for coverage.** It closed exactly before FY3 and
    closes exactly after, at every aspect ratio -- which is what established that the error
    was in the triangle's treatment rather than in this file's reference geometry. A repair
    that broke the box would be caught by the same assertion that passes the triangle.
    """
    for label, got in (
        ("Vz", _vertical_closure(shape, h, b)),
        ("Mx/T", _torque_closure(shape, h, b)),
    ):
        assert abs(got - 1.0) <= TRUSS_FACE_CLOSURE_RELATIVE, (shape, h, b, label, got)


@pytest.mark.parametrize(("h", "b"), [(3.0, 8.0), (2.0, 8.0), (8.0, 3.0), (1.5, 11.0)])
def test_FY3_the_COUNTER_perturbation_is_DETECTED_by_the_closure(h: float, b: float) -> None:
    """The counter-case the closure assertion must catch, at four aspect ratios.

    `TRUSS_FACE_CLOSURE_RELATIVE_COUNTER` is the smallest relative perturbation of an inclined
    face's shear that closure must detect; `TRUSS_FACE_CLOSURE_RELATIVE` is the width it
    may ignore. Without this cell the assertion above could be satisfied by a closure that
    is insensitive rather than exact -- which is what it WAS before FY3, in the other
    direction.
    """
    perturbed = 1.0 + TRUSS_FACE_CLOSURE_RELATIVE_COUNTER
    for label, got in (
        ("Vz", _vertical_closure("triangle", h, b, scale=perturbed)),
        ("Mx/T", _torque_closure("triangle", h, b, scale=perturbed)),
    ):
        assert abs(got - 1.0) > TRUSS_FACE_CLOSURE_RELATIVE, (h, b, label, got)
    assert TRUSS_FACE_CLOSURE_RELATIVE_COUNTER > TRUSS_FACE_CLOSURE_RELATIVE


def test_FY3_the_PRE_REPAIR_allocation_does_NOT_close() -> None:
    """The measurement that made R1072 a finding, reproduced as an assertion.

    **THIS IS THE ROW THAT STOPS THE CELLS ABOVE PASSING VACUOUSLY.** They assert that the
    shipped allocation closes; this asserts that the one it replaced does NOT, at the two
    aspect ratios where the shortfall is largest. Written in terms of the vertical
    projection the old code used -- `|Vz|/2` per face and `q*h` along each wall -- rather
    than by calling anything, because the old code is gone and a cell that needs it back
    is a cell that cannot run.

    The figures are verdict 42's own, recomputed here: at `h=3, b=8` the recovered `Vz` is
    `0.600000` and at `h=2, b=8` it is `0.447214`, which is `h/Lf` in both cases.
    """
    for h, b in ((3.0, 8.0), (2.0, 8.0), (8.0, 3.0)):
        lf = inclined_face_length(h, b)
        # The OLD rule gave each inclined face the vertical projection `|Vz|/2`, so the
        # two recovered `2 * (|Vz|/2) * h/Lf` -- which is `h/Lf` of the applied load.
        # Expressed from the geometry rather than as a literal: `h/Lf` IS the shortfall,
        # and writing `0.600000` here would be a figure this cell could not regenerate.
        old_recovered = 2.0 * 0.5 * h / lf
        # **THE RESIDUAL AGAINST THE DECLARED COUNTER, not `1.0 - COUNTER`.** My first
        # form was the latter, and the tolerance guard refused it: the bound of that
        # comparison is the composed value, so the literal `1.0` is deciding it. This is
        # the same shape the counter cell above uses, which the guard accepts.
        assert abs(old_recovered - 1.0) > TRUSS_FACE_CLOSURE_RELATIVE_COUNTER, (h, b, old_recovered)
        # and the SHIPPED rule closes at the same geometry, which is the pair that makes
        # this cell a comparison rather than two separate claims
        assert abs(_vertical_closure("triangle", h, b) - 1.0) <= TRUSS_FACE_CLOSURE_RELATIVE


def test_FY3_the_triangle_diagonal_at_h2_b8_is_the_HAND_CALCULATION() -> None:
    """One absolute triangle cell at `h != b`, derived by hand in this docstring (FY3).

    **THE CONFIGURATION.** `h = 2.0` m, `b = 8.0` m, apex up, reading `per_face_45`, under
    the probe load verdict 42 used: `N = -1.0e6` N, `Vy = 0`, `Vz = 3.0e6` N, `T = 0`,
    `My = 1.9e8` N.m, `Mz = 0`. That load is chosen because `Vy = T = 0` is what makes the
    INCLINED face govern; on the deck's own governing rows the bottom face governs at all
    60 declared cells and the whole correction is invisible in `diag A`.

    **THE HAND CALCULATION, step by step.**

      1. `Lf = hypot(h, b/2) = hypot(2, 4) = sqrt(20) = 4.472135955` m, and
         `Lf/h = 2.2360679...` -- the factor the old rule dropped.
      2. The inclined face's in-plane shear, with `T = 0` so no shear-flow term:
         `S = |Vz|/2 * Lf/h = 1.5e6 * 2.2360679 = 3.3541020e6` N.
      3. At `per_face_45` the panel is the face's own dimension, so the diagonal runs at
         45 degrees over `Lf` and its length is `Lf * sqrt(2)`; the diagonal force is
         `S * length / dimension = S * sqrt(2) = 4.7434165e6` N. The dimension CANCELS at
         this reading, which is why the force factor is exactly `Lf/h` and why the braced
         length alone moves no force here -- the two halves of R1072 separate cleanly.
      4. The bottom face carries `|Vy| + |q*b| = 0`, so the inclined face governs, which
         `diagonal_face` must report.

    **WHAT IS ASSERTED.** The diagonal FORCE against that hand value, and the governing
    face. The AREA is not hand-derived here: it comes from `area_for_compression`'s
    bisection against the API clause and a `d/t` of 24, which is a numerical search this
    docstring cannot reproduce honestly -- so the area is pinned as a measured absolute
    with its own command in the step report, and what this cell pins by hand is the
    quantity the hand calculation actually determines.
    """
    material = load_config(EXAMPLE).sections.material
    rows = [("platform:hub1_arm ROOT", (-1.0e6, 0.0, 3.0e6, 0.0, 1.9e8, 0.0))]
    truss = TrussOptions(
        depths=(2.0,),
        widths=(8.0,),
        shapes=("triangle",),
        d_over_t=24.0,
        joint_allowance=1.15,
        diameter_search=(0.05, 6.0),
    )
    group = resolve_group("platform", rows, truss, material)
    cell = next(c for c in group.cells if c.geometry == "per_face_45")

    lf = math.hypot(2.0, 4.0)
    hand_shear = 1.5e6 * lf / 2.0
    hand_force = hand_shear * math.sqrt(2.0)

    assert cell.diagonal_face == "inclined", cell.diagonal_face
    # **COMPARED AGAINST THE DECLARED CLOSURE TOLERANCE, not against an `approx` literal.**
    # My first draft wrote `pytest.approx(hand_force, rel=1e-9)`, and
    # `tests/test_no_tolerance_literals.py` refuses that by name: an `approx` tolerance is
    # a tolerance, and `1e-9` here would be an undeclared one in the commit that declares
    # two. The hand value and the module's value differ only by the order the same three
    # factors are multiplied in, which is the same class of residual
    # `TRUSS_FACE_CLOSURE_RELATIVE` is set against.
    assert abs(cell.diagonal_force / hand_force - 1.0) <= TRUSS_FACE_CLOSURE_RELATIVE, (
        cell.diagonal_force,
        hand_force,
    )
    # and `Lf/h` is the factor the old rule dropped, from the geometry rather than typed
    assert abs(lf / 2.0 - math.sqrt(5.0)) <= TRUSS_FACE_CLOSURE_RELATIVE


def test_FY3_the_BOX_is_unchanged_at_the_cells_the_box_regressions_pin() -> None:
    """FY3's "box section must be unchanged", asserted against the box's own geometry.

    `tests/regression/test_ft25_truss_sizing.py` pins the box at `:497` and `:657` and both
    are `shapes=("box",)`; this is the cell that says FY3 did not move what they pin. It
    asserts the box's own face allocation and dimensions directly, because that is what FY3
    could have broken -- `box_resolution` and `faces("box", ...)` are not in FY3's diff, and
    this is the assertion that says so rather than a reading of the diff.

    **The box's faces are GENUINELY vertical and horizontal**, so no projection enters and
    its closure was exact before FY3 and is exact after -- which is why it was the control
    that established the triangle's error was the triangle's.
    """
    from floatfea.run.truss import faces

    for h, b in ((8.0, 3.0), (6.0, 5.0), (3.0, 8.0)):
        box = faces("box", h, b)
        assert [f.dimension for f in box] == [h, b], (h, b, box)
        assert [f.shear_key for f in box] == ["vertical", "horizontal"], box
        forces = RESOLVERS["box"](0.0, 7.0, 11.0, 13.0, 0.0, 0.0, h, b)
        q = 13.0 / (2.0 * enclosed_area("box", h, b))
        # EXACT equality: the right-hand side is the same expression the module evaluates,
        # in the same order, so there is nothing for a tolerance to absorb -- and an
        # `approx` here would hide the day the module stopped computing it that way.
        assert forces.face_shear["vertical"] == 11.0 / 2.0 + abs(q * h), (h, b)
        assert forces.face_shear["horizontal"] == 7.0 / 2.0 + abs(q * b), (h, b)


def test_FY3_the_F6b_GENERATOR_does_not_crash_AFTER_writing(tmp_path: Path) -> None:
    """A deliverable generator that writes the file and then exits 1 (FZ rule 5).

    **FOUND WHILE REGENERATING `results/F6b/truss_sizing.md` FOR FY3's SUPERSESSION.** The
    final log line was `args.out.relative_to(ROOT)`, which raises `ValueError` for any
    `--out` that is not under the repository root -- a relative path, or any path outside
    it. The write had already happened, so the artifact was on disk and the process exited
    **1**: a caller checking the exit code concludes the file was not produced, and a
    caller that does not gets a traceback beside a correct artifact.

    It is not a wrong number, so it does not block under FR1. It is one line, so FZ rule 1
    puts it in-cycle rather than in the ledger, and FZ rule 5 asks for this row.

    `scripts/measure/` is a published deliverable path under EZ0, which is why this sits in
    `tests/regression/` with the rest of FY3 rather than beside a unit test.
    """
    import subprocess
    import sys

    generator = ROOT / "scripts" / "measure" / "f6b_report.py"
    source = ROOT / "results" / "F6b" / "truss_sizing.json"
    assert generator.is_file() and source.is_file()

    # THE PATH SHAPE THAT CRASHED: outside the repository root entirely.
    outside = tmp_path / "truss_sizing.md"
    proc = subprocess.run(
        [sys.executable, str(generator), "--json", str(source), "--out", str(outside)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert outside.is_file(), proc.stdout + proc.stderr
    assert "Traceback" not in proc.stderr, proc.stderr

    # AND THE DELIVERABLE IT PRODUCES IS THE ONE COMMITTED -- which is the property the
    # crash was hiding: an exit code of 1 beside a correct file teaches a reader to ignore
    # the exit code.
    committed = (ROOT / "results" / "F6b" / "truss_sizing.md").read_text(encoding="utf-8")
    assert outside.read_text(encoding="utf-8") == committed

    # AND THE SUPERSESSION NOTE FY3 ASKS FOR IS IN IT, dated, naming the shape it covers
    # and the shape it does not.
    assert "## SUPERSEDED" in committed
    assert "2026-10-31" in committed and "FY3" in committed
    assert "TRIANGLE" in committed and "box rows are not" in committed


def _f6b_csv_rows() -> list[dict[str, str]]:
    """The CSV data rows, skipping the leading `#` banner.

    `csv.DictReader` does NOT skip comment lines -- it takes the first one as the
    header. That is precisely why R1106's mark is a per-row column and not only a
    banner: a script reading this file the obvious way never sees the comments at
    all, and before this repair it never saw the supersession either.
    """
    import csv

    text = (ROOT / "results" / "F6b" / "truss_sizing.csv").read_text(encoding="utf-8")
    body = [ln for ln in text.splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(body))


def test_R1106_the_SUPERSESSION_reaches_BOTH_MACHINE_READABLE_SIBLINGS() -> None:
    """FY3's mark reached `truss_sizing.md` and NEITHER of its two siblings.

    The finding, measured before the repair:

        grep -c -i "superseded|FY3|R1072"  .md -> 3   .csv -> 0   .json -> 0

    with **84 of 168** CSV data rows being triangle rows. The silently wrong
    result that makes it blocking under FR1: a reader or a script taking a
    triangle row from that CSV gets sizing from the allocation FY3 ruled
    unconservative, with nothing in the file saying so. The inclined-face shear
    is low by `Lf/h`, which is `1.0050` to `2.2361` over the swept grid.

    **The numbers are NOT recomputed and this cell does not ask them to be**
    (SR-4). Regeneration was proven byte-identical on every shared column before
    the mark was added: 168 rows both ways, one column added, none removed, zero
    cells moved, and the `.md` rebuilt from the new JSON is byte-identical to the
    committed one.
    """
    import json

    rows = _f6b_csv_rows()
    assert len(rows) == 168, len(rows)

    # (1) THE CSV, PER ROW -- the half a script sees.
    tri = [r for r in rows if r["section"] == "triangle"]
    box = [r for r in rows if r["section"] == "box"]
    assert len(tri) == 84 and len(box) == 84, (len(tri), len(box))
    assert all(
        r["superseded_FY3"] == "True" for r in tri
    ), "a triangle row carries no supersession flag -- R1106"
    # The box rows were the CONTROL and the repair does not touch them. Asserting
    # the False side too, because a flag that is True everywhere marks nothing.
    assert all(
        r["superseded_FY3"] == "False" for r in box
    ), "a box row is flagged superseded; the box was the control"

    # (2) THE CSV BANNER -- the half a human reading a spreadsheet sees.
    csv_text = (ROOT / "results" / "F6b" / "truss_sizing.csv").read_text(encoding="utf-8")
    banner = "\n".join(ln for ln in csv_text.splitlines() if ln.startswith("#"))
    assert "SUPERSEDED" in banner and "2026-10-31" in banner and "FY3" in banner
    assert "triangle" in banner and "box rows are NOT superseded" in banner

    # (3) THE JSON, as data rather than as prose.
    blob = json.loads((ROOT / "results" / "F6b" / "truss_sizing.json").read_text(encoding="utf-8"))
    mark = blob["superseded"]
    assert mark["ruling"] == "FY3" and mark["date"] == "2026-10-31"
    assert mark["recomputed"] is False
    assert mark["per_row_flag"] == "superseded_FY3"
    assert "triangle" in mark["applies_to"] and "box" in mark["not_applies_to"]
    answers = blob["answers"]
    assert len(answers) == 168, len(answers)
    assert all(
        a["superseded_FY3"] is (a["section"] == "triangle") for a in answers
    ), "a JSON answer disagrees with its own section about being superseded"


def test_SR10_the_SIZING_generator_also_does_not_crash_AFTER_writing(
    tmp_path: Path,
) -> None:
    """The sibling of the crash the cell above pins, in the OTHER F6b generator.

    `test_FY3_the_F6b_GENERATOR_does_not_crash_AFTER_writing` covers
    `f6b_report.py`. `f6b_truss_sizing.py` carried the same bare
    `relative_to(ROOT)` in its closing log lines, after BOTH deliverables are
    written -- so pointing it at a scratch directory produced two correct files
    and an exit code of 1.

    Found by doing exactly that: regenerating to a scratch path to prove R1106
    had not moved any number. The control reported `GEN rc=1` with both files
    byte-identical, which is the shape the cell above calls out -- an exit code
    of 1 beside a correct file teaches a reader to ignore the exit code.

    `member_forces_table.py` records that five `scripts/measure/` scripts still
    carry the bare form. This is one of the five, so that count is now four; the
    remaining four are named there rather than left silent.
    """
    import subprocess
    import sys

    generator = ROOT / "scripts" / "measure" / "f6b_truss_sizing.py"
    assert generator.is_file()

    out_csv = tmp_path / "truss_sizing.csv"
    out_json = tmp_path / "truss_sizing.json"
    proc = subprocess.run(
        [sys.executable, str(generator), "--out", str(out_csv), "--json", str(out_json)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Traceback" not in proc.stderr, proc.stderr
    assert out_csv.is_file() and out_json.is_file()

    # AND THE DELIVERABLES IT PRODUCES ARE THE ONES COMMITTED, which is what makes
    # the exit code the only thing that was ever wrong here.
    for produced, committed_name in (
        (out_csv, "truss_sizing.csv"),
        (out_json, "truss_sizing.json"),
    ):
        committed = (ROOT / "results" / "F6b" / committed_name).read_text(encoding="utf-8")
        assert produced.read_text(encoding="utf-8") == committed, committed_name
