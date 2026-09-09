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

# IMPORTED AT MODULE LEVEL BECAUSE THE ANNOTATIONS ALREADY NEEDED IT (CA0).
# Three functions imported numpy inside their own bodies while two module-level
# annotations referenced `np.ndarray`, so the name was undefined at the scope
# that used it: the runtime worked, and a type checker resolving the annotation
# could not. `ruff` had never run in CI, which is the only reason it stood.
import numpy as np

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
N_DOF_TOTAL: Final[int] = N_BODIES * 6  # 102
N_DOF_HYDRO: Final[int] = N_HYDRO_BODIES * 6  # 72
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


# ---------------------------------------------------------------------------
# Index-space conversion (Z4).
#
# Asserting N_HYDRO_DOF == 72 does NOT protect the mapping. What bit in practice
# was an index-SPACE confusion: a 72-space index used against a 102-space array,
# where BOTH spaces have a valid entry at 46 -- global 46 lands in hub2, which is
# structural, so the comparison silently returned zero damping and looked like a
# spectacular confirmation of the hypothesis under test.
#
# A count assertion cannot catch that. These helpers make the mapping structural
# rather than remembered: never index across spaces by hand.
# ---------------------------------------------------------------------------

HYDRO_GLOBAL_DOF: Final[tuple[int, ...]] = tuple(
    6 * buoy_body_index(k) + i for k in range(N_HYDRO_BODIES) for i in range(6)
)
"""The 72 GLOBAL DOF indices that carry hydrodynamics, in hydro-subset order."""


def hydro_to_global(j: int) -> int:
    """Global DOF index for hydro-subset index ``j`` (0 <= j < 72)."""
    if not 0 <= j < N_DOF_HYDRO:
        raise IndexError(
            f"hydro index {j} outside [0, {N_DOF_HYDRO}). Passing a GLOBAL index "
            "here is the error this function exists to prevent."
        )
    return HYDRO_GLOBAL_DOF[j]


def global_to_hydro(g: int) -> int:
    """Hydro-subset index for global DOF ``g``. Raises if ``g`` is structural.

    The raise is the point: the hubs and platform have no radiation field, and a
    silent zero from indexing into them is indistinguishable from a physical
    result.
    """
    if not 0 <= g < N_DOF_TOTAL:
        raise IndexError(f"global index {g} outside [0, {N_DOF_TOTAL})")
    try:
        return HYDRO_GLOBAL_DOF.index(g)
    except ValueError:
        raise IndexError(
            f"global DOF {g} is STRUCTURAL (a hub or the platform) and carries no "
            "hydrodynamics. Indexing a 72-space array with it, or a 102-space "
            "array with a hydro index, is the 72-vs-102 trap."
        ) from None


def live_dof(reference: Any) -> np.ndarray:
    """Mask of DOF carrying real signal, excluding structurally dead ones.

    Same treatment as the index-space helpers above, and for the same reason:
    **enforced in code, not held in mind.** The dead-DOF rule was written into
    `docs/instrumentation.md` as the eighth guard and then violated one commit
    later, which is the evidence that recording it is not enough.

    What this prevents
    ------------------
    A body of revolution has no yaw radiation, so yaw ``mu`` on this platform is
    ``1.2e-17`` against ``4.2e-01`` in surge. That is round-off, not a small
    physical quantity. A correlation or norm formed over it computes a statistic
    on noise and reports it as a measurement -- it moved an AG5 correlation from
    ``+0.53`` to ``+0.65``, and nothing in the output said so.

    ``reference`` is the per-DOF magnitude the statistic is formed over (``|mu|``,
    ``|B|``, whatever is being aggregated). The floor is **relative** to the
    largest entry, because "dead" is only meaningful against the scale of the
    live DOF beside it.

    What this does NOT catch
    ------------------------
    Because the floor is relative, the largest entry is always ``1.0`` and so is
    always live. **A uniformly dead set is reported as entirely live.** Comparing
    a quantity that is round-off in *every* DOF -- yaw alone, say -- gets no
    warning from this function, and the caller must supply the physical scale.

    Stated rather than fixed: an absolute floor would need a scale this function
    cannot know, and inventing one would be a fudge factor. The eighth guard
    applies to guards too -- say what the check cannot see.
    """

    from floatfea.tolerances import DEAD_DOF_RELATIVE_FLOOR

    ref = np.abs(np.asarray(reference, dtype=np.float64))
    if ref.ndim != 1:
        raise ValueError(f"reference must be 1-D, one entry per DOF; got {ref.shape}")
    peak = ref.max(initial=0.0)
    if peak == 0.0:
        raise ValueError(
            "every DOF in this reference is exactly zero -- there is no signal to "
            "form a statistic over, and a statistic computed anyway would be "
            "meaningless rather than small."
        )
    live: np.ndarray = ref / peak >= DEAD_DOF_RELATIVE_FLOOR
    return live


def over_live(values: Any, reference: Any, *, what: str) -> np.ndarray:
    """``values`` restricted to the DOF that carry signal.

    Use this wherever a correlation, norm or mean is formed across DOF. Going
    around it is possible; that is what makes it a guard rather than a proof, and
    the raise below is the part worth having -- a fully dead set is an error, not
    an empty aggregate that reduces to ``nan`` and gets read as a small number.
    """

    v = np.asarray(values)
    mask = live_dof(reference)
    if v.shape[0] != mask.size:
        raise ValueError(
            f"{what}: values has {v.shape[0]} entries but the reference names "
            f"{mask.size} DOF -- these must be the same DOF in the same order."
        )
    if not mask.any():
        raise ValueError(
            f"{what}: every DOF is below the dead-DOF floor. A statistic over an "
            "empty set is not a small result, it is no result."
        )
    kept: np.ndarray = v[mask]
    return kept


