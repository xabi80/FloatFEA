"""Prose in the source tree does not claim things about the code (CW0, CW1).

`tests/test_report_numbers_are_sourced.py` makes a number in a step report
carry the command that produced it, and stops at `docs/reports/`. This file is
the same discipline for the rest of the tree, at its second shape.

WHY THE FIRST SHAPE IS GONE. CV0 built two DETECTORS beside the triple runner:
a keyword list for absence claims and an alias list for retired quantities.
The reviewer measured them against unseen phrasings in
`tests/corpus/tree_prose_claims.txt` and got **0 of 20** and **3 of 8** -- the
only shapes either caught were the ones their author had written. A probe over
this file's own roots found 21 absence-shaped paragraphs the pattern missed
against 13 it matched. That is not a list that converges with another round of
words in it: the defect is a sentence making an unchecked claim, and "makes an
unchecked claim" is not a keyword.

So the rule is smaller and it is a prohibition rather than a search. **Prose
here does not assert what the code does or does not do.** A claim is one of
three things:

  * a test, which is the normal case and always was;
  * a TRIPLE, checked by this file;
  * deleted.

The reviewer reads for the fourth case. Three rounds running it has found
those sentences by reading, and by measurement it is better at it than any
pattern written here -- R436's two were in docstrings the same round rewrote,
and neither phrasing was in the list.

THE TRIPLE

    claim: <one sentence about what this repository contains>
    cmd:   <a call from the vocabulary below>
    ctl:   <an id in tests/prose_triple_controls.txt>    (see NEGATIVE CONTROL)
    out:   <what that call returns>

The vocabulary is `count`, `lines`, `files`, `defined` and nothing else: the
expression is PARSED and refused unless it is one of those four names applied
to string literals, because `eval` over a comment in the source tree is
otherwise a way to run anything from a docstring.

NEGATIVE CONTROL, AND WHAT IT IS AND IS NOT (R434, corrected at R469). A
command whose answer is `none` or a count proves nothing about a needle nobody
has looked at. The needle that failed was a retired ceiling's name with a right
paren after it -- spelled out nowhere here, because naming it would put this
file into the answer of the very command it is the example for -- and it
matches nothing anywhere, so it printed `none` whatever the tree did, under a
claim that was false in both halves and now looked certified.

So every triple reporting an absence or a count REGISTERS its needle, by exact
text, in `tests/prose_triple_controls.txt`, and this file refuses a needle that
is not registered, is registered twice, or differs from its registration by so
much as a space.

**REGISTRATION IS NOT FINDABILITY, and the earlier wording here claimed it
was.** Under the equality rule the planted line IS the needle, so "the same
needle is found there" is true by construction for every needle a triple
declares and demonstrates nothing about the tree. What registration buys is
that a reader sees the exact string the claim rests on, in one file, without
reading the claim -- a decision made visible, not a property proved. The
fifty-second verdict measured this over unseen defect shapes -- needles
registered, claims false, and most of them green -- and the count lives there,
in `docs/reviews/F2/step-5.md` under R469. It is not repeated here: nothing in
this tree regenerates it, and a figure nothing regenerates goes stale in place
(BI3). The mechanism that would close that is frozen into 4a's
list in `docs/milestones/F2a.md`; the
direction is still right, because it refuses every re-admission through a
plausible-looking fake control line and a file of bare needles is the one an
adversarial reader can check.

WHAT THIS STILL DOES NOT DO, said plainly:

* it checks the triples that exist. A sentence with no triple is invisible to
  it -- that is the reviewer's half, and it is now the stated division of
  labour rather than a gap left by a list;
* a triple proves its `out` is current and its needle is findable. It does not
  prove the `claim` sentence is what the `cmd` measures. R434 and R435 were
  both that failure, and both would have survived a green run of this file;
  the answer is that a human reads the claim against the command, which is
  what the reviewer did.
"""

from __future__ import annotations

import ast
import io
import re
import tokenize
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

