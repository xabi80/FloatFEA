"""No undeclared tolerance may reach a comparison (BD4). AST, not regex.

`CLAUDE.md` § Tolerances: every numerical tolerance lives in
`floatfea/tolerances.py`. That was a rule, and it was broken three times -- an
undeclared `rtol=1e-10` (AW2), then `rel=1e-6` and `> 1e4` two commits after AW2
closed (R13), then a regex scanner that missed 13 of 15 planted shapes.

Why the regex failed, and why this walks the AST instead
--------------------------------------------------------
The regex cleared a whole LINE if a tolerance name appeared anywhere on it --
including inside the f-string message -- so
``pytest.approx(PATCH_TEST_EXACTNESS, rel=0.99)`` read clean. It also keyed on
lines beginning ``assert ``, so ``np.testing.assert_allclose(...)`` was invisible,
and on a fixed keyword set, so ``matrix_rank(tol=...)`` was invisible.

Walking the AST closes all three by construction: the check is on the *argument
node*, message strings are not on that path, and every comparison call is found
wherever it sits.

What is flagged
---------------
* any keyword named ``tol``/``atol``/``rtol``/``abs``/``rel`` whose value carries
  a numeric constant;
* the second positional argument of ``approx`` -- its tolerance slot;
* a bare ``pytest.approx(x)`` with no ``abs``/``rel``, itself an undeclared
  tolerance since it defaults to ``rel=1e-6, abs=1e-12``;
* a float threshold on the RIGHT of a comparison, other than ``0.0`` or ``1.0``,
  which are canonical structural bounds; integers are counts and are never
  flagged. **The left operand is not read** (R237): ``assert 0.05 > ratio``
  returns nothing, and this list said "any float threshold" while two live sites
  sit on that side. Widening it to ``node.left`` is a change to the guard's
  reach and belongs to step 4a; the sentence is what was false and it is fixed
  here.

Each must resolve to a `Name` imported from `floatfea.tolerances`, or be a call to
`floatfea.testing.assert_close` / `assert_differs`, which carry their own floor.
"""

from __future__ import annotations

import ast
import io
import tokenize
from pathlib import Path

import pytest

TESTS = Path(__file__).resolve().parent
TOL_KEYWORDS = {"tol", "atol", "rtol", "abs", "rel"}
APPROX_NAMES = {
    "approx",
    "assert_allclose",
    "allclose",
    "isclose",
    "assert_array_almost_equal",
    "almost_equal",
}
SAFE_CALLS = {"assert_close", "assert_differs"}
EXEMPT = "not-a-tolerance:"


def _marker_lines(src: str) -> set[int]:
    """Lines carrying the exemption marker IN A COMMENT, never in a string (CB0).

    The marker used to be matched against raw text, so
    `assert residual < 1e-9, "not-a-tolerance: for context"` exempted the
    comparison -- in a file whose own docstring says message strings are not on
    that path. Tokenising makes that docstring true: a COMMENT token is a
    comment by the grammar, not by a substring search.
    """
    lines: set[int] = set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT and EXEMPT in tok.string:
                lines.add(tok.start[0])
    except (tokenize.TokenError, IndentationError, SyntaxError):
        # A file that does not tokenise does not parse either, and `ast.parse`
        # raises with a better message. NEVER fall back to the text scan: that
        # is the hole this function closes.
        return set()
    return lines


def _tolerance_names() -> set[str]:
    from floatfea import tolerances

    return {n for n in dir(tolerances) if n.isupper()}


def _declared(node: ast.AST, names: set[str]) -> bool:
    """True if this argument resolves to a declared tolerance name."""
    for sub in ast.walk(node):
        if isinstance(sub, ast.Name) and sub.id in names:
            return True
        if isinstance(sub, ast.Attribute) and sub.attr in names:
            return True
    return False


def _has_number(node: ast.AST) -> bool:
    return any(
        isinstance(s, ast.Constant)
        and isinstance(s.value, (int, float))
        and not isinstance(s.value, bool)
        for s in ast.walk(node)
    )


