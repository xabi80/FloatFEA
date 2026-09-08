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
                `PATCH_TEST_EXACTNESS`, and every NAMED DEFECT injected into it
                pushes the out-of-balance ABOVE `PATCH_TEST_EXACTNESS` -- the
                gate goes red. The margin is reported, never asserted (BO0).
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

from floatfea.assemble.system import (BeamElement, assemble,
                                      element_length, solve)
from floatfea.element.beam import local_stiffness
from floatfea.element.transform import rotation_matrix
from floatfea.model.admissibility import (assert_beam_admissible,
                                          member_l_over_d)
from floatfea.model.admissibility import member_lambda as _member_lambda
from floatfea.model.material import S355, Section
from floatfea.testing import assert_close
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (BEAM_ADMISSION_L_OVER_D,
                                 PATCH_TEST_COUNTER_HEADROOM,
                                 PATCH_TEST_EXACTNESS,
                                 PATCH_TEST_EXACTNESS_COUNTER_DEFECT,
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
EXTRA_KEYS = ("orientation_node", "roll", "I_y_over_I_z")

# THE SYNTHETIC ANISOTROPY ROUTE'S ADMISSIBLE RANGE (BP5/R119). `I_y_over_I_z`
# writes `I_y` with `object.__setattr__`, which is the ONLY route in this
# repository past `Section.__post_init__` -- and the invariant that guard enforces
# for a circular shape is `I_y == I_z`, not merely a positive sign. R114 closed
# this as a sign test, which let `1e-300` through: the resulting element has a
# bending stiffness 300 orders below its axial one, its weakest-state response to
# a defect is exactly `0.0`, and a control measured on it certifies nothing.
#
# THE RANGE IS JUSTIFIED BY WHAT THE ROUTE IS FOR, not by a numerical floor
# (R128). Synthetic anisotropy exists to pin the INDEX MAPPING: with `I_y == I_z`
# forced on every section the type admits, an element that swapped the two
# bending blocks would be indistinguishable from a correct one, and R53 is that
# blindness recorded. Making `I_y != I_z` by the only route past
# `Section.__post_init__` is how a corpus entry can tell them apart.
#
# A ratio far from 1 serves that purpose no better than a ratio near it -- one
# order either way already separates the blocks unambiguously -- so the range is
# set wide enough to leave the reviewer room (the corpus carries `0.02` and
# `500`) and no wider than the purpose needs. `1e-6 .. 1e6` is twelve orders,
# 3000x beyond the widest entry written so far.
#
# The first version of this comment argued the bound from a numerical floor
# derived from the sensitivity band -- a quantity deleted in the same commit.
I_Y_OVER_I_Z_RANGE = (1.0e-6, 1.0e6)
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
            rows.append(_error_row(n, line, exc))
    return rows


def _field(line: str, key: str, default: str) -> str:
    """One `key=value` token out of a raw corpus line, without parsing the line.

    Used only on lines the parser has already refused, where the structured row
    does not exist and the raw text is all there is.

    A REPEATED KEY IS NOT RESOLVED HERE (R104). This took the FIRST match, while
    `_parse_line` refuses duplicates outright -- so `expect=raise expect=hold`
    came back as `"raise"` and the per-entry assertion passed on a line whose
    recorded expectation is contradictory. Taking the first is as arbitrary as
    taking the last; the value returned names the problem so the assertion that
    reads it reddens with something a reader can act on.
    """
    found = [t.split("=", 1)[1] for t in line.split()
             if t.startswith(key + "=")]
    if len(found) > 1:
        return "AMBIGUOUS(" + "|".join(found) + ")"
    return found[0] if found else default


def _error_row(n: int, line: str, exc: Exception) -> dict[str, str]:
    """The row for a line that cannot be executed.

    **THE REVIEWER'S `expect` SURVIVES (R91).** This used to write
    `"expect": "raise"` unconditionally, and the per-entry test then asserted
    `expect == "raise"` -- comparing a variable with the constant assigned to it
    eighty lines earlier, on the one instrument in this repository the
    implementer does not write. A line the reviewer recorded as `hold` and the
    module cannot build read GREEN while measuring nothing.

    Twelfth guard, again: the parser reports what it cannot do rather than doing
    something else. Overwriting a field to make a downstream comparison succeed
    IS doing something else, and it is worse than the skip that guard was written
    against, because a skip is visible in the count.

    `unrecorded` is used when the line carries no `expect` at all -- itself a
    malformed line, and one whose only admissible reading is not "raise".
    """
    return {
        "id": _field(line, "id", f"line{n}"),
        "expect": _field(line, "expect", "unrecorded"),
        "_error": str(exc),
        "_line": line,
    }


def _extras(n: int, text: str) -> dict[str, list[str]]:
    """`extra=` is a SEQUENCE of `key=value` pairs, not one (R91).

    The reviewer asked for roll and anisotropy on one member and could not write
    it: the field took a single key, so the line was unparseable, and the parser
    then recorded it as `expect=raise` and the entry read green. Two defects in
    one line -- the missing capability and the overwritten field -- and only the
    second is a correctness bug. This closes both.

    The separator is a comma, because that is what the corpus already uses, and a
    value may itself contain commas (`orientation_node=1,0,0`). The rule that
    resolves it without a second separator: a comma-separated token containing
    `=` starts a NEW key; a token without one continues the previous key's value.
    Ambiguity is refused, not guessed at -- a leading token with no key raises.
    """
    if text == "none":
        return {}
    out: dict[str, list[str]] = {}
    key: str | None = None
    for token in text.split(","):
        name, sep, value = token.partition("=")
        if sep:
            if name not in EXTRA_KEYS:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: extra key {name!r} is not one of "
                    f"{list(EXTRA_KEYS)}. A typo here used to produce the "
                    "DEFAULT configuration and pass.")
            if name in out:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: extra key {name!r} appears twice. "
                    "Taking the last silently runs a configuration nobody "
                    "wrote.")
            key = name
            out[key] = [value]
        else:
            if key is None:
                raise CorpusError(
                    f"{CORPUS.name}:{n}: extra={text!r} starts with {token!r}, "
                    "which names no key")
            out[key].append(token)

    for name, parts in out.items():
        want = 3 if name == "orientation_node" else 1
        if name == "I_y_over_I_z" and len(parts) == 1:
            lo_r, hi_r = I_Y_OVER_I_Z_RANGE
            # R114. `I_y_over_I_z=0` built a section with ZERO bending stiffness
            # about one axis and `=-1.0` built a NEGATIVE one, both silently:
            # `object.__setattr__` writes past `Section.__post_init__`, which is
            # the only place that checks. A structure with negative bending
            # stiffness is not a structure, and the entry that asks for one is
            # asking this module to build something no production path can.
            try:
                ratio = float(parts[0])
            except ValueError:
                ratio = float("nan")
            if not (lo_r <= ratio <= hi_r):
                raise CorpusError(
                    f"{CORPUS.name}:{n}: extra I_y_over_I_z={parts[0]!r} is "
                    f"outside the admissible range {lo_r:g} .. {hi_r:g}. A "
                    "second moment of area is positive by definition, so zero "
                    "or negative builds an element with no bending stiffness or "
                    "with negative bending stiffness; and a denormal ratio "
                    "builds one whose weakest-state response to a defect is "
                    "exactly 0.0, which is a control that certifies nothing. "
                    "`Section.__post_init__` is the only guard on any of this "
                    "and the route this field uses bypasses it.")
        if len(parts) != want:
            raise CorpusError(
                f"{CORPUS.name}:{n}: extra {name} takes {want} value(s); got "
                f"{len(parts)} ({parts})")
        for i, part in enumerate(parts):
            _finite(n, f"extra {name}[{i}]" if want > 1 else f"extra {name}",
                    part)
    return out


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
        _extras(n, row.get("extra", "none"))
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

    # EVERY extra the line carries, not the first one that matches (R91).
    extras = _extras(0, entry.get("extra", "none"))
    onode = None
    roll = 0.0
    for name, parts in extras.items():
        if name == "orientation_node":
            onode = np.array([float(v) for v in parts])
        elif name == "roll":
            roll = float(parts[0])
        elif name == "I_y_over_I_z":
            object.__setattr__(sec, "I_y", sec.I_z * float(parts[0]))
        else:  # pragma: no cover -- _extras refuses these first
            raise CorpusError(f"{entry['id']}: unhandled extra {name!r}")

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
             defect_size: float = 0.0) -> tuple[float, float]:
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
    if defect_size != 0.0:
        from floatfea.assemble.system import element_global_stiffness
        # THE DEFECT SIZE IS APPLIED DIRECTLY, not as `(1 + size) - 1` (BQ0).
        # That subtraction loses `eps/size ~ 2e-10` of relative precision to
        # cancellation, so a defect declared as `1e-6` was injected at
        # `9.99999999955e-07` -- and `classify`, comparing the measured size
        # against the declared one, put the gate's OWN counter-defect below its
        # own resolution on every entry. The arithmetic was deciding a
        # classification.
        delta = defect_size * element_global_stiffness(m, els[1])
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


