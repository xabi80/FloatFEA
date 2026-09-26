#!/usr/bin/env python
"""TWO measurements about the same three defect shapes: what the element-local
diagnostic fails to redden, and what the per-frame `lambda_6` ceiling does.

    python scripts/rigid_counter_response.py

WHY THIS IS A SCRIPT AND NOT A TEST. Neither measurement is asserted anywhere.
Claim A was dropped as an F2 gate (DG2), so the first has no gate to guard and
a test would be a guard without one; the second is the SENSITIVITY of a gate
that does exist, which is a property of the corpus rather than of the code.
`CLAUDE.md` says a figure in a plan, a report or a tolerance comment is
produced by a command at the commit that publishes it. This is that command,
and the plan, the entry and the test comments cite it instead of carrying its
numbers -- because `298 of 1592` was carried, and was stale in the commit that
published it.

The reviewer could not reproduce that count at the sixtieth verdict, and was
right not to accept it: the three counters existed only in the implementer's
scratchpad. A figure whose only witness is a scratch file is a figure with no
witness.

WHAT THE SECOND MEASUREMENT IS FOR (R540). `RIGID_MODE_BOUND` is read in two
directions -- a floor on `lambda_7` and, per frame, a ceiling on `lambda_6`.
The ceiling is EVALUATED at every corpus frame including the ones the spectral
half refuses, and a comment claimed that therefore "the element is under test
everywhere". Evaluated is not sensitive. This script injects each defect shape
into every element's local stiffness AT THE ASSEMBLY SITE, reassembles, and
reports how many frames the ceiling reddens on -- separately for the frames
the spectral half decides and the frames it refuses, which is the split the
claim was made across.

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

import floatfea.assemble.system as SYSTEM  # noqa: E402
from floatfea.assemble.system import assemble_dense, element_length  # noqa: E402
from floatfea.element.beam import local_stiffness  # noqa: E402
from floatfea.tolerances import RIGID_MODE_BOUND, RIGID_MODE_EXACTNESS  # noqa: E402

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

ASSEMBLED_SIZES = (1.0e-8, 1.0e-4)
"""The two sizes the per-frame ceiling is probed at. The first is `SIZE`, so the
two measurements are comparable; the second is four decades up, because a shape
that reddens nothing at the first is worth asking about again before the word
"insensitive" is used.

not-a-tolerance: nothing is compared against either value. They are the sizes of
an injected defect, and the output is a count."""


def frame_response(model, els, kind: str | None, size: float, rbm) -> float:
    """`lambda_6` of the assembled matrix, with `kind` in every element.

    THE PATCH IS AT THE ASSEMBLY SITE and not at `floatfea.element.beam`.
    `assemble_dense` resolved `local_stiffness` through its own module's
    namespace, so patching the definition's home injects nothing at all and the
    measurement reads "no defect" on a defect that was never applied. The
    reviewer's first cell did exactly that.
    """
    if kind is None:
        return float(rbm.largest_rigid_eigenvalue(assemble_dense(model, els)))
    original = SYSTEM.local_stiffness

    def patched(section, material, length):
        return injected(original(section, material, length), kind, size)

    SYSTEM.local_stiffness = patched
    try:
        return float(rbm.largest_rigid_eigenvalue(assemble_dense(model, els)))
    finally:
        SYSTEM.local_stiffness = original


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

    # ---------------------------------------------------------------- R540
    print()
    print("THE PER-FRAME lambda_6 CEILING, split by the gate's own domain:")
    decided, refused = [], []
    for entry in rbc.ENTRIES:
        try:
            model, els = rbc._build(entry)
        except Exception:
            continue
        k = assemble_dense(model, els)
        over = rbm.seventh_over_epsilon(k)
        (decided if over >= RIGID_MODE_BOUND else refused).append((entry, model, els))
    print(
        f"  the spectral half decides {len(decided)} frames and refuses "
        f"{len(refused)}; the ceiling is evaluated at all "
        f"{len(decided) + len(refused)}"
    )
    for size in ASSEMBLED_SIZES:
        print(f"  injected at {size:g} of max|k_e| into EVERY element:")
        for kind in KINDS:
            counts = []
            for label, half in (("decided", decided), ("refused", refused)):
                red = sum(
                    1
                    for _entry, model, els in half
                    if frame_response(model, els, kind, size, rbm) >= RIGID_MODE_BOUND
                )
                counts.append(f"{label} {red:4d} of {len(half):4d}")
            print(f"    {kind:18s} " + "   ".join(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
