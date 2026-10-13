"""`examples/platform12_placeholder.yaml` reproduces F4 and F6 EXACTLY (FL1(c)).

**WHAT THIS TEST IS FOR.** R1 generalises the tool: a configuration file now drives what
four milestones drove with hard-coded constants. The whole claim of that generalisation
is that it changed no physics, and this is where the claim is checked. If a figure here
moves, the generalisation broke something -- `docs/milestones/R1.md` section 5 says a
different number for the placeholder configuration is a defect in R1 and not a result
about the platform.

Golden-file discipline applies (`CLAUDE.md`): a figure that moves needs a written
explanation of WHY, and regenerating an expectation to match new output is the same error
as widening a tolerance.

**THE FULL RUN TAKES ABOUT 67 SECONDS, SO IT RUNS ONCE PER MODULE** and every assertion
reads the one result. It carries no `slow` marker: `--strict-markers` is on and no
regression test in this directory is marked, so inventing a marker would be new
apparatus for 67 s against a suite that already takes 1528 s.

**NO TOLERANCE IS USED ANYWHERE IN THIS FILE.** The force comparison is exact equality on
the decimal text the committed deliverable carries, read back as floats, and the
utilisation comparison is exact equality on the same 6-significant-figure text the
deliverable publishes. There is nothing to be approximate about: the configured path
calls the same functions on the same inputs, so the numbers are either bit-identical or
the generalisation is wrong.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import yaml

from floatfea.checks.api_wsd import check_member
from floatfea.post.forces_table import _lam_full_scale
from floatfea.run.config import ConfigError, load_config
from floatfea.run.pipeline import _k_l_over_r, _section_properties, exported_froude_lambda
from floatfea.run.pipeline import run as run_pipeline

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"
COMMITTED_FORCES = ROOT / "docs" / "F4_member_forces.csv"
COMMITTED_UTILISATION = ROOT / "docs" / "F6_utilisation.csv"


FORCE_COMPONENTS = ("N", "Vy", "Vz", "T", "My", "Mz")
KEY_FIELDS = ("body", "member", "station", "basis", "period_full_s")


def _rows(path: Path) -> list[dict[str, str]]:
    """A committed deliverable's data rows, with its `#` label block stripped."""
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line[:1] != "#"]
    return list(csv.DictReader(lines))


@pytest.fixture(scope="module")
def result() -> Any:
    """One run of the example configuration. About 67 s; shared by every assertion."""
    return run_pipeline(load_config(EXAMPLE))


# ---------------------------------------------------------------------------
# F4: the member-force envelope
# ---------------------------------------------------------------------------
def test_the_envelope_has_the_SAME_ROWS_as_the_committed_table(result: Any) -> None:
    """Same 1248 rows, keyed by member, station, basis and period -- no more, no fewer.

    Checked before the values, because a run that produced the right numbers on a
    different SET of rows would pass a value comparison that only visited the
    intersection.
    """
    committed = {tuple(r[f] for f in KEY_FIELDS) for r in _rows(COMMITTED_FORCES)}
    produced = {
        (
            row.body,
            row.member,
            row.station,
            row.basis,
            "" if row.period_full_s != row.period_full_s else f"{row.period_full_s:g}",
        )
        for row in result.rows
    }
    assert produced == committed, (
        f"the configured run produced {len(produced)} distinct rows against the committed "
        f"table's {len(committed)}. Only in the run: "
        f"{sorted(produced - committed)[:5]}. Only in the table: "
        f"{sorted(committed - produced)[:5]}."
    )