def _call_name(node: ast.Call) -> str:
    f = node.func
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Name):
        return f.id
    return ""


def offending(path: Path) -> list[tuple[int, str]]:
    names = _tolerance_names()
    src = path.read_text(encoding="utf-8")
    marked = _marker_lines(src)
    tree = ast.parse(src)

    # THE MARKER ANNOTATES THE STATEMENT IT SITS IN (CA0). Keyed to a single line
    # number it was voided by any reformatting: `black` split single-line calls
    # across lines, the trailing comment stayed at the end, the flagged node's
    # `lineno` moved to the start, and nine files went red on markers that had
    # been placed correctly. A guard whose exemptions depend on line breaks is a
    # guard that a formatter silently rewrites.
    #
    # A COMPOUND STATEMENT GETS ONLY ITS HEADER, and the header ends at the first
    # DESCENDANT STATEMENT rather than at `body[0]` (CB0). `ast.Match` has no
    # `body` attribute -- its blocks hang off `cases` -- so keying on `body`
    # sent every `match` to the whole-statement branch and one marker anywhere
    # in it exempted every comparison in every case. That is precisely the "far
    # larger hole" this paragraph claimed to avoid, in the one compound
    # statement it did not name. The minimum over descendant statements covers
    # `Match`, `Try`, `If/else` and anything added later, by construction.
    marker_span: dict[int, set[int]] = {}
    for stmt in ast.walk(tree):
        if not isinstance(stmt, ast.stmt):
            continue
        inner = [n.lineno for n in ast.walk(stmt) if isinstance(n, ast.stmt) and n is not stmt]
        if inner:
            span = range(stmt.lineno, min(inner))
        else:
            span = range(stmt.lineno, (stmt.end_lineno or stmt.lineno) + 1)
        for m in marked:
            if m in span:
                marker_span.setdefault(m, set()).update(span)
    for m in marked:
        marker_span.setdefault(m, {m})

    candidates: list[tuple[int, int, str, int]] = []

    def flag(node: ast.AST, why: str) -> None:
        # KEYED ON THE NODE, not on the value (CD2). A chained comparison
        # `0.34 < x < 0.3536` is ONE `Compare` with a threshold on each side, so
        # reading both sides made it two candidates -- and "one marker exempts
        # one node" then left the second reported on two correctly-marked live
        # sites. A marker annotates the comparison; a chain is one comparison.
        candidates.append((node.lineno, getattr(node, "col_offset", 0), why, id(node)))

    # CLAUDE.md sec. Tolerances names three things, and the scanner read one of
    # them (CD2). "No exceptions, no local literals, NO DEFAULT ARGUMENTS
    # CARRYING A TOLERANCE" -- both of the other two were written out verbatim
    # by the reviewer and both scanned clean. A guard that misses the rule it
    # quotes is the shape this milestone keeps finding.
    #
    # A module-level `NAME = <float>` used as a threshold is a local literal
    # wearing a name; the indirection is the point of the clause.
    local_floats: dict[str, float] = {}
    for stmt in tree.body:
        if (
            isinstance(stmt, ast.Assign)
            and isinstance(stmt.value, ast.Constant)
            and isinstance(stmt.value.value, float)
        ):
            for tgt in stmt.targets:
                if isinstance(tgt, ast.Name) and tgt.id not in names:
                    local_floats[tgt.id] = stmt.value.value

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = node.args
            for arg, default in zip(
                args.args[len(args.args) - len(args.defaults) :],
                args.defaults,
                strict=True,
            ):
                if (
                    arg.arg in TOL_KEYWORDS
                    and _has_number(default)
                    and not _declared(default, names)
                ):
                    flag(node, f"default argument {arg.arg}=<literal>")
        if isinstance(node, ast.Call):
            cname = _call_name(node)
            if cname in SAFE_CALLS:
                continue
            for kw in node.keywords:
                if kw.arg in TOL_KEYWORDS and _has_number(kw.value):
                    # `rtol=0` DISABLES a tolerance rather than setting one --
                    # there is no value to declare, and flagging it would push
                    # callers toward a non-zero default they did not choose.
                    zero = isinstance(kw.value, ast.Constant) and kw.value.value == 0
                    if not zero and not _declared(kw.value, names):
                        flag(node, f"{cname}({kw.arg}=<literal>)")
            if cname == "approx":
                if len(node.args) > 1 and not _declared(node.args[1], names):
                    flag(node, "approx(_, <literal>)")
                if not node.keywords and len(node.args) == 1:
                    flag(
                        node,
                        "approx() with NO abs/rel -- its defaults "
                        "(rel=1e-6, abs=1e-12) are an undeclared tolerance",
                    )
        elif isinstance(node, ast.Compare):
            # BOTH SIDES (R237, closed at CD2). `node.left` was never read, so
            # `assert 0.05 > ratio` was invisible while this file's own "What is
            # flagged" list promised any float threshold. Six of seventeen known
            # misses were that one omission, and the quarter-rule below is what
            # made closing it the answer rather than listing them.
            for comp in [node.left, *node.comparators]:
                # Any FLOAT threshold, at any magnitude: `> 1e4` is as much a
                # tolerance as `< 0.05`, and the first is what R13 named.
                # Integers are counts and 0.0 / 1.0 are canonical structural
                # bounds ("is this non-zero", "is this a ratio above unity").
                if (
                    isinstance(comp, ast.Constant)
                    and isinstance(comp.value, float)
                    and abs(comp.value) not in (0.0, 1.0)
                ):
                    flag(node, f"comparison against {comp.value!r}")
                elif (
                    isinstance(comp, ast.UnaryOp)
                    and isinstance(comp.op, ast.USub)
                    and isinstance(comp.operand, ast.Constant)
                    and isinstance(comp.operand.value, float)
                    and abs(comp.operand.value) not in (0.0, 1.0)
                ):
                    # A NEGATIVE LITERAL IS NOT A `Constant` NODE. `-1e-09`
                    # parses as `UnaryOp(USub, Constant)`, so the flat branch
                    # above never saw it. Narrow on purpose: scanning every
                    # expression that merely CONTAINS a float reddened seven
                    # correct files, and adding markers to seven correct files
                    # is the growth CD1's bound exists to stop.
                    flag(node, f"comparison against -{comp.operand.value!r}")
                elif isinstance(comp, ast.Name) and comp.id in local_floats:
                    flag(
                        node,
                        f"comparison against {comp.id}, a module-level "
                        f"{local_floats[comp.id]!r} -- a local literal with a name",
                    )

    # ONE MARKER EXEMPTS AT MOST ONE NODE (CB0). The statement window let a
    # single marker cover every flaggable node in its span, so a two-clause
    # assertion with a marker on the first clause exempted the second as well --
    # nineteen of the reviewer's twenty-eight shapes, every one of which the
    # line-keyed window this replaced had caught. Exemptions are consumed in
    # source order, so a marker annotates the node it sits nearest and every
    # other flaggable node in the same statement is still reported.
    # ONE MARKER, ONE FLAGGED VALUE -- not one node (CE3, the reviewer's ruling).
    # Node-keying was chosen here to keep two bracket assertions clean, and it
    # reinstated CB0's own hole one level down: `assert 1e-09 < r < 0.05` with a
    # marker saying only the lower bound is deliberate scanned clean, because one
    # marker covered both thresholds of one `Compare`. The option set was wrong:
    # value-keying plus ONE MORE marker comment in each of those two statements
    # leaves both files clean, measured, at a cost of two comment lines.
    used: set[int] = set()
    out: list[tuple[int, str]] = []
    for lineno, _col, why, _node_id in sorted(set(candidates)):
        claim = next(
            (m for m in sorted(marker_span) if m not in used and lineno in marker_span[m]),
            None,
        )
        if claim is None:
            out.append((lineno, why))
        else:
            used.add(claim)
    return sorted(set(out))