# `docs/verification/` IS IN SCOPE FROM CW1 (R437). The ladder document is what
# `CLAUDE.md` § Testing names as the ordering authority, and it defined G2.1 by
# a quantity retired two steps earlier while four roots that excluded it were
# being checked. `CLAUDE.md` itself is in scope for the same reason.
ROOTS = ("floatfea", "tests", "scripts", "docs/milestones", "docs/verification")
EXTRA_FILES = ("CLAUDE.md",)

# `docs/reports/` is NOT in scope: a step report is a record of a moment rather
# than a description of the tree, and revision 14 must keep saying true things
# about a commit fourteen revisions back. It has its own guard.

CONTROLS = ROOT / "tests" / "prose_triple_controls.txt"
SELF = Path(__file__).resolve()


# --------------------------------------------------------------------------
# The vocabulary. This is the grep, and nothing else runs.
# --------------------------------------------------------------------------

# AN ANNOTATION LINE IS NOT PART OF THE TREE IT MEASURES: every `cmd:` contains
# the needle it searches for, so the first four triples written here counted
# themselves.
#
# KEYED ON THE PREFIX AT LINE START (CW0, R443b) AND DISAMBIGUATED BY A
# PARSE (CX2, R450). The first version matched any line beginning with
# `out:`, which includes a Python annotated assignment --
# `out: list[tuple[int, str]] = []` -- so a count over this file read one
# short. The second excluded any annotation line whose REST CONTAINED AN
# EQUALS SIGN, which is every `cmd:` whose needle has one: the single shipped
# triple searching for `log=True` then counted its own `claim:` and `cmd:`
# lines, `out: 4` became `out: 6`, and the claim was rewritten to justify the
# new number by naming two lines that do not exist.
#
# The question is whether the line is a Python ANNOTATED ASSIGNMENT, and that
# is a parse rather than a character. `ast` answers it exactly.
_ANNOTATION_PREFIX = re.compile(r"^[ \t]*(?:#[ \t]*)?(?:claim|cmd|ctl|out):")


def _is_annotated_assignment(line: str) -> bool:
    """`out: list[int] = []` is code; `out:   none` is an annotation.

    THE DISCRIMINATOR IS THE VALUE, not the parse. `cmd: count("a", "b")` is
    also a well-formed `AnnAssign` -- Python allows a bare annotation -- so
    testing the node type alone classified every `cmd:` line as code and
    stopped stripping it, which is the self-counting defect one turn later.
    What only code has is an assigned value.

    The cost, stated: a genuine bare Python declaration whose target is
    literally `claim`, `cmd`, `ctl` or `out` would be read as an annotation.
    There is none, and a four-name collision is a cheaper hole than the one
    this closes.
    """
    try:
        tree = ast.parse(line.strip())
    except SyntaxError:
        return False
    return (
        len(tree.body) == 1
        and isinstance(tree.body[0], ast.AnnAssign)
        and tree.body[0].value is not None
    )


def _is_annotation(line: str) -> bool:
    return bool(_ANNOTATION_PREFIX.match(line)) and not _is_annotated_assignment(line)


def _without_annotations(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not _is_annotation(line))


def _read(rel: str) -> str:
    return _without_annotations((ROOT / rel).read_text(encoding="utf-8", errors="replace"))


def _paths(pattern: str) -> list[Path]:
    """Every file matching `pattern`, which is a path or a glob under ROOT.

    AN EMPTY MATCH IS AN ERROR AND NOT AN ANSWER (R443a). A glob that reaches
    no file returned `none` from `files()` and `0` from `count()`, so a triple
    could certify an absence with a pattern that looked at nothing -- AM5's
    rule about empty parameter sets, inside this guard.
    """
    if any(ch in pattern for ch in "*?["):
        got = sorted(p for p in ROOT.glob(pattern) if p.is_file())
    else:
        got = [ROOT / pattern]
    # THERE IS NO IMPLICIT SCOPE (CY1, R459). Two files were excluded here --
    # the control file and this module -- and the cost was stated as "no
    # triple can make a claim about them". The real cost was larger and was
    # not stated: EVERY triple whose glob contains those files silently
    # changed answer, so `files()` stopped meaning what a reader's grep
    # means, and two published claims in `floatfea/tolerances.py` went false
    # in the same commit that narrowed the rule while their triples stayed
    # green.
    #
    # A pattern now searches what it says. A triple that wants a file out
    # writes a glob that leaves it out, visibly, in the `cmd:` a reader
    # sees -- and a triple's answer can never change because the runner
    # changed underneath it.
    if not got or not all(p.exists() for p in got):
        raise ValueError(f"the pattern {pattern!r} matches no file under the repository root")
    return got


