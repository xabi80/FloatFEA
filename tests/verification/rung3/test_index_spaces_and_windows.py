"""The 72-vs-102 trap, and comparison-window containment.

Both are structural guards for mistakes that have already happened here.
"""

from __future__ import annotations

import pytest

from floatfea.io.frames import (
    HYDRO_GLOBAL_DOF,
    N_DOF_HYDRO,
    assert_comparison_window_is_valid,
    global_to_hydro,
    hydro_to_global,
)


def test_hydro_index_46_and_global_index_46_are_different_dof() -> None:
    """The exact collision that bit: BOTH spaces have a valid entry at 46.

    A count assertion (N_HYDRO_DOF == 72) cannot catch this, which is why the
    conversion is a function rather than a remembered rule.
    """
    assert hydro_to_global(46) == 58
    assert hydro_to_global(46) != 46


def test_global_dof_46_is_structural_and_raises() -> None:
    """Global 46 lies in hub2. Indexing hydro arrays with it returned a silent
    zero and looked like a confirmed hypothesis."""
    with pytest.raises(IndexError, match="STRUCTURAL"):
        global_to_hydro(46)


def test_round_trip_over_every_hydro_dof() -> None:
    for j in range(N_DOF_HYDRO):
        assert global_to_hydro(hydro_to_global(j)) == j


def test_hydro_dof_are_exactly_the_buoy_slots() -> None:
    assert len(HYDRO_GLOBAL_DOF) == 72
    assert len(set(HYDRO_GLOBAL_DOF)) == 72
    assert max(HYDRO_GLOBAL_DOF) < 102


def test_a_hydro_index_passed_as_global_is_rejected() -> None:
    with pytest.raises(IndexError):
        hydro_to_global(102)


def test_comparison_window_inside_both_validity_windows_passes() -> None:
    assert_comparison_window_is_valid((70.0, 95.0), mu=(60.0, 120.0), panels=(0.0, 120.0))


def test_comparison_window_starting_inside_the_mu_warmup_is_refused() -> None:
    """The fifth appearance of the validity-window rule, now an assertion.

    mu is valid only from t0 + kernel memory (60 s here). A comparison window
    starting earlier compares mu against a prediction it cannot satisfy, and the
    discrepancy looks like physics.
    """
    with pytest.raises(ValueError, match="looks like physics"):
        assert_comparison_window_is_valid((30.0, 95.0), mu=(60.0, 120.0))


def test_reversed_comparison_window_is_refused() -> None:
    with pytest.raises(ValueError, match="empty or reversed"):
        assert_comparison_window_is_valid((95.0, 70.0), mu=(0.0, 120.0))
