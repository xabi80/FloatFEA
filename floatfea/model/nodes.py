"""Nodes, DOF numbering, and the model container (D2 step 1).

DOF numbering is the one thing here that every later matrix depends on, so it is
fixed by construction rather than by convention: node ``i`` owns global DOF
``6i .. 6i+5`` in the order ``(ux, uy, uz, rx, ry, rz)``, matching
`docs/conventions.md` and the interchange record's per-body ordering.

**Numbering is derived from insertion order, never from a set or dict iteration.**
`floatfea/determinism.py` records why: `PYTHONHASHSEED` permutes set iteration, and
an assembly ordering built by iterating a set silently permutes the matrix.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final

import numpy as np
from numpy.typing import NDArray

DOF_PER_NODE: Final[int] = 6
DOF_NAMES: Final[tuple[str, ...]] = ("ux", "uy", "uz", "rx", "ry", "rz")


@dataclass(frozen=True)
class Node:
    """A point in the global frame. Immutable: geometry is not edited in place."""

    x: float
    y: float
    z: float
    name: str = ""

    @property
    def xyz(self) -> NDArray[np.float64]:
        return np.array([self.x, self.y, self.z], dtype=np.float64)


class NodeSet:
    """Ordered node collection with deterministic DOF numbering.

    Insertion order IS the numbering. `add` returns the index so a caller never
    has to look one up, and there is deliberately no `by_name` iteration order
    exposed: the only ordering that exists is the one the matrices use.
    """

    def __init__(self) -> None:
        self._nodes: list[Node] = []
        self._by_name: dict[str, int] = {}

    def add(self, node: Node) -> int:
        if node.name:
            if node.name in self._by_name:
                raise ValueError(
                    f"duplicate node name {node.name!r}; names must be unique or "
                    "empty, since a silently reused name would make two members "
                    "share a node that was meant to be two."
                )
            self._by_name[node.name] = len(self._nodes)
        self._nodes.append(node)
        return len(self._nodes) - 1

    def index(self, name: str) -> int:
        try:
            return self._by_name[name]
        except KeyError:
            raise KeyError(f"no node named {name!r}") from None

    def __len__(self) -> int:
        return len(self._nodes)

    def __getitem__(self, i: int) -> Node:
        return self._nodes[i]

    def __iter__(self):
        return iter(self._nodes)

    @property
    def n_dof(self) -> int:
        return DOF_PER_NODE * len(self._nodes)

    def coords(self) -> NDArray[np.float64]:
        """``(n_nodes, 3)`` in numbering order."""
        if not self._nodes:
            return np.zeros((0, 3), dtype=np.float64)
        return np.array([n.xyz for n in self._nodes], dtype=np.float64)


def node_dofs(index: int) -> NDArray[np.int64]:
    """The six global DOF indices owned by node ``index``.

    Same role as `io/frames.hydro_to_global`: the mapping is structural rather
    than remembered, so no call site writes ``6 * i + 3`` by hand. That arithmetic
    is where an off-by-one lands in a stiffness row and looks like a physical
    asymmetry.
    """
    if index < 0:
        raise IndexError(f"node index must be non-negative; got {index}")
    base = DOF_PER_NODE * index
    return np.arange(base, base + DOF_PER_NODE, dtype=np.int64)


def element_dofs(node_a: int, node_b: int) -> NDArray[np.int64]:
    """The twelve global DOF indices of a two-node element, A then B."""
    if node_a == node_b:
        raise ValueError(
            f"element connects node {node_a} to itself; a zero-length member has "
            "no axis and its local triad is undefined."
        )
    return np.concatenate([node_dofs(node_a), node_dofs(node_b)])


@dataclass
class Model:
    """The container F2 assembles from. Elements are added in later steps."""

    nodes: NodeSet = field(default_factory=NodeSet)

    @property
    def n_dof(self) -> int:
        return self.nodes.n_dof
