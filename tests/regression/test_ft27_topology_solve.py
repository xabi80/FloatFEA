"""R868: every declared topology goes through a SOLVE, and the published U is pinned.

**WHAT THIS CLOSES.** The plan's R868 entry measured that every case in
`tests/unit/test_topology_from_config.py` stopped at `build_superstructure` or at
`load_config`, so the collection the assertions inspected could not contain a downstream
failure. That is why FL2(a) shipped with three declared topologies dying in a `KeyError`
three layers below the builder, and why R867 was found by a reviewer rather than by this
suite. **That figure has since moved, by this work's own hand** -- R867's cells reach
`joint_nodes_of`, which is the "at minimum" route the plan's own closing condition names,
and the plan records the move.

**THE NUMBERS HERE ARE MEASURED AT THIS COMMIT, THROUGH `cli.main`, AND COMPARED AS
STRINGS.** `report.md` publishes the governing utilisation at `.6g`, so the assertion is
on the published text and needs no epsilon and no tolerance entry. A figure compared
numerically here would have required one, and `CLAUDE.md` is explicit that a comparison
epsilon is a tolerance under another name.

**TWO STRUCTURES, DECLARED THREE WAYS -- NOT THREE.** Verdict 42's R868 caveat reads
"`U = 1.82047` for #1, #2 and #3 -- the same structure declared three ways". Measured, #3
is the four-member star with one arm written backwards and gives the star's own
`1.71167`; the braced star of #1 and #2 has five members and gives `1.82047`. The caveat's
substance is right and its grouping is not, and the grouping is what a test would have
encoded.

**EACH DECLARATION IS SOLVED ONCE, AND THAT IS DELIBERATE.** A full run of the shipped
example is about 65 s. Written as one run per assertion this file would have made eleven
of them; the module-scoped cache below makes six, one per distinct declaration, and the
pair assertions read the cached outputs. The whole of `tests/regression` is CI's job at
the pushed sha (FV1), and rung 6 runs it -- so a file that solves the same structure
twice is paying twice on every push for the rest of the project.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "examples" / "platform12_placeholder.yaml"

HUBS = ("hub1", "hub2", "hub3", "hub4")
STAR = [["centre", h] for h in HUBS]
BRACE = ["hub1", "hub2"]

# The declared topologies of `docs/milestones/R1.md`'s FT2.7 table that RUN, plus the
# generated star as the control. #5, #6 and #7 are refused by R869 and #8 at build, and
# all four refusals are asserted in `tests/unit/test_topology_from_config.py`.
#
# `None` means NO `topology` block at all, which is the generated star -- a different
# code path from declaring the same four members, which is why both are here.
DECLARATIONS: dict[str, list[list[str]] | None] = {
    "generated": None,
    "declared_star": STAR,
    "braced_arms_first": [*STAR, BRACE],
    "braced_brace_first": [BRACE, *STAR],
    "reversed_arm": [["hub1", "centre"], *STAR[1:]],
    "hub4_via_brace": [*STAR[:3], ["hub3", "hub4"]],
}

# measured at this commit, six runs through `cli.main`; see the module docstring
U_STAR = "1.71167"
U_BRACED = "1.82047"
U_HUB4_BRACE = "1.81076"


def _write_config(work: Path, members: list[list[str]] | None) -> tuple[Path, Path]:
    """The shipped example, with a `topology` block or deliberately without one."""
    data = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    data["floatsim"]["deck"] = str((EXAMPLE.parent / data["floatsim"]["deck"]).resolve())
    data["load_cases"]["npz"] = str((EXAMPLE.parent / data["load_cases"]["npz"]).resolve())
    if members is None:
        data.pop("topology", None)
    else:
        data["topology"] = {"platform": {"members": members}}
    out = work / "out"
    data["outputs"]["directory"] = str(out)
    data["outputs"]["truss_sizing"] = False
    data["outputs"]["required_section"] = False
    path = work / "config.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path, out


@pytest.fixture(scope="module")
def solved(tmp_path_factory: pytest.TempPathFactory) -> dict[str, Path]:
    """Every declaration in `DECLARATIONS`, run once, as `{name: output directory}`.

    The exit code is asserted HERE rather than in each cell, because a non-zero exit
    leaves a cell asserting on a report that does not exist and the failure then reads as
    a missing file rather than as a refused run.
    """
    from floatfea import cli

    out_of: dict[str, Path] = {}
    for name, members in DECLARATIONS.items():
        work = tmp_path_factory.mktemp(name)
        cfg, out = _write_config(work, members)
        assert cli.main(["run", str(cfg)]) == 0, name
        out_of[name] = out
    return out_of


def _governing(out: Path) -> str:
    """`report.md`'s governing line, whole, as published."""
    text = (out / "report.md").read_text(encoding="utf-8")
    line = [ln.strip() for ln in text.splitlines() if ln.startswith("**U = ")]
    assert len(line) == 1, line
    return line[0]


def _rows(out: Path, name: str) -> int:
    body = [
        ln
        for ln in (out / name).read_text(encoding="utf-8").splitlines()
        if ln and not ln.startswith("#")
    ]
    return max(0, len(body) - 1)


