"""No undeclared tolerance may reach a comparison (BD4). AST, not regex.

`CLAUDE.md` § Tolerances: every numerical tolerance lives in
`floatfea/tolerances.py`. That was a rule, and it was broken three times -- an
undeclared `rtol=1e-10` (AW2), then `rel=1e-6` and `> 1e4` two commits after AW2
closed (R13), then a regex scanner that missed 13 of 15 planted shapes.

AND IT IS BROKEN RIGHT NOW, IN THE TREE THIS FILE PROTECTS (R379). The
paragraph above cited `rtol=1e-10` as a CLOSED breach; one stands undeclared at
`floatfea/io/reader.py:223` on the inertia-symmetry check, beside `rtol=1e-9`
at `:206`, `atol=1e-9` at `:155` and `atol=1e-12` at `floatfea/io/frames.py:358`.
All four have been there since F1 and THIS GUARD HAS NEVER LOOKED: its domain
is `TESTS.rglob("test_*.py")`, so the package it exists to protect has been
outside its reach throughout. Three of the four decide whether a record is
REJECTED. They are declared under `docs/milestones/F2.md` §D5a, at their
identical values, and the domain widens there -- in that order, because
widening it first reddens the build for work that has not happened yet.

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
* a float threshold on EITHER side of a comparison, other than ``0.0`` or
  ``1.0``, which are canonical structural bounds; integers are counts and are
  never flagged. A negated literal counts, since ``-1e-9`` is a ``UnaryOp`` and
  not a ``Constant``;
* a module-level name bound to a float literal and used as a threshold, and a
  default argument named like a tolerance carrying one -- the two clauses of
  ``CLAUDE.md`` § Tolerances that this list did not read;

  This paragraph has been wrong twice in opposite directions (R255, R269). It
  first said "any float threshold" while only the right operand was read; the
  round that read the left operand left the sentence saying it did not. What is
  NOT read is listed in ``tests/test_marker_exemption_corpus.py`` by species,
  measured against the reviewer's shapes, rather than described here.

Each must resolve to a `Name` imported from `floatfea.tolerances`, or be a call to
`floatfea.testing.assert_close` / `assert_differs`, which carry their own floor.
"""

from __future__ import annotations

import ast
import io
import math
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


def _floats_in(node: ast.AST) -> list[float]:
    """Every float literal in an expression, signed."""
    out: list[float] = []
    for inner in ast.walk(node):
        if isinstance(inner, ast.UnaryOp) and isinstance(inner.op, ast.USub):
            if isinstance(inner.operand, ast.Constant) and isinstance(inner.operand.value, float):
                out.append(-inner.operand.value)
        elif (
            isinstance(inner, ast.Constant)
            and isinstance(inner.value, float)
            and not any(isinstance(u, ast.UnaryOp) and u.operand is inner for u in ast.walk(node))
        ):
            out.append(inner.value)
    return [v for v in out if abs(v) not in (0.0, 1.0)]


_ARITH = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Pow)


def _folds_to_a_small_constant(node: ast.AST) -> float | None:
    """The value of a wholly-constant arithmetic expression, if it is under 1.

    CP4, first species. `assert r < 1/1000000` has no float node in it at all:
    two integers and a `Div`, and `_floats_in` looks for `Constant` floats. The
    scanner's own docstring says "any FLOAT threshold, at any magnitude", and
    integers are excused as counts -- which is right for `2` and wrong for a
    quotient of two of them that is a millionth.

    UNDER ONE, AND NOT ZERO, is the bound and it is not arbitrary: a constant
    expression that folds to something smaller than unity is standing where a
    tolerance stands. Above one it is a scale or a count and this says nothing
    about it, which keeps the rule off the 41 correct files the wide version
    reddened.
    """
    # ONLY AN ARITHMETIC EXPRESSION, never a bare constant. A `Constant` is
    # what every rule above this one already reads, and folding one here
    # reported `0.0`, `1.0` and every integer count in the tree -- measured at
    # 38 failures in the corpus before this line was written.
    sign = 1.0
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        node, sign = node.operand, -1.0
    if not isinstance(node, ast.BinOp) or not isinstance(node.op, _ARITH):
        return None
    inner = _folds_to_a_small_constant_raw(node)
    value = None if inner is None else sign * inner
    if value is None or value == 0.0 or abs(value) >= 1.0:
        return None
    return value


