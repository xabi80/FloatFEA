"""Sentences in the SOURCE TREE are checked the way sentences in a report are (CV0).

`tests/test_report_numbers_are_sourced.py` makes a number in a step report carry
the command that produced it. It stops at `docs/reports/`. Eight findings in the
forty-eighth verdict were sentences in `floatfea/`, `tests/`, `scripts/` and the
locked plan, **every one of them refuted by a grep over a file the same commit
touched**, and five of the eight were written in the round that fixed the same
species somewhere else. The reviewer's words: that is worth a rule rather than
eight repairs.

WHAT THIS FILE DECIDES, IN THREE PARTS.

1. **A TRIPLE IS RUN.** Prose anywhere under the roots below may write

       claim: <one sentence about what this repository contains>
       cmd:   <a call from the vocabulary in `_VOCABULARY`>
       out:   <what that call returns>

   and this file evaluates the call and compares. A triple whose `out` is stale
   is a failure, so the sentence cannot rot silently the way a comment does.
   The vocabulary is deliberately tiny and is *the grep the reviewer ran*:
   `count`, `lines`, `files`, `defined`. No shell, no network, no arbitrary
   Python -- the expression is parsed and rejected if it is anything but a call
   to one of those names on literal arguments.

2. **AN ABSENCE CLAIM CARRIES A TRIPLE.** A paragraph that says something is
   *not* in the tree -- "nothing asserts against it", "no shipped row declares
   it", "not typed anywhere", "NOTHING ASSERTS AGAINST THIS AND NOTHING MAY" --
   is the exact shape that failed. Those sentences look like documentation and
   read like guarantees, and nothing has ever checked one. Each must carry a
   triple or be listed in `_ABSENCE_EXEMPT` with a reason.

3. **A RETIRED QUANTITY IS NOT DESCRIBED IN THE PRESENT TENSE.** When a gate
   changes shape the old quantity keeps its entry, marked `RETIRED`, and every
   sentence describing the gate BY that quantity has to move with it in the
   same commit (BP0). Nothing enforced that, so the plan's own gate register
   still called G2.1 an eigenvalue ratio 1600 lines above the section that says
   the ratio is retired. Each retired entry declares its prose names beside
   itself:

       # RETIRED-ALIAS: eigenvalue ratio

   and any paragraph using an alias must say `retired` (or carry a triple).
   The aliases live next to the constant, written by whoever retires it, so
   the vocabulary cannot drift from the retirement.

WHAT IT DOES NOT DECIDE, said so it is not trusted past its reach:

* it cannot find a POSITIVE claim that is false -- "this file asserts X" when
  it does not. Absence and retirement are the two species this milestone has
  actually produced, eight times and four times respectively; a general
  checker for "is this sentence about the code true" is not a thing that
  exists;
* the patterns in `_ABSENCE` are a list, not a grammar. A sentence that says
  the same thing in words nobody has used yet is not seen. `R429` is the same
  limitation one file over and the answer there was the reviewer's corpus of
  unseen shapes; the answer here is the same, and until that corpus exists the
  coverage is the list;
* a triple proves its own `out` is current. It does not prove the `claim`
  sentence is what the `cmd` measures -- that half is a reader's, and it is
  why the claim is written out in full beside the call rather than left as a
  bare assertion.
"""

from __future__ import annotations

import ast
import io
import re
import tokenize
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ROOTS = ("floatfea", "tests", "scripts", "docs/milestones")

# `docs/reports/` is NOT a root here: it has its own guard, and a step report
# is a record of a moment rather than a description of the tree -- revision 14
# says true things about a commit fourteen revisions back and must keep saying
# them.


# --------------------------------------------------------------------------
# The vocabulary. This is the grep, and nothing else runs.
# --------------------------------------------------------------------------