def test_every_force_component_is_EXACTLY_the_committed_value(result: Any) -> None:
    """All 7488 cells, exact equality, no tolerance.

    The committed table carries six significant figures of each component; the run is
    compared against exactly that text. A single differing cell fails and names itself,
    rather than a count being reported.
    """
    committed = {tuple(r[f] for f in KEY_FIELDS): r for r in _rows(COMMITTED_FORCES)}
    differing: list[str] = []
    checked = 0
    for row in result.rows:
        period = "" if row.period_full_s != row.period_full_s else f"{row.period_full_s:g}"
        want = committed[(row.body, row.member, row.station, row.basis, period)]
        for i, component in enumerate(FORCE_COMPONENTS):
            checked += 1
            # Both sides through the same 6-significant-figure decimal the deliverable
            # publishes, so the comparison is of published values and not of one
            # published value against a full-precision one.
            got = float(f"{float(row.values[i]):.6e}")
            if got != float(want[component]):
                differing.append(
                    f"{row.body}:{row.member} {row.station} {row.basis} T={period} "
                    f"{component}: committed {want[component]}, run {got:.6e}"
                )
    assert checked == 7488, f"expected 7488 component cells, compared {checked}"
    assert not differing, "component cells differ from the committed table:\n  " + "\n  ".join(
        differing[:20]
    )


def test_the_static_analytic_symmetry_holds_on_ALL_FOUR_platform_arms(result: Any) -> None:
    """`My = +1.916016e+08` N·m at ROOT on each arm, identical, with `Mz` and `N` zero.

    The cheapest fixture in the set and the most diagnostic: it is an ANALYTIC value, so
    a configured path that reproduces it has the geometry, the frame and the self-weight
    right independently of any golden file. Heading 0 static is pure vertical bending,
    which is why `Mz` and `N` are exactly zero rather than small.
    """
    arms = {
        row.member: row.values
        for row in result.rows
        if row.basis == "static" and row.station == "ROOT" and row.body == "platform"
    }
    assert len(arms) == 4, f"expected four platform arms at ROOT, got {sorted(arms)}"

    my = {label: float(f"{float(v[4]):.6e}") for label, v in arms.items()}
    assert set(my.values()) == {1.916016e08}, (
        f"the four platform arms must carry an identical static ROOT My of +1.916016e+08 "
        f"N·m; got {my}. They are geometrically identical and uniformly sized, so a split "
        f"here means the symmetry the model rests on is gone."
    )
    for label, values in sorted(arms.items()):
        assert float(values[5]) == 0.0, f"{label}: static Mz is {values[5]!r}, not zero"
        assert float(values[0]) == 0.0, f"{label}: static N is {values[0]!r}, not zero"


# ---------------------------------------------------------------------------
# F6: the utilisation screen
# ---------------------------------------------------------------------------
def test_the_screen_has_the_SAME_32_STATIONS_at_the_same_periods(result: Any) -> None:
    """32 rows, one per checked member-station, each at its own governing period."""
    committed = {
        (r["body"], r["member"], r["station"], r["period_full_s"])
        for r in _rows(COMMITTED_UTILISATION)
    }
    produced = {
        (r["body"], r["member"], r["station"], f"{float(r['period_full_s']):g}")
        for r in result.utilisations
    }
    assert len(committed) == 32, f"the committed screen has {len(committed)} rows, not 32"
    assert produced == committed, (
        f"Only in the run: {sorted(produced - committed)}. "
        f"Only in the committed screen: {sorted(committed - produced)}."
    )


