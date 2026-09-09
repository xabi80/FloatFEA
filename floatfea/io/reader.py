"""Reader and validator for the `.flr` load interchange record, schema v1.2.

**The reader rejects. It never warns and continues.** A structure analysed under
misinterpreted loads is the failure mode this whole project is built to prevent,
so every fault below is fatal and carries a message naming the specific fault —
gate **G1.2**.

Two properties the rejection set is designed for
------------------------------------------------
**Every rejection is paired with a positive control.** A validator that rejects
everything passes every rejection test, which is the same shape as a negative
control on a degenerate fixture: it certifies nothing while reading green. The
matrix in `tests/verification/rung4/` asserts both directions.

**No two faults share a message.** The easy implementation collapses several
faults into one generic "invalid record", which satisfies "it rejected" while
destroying the diagnostic value G1.2 asks for. Each fault carries a distinct
`Fault` tag and the test suite asserts distinctness across the whole matrix.

What the validator holds, and what the record holds
---------------------------------------------------
The rotation validity bound is **declared by the record**, not held here. The
validator enforces whatever the record declares; Q2 decides what the exporter
*should* declare. That split is what makes the rejection implementable while the
physics question is still open — and it is why a record that fails to declare a
bound is rejected as firmly as one that exceeds it. Omitting the field must not
be a way to pass by having made no claim.
"""

from __future__ import annotations

import json
from enum import Enum
from typing import Any, Final

import numpy as np

from floatfea.io.frames import (
    GRAVITY_MAGNITUDE,
    MU_TREATMENTS,
    ROTATION_PARAMETERISATIONS,
    TIME_ALIGNMENTS,
    TIME_CONVENTIONS,
)

SUPPORTED_SCHEMA: Final[str] = "1.2"

_REQUIRED_UNITS: Final[frozenset[str]] = frozenset({"length", "mass", "time", "force", "angle"})
_REQUIRED_INTEGRATOR: Final[frozenset[str]] = frozenset(
    {"scheme", "rho_inf", "alpha_m", "alpha_f", "beta", "gamma", "dt", "mu_treatment"}
)


class Fault(Enum):
    """One tag per rejection. Distinctness is asserted by the test matrix."""

    SCHEMA_VERSION = "unsupported schema_version"
    UNITS_MISSING = "missing or partial units block"
    PROVENANCE_MISSING = "missing hsp_git_sha or run_id"
    GRAVITY_MISMATCH = "gravity disagrees with FloatSim"
    INTEGRATOR_INCOMPLETE = "missing or partial integrator block"
    TIME_CONVENTION_MISSING = "missing or unrecognised time_convention"
    MU_TREATMENT_UNKNOWN = "unrecognised mu_treatment"
    TIME_NON_UNIFORM = "non-uniform or non-monotonic time base"
    NON_FINITE = "NaN or inf in a channel"
    ROTATION_PARAM_MISSING = "missing rotation_parameterisation"
    ROTATION_BOUND_MISSING = "missing rotation_validity_bound"
    ROTATION_BOUND_EXCEEDED = "rotation exceeds the declared validity bound"
    TIME_ALIGNMENT_MISSING = "missing time_alignment"
    INERTIA_REFERENCE_MISSING = "missing inertia_reference_point"
    INERTIA_NOT_SPD = "inertia tensor is not symmetric positive definite"
    JACOBIAN_EVAL_MISSING = "missing jacobian_evaluation"
    MU_WARMUP = "record lies inside the mu warm-up region"
    UNKNOWN_BODY = "load or joint references a body absent from /bodies"


class FlrValidationError(ValueError):
    """A specific, named rejection. Never a generic 'invalid record'.

    **Not a frozen dataclass, and it must not become one again.** It was one, and
    that is a defect rather than a style choice: Python assigns ``__traceback__``
    on an exception as it propagates, and a frozen dataclass forbids the
    assignment. The failure is not a clean error but a *substitution* --
    ``FrozenInstanceError: cannot assign to field '__traceback__'`` arrives in
    place of the named fault, so the diagnostic this class exists to deliver is
    replaced by an unrelated one at the moment it is needed.

    It survived undetected because the rejection matrix catches the error at the
    point of raise, where no propagation happens. The first real propagation --
    a validator rejection reaching a test through a context manager, on the first
    record the writer had actually produced (V2) -- lost the fault immediately.

    A validation error that destroys its own message under the conditions it is
    raised in is the reader's failure mode, applied to the reader.
    """

    __slots__ = ("fault", "detail")

    def __init__(self, fault: Fault, detail: str) -> None:
        super().__init__(fault, detail)
        self.fault = fault
        self.detail = detail

    def __str__(self) -> str:  # pragma: no cover - formatting only
        return f"[{self.fault.name}] {self.fault.value}: {self.detail}"

    def __repr__(self) -> str:  # pragma: no cover - formatting only
        return f"FlrValidationError(fault={self.fault!r}, detail={self.detail!r})"


