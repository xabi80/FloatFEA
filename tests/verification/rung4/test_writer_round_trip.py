"""G1.1 — a record the WRITER produced, round-tripped against its closed form (V2).

**NOT BIT-EXACT, AND THE TITLE SAID SO FOR ONE COMMIT TOO LONG (R328).** Twelve
kinematic pairs and `joints/lam` are compared within `INTERCHANGE_CHANNEL_DRIFT_ULP`
of each channel's own amplitude, because the comparison is not against the file:
it is against `np.sin` and `np.cos` re-evaluated here, and those are not
correctly rounded. `time/t` and the interchangeability control are still exact.

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

**THE SIDECAR ROUTE EXISTS AND WAS NOT TAKEN (R328).** `artifacts/make_fixture_flr.py`
already writes `writer_output.expected.npz` beside the fixture, and it is not
committed. Committing it would make this comparison bit-exact on every machine,
because both sides would then be stored data — and that is a real alternative to
a band, so it is recorded here rather than left unsaid.

It was not taken for the reason the paragraph above gives, and the reason is
narrower than it looks: a binary sidecar moves the expectation out of the file a
reviewer reads and into a blob that only the generator can explain, and the two
would then be regenerated together by the same script, which is how a writer and
a validator come to encode one misreading twice. What the band costs is that a
libm's last bit is admitted; what the sidecar would cost is that the closed form
stops being visible at the point of comparison. The visible closed form is the
thing G1.2's positive control was missing, so it is the half kept.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pytest

h5py = pytest.importorskip("h5py")

from floatfea.io.reader import validate  # noqa: E402
from floatfea.tolerances import (  # noqa: E402
    INTERCHANGE_CHANNEL_DRIFT_ULP,
    INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER,
)

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
    xi[:, rot] *= 0.02  # rotations kept inside the declared validity bound
    return {
        "t": t,
        "xi": xi,
        "xi_dot": np.cos(2.3 * t[:, None] - 0.17 * j) * (2.0 + 0.03 * j),
        "xi_ddot": np.sin(3.1 * t[:, None] + 0.09 * j) * (3.0 - 0.02 * j),
        "lam": np.cos(1.1 * t[:, None] + 0.5 * np.arange(4)[None, :]),
    }


def _drift_ulp(got: np.ndarray, want: np.ndarray) -> tuple[float, int]:
    """`(largest difference in ULP of the channel's amplitude, values exact)`.

    OF THE CHANNEL'S OWN AMPLITUDE, which is the plan's wording and is what
    lets one number cover channels two orders apart: `rotation` peaks at
    2.5e-02 and `acceleration` at 3.0e+00, and at one ULP of each they are
    four orders apart in absolute difference and identical here.
    """
    ampl = float(np.max(np.abs(want)))
    if ampl == 0.0:
        # AN UNSUPPORTED CASE RAISES; IT DOES NOT DEFAULT (R329). `or 1.0`
        # invented a scale for a dimensional quantity inside a test file, and
        # an all-zero channel would then have passed at up to 4.4e-16
        # absolute -- which is the shape a writer that forgot a channel
        # produces, and is why `test_mu_is_present_and_not_all_zero` exists.
        raise ValueError(
            "the reference channel is identically zero, so there is no "
            "amplitude to measure ULP against. A channel that should be zero "
            "and is not is a defect, not a rounding question."
        )
    diff = float(np.max(np.abs(got - want)))
    return diff / math.ulp(ampl), int(np.count_nonzero(got == want))


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
def test_every_kinematic_channel_round_trips_WITHIN_ITS_CLASS(
    body: str, k: int, dataset: str, channel: str, offset: int
) -> None:
    """Q8's second local class, measured (CJ1).

    THIS ASSERTED BIT-EXACTNESS AND THAT WAS WRONG, for a reason the container
    is not to blame for: HDF5 float64 is lossless, so the round trip through
    the file is exact, and the comparison is not against the file alone. It is
    against `np.sin` and `np.cos` re-evaluated HERE. Those are not correctly
    rounded and the standard does not require them to be, so a committed
    fixture produced on one machine cannot round-trip bit-exactly on another --
    and thirteen of these pairs were red on CI for eleven rounds, every one of
    them in the last bit.

    The band is `INTERCHANGE_CHANNEL_DRIFT_ULP`, in ULP of the channel's own
    amplitude, declared in the plan from the canonical measurement: worst
    `1.0` there, `0.0` on the machine that produced the fixture, `1.0` on every
    determinism leg of run 34545832426, across three CPU models (R325: `six`
    stood here and the run prints three).

    WHAT IS NOT RELAXED. `time/t` goes through no transcendental and is still
    asserted bit-exact below; the channels are still each other's controls
    (`test_channels_are_not_interchangeable`); and the band is two ULP of an
    amplitude, which for `rotation` is `5e-18` in absolute terms.
    """
    want = _expected()[channel][:, 6 * k + offset : 6 * k + offset + 3]
    with h5py.File(FIXTURE, "r") as f:
        got = f[f"kinematics/{body}/{dataset}"][...]
    drift, exact = _drift_ulp(got, want)
    assert drift <= INTERCHANGE_CHANNEL_DRIFT_ULP, (
        f"{body}/{dataset} is {drift:.4f} ULP of its own amplitude from the "
        f"generator's closed form, and the band is "
        f"{INTERCHANGE_CHANNEL_DRIFT_ULP}. {exact} of {want.size} values agree "
        "bit for bit. A drift this size is not the last bit of a libm; "
        "regenerate nothing until it is understood."
    )


def test_time_round_trips_bit_exact() -> None:
    """ARITHMETIC ONLY, SO EXACT (Q8's first class). `arange(N+1) * DT` has no
    transcendental in it, and it agrees bit for bit on both machines -- 25 of
    25 values on the canonical one. It is deliberately outside the band: a band
    that covered this channel would be fitted to the loosest one."""
    with h5py.File(FIXTURE, "r") as f:
        assert np.array_equal(f["time/t"][...], _expected()["t"])


def test_joint_multipliers_round_trip_within_their_class() -> None:
    """`cos` again, so the same band and for the same reason."""
    want = _expected()["lam"]
    with h5py.File(FIXTURE, "r") as f:
        got = f["joints/lam"][...]
    drift, exact = _drift_ulp(got, want)
    assert drift <= INTERCHANGE_CHANNEL_DRIFT_ULP, (
        f"joints/lam is {drift:.4f} ULP of its amplitude from the closed form, "
        f"band {INTERCHANGE_CHANNEL_DRIFT_ULP}; {exact} of {want.size} exact."
    )


@pytest.mark.parametrize(
    "dataset, channel, offset",
    [("position", "xi", 0), ("acceleration", "xi_ddot", 0)],
)
def test_a_drift_PAST_the_band_is_refused(dataset: str, channel: str, offset: int) -> None:
    """The counter, injected into the value the comparison reads (V2).

    `INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER` is one ULP past the band: the
    smallest injection unambiguously outside it. A counter AT the band would
    test the comparison operator, and one an order out would pass a band ten
    times too wide.
    """
    want = _expected()[channel][:, offset : offset + 3]
    with h5py.File(FIXTURE, "r") as f:
        got = np.array(f[f"kinematics/bodyA/{dataset}"][...])
    ampl = float(np.max(np.abs(want)))

    # THE INJECTION IS RELATIVE TO THE CLEAN DEVIATION AT THIS SITE (R324).
    # Adding an absolute 3 ULP to a value the machine already holds 1 ULP
    # BELOW the reference measures 2 ULP against a band of 2, and the
    # assertion then fails on the very machine the band was measured on. The
    # canonical machine puts a full ULP on two of this channel's seventy-five
    # values and which two is a property of a libm, so the margin was decided
    # by luck of the draw.
    #
    # Measured from the site and added beyond it, the injected DELTA is the
    # same on every machine and the margin is one ULP by construction.
    clean = (got[0, 0] - want[0, 0]) / math.ulp(ampl)
    direction = 1.0 if clean >= 0.0 else -1.0
    got[0, 0] += direction * INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER * math.ulp(ampl)
    drift, _ = _drift_ulp(got, want)
    expected_drift = abs(clean) + INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER
    assert drift > INTERCHANGE_CHANNEL_DRIFT_ULP, (
        f"a {INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER} ULP injection beyond a "
        f"clean deviation of {clean:+.4f} ULP measured as {drift:.4f}, and the "
        f"band is {INTERCHANGE_CHANNEL_DRIFT_ULP}. The band does not catch the "
        "defect it is sized against."
    )
    assert drift >= expected_drift - 1e-9, (
        f"the injection measured {drift:.4f} ULP where {expected_drift:.4f} was "
        "put in. The delta is not what reached the comparison, so the counter "
        "is measuring something other than itself."
    )


def test_a_swapped_sign_is_orders_away_from_the_band() -> None:
    """What the band is NOT wide enough to hide, stated as arithmetic.

    THE ASSERTION WAS `drift > 1e12 * BAND` AND THAT WAS A THRESHOLD (R326):
    an undeclared literal reaching a comparison, invisible to the scanner
    because it sits inside a `BinOp`, and `CLAUDE.md` § Tolerances admits no
    local literals. It also certified far less than the sentence beside it
    claimed -- it is satisfied for any band below ten thousand ULP.

    There is no threshold here now. A sign flip on a value `v` moves it by
    exactly `2|v|`, so the drift it produces is `2|v| / ulp(amplitude)` and
    that is a PREDICTION, not a bound. Asserting the measurement equals the
    prediction says the instrument measures what it claims to; the ORDERS
    between it and the band are then a published figure in the step report,
    where a figure belongs, rather than a number chosen in a test.

    IT READS NO FIXTURE, and the previous docstring did not say so: `got` is
    built from `want`, so this cannot fail for any defect in the repository.
    It is a statement about the scale of the band and nothing else.
    """
    want = _expected()["xi"][:, 3:6]
    got = np.array(want)
    got[0, 0] = -got[0, 0]
    drift, exact = _drift_ulp(got, want)
    ampl = float(np.max(np.abs(want)))
    predicted = 2.0 * abs(float(want[0, 0])) / math.ulp(ampl)
    assert drift == predicted, (
        f"a sign flip measured {drift:.6e} ULP and the arithmetic predicts "
        f"{predicted:.6e}. The instrument is not measuring what it says."
    )
    assert exact == want.size - 1, (
        "the flip moved more than the one value it was applied to, so the "
        "comparison is not per-element."
    )