def _text(p: Path) -> str:
    return _without_annotations(p.read_text(encoding="utf-8", errors="replace"))


def count(pattern: str, needle: str) -> int:
    """How many LINES across `pattern` contain `needle`, literally."""
    return sum(1 for p in _paths(pattern) for line in _text(p).splitlines() if needle in line)


def lines(rel: str, needle: str) -> str:
    """The 1-based line numbers in one file containing `needle`, comma-joined.

    Filtered in place rather than through `_read`, because dropping the
    annotation lines first would renumber every line after them.
    """
    _paths(rel)
    raw = (ROOT / rel).read_text(encoding="utf-8", errors="replace").splitlines()
    got = [str(i) for i, line in enumerate(raw, 1) if needle in line and not _is_annotation(line)]
    return ",".join(got) if got else "none"


def files(pattern: str, needle: str) -> str:
    """The files under `pattern` containing `needle`, comma-joined, or `none`."""
    got = [
        str(p.relative_to(ROOT)).replace("\\", "/") for p in _paths(pattern) if needle in _text(p)
    ]
    return ",".join(sorted(got)) if got else "none"


def defined(name: str) -> str:
    """`yes` if `floatfea/tolerances.py` declares this constant, else `no`."""
    hit = re.search(rf"^{re.escape(name)}\s*:", _read("floatfea/tolerances.py"), re.M)
    return "yes" if hit else "no"


_VOCABULARY = {"count": count, "lines": lines, "files": files, "defined": defined}


def _parse(expr: str) -> tuple[str, list[str]]:
    """`(name, string arguments)` for one `cmd:`, refusing anything else."""
    node = ast.parse(expr.strip(), mode="eval").body
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
        raise ValueError(f"not a call: {expr!r}")
    if node.func.id not in _VOCABULARY:
        raise ValueError(f"{node.func.id} is not in the vocabulary {sorted(_VOCABULARY)}")
    if node.keywords or not all(
        isinstance(a, ast.Constant) and isinstance(a.value, str) for a in node.args
    ):
        raise ValueError(f"arguments must be string literals: {expr!r}")
    return node.func.id, [a.value for a in node.args]


def _evaluate(expr: str) -> str:
    name, args = _parse(expr)
    return str(_VOCABULARY[name](*args))


def _needle(expr: str) -> str:
    """The string a command searches for: the last argument."""
    return _parse(expr)[1][-1]


# --------------------------------------------------------------------------
# Reading prose out of the tree
# --------------------------------------------------------------------------