def _oob_state(entry, state: str, defect_size: float = 0.0) -> float:
    return _measure(entry, state, defect_size)[1]


def _entry_section(entry) -> Section:
    """The section this entry actually builds, `extra=` INCLUDED.

    `_section` reads `section=` alone, so an entry carrying
    `extra=I_y_over_I_z=` got a section it does not use. Everything that
    characterises an entry has to come through here (R96).
    """
    sec = _section(entry["section"])
    extras = _extras(0, entry.get("extra", "none"))
    if "I_y_over_I_z" in extras:
        object.__setattr__(sec, "I_y",
                           sec.I_z * float(extras["I_y_over_I_z"][0]))
    return sec


def member_lambda(entry) -> float:
    """`L_member / r_min` on the WEAK axis -- the axis sensitivity tracks (R96).

    THIS READ THE STRONG AXIS AND ORDERED ENTRIES WRONGLY. It rebuilt the section
    from `section=` and discarded `extra=I_y_over_I_z=`, so an anisotropic entry
    reported `min(I_y, I_z)`'s partner. Two entries printed the same
    `lambda = 153.9` and sat 5x apart in detection; on the weak axis they are
    `688` and `1539`, and the ordering is right. The mechanism says it must be the
    weak axis: the residual normalises by the LARGEST stiffness, so what falls is
    the ratio to the SMALLEST bending stiffness.


    Measured on a 2-D grid over element count and member lambda, because both
    one-dimensional sweeps were confounded: element L/r = lambda / n, so only two
    of the three are independent. Member lambda carries the frame-dependent part
    at exponent ~2 in skew against 0.68 axis-aligned; element L/r is refuted,
    since if it governed the two exponents would be equal and opposite.
    """
    return _member_lambda(float(entry["stations"]), _entry_section(entry))


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
            f"{entry['id']}: the corpus records expect={expect!r}, and this "
            f"module cannot execute the line at all -- {entry['_error']}. The "
            "disagreement is the finding: either the entry names something this "
            "module should be able to build and does not, or the entry is "
            "malformed and belongs at expect=raise. It is not resolved here."
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


SOLVED = [e for e in ENTRIES
          if e["expect"] != "raise" and "_error" not in e
          and _inadmissible(e) is None]


# `no_op` is a NAMED control, not a defect: it returns the element unchanged, so
# `classify` must place it below the declared resolution. A classification that
# cannot say `no` classifies nothing (R126).
ORIGINAL_LOCAL_STIFFNESS = local_stiffness

DEFECT_BUILDERS = ("dropped_flip", "wrong_dof_index",
                   "dropped_shear_parameter", "no_op")


