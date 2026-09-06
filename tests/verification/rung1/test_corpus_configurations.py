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
EVERY entry that builds  the six states' INTERIOR OUT-OF-BALANCE is below
                `PATCH_TEST_EXACTNESS`, and the 1e-6 single-element control
                still exceeds `PATCH_TEST_EXACTNESS_COUNTER`.
`expect=raise`  the configuration must raise at construction rather than fall
                back to a silent default.

ONE TIER, AND THE QUANTITY CHANGED (F2.md sec. 5b, Q6). The gate asserts how far
the EXACT constant-strain field is from satisfying `K u = 0` on the interior --
no solve in it. The solved nodal field error is the FORWARD error of a linear
solve and is now REPORTED per entry and asserted nowhere; `PATCH_TEST_ROUNDOFF`,
its counter and `G22_VALIDATED_MEMBER_LAMBDA` are gone with it. This is a
STRENGTHENING of the corpus: the eleven entries the second tier relieved and the
entries the reviewer marked `breach` are now all held to the tightest ceiling in
`tolerances.py`.

`expect=breach` IS THE REVIEWER'S RECORD AGAINST A RETIRED QUANTITY, so this
module can no longer assert it: the ceiling it was recorded against no longer
exists as a constant, and inventing one to keep the assertion alive would be a
tolerance in disguise. Those entries are REPORTED with both quantities by
`test_the_recorded_breaches_are_REPORTED_for_re_recording`, for the reviewer to
re-record. They are not exempted from anything -- the single-tier gate and the
counter apply to them like every other entry.

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
there (`docs/milestones/F2.md sec. 5b, Q5`). Such an entry is asserted
to RAISE whatever its `expect` field says.