def _python_prose(path: Path) -> list[tuple[int, str]]:
    """Comment and docstring lines only -- never executable code.

    An assertion MESSAGE is not a claim about the tree; it is a sentence the
    program prints when something else is wrong.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    out: list[tuple[int, str]] = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(text).readline):
            if tok.type == tokenize.COMMENT:
                out.append((tok.start[0], tok.string.lstrip("#").strip()))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return out
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        doc = ast.get_docstring(node, clean=False)
        if doc is None or not node.body:
            continue
        for k, line in enumerate(doc.splitlines()):
            out.append((node.body[0].lineno + k, line.strip()))
    return sorted(set(out))


def _markdown_prose(path: Path) -> list[tuple[int, str]]:
    out, fenced = [], False
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append((i, ""))
            continue
        out.append((i, "" if fenced else line.strip()))
    return out


def _prose_files() -> list[Path]:
    got: list[Path] = [ROOT / name for name in EXTRA_FILES]
    for where in ROOTS:
        for p in sorted((ROOT / where).rglob("*")):
            if p.suffix in (".py", ".md") and "__pycache__" not in str(p):
                got.append(p)
    return got


LINES_OF: dict[str, list[tuple[int, str]]] = {}
for _p in _prose_files():
    _rel = str(_p.relative_to(ROOT)).replace("\\", "/")
    LINES_OF[_rel] = _python_prose(_p) if _p.suffix == ".py" else _markdown_prose(_p)


# --------------------------------------------------------------------------
# The triples
# --------------------------------------------------------------------------

_CLAIM = re.compile(r"^claim:\s*(.+)$")
_CMD = re.compile(r"^cmd:\s*(.+)$")
_CTL = re.compile(r"^ctl:\s*(.+)$")
_OUT = re.compile(r"^out:\s*(.+)$")
_BARE_COUNT = re.compile(r"^\d+$")


Triple = tuple[str, int, str, str, str, str]


def _triples_in(rel: str, prose: list[tuple[int, str]]) -> list[Triple]:
    """`claim:` then `cmd:`, then an optional `ctl:`, then `out:`.

    A claim may WRAP: continuation lines before `cmd:` are part of the
    sentence. The other three may not -- a call, a control id and a result are
    one line each, and letting them wrap is how an earlier version swallowed
    the rest of the comment into `out`.
    """
    got: list[Triple] = []
    i, n = 0, len(prose)
    while i < n:
        m = _CLAIM.match(prose[i][1])
        if not m:
            i += 1
            continue
        start, claim, j = prose[i][0], m.group(1), i + 1
        while j < n and not _CMD.match(prose[j][1]) and prose[j][1]:
            claim += " " + prose[j][1]
            j += 1
        cmd = _CMD.match(prose[j][1]) if j < n else None
        if cmd is None:
            raise AssertionError(
                f"{rel}:{start} opens `claim:` and no `cmd:` follows it. A claim "
                f"without its command is the thing this file exists to refuse.\n"
                f"    {claim[:200]}"
            )
        j += 1
        ctl = ""
        ctl_match = _CTL.match(prose[j][1]) if j < n else None
        if ctl_match:
            ctl = ctl_match.group(1).strip()
            j += 1
        out = _OUT.match(prose[j][1]) if j < n else None
        if out is None:
            raise AssertionError(
                f"{rel}:{start} has `claim:` and `cmd:` and no `out:`.\n    {claim[:200]}"
            )
        # AN `out:` MAY CONTINUE ON FURTHER `out:` LINES, joined with nothing
        # between them. A list of file paths does not fit in a hundred columns
        # and shortening the answer to fit would be shortening what the
        # command is allowed to check. The continuation is bounded by the
        # marker itself -- the first line that is not `out:` ends it -- which
        # is why a bare wrap is still refused and why this cannot swallow the
        # rest of the comment, as an earlier version did.
        answer = out.group(1).strip()
        j += 1
        while j < n and _OUT.match(prose[j][1]):
            answer += _OUT.match(prose[j][1]).group(1).strip()
            j += 1
        got.append((rel, start, claim.strip(), cmd.group(1).strip(), ctl, answer))
        i = j
    return got


TRIPLES: list[Triple] = [
    t
    for rel, prose in LINES_OF.items()
    if rel != "tests/test_tree_prose_consistent.py"
    for t in _triples_in(rel, prose)
]

_CONTROL_LINES: dict[str, str] = {
    k.strip(): v.strip()
    for k, _, v in (
        line.partition(":")
        for line in CONTROLS.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    )
}

_FALLBACK = [("(none)", 0, "", "count('tests/**/*.py','x')", "", "0")]


def test_there_are_triples_to_run() -> None:
    """Meta-test: zero triples makes everything below a test of nothing."""
    assert len(TRIPLES) >= 6, (
        f"only {len(TRIPLES)} prose triple(s) found. Either the sentences lost "
        "their commands or the pattern stopped matching, and both make this "
        "file vacuous."
    )


def test_every_control_line_is_used_by_a_triple() -> None:
    """A planted line no triple names is a control for nothing."""
    named = {t[4] for t in TRIPLES if t[4]}
    unused = sorted(set(_CONTROL_LINES) - named)
    assert not unused, (
        f"{unused} are planted in {CONTROLS.name} and no triple names them. A "
        "control nothing runs is a line in a file."
    )


@pytest.mark.parametrize(
    "rel, start, claim, cmd, ctl, expected",
    TRIPLES or _FALLBACK,
    ids=[f"{r}:{s}" for r, s, *_ in TRIPLES] or ["(none)"],
)
def test_a_prose_triple_still_says_what_the_tree_says(
    rel: str, start: int, claim: str, cmd: str, ctl: str, expected: str
) -> None:
    """The sentence's own command, run here, against the `out` beside it."""
    if rel == "(none)":
        pytest.skip("reported by test_there_are_triples_to_run")
    got = _evaluate(cmd)
    assert got == expected.strip(), (
        f"{rel}:{start} claims:\n    {claim}\n"
        f"and its own command `{cmd}` returns `{got}`, not `{expected.strip()}`.\n"
        "Either the sentence is stale or the tree moved under it."
    )


