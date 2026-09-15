"""DOF numbering is structural, not remembered (D2 step 1)."""

from __future__ import annotations

import numpy as np
import pytest

from floatfea.model.nodes import (
    DOF_PER_NODE,
    Model,
    Node,
    NodeSet,
    element_dofs,
    node_dofs,
)


def test_node_dofs_are_contiguous_and_in_convention_order() -> None:
    assert np.array_equal(node_dofs(0), np.arange(0, 6))
    assert np.array_equal(node_dofs(3), np.arange(18, 24))
    assert DOF_PER_NODE == 6


def test_element_dofs_are_A_then_B() -> None:
    d = element_dofs(2, 5)
    assert np.array_equal(d[:6], node_dofs(2))
    assert np.array_equal(d[6:], node_dofs(5))


def test_a_self_connected_element_is_refused() -> None:
    """A zero-length member has no axis, so its local triad is undefined --
    the same degeneracy `local_axes.py` guards, caught one level earlier."""
    with pytest.raises(ValueError, match="itself"):
        element_dofs(4, 4)


def test_numbering_follows_INSERTION_order() -> None:
    """Not set or dict iteration order, which PYTHONHASHSEED permutes."""
    ns = NodeSet()
    idx = [ns.add(Node(float(i), 0.0, 0.0, name=f"n{i}")) for i in range(5)]
    assert idx == [0, 1, 2, 3, 4]
    assert ns.index("n3") == 3
    assert np.allclose(ns.coords()[:, 0], np.arange(5))


def test_duplicate_names_are_refused() -> None:
    ns = NodeSet()
    ns.add(Node(0, 0, 0, name="a"))
    with pytest.raises(ValueError, match="duplicate node name"):
        ns.add(Node(1, 0, 0, name="a"))


def test_unnamed_nodes_are_allowed_and_do_not_collide() -> None:
    ns = NodeSet()
    assert [ns.add(Node(0, 0, 0)), ns.add(Node(1, 0, 0))] == [0, 1]


def test_model_n_dof_tracks_the_nodes() -> None:
    m = Model()
    assert m.n_dof == 0
    for i in range(4):
        m.nodes.add(Node(float(i), 0.0, 0.0))
    assert m.n_dof == 24