def _reject(fault: Fault, detail: str) -> None:
    raise FlrValidationError(fault=fault, detail=detail)


def _meta(handle: Any) -> dict[str, Any]:
    raw = handle.attrs.get("meta")
    if raw is None:
        _reject(Fault.PROVENANCE_MISSING, "root attribute 'meta' is absent")
    meta: dict[str, Any] = json.loads(raw if isinstance(raw, str) else raw.decode())
    return meta


def validate(handle: Any) -> dict[str, Any]:
    """Validate an open `.flr` handle. Returns its metadata, or raises.

    Order matters only for readability; each check is independent so a record
    with several faults reports the first, and fixing it reveals the next.
    """
    meta = _meta(handle)

    if meta.get("schema_version") != SUPPORTED_SCHEMA:
        _reject(
            Fault.SCHEMA_VERSION,
            f"got {meta.get('schema_version')!r}, this reader supports "
            f"{SUPPORTED_SCHEMA!r}. The reader never guesses at an unknown "
            "version -- the alternative is silently analysing a structure under "
            "misinterpreted loads.",
        )

    units = meta.get("units") or {}
    if not _REQUIRED_UNITS.issubset(units):
        _reject(
            Fault.UNITS_MISSING,
            f"missing {sorted(_REQUIRED_UNITS - set(units))}",
        )

    if not meta.get("hsp_git_sha") or not meta.get("run_id"):
        _reject(
            Fault.PROVENANCE_MISSING,
            "a record without provenance is not analysable, so it is rejected "
            "rather than warned about",
        )

    gravity = meta.get("gravity") or [0.0, 0.0, 0.0]
    if not np.isclose(abs(gravity[2]), GRAVITY_MAGNITUDE, rtol=0.0, atol=1e-9):
        _reject(
            Fault.GRAVITY_MISMATCH,
            f"record declares |g| = {abs(gravity[2])}, FloatSim uses "
            f"{GRAVITY_MAGNITUDE}. A mismatch surfaces downstream as an "
            "unexplained mass error and gets hunted in the wrong place.",
        )

    integrator = meta.get("integrator") or {}
    if not _REQUIRED_INTEGRATOR.issubset(integrator):
        _reject(
            Fault.INTEGRATOR_INCOMPLETE,
            f"missing {sorted(_REQUIRED_INTEGRATOR - set(integrator))}. A partial "
            "block is worse than none: a reader holding alpha_f but not alpha_m "
            "would silently blend the inertia term wrongly and still produce "
            "numbers.",
        )

    if integrator.get("mu_treatment") not in MU_TREATMENTS:
        _reject(
            Fault.MU_TREATMENT_UNKNOWN,
            f"got {integrator.get('mu_treatment')!r}; the reader branches on this "
            "rather than assuming, because mu is lagged and unblended while the "
            "other terms blend with alpha_f",
        )

    if meta.get("time_convention") not in TIME_CONVENTIONS:
        _reject(
            Fault.TIME_CONVENTION_MISSING,
            f"got {meta.get('time_convention')!r}. With coefficients stored "
            "rather than samples the reader applies the convention; assuming the "
            "wrong one is a 180 degree phase error on every damping term.",
        )

    _validate_time(handle)
    _validate_bodies(handle)
    _validate_kinematics(handle)
    _validate_loads(handle, meta)
    _validate_joints(handle)
    return meta