def test_every_utilisation_matches_the_committed_screen_except_ONE_ROUNDING_BOUNDARY(
    result: Any,
) -> None:
    """31 of 32 exactly, and the 32nd differs because of an INTERMEDIATE ROUNDING.

    **THE CAUSE IS ISOLATED HERE RATHER THAN ALLOWED FOR.** `CLAUDE.md`'s default
    hypothesis on a disagreement is that the code is wrong, so this was chased before it
    was written down, and the answer is a property of the OLD two-stage path rather than
    of the configured one:

        scripts/measure/api_wsd_utilisation.py reads docs/F4_member_forces.csv

    -- that is, it computes the screen from the forces as PUBLISHED, at six significant
    figures. `floatfea run` computes it from the full-precision forces in memory, because
    nothing makes it write and re-read a file. On 31 rows the two agree to every published
    digit. On `hub3:buoy7_arm` TIP the rounded input gives
    `0.073857650219503301`, which sits `2.2e-10` ABOVE the `0.07385765` boundary and so
    publishes as `0.0738577`, while the exact input falls just below it and publishes as
    `0.0738576`.

    So the committed digit is decided by a `2.2e-10` perturbation of its own input. The
    configured run is the more accurate of the two; the committed value is the correct
    consequence of a documented two-stage process that rounds in the middle. Neither is a
    defect in this commit, and the station is at `U = 0.074` -- nowhere near unity -- so
    nothing anyone sizes depends on it.

    **NO TOLERANCE.** The assertion is not "close enough": it names the one row allowed to
    differ, and then PROVES the cause by feeding the committed rounded forces through the
    same checker and requiring the committed digit back exactly. A second differing row,
    or this row differing for any other reason, fails.
    """
    committed_rows = {
        (r["body"], r["member"], r["station"]): r for r in _rows(COMMITTED_UTILISATION)
    }
    assert len(committed_rows) == 32

    differing: dict[tuple[str, str, str], tuple[str, str]] = {}
    for row in result.utilisations:
        key = (row["body"], row["member"], row["station"])
        got = f"{float(row['utilisation']):.6g}"
        want = committed_rows[key]["utilisation_K2"]
        if got != want:
            differing[key] = (want, got)

    expected = ("hub3", "hub3:buoy7_arm", "TIP")
    assert set(differing) <= {expected}, (
        f"rows differ from the committed screen beyond the one known rounding boundary: "
        f"{ {k: v for k, v in differing.items() if k != expected} }. Every other station "
        f"must reproduce every published digit."
    )

    if not differing:
        # Not an error: it would mean the boundary row now agrees too, which is strictly
        # better. It must not pass silently, because the explanation above would have
        # stopped being true and the next reader needs to know that.
        pytest.fail(
            "the known rounding-boundary row now AGREES with the committed screen. That "
            "is an improvement, not a failure, but this test documents why it used to "
            "differ -- update the docstring and the expectation rather than leaving an "
            "explanation in place for something that no longer happens."
        )

    want, got = differing[expected]
    assert (want, got) == ("0.0738577", "0.0738576"), (
        f"the boundary row differs by more than the last published digit: committed "
        f"{want}, run {got}. The intermediate-rounding explanation only covers a one-unit "
        f"difference in the sixth significant figure."
    )

    # THE CELL THAT ISOLATES IT (BG0): one variable moved -- the input precision -- and
    # everything else held, including the section, the KL/r, the grade and Cm. Feeding the
    # committed table's own rounded forces through the same checker must return the
    # committed digit.
    body = next(b for b in result.built.bodies if b.name == expected[0])
    member = next(m for m in body.members if m.label == expected[1])
    area, w_bend, w_tors, d_outer, wall = _section_properties(member.section)
    committed_force_row = next(
        r
        for r in _rows(COMMITTED_FORCES)
        if (r["body"], r["member"], r["station"], r["basis"]) == (*expected, "total_instant")
    )
    forces = [float(committed_force_row[c]) for c in FORCE_COMPONENTS]
    from_rounded = check_member(
        axial_n=forces[0],
        shear_y_n=forces[1],
        shear_z_n=forces[2],
        torsion_nm=forces[3],
        moment_y_nm=forces[4],
        moment_z_nm=forces[5],
        area_m2=area,
        section_modulus_m3=w_bend,
        torsional_modulus_m3=w_tors,
        d_outer_m=d_outer,
        wall_m=wall,
        k_l_over_r=_k_l_over_r(body, result.config.code_check.k),
        fy=result.config.sections.material.fy,
        e=result.config.sections.material.e,
        cm=result.config.code_check.cm,
    ).utilisation
    assert f"{from_rounded:.6g}" == want, (
        f"the committed value {want} is NOT reproduced by feeding the committed rounded "
        f"forces through the same checker (got {from_rounded:.6g}). The "
        f"intermediate-rounding explanation for this row is therefore wrong, and the "
        f"difference has another cause that needs finding."
    )


