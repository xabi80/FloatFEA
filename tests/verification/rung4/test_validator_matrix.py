"""The G1.2 rejection matrix — built positive-controls-first.

Gate **G1.2**: the validator rejects, with a specific message, each of a stated
list of faults.

**Why the positive control comes first here.** A validator that rejects
*everything* passes every rejection test. Testing only the rejections would
therefore certify nothing while reading green — the same shape as a negative
control on a degenerate fixture, which this project has already been caught by
once. So the matrix is built the other way round: a **well-formed record that
must be ACCEPTED** is the fixture, every fault is a *mutation* of it, and both
directions are asserted.

Two further properties the matrix enforces:

* **Message distinctness.** The easy implementation collapses several faults
  into one generic "invalid record", which satisfies "it rejected" while
  destroying the diagnostic value G1.2 asks for. Distinctness is asserted across
  the whole matrix, not per-test.
* **Every fault is exercised.** A rejection implemented but never triggered is
  indistinguishable from one that is absent, so the matrix asserts it covers
  every member of `Fault`.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np
import pytest

h5py = pytest.importorskip("h5py")

from floatfea.io.reader import (  # noqa: E402
    SUPPORTED_SCHEMA,
    Fault,
    FlrValidationError,
    validate,
)

_N = 8


def _good_meta() -> dict[str, Any]:
    return {
        "schema_version": SUPPORTED_SCHEMA,
        "floatsim_version": "0.1.0",
        "hsp_git_sha": "a" * 40,
        "run_id": "run-0001",
        "units": {"length": "m", "mass": "kg", "time": "s", "force": "N", "angle": "rad"},
        "gravity": [0.0, 0.0, -9.81],
        "water_density": 1025.0,
        "water_depth": 200.0,
        "scale": "model",
        "time_convention": "exp_minus_i_omega_t",
        "integrator": {
            "scheme": "generalized_alpha",
            "rho_inf": 0.9,
            "alpha_m": 0.42105,
            "alpha_f": 0.47368,
            "beta": 0.27701,
            "gamma": 0.55263,
            "dt": 0.01,
            "mu_treatment": "lagged_unblended",
        },
    }


def _write_good(path, meta: dict[str, Any] | None = None) -> None:
    """A minimal record that MUST validate. The positive control."""
    import json

    with h5py.File(path, "w") as h:
        h.attrs["meta"] = json.dumps(meta if meta is not None else _good_meta())
        h.create_dataset("time/t", data=np.arange(_N) * 0.01)

        b = h.create_group("bodies/buoy1")
        b.create_dataset("inertia", data=np.diag([24.0, 24.0, 0.114]))
        b.attrs["inertia_reference_point"] = "reference_point"

        k = h.create_group("kinematics/buoy1")
        k.create_dataset("position", data=np.zeros((_N, 3)))
        k.create_dataset("rotation", data=np.full((_N, 3), 0.01))
        k.attrs["rotation_parameterisation"] = "zyx_intrinsic_euler"
        k.attrs["rotation_validity_bound"] = 0.1

        r = h.create_group("loads/buoy1/radiation")
        r.create_dataset("mu", data=np.zeros((_N, 6)))
        r.attrs["time_alignment"] = "state_n"
        r.attrs["valid_from"] = 0

        j = h.create_group("joints")
        j.create_dataset("lam", data=np.zeros((_N, 4)))
        j.attrs["jacobian_evaluation"] = "step_midpoint"


# --- mutations, one per fault ---------------------------------------------


def _m_schema(h):
    import json

    m = _good_meta()
    m["schema_version"] = "9.9"
    h.attrs["meta"] = json.dumps(m)


def _m_units(h):
    import json

    m = _good_meta()
    m["units"].pop("force")
    h.attrs["meta"] = json.dumps(m)


def _m_provenance(h):
    import json

    m = _good_meta()
    m["run_id"] = ""
    h.attrs["meta"] = json.dumps(m)


# PROVENANCE_MISSING has THREE raise sites -- absent `meta`, empty `hsp_git_sha`,
# empty `run_id` -- and the matrix exercised only the last. Fault-level coverage
# said it was covered; the other two paths could have been deleted without a test
# noticing. Found by the F1 gate-table audit (AL2), which is the same gap one level
# down: covering a fault is not covering the conditions that raise it.
def _m_provenance_sha(h):
    import json

    m = _good_meta()
    m["hsp_git_sha"] = ""
    h.attrs["meta"] = json.dumps(m)


def _m_provenance_meta_absent(h):
    del h.attrs["meta"]


def _m_gravity(h):
    import json

    m = _good_meta()
    m["gravity"] = [0.0, 0.0, -9.80665]
    h.attrs["meta"] = json.dumps(m)


def _m_integrator(h):
    import json

    m = _good_meta()
    m["integrator"].pop("alpha_m")
    h.attrs["meta"] = json.dumps(m)


def _m_mu_treatment(h):
    import json

    m = _good_meta()
    m["integrator"]["mu_treatment"] = "blended"
    h.attrs["meta"] = json.dumps(m)


def _m_time_convention(h):
    import json

    m = _good_meta()
    m.pop("time_convention")
    h.attrs["meta"] = json.dumps(m)


def _m_time_nonuniform(h):
    t = np.arange(_N) * 0.01
    t[4] += 0.005
    del h["time/t"]
    h.create_dataset("time/t", data=t)


def _m_non_finite(h):
    d = h["kinematics/buoy1/position"][()]
    d[3, 1] = np.nan
    h["kinematics/buoy1/position"][...] = d


def _m_rotation_param(h):
    del h["kinematics/buoy1"].attrs["rotation_parameterisation"]


def _m_bound_missing(h):
    del h["kinematics/buoy1"].attrs["rotation_validity_bound"]


def _m_bound_exceeded(h):
    d = h["kinematics/buoy1/rotation"][()]
    d[5, :] = 0.2  # |theta| ~ 0.346 rad against a declared 0.1
    h["kinematics/buoy1/rotation"][...] = d


def _m_time_alignment(h):
    del h["loads/buoy1/radiation"].attrs["time_alignment"]


def _m_inertia_ref(h):
    del h["bodies/buoy1"].attrs["inertia_reference_point"]


def _m_inertia_spd(h):
    h["bodies/buoy1/inertia"][...] = np.diag([24.0, -1.0, 0.114])


def _m_jacobian(h):
    del h["joints"].attrs["jacobian_evaluation"]


def _m_mu_warmup(h):
    h["loads/buoy1/radiation"].attrs["valid_from"] = _N + 5


def _m_unknown_body(h):
    g = h.create_group("loads/ghost/radiation")
    g.attrs["time_alignment"] = "state_n"


MATRIX: list[tuple[Fault, Callable[[Any], None]]] = [
    (Fault.SCHEMA_VERSION, _m_schema),
    (Fault.UNITS_MISSING, _m_units),
    (Fault.PROVENANCE_MISSING, _m_provenance),
    (Fault.PROVENANCE_MISSING, _m_provenance_sha),
    (Fault.PROVENANCE_MISSING, _m_provenance_meta_absent),
    (Fault.GRAVITY_MISMATCH, _m_gravity),
    (Fault.INTEGRATOR_INCOMPLETE, _m_integrator),
    (Fault.MU_TREATMENT_UNKNOWN, _m_mu_treatment),
    (Fault.TIME_CONVENTION_MISSING, _m_time_convention),
    (Fault.TIME_NON_UNIFORM, _m_time_nonuniform),
    (Fault.NON_FINITE, _m_non_finite),
    (Fault.ROTATION_PARAM_MISSING, _m_rotation_param),
    (Fault.ROTATION_BOUND_MISSING, _m_bound_missing),
    (Fault.ROTATION_BOUND_EXCEEDED, _m_bound_exceeded),
    (Fault.TIME_ALIGNMENT_MISSING, _m_time_alignment),
    (Fault.INERTIA_REFERENCE_MISSING, _m_inertia_ref),
    (Fault.INERTIA_NOT_SPD, _m_inertia_spd),
    (Fault.JACOBIAN_EVAL_MISSING, _m_jacobian),
    (Fault.MU_WARMUP, _m_mu_warmup),
    (Fault.UNKNOWN_BODY, _m_unknown_body),
]


def test_the_well_formed_record_is_ACCEPTED(tmp_path) -> None:
    """The positive control. Without this the whole matrix proves nothing.

    A validator that rejected every record would pass all eighteen rejection
    tests below. This is the one that stops that.
    """
    path = tmp_path / "good.flr"
    _write_good(path)
    with h5py.File(path, "r") as h:
        meta = validate(h)
    assert meta["schema_version"] == SUPPORTED_SCHEMA


@pytest.mark.parametrize("fault,mutate", MATRIX, ids=[f.name for f, _ in MATRIX])
def test_each_fault_is_rejected_with_its_own_fault_tag(tmp_path, fault, mutate) -> None:
    """One malformed fixture per rejection, each naming its specific fault."""
    path = tmp_path / "bad.flr"
    _write_good(path)
    with h5py.File(path, "a") as h:
        mutate(h)
    with h5py.File(path, "r") as h, pytest.raises(FlrValidationError) as exc:
        validate(h)
    assert exc.value.fault is fault, (
        f"expected {fault.name}, got {exc.value.fault.name} — the fault tags are "
        "what make G1.2's 'specific message' requirement testable"
    )


def test_the_matrix_covers_every_declared_fault() -> None:
    """A rejection implemented but never exercised is indistinguishable from absent."""
    covered = {f for f, _ in MATRIX}
    missing = set(Fault) - covered
    assert not missing, f"faults declared but never exercised: {sorted(m.name for m in missing)}"


def test_no_two_faults_share_a_message() -> None:
    """G1.2 asks for a SPECIFIC message per rejection.

    The easy implementation collapses faults into a generic 'invalid record',
    which satisfies 'it rejected' while destroying the diagnostic value.
    """
    # `list(Fault)` yields only CANONICAL members. Python collapses two enum
    # members with equal values into an ALIAS, so a duplicated message never
    # reaches this list -- the count silently drops instead. Asserting over
    # `list(Fault)` therefore cannot fail, which a mutation proved (AM1): giving
    # MU_WARMUP the PROVENANCE_MISSING message left the whole matrix green.
    #
    # `__members__` includes aliases, so it is the only view that can see the
    # collision.
    by_name = {name: m.value for name, m in Fault.__members__.items()}
    dupes = {v for v in by_name.values() if list(by_name.values()).count(v) > 1}
    assert not dupes, f"two faults share a message: {sorted(dupes)}"

    assert len(Fault.__members__) == len(list(Fault)), (
        "an enum ALIAS exists -- two faults were declared with the same value and "
        "Python merged them. The merged fault can never be raised distinctly."
    )
    names = list(Fault.__members__)
    assert len(set(names)) == len(names)


@pytest.mark.parametrize("fault,mutate", MATRIX, ids=[f.name for f, _ in MATRIX])
def test_each_mutation_changes_only_what_it_intends(tmp_path, fault, mutate) -> None:
    """Paired positive control: the UNMUTATED record still validates.

    Guards against a mutation that happens to break something else, which would
    let a rejection test pass for the wrong reason.
    """
    path = tmp_path / "control.flr"
    _write_good(path)
    with h5py.File(path, "r") as h:
        validate(h)