def _validate_time(handle: Any) -> None:
    if "time/t" not in handle:
        _reject(Fault.TIME_NON_UNIFORM, "no /time/t dataset")
    t = np.asarray(handle["time/t"][()], dtype=np.float64)
    if t.size < 2:
        _reject(Fault.TIME_NON_UNIFORM, f"only {t.size} samples")
    dt = np.diff(t)
    if np.any(dt <= 0.0):
        _reject(Fault.TIME_NON_UNIFORM, "time base is not strictly increasing")
    if not np.allclose(dt, dt[0], rtol=1e-9, atol=0.0):
        _reject(
            Fault.TIME_NON_UNIFORM,
            "time base is non-uniform and carries no explicit flag",
        )


def _validate_bodies(handle: Any) -> None:
    for name, grp in handle.get("bodies", {}).items():
        if "inertia_reference_point" not in grp.attrs:
            _reject(
                Fault.INERTIA_REFERENCE_MISSING,
                f"body {name!r}. G3.1a cannot catch a wrong reference point, "
                "because both sides would be internally consistent and "
                "consistently wrong.",
            )
        inertia = np.asarray(grp["inertia"][()], dtype=np.float64)
        if not np.allclose(inertia, inertia.T, rtol=1e-10, atol=0.0):
            _reject(Fault.INERTIA_NOT_SPD, f"body {name!r}: tensor is not symmetric")
        if np.any(np.linalg.eigvalsh(inertia) <= 0.0):
            _reject(Fault.INERTIA_NOT_SPD, f"body {name!r}: tensor is not positive definite")


def _validate_kinematics(handle: Any) -> None:
    for name, grp in handle.get("kinematics", {}).items():
        if grp.attrs.get("rotation_parameterisation") not in ROTATION_PARAMETERISATIONS:
            _reject(
                Fault.ROTATION_PARAM_MISSING,
                f"body {name!r}. FloatSim reads xi[3:6] three ways across its own "
                "modules; a record carrying the loads but not the interpretation "
                "carries half the information.",
            )
        if "rotation_validity_bound" not in grp.attrs:
            _reject(
                Fault.ROTATION_BOUND_MISSING,
                f"body {name!r}: an undeclared bound cannot be checked, and "
                "omitting the field must not be a way to pass by having made no "
                "claim",
            )
        bound = float(grp.attrs["rotation_validity_bound"])
        theta = np.linalg.norm(np.asarray(grp["rotation"][()], dtype=np.float64), axis=1)
        worst = float(theta.max())
        if worst > bound:
            _reject(
                Fault.ROTATION_BOUND_EXCEEDED,
                f"body {name!r}: max |theta| = {worst:.5f} rad exceeds the "
                f"declared bound {bound:.5f} rad",
            )
        for field in ("position", "rotation"):
            if not np.all(np.isfinite(np.asarray(grp[field][()]))):
                _reject(Fault.NON_FINITE, f"kinematics/{name}/{field}")


def _validate_loads(handle: Any, meta: dict[str, Any]) -> None:
    known = set(handle.get("bodies", {}).keys())
    for body, grp in handle.get("loads", {}).items():
        if known and body not in known:
            _reject(Fault.UNKNOWN_BODY, f"/loads/{body} has no entry in /bodies")
        for source, sgrp in grp.items():
            if sgrp.attrs.get("time_alignment") not in TIME_ALIGNMENTS:
                _reject(
                    Fault.TIME_ALIGNMENT_MISSING,
                    f"/loads/{body}/{source}: state_force is evaluated at step n "
                    "and applied to the step-(n+1) RHS, so the index a channel "
                    "is written at must be declared",
                )
            if source == "radiation" and "mu" in sgrp:
                valid_from = int(sgrp.attrs.get("valid_from", 0))
                n = np.asarray(sgrp["mu"]).shape[0]
                if valid_from >= n:
                    _reject(
                        Fault.MU_WARMUP,
                        f"/loads/{body}/radiation: valid_from = {valid_from} but "
                        f"only {n} samples. mu before that index saw a "
                        "zero-padded buffer the solver did not, so it is invalid "
                        "rather than approximate.",
                    )


def _validate_joints(handle: Any) -> None:
    joints = handle.get("joints")
    if joints is None:
        return
    if "lam" in joints and joints.attrs.get("jacobian_evaluation") is None:
        _reject(
            Fault.JACOBIAN_EVAL_MISSING,
            "lam is expressed against constraint-Jacobian rows in each joint's "
            "own basis, not a force/moment 6-vector, so the evaluation point "
            "must travel with it",
        )