def test_the_governing_utilisation_is_1_71167(result: Any) -> None:
    """FL1(c)'s headline figure, and the tie it conceals.

    **THE VALUE IS PINNED AND THE MEMBER IS NOT PINNED BY NAME ALONE, DELIBERATELY.**
    At the six significant figures the deliverable publishes, `platform:hub2_arm` ROOT
    and `platform:hub4_arm` ROOT BOTH read `1.71167`, so `max()` over the committed CSV
    returns whichever the reader happens to traverse first. An earlier revision of
    `docs/milestones/R1.md` recorded the governing member as `hub2_arm` for exactly that
    reason, and it was wrong: at full precision `hub4_arm` is `1.7116716105567911` and
    `hub2_arm` is `1.711671608463575`, so the governing member is `hub4_arm` and the two
    differ in the ninth significant figure.

    So this asserts three separate things, none of which depends on a tie-break: the
    published value, that the maximum is attained on the platform body at ROOT, and that
    `hub4_arm` is the member that attains it at full precision.
    """
    governing = result.governing()
    assert f"{float(governing['utilisation']):.6g}" == "1.71167", (
        f"the governing utilisation must publish as 1.71167; got "
        f"{float(governing['utilisation']):.6g} at {governing['member']}."
    )
    assert governing["body"] == "platform", governing
    assert governing["station"] == "ROOT", governing
    assert f"{float(governing['period_full_s']):g}" == "12.5", governing
    assert governing["governing_clause"] == "3.3.2 interaction", governing

    ranked = sorted(result.utilisations, key=lambda r: -float(r["utilisation"]))
    assert ranked[0]["member"] == "platform:hub4_arm", (
        f"at FULL precision the governing member is `platform:hub4_arm`; the run ranks "
        f"{ranked[0]['member']} first. If this moved, the tie between hub2 and hub4 has "
        f"shifted and the published 1.71167 may now belong to a different arm."
    )
    assert float(ranked[0]["utilisation"]) > float(ranked[1]["utilisation"]), (
        "hub4 and hub2 must remain distinguishable at full precision; they are now equal, "
        "so no member can be named as governing."
    )


def test_the_run_reports_a_wall_time_for_every_stage(result: Any) -> None:
    """FL1(d). A stage with no timing is a stage nobody can see the cost of."""
    for stage in ("build", "load", "solve", "code_check", "total"):
        assert stage in result.timings, f"no wall time recorded for `{stage}`"
        assert result.timings[stage] >= 0.0, (stage, result.timings[stage])
    parts = sum(result.timings[s] for s in ("build", "load", "solve", "code_check"))
    assert result.timings["total"] == parts, (
        f"`total` is {result.timings['total']!r} and its parts sum to {parts!r}; the "
        f"reported total must be the sum of the stages, not a separate measurement."
    )


def test_the_mass_residual_is_reported_PER_BODY_and_every_body_is_admissible(
    result: Any,
) -> None:
    """Per body, never summed (`CLAUDE.md` forbids averaging a per-case diagnostic).

    The residual is `deck - member - remainder`, formed from its own terms (G4.1). It is
    asserted to be exactly representable rather than merely small: the split is defined
    so that the three account for each other, so a nonzero residual is a real
    inconsistency and not round-off to be absorbed.
    """
    assert len(result.mass) == 5, [m.body for m in result.mass]
    for entry in result.mass:
        assert entry.psd_admissible, (
            f"{entry.body}: the remainder inertia is not PSD at f = {entry.fraction:g}. "
            f"DY0(d) is what admissibility means here and a non-PSD remainder is not a "
            f"body."
        )
        assert entry.deck_mass > 0.0, entry
        # EXACTLY ZERO, AND NOT A SMALL NUMBER. The first version of this bounded the
        # residual by `deck_mass * 2**-45`, which is a "small number" guard -- a
        # tolerance under another name, with a local literal and no entry in
        # `floatfea/tolerances.py`. Measured, the residual is `0.0` on all five bodies
        # at this configuration, because `member_mass = f * deck_mass` and
        # `remainder_mass = (1 - f) * deck_mass` are two halves of one number. There is
        # nothing to absorb, so nothing is allowed for.
        assert entry.residual == 0.0, (
            f"{entry.body}: residual {entry.residual!r} kg against a deck mass of "
            f"{entry.deck_mass!r} kg. The member and remainder masses are two halves of "
            f"the deck total and must account for it exactly; a nonzero residual is a "
            f"real inconsistency, not round-off."
        )