def _folds_to_a_small_constant_raw(node: ast.AST) -> float | None:
    """The arithmetic value of `node`, or `None` if anything in it is not a
    numeric constant. No names, no calls, no subscripts: a name could be a
    declared tolerance and folding it away is how a declared value gets read
    as a literal."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            return None
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _folds_to_a_small_constant_raw(node.operand)
        return None if inner is None else -inner
    if isinstance(node, ast.BinOp) and isinstance(node.op, _ARITH):
        left = _folds_to_a_small_constant_raw(node.left)
        right = _folds_to_a_small_constant_raw(node.right)
        if left is None or right is None:
            return None
        try:
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.FloorDiv):
                return float(left // right)
            return float(left**right)
        except (ZeroDivisionError, OverflowError, ValueError):
            return None
    return None


def _float_of_a_string(node: ast.AST) -> float | None:
    """The value of `float("...")` with a literal string, if it is a tolerance.

    CP4, second species. The number is inside a string, so no `Constant` float
    exists anywhere in the tree and every rule above it looks past. `0.0` and
    `1.0` are excused here for the same reason they are excused everywhere in
    this file: they are structural bounds rather than tolerances.
    """
    if not isinstance(node, ast.Call) or _call_name(node) != "float":
        return None
    if len(node.args) != 1 or node.keywords:
        return None
    arg = node.args[0]
    if not isinstance(arg, ast.Constant) or not isinstance(arg.value, str):
        return None
    try:
        value = float(arg.value)
    except ValueError:
        return None
    # INFINITY AND NaN ARE NOT TOLERANCES (R381). `float("inf")` is the
    # absence of a bound, and it is the one spelling here with no bare-literal
    # form for the older rules to be consistent with -- so this rule would
    # report it and every other rule in the file would not.
    if not math.isfinite(value):
        return None
    return None if abs(value) in (0.0, 1.0) else value


# WHAT LEAVES A DECLARED VALUE ALONE, per operator. `* 1` and `/ 1` are
# identities; `+ 1` is not, and excusing magnitude 1 everywhere -- which is
# what every other rule in this file does, correctly, for a bare literal --
# let `DECLARED + 1` through while catching `DECLARED * 10`. Measured before
# this table replaced it.
# WHAT LEAVES A DECLARED VALUE ALONE, PER OPERATOR AND PER SIDE (CR1, R389).
# The first version of this table had no side and four of its eight operators
# are not commutative, so it read `1 / DECLARED` as an identity. That is a
# RECIPROCAL -- a conditioning ceiling fifteen orders from the declared value,
# and not an exotic line in this repository. `1 ** DECLARED` is the constant
# one with the name decorative; `0 - DECLARED` is a sign flip.
#
#   (left identity, right identity), `None` where no constant leaves it alone
_IDENTITY: dict[type, tuple[float | None, float | None]] = {
    ast.Add: (0.0, 0.0),
    ast.Sub: (None, 0.0),
    ast.Mult: (1.0, 1.0),
    ast.Div: (None, 1.0),
    ast.FloorDiv: (None, 1.0),
    ast.Pow: (None, 1.0),
    ast.LShift: (None, 0.0),
    ast.RShift: (None, 0.0),
    ast.Mod: (None, None),
    ast.BitXor: (None, None),
    ast.BitOr: (None, None),
    ast.BitAnd: (None, None),
    ast.MatMult: (None, None),
}

# Calls that return the number handed to them, so `DECLARED * float(2)` is
# `DECLARED * 2`. `np.float64(...)` arrives as an Attribute call.
_NUMERIC_CALLS = ("float", "int", "abs", "float64", "float32", "double")


def _const_value(node: ast.AST) -> float | None:
    """The value of a wholly constant expression, or `None` (CR1).

    RECURSIVE, which is the half of R389 the previous version got wrong by
    assertion: its docstring said "every nested BinOp is visited ... reached
    as somebody's operand", and `(1 + 1)` holds no declared name, so the
    caller skipped it and the outer operand was a BinOp that nothing read.
    A declared tolerance DOUBLED by `* (1 + 1)` reached the comparison with
    nothing looking at it.

    Names are never constant here. A name could BE the declared tolerance,
    and folding it away would read a declared value as a literal.
    """
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            return None
        return float(node.value)
    if isinstance(node, ast.UnaryOp):
        inner = _const_value(node.operand)
        if inner is None:
            return None
        if isinstance(node.op, ast.USub):
            return -inner
        if isinstance(node.op, ast.UAdd):
            return inner
        return None
    if isinstance(node, ast.Call) and _call_name(node) in _NUMERIC_CALLS:
        if len(node.args) != 1 or node.keywords:
            return None
        return _const_value(node.args[0])
    if isinstance(node, ast.BinOp):
        left, right = _const_value(node.left), _const_value(node.right)
        if left is None or right is None:
            return None
        try:
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.FloorDiv):
                return float(left // right)
            if isinstance(node.op, ast.Pow):
                return float(left**right)
            if isinstance(node.op, ast.Mod):
                return float(left % right)
        except (ZeroDivisionError, OverflowError, ValueError):
            return None
    return None


def _numbers_beside_a_declared_name(node: ast.AST, names: set[str]) -> list[float]:
    """Constants that CHANGE a declared tolerance, on either side (CR1).

    An integer alone in a comparison is a count and is excused everywhere
    else in this file. Beside a DECLARED tolerance it is a scale, and so is a
    compound expression that folds to one: `DECLARED * (1 + 1)` doubles it.

    THE OTHER SIDE MUST CARRY THE DECLARED NAME. `RIGID_BODY_MODE_RATIO *
    w[RIGID - 1]` is a tolerance scaled by DATA, which is the relative-
    tolerance idiom and is not a new bound; the `1` inside that subscript is
    an index. So a constant is only read when the name is opposite it.
    """
    if not isinstance(node, ast.BinOp):
        return []
    left_id, right_id = _IDENTITY.get(type(node.op), (None, None))
    out: list[float] = []
    for side, other, identity in (
        (node.left, node.right, left_id),
        (node.right, node.left, right_id),
    ):
        value = _const_value(side)
        if value is None or (identity is not None and value == identity):
            continue
        if not any(isinstance(n, ast.Name) and n.id in names for n in ast.walk(other)):
            continue
        out.append(value)
    return out


def _literal_thresholds_inside(comp: ast.AST, names: set[str]) -> list[str]:
    """Float literals inside a comparator that ARE thresholds (R326).

    NOT EVERY FLOAT IN AN EXPRESSION. Walking the whole comparator flags 41
    correct files in this repository -- a scale, a physical constant, an index
    arithmetic -- and adding markers to 41 correct files is the growth CD1's
    bound exists to stop. The recorded warning on the narrow branch above said
    exactly that, and it was measured again here before this rule was written.

    What makes a literal a THRESHOLD rather than a number is that it stands in
    the place a declared tolerance stands in:

      * it MODIFIES a declared tolerance -- `1e12 * BAND`, `BAND / 4.0`,
        `BAND + 0.5`, and the same with the declared name on either side. The
        product is the bound the comparison uses, and it is not the declared
        one;
      * it is a candidate inside `min(...)` or `max(...)`, where the smallest
        or largest wins and a literal among the candidates can be the bound;
      * it is an element of a tuple or list that the comparator subscripts,
        which is a table of bounds written inline.

    These are the nine shapes the reviewer's corpus names, and the escalation
    condition the repository wrote for itself -- "unless one exposes a false
    pass on a real file in the tree" -- fired on the first of them.
    """
    out: list[str] = []
    # THE SAME ARITHMETIC EXPRESSION, not merely the same comparator. Reading
    # the whole comparator flagged `pytest.approx(0.6 * fy, rel=DECLARED)` --
    # a physical factor in the value and a declared tolerance in `rel`, two
    # unrelated numbers sharing a line. The shape that matters is a literal
    # and a declared name inside ONE `BinOp`, where the product is the bound.
    for inner in ast.walk(comp):
        if not isinstance(inner, ast.BinOp):
            continue
        declared = {n.id for n in ast.walk(inner) if isinstance(n, ast.Name) and n.id in names}
        if not declared:
            continue
        # CQ3: INTEGERS COUNT HERE. Everywhere else in this file an integer is
        # a count and is excused; beside a declared tolerance it is a scale,
        # and `DECLARED * 10` is as much a new bound as `DECLARED * 2.0`.
        for value in _numbers_beside_a_declared_name(inner, names):
            out.append(
                f"comparison against {value!r} combined with "
                f"{sorted(declared)[0]} -- the bound is the product, not the "
                "declared value"
            )
    if out:
        return out
    # CP4: THE TWO SPECIES THAT ARE NOT FLOAT NODES. Everything above looks
    # for a `Constant` float somewhere; these two put a tolerance in a
    # comparison without one existing in the tree.
    for inner in ast.walk(comp):
        folded = _folds_to_a_small_constant(inner)
        if folded is not None:
            out.append(
                f"comparison against a constant expression folding to "
                f"{folded!r} -- a tolerance with no float literal in it"
            )
        as_string = _float_of_a_string(inner)
        if as_string is not None:
            out.append(
                f"comparison against float(<string>) = {as_string!r} -- the "
                "number is inside a string and no rule above sees it"
            )
    if out:
        return out
    for inner in ast.walk(comp):
        if (
            isinstance(inner, ast.Call)
            and isinstance(inner.func, ast.Name)
            and inner.func.id in ("min", "max")
        ):
            for value in _floats_in(inner):
                out.append(f"comparison against {inner.func.id}(... {value!r} ...)")
        if isinstance(inner, ast.Subscript) and isinstance(inner.value, (ast.Tuple, ast.List)):
            for value in _floats_in(inner.value):
                out.append(f"comparison against an inline table holding {value!r}")
    return out


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
            #
            # AND INSIDE THE EXPRESSION, NOT ONLY AT ITS ROOT (R326). A
            # comparator is an expression: `1e12 * DECLARED`, `DECLARED / 4.0`,
            # `min(x, 0.05)`, `bounds[1]`. Reading only a bare `Constant` and a
            # negated one left every arithmetic form invisible, and the bound in
            # `tests/test_marker_exemption_corpus.py` that filed those as known
            # misses said they stayed 4a "unless one exposes a false pass on a
            # real file in the tree". One did: `assert drift > 1e12 * BAND`
            # shipped in `tests/verification/rung4`. The condition the
            # repository wrote for itself fired, so the misses are closed here
            # rather than re-listed.
            #
            # THE WALK IS OVER THE WHOLE COMPARATOR and it stops at a call's
            # arguments only to the extent that a call IS an expression: a
            # threshold handed to `min` is a threshold. What it still does not
            # see is a threshold that never appears as a literal at all -- a
            # value read from a file, or computed -- and that is stated in the
            # reach below rather than implied away.
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
                    # above never saw it.
                    flag(node, f"comparison against -{comp.operand.value!r}")
                else:
                    for reason in _literal_thresholds_inside(comp, names):
                        flag(node, reason)
                if isinstance(comp, ast.Name) and comp.id in local_floats:
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