@pytest.mark.parametrize(
    ("name", "u", "member", "clause", "force_rows", "stations"),
    [
        ("generated", U_STAR, "hub4_arm", "3.3.2", 1248, 32),
        ("declared_star", U_STAR, "hub4_arm", "3.3.2", 1248, 32),
        ("braced_arms_first", U_BRACED, "hub4_arm", "3.3.2", 1326, 34),
        ("braced_brace_first", U_BRACED, "hub4_arm", "3.3.2", 1326, 34),
        ("reversed_arm", U_STAR, "hub4_arm", "3.3.2", 1248, 32),
        ("hub4_via_brace", U_HUB4_BRACE, "hub1_arm", "3.3.1", 1248, 32),
    ],
)
def test_R868_a_declared_topology_SOLVES_and_publishes_the_measured_U(
    solved: dict[str, Path],
    name: str,
    u: str,
    member: str,
    clause: str,
    force_rows: int,
    stations: int,
) -> None:
    """The PUBLISHED governing line, per declared topology.

    **THE GOVERNING MEMBER AND CLAUSE ARE ASSERTED, NOT ONLY THE NUMBER.**
    `hub4_via_brace` governs at `platform:hub1_arm` under clause 3.3.1 where every other
    row governs at `platform:hub4_arm` under 3.3.2 -- so a repair that moved the load path
    while leaving the magnitude close would pass a bare `U` check and fail this one.

    The row counts are asserted for the same reason: the braced star has one more member
    than the star and therefore two more checked stations, and a topology silently built
    with the wrong member count would otherwise show up only as a utilisation that is
    plausible.
    """
    out = solved[name]
    governing = _governing(out)
    assert f"**U = {u}**" in governing, governing
    assert f"`platform:{member}` ROOT" in governing, governing
    assert f"clause {clause} interaction" in governing, governing
    assert "`T_full = 12.5 s`" in governing, governing
    assert _rows(out, "member_forces.csv") == force_rows, _rows(out, "member_forces.csv")
    assert _rows(out, "utilisation.csv") == stations, _rows(out, "utilisation.csv")


def test_R868_the_DECLARATION_ORDER_cannot_change_the_published_U(
    solved: dict[str, Path],
) -> None:
    """R867's property through a SOLVE: the same structure, two orders, one answer.

    **THIS IS THE CELL R867 EXISTS FOR, and it is stronger than the naming assertions in
    `tests/unit/test_topology_from_config.py` because it compares PUBLISHED output.** The
    braced star declared arms-first and brace-first is one structure written two ways; the
    schema's duplicate-member check already keys on `frozenset((a, b))`, which is the
    schema stating that order does not identify a member. Before R867 the brace-first
    order did not reach a solve at all -- it raised a `KeyError` for a node name that the
    declaration order had prevented from existing.

    The whole governing LINE is compared, not the number, so the member, the station, the
    period, the basis and the clause all have to agree as well.
    """
    first, second = solved["braced_arms_first"], solved["braced_brace_first"]
    assert _governing(first) == _governing(second), (_governing(first), _governing(second))
    assert f"**U = {U_BRACED}**" in _governing(first), _governing(first)
    for name in ("member_forces.csv", "utilisation.csv"):
        assert _rows(first, name) == _rows(second, name), name


def test_R868_a_FOUR_member_star_is_NOT_the_braced_star(solved: dict[str, Path]) -> None:
    """The control that stops the previous cell passing for the wrong reason.

    **TWO STRUCTURES, DECLARED THREE WAYS -- NOT THREE.** If every declared topology
    happened to publish one number, the order-independence cell above would hold whatever
    the builder did with the declaration. It does not: the four-member star of
    `reversed_arm` gives `1.71167` and the five-member braced star gives `1.82047`, so the
    equality asserted above is a property of the declaration order and not an artefact of
    a flat response.

    This is also the correction to verdict 42's R868 caveat, which grouped the reversed
    arm with the two braced orders as "the same structure declared three ways". Measured,
    it belongs with the control.
    """
    braced, reversed_arm = solved["braced_arms_first"], solved["reversed_arm"]
    assert f"**U = {U_BRACED}**" in _governing(braced), _governing(braced)
    assert f"**U = {U_STAR}**" in _governing(reversed_arm), _governing(reversed_arm)
    assert _governing(braced) != _governing(reversed_arm)
    assert _rows(braced, "utilisation.csv") == 34
    assert _rows(reversed_arm, "utilisation.csv") == 32


def test_R868_the_GENERATED_star_and_the_DECLARED_star_publish_the_SAME_report(
    solved: dict[str, Path],
) -> None:
    """FL2(a)'s own gate, carried to the published artifact rather than to the member list.

    `tests/unit/test_topology_from_config.py` asserts the declared star reproduces the
    generated one member for member. This asserts it through a solve, on the governing
    line and on both deliverables' row counts -- so the default cannot drift away from
    the thing it replaced in any way a reader of `report.md` would see.
    """
    generated, declared = solved["generated"], solved["declared_star"]
    assert _governing(generated) == _governing(declared), (
        _governing(generated),
        _governing(declared),
    )
    assert f"**U = {U_STAR}**" in _governing(generated), _governing(generated)
    for name in ("member_forces.csv", "utilisation.csv"):
        assert _rows(generated, name) == _rows(declared, name), name