# ---------------------------------------------------------------------------
# FN0: the Froude scale has ONE source, and a mismatch refuses
# ---------------------------------------------------------------------------
#
# R805 is why these exist. `floatsim.froude_lambda` reached `build_superstructure` and
# NOT `_lam_full_scale`, which carried `FROUDE_LAMBDA = 50.0` at module scope. A
# configuration declaring 25.0 built the deck at scale 25 and scaled the joint reactions
# by 50 -- 8x on force, 16x on the locked moment -- while `provenance()` printed 25.0.
#
# **NOTHING WAS RED, AND THE GOLDEN ABOVE COULD NOT SEE IT**: the declared range is
# [1, 1000] and the example sits on the single point in three decades where the constant
# and the configuration agree. A test that only exercises the shipped configuration
# cannot find a constant that is right there and wrong everywhere else.


def test_FN0_the_exported_scale_is_READ_and_not_assumed() -> None:
    """The committed npz's scale is a RECORDED fact, not a default anyone chose.

    `scripts/export_f4_dynamic_inputs.py` has always written `run.lambda` into the
    provenance sidecar, so the one dynamic-inputs file this repository ships states its
    own scale. That is what makes refusing a mismatch possible without assuming anything.
    """
    npz = ROOT / "data" / "f4" / "dynamic_inputs.npz"
    exported, where = exported_froude_lambda(npz)
    # not-a-tolerance: the Froude scale the committed npz was EXPORTED at, read
    # from its provenance sidecar. It is an input recorded by the generator, and
    # the comparison is exact equality against that record -- nothing is being
    # allowed to differ by it.
    assert exported == 50.0, (  # not-a-tolerance: the scale the npz was EXPORTED at
        exported,
        where,
    )
    assert "provenance" in where, (
        f"the scale must be reported as coming from the sidecar so a reader can check it; "
        f"got {where!r}"
    )


def test_FN0_a_DECLARED_scale_that_differs_from_the_export_REFUSES(tmp_path) -> None:
    """FN0's first counter-case: lambda = 25 against a lambda = 50 npz must refuse.

    And the message must carry BOTH numbers and the consequence, because the whole defect
    was that the two scales never met: a refusal naming only one of them would leave the
    reader to work out which side to change.
    """
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    data["outputs"]["directory"] = str(tmp_path / "out")
    data["floatsim"]["froude_lambda"] = 25.0
    path = tmp_path / "lambda25.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")

    with pytest.raises(ConfigError) as caught:
        run_pipeline(load_config(path))
    message = str(caught.value)
    assert "scale mismatch" in message, message
    assert (
        "25.0" in message and "50.0" in message
    ), f"the refusal must name BOTH scales; got: {message}"
    assert "8" in message and "16" in message, (
        f"the refusal must state the consequence -- lambda^3 on force, lambda^4 on the "
        f"locked moment -- so the reader sees what the mismatch would have cost: {message}"
    )


def test_FN0_an_export_recording_NO_scale_REFUSES(tmp_path) -> None:
    """A file whose scale nobody recorded is refused, not guessed.

    Assuming 50 here would be R805 wearing a different coat: the defect was never the
    number, it was that a scale nobody declared got used as though it had been.
    """
    npz = tmp_path / "no_scale.npz"
    np.savez(npz, periods_full_s=np.array([12.5]))
    exported, where = exported_froude_lambda(npz)
    assert exported is None, (exported, where)
    assert "records the export scale" in where or "is absent" in where, where


