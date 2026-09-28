"""The nondeterminism class is enumerated and pinned (Q4).

Three library defaults surfaced separately during F1 and F2's lock — Hypothesis
seeding, BLAS thread count, sparse factorisation ordering. Three is a class, so
`floatfea/determinism.py` enumerates it once. These tests assert the pins exist
and, where it is cheap, that they actually bite.
"""

from __future__ import annotations

import numpy as np
import pytest

from floatfea import determinism as det


def test_every_named_pin_has_a_value() -> None:
    r = det.report()
    assert r["sparse_permc_spec"], "sparse ordering not pinned"
    assert isinstance(r["arpack_v0_seed"], int), "ARPACK start vector not pinned"
    assert r["hypothesis_derandomize"] is True


def test_pin_threads_sets_every_variable() -> None:
    det.pin_threads(1)
    import os

    for v in det.THREAD_ENV:
        assert os.environ[v] == "1", f"{v} not pinned"


def test_the_arpack_start_vector_is_reproducible() -> None:
    """The pin must bite: two calls give the same vector, bit for bit."""
    a, b = det.deterministic_v0(37), det.deterministic_v0(37)
    assert np.array_equal(a, b)
    assert a.shape == (37,)


def test_the_arpack_pin_is_independent_of_global_numpy_state() -> None:
    """A caller seeding numpy elsewhere must not move an eigenvalue result.

    This is why `deterministic_v0` uses a dedicated generator rather than
    `np.random.seed`. Without it the pin is only as stable as every other
    module's use of the global state.

    THE LEGACY API IS THE SUBJECT, NOT AN OVERSIGHT (CA0). `NPY002` asks for
    `np.random.Generator` here, and a Generator cannot perturb the legacy GLOBAL
    state -- which is the exact thing this test proves the pin is immune to. The
    modern call would leave the assertion true by construction and testing
    nothing. Suppressed per line, with the reason, rather than by disabling the
    rule or excluding the file; the six sites are named in the step report.
    """
    np.random.seed(1)  # noqa: NPY002 -- perturbing the legacy global state IS the test
    a = det.deterministic_v0(16)
    np.random.seed(999)  # noqa: NPY002 -- and again, with a different seed
    b = det.deterministic_v0(16)
    assert np.array_equal(a, b)


def test_an_unseeded_arpack_start_would_NOT_be_reproducible() -> None:
    """Negative control: the thing being guarded against must actually vary.

    If unseeded draws happened to be reproducible, every assertion above would
    pass for the wrong reason and the pin would be ceremony.
    """
    # THE LEGACY API IS THE SUBJECT HERE TOO (CA0): "an unseeded legacy draw" is
    # the construct whose nondeterminism the pin exists to remove, so it cannot
    # be written with a Generator without ceasing to be that construct.
    np.random.seed(None)  # noqa: NPY002 -- an UNSEEDED legacy draw is the subject
    a = np.random.standard_normal(64)  # noqa: NPY002 -- see above
    np.random.seed(None)  # noqa: NPY002 -- see above
    b = np.random.standard_normal(64)  # noqa: NPY002 -- see above
    assert not np.array_equal(a, b), (
        "two unseeded draws matched -- the nondeterminism this pins does not "
        "exist in this environment, so the pin is untested"
    )


def test_the_sparse_ordering_is_named_not_defaulted() -> None:
    """Naming COLAMD is the point; it is also SciPy's default TODAY.

    A default that is correct now is not a pin: it can change with a version and
    move stored results with no code change. Asserting the constant exists and is
    a permutation SuperLU accepts is what makes the choice explicit.
    """
    assert det.SPARSE_PERMC_SPEC in {
        "NATURAL",
        "MMD_ATA",
        "MMD_AT_PLUS_A",
        "COLAMD",
    }


@pytest.mark.parametrize(
    "member",
    ["threads", "sparse_permc_spec", "arpack_v0_seed", "pythonhashseed", "hypothesis_derandomize"],
)
def test_the_report_covers_every_class_member(member: str) -> None:
    """A run log that omits a pin cannot be used to reproduce the run."""
    assert member in det.report()