def _defective_stiffness(kind: str):
    """A builder for `local_stiffness` carrying ONE structural defect.

    AN UNRECOGNISED NAME RAISES (BQ2/R126). It used to fall through every branch
    and return the CLEAN matrix, so a typo -- or `injected_delta(entry,
    "transposed_transform")`, a defect this builder does not implement -- reported
    a delta of `0.0` and was classified as changing nothing. A builder that
    silently returns the thing it was asked to corrupt is the vacuous-parameter
    failure AM5 named, one level down.

    These are FORMULATION defects: they change what the element is, not how stiff
    it is. That is the class this gate exists for, and it is the class whose
    response does NOT fall with slenderness -- which is why it, and not a fixed
    small-defect threshold, is what the red-on-defect assertion is about.
    """
    from floatfea.element.beam import bending_stiffness, shear_parameter

    if kind not in DEFECT_BUILDERS:
        raise ValueError(
            f"no defect builder for {kind!r}; known builders are "
            f"{list(DEFECT_BUILDERS)}. Returning the clean matrix for an "
            "unrecognised name would report the defect as changing nothing.")

    def build(section, material, ll):
        if kind == "no_op":
            return ORIGINAL_LOCAL_STIFFNESS(section, material, ll)
        k = np.zeros((12, 12))
        k[np.ix_([0, 6], [0, 6])] = (material.E * section.A / ll) * np.array(
            [[1.0, -1.0], [-1.0, 1.0]])
        k[np.ix_([3, 9], [3, 9])] = (material.G * section.J / ll) * np.array(
            [[1.0, -1.0], [-1.0, 1.0]])

        # `dropped_shear_parameter`: Timoshenko reduced to Euler-Bernoulli, `Phi`
        # forced to zero in both planes. Reinstated as a gate defect (BP3): the
        # figure that excluded it -- "undetectable on 22 of 63 entries" -- was
        # measured against a response floor that no longer exists, and against
        # the CEILING it is 0 of 74, minimum margin 1739x.
        def phi(plane: str) -> float:
            if kind == "dropped_shear_parameter":
                return 0.0
            return shear_parameter(section, material, ll, plane=plane)

        kz = bending_stiffness(material.E * section.I_z, ll, phi("xy"))
        # `wrong_dof_index`: the x-y block scattered onto DOF 10 instead of 11 --
        # rz_B landing on ry_B. One character in a slice.
        idx_xy = [1, 5, 7, 10] if kind == "wrong_dof_index" else [1, 5, 7, 11]
        k[np.ix_(idx_xy, idx_xy)] = kz

        ky = bending_stiffness(material.E * section.I_y, ll, phi("xz"))
        # `dropped_flip`: the x-z block without its sign correction. A positive
        # rotation about +y produces a NEGATIVE w-slope; drop `flip` and the block
        # is the x-y pattern in the x-z plane.
        if kind != "dropped_flip":
            f = np.diag([1.0, -1.0, 1.0, -1.0])
            ky = f @ ky @ f
        k[np.ix_([2, 4, 8, 10], [2, 4, 8, 10])] = ky
        return k

    return build


def _oob_with_defect(entry, state: str, kind: str) -> float:
    """`_oob_state` with `kind` injected into every element's local stiffness.

    The assembler imports `local_stiffness` by name, so the patch goes on
    `floatfea.assemble.system` -- patching `floatfea.element.beam` changes
    nothing and every defect then reports the clean value.
    """
    import floatfea.assemble.system as system

    original = system.local_stiffness
    system.local_stiffness = _defective_stiffness(kind)
    try:
        return _oob_state(entry, state)
    finally:
        system.local_stiffness = original


# THE DEFECTS THIS GATE IS ASSERTED AGAINST, each injected and each required to
# turn the gate red on EVERY entry (BO0/BO1).
#
# `dropped_flip`, `wrong_dof_index` and `dropped_shear_parameter` are injected
# into `local_stiffness`;
# `one_element_scaled` is the `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`-sized
# perturbation of a single interior element.
#
# TWO DEFECTS ARE DELIBERATELY NOT HERE, and where they go vacuous is measured
# rather than assumed. Both are cases of the defect being ABSENT, which is what
# `classify` now states as a rule rather than as a list:
#
#   `I_y <-> I_z`         a no-op wherever `I_y == I_z`, which is every section
#                         `basis.kappa` admits (R53).
#   transposed transform  a no-op wherever the rotation is SYMMETRIC. Measured,
#                         `|R - R.T| = 0` exactly on 8 corpus entries -- an
#                         axis-aligned member with no roll has `R = I`. On two
#                         further entries the injected difference is ABSENT from
#                         the assembled matrix rather than small: see the
#                         corrected statement in `test_patch_test.py`. It stays
#                         the SKEW counter-case it already is.
#
# THE DROPPED SHEAR PARAMETER IS IN THE SET (BP3), and the sentence that excluded
# it is withdrawn: "undetectable on 22 of 63 entries" was measured against a
# response floor deleted in the same round, and against the CEILING no corpus
# entry was below it at that commit.
INJECTED_DEFECTS = ("dropped_flip", "wrong_dof_index",
                    "dropped_shear_parameter", "one_element_scaled")


def _homogeneous(k: np.ndarray, ell: float) -> np.ndarray:
    """`D^-1 k D^-1` with `D = diag(I3, l I3, I3, l I3)` -- the residual's units.

    The same scaling `interior_out_of_balance` applies before it takes a norm, so
    a defect measured through here is measured in the units the gate decides in.

    THE CONVENTION IS `ell = MEMBER LENGTH`, and what matters is not the number
    but that it SCALES WITH THE MODEL. Multiplying it by a constant is a change
    of convention, not a defect: it rescales every rotational row and column of
    both the numerator and the denominator, and `injected_delta` is a ratio of
    the two. What would be a defect is `ell` becoming a CONSTANT -- then a member
    measured in millimetres and the same member in kilometres would weight their
    rotations identically and the measure would stop being unit-invariant.

    That is the property, and it has a shipped control on each side:
    `test_the_delta_measure_is_UNIT_INVARIANT` and its negative
    `test_a_CONSTANT_ell_breaks_unit_invariance` (BS3, from BI1's pattern).
    """
    w = np.ones(12)
    w[3:6] = ell
    w[9:12] = ell
    return (k / w[:, None]) / w[None, :]


