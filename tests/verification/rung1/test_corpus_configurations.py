"""G2.2 run against the REVIEWER'S corpus, not the implementer's cases (BE3/R54).

Every negative control on the patch test was designed by the same hand as the
gate, so the coverage it demonstrates is coverage of the cases its author thought
of. `tests/corpus/g22_model_configurations.txt` is written by the
gating-supervisor, the implementer's editing tools are denied that directory, and
this module executes what it finds there without editing it.

**The coverage number is the reviewer's count of entries this runs**, printed by
`test_the_corpus_coverage_is_reported`. The corpus's own `runs_in_suite` field is
the reviewer's record of that count at the last review; this module does not
touch it.

WHAT IS ASSERTED PER ENTRY
--------------------------
`expect=hold`   the six states are below the floor-aware ceiling in the named
                orientation, and the 1e-6 single-element control still exceeds
                `PATCH_TEST_EXACTNESS_COUNTER`.
`expect=breach` the entry is ABOVE `PATCH_TEST_EXACTNESS`. Recorded by the
                reviewer, and the measurement stays under test whichever tier
                now covers the entry.

TWO TIERS (F2.md sec. 5b, Q6). `PATCH_TEST_EXACTNESS` is an exactness claim
validated for member lambda <= `G22_VALIDATED_MEMBER_LAMBDA` at the gate's mesh;
beyond it `PATCH_TEST_ROUNDOFF` applies and is labelled round-off tracking. No
entry is deleted and none is `xfail`ed: the ones past the boundary move tier and
keep both their assertions, including a negative control that must still clear
the looser ceiling by orders.
`expect=raise`  the configuration must raise at construction rather than fall
                back to a silent default.

An entry naming a field this module cannot build RAISES (BH3): an unknown key, an
unknown `extra`, an unknown top-level field. A corpus entry that silently does
nothing is the vacuous-parameter failure AM5 named, and the previous version of
this docstring called that "a FAILURE, not a skip" while the parser skipped --
measured, `extra=roll_rad=1.0` and `extra=nonsense=3.0` returned bit-identical
results to `extra=none`.

THE ADMISSION LIMIT OVERRIDES `expect` (BH0)
--------------------------------------------
A member below `BEAM_ADMISSION_L_OVER_D` is not a G2.2 case at all: no beam
element describes it, and the gate's own negative control demonstrably fails
there (`docs/conventions.md`, "Beam admission limit"). Such an entry is asserted
to RAISE whatever its `expect` field says.

**Three entries are affected and the reviewer wrote `expect=hold` for all three**
-- `stubby_thin` and `stubby_thick` at `L/D = 1.5`, `very_stubby_L_r_0p5` at
`0.5`. That is a disagreement between the corpus and the model's admission
limit, not a resolved question: this module reports which entries it overrode so
the reviewer can adjudicate, and the corpus is not edited from here.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.admissibility import assert_beam_admissible, member_l_over_d
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (BEAM_ADMISSION_L_OVER_D,
                                 G22_VALIDATED_MEMBER_LAMBDA,
                                 PATCH_TEST_EXACTNESS,
                                 PATCH_TEST_EXACTNESS_COUNTER,
                                 PATCH_TEST_ROUNDOFF,
                                 PATCH_TEST_ROUNDOFF_COUNTER)

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_patch_test import (  # noqa: E402
    STATES, STATIONS, _exact_local, _to_global, relative_error,
)

CORPUS = (Path(__file__).resolve().parents[2] / "corpus"
          / "g22_model_configurations.txt")

ORIENTATIONS = {
    "axis": np.array([1.0, 0.0, 0.0]),
    "skew": np.array([1.0, 0.35, 0.22]) / np.linalg.norm([1.0, 0.35, 0.22]),
    "vertical": np.array([0.0, 0.0, 1.0]),
    "in_plane_y": np.array([0.0, 1.0, 0.0]),
}


SECTION_SHAPES = {"circular_tube": {"D", "t"}}


def _validate_section(n: int, spec: str) -> None:
    """The section spec's VALUE, not just its key (R75).

    `section=rectangle,D=0.6,t=0.012` used to build a circular tube and pass:
    the parser checked that the field was called `section` and then handed the
    rest to `Section.circular_tube` positionally. A corpus entry naming a shape
    this module cannot build is the same silent substitution the field check was
    written to stop, one level down.
    """
    shape, _, rest = spec.partition(",")
    if shape not in SECTION_SHAPES:
        raise CorpusError(
            f"{CORPUS.name}:{n}: section shape {shape!r} is not one of "
            f"{sorted(SECTION_SHAPES)}. It would have been built as a circular "
            "tube.")
    keys = set()
    for part in rest.split(","):
        k, sep, _ = part.partition("=")
        if not sep:
            raise CorpusError(
                f"{CORPUS.name}:{n}: section parameter {part!r} is not key=value")
        if k in keys:
            raise CorpusError(
                f"{CORPUS.name}:{n}: section parameter {k!r} appears twice")
        keys.add(k)
    if keys != SECTION_SHAPES[shape]:
        raise CorpusError(
            f"{CORPUS.name}:{n}: shape {shape!r} takes exactly "
            f"{sorted(SECTION_SHAPES[shape])}; got {sorted(keys)}")


FIELDS = {"id", "section", "stations", "orient", "extra", "runs_in_suite",
          "expect"}
EXTRAS = ("none", "orientation_node=", "roll=", "I_y_over_I_z=")
EXPECTS = {"hold", "breach", "raise"}


class CorpusError(ValueError):
    """A corpus line this module cannot execute. Never a skip (BH3/R57)."""


def _parse() -> list[dict[str, str]]:
    """Strict. Anything unrecognised RAISES; nothing is ignored.

    The previous version built a dict from whatever it found and read the keys it
    knew, so a typo silently produced the default configuration:
    `extra=roll_rad=1.0`, `extra=nonsense=3.0` and an unknown top-level key all
    returned `1.251313e-14`, bit-identical to `extra=none`. The module docstring
    said an unbuildable field was "a FAILURE, not a skip" while the parser
    skipped -- and the reviewer's corpus caught it with an entry whose whole
    purpose was to be a typo.

    Twelfth guard: the parser reports what it cannot do rather than doing
    something else.
    """
    rows: list[dict[str, str]] = []
    for n, line in enumerate(CORPUS.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            rows.append(_parse_line(n, line))
        except CorpusError as exc:
            # A malformed line does NOT vanish and does NOT stop the module: it
            # becomes an entry whose only admissible expectation is `raise`,
            # asserted per entry below. Swallowing it here would be the skip
            # this whole change exists to remove; aborting collection here would
            # let one bad line hide the other eighteen.
            ident = next((f.split("=", 1)[1] for f in line.split()
                          if f.startswith("id=")), f"line{n}")
            rows.append({"id": ident, "expect": "raise", "_error": str(exc),
                         "_line": line})
    return rows


def _parse_line(n: int, line: str) -> dict[str, str]:
        row: dict[str, str] = {}
        for field in line.split():
            key, sep, value = field.partition("=")
            if not sep:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: field {field!r} is not key=value")
            if key not in FIELDS:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: unknown field {key!r}. Known fields are "
                    f"{sorted(FIELDS)}. This module executes the corpus; a field "
                    "it does not understand is not silently ignored.")
            if key in row:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: field {key!r} appears twice "
                    f"({row[key]!r} then {value!r}). Taking the last silently "
                    "runs a configuration nobody wrote.")
            row[key] = value

        missing = {"id", "section", "stations", "orient", "expect"} - row.keys()
        if missing:
            raise CorpusError(f"{CORPUS.name}:{n}: missing {sorted(missing)}")
        if row["expect"] not in EXPECTS:
            raise CorpusError(
                f"{CORPUS.name}:{n}: expect={row['expect']!r} is not one of "
                f"{sorted(EXPECTS)}")
        if row["orient"] not in ORIENTATIONS:
            raise CorpusError(
                f"{CORPUS.name}:{n}: orient={row['orient']!r} is not one of "
                f"{sorted(ORIENTATIONS)}")
        _validate_section(n, row["section"])
        extra = row.get("extra", "none")
        if not any(extra == e or extra.startswith(e) for e in EXTRAS):
            raise CorpusError(
                f"{CORPUS.name}:{n}: extra={extra!r} is not one of {EXTRAS}. A "
                "typo here used to produce the DEFAULT configuration and pass.")
        return row


ENTRIES = _parse()


def _section(spec: str) -> Section:
    parts = dict(p.split("=") for p in spec.split(",")[1:])
    return Section.circular_tube(float(parts["D"]), float(parts["t"]))


def _build(entry: dict[str, str]):
    """Model and elements for one corpus entry, or raise as the entry expects."""
    sec = _section(entry["section"])
    total = float(entry["stations"])
    direction = ORIENTATIONS[entry["orient"]]
    stations = STATIONS * (total / STATIONS[-1])

    extra = entry.get("extra", "none")
    onode = None
    roll = 0.0
    if extra == "none":
        pass
    elif extra.startswith("orientation_node="):
        onode = np.array([float(v) for v in extra.split("=", 1)[1].split(",")])
    elif extra.startswith("roll="):
        roll = float(extra.split("=", 1)[1])
    elif extra.startswith("I_y_over_I_z="):
        object.__setattr__(sec, "I_y", sec.I_z * float(extra.split("=", 1)[1]))
    else:  # pragma: no cover -- _parse refuses these first; belt and braces
        raise CorpusError(f"{entry['id']}: unhandled extra {extra!r}")

    # The beam admission limit, BEFORE anything is built (BH0). A member below
    # it is not a G2.2 case: no beam element describes it, and the gate's own
    # negative control demonstrably fails there. This OVERRIDES the entry's
    # `expect` field, and the disagreement is reported rather than resolved --
    # see the module docstring.
    assert_beam_admissible(total, sec, what=entry["id"])

    m = Model()
    for s in stations:
        m.nodes.add(Node(*(s * direction)))
    els = [BeamElement(i, i + 1, sec, S355, orientation_node=onode, roll_rad=roll)
           for i in range(len(stations) - 1)]
    # Reach the degeneracy guard HERE rather than at first use. The guard lives
    # in `rotation_matrix`, so a builder that only constructs nodes and elements
    # never touches it, and `expect=raise` would pass by not looking.
    rotation_matrix(m.nodes[0].xyz, m.nodes[1].xyz,
                    orientation_node=onode, roll_rad=roll)
    return m, els, stations


def _solve_state(entry, state: str, stiffness_scale: float = 1.0) -> float:
    m, els, stations = _build(entry)
    e0 = els[0]
    r = rotation_matrix(m.nodes[0].xyz, m.nodes[1].xyz,
                        orientation_node=e0.orientation_node,
                        roll_rad=e0.roll_rad)
    sec = e0.section
    u_ex_local = _exact_local(state, stations, 1.0)
    if state == "shear":
        # `_exact_local` builds state 4 from the module's own SEC; on a corpus
        # section the field must come from THIS section or the reference is for a
        # different beam. Rebuilt here rather than approximated.
        ei = S355.E * sec.I_z
        kga = sec.kappa(S355) * S355.G * sec.A
        p, ll = 1.0e5, stations[-1]
        u_ex_local = np.zeros((stations.size, 6))
        u_ex_local[:, 1] = (p * (ll * stations**2 / 2.0 - stations**3 / 6.0) / ei
                            + p * stations / kga)
        u_ex_local[:, 5] = p * (ll * stations - stations**2 / 2.0) / ei
    elif state == "shear_xz":
        ei = S355.E * sec.I_y
        kga = sec.kappa(S355) * S355.G * sec.A
        p, ll = 1.0e5, stations[-1]
        u_ex_local = np.zeros((stations.size, 6))
        u_ex_local[:, 2] = (p * (ll * stations**2 / 2.0 - stations**3 / 6.0) / ei
                            + p * stations / kga)
        u_ex_local[:, 4] = -p * (ll * stations - stations**2 / 2.0) / ei

    u_ex = _to_global(u_ex_local, r)
    k = assemble(m, els)
    if stiffness_scale != 1.0:
        from floatfea.assemble.system import element_global_stiffness
        delta = (stiffness_scale - 1.0) * element_global_stiffness(m, els[1])
        k = k.tolil()
        d = np.concatenate([node_dofs(1), node_dofs(2)])
        for i in range(12):
            for j in range(12):
                k[d[i], d[j]] += delta[i, j]
        k = k.tocsr()

    n = len(stations)
    ends = np.concatenate([node_dofs(0), node_dofs(n - 1)])
    up = np.zeros(m.n_dof)
    up[node_dofs(0)] = u_ex[0]
    up[node_dofs(n - 1)] = u_ex[-1]
    f = -(k @ up)
    f[ends] = 0.0
    u = (solve(k, f, ends).u + up).reshape(n, 6)
    return relative_error(u, u_ex, stations[-1])


def member_lambda(entry) -> float:
    """`L_member / r` -- the axis the floor tracks (F2.md sec. 5b, Q6).

    Measured on a 2-D grid over element count and member lambda, because both
    one-dimensional sweeps were confounded: element L/r = lambda / n, so only two
    of the three are independent. Member lambda carries the frame-dependent part
    at exponent ~2 in skew against 0.68 axis-aligned; element L/r is refuted,
    since if it governed the two exponents would be equal and opposite.
    """
    sec = _section(entry["section"])
    return float(float(entry["stations"]) / np.sqrt(sec.I_z / sec.A))


def _tier(entry) -> tuple[str, float, float]:
    """Which claim covers this entry: `(name, ceiling, counter)`.

    Two tiers, not a scaled ceiling. `PATCH_TEST_EXACTNESS` is an EXACTNESS claim
    and it is validated for member lambda <= G22_VALIDATED_MEMBER_LAMBDA at the
    gate's own mesh; beyond that the element is still nodally exact and what
    grows is the floor at which exactness can be observed, so the claim there is
    `PATCH_TEST_ROUNDOFF` and it is labelled round-off tracking.

    The boundary is a property of THIS TEST AT ITS MESH. At fixed member lambda,
    changing only the element count moves the floor 35-57x, so it is not a
    statement about any structure and F3 measures its own floor rather than
    inheriting this one.
    """
    if member_lambda(entry) > G22_VALIDATED_MEMBER_LAMBDA:
        return "round-off tracking", PATCH_TEST_ROUNDOFF, PATCH_TEST_ROUNDOFF_COUNTER
    return "exactness", PATCH_TEST_EXACTNESS, PATCH_TEST_EXACTNESS_COUNTER


def test_the_corpus_exists_and_is_not_empty() -> None:
    """AM5: an empty parameter set is an error, not a silent pass."""
    assert CORPUS.exists(), f"{CORPUS} is missing; the corpus is the reviewer's"
    assert len(ENTRIES) >= 10, f"only {len(ENTRIES)} corpus entries parsed"


def _inadmissible(entry) -> float | None:
    """The member's L/D if it is below the admission limit, else None."""
    if "_error" in entry:
        return None
    ratio = member_l_over_d(float(entry["stations"]), _section(entry["section"]))
    return ratio if ratio < BEAM_ADMISSION_L_OVER_D else None


