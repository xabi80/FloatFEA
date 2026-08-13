"""The single source of truth for frame and convention definitions.

**This module is the source. `docs/conventions.md`'s frame section is generated
from it.** Not the other way round, and not two artifacts held together by a
test.

Why this direction
------------------
Gate **G0.2** originally asked for a machine-readable copy "generated from, or
tested against" the document. Both halves of that are worse than they look:

*Tested against* leaves two hand-maintained artifacts and a test holding them
together — which works until someone edits one and updates the test to match,
at which point the test certifies the drift instead of catching it. The failure
mode is the same as a vacuous negative control.

*Generated from* the document means parsing prose, which is fragile in the
direction that matters: a formatting change silently alters a frame definition.

So the direction is inverted. The **data lives here**, the prose is rendered
from it, and `tests/verification/rung3/test_conventions_are_generated.py` fails
if the committed document does not match what this module renders. Drift is not
detected — it is impossible, because there is only one place to state a value.

What is NOT here
----------------
Anything still UNRESOLVED in `docs/conventions.md` stays unresolved there, in
prose, and is deliberately absent from this module. A machine-readable file that
carried a placeholder would let the validator check a record against a value
nobody had decided.
"""

from __future__ import annotations

from typing import Any, Final

# ---------------------------------------------------------------------------
# Units. FloatSim's gravity, NOT standard gravity -- cluster_common.py:26 sets
# 9.81, and a mismatch surfaces downstream as an unexplained mass error hunted
# in the wrong place.
# ---------------------------------------------------------------------------
UNITS: Final[dict[str, str]] = {
    "length": "m",
    "mass": "kg",
    "time": "s",
    "force": "N",
    "moment": "N*m",
    "angle": "rad",
    "stress": "Pa",
}

GRAVITY_MAGNITUDE: Final[float] = 9.81
GRAVITY_VECTOR: Final[tuple[float, float, float]] = (0.0, 0.0, -GRAVITY_MAGNITUDE)
WATER_DENSITY: Final[float] = 1025.0

# ---------------------------------------------------------------------------
# Global frame.
# ---------------------------------------------------------------------------
GLOBAL_FRAME: Final[dict[str, Any]] = {
    "origin": "platform geometric centre",
    "z_up": True,
    "vertical_datum": "still_water_level",
    "handedness": "right",
    # heading 0 propagates along +X, direction-of-travel -- waves/regular.py:56-59
    # and excitation.py:50; Capytaine agrees, readers/capytaine.py:191-194.
    "heading_zero_axis": "+x",
    "heading_is_direction_of_travel": True,
}

# ---------------------------------------------------------------------------
# Body frames. Origin at the body REFERENCE POINT, not the CoG -- the two are
# 37.0 mm apart on this platform and FloatSim assumes they coincide.
# ---------------------------------------------------------------------------
BODY_FRAME: Final[dict[str, Any]] = {
    "origin": "body_reference_point",
    "axes_at_rest": "parallel_to_global",
    "moment_reference": "body_reference_point",
    "inertia_reference_point_required": True,
}

# ---------------------------------------------------------------------------
# Rotations. FloatSim reads xi[3:6] three ways across its own modules; they
# agree only to first order, so the interpretation is PER CHANNEL GROUP.
# ---------------------------------------------------------------------------
ROTATION_PARAMETERISATIONS: Final[tuple[str, ...]] = (
    "zyx_intrinsic_euler",
    "rotation_vector",
    "linearised",
)

ROTATION_BY_PRODUCER: Final[dict[str, str]] = {
    "morison_drag": "zyx_intrinsic_euler",
    "plate_drag": "zyx_intrinsic_euler",
    "strips": "zyx_intrinsic_euler",
    "patches": "zyx_intrinsic_euler",
    "joints": "rotation_vector",
    "hydrostatic_restoring": "linearised",
}

ROTATION_DIRECTION: Final[str] = "body_to_global"

