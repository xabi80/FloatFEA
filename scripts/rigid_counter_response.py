#!/usr/bin/env python
"""The measurement DG2's decision rests on: how many elements the element-local
counters fail to redden.

    python scripts/rigid_counter_response.py

WHY THIS IS A SCRIPT AND NOT A TEST. It measures a quantity nothing asserts:
claim A was dropped as an F2 gate, so there is no gate here to guard and a test
would be a guard without one. What the plan cites is a NUMBER -- 298 of 1592 --
and `CLAUDE.md` says a figure in the plan is produced by a command at the
commit that publishes it. This is that command.

The reviewer could not reproduce 298 at the sixtieth verdict, and was right not
to accept it: the three counters existed only in the implementer's scratchpad.
A figure whose only witness is a scratch file is a figure with no witness.

WHAT IT MEASURES. For every distinct element in the rigid-body corpus --
distinct by (length, A, I_y, I_z, J, E, nu), because two tubes can share an
area and differ in I -- inject each of three defects into the element's own
local stiffness and ask whether the element-local rigid residual crosses
`RIGID_MODE_EXACTNESS`:

  * `dropped_flip`      a sign error on one bending coupling
  * `wrong_dof_index`   a coupling written into the neighbouring DOF
  * `rotational_block`  a perturbed torsional diagonal

each as a fraction of the largest entry of `k_e`, which is this repository's
counter-as-injection convention.

WHAT IT DOES NOT DO: decide anything. It prints.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from floatfea.assemble.system import element_length  # noqa: E402
from floatfea.element.beam import local_stiffness  # noqa: E402
from floatfea.tolerances import RIGID_MODE_EXACTNESS  # noqa: E402

SIZE = 1.0e-8
"""The injected size, as a fraction of `max|k_e|`. Chosen once and not tuned:
the point of the measurement is how many elements this does NOT reach, so a
size picked to make the count small would be picking the answer."""


def _module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def injected(k: np.ndarray, kind: str, size: float) -> np.ndarray:
    """A fraction `size` of the largest entry, at the site `kind` names."""
    out = k.copy()
    big = float(np.abs(k).max())
    if kind == "dropped_flip":
        out[1, 5] -= size * big
        out[5, 1] = out[1, 5]
    elif kind == "wrong_dof_index":
        out[0, 7] += size * big
        out[7, 0] = out[0, 7]
    elif kind == "rotational_block":
        out[3, 3] += size * big
    else:
        raise SystemExit(f"unknown counter {kind!r}")
    return out


KINDS = ("dropped_flip", "wrong_dof_index", "rotational_block")


def main() -> int:
    rbc = _module("rbc", "tests/verification/rung1/test_rigid_body_corpus.py")
    rbm = _module("rbm", "tests/verification/rung1/test_rigid_body_modes.py")

    elements: dict[tuple, tuple[np.ndarray, float, str]] = {}
    for entry in rbc.ENTRIES:
        try:
            model, els = rbc._build(entry)
        except Exception:  # a frame the builder refuses is not this measurement's
            continue
        for el in els:
            length = element_length(model, el)
            section = el.section
            key = (
                length,
                section.A,
                section.I_y,
                section.I_z,
                section.J,
                el.material.E,
                el.material.nu,
            )
            if key not in elements:
                elements[key] = (
                    local_stiffness(section, el.material, length),
                    length,
                    entry.get("id", "?"),
                )

    clean: list[tuple[float, str]] = []
    failures: dict[str, list[tuple[float, str]]] = {k: [] for k in KINDS}
    any_fail = 0
    for k_local, length, frame in elements.values():
        clean.append((rbm.element_rigid_residual(k_local, length), frame))
        misses = 0
        for kind in KINDS:
            response = rbm.element_rigid_residual(injected(k_local, kind, SIZE), length)
            if response <= RIGID_MODE_EXACTNESS:
                failures[kind].append((response / RIGID_MODE_EXACTNESS, frame))
                misses += 1
        any_fail += 1 if misses else 0

    worst_clean = max(clean)
    print(f"{len(elements)} distinct elements over the rigid-body corpus")
    print(
        f"clean worst {worst_clean[0]:.4e} = "
        f"{worst_clean[0] / float(np.finfo(np.float64).eps):.3f} eps at {worst_clean[1]}"
    )
    print(
        f"clean clears {RIGID_MODE_EXACTNESS:.0e} by "
        f"{RIGID_MODE_EXACTNESS / worst_clean[0]:.3f}x"
    )
    print()
    print(f"injected at {SIZE:g} of max|k_e|:")
    for kind in KINDS:
        missed = failures[kind]
        if missed:
            low = min(missed)
            print(
                f"  {kind:18s} {len(missed):4d} elements not reddened; "
                f"minimum {low[0]:.4e}x the ceiling at {low[1]}"
            )
        else:
            print(f"  {kind:18s} reddens every element")
    print()
    print(f"ELEMENTS FAILING AT LEAST ONE COUNTER: {any_fail} of {len(elements)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