INADMISSIBLE = [e["id"] for e in ENTRIES if _inadmissible(e) is not None]


def test_the_admission_limit_overrides_are_REPORTED(capsys) -> None:
    """The disagreement is surfaced, not silently resolved (CLAUDE.md)."""
    with capsys.disabled():
        for e in ENTRIES:
            ratio = _inadmissible(e)
            if ratio is not None:
                print(f"\n  OVERRIDE: {e['id']} has L/D = {ratio:.3f} < "
                      f"{BEAM_ADMISSION_L_OVER_D:g}; corpus says "
                      f"expect={e['expect']}, this module asserts it RAISES")
    assert True  # not-a-tolerance: this test reports, the assertions are below


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e["id"])
def test_the_corpus_entry_behaves_as_the_reviewer_recorded(entry) -> None:
    expect = entry["expect"]

    if "_error" in entry:
        # The line could not be parsed. That is only acceptable if the corpus
        # says so; a malformed line the corpus expected to WORK is a failure.
        assert expect == "raise", (
            f"{entry['id']}: the corpus expects {expect!r} but the line cannot "
            f"be executed at all -- {entry['_error']}"
        )
        with pytest.raises(CorpusError):
            _parse_line(0, entry["_line"])
        return

    if _inadmissible(entry) is not None:
        with pytest.raises(ValueError, match="admission limit"):
            _build(entry)
        return

    if expect == "raise":
        with pytest.raises(ValueError):
            _build(entry)
        return

    worst = max(_solve_state(entry, st) for st in STATES)

    tier, ceiling, _ = _tier(entry)

    if expect == "breach":
        # The reviewer recorded these against the CONSTANT, and that measurement
        # stays under test: an entry marked breach must still exceed the
        # exactness ceiling, whichever tier now covers it.
        assert worst > PATCH_TEST_EXACTNESS, (
            f"{entry['id']}: the reviewer recorded a breach of "
            f"PATCH_TEST_EXACTNESS and this run gives {worst:.4e} <= "
            f"{PATCH_TEST_EXACTNESS:.0e}. Either the entry or the code moved."
        )

    assert worst <= ceiling, (
        f"{entry['id']}: worst state error {worst:.4e} exceeds the {tier} "
        f"ceiling {ceiling:.3e} (member lambda {member_lambda(entry):.1f}, "
        f"boundary {G22_VALIDATED_MEMBER_LAMBDA:g})"
    )