def injected_delta(entry, kind: str) -> float:
    """The defect's EFFECTIVE SIZE: `max |dK_hat| / max |K_hat|` (BR1).

    The absolute change normalised by the LARGEST stiffness in the element, in the
    residual's homogeneous units, taken over every element the defect touches.

    WHY THIS RATHER THAN THE RELATIVE CHANGE INSIDE THE BLOCK. Two rules were
    refuted before this one, and the second by its own premise. It compared a
    defect's relative change within its block against the declared resolution --
    and the residual does not see a block, it normalises by the largest stiffness
    in the element. At equal declared size a bending-block defect responds
    `2.00/lambda^2` of a whole-element one, measured to +/-6% over 59x in lambda
    and four section families. So a bending defect of "size 1e-6" is not a defect
    of size 1e-6 to this gate, and calling it one put two corpus entries 25-36x
    above the declared resolution and undetected.

    THERE IS NO `lambda` IN THIS. The `lambda^2` suppression falls out of the
    matrix rather than being declared, which is why the corpus entry whose
    `L/r_min` moves tenfold with no change in margin stops being a
    counterexample: the variable was never a slenderness, it was which block the
    defect lands in.

    `test_the_delta_measure_is_CALIBRATED` pins it in both directions.
    """
    import floatfea.assemble.system as system

    m, els, stations = _build(entry)
    ell = float(stations[-1])
    worst = 0.0
    for i, e in enumerate(els):
        length = element_length(m, e)
        clean = ORIGINAL_LOCAL_STIFFNESS(e.section, e.material, length)
        if kind == "one_element_scaled":
            if i != 1:
                continue
            change = PATCH_TEST_EXACTNESS_COUNTER_DEFECT * clean
        else:
            change = (_defective_stiffness(kind)(e.section, e.material, length)
                      - clean)
        denom = float(np.abs(_homogeneous(clean, ell)).max())
        if denom > 0.0:
            worst = max(worst,
                        float(np.abs(_homogeneous(change, ell)).max() / denom))
    return worst


def classify(entry, kind: str) -> str:
    """`live` if the defect is at least the size the gate claims to detect.

    THE RULE, AND IT REPLACES A DOMAIN ON SLENDERNESS (BQ0/R123). A named defect
    must redden the gate wherever it is at least as large as the defect the gate
    claims to detect. Below that it is not a failure of the gate: the gate says
    it resolves `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, and a defect smaller than
    that is outside what it ever claimed.

    The dropped shear parameter is why this is a rule and not a boundary. Its
    magnitude is `Phi ~ 59/lambda^2`, so at `L/r_min ~ 2e4` it changes the bending
    block by `1.5e-07` -- less than the `1e-6` the gate claims to resolve -- and
    its measured margin falls as `lambda^-4`, which is `Phi(lambda)` times the
    residual's own `lambda^-2`. Bounding it by a slenderness would state the
    consequence; this states the cause, and it needs no new constant.

    THE RESOLUTION IS THE DECLARED ONE, NEVER A MEASURED PER-ENTRY ONE. A gate
    that went blind would coarsen its own resolution and exempt exactly the
    defects it had stopped seeing -- R56's species. The declared constant is
    guarded in both directions by `test_the_counter_DEFECT_SIZE_cannot_be_raised`
    and its counter, and this classification borrows that guard.
    """
    # THE COMPARISON CARRIES THE SAME ULP ALLOWANCE THE CALIBRATION DOES
    # (R142). `injected_delta` computes `max|CD k_hat| / max|k_hat|`, which lands
    # one ULP below `CD` on some entries -- and a bare `>=` then classified the
    # gate's OWN counter-defect as below its own resolution on one of them.
    floor = PATCH_TEST_EXACTNESS_COUNTER_DEFECT * (1.0 - ROUNDOFF_IDENTITY)
    return ("live" if injected_delta(entry, kind) >= floor
            else "below resolution")


# THE DEFECTS WHOSE REDNESS IS NOT SUBJECT TO CLASSIFICATION (BR3). These are
# asserted red on EVERY entry with no classification in front of them, so no
# change to `injected_delta` or to a tolerance can exempt them.
#
# THE DIRECTIVE ASKED FOR THEM TO BE ASSERTED `live` AS WELL, AND MEASUREMENT
# REFUSES THAT. On 19 (entry, defect) pairs -- the most slender corpus entries --
# a structural defect's effective size falls below `1e-6`, because
# `K_bend/K_max ~ 12/lambda_elem^2` shrinks any bending-block defect however
# structural it is. Every one of those 19 is still RED, from `2.838e+05x` at the
# weakest to `1.114e+08x`. So the surviving half of the claim is the half that
# matters, and the `live` half is withdrawn rather than asserted where it does
# not hold.
UNCONDITIONALLY_RED = ("dropped_flip", "wrong_dof_index", "one_element_scaled")


def _oob_with_injected(entry, state: str, kind: str) -> float:
    if kind == "one_element_scaled":
        return _oob_state(
            entry, state,
            defect_size=PATCH_TEST_EXACTNESS_COUNTER_DEFECT)
    return _oob_with_defect(entry, state, kind)


@pytest.mark.parametrize("kind", INJECTED_DEFECTS)
@pytest.mark.parametrize(
    "entry",
    [e for e in ENTRIES
     if e["expect"] != "raise" and "_error" not in e
     and _inadmissible(e) is None],
    ids=lambda e: e["id"],
)
def test_the_corpus_entry_goes_RED_under_every_injected_defect(
    entry, kind: str
) -> None:
    """THE COUNTER-CASE, in the only form that means anything (BO0).

    A counter-case is the DEFECT whose presence must make the gate red. The
    comparison is to the gate's own ceiling and to nothing else; the margin is
    reported by `test_the_forward_error_is_REPORTED_and_the_floor_is_too` and
    asserted against no constant.

    THE FORM THIS REPLACES WAS WRONG FOR SIX ROUNDS. `1.0e-7`, `1.0e-13` and
    `3.5e-05` were each called a counter while functioning as a floor on the
    RESPONSE, so an entry "failed to detect" when its response fell below a
    constant rather than below the ceiling. At `L/r_min = 2885` the wrong-DOF
    defect responds at `3.5e-06` against a ceiling of `5e-15` -- nine orders of
    detection, reported as a wall.

    THE MINIMA ARE NOT REPEATED HERE (BP0/BI3). They move with every corpus
    round -- the four figures this docstring carried were already refuted by the
    module's own regenerated table by `2.0x` and `7.4x` at the commit that
    published them -- so they are printed by
    `test_the_forward_error_is_REPORTED_and_the_floor_is_too`, which runs, and
    quoted in the step report, which is regenerated by rule.

    The gate fails if ANY state exceeds the ceiling, so detection is the worst
    state.
    """
    delta = injected_delta(entry, kind)
    if kind not in UNCONDITIONALLY_RED and classify(entry, kind) == "below resolution":
        # NOT A PASS AND NOT A SKIP: the pair is classified, every classified
        # pair is printed by `test_the_forward_error_is_REPORTED_and_the_floor_
        # is_too`, and `test_every_entry_carries_at_least_one_LIVE_defect`
        # refuses an entry whose every defect lands here. The gate claims to
        # resolve `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`; a smaller defect is
        # outside that claim, not a failure of it.
        assert delta < PATCH_TEST_EXACTNESS_COUNTER_DEFECT
        return

    worst = max(_oob_with_injected(entry, st, kind) for st in STATES)
    assert worst > PATCH_TEST_EXACTNESS, (
        f"{entry['id']}: the {kind} defect left the interior out-of-balance at "
        f"{worst:.4e}, at or below the ceiling {PATCH_TEST_EXACTNESS:.0e} "
        f"(L/r_min {member_lambda(entry):.1f}). The gate holds here and cannot "
        "fail here."
    )