def _test_files() -> list[Path]:
    return sorted(p for p in TESTS.rglob("test_*.py") if p.name != Path(__file__).name)


# --------------------------------------------------------------------------
# The scanner's own tests. The fifteen shapes are the ones the regex version
# was measured against: it caught two.
# --------------------------------------------------------------------------
PLANTED = [
    "assert a == pytest.approx(b, rel=1e-6)",
    "assert spread > 1e4",
    "assert np.linalg.matrix_rank(k, tol=1e-9 * abs(k).max()) == 6",
    "np.testing.assert_allclose(a, b, atol=1e-12)",
    "assert np.allclose(a, b, rtol=0, atol=1e-9)",
    "assert np.isclose(x, 0.0, atol=1e-12)",
    "assert a == pytest.approx(PATCH_TEST_EXACTNESS, rel=0.99)",
    "assert a == pytest.approx(b)",
    "assert ratio < 0.05",
    "np.testing.assert_array_almost_equal(a, b, atol=1e-8)",
    "assert err <= 1e-13",
    "assert abs(x - y) < 0.001",
    "assert v == pytest.approx(1.0, abs=5e-4)",
    "assert np.allclose(a, b, atol=2e-15 * scale)",
    "assert q > 0.15",
]

_HEADER = (
    "import numpy as np\n"
    "import pytest\n"
    "from floatfea.testing import assert_close\n"
    "from floatfea.tolerances import (MATRIX_SYMMETRY, PATCH_TEST_EXACTNESS,\n"
    "                                 ROUNDOFF_IDENTITY)\n"
    "def test_x():\n    "
)