# ---------------------------------------------------------------------------
# Timestamps and conventions the reader must honour.
# ---------------------------------------------------------------------------
TIME_ALIGNMENTS: Final[tuple[str, ...]] = ("state_n", "external_n_plus_1")
MU_TREATMENTS: Final[tuple[str, ...]] = ("lagged_unblended",)
TIME_CONVENTIONS: Final[tuple[str, ...]] = ("exp_minus_i_omega_t", "exp_plus_i_omega_t")
JACOBIAN_EVALUATIONS: Final[tuple[str, ...]] = ("step_midpoint",)

# ---------------------------------------------------------------------------
# Numbering. Deck order is [3 buoys, 1 hub] per cluster, platform last.
# ---------------------------------------------------------------------------
N_BODIES: Final[int] = 17
N_HYDRO_BODIES: Final[int] = 12
N_DOF_TOTAL: Final[int] = N_BODIES * 6          # 102
N_DOF_HYDRO: Final[int] = N_HYDRO_BODIES * 6    # 72
N_JOINTS: Final[int] = 16
JOINT_CONSTRAINT_ROWS: Final[int] = 4
N_DOF_FREE: Final[int] = N_DOF_TOTAL - N_JOINTS * JOINT_CONSTRAINT_ROWS  # 38
PLATFORM_BODY_INDEX: Final[int] = 16


def buoy_body_index(buoy_k0: int) -> int:
    """Deck body index of buoy ``k`` (0-based). Clusters occupy 4 slots each."""
    if not 0 <= buoy_k0 < N_HYDRO_BODIES:
        raise ValueError(f"buoy index must be in [0, {N_HYDRO_BODIES}); got {buoy_k0}")
    c, b = divmod(buoy_k0, 3)
    return 4 * c + b


def render_markdown() -> str:
    """Render the frame section of ``docs/conventions.md`` from this module.

    The committed document must match this exactly; the rung-3 test enforces it.
    Edit **this module**, then regenerate — editing the prose will fail the test
    with a diff rather than silently diverging.
    """
    lines: list[str] = [
        "<!-- GENERATED FROM floatfea/io/frames.py -- DO NOT EDIT BY HAND -->",
        "",
        "| quantity | value |",
        "|---|---|",
        f"| Gravity | {GRAVITY_VECTOR} m/s^2 (magnitude {GRAVITY_MAGNITUDE}, "
        "FloatSim's value, **not** 9.80665) |",
        f"| Water density | {WATER_DENSITY} kg/m^3 |",
        f"| Global origin | {GLOBAL_FRAME['origin']} |",
        f"| Vertical datum | {GLOBAL_FRAME['vertical_datum']}, z up, "
        f"{GLOBAL_FRAME['handedness']}-handed |",
        f"| Heading 0 | propagates along {GLOBAL_FRAME['heading_zero_axis']}, "
        "direction of travel |",
        f"| Body frame origin | {BODY_FRAME['origin']} (**not** the CoG) |",
        f"| Moment reference | {BODY_FRAME['moment_reference']} |",
        f"| Rotation direction | {ROTATION_DIRECTION} |",
        f"| Bodies / DOF | {N_BODIES} bodies, {N_DOF_TOTAL} DOF, "
        f"{N_JOINTS} joints x {JOINT_CONSTRAINT_ROWS} rows, "
        f"**{N_DOF_FREE} free** |",
        f"| Hydro DOF | {N_DOF_HYDRO} ({N_HYDRO_BODIES} buoys x 6; hubs and "
        "platform are structural) |",
        "",
        "Rotation parameterisation **per producing module**:",
        "",
        "| producer | parameterisation |",
        "|---|---|",
    ]
    lines += [f"| `{k}` | `{v}` |" for k, v in ROTATION_BY_PRODUCER.items()]
    lines += [
        "",
        "<!-- END GENERATED -->",
    ]
    return "\n".join(lines)