# A TRIPLE'S OWN ANNOTATION IS NOT PART OF THE TREE IT MEASURES.
#
# Every `cmd:` line contains the needle it searches for, so the first four
# triples written against this file all counted themselves: "nothing reads
# `last_below`" returned 1, and the 1 was the sentence saying it returned 0.
# That is the citation rule catching its own explanation, one file over, and
# the fix is the same -- the annotation lines are stripped before any search.
#
# The cost is real and is stated rather than hidden: a needle that only ever
# appears on an annotation line is invisible to the vocabulary, so a triple
# cannot assert anything about the triples.
_ANNOTATION = re.compile(r"^\s*(?:#\s*)?(?:claim|cmd|out):", re.M)


def _without_annotations(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not _ANNOTATION.match(line))


def _read(rel: str) -> str:
    return _without_annotations((ROOT / rel).read_text(encoding="utf-8", errors="replace"))


def _paths(pattern: str) -> list[Path]:
    """Every file matching `pattern`, which is a path or a glob under ROOT."""
    if any(ch in pattern for ch in "*?["):
        return sorted(p for p in ROOT.glob(pattern) if p.is_file())
    return [ROOT / pattern]


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
    raw = (ROOT / rel).read_text(encoding="utf-8", errors="replace").splitlines()
    got = [
        str(i) for i, line in enumerate(raw, 1) if needle in line and not _ANNOTATION.match(line)
    ]
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


def _evaluate(expr: str) -> str:
    """Run one `cmd:` call, refusing anything that is not a vocabulary call.

    Parsed rather than pattern-matched: a call is admitted only when it is a
    single `Name(args...)` whose name is in the vocabulary and whose arguments
    are string literals. `eval` on a comment in the source tree would otherwise
    be a way to run anything from a docstring.
    """
    tree = ast.parse(expr.strip(), mode="eval")
    node = tree.body
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
        raise ValueError(f"not a call: {expr!r}")
    if node.func.id not in _VOCABULARY:
        raise ValueError(f"{node.func.id} is not in the vocabulary {sorted(_VOCABULARY)}")
    if node.keywords or not all(
        isinstance(a, ast.Constant) and isinstance(a.value, str) for a in node.args
    ):
        raise ValueError(f"arguments must be string literals: {expr!r}")
    return str(_VOCABULARY[node.func.id](*[a.value for a in node.args]))


# --------------------------------------------------------------------------
# Reading prose out of the tree
# --------------------------------------------------------------------------