def control_defect(cmd: str, ctl: str, answer: str) -> str | None:
    """Why this triple's negative control does not hold, or None (CX2).

    A FUNCTION, so the reviewer's re-admission shapes can be run against it
    directly. Three rules, each closing one hole it re-admitted R434 through:

      1. AN ABSENCE INCLUDES `no`. The requirement keyed on `none` or a bare
         count, and `defined("RIGID_MODE_BONUD")` returns `no` -- a
         misspelling certified as an absence with no control required at all.
      2. THE NEEDLE IS A TOKEN, not a token with whitespace around it.
         `"RIGID_MODE_FLOOR "` -- the name plus a trailing space -- answers
         `none` over `tests/` while the shipped control line contains it, so
         the control passed and the claim was false. A needle that differs
         from the thing it claims to be about by invisible characters is the
         R434 shape with a space instead of a paren.
      3. THE NEEDLE IS REGISTERED EXACTLY ONCE. Under equality a needle can
         match two planted lines only if two registrations are byte-identical,
         so this rule is now about the registry being unambiguous and not, as
         it read before, about a needle that matches more of the tree than its
         author expected.

    WHAT THIS FUNCTION DOES NOT DECIDE: whether the needle is the right needle.
    It is a registry check, and most unseen defect shapes pass it. Read R469 in
    the verdict for the measurement before quoting this as coverage.
    """
    answer = answer.strip()
    if answer not in ("none", "no") and not _BARE_COUNT.match(answer):
        return None
    if not ctl:
        return f"reports `{answer}` and names no `ctl:`"
    if ctl not in _CONTROL_LINES:
        return f"names control `{ctl}`, which is not planted"
    needle = _needle(cmd)
    if not needle or needle != needle.strip():
        return f"searches for `{needle}`, which is empty or carries whitespace"
    # EQUALITY, NOT CONTAINMENT (CY3, R464). A control line that CONTAINS the
    # needle certifies every needle its own text contains: the reviewer
    # walked four fresh R434s through shipped control lines without planting
    # anything -- `RIGID_MODE_FLOOR * norm` against
    # `tau = RIGID_MODE_FLOOR * norm * EPS`, and three more. The uniqueness
    # rule pointed the wrong way for the same reason: a needle matching nine
    # controls was refused and a needle matching one was allowed, when what
    # distinguishes them is whether the control was planted FOR it.
    if _CONTROL_LINES[ctl] != needle:
        return (
            f"searches for `{needle}` and its control `{ctl}` is "
            f"`{_CONTROL_LINES[ctl]}` -- a control is the needle, exactly"
        )
    others = sorted(k for k, v in _CONTROL_LINES.items() if v == needle and k != ctl)
    if others:
        return f"searches for `{needle}`, which is also planted as {others}"
    return None


@pytest.mark.parametrize(
    "rel, start, claim, cmd, ctl, expected",
    TRIPLES or _FALLBACK,
    ids=[f"{r}:{s}" for r, s, *_ in TRIPLES] or ["(none)"],
)
def test_a_triple_that_reports_an_ABSENCE_carries_a_negative_control(
    rel: str, start: int, claim: str, cmd: str, ctl: str, expected: str
) -> None:
    """R434. `out: none` proves nothing if the needle cannot match anything."""
    if rel == "(none)":
        pytest.skip("reported by test_there_are_triples_to_run")
    why = control_defect(cmd, ctl, expected)
    assert why is None, (
        f"{rel}:{start} {why}.\\n"
        "A command that returns none, no, or a count is a command a malformed "
        "needle satisfies for free."
    )