def test_the_delta_measure_is_CALIBRATED() -> None:
    """The classification is only meaningful if the measure agrees with the claim.

    `classify` compares `injected_delta` against
    `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, which is the size of the counter-defect
    injection. So that injection must measure exactly that size under the same
    definition, or the two sides of the comparison are in different units -- which
    is what the previous `max|K_bad - K_clean| / max|K|` was, dividing a
    bending-block change by the AXIAL stiffness.
    """
    for entry in SOLVED:
        measured = injected_delta(entry, "one_element_scaled")
        # COMPARED ON THE O(1) QUANTITY, which is where the defect actually
        # lives: the injection is `k * (1 + CD)`, and `(1 + CD) - 1` loses
        # `eps/CD ~ 2e-10` of relative precision to cancellation. Comparing the
        # differences directly would be comparing two 1e-6 numbers through that
        # cancellation and would report a 4.5e-12 disagreement that is the
        # arithmetic, not the measure (R38's lesson, in a new place).
        # TO ONE ULP, NOT EXACTLY, AND THE ARGUMENT FOR `==` IS WITHDRAWN
        # (R142). It said the constant "divides out and the result is the same
        # float". It does not: `(CD * x) / x != CD` for 0.19% of random `x` at
        # `CD = 1e-6`, and for 24% at `3.7e-6`. Green here was 89 draws at
        # p = 0.0019 -- about one-in-seven odds of having been red at the commit
        # that published the claim, and a reviewer's corpus entry duly reddened
        # it at the shipped constant. A one-ULP disagreement is rounding, not a
        # units error, and the message said units.
        assert_close(
            measured, PATCH_TEST_EXACTNESS_COUNTER_DEFECT, ROUNDOFF_IDENTITY,
            floor=np.finfo(float).eps * PATCH_TEST_EXACTNESS_COUNTER_DEFECT,
            what=(f"{entry['id']}: the counter-defect injection measures "
                  f"{measured:.17g} under `injected_delta`, against its declared "
                  f"size {PATCH_TEST_EXACTNESS_COUNTER_DEFECT:.17g}. Within one "
                  "ULP this is rounding; beyond it the measure and the claim "
                  "have stopped being the same quantity"),
        )

    # THE OTHER DIRECTION: a bending-only defect of the SAME declared size must
    # measure the block ratio, which is where the lambda^2 suppression enters --
    # from the matrix, not from a declaration.
    stub = min(SOLVED, key=member_lambda)
    slender = max(SOLVED, key=member_lambda)
    ratios = [_bending_only_effective_size(e) / PATCH_TEST_EXACTNESS_COUNTER_DEFECT
              for e in (stub, slender)]
    assert ratios[0] > ratios[1], (
        f"the bending-block ratio does not fall with slenderness: "
        f"{stub['id']} (L/r_min {member_lambda(stub):.0f}) gives {ratios[0]:.3e} "
        f"and {slender['id']} (L/r_min {member_lambda(slender):.0f}) gives "
        f"{ratios[1]:.3e}. The suppression this measure exists to capture is "
        "not in it."
    )
    assert ratios[0] < 1.0, (
        f"a bending-only defect measures {ratios[0]:.3e} of its declared size "
        "even on the stubbiest entry in the corpus; it should be strictly below "
        "1, since the bending block is never the largest stiffness in the element"
    )


def _bending_only_effective_size(entry) -> float:
    """`injected_delta` for a defect confined to the x-y bending block.

    Not a shipped defect -- it is the control that shows the measure carries the
    block ratio, which is the whole reason the metric changed (BR1).
    """
    m, els, stations = _build(entry)
    ell = float(stations[-1])
    e = els[1]
    clean = ORIGINAL_LOCAL_STIFFNESS(e.section, e.material, element_length(m, e))
    change = np.zeros_like(clean)
    idx = [1, 5, 7, 11]
    change[np.ix_(idx, idx)] = (PATCH_TEST_EXACTNESS_COUNTER_DEFECT
                                * clean[np.ix_(idx, idx)])
    denom = float(np.abs(_homogeneous(clean, ell)).max())
    return float(np.abs(_homogeneous(change, ell)).max() / denom)


SAME_MEMBER_DIFFERENT_UNITS = ("unit_mm_similar", "posed_metre",
                               "unit_km_similar")


def _by_id(name: str):
    return next(e for e in SOLVED if e["id"] == name)


def test_the_delta_measure_is_UNIT_INVARIANT() -> None:
    """The same physical member in three length units measures the same defect.

    `injected_delta` normalises by the largest stiffness in the residual's
    homogeneous units, and both of those carry the length unit, so the ratio must
    not. Three corpus entries are the same member at `10^-3`, `1` and `10^3`
    metres, six orders end to end.
    """
    for kind in INJECTED_DEFECTS:
        values = [injected_delta(_by_id(n), kind)
                  for n in SAME_MEMBER_DIFFERENT_UNITS]
        for name, value in zip(SAME_MEMBER_DIFFERENT_UNITS[1:], values[1:]):
            assert_close(
                value, values[0], ROUNDOFF_IDENTITY,
                floor=np.finfo(float).eps * values[0],
                what=(f"{kind}: measured {value:.9e} on {name} against "
                      f"{values[0]:.9e} on {SAME_MEMBER_DIFFERENT_UNITS[0]} -- "
                      "the same member in a different length unit"),
            )