def _python_prose(path: Path) -> list[tuple[int, str]]:
    """Comment and docstring lines only -- never executable code.

    An assertion MESSAGE is not a claim about the tree; it is a sentence the
    program prints when something else is wrong. Reading code as prose put
    every f-string in the repository into this guard's domain, which is how
    the first version of it found forty-seven sites and meant nothing.
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
    got: list[Path] = []
    for where in ROOTS:
        for p in sorted((ROOT / where).rglob("*")):
            if p.suffix in (".py", ".md") and "__pycache__" not in str(p):
                got.append(p)
    return got


def _paragraphs(prose: list[tuple[int, str]]) -> list[tuple[int, int, str]]:
    """Consecutive non-blank prose lines as `(first, last, joined)`.

    A claim is a sentence and a sentence wraps: the first version of this
    matched line by line and missed three of the eight findings because the
    verb and the symbol were on different lines. The extent comes back with
    it so a paragraph can be asked whether a triple sits inside it -- joining
    first and searching the joined text for `out:` ran the expected value to
    the end of the paragraph, which made every triple's `out` the rest of the
    comment.
    """
    out: list[tuple[int, int, str]] = []
    cur: list[str] = []
    start: int | None = None
    last = 0
    prev: int | None = None
    for lineno, line in prose:
        if not line or (prev is not None and lineno > prev + 1):
            if cur:
                out.append((start or 0, last, " ".join(cur)))
            cur, start = [], None
        if line:
            start = lineno if start is None else start
            last = lineno
            cur.append(line)
        prev = lineno
    if cur:
        out.append((start or 0, last, " ".join(cur)))
    return out


PROSE: list[tuple[str, int, int, str]] = []
LINES_OF: dict[str, list[tuple[int, str]]] = {}
for _p in _prose_files():
    _rel = str(_p.relative_to(ROOT)).replace("\\", "/")
    _lines = _python_prose(_p) if _p.suffix == ".py" else _markdown_prose(_p)
    LINES_OF[_rel] = _lines
    for _first, _last, _para in _paragraphs(_lines):
        PROSE.append((_rel, _first, _last, _para))


# --------------------------------------------------------------------------
# 1. The triples
# --------------------------------------------------------------------------

_CLAIM = re.compile(r"^claim:\s*(.+)$")
_CMD = re.compile(r"^cmd:\s*(.+)$")
_OUT = re.compile(r"^out:\s*(.+)$")


def _triples_in(rel: str, prose: list[tuple[int, str]]) -> list[tuple[str, int, str, str, str]]:
    """`claim:` then `cmd:` then `out:`, each on its own prose line.

    A claim may WRAP: continuation lines between `claim:` and `cmd:` are part
    of the sentence. `cmd:` and `out:` may not -- a call and its result are
    one line each, and letting them wrap is how the joined-paragraph version
    swallowed the rest of the comment into `out`.
    """
    got: list[tuple[str, int, str, str, str]] = []
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
        if j + 1 < n and _CMD.match(prose[j][1]) and _OUT.match(prose[j + 1][1]):
            got.append(
                (
                    rel,
                    start,
                    claim.strip(),
                    _CMD.match(prose[j][1]).group(1).strip(),
                    _OUT.match(prose[j + 1][1]).group(1).strip(),
                )
            )
            i = j + 2
            continue
        raise AssertionError(
            f"{rel}:{start} opens `claim:` and the next prose lines are not "
            f"`cmd:` then `out:`. A claim without its command is the thing "
            f"this file exists to refuse.\n    {claim[:200]}"
        )
    return got


TRIPLES: list[tuple[str, int, str, str, str]] = [
    t
    for rel, prose in LINES_OF.items()
    if rel != "tests/test_tree_prose_consistent.py"
    for t in _triples_in(rel, prose)
]
TRIPLE_LINES: dict[str, set[int]] = {}
for _t in TRIPLES:
    TRIPLE_LINES.setdefault(_t[0], set()).add(_t[1])


def test_there_are_triples_to_run() -> None:
    """Meta-test: zero triples makes the runner below a test of nothing."""
    assert len(TRIPLES) >= 6, (
        f"only {len(TRIPLES)} prose triple(s) found in the tree. Either the "
        "sentences lost their commands or the pattern stopped matching, and "
        "both make this file vacuous."
    )


@pytest.mark.parametrize(
    "rel, start, claim, cmd, expected",
    TRIPLES or [("(none)", 0, "", "count('x','y')", "0")],
    ids=[f"{r}:{s}" for r, s, *_ in TRIPLES] or ["(none)"],
)
def test_a_prose_triple_still_says_what_the_tree_says(
    rel: str, start: int, claim: str, cmd: str, expected: str
) -> None:
    """The sentence's own command, run here, against the `out` beside it."""
    if rel == "(none)":
        pytest.skip("reported by test_there_are_triples_to_run")
    got = _evaluate(cmd)
    assert got == expected.strip(), (
        f"{rel}:{start} claims:\n    {claim}\n"
        f"and its own command `{cmd}` returns `{got}`, not `{expected.strip()}`.\n"
        "Either the sentence is stale or the tree moved under it. This is the "
        "species the forty-eighth verdict found eight times in one round."
    )


# --------------------------------------------------------------------------
# 2. Absence claims
# --------------------------------------------------------------------------

_ABSENCE = re.compile(
    r"\b(?:"
    r"nothing (?:asserts|reads|counts|publishes|declares|registers|cites)"
    r"|and nothing may\b"
    r"|(?:asserted|referenced|declared|registered|published|cited) by nothing"
    r"|no shipped \w+ (?:declares|carries|uses|reads|produces)"
    r"|no shipped row declares"
    r"|typed anywhere"
    r"|no figure publishes"
    r"|is not written here|not written here|count is written here"
    r"|appears nowhere|exists nowhere"
    r"|both counters|both are registered"
    r")",
    re.I,
)