# THE REVIEWER'S RE-ADMISSION SHAPES, run against the function directly. Each
# reproduced R434 with the guard green, and the last three are the shapes that
# must still be allowed.
_CONTROL_SHAPES: list[tuple[str, str, str, str, bool]] = [
    (
        "needle_with_a_trailing_space",
        'files("tests/**/*.py", "RIGID_MODE_FLOOR ")',
        "floor_constant_name",
        "none",
        True,
    ),
    (
        "defined_of_a_misspelled_constant",
        'defined("RIGID_MODE_BONUD")',
        "",
        "no",
        True,
    ),
    (
        "an_absence_with_no_control_at_all",
        'count("tests/**/*.py", "RIGID_BODY_MODE_RATIO)")',
        "",
        "0",
        True,
    ),
    (
        "a_control_that_is_not_planted",
        'count("tests/**/*.py", "RIGID_MODE_FLOOR")',
        "no_such_control",
        "0",
        True,
    ),
    (
        # R464's shape, and the reason the rule inverted. Under CONTAINMENT
        # this needle was certified by the control planted for the bare
        # name; under EQUALITY the control must BE the needle, so a needle
        # carrying a neighbouring token needs its own plant.
        "a_needle_with_an_interior_match_in_a_shipped_control",
        'count("tests/**/*.py", "RIGID_MODE_FLOOR * norm")',
        "floor_constant_name",
        "0",
        True,
    ),
    (
        "a_needle_whose_control_was_planted_for_another",
        'count("tests/**/*.py", "RIGID_BODY_MODE_RATIO")',
        "loss_ceiling_name",
        "0",
        True,
    ),
    (
        "a_well_formed_absence",
        'count("tests/verification/rung1/test_rigid_body_modes.py", "last_below")',
        "last_below_needle",
        "0",
        False,
    ),
    (
        "an_answer_that_is_not_an_absence",
        'files("tests/**/*.py", "RIGID_MODE_FLOOR")',
        "",
        "tests/test_counters_are_injected.py",
        False,
    ),
]


@pytest.mark.parametrize(
    "name, cmd, ctl, answer, must_refuse",
    _CONTROL_SHAPES,
    ids=[s[0] for s in _CONTROL_SHAPES],
)
def test_the_CONTROL_rule_rules_on_the_reviewer_shapes(
    name: str, cmd: str, ctl: str, answer: str, must_refuse: bool
) -> None:
    """R455. Each of the first five certified an absence with the guard green."""
    got = control_defect(cmd, ctl, answer) is not None
    assert got == must_refuse, (
        f"shape `{name}`: the rule {'allowed' if must_refuse else 'refused'} it "
        f"-- control_defect returned {control_defect(cmd, ctl, answer)!r}"
    )


def test_an_EMPTY_GLOB_is_an_error_and_not_an_answer() -> None:
    """R443a, with its own control. AM5 one level down."""
    with pytest.raises(ValueError, match="matches no file"):
        count("floatfea/**/*.rs", "anything")
    # And a pattern that does reach files still answers, so the raise above is
    # about the empty match and not about the call.
    assert count("floatfea/*.py", "def ") > 0


def test_the_ANNOTATION_strip_does_not_eat_a_python_annotation() -> None:
    """R443b, with its own control.

    `out: list[tuple[int, str]] = []` begins with the annotation prefix and is
    executable code. Stripping it made a count over this file read one short.
    """
    assert _is_annotation("# out:   none")
    assert _is_annotation("out:   none")
    assert _is_annotation("    claim: something")
    assert not _is_annotation("    out: list[tuple[int, str]] = []")
    assert not _is_annotation("    counts: dict[str, int] = {}")
    # R450: a `cmd:` whose NEEDLE carries an equals sign is still an
    # annotation. The equals-sign carve-out said otherwise and the triple
    # counted itself.
    assert _is_annotation('# cmd:   count("scripts/regen_figures.py", "log=True")')
    assert _is_annotation('cmd:   count("a.py", "x=1")')
    # And a bare Python annotation with no value is code-shaped but harmless:
    # what makes a line code here is the assigned value.
    assert _is_annotation("out:   none")
