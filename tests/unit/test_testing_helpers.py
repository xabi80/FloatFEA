"""`assert_close` refuses a vacuous comparison (BD0)."""

from __future__ import annotations

import numpy as np
import pytest

from floatfea.testing import DEFAULT_FLOOR_FACTOR, assert_close, assert_differs


def test_it_passes_a_real_agreement() -> None:
    assert_close(1.0, 1.0 + 1e-15, tol=1e-12, floor=1e-16, what="ok")


def test_it_fails_a_real_disagreement() -> None:
    with pytest.raises(AssertionError, match="failed"):
        assert_close(1.0, 1.1, tol=1e-12, floor=1e-16, what="bad")


def test_it_REFUSES_operands_at_the_floor() -> None:
    """The R9 failure, reproduced: two tiny numbers that agree trivially.

    Both malformed controls compared quantities the comparison could not resolve.
    `pytest.approx(4.15e-16, rel=1e-12)` passes against `4.15e-12` because of an
    undeclared default `abs=1e-12`; this raises instead.
    """
    with pytest.raises(AssertionError, match="VACUOUS"):
        assert_close(4.15e-16, 4.15e-12, tol=1e-12, floor=1e-12, what="the R9 case")


def test_the_refusal_boundary_is_where_it_says() -> None:
    floor = 1e-12
    assert_close(
        DEFAULT_FLOOR_FACTOR * floor * 1.01,
        DEFAULT_FLOOR_FACTOR * floor * 1.01,
        tol=1e-9,
        floor=floor,
        what="just above",
    )
    with pytest.raises(AssertionError, match="VACUOUS"):
        assert_close(
            DEFAULT_FLOOR_FACTOR * floor * 0.99,
            DEFAULT_FLOOR_FACTOR * floor * 0.99,
            tol=1e-9,
            floor=floor,
            what="just below",
        )


def test_assert_differs_separates_and_refuses() -> None:
    assert_differs(1.0, 2.0, by=0.5, floor=1e-16, what="real")
    with pytest.raises(AssertionError, match="did not separate"):
        assert_differs(1.0, 1.0 + 1e-15, by=0.5, floor=1e-16, what="same")
    with pytest.raises(AssertionError, match="VACUOUS"):
        assert_differs(1e-14, 2e-14, by=0.5, floor=1e-12, what="tiny")


def test_it_works_on_arrays() -> None:
    a = np.array([1.0, 2.0, 3.0])
    assert_close(a, a * (1 + 1e-15), tol=1e-12, floor=1e-16, what="array")
    with pytest.raises(AssertionError, match="failed"):
        assert_close(a, a + 0.5, tol=1e-12, floor=1e-16, what="array bad")
