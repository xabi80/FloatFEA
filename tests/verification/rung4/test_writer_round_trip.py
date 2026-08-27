"""G1.1 — bit-exact round-trip of a record the WRITER actually produced (V2).

What this replaces
------------------
The G1.2 matrix's positive control is a record **hand-built in Python**, so until
now nothing in FloatFEA had ever read writer output. That gap is not theoretical:
the first end-to-end pass found `time_convention` missing from the writer, with
writer and validator each correct against their own reading of the spec and
neither ever meeting.

The fixture is a **committed `.flr`**, not an import of `floatsim`. `CLAUDE.md`
says the two codebases meet only at a versioned interchange file; a test that
imported the writer would make that false and would make this suite unrunnable
without HSP at a matching state. The boundary object is the fixture.

It is therefore a **golden file**: regenerating it requires a written explanation
of why the bytes moved (`CLAUDE.md` § Testing). Generator:
`artifacts/make_fixture_flr.py`.

The channel values are recomputed here from the same closed forms the generator
used, rather than shipped in a sidecar — so what is asserted is readable, and a
reviewer can check the expectation without loading a binary.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

h5py = pytest.importorskip("h5py")

from floatfea.io.reader import validate  # noqa: E402

FIXTURE = Path(__file__).resolve().parents[2] / "fixtures" / "writer_output.flr"
N, NB, DT, NLAG = 24, 2, 0.05, 8
NDOF = 6 * NB


def _expected() -> dict[str, np.ndarray]:
    """The generator's closed forms, restated. Deliberately duplicated: a shared
    helper would let one edit move both sides together and the test would keep
    passing while the fixture drifted."""
    t = np.arange(N + 1) * DT
    j = np.arange(NDOF)[None, :]
    rot = (np.arange(NDOF) % 6) >= 3
    xi = np.sin(1.7 * t[:, None] + 0.31 * j) * (1.0 + 0.05 * j)
    xi[:, rot] *= 0.02          # rotations kept inside the declared validity bound
    return {
        "t": t,
        "xi": xi,
        "xi_dot": np.cos(2.3 * t[:, None] - 0.17 * j) * (2.0 + 0.03 * j),
        "xi_ddot": np.sin(3.1 * t[:, None] + 0.09 * j) * (3.0 - 0.02 * j),
        "lam": np.cos(1.1 * t[:, None] + 0.5 * np.arange(4)[None, :]),
    }


def test_the_fixture_exists_and_is_writer_produced() -> None:
    """Meta-test. Every assertion below is vacuous on a missing or empty file."""
    assert FIXTURE.is_file(), (
        f"{FIXTURE} is missing -- regenerate with artifacts/make_fixture_flr.py "
        "under HSP. Without it the round-trip below tests nothing."
    )
    with h5py.File(FIXTURE, "r") as f:
        assert "meta" in f.attrs, "no /meta -- this is not a writer-produced record"
        assert f["time/t"].shape == (N + 1,)


def test_the_validator_ACCEPTS_real_writer_output() -> None:
    """The positive control G1.2 never had: writer output, not a hand-built dict.

    A validator tested only against fixtures it was written beside can encode the
    same misreading of the spec twice and stay green.
    """
    with h5py.File(FIXTURE, "r") as f:
        validate(f)


@pytest.mark.parametrize("body, k", [("bodyA", 0), ("bodyB", 1)])
@pytest.mark.parametrize(
    "dataset, channel, offset",
    [
        ("position", "xi", 0),
        ("rotation", "xi", 3),
        ("velocity", "xi_dot", 0),
        ("angular_velocity", "xi_dot", 3),
        ("acceleration", "xi_ddot", 0),
        ("angular_acceleration", "xi_ddot", 3),
    ],
)
def test_every_kinematic_channel_round_trips_BIT_EXACT(
    body: str, k: int, dataset: str, channel: str, offset: int
) -> None:
    want = _expected()[channel][:, 6 * k + offset : 6 * k + offset + 3]
    with h5py.File(FIXTURE, "r") as f:
        got = f[f"kinematics/{body}/{dataset}"][...]
    # Bit-exact, not approximate: HDF5 float64 is a lossless container, so any
    # difference at all is a defect rather than a rounding artifact.
    assert np.array_equal(got, want), (
        f"{body}/{dataset} differs from the generator's closed form; "
        f"max |diff| = {np.abs(got - want).max():.3e}"
    )


def test_time_round_trips_bit_exact() -> None:
    with h5py.File(FIXTURE, "r") as f:
        assert np.array_equal(f["time/t"][...], _expected()["t"])


def test_joint_multipliers_round_trip_bit_exact() -> None:
    with h5py.File(FIXTURE, "r") as f:
        assert np.array_equal(f["joints/lam"][...], _expected()["lam"])


def test_channels_are_not_interchangeable() -> None:
    """Guards the round-trip against passing on a swapped channel.

    The generator gives every channel and every DOF a different closed form for
    this reason: if position and velocity were both, say, sin(t), the assertions
    above would pass with the two swapped.
    """
    e = _expected()
    with h5py.File(FIXTURE, "r") as f:
        pos = f["kinematics/bodyA/position"][...]
    assert not np.allclose(pos, e["xi_dot"][:, 0:3]), "position matches velocity"
    assert not np.allclose(pos, e["xi_ddot"][:, 0:3]), "position matches acceleration"
    assert not np.allclose(pos, e["xi"][:, 3:6]), "position matches rotation"


def test_a_validation_error_SURVIVES_propagation() -> None:
    """`FlrValidationError` must carry a traceback out through a context manager.

    It was a frozen dataclass, which forbids Python's `__traceback__` assignment,
    so a real rejection arrived as `FrozenInstanceError: cannot assign to field
    '__traceback__'` -- the named fault replaced by an unrelated error exactly
    when it was needed. The rejection matrix never saw it because it catches at
    the point of raise. This asserts the propagation path the matrix does not.
    """
    from contextlib import contextmanager

    from floatfea.io.reader import Fault, FlrValidationError

    @contextmanager
    def _through():
        yield

    with pytest.raises(FlrValidationError) as caught:
        with _through():
            raise FlrValidationError(Fault.MU_WARMUP, "propagation check")
    assert caught.value.fault is Fault.MU_WARMUP
    assert caught.value.__traceback__ is not None


def test_mu_is_present_and_not_all_zero() -> None:
    """`mu` at a run start has `mu[0] = 0` by convention; the rest must not be.

    An all-zero `mu` is what a writer that forgot the radiation channel produces,
    and it would satisfy any test that only checked the dataset's presence.
    """
    with h5py.File(FIXTURE, "r") as f:
        mu = f["loads/bodyA/radiation/mu"][...]
    assert mu.shape == (N + 1, 6)
    assert np.array_equal(mu[0], np.zeros(6)), "mu[0] must be zero at a run start"
    assert np.abs(mu[1:]).max() > 0.0, "mu is identically zero -- channel not written"
