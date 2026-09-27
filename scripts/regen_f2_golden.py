#!/usr/bin/env python
"""Regenerate V6.1's golden for what F2 ships.

    python scripts/regen_f2_golden.py

`CLAUDE.md` § Testing: regenerating a golden file to match new output, without a
written explanation of why the numbers moved, is the same error as widening a
tolerance. This script exists so the file is PRODUCED rather than typed, not so
it is cheap to overwrite.

WHAT IS IN IT, AND WHAT IS DELIBERATELY NOT. Every recorded quantity is a
scalar invariant of a matrix F2 ships -- a trace, a Frobenius norm, a specific
entry, a rigid-body quadratic form. Those are stable summaries: a change in any
element formulation, transformation, condensation or link moves at least one of
them, and none of them depends on the ORDER a solver happened to visit
eigenvalues in.

**Frequencies are not recorded.** They come out of `eigh`, whose last bits differ
between LAPACK builds, and a golden is checked on two platforms here -- Windows
locally and Linux on CI. Recording them at a tolerance loose enough to survive
that would record almost nothing; recording them tighter would redden on a
platform difference that the determinism legs exist to measure separately. The
cross-platform drift is a measurement, not a guess, and until it is taken V6.1
covers the matrices and the verification tests cover the frequencies.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from floatfea import basis  # noqa: E402
from floatfea.assemble.system import (  # noqa: E402
    BeamElement,
    assemble_dense,
    assemble_mass_dense,
)
from floatfea.element.beam import local_mass, local_stiffness  # noqa: E402
from floatfea.element.constraints import (  # noqa: E402
    constraint_transform,
    reduce_matrix,
    rigid_link_block,
)
from floatfea.element.releases import (  # noqa: E402
    condense,
    gimbal_release,
    recovery_matrix,
)
from floatfea.model.material import Material, Section  # noqa: E402
from floatfea.model.nodes import Model, Node, NodeSet  # noqa: E402

GOLDEN = ROOT / "tests" / "regression" / "f2_shipped_matrices.json"

STEEL = Material(E=2.1e11, nu=0.3, rho=7850.0, fy=355.0e6, name="S355")


def tube(d_outer: float, t: float) -> Section:
    inertia = basis.tube_second_moment(d_outer, t)
    return Section(
        A=basis.tube_area(d_outer, t),
        I_y=inertia,
        I_z=inertia,
        J=basis.torsion_constant("thin_tube", inertia, inertia),
        shape="thin_tube",
    )


def invariants(name: str, matrix: np.ndarray) -> dict[str, float]:
    """Scalar summaries of a matrix: trace, Frobenius norm, and its extreme entry.

    Three and not one, because a single summary can be insensitive to a real
    change: a trace misses an off-diagonal sign flip, and a Frobenius norm misses
    a transposition. The extreme entry catches a change in scale that both could
    average away.
    """
    m = np.asarray(matrix, dtype=np.float64)
    flat = m.ravel()
    extreme = flat[int(np.argmax(np.abs(flat)))]
    return {
        f"{name}|trace": float(np.trace(m)),
        f"{name}|frobenius": float(np.linalg.norm(m)),
        f"{name}|extreme_entry": float(extreme),
    }


def rigid_forms(name: str, m: np.ndarray, length: float) -> dict[str, float]:
    """The six rigid-body quadratic forms of a 12x12 element mass matrix."""
    half = length / 2.0
    vectors: dict[str, np.ndarray] = {}
    for axis, label in ((0, "ux"), (1, "uy"), (2, "uz")):
        v = np.zeros(12)
        v[axis] = 1.0
        v[6 + axis] = 1.0
        vectors[label] = v
    twist = np.zeros(12)
    twist[3] = twist[9] = 1.0
    vectors["rx"] = twist
    rz = np.zeros(12)
    rz[1], rz[5], rz[7], rz[11] = -half, 1.0, half, 1.0
    vectors["rz"] = rz
    ry = np.zeros(12)
    ry[2], ry[4], ry[8], ry[10] = half, 1.0, -half, 1.0
    vectors["ry"] = ry
    return {f"{name}|rigid_{label}": float(v @ m @ v) for label, v in vectors.items()}


def collect() -> dict[str, float]:
    out: dict[str, float] = {}

    # The element, at three spans and two sections.
    for d_outer, thickness in ((0.6, 0.012), (0.3, 0.008)):
        section = tube(d_outer, thickness)
        tag = f"D{d_outer:g}_t{thickness:g}"
        for length in (1.0, 4.0, 60.0):
            k = local_stiffness(section, STEEL, length)
            m = local_mass(section, STEEL, length)
            out.update(invariants(f"k_local|{tag}|L{length:g}", k))
            out.update(invariants(f"m_local|{tag}|L{length:g}", m))
            out.update(rigid_forms(f"m_local|{tag}|L{length:g}", m, length))

    # The release, including DJ0's gimbal, on one representative member.
    section = tube(0.4, 0.010)
    length = 4.0
    k = local_stiffness(section, STEEL, length)
    m = local_mass(section, STEEL, length)
    for label, released in (
        ("pin_b_z", (11,)),
        ("pin_a_y", (4,)),
        ("gimbal_b_locked_x", gimbal_release("b", "x")),
        ("gimbal_a_locked_z", gimbal_release("a", "z")),
    ):
        recovery = recovery_matrix(k, released)
        out.update(invariants(f"k_released|{label}", condense(k, recovery)))
        out.update(invariants(f"m_released|{label}", condense(m, recovery)))
        out.update(invariants(f"recovery|{label}", recovery))

    # The rigid link.
    for offset in ((1.0, 0.0, 0.0), (0.7, -1.3, 2.9)):
        tag = "_".join(f"{v:g}" for v in offset)
        out.update(invariants(f"link_block|{tag}", rigid_link_block(np.array(offset))))

    # An assembled frame, with and without a link.
    nodes = NodeSet()
    for x, y, z in ((0.0, 0.0, 0.0), (4.0, 0.0, 0.0), (8.0, 0.0, 0.0), (8.0, 1.5, 0.6)):
        nodes.add(Node(x=x, y=y, z=z))
    model = Model(nodes=nodes)
    els = [
        BeamElement(node_a=0, node_b=1, section=section, material=STEEL),
        BeamElement(node_a=1, node_b=2, section=section, material=STEEL),
    ]
    k_sys = assemble_dense(model, els)
    m_sys = assemble_mass_dense(model, els)
    out.update(invariants("k_system|three_node_frame", k_sys))
    out.update(invariants("m_system|three_node_frame", m_sys))

    offset = model.nodes[3].xyz - model.nodes[2].xyz
    t = constraint_transform(model.n_dof, {3: (2, offset)})
    out.update(invariants("k_system|link_reduced", reduce_matrix(k_sys, t)))
    out.update(invariants("m_system|link_reduced", reduce_matrix(m_sys, t)))
    return out


def main() -> int:
    values = collect()
    GOLDEN.write_text(
        json.dumps({k: values[k] for k in sorted(values)}, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{GOLDEN.relative_to(ROOT).as_posix()}: {len(values)} recorded quantities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