class Reference:
    """A reference value that carries **how it was obtained** (AK3).

    Third time an interpolated reference manufactured a residual: the first
    pass's nearest-neighbour lookup (8%), the AD2 band comparison, and the AF3
    panel run (`5.914e-04` against a true `1.359e-15` — eleven orders, all
    interpolation).

    The structural point is that this will keep happening. Case frequencies are
    chosen for **physics, not grid alignment**, so they land wherever they land:
    ω=2.000377 sat at **48.6% of its gap** — dead centre, the worst available
    position. That is not bad luck to be avoided next time.

    So the provenance travels with the value, and
    :func:`assert_reference_supports` refuses an interpolated one where the
    tolerance is too tight for it to be distinguishable. Same treatment as the
    index-space helpers and ``live_dof``: eleven orders between the artifact and
    the real error is not something to catch by noticing it looks large.
    """

    __slots__ = ("value", "omega", "interpolated", "gap_fraction", "source")

    def __init__(
        self,
        value: Any,
        *,
        omega: float,
        interpolated: bool,
        source: str,
        gap_fraction: float | None = None,
    ) -> None:
        if interpolated and gap_fraction is None:
            raise ValueError(
                "an interpolated reference must record its gap_fraction -- how far "
                "between grid points it sits is what sets the error it carries."
            )
        self.value = value
        self.omega = float(omega)
        self.interpolated = bool(interpolated)
        self.gap_fraction = gap_fraction
        self.source = source

    def __repr__(self) -> str:  # pragma: no cover - diagnostic only
        how = f"interpolated at {self.gap_fraction:.1%} of gap" if self.interpolated else "exact"
        return f"Reference({self.source}, omega={self.omega:.6f}, {how})"


def interpolated_reference(grid: Any, values: Any, omega: float, *, source: str) -> Reference:
    """Linear interpolation of ``values`` along ``grid`` to ``omega``, flagged.

    Returns an *exact* reference when ``omega`` lands on a grid point, so a
    comparison at a solved frequency is not penalised for using this helper.
    """

    g = np.asarray(grid, dtype=np.float64)
    v = np.asarray(values)
    hit = np.flatnonzero(np.isclose(g, omega, rtol=0.0, atol=1e-12))
    if hit.size:
        return Reference(v[..., int(hit[0])], omega=omega, interpolated=False, source=source)
    k = int(np.clip(np.searchsorted(g, omega), 1, g.size - 1))
    f = (omega - g[k - 1]) / (g[k] - g[k - 1])
    return Reference(
        v[..., k - 1] * (1 - f) + v[..., k] * f,
        omega=omega,
        interpolated=True,
        gap_fraction=float(f),
        source=source,
    )


def assert_reference_supports(reference: Reference, *, tolerance: float, what: str) -> None:
    """Refuse an interpolated reference for a comparison asserting at round-off.

    The failure this prevents is not a wrong number but an **undetectable** one:
    the interpolation error and the quantity under test enter the same scalar,
    and no amount of care reading that scalar separates them.
    """
    from floatfea.tolerances import INTERPOLATED_REFERENCE_TOLERANCE_FLOOR

    if not reference.interpolated:
        return
    if tolerance <= INTERPOLATED_REFERENCE_TOLERANCE_FLOOR:
        raise ValueError(
            f"{what}: comparing at tolerance {tolerance:.3e} against a reference "
            f"INTERPOLATED at {reference.gap_fraction:.1%} of its grid gap "
            f"(omega={reference.omega:.6f}, source={reference.source}). The "
            f"interpolation injects an error the comparison cannot separate from "
            f"what it is measuring -- measured at 5.914e-04 against a true "
            f"1.359e-15 on exactly this case. Compare at a solved frequency, or "
            f"interpolate BOTH sides identically so the error is common-mode."
        )


def assert_comparison_window_is_valid(
    comparison: tuple[float, float],
    **validity: tuple[float, float],
) -> None:
    """Every side of a comparison must be valid across the comparison window.

    Extends the validity-window rule (`docs/instrumentation.md`) from *carrying*
    a window to *asserting containment*. The rule has now appeared five times —
    ``mu``'s warm-up, the truncated stored window, the drift magnitude, the panel
    reference pose, and a comparison window shorter than the kernel memory that
    feeds one of its sides. The fifth is what motivates making it an assertion
    rather than a note.

    ``mu`` is valid only from ``t0 + kernel_memory``; a comparison window that
    starts earlier is comparing a quantity against a prediction it cannot
    satisfy, and the discrepancy looks like physics.
    """
    c0, c1 = comparison
    if c1 <= c0:
        raise ValueError(f"comparison window is empty or reversed: {comparison}")
    bad = {name: win for name, win in validity.items() if not (win[0] <= c0 and c1 <= win[1])}
    if bad:
        detail = "; ".join(f"{n} valid over {w}" for n, w in sorted(bad.items()))
        raise ValueError(
            f"comparison window {comparison} is not contained in every side's "
            f"validity window -- {detail}. A quantity compared outside its "
            "validity window produces a discrepancy that looks like physics."
        )