def test_FN0_the_npz_key_is_PREFERRED_over_the_sidecar(tmp_path) -> None:
    """When both record a scale, the one travelling with the arrays wins.

    A sidecar can be separated from its npz by a copy; the key cannot. They are given
    DIFFERENT values here on purpose -- a test where both agree cannot tell which was
    read.
    """
    npz = tmp_path / "both.npz"
    np.savez(npz, periods_full_s=np.array([12.5]), froude_lambda=np.array(25.0))
    (tmp_path / "both.provenance.json").write_text(
        json.dumps({"run": {"lambda": 50.0}}), encoding="utf-8"
    )
    exported, where = exported_froude_lambda(npz)
    assert (
        # not-a-tolerance: the scale written into the synthetic npz two lines
        # above. The test asserts the reader returned the value it was GIVEN.
        exported
        == 25.0
    ), f"the npz's own key must win over the sidecar; got {exported!r} from {where!r}"
    assert where == "the npz", where


def test_FN0_the_scale_reaches_the_FROUDE_CONVERSION_as_cubed_and_fourth() -> None:
    """FN0's second counter-case: forces go as lambda^3, the locked moment as lambda^4.

    Measured against the declared composite rather than asserted from the exponents:
    `joint_multiplier_yaw_locked` is `((0, 3, "force"), (3, 4, "moment"))`, so rows 0-2
    carry the force factor and row 3 the locked moment's. Writing one factor for all four
    rows would be wrong by one power of lambda on the fourth, which is why the composite
    is declared rather than computed here.
    """
    block = np.ones(4, dtype=np.float64)
    at50 = _lam_full_scale(block, 50.0)
    at25 = _lam_full_scale(block, 25.0)

    ratio = at50 / at25
    assert list(ratio[:3]) == [8.0, 8.0, 8.0], (
        f"force rows must go as lambda^3, so halving lambda is a factor of 8; got "
        f"{list(ratio[:3])}"
    )
    # not-a-tolerance: `(50/25)**4`, the exact exponent the yaw-locked composite
    # declares for the locked moment. An integer power of two, computed from the
    # declared composite rather than chosen, and exact in binary floating point.
    assert ratio[3] == 16.0, (  # not-a-tolerance: (50/25)**4, the declared exponent
        f"the locked moment row must go as lambda^4, so halving lambda is a factor of 16; "
        f"got {ratio[3]}"
    )
    # The absolute values too, so this cannot pass on a pair of wrong numbers whose ratio
    # happens to be right.
    assert list(at50) == [125000.0, 125000.0, 125000.0, 6250000.0], list(at50)
    assert list(at25) == [15625.0, 15625.0, 15625.0, 390625.0], list(at25)


def test_FN0_there_is_NO_module_constant_on_the_run_path() -> None:
    """The repair, asserted rather than described.

    `_lam_full_scale` must take the scale as a required argument and
    `floatfea.post.forces_table` must carry no module-level scale for it to fall back on.
    A default would be the same constant wearing a different hat, so its absence is
    checked too.
    """
    import inspect

    from floatfea.post import forces_table

    assert not hasattr(forces_table, "FROUDE_LAMBDA"), (
        "floatfea.post.forces_table must carry no module-level FROUDE_LAMBDA; a "
        "configured scale was silently overridden by exactly such a constant (R805)."
    )
    signature = inspect.signature(forces_table._lam_full_scale)
    assert "froude_lambda" in signature.parameters, signature
    assert signature.parameters["froude_lambda"].default is inspect.Parameter.empty, (
        "the scale must be REQUIRED. A default is a module constant with extra steps, and "
        "every caller would then be free not to state its scale."
    )
    assert "froude_lambda" in inspect.signature(forces_table.compute_rows).parameters