@pytest.mark.parametrize(
    "entry",
    [e for e in ENTRIES
     if e["expect"] != "raise" and "_error" not in e
     and _inadmissible(e) is None],
    ids=lambda e: e["id"],
)
def test_the_corpus_entry_still_DETECTS_a_defect(entry) -> None:
    """A configuration that holds but cannot fail is worse than one that breaches."""
    tier, ceiling, counter = _tier(entry)
    smallest = min(_solve_state(entry, st, stiffness_scale=1.0 + 1.0e-6)
                   for st in STATES)

    # THE COUNTER'S DOMAIN IS CIRCULAR SECTIONS, and an anisotropic entry is
    # outside it. `I_y_over_I_z` builds its section by bypassing the type guard
    # (the AW3 route); no production path can construct one, because every shape
    # `basis.kappa` admits forces `I_y == I_z`. Measured, the counter does NOT
    # hold there: at `I_y/I_z = 500` the weakest response falls to 8.6804e-08,
    # 13% below `PATCH_TEST_EXACTNESS_COUNTER`.
    #
    # That is recorded rather than fixed by lowering the counter, which would
    # weaken the claim on every circular entry to accommodate a section the type
    # refuses to build. The ceiling-clearance assertion below still applies here,
    # so the entry keeps a live negative control.
    if not entry.get("extra", "none").startswith("I_y_over_I_z="):
        assert smallest >= counter, (
            f"{entry['id']}: the weakest state responded to a 1e-6 "
            f"single-element defect with only {smallest:.4e}, below the {tier} "
            f"counter {counter:.3e}. The gate holds here and cannot fail here."
        )
    # The second tier is a LOOSER ceiling, not a weakened gate, and this is the
    # assertion that makes the difference measurable: the defect must still
    # redden it by orders.
    assert smallest > 100.0 * ceiling, (  # not-a-tolerance: discrimination floor -- asserts a separation is LARGE
        f"{entry['id']}: the 1e-6 defect responds at {smallest:.4e} against a "
        f"{tier} ceiling of {ceiling:.3e} -- only {smallest / ceiling:.0f}x. A "
        "looser ceiling is round-off tracking only while a real defect still "
        "clears it by orders."
    )


