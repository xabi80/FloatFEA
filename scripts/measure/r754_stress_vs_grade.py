#!/usr/bin/env python
"""R754's controlled cell: which predicate stands in front of a REDUCED STRESS.

    python scripts/measure/r754_stress_vs_grade.py

ONE VARIABLE (BG0): whether the funnel in front of `column_slenderness_parameter`'s
argument is the plausible-GRADE range `_require_plausible_fy` -- the C72 repair as it
shipped at `5c71cb4` -- or the plausible-STRESS range `_require_plausible_stress`. Held:
the grid, the module, the six declared grades, and the `D/t` range the clause admits.

Nothing is patched. `allowable_axial_compression` calls `local_buckling_stress` and then
`column_slenderness_parameter(F_xc, E)`, so the two predicates are asked the same question
about the same `F_xc` the module itself computes, which is the whole of the difference.

WHY A SCRIPT AND NOT A SENTENCE. The denying figure in the commit that introduced the
defect was `F_xc = 242.39 MPa` at `D/t = 300`, `1.21x` of margin -- correct at S355 and a
function of the grade. A cell that sweeps the grid cannot be right at one configuration
and wrong at the others, which is what EU1/R694 asks of a constant.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from floatfea.checks.api_wsd import (  # noqa: E402
    _require_plausible_fy,
    _require_plausible_stress,
    local_buckling_stress,
)
from floatfea.tolerances import (  # noqa: E402
    F6_API_FY_PLAUSIBLE_MIN,
    F6_API_STRESS_PLAUSIBLE_MIN,
)

E = 210e9
D = 2.5
GRADES = (235e6, 275e6, 355e6, 420e6, 460e6, 690e6)
DT_LO, DT_HI, DT_STEP = 5.00, 300.00, 0.01


def _raises(predicate, value: float) -> bool:
    try:
        predicate(value)
    except ValueError:
        return True
    return False


def main() -> int:
    print(
        f"grid: {len(GRADES)} declared grades x D/t in "
        f"[{DT_LO:.2f}, {DT_HI:.2f}] step {DT_STEP:.2f}"
    )
    print(f"held: the module, the grid, E = {E:.3e} Pa, D = {D} m")
    print("moved: the predicate in front of column_slenderness_parameter's argument")
    print()
    print(
        f"{'predicate':34s} {'floor [MPa]':>12s} {'refused':>9s} {'of':>7s} "
        f"{'fraction':>9s} {'binding F_xc [Pa]':>22s}"
    )

    cells = (
        ("_require_plausible_fy   (GRADE)", _require_plausible_fy, F6_API_FY_PLAUSIBLE_MIN),
        (
            "_require_plausible_stress (STRESS)",
            _require_plausible_stress,
            F6_API_STRESS_PLAUSIBLE_MIN,
        ),
    )
    for label, predicate, floor in cells:
        total = refused = 0
        binding = float("inf")
        for fy in GRADES:
            steps = round((DT_HI - DT_LO) / DT_STEP) + 1
            for i in range(steps):
                d_over_t = DT_LO + i * DT_STEP
                f_xc = local_buckling_stress(D, D / d_over_t, fy, E)
                total += 1
                if _raises(predicate, f_xc):
                    refused += 1
                else:
                    binding = min(binding, f_xc)
        print(
            f"{label:34s} {floor / 1e6:12.1f} {refused:9d} {total:7d} "
            f"{refused / total:8.3%} {binding:22.10e}"
        )

    print()
    print("the binding value MOVES between the cells, and that is the point: under the")
    print("grade predicate the points below 200 MPa are the ones being refused, so its")
    print("binding figure measures the defect and not the clause.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