**Three entries are affected and the reviewer wrote `expect=hold` for all three**
-- `stubby_thin` and `stubby_thick` at `L/D = 1.5`, `very_stubby_L_r_0p5` at
`0.5`. That is a disagreement between the corpus and the model's admission
limit, not a resolved question: this module reports which entries it overrode so
the reviewer can adjudicate, and the corpus is not edited from here.
"""
from __future__ import annotations

from pathlib import Path

import math

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.admissibility import (assert_beam_admissible,
                                          member_l_over_d)
from floatfea.model.admissibility import member_lambda as _member_lambda
from floatfea.model.material import S355, Section
from floatfea.testing import assert_close
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (BEAM_ADMISSION_L_OVER_D,
                                 PATCH_TEST_EXACTNESS,
                                 PATCH_TEST_EXACTNESS_COUNTER,
                                 ROUNDOFF_IDENTITY)

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_patch_test import (  # noqa: E402
    STATES, STATIONS, _exact_local, _to_global, interior_out_of_balance,
    relative_error,
)

CORPUS = (Path(__file__).resolve().parents[2] / "corpus"
          / "g22_model_configurations.txt")

# Four NAMED directions, kept because the corpus already uses them and a name is
# easier to read than three numbers. They are shorthand, not the vocabulary: the
# reviewer may write any direction (see `_direction`).
ORIENTATIONS = {
    "axis": np.array([1.0, 0.0, 0.0]),
    "skew": np.array([1.0, 0.35, 0.22]) / np.linalg.norm([1.0, 0.35, 0.22]),
    "vertical": np.array([0.0, 0.0, 1.0]),
    "in_plane_y": np.array([0.0, 1.0, 0.0]),
}


SECTION_SHAPES = {"circular_tube": {"D", "t"}}


def _finite(n: int, label: str, text: str) -> float:
    """Every number the corpus carries, parsed strictly.

    `float()` accepts `nan`, `inf` and `-inf`, and NumPy propagates them without
    complaint: `roll=NaN` built a rotation matrix of NaN, assembled a matrix of
    NaN, solved it, and produced `nan` -- which is not `> ceiling`, so every
    comparison in this module came out False and the entry PASSED. A corpus entry
    written to be refused was instead absorbed. The parser is the place to stop
    it, because the failure is silent everywhere downstream of here.
    """
    try:
        value = float(text)
    except ValueError:
        raise CorpusError(
            f"{CORPUS.name}:{n}: {label}={text!r} is not a number") from None
    if not math.isfinite(value):
        raise CorpusError(
            f"{CORPUS.name}:{n}: {label}={text!r} is not finite. NaN and inf "
            "propagate silently through assembly and the solve, and a NaN "
            "result compares False against every ceiling -- so this would have "
            "been recorded as a pass.")
    return value


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
        k, sep, v = part.partition("=")
        if sep and _finite(n, f"section {k}", v) <= 0.0:
            raise CorpusError(
                f"{CORPUS.name}:{n}: section {k}={v!r} is not positive. "
                "Refused HERE rather than at `Section(...)`, because this "
                "module builds sections while collecting and a constructor "
                "raising at import takes every other entry down with it (R89).")
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


def _direction(n: int, text: str) -> np.ndarray:
    """`orient=` is a NAME or a FREE VECTOR, and the free form is the point.

    A fixed set of four directions makes the orientation axis a parameter the
    IMPLEMENTER chose, which is the failure BE3 moved the corpus out of this
    repository's editable tree to prevent: an adversarial case that can only be
    written in the shapes the author of the check thought of is not adversarial.
    The floor of a skew solve was measured to vary 5.964x across orientations, so
    "which direction" is a live axis and the reviewer must be able to reach all
    of it.

    `orient=x,y,z` takes any three finite numbers and NORMALISES them, so the
    reviewer writes a direction and not a unit vector. Normalising rather than
    demanding a unit vector is deliberate: a hand-written direction truncated to
    six decimals is not a unit vector, and that exact mistake -- a hardcoded SKEW
    at `1.0, 0.35, 0.22` truncated -- produced a whole sweep of numbers belonging
    to a beam nobody was testing.

    A zero vector is REFUSED rather than normalised: `rotation_matrix` would see
    a degenerate element and there is no direction to test.
    """
    if text in ORIENTATIONS:
        return ORIENTATIONS[text]
    parts = text.split(",")
    if len(parts) != 3:
        raise CorpusError(
            f"{CORPUS.name}:{n}: orient={text!r} is neither one of "
            f"{sorted(ORIENTATIONS)} nor three comma-separated numbers")
    v = np.array([_finite(n, f"orient[{i}]", t) for i, t in enumerate(parts)])
    norm = float(np.linalg.norm(v))
    if norm == 0.0:
        raise CorpusError(
            f"{CORPUS.name}:{n}: orient={text!r} is the zero vector; there is no "
            "direction to build a member along")
    return v / norm



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
        _direction(n, row["orient"])
        _validate_section(n, row["section"])
        if _finite(n, "stations", row["stations"]) <= 0.0:
            raise CorpusError(
                f"{CORPUS.name}:{n}: stations={row['stations']!r} is not "
                "positive; a member has a length or it is not a member")
        extra = row.get("extra", "none")
        if not any(extra == e or extra.startswith(e) for e in EXTRAS):
            raise CorpusError(
                f"{CORPUS.name}:{n}: extra={extra!r} is not one of {EXTRAS}. A "
                "typo here used to produce the DEFAULT configuration and pass.")
        # EVERY numeric payload, not only the ones a state happens to reach.
        if extra != "none":
            key, _, payload = extra.partition("=")
            for i, part in enumerate(payload.split(",")):
                _finite(n, f"extra {key}[{i}]" if "," in payload
                        else f"extra {key}", part)
        return row


ENTRIES = _parse()


def _section(spec: str) -> Section:
    parts = dict(p.split("=") for p in spec.split(",")[1:])
    return Section.circular_tube(float(parts["D"]), float(parts["t"]))


def _build(entry: dict[str, str]):
    """Model and elements for one corpus entry, or raise as the entry expects."""
    sec = _section(entry["section"])
    total = float(entry["stations"])
    direction = _direction(0, entry["orient"])
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


def _measure(entry, state: str,
             stiffness_scale: float = 1.0) -> tuple[float, float]:
    """`(forward, oob)` for one state: the SOLVED nodal field error, and G2.2's
    quantity -- the interior out-of-balance of the EXACT field.

    Both are computed from the same assembled matrix, so the reported forward
    error is the one belonging to the configuration the gate is asserting on.
    Only `oob` is asserted (F2.md sec. 5b, Q6).
    """
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

    oob = interior_out_of_balance(m, els, u_ex.reshape(-1),
                                  float(stations[-1]), k=k)
    return relative_error(u, u_ex, stations[-1]), oob


def _oob_state(entry, state: str, stiffness_scale: float = 1.0) -> float:
    return _measure(entry, state, stiffness_scale)[1]


def member_lambda(entry) -> float:
    """`L_member / r` -- the axis the floor tracks (F2.md sec. 5b, Q6).

    Measured on a 2-D grid over element count and member lambda, because both
    one-dimensional sweeps were confounded: element L/r = lambda / n, so only two
    of the three are independent. Member lambda carries the frame-dependent part
    at exponent ~2 in skew against 0.68 axis-aligned; element L/r is refuted,
    since if it governed the two exponents would be equal and opposite.
    """
    return _member_lambda(float(entry["stations"]), _section(entry["section"]))


FREE_DIRECTIONS = [
    ("named", "skew", ORIENTATIONS["skew"]),
    ("unit vector", "0,0,1", np.array([0.0, 0.0, 1.0])),
    ("NOT a unit vector", "3,4,0", np.array([0.6, 0.8, 0.0])),
    ("truncated, as a hand-written one is",
     "-0.384196,-0.923213,0.008385",
     np.array([-0.384196, -0.923213, 0.008385])
     / np.linalg.norm([-0.384196, -0.923213, 0.008385])),
]


@pytest.mark.parametrize("label, text, expected", FREE_DIRECTIONS,
                         ids=[d[0] for d in FREE_DIRECTIONS])
def test_orient_takes_any_direction_and_NORMALISES_it(
    label: str, text: str, expected
) -> None:
    """The reviewer writes a direction; this module makes it a unit vector.

    `3,4,0` is the case that matters: it is not a unit vector, and if it were
    used as one the member would be 5x its stated length and every figure
    measured on it would belong to a different beam. That is not hypothetical --
    a hardcoded SKEW truncated to six decimals did exactly this and produced a
    whole sweep of numbers for a beam nobody was testing.
    """
    got = _direction(0, text)
    assert_close(float(np.linalg.norm(got)), 1.0, ROUNDOFF_IDENTITY,
                 floor=np.finfo(float).eps,
                 what=f"|orient={text}| after normalisation")
    # THE DIRECTION, on an O(1) quantity (R38). `got . expected` is 1 exactly
    # when the two are parallel AND both unit, so this one comparison carries
    # both properties without ever comparing two numbers near zero -- which is
    # the comparison `assert_close` refuses to make, for the reason R38 records.
    assert_close(float(got @ expected), 1.0, ROUNDOFF_IDENTITY,
                 floor=np.finfo(float).eps,
                 what=f"orient={text} against its normalised expectation")


BAD_DIRECTIONS = [
    ("zero vector", "0,0,0"),
    ("two components", "1,0"),
    ("four components", "1,0,0,0"),
    ("a bare number", "1.0"),
    ("a typo'd name", "skewed"),
    ("non-finite", "1,NaN,0"),
    ("infinite", "1,inf,0"),
]


@pytest.mark.parametrize("label, text", BAD_DIRECTIONS,
                         ids=[d[0] for d in BAD_DIRECTIONS])
def test_a_direction_that_cannot_be_built_RAISES(label: str, text: str) -> None:
    """Never a silent default. A typo'd name used to be caught by the name check
    and everything else did not exist; opening the field up without opening the
    refusals up would have been the vacuous-parameter failure again."""
    with pytest.raises(CorpusError):
        _direction(0, text)


def test_the_counter_is_ABOVE_the_ceiling() -> None:
    """The one relation that makes a ceiling and a counter into a gate (R85).

    If the smallest defect a configuration must detect sits BELOW the largest
    clean value the gate admits, then an entry can hold and be undetectable at
    the same time and the pair asserts nothing. This is not hypothetical: at the
    ceiling this gate carried one commit ago -- 1e-12, a value derived for the
    quantity G2.2 no longer asserts -- the counter sat at 0.11x of it, and a 1e-6
    single-element defect on the most slender corpus entry would have passed.

    Stated with the two values `tolerances.py` already owns and no third number,
    because a multiplier written here is a decision threshold outside
    `tolerances.py`, which is what R85 found (`100.0`, settable to `1e-30` with
    the suite green).
    """
    assert PATCH_TEST_EXACTNESS_COUNTER > PATCH_TEST_EXACTNESS, (
        f"the counter {PATCH_TEST_EXACTNESS_COUNTER:.3e} is not above the "
        f"ceiling {PATCH_TEST_EXACTNESS:.3e}. A defect the gate is required to "
        "catch is smaller than the deviation the gate is allowed to ignore, so "
        "an entry can pass the ceiling and fail nothing."
    )


def test_the_corpus_exists_and_is_not_empty() -> None:
    """AM5: an empty parameter set is an error, not a silent pass."""
    assert CORPUS.exists(), f"{CORPUS} is missing; the corpus is the reviewer's"
    assert len(ENTRIES) >= 10, f"only {len(ENTRIES)} corpus entries parsed"


def _inadmissible(entry) -> float | None:
    """The member's L/D if it is below the admission limit, else None.

    NEVER RAISES, because it runs at IMPORT (R89). It used to call `_section` and
    `member_l_over_d` unguarded while building `INADMISSIBLE` at module level, so
    a single entry whose section or length the constructors refuse took the whole
    module out at COLLECTION -- and every other entry stopped being measured. Two
    such shapes had to be carried in the corpus as comments rather than as
    entries, which is a corpus that cannot be run.

    A configuration this cannot evaluate is not "admissible"; it is one whose
    refusal belongs to `_build`, where it produces a FAILING TEST that names the
    entry instead of a collection error that names nothing.
    """
    if "_error" in entry:
        return None
    try:
        ratio = member_l_over_d(float(entry["stations"]),
                                _section(entry["section"]))
    except Exception:
        return None
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


def _branch(entry) -> str:
    """Which path the per-entry test takes for this entry.

    Named and returned rather than left implicit in a chain of `if`s, so the
    coverage test can recompute the partition by a SECOND route and compare
    (R77). The previous coverage assertion built `solved` and `refused` from
    predicates that were exact complements by De Morgan, so `solved & refused`
    was empty and `solved | refused` was everything -- for any corpus, including
    an empty one. It asserted nothing, and was carried as an open finding for
    three rounds.
    """
    if "_error" in entry:
        return "unparseable"
    if _inadmissible(entry) is not None:
        return "inadmissible"
    if entry["expect"] == "raise":
        return "refused"
    return "measured"


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

    # ONE TIER, EVERY ENTRY, INCLUDING THE ONES MARKED `breach`. There is no
    # relief branch here any more: the quantity that needed one is no longer
    # asserted.
    worst = max(_oob_state(entry, st) for st in STATES)

    assert worst <= PATCH_TEST_EXACTNESS, (
        f"{entry['id']}: the exact constant-strain field leaves an interior "
        f"out-of-balance of {worst:.4e}, above {PATCH_TEST_EXACTNESS:.0e} "
        f"(member lambda {member_lambda(entry):.1f}, expect={expect}). The "
        "field does not satisfy the discrete equations on this configuration."
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
    smallest = min(_oob_state(entry, st, stiffness_scale=1.0 + 1.0e-6)
                   for st in STATES)

    # NO EXEMPTION BRANCH, and its removal is a strengthening (R83). Under the
    # retired quantity the anisotropic entry `aniso_I_y_500x` responded at
    # 8.6804e-08 -- 13% below its counter -- and had to be excluded by name, with
    # the counter carrying a stated domain of circular sections. Under the
    # out-of-balance quantity it responds at 1.7605e-11, 164x clear, so every
    # entry in the corpus is now held to this control.
    assert smallest >= PATCH_TEST_EXACTNESS_COUNTER, (
        f"{entry['id']}: the weakest state responded to a 1e-6 single-element "
        f"defect with only {smallest:.4e}, below the counter "
        f"{PATCH_TEST_EXACTNESS_COUNTER:.3e}. The gate holds here and cannot "
        "fail here."
    )

    # THE SEPARATION IS ASSERTED WITH NO FRESH NUMBER (R85). The previous form
    # was `smallest > 100.0 * ceiling`, and the reviewer set that multiplier to
    # `1e-30` with the suite green: a decision threshold living outside
    # `tolerances.py`, which `CLAUDE.md` forbids under "tier cutoffs in
    # screening". A second literal here would have been the fourth instance.
    #
    # The property that matters is that the counter is ABOVE the ceiling -- if it
    # is not, an entry can hold and be undetectable at the same time -- and that
    # is a relation between two values `tolerances.py` already owns. It is
    # asserted once, in `test_the_counter_is_ABOVE_the_ceiling`, and needs no
    # third number to state.


SOLVED = [e for e in ENTRIES
          if e["expect"] != "raise" and "_error" not in e
          and _inadmissible(e) is None]


def test_the_recorded_breaches_are_REPORTED_for_re_recording(capsys) -> None:
    """The reviewer's `expect=breach` record was against a RETIRED quantity.

    It was the solved nodal field error against a 1e-12 ceiling. Both are gone:
    the quantity is reported and not asserted, and the constant it was recorded
    against does not exist. This module will not manufacture a replacement
    constant to keep the assertion alive -- that is a tolerance wearing a
    record's clothes -- so it prints both quantities for every breach entry and
    the reviewer re-records `expect`.

    What is NOT relaxed: these entries are asserted by the single-tier gate and
    by the counter exactly like every other entry, in the two tests above.
    """
    breaches = [e for e in SOLVED if e["expect"] == "breach"]
    with capsys.disabled():
        print(f"\n  RE-RECORD ({len(breaches)} entries marked expect=breach "
              "against the retired quantity):")
        print(f"  {'id':32} {'member lam':>10} {'forward':>12} "
              f"{'out-of-balance':>15} {'x ceiling':>10}")
        for e in breaches:
            fwd = max(_measure(e, st)[0] for st in STATES)
            oob = max(_measure(e, st)[1] for st in STATES)
            print(f"  {e['id']:32} {member_lambda(e):10.1f} {fwd:12.4e} "
                  f"{oob:15.4e} {oob / PATCH_TEST_EXACTNESS:9.3f}x")
    assert True  # not-a-tolerance: this test reports, the assertions are above


def test_the_forward_error_is_REPORTED_and_the_floor_is_too(capsys) -> None:
    """The diagnostic the gate stopped asserting, kept visible per entry.

    Printed rather than asserted, because it is `cond` x backward error and no
    constant survives contact with the axes `cond` moves along. The gate's own
    floor and the counter's smallest response are printed with it, because those
    two numbers are what set `PATCH_TEST_EXACTNESS` and they must be regenerable
    from the shipped suite (BI3).
    """
    rows = []
    for e in SOLVED:
        fwd = max(_measure(e, st)[0] for st in STATES)
        oob = max(_measure(e, st)[1] for st in STATES)
        det = min(_oob_state(e, st, stiffness_scale=1.0 + 1.0e-6)
                  for st in STATES)
        rows.append((e["id"], member_lambda(e), fwd, oob, det))
    eps = float(np.finfo(float).eps)
    worst_oob = max(r[3] for r in rows)
    worst_id = max(rows, key=lambda r: r[3])[0]
    least_det = min(r[4] for r in rows)
    least_id = min(rows, key=lambda r: r[4])[0]
    with capsys.disabled():
        print(f"\n  {'id':32} {'member lam':>10} {'forward':>12} "
              f"{'out-of-balance':>15} {'1e-6 defect':>13}")
        for i, lam, fwd, oob, det in sorted(rows, key=lambda r: -r[3]):
            print(f"  {i:32} {lam:10.1f} {fwd:12.4e} {oob:15.4e} {det:13.4e}")
        print(f"\n  FLOOR    worst clean out-of-balance {worst_oob:.4e} "
              f"({worst_oob / eps:.2f} eps, {worst_id})")
        print(f"  COUNTER  smallest 1e-6 response      {least_det:.4e} "
              f"({least_id})")
        print(f"  CEILING  PATCH_TEST_EXACTNESS        "
              f"{PATCH_TEST_EXACTNESS:.4e}   "
              f"{PATCH_TEST_EXACTNESS / worst_oob:.1f}x above the floor, "
              f"{least_det / PATCH_TEST_EXACTNESS:.1f}x below the counter")
    assert True  # not-a-tolerance: this test reports, the assertions are above


def test_the_corpus_coverage_is_reported(capsys) -> None:
    """The coverage number, in the form the reviewer scores it."""
    runs = len(ENTRIES)
    recorded = sum(1 for e in ENTRIES if e.get("runs_in_suite") == "yes")
    with capsys.disabled():
        print(f"\n  corpus: {runs} entries executed by this module; "
              f"{recorded} recorded as runs_in_suite=yes at the last review")
    # TWO INDEPENDENT ROUTES TO THE SAME PARTITION, COMPARED (R77). One is the
    # branch the per-entry test actually takes; the other is the predicate that
    # decides which entries the DETECTION test is parametrised over. They are
    # written separately and can drift, and if they do, an entry is measured by
    # one test and silently absent from the other -- which is the failure this
    # test is for. Comparing a predicate with its own negation, as this did for
    # three rounds, could not detect that or anything else.
    measured = {e["id"] for e in ENTRIES if _branch(e) == "measured"}
    parametrised = {e["id"] for e in SOLVED}
    assert measured == parametrised, (
        f"the per-entry test measures {sorted(measured - parametrised)} that the "
        f"detection test never sees, and the detection test is parametrised over "
        f"{sorted(parametrised - measured)} that the per-entry test refuses. One "
        "of the two predicates has drifted."
    )

    # And the partition is non-degenerate in BOTH directions: a predicate bug
    # that routed every entry to one branch would leave the other empty and
    # score nothing, with every remaining assertion vacuously satisfied.
    tally: dict[str, int] = {}
    for e in ENTRIES:
        tally[_branch(e)] = tally.get(_branch(e), 0) + 1
    assert tally.get("measured", 0) > 0, "no entry is measured at all"
    assert len(ENTRIES) - tally.get("measured", 0) > 0, "no entry is refused at all"
    solved = measured
    refused = {e["id"] for e in ENTRIES} - measured
    with capsys.disabled():
        print("          branches: "
              + ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))
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
    # THE TWO SHAPES THAT USED TO TAKE THE MODULE OUT AT COLLECTION (R89). Each
    # is a value, not a key, so every check above passed it and `Section(...)` or
    # `member_l_over_d` raised while `INADMISSIBLE` was being built at import --
    # taking every other entry's measurement with it. They were carried in the
    # corpus as comments for exactly that reason.
    ("negative wall", "id=x section=circular_tube,D=0.600,t=-0.01200 "
     "stations=9.67 orient=skew expect=raise"),
    ("negative stations", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=-9.67 orient=skew expect=raise"),
    ("zero diameter", "id=x section=circular_tube,D=0,t=0.012 "
     "stations=9.67 orient=skew expect=raise"),
    ("non-finite wall", "id=x section=circular_tube,D=0.6,t=inf "
     "stations=9.67 orient=skew expect=raise"),
    ("non-finite roll", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=skew extra=roll=NaN expect=raise"),
    ("free direction, zero vector", "id=x section=circular_tube,D=0.6,t=0.012 "
     "stations=9.67 orient=0,0,0 expect=raise"),
]


@pytest.mark.parametrize("label, line", MALFORMED, ids=[m[0] for m in MALFORMED])
def test_a_malformed_corpus_line_RAISES(label: str, line: str) -> None:
    """Measured before this existed: every one of these produced the DEFAULT
    configuration and a passing result identical to `extra=none`."""
    with pytest.raises(CorpusError):
        _parse_line(1, line)


def test_a_REFUSING_entry_does_not_take_the_module_out_at_collection() -> None:
    """R89's real closing condition, and it is about WHEN the failure happens.

    `INADMISSIBLE` is built at import from every entry, so a construction error
    there is a COLLECTION error: pytest reports one broken file and 48 solved
    entries stop being measured. That is worse than a silent pass, because a
    silent pass at least leaves the other entries scored.

    Both halves are asserted: the parser refuses these values (above), and
    `_inadmissible` -- the function that runs at import -- returns rather than
    raising on anything it cannot evaluate.
    """
    for entry in ({"id": "x", "stations": "-9.67",
                   "section": "circular_tube,D=0.6,t=0.012", "expect": "raise"},
                  {"id": "x", "stations": "9.67",
                   "section": "circular_tube,D=0.6,t=-0.012", "expect": "raise"},
                  {"id": "x", "stations": "9.67",
                   "section": "circular_tube,D=0.0,t=0.0", "expect": "raise"}):
        assert _inadmissible(entry) is None, (
            f"{entry}: _inadmissible returned a value for a section it cannot "
            "build; it runs at import and must never raise or guess"
        )


def test_a_WELL_FORMED_line_still_parses() -> None:
    """The strictness must not refuse everything -- the meta-test for a guard."""
    row = _parse_line(
        1,
        "id=ok section=circular_tube,D=0.6,t=0.012 stations=9.67 orient=skew "
        "extra=roll=0.5 runs_in_suite=no expect=hold")
    assert row["id"] == "ok" and row["extra"] == "roll=0.5"