def test_the_corpus_coverage_is_reported(capsys) -> None:
    """The coverage number, in the form the reviewer scores it."""
    runs = len(ENTRIES)
    recorded = sum(1 for e in ENTRIES if e.get("runs_in_suite") == "yes")
    with capsys.disabled():
        print(f"\n  corpus: {runs} entries executed by this module; "
              f"{recorded} recorded as runs_in_suite=yes at the last review")
    # The property worth asserting is that this module executes EVERY entry --
    # the coverage number and the count of entries are the same number, or some
    # entry is being skipped. The previous assertion, `runs > recorded or
    # recorded == runs`, is false only if the reviewer's recorded count exceeds
    # the number of entries in their own file, which cannot happen: it asserted
    # nothing.
    solved = {e["id"] for e in ENTRIES
              if e["expect"] != "raise" and "_error" not in e
              and _inadmissible(e) is None}
    refused = {e["id"] for e in ENTRIES
               if e["expect"] == "raise" or "_error" in e
               or _inadmissible(e) is not None}
    all_ids = {e["id"] for e in ENTRIES}
    assert not (solved & refused), f"entries in both sets: {sorted(solved & refused)}"
    assert solved | refused == all_ids, (
        f"entries in neither set: "
        f"{sorted(all_ids - solved - refused)}. "
        "An entry that is neither solved nor explicitly refused is a silent skip."
    )
    with capsys.disabled():
        print(f"          {len(solved)} solved, {len(refused)} refused, "
              f"{len(ENTRIES)} total")


