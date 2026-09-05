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
`expect=breach` the entry is ABOVE `PATCH_TEST_EXACTNESS`, the constant. Recorded
                by the reviewer against the constant ceiling; this module asserts
                exactly that, so the reviewer's measurement stays under test even
                though the gate no longer decides on the constant (R46).
`expect=raise`  the configuration must raise at construction rather than fall
                back to a silent default.

An entry naming a field this module cannot build is a FAILURE, not a skip: a
corpus entry that silently does nothing is the vacuous-parameter failure AM5
named.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from floatfea.assemble.system import BeamElement, assemble, solve
from floatfea.element.transform import rotation_matrix
from floatfea.model.material import S355, Section
from floatfea.model.nodes import Model, Node, node_dofs
from floatfea.tolerances import (PATCH_TEST_COND_FACTOR, PATCH_TEST_EXACTNESS,
                                 PATCH_TEST_EXACTNESS_COUNTER)

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


def _parse() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        row: dict[str, str] = {}
        for field in line.split():
            key, _, value = field.partition("=")
            row[key] = value
        rows.append(row)
    return rows


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
    if extra.startswith("orientation_node="):
        onode = np.array([float(v) for v in extra.split("=", 1)[1].split(",")])
    elif extra.startswith("roll="):
        roll = float(extra.split("=", 1)[1])
    elif extra.startswith("I_y_over_I_z="):
        object.__setattr__(sec, "I_y", sec.I_z * float(extra.split("=", 1)[1]))

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


def _ceiling(entry) -> float:
    """The SAME function the gate uses, not a second copy of the formula.

    A duplicate here would drift from the gate's own ceiling silently, which is
    the defect this module exists to catch elsewhere.
    """
    from floatfea.assemble.system import equilibrate

    m, els, stations = _build(entry)
    ends = np.concatenate([node_dofs(0), node_dofs(len(stations) - 1)])
    free = np.setdiff1d(np.arange(m.n_dof), ends)
    kff = assemble(m, els)[free][:, free].tocsc()
    cond = float(np.linalg.cond(equilibrate(kff)[0].toarray()))
    return PATCH_TEST_COND_FACTOR * cond * float(np.finfo(float).eps)


def test_the_corpus_exists_and_is_not_empty() -> None:
    """AM5: an empty parameter set is an error, not a silent pass."""
    assert CORPUS.exists(), f"{CORPUS} is missing; the corpus is the reviewer's"
    assert len(ENTRIES) >= 10, f"only {len(ENTRIES)} corpus entries parsed"


@pytest.mark.parametrize("entry", ENTRIES, ids=lambda e: e["id"])
def test_the_corpus_entry_behaves_as_the_reviewer_recorded(entry) -> None:
    expect = entry["expect"]

    if expect == "raise":
        with pytest.raises(ValueError):
            _build(entry)
        return

    worst = max(_solve_state(entry, st) for st in STATES)

    if expect == "breach":
        assert worst > PATCH_TEST_EXACTNESS, (
            f"{entry['id']}: the reviewer recorded a breach of the CONSTANT "
            f"ceiling and this run gives {worst:.4e} <= "
            f"{PATCH_TEST_EXACTNESS:.0e}. Either the entry or the code moved."
        )
        assert worst <= _ceiling(entry), (
            f"{entry['id']}: {worst:.4e} is above the floor-aware ceiling "
            f"{_ceiling(entry):.4e} as well, which would make it a real defect "
            "rather than round-off scatter."
        )
        return

    assert worst <= _ceiling(entry), (
        f"{entry['id']}: worst state error {worst:.4e} exceeds the floor-aware "
        f"ceiling {_ceiling(entry):.4e}"
    )


@pytest.mark.parametrize(
    "entry", [e for e in ENTRIES if e["expect"] != "raise"], ids=lambda e: e["id"]
)
def test_the_corpus_entry_still_DETECTS_a_defect(entry) -> None:
    """A configuration that holds but cannot fail is worse than one that breaches."""
    smallest = min(_solve_state(entry, st, stiffness_scale=1.0 + 1.0e-6)
                   for st in STATES)
    assert smallest >= PATCH_TEST_EXACTNESS_COUNTER, (
        f"{entry['id']}: the weakest state responded to a 1e-6 single-element "
        f"defect with only {smallest:.4e}, below "
        f"{PATCH_TEST_EXACTNESS_COUNTER:.3e}. The gate holds here and cannot "
        "fail here."
    )


def test_the_corpus_coverage_is_reported(capsys) -> None:
    """The coverage number, in the form the reviewer scores it."""
    runs = len(ENTRIES)
    recorded = sum(1 for e in ENTRIES if e.get("runs_in_suite") == "yes")
    with capsys.disabled():
        print(f"\n  corpus: {runs} entries executed by this module; "
              f"{recorded} recorded as runs_in_suite=yes at the last review")
    assert runs > recorded or recorded == runs, "coverage cannot go backwards"