def test_the_scanner_catches_every_planted_shape(tmp_path: Path) -> None:
    """All fifteen. The regex this replaces caught two of them."""
    missed = []
    for i, line in enumerate(PLANTED):
        p = tmp_path / f"test_p{i}.py"
        p.write_text(_HEADER + line + "\n", encoding="utf-8")
        if not offending(p):
            missed.append(line)
    assert not missed, f"{len(missed)} of {len(PLANTED)} shapes missed:\n" + "\n".join(missed)


def test_declared_usages_are_NOT_flagged(tmp_path: Path) -> None:
    """A corpus that must stay clean, or the scanner is unusable and gets removed."""
    ok = [
        "assert a == pytest.approx(b, rel=ROUNDOFF_IDENTITY)",
        "assert np.allclose(a, b, rtol=0, atol=MATRIX_SYMMETRY * s)",
        "assert err <= PATCH_TEST_EXACTNESS",
        "assert_close(a, b, ROUNDOFF_IDENTITY, floor=1e-16)",
        "assert n >= 32",
        "assert np.abs(x).max() > 0.0",
        "assert mask.sum() == 5",
    ]
    for i, line in enumerate(ok):
        p = tmp_path / f"test_ok{i}.py"
        p.write_text(_HEADER + line + "\n", encoding="utf-8")
        assert not offending(p), f"false positive on: {line}"


def test_the_annotation_exempts_a_line(tmp_path: Path) -> None:
    p = tmp_path / "test_e.py"
    p.write_text(
        "def test_x():\n    assert q > 0.15  # not-a-tolerance: mesh station\n",
        encoding="utf-8",
    )
    assert not offending(p)


def test_there_are_test_files_to_scan() -> None:
    assert len(_test_files()) > 5, "the scan is vacuous"


@pytest.mark.parametrize("path", _test_files(), ids=lambda p: p.name)
def test_no_undeclared_tolerance_reaches_a_comparison(path: Path) -> None:
    bad = offending(path)
    assert not bad, (
        f"{path.name}:\n"
        + "\n".join(f"  line {n}: {w}" for n, w in bad)
        + "\n\nDeclare the value in floatfea/tolerances.py, use "
        "floatfea.testing.assert_close, or annotate `# not-a-tolerance: <what the "
        "quantity is and why it is an input, not a comparison>`."
    )