def test_a_CONSTANT_ell_breaks_unit_invariance() -> None:
    """BS3's negative control, in BI1's pattern: the property must be losable.

    `_homogeneous`'s `ell` scales with the model. Freeze it at `1.0` -- the shape
    of the mistake, a characteristic length that does not follow the geometry --
    and the same member in millimetres and in kilometres must stop agreeing. If
    this ever passes, the invariance above is a property of the arithmetic rather
    than of the scaling, and the scaling is unguarded.
    """
    # PATCHED THROUGH `globals()`, NOT THROUGH AN `import` OF THIS FILE. Pytest
    # imports this module under its package-qualified name; `import
    # test_corpus_configurations` inside the test creates a SECOND module object,
    # and patching that one leaves the running code untouched. The first version
    # of this control did exactly that and measured the unpatched function --
    # reporting perfect invariance and failing for the right reason.
    original = globals()["_homogeneous"]
    globals()["_homogeneous"] = lambda k, ell: original(k, 1.0)
    try:
        broken = [injected_delta(_by_id(n), "dropped_flip")
                  for n in SAME_MEMBER_DIFFERENT_UNITS]
    finally:
        globals()["_homogeneous"] = original

    spread = max(broken) / min(broken)
    assert spread > 10.0, (  # not-a-tolerance: discrimination floor -- asserts a separation is LARGE
        f"with `ell` frozen at 1.0 the three unit systems still agree to "
        f"{spread:.4g}x ({broken}). The unit invariance asserted above does not "
        "depend on the scaling it is attributed to, so nothing is guarding it."
    )


def test_an_UNRECOGNISED_defect_name_raises() -> None:
    """BQ2/R126's first control. The builder used to return the CLEAN matrix for
    any name it did not implement, so `injected_delta` reported `0.0` for a defect
    that simply does not exist here -- classification by typo."""
    with pytest.raises(ValueError, match="no defect builder"):
        _defective_stiffness("transposed_transform")
    with pytest.raises(ValueError, match="no defect builder"):
        _defective_stiffness("")


def test_a_NO_OP_defect_classifies_below_resolution() -> None:
    """BQ2/R126's second control: the classification must be able to say `no`.

    `no_op` is a named builder that returns the element unchanged. It is a defect
    of size zero, and zero is the limiting case of "below the declared
    resolution" rather than a branch of its own -- which is what retires the old
    `delta > 0` guard, a guard that passed at `3.497e-301` and could not fire on
    any of the four shipped defects.

    If this ever classified `live`, every below-resolution pair in the suite would
    be one the classification cannot actually reject.
    """
    for entry in SOLVED[:5]:
        assert injected_delta(entry, "no_op") == 0.0
        assert classify(entry, "no_op") == "below resolution"
    # And the meta-half: a real defect on the same entries classifies `live`.
    assert classify(SOLVED[0], "dropped_flip") == "live"


def test_every_entry_carries_at_least_one_LIVE_defect() -> None:
    """BP5's other half: `not injectable` must never become a silent exemption.

    The red-on-defect test above asserts the delta is non-zero for each pair, so
    a dead pair reddens there. This is the aggregate: every entry must have at
    least one live defect, and the total count of live pairs is asserted
    non-empty, so the day the injection machinery breaks it says so in one line
    rather than in 296 identical ones.

    Measured at this commit: every one of the four defects is live on every
    solved entry; the dead-pair count is zero.
    """
    dead: list[str] = []
    live = 0
    for entry in SOLVED:
        alive = [k for k in INJECTED_DEFECTS
                 if injected_delta(entry, k) > 0.0]
        live += len(alive)
        if not alive:
            dead.append(entry["id"])
    assert live > 0, (
        "no (entry, defect) pair changes the assembled matrix at all. The "
        "injection is broken and nothing above it is testing anything."
    )
    assert not dead, (
        f"{sorted(dead)} have no defect that changes their assembled matrix, so "
        "the gate is uncontrolled on them however green they look."
    )


# Bisecting 74 entries costs a few seconds; the two tests that need it get the
# same answer, so it is computed once. A cache is safe here because the corpus and
# the code are both fixed for the duration of a run -- and it is a LIST rather
# than a module constant so that nothing can read a stale value at import.
_EDGE_CACHE: list[tuple[str, float]] = []


def _smallest_detection_edge() -> tuple[str, float]:
    """`(entry id, edge)` for the entry with the SMALLEST detection edge.

    Bisected on every solved entry and the minimum taken. **The selection does
    not use the constant the guard bounds** (R124): the previous version picked
    the entry by its margin at `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, so the edge
    moved with the value it was supposed to bound, the named entry changed five
    times across a sweep, and the published boundary ("any raise of 2.31x or
    more") was wrong -- solved, it was 2.26x..2.28x.

    Ties are broken BY NAME, deterministically, and a tie is reported rather than
    hidden: at the fourteenth verdict the largest edge was an exact two-way tie
    resolved by file order, which is not a property anyone chose (R125).
    """
    if _EDGE_CACHE:
        return _EDGE_CACHE[0]
    edges = sorted((_detection_edge(e), e["id"]) for e in SOLVED)
    smallest = edges[0][0]
    tied = sorted(name for value, name in edges if value == smallest)
    _EDGE_CACHE.append((tied[0], smallest))
    return _EDGE_CACHE[0]


def _detection_edge(entry) -> float:
    """The smallest single-element defect this entry still reddens on.

    Bisected on the gate's OWN rule -- worst state against the ceiling -- because
    that is the decision the gate makes. The response is linear in the defect
    size well above the round-off floor, so the predicate is monotone and the
    bisection is well posed.
    """
    lo, hi = 1e-20, 1e-1
    for _ in range(200):
        mid = (lo * hi) ** 0.5
        if max(_oob_state(entry, st, defect_size=mid)
               for st in STATES) > PATCH_TEST_EXACTNESS:
            hi = mid
        else:
            lo = mid
        if hi / lo < 1.000001:  # not-a-tolerance: bisection convergence, not a comparison of results
            break
    return hi