# EXEMPT, WITH THE REASON, and keyed on the matched phrase plus the file rather
# than on a line number, so the row lapses when the sentence is rewritten.
#
# A row here is a statement that the phrase is not a claim about what this tree
# contains. It is NOT a way to keep an unchecked claim: where the sentence does
# assert something about the tree, it gets a triple instead.
# KEYED ON (file, the matched phrase, lowercased), so a row lapses the moment
# the sentence is reworded -- the same content-addressing the marker exemption
# corpus uses, and for the same reason: an exemption that survives a rewrite is
# an exemption for a sentence nobody has read since.
_ABSENCE_EXEMPT: dict[tuple[str, str], str] = {
    ("floatfea/tolerances.py", "not written here"): (
        "POLICY, not a claim: BI3's rule that a measured value is cited by "
        "name or it is not written, and R316's that the spread's count is "
        "re-taken rather than typed. Both say what this file may contain, "
        "not what it does contain"
    ),
    ("tests/test_marker_exemption_corpus.py", "not written here"): (
        "policy, as above -- the two counts move with the scanner and the "
        "file says it will not type them"
    ),
    ("tests/verification/rung1/test_rigid_body_corpus.py", "not written here"): (
        "policy, twice: the docstring refuses to type a count and names the "
        "test that prints it instead"
    ),
    ("tests/test_collected_set_golden.py", "not written here"): (
        "a deliberate omission with its reason inline -- writing the dead "
        "name in backticks would make that rule flag its own explanation"
    ),
    ("tests/test_collected_set_golden.py", "exists nowhere"): (
        "HISTORY: R387's dead test name, which existed nowhere at the commit "
        "that shipped it. Past tense, about a name no longer in the tree"
    ),
    ("tests/verification/rung1/test_patch_test.py", "shipped test produces"): (
        "a CONDITIONAL -- 'where a block carries a table that no shipped test "
        "produces, it says so' -- which states a policy for future blocks "
        "rather than asserting anything about the tree now"
    ),
    ("tests/verification/rung1/test_corpus_configurations.py", "nothing asserts"): (
        "BO2's rule about a fitted DIAGNOSTIC curve: the sentence says the "
        "curve may not be asserted on, not that no assertion exists"
    ),
}


# THIS FILE IS OUT OF ITS OWN DOMAIN, and that is a hole rather than a
# convenience: it has to quote every phrase it forbids in order to define
# them, so every pattern matches its own docstring. The same exemption exists
# one file over in `tests/test_no_tolerance_literals.py`, for the same reason
# and with the same cost -- a false sentence written HERE is not caught here.
SELF = "tests/test_tree_prose_consistent.py"


def _carries_a_triple(rel: str, first: int, last: int) -> bool:
    return any(first <= ln <= last + 3 for ln in TRIPLE_LINES.get(rel, ()))


ABSENCE_HITS: list[tuple[str, int, int, str, str]] = []
for _rel, _first, _last, _para in PROSE:
    if _rel == SELF:
        continue
    for _m in _ABSENCE.finditer(_para):
        ABSENCE_HITS.append((_rel, _first, _last, _m.group(0), _para))


def test_the_absence_pattern_finds_something() -> None:
    """Meta-test: a pattern that matches nothing cannot be enforcing anything."""
    assert len(ABSENCE_HITS) >= 5, (
        f"the absence pattern matched {len(ABSENCE_HITS)} paragraph(s). It was "
        "written against eight real findings; if it now finds almost nothing "
        "the pattern broke rather than the prose improving."
    )


def _norm(phrase: str) -> str:
    """An exemption key: lowercased, with a leading `is`/`and` dropped.

    `is not written here` and `not written here` are the same claim and the
    pattern reports whichever the sentence happens to start with.
    """
    return re.sub(r"^(?:is|and|no)\s+", "", phrase.strip().lower())