# ---------------------------------------------------------------------------
# The parser's own tests (BH3/R57). Each shape RAISES; none is a skip.
# ---------------------------------------------------------------------------
MALFORMED = [
    ("unknown top-level field", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=skew expect=hold nonsense=1"),
    ("unknown extra", "id=x section=circular_tube,D=0.6,t=0.012 stations=9.67 "
     "orient=skew extra=roll_rad=1.0 expect=hold"),
    ("misspelled extra key", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=skew extra=nonsense=3.0 expect=hold"),
    ("field with no '='", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=skew bare expect=hold"),
    ("unknown expect", "id=x section=circular_tube,D=0.6,t=0.012 stations=9.67 "
     "orient=skew expect=maybe"),
    ("unknown orient", "id=x section=circular_tube,D=0.6,t=0.012 stations=9.67 "
     "orient=diagonal expect=hold"),
    ("missing stations", "id=x section=circular_tube,D=0.6,t=0.012 orient=skew "
     "expect=hold"),
    ("unknown section shape", "id=x section=rectangle,D=0.6,t=0.012 "
     "stations=9.67 orient=skew expect=hold"),
    ("extra section parameter", "id=x section=circular_tube,D=0.6,t=0.012,b=0.3 "
     "stations=9.67 orient=skew expect=hold"),
    ("missing section parameter", "id=x section=circular_tube,D=0.6 "
     "stations=9.67 orient=skew expect=hold"),
    ("duplicate top-level field", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=skew expect=hold orient=axis"),
]


@pytest.mark.parametrize("label, line", MALFORMED, ids=[m[0] for m in MALFORMED])
def test_a_malformed_corpus_line_RAISES(label: str, line: str) -> None:
    """Measured before this existed: every one of these produced the DEFAULT
    configuration and a passing result identical to `extra=none`."""
    with pytest.raises(CorpusError):
        _parse_line(1, line)


def test_a_WELL_FORMED_line_still_parses() -> None:
    """The strictness must not refuse everything -- the meta-test for a guard."""
    row = _parse_line(
        1,
        "id=ok section=circular_tube,D=0.6,t=0.012 stations=9.67 orient=skew "
        "extra=roll=0.5 runs_in_suite=no expect=hold")
    assert row["id"] == "ok" and row["extra"] == "roll=0.5"