def test_the_counter_DEFECT_SIZE_cannot_be_raised(capsys) -> None:
    """R115. The constant this round is about had no guard in either direction.

    `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` could be moved from `1e-6` to `1e+6` --
    a defect multiplying one element by a million -- with the whole suite green.
    RAISING IT WEAKENS THE CLAIM: "the gate reddens on a sixth-digit slip" is
    strictly stronger than "the gate reddens on a 100x element". The
    `_COUNTER_DEFECT` form correctly exempts the value from the
    ceiling-below-counter ordering, because a defect size is not in the ceiling's
    quantity, and nothing replaced the guard that exemption removed.

    So the edge is measured rather than assumed: the smallest defect the gate
    still reddens on, bisected at the WORST entry, and the shipped size must sit
    within `PATCH_TEST_COUNTER_HEADROOM` of it.
    """
    worst_id, edge = _smallest_detection_edge()
    ratio = PATCH_TEST_EXACTNESS_COUNTER_DEFECT / edge
    with capsys.disabled():
        print(f"\n  detection edge {edge:.4e} at {worst_id}; shipped defect "
              f"{PATCH_TEST_EXACTNESS_COUNTER_DEFECT:g} is {ratio:.4g}x it, "
              f"against a headroom of {PATCH_TEST_COUNTER_HEADROOM:.3g} "
              f"({PATCH_TEST_COUNTER_HEADROOM / ratio:.2f}x of room)")
    assert ratio <= PATCH_TEST_COUNTER_HEADROOM, (
        f"PATCH_TEST_EXACTNESS_COUNTER_DEFECT = "
        f"{PATCH_TEST_EXACTNESS_COUNTER_DEFECT:g} is {ratio:.4g}x the smallest "
        f"defect this gate still catches ({edge:.4e}, at {worst_id}), above the "
        f"declared headroom {PATCH_TEST_COUNTER_HEADROOM:.3g}. A larger injected "
        "defect is a WEAKER claim, and this is the line that says so."
    )


def test_a_RAISED_counter_defect_breaks_that(capsys) -> None:
    """The guard's own counter, injected (BG1).

    A guard whose only evidence is that it has not fired is not evidence. The
    shipped size is multiplied by `1e3` -- three orders, far inside the range the
    suite tolerated before this test existed -- and the assertion above must fail.
    """
    _, edge = _smallest_detection_edge()
    raised = PATCH_TEST_EXACTNESS_COUNTER_DEFECT * 1.0e3
    ratio = raised / edge
    with capsys.disabled():
        print(f"\n  raised defect {raised:g} is {ratio:.4g}x the edge, "
              f"{ratio / PATCH_TEST_COUNTER_HEADROOM:.1f}x past the headroom")
    assert ratio > PATCH_TEST_COUNTER_HEADROOM, (
        f"multiplying the counter-defect by 1e3 gives {ratio:.4g}x the detection "
        f"edge, which is still within the headroom "
        f"{PATCH_TEST_COUNTER_HEADROOM:.3g}. The guard above would not have "
        "caught it, so it is not a guard."
    )


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
    """Everything the step report quotes about the corpus, produced HERE.

    BI3: a table is regenerated by something committed, or it does not belong in
    a file a reader trusts. This is that something for the corpus figures --
    the ceiling's floor, both formulation controls, and the sensitivity curve's
    residuals -- so the report's tables are shipped-test output rather than a
    scratch harness's.

    The solved field's forward error is printed with them and asserted nowhere:
    it is `cond` x backward error, and no constant survives contact with the axes
    `cond` moves along.
    """
    eps = float(np.finfo(float).eps)
    rows = []
    for e in SOLVED:
        lam = member_lambda(e)
        fwd = max(_measure(e, st)[0] for st in STATES)
        oob = max(_measure(e, st)[1] for st in STATES)
        form = {k: max(_oob_with_injected(e, st, k) for st in STATES)
                for k in INJECTED_DEFECTS}
        # The WEAKEST state under the scaled element -- the quantity the recorded
        # curve describes. The margins above are the worst state, because the
        # gate fails if any state exceeds; the curve is about the state that
        # responds least, which is the one slenderness eats.
        weak = min(_oob_with_injected(e, st, "one_element_scaled")
                   for st in STATES)
        rows.append((e["id"], lam, fwd, oob, form, weak))

    worst = max(rows, key=lambda r: r[3])
    with capsys.disabled():
        print(f"\n  {'id':32} {'L/r_min':>9} {'forward':>11} {'out-of-bal':>11}"
              + "".join(f"{k[:16]:>18}" for k in INJECTED_DEFECTS))
        for i, lam, fwd, oob, form, _w in sorted(rows, key=lambda r: r[1]):
            print(f"  {i:32} {lam:9.1f} {fwd:11.3e} {oob:11.3e}"
                  + "".join(f"{form[k] / PATCH_TEST_EXACTNESS:18.4g}"
                            for k in INJECTED_DEFECTS))

        eps = float(np.finfo(float).eps)
        print(f"\n  CEILING  {PATCH_TEST_EXACTNESS:.3e}   worst clean "
              f"{worst[3]:.4e} ({worst[3] / eps:.2f} eps, {worst[0]}) "
              f"= {worst[3] / PATCH_TEST_EXACTNESS:.4f}x")
        exempt: dict[str, list[str]] = {}
        for e in SOLVED:
            for k in INJECTED_DEFECTS:
                if classify(e, k) == "below resolution":
                    exempt.setdefault(k, []).append(e["id"])
        n_exempt = sum(len(v) for v in exempt.values())
        print(f"  EXEMPT   {n_exempt} of {len(SOLVED) * len(INJECTED_DEFECTS)} "
              f"(entry, defect) pairs are below the declared resolution and "
              f"carry no red assertion: "
              + ", ".join(f"{k} {len(v)}" for k, v in sorted(exempt.items())))
        detected = sum(
            1 for k, ids in exempt.items() for i in ids
            if max(_oob_with_injected(next(e for e in SOLVED if e["id"] == i),
                                      st, k) for st in STATES)
            > PATCH_TEST_EXACTNESS)
        print(f"           of those, {detected} ARE detected by the gate today; "
              "their responses are golden values in "
              "tests/regression/test_exempt_pair_responses.py, so a pair that is "
              "caught now cannot stop being caught in silence (BS2)")
        print("  MARGINS  response / ceiling, reported and asserted against no "
              "constant (BO0):")
        # PER-STATE responses, a DIAGNOSTIC since BP2. The assertion that every
        # state detects was removed -- the gate decides on the worst state, and a
        # min-over-states universal with an edge inside the corpus is stronger
        # than the rule it guards. The numbers stay visible here.
        weak = [(e["id"], member_lambda(e),
                 min(_oob_with_injected(e, st, "one_element_scaled")
                     for st in STATES) / PATCH_TEST_EXACTNESS)
                for e in SOLVED]
        lo_w = min(weak, key=lambda r: r[2])
        below = [w for w in weak if w[2] <= 1.0]
        print(f"  PER-STATE  weakest state / ceiling: minimum {lo_w[2]:.3f}x at "
              f"{lo_w[0]} (L/r_min {lo_w[1]:.1f}); {len(below)} of {len(weak)} "
              "entries below 1.0 -- DIAGNOSTIC, asserted nowhere (BP2)")
        for k in INJECTED_DEFECTS:
            lo = min(rows, key=lambda r: r[4][k])
            print(f"    {k:22} minimum {lo[4][k] / PATCH_TEST_EXACTNESS:12.4g}x"
                  f"   at {lo[0]} (L/r_min {lo[1]:.1f})")
        # The fitted curve is a DIAGNOSTIC and nothing asserts it (BO2). It is
        # regenerated here so the step report's statement of what the gate's
        # sensitivity IS comes from a run rather than from a scratch harness.
        lam = np.array([r[1] for r in rows])
        sml = np.array([r[5] for r in rows])
        fit = np.polyfit(np.log(lam), np.log(sml), 1)
        resid = sml / np.exp(np.polyval(fit, np.log(lam)))
        print(f"  CURVE    weakest-state response = {np.exp(fit[1]):.3e} * "
              f"(L/r_min)^({fit[0]:.3f})   scatter {resid.min():.3f}x .. "
              f"{resid.max():.3f}x   DIAGNOSTIC, asserted nowhere")
        wk = min(rows, key=lambda r: r[5])
        print(f"           weakest state anywhere {wk[5] / PATCH_TEST_EXACTNESS:.3f}x "
              f"the ceiling, at {wk[0]} (L/r_min {wk[1]:.1f})")
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