@pytest.mark.parametrize(
    "rel, first, last, phrase, para",
    ABSENCE_HITS or [("(none)", 0, 0, "", "")],
    ids=[f"{r}:{f}-{p[:24]}" for r, f, _l, p, _ in ABSENCE_HITS] or ["(none)"],
)
def test_an_ABSENCE_claim_carries_the_command_that_would_refute_it(
    rel: str, first: int, last: int, phrase: str, para: str
) -> None:
    """ "Nothing asserts against it" is a grep, written as a sentence."""
    if rel == "(none)":
        pytest.skip("reported by test_the_absence_pattern_finds_something")
    if _carries_a_triple(rel, first, last):
        return
    if (rel, _norm(phrase)) in _ABSENCE_EXEMPT:
        return
    start = first
    pytest.fail(
        f"{rel}:{start} says `{phrase}` and carries no command.\n"
        f"    {para[:300]}\n"
        "An absence claim is a grep written as a sentence: put the grep beside "
        "it as `claim:` / `cmd:` / `out:`, delete the sentence, or add a row to "
        "`_ABSENCE_EXEMPT` saying why it is not a claim about this tree."
    )


# --------------------------------------------------------------------------
# 3. Retired quantities
# --------------------------------------------------------------------------

_ALIAS = re.compile(r"^#\s*RETIRED-ALIAS:\s*(.+?)\s*$", re.M)
RETIRED_ALIASES: list[str] = sorted(set(_ALIAS.findall(_read("floatfea/tolerances.py"))))

# The sentence is allowed to use the alias when it SAYS the thing is retired,
# or when it is the retirement itself talking.
# `no longer` is a retirement in as many words, and `used to` and `was the
# gate` are the two other spellings already in the tree. The list is a list:
# a sentence that retires a quantity in words nobody has used yet reads as a
# present-tense description and fails here, which is the safe direction.
_SAYS_RETIRED = re.compile(
    r"\bretire[ds]?\b|\bwas the gate\b|\bused to\b|\bformer\b|\bno longer\b",
    re.I,
)


def test_a_retired_quantity_declares_its_prose_names() -> None:
    """Meta-test: no aliases means part 3 checks nothing."""
    assert len(RETIRED_ALIASES) >= 3, (
        f"`floatfea/tolerances.py` declares {RETIRED_ALIASES}. Every retired "
        "quantity carries `# RETIRED-ALIAS:` lines for the words prose calls "
        "it by, or a sentence describing the gate by the old quantity cannot "
        "be found. R421 was four such sentences in the locked plan."
    )


def _unemphasised(text: str) -> str:
    """`an eigenvalue *ratio*` is the alias `eigenvalue ratio`.

    Markdown emphasis lands in the middle of the phrase, so matching the raw
    line missed the plan's gate register -- which is the site R421 is about.
    """
    return re.sub(r"[*_`]+", "", text)


ALIAS_HITS: list[tuple[str, int, str, str]] = []
for _rel, _first, _last, _para in PROSE:
    if _rel in ("floatfea/tolerances.py", SELF):
        continue  # the retirement entries themselves, and this file's own prose
    _flat = _unemphasised(_para)
    for _alias in RETIRED_ALIASES:
        if re.search(rf"\b{re.escape(_alias)}\b", _flat, re.I):
            ALIAS_HITS.append((_rel, _first, _alias, _para))


@pytest.mark.parametrize(
    "rel, start, alias, para",
    ALIAS_HITS or [("(none)", 0, "", "")],
    ids=[f"{r}:{s}-{a[:20]}" for r, s, a, _ in ALIAS_HITS] or ["(none)"],
)
def test_prose_naming_a_RETIRED_quantity_says_that_it_is_retired(
    rel: str, start: int, alias: str, para: str
) -> None:
    """BP0, made mechanical: the rule moved, so every sentence citing it moves."""
    if rel == "(none)":
        pytest.skip("no retired aliases declared")
    if _SAYS_RETIRED.search(para):
        return
    pytest.fail(
        f"{rel}:{start} describes the gate by `{alias}`, which "
        "`floatfea/tolerances.py` declares as a RETIRED quantity's prose name, "
        "and the paragraph does not say it is retired.\n"
        f"    {para[:300]}\n"
        "Say the form it asserts now, or say at this sentence that this is the "
        "retired form. BP0: when a decision rule changes, every sentence citing "
        "the old rule moves in the same commit."
    )