def test_the_reviewers_EXPECT_survives_a_parse_failure() -> None:
    """R91. The field the per-entry test compares against is not written by the
    thing it is comparing.

    `_error_row` used to write `expect="raise"` unconditionally, so the per-entry
    assertion `expect == "raise"` compared a variable with the constant assigned
    to it eighty lines earlier. A line the reviewer recorded as `hold` that this
    module cannot build read GREEN while measuring nothing -- on the one
    instrument in this repository the implementer does not write.
    """
    line = ("id=probe_hold_unparseable section=circular_tube,D=0.6,t=0.012 "
            "stations=9.67 orient=skew extra=nonsense=1 expect=hold")
    with pytest.raises(CorpusError):
        _parse_line(1, line)

    row = _error_row(1, line, CorpusError("x"))
    assert row["expect"] == "hold", (
        f"the reviewer wrote expect=hold and the row records "
        f"{row['expect']!r}; the module is overwriting the field it is about "
        "to check itself against"
    )
    assert row["id"] == "probe_hold_unparseable"

    # And the per-entry assertion now REDDENS on it, which is the whole point.
    with pytest.raises(AssertionError, match="disagreement is the finding"):
        test_the_corpus_entry_behaves_as_the_reviewer_recorded(row)

    # The meta-test: a line the reviewer DID record as raise still passes.
    ok = _error_row(1, line.replace("expect=hold", "expect=raise"),
                    CorpusError("x"))
    assert ok["expect"] == "raise"

    # A line carrying no `expect` at all is not silently read as "raise" either.
    none = _error_row(1, "id=x section=nonsense", CorpusError("x"))
    assert none["expect"] == "unrecorded"

    # R104: a REPEATED `expect` is not resolved by taking the first one.
    # `_parse_line` refuses duplicates, so `expect=raise expect=hold` reached the
    # per-entry test as "raise" and passed on a contradictory line.
    dup = _error_row(1, line.replace("expect=hold", "expect=raise expect=hold"),
                     CorpusError("x"))
    assert dup["expect"].startswith("AMBIGUOUS"), (
        f"a repeated expect came back as {dup['expect']!r}; taking the first is "
        "as arbitrary as taking the last"
    )
    with pytest.raises(AssertionError, match="disagreement is the finding"):
        test_the_corpus_entry_behaves_as_the_reviewer_recorded(dup)


MULTI_EXTRAS = [
    ("one key", "roll=0.3", {"roll": ["0.3"]}),
    ("two keys", "roll=0.3,I_y_over_I_z=0.5",
     {"roll": ["0.3"], "I_y_over_I_z": ["0.5"]}),
    ("a vector value", "orientation_node=1,0,0",
     {"orientation_node": ["1", "0", "0"]}),
    ("a vector and a scalar", "orientation_node=0,0,1,roll=-1.2",
     {"orientation_node": ["0", "0", "1"], "roll": ["-1.2"]}),
    ("none", "none", {}),
]


@pytest.mark.parametrize("label, text, expected", MULTI_EXTRAS,
                         ids=[e[0] for e in MULTI_EXTRAS])
def test_extra_takes_MORE_THAN_ONE_key(label: str, text: str, expected) -> None:
    """R91's other half: the capability the reviewer asked for and could not write.

    A comma-separated token containing `=` starts a new key; one without
    continues the previous key's value. That resolves `orientation_node=1,0,0`
    and `roll=0.3,I_y_over_I_z=0.5` with the separator the corpus already uses,
    and without a second separator to remember.
    """
    assert _extras(1, text) == expected


BAD_EXTRAS = [
    ("unknown key", "nonsense=3.0"),
    ("the old typo", "roll_rad=1.0"),
    ("no key at all", "0.3,0.4"),
    ("duplicate key", "roll=0.1,roll=0.2"),
    ("too few components", "orientation_node=1,0"),
    ("too many components", "orientation_node=1,0,0,0"),
    ("non-finite", "roll=NaN"),
]


@pytest.mark.parametrize("label, text", BAD_EXTRAS,
                         ids=[e[0] for e in BAD_EXTRAS])
def test_an_extra_that_cannot_be_built_RAISES(label: str, text: str) -> None:
    """Opening the field up did not open a silent default with it."""
    with pytest.raises(CorpusError):
        _extras(1, text)


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
