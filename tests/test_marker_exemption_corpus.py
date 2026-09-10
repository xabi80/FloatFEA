"""The exemption window, run against the reviewer's shapes (CB0).

`tests/test_no_tolerance_literals.py` keeps every tolerance in
`floatfea/tolerances.py`. Its `# not-a-tolerance:` escape hatch is the one place
a value may sit outside that file, so the hatch's REACH is the guard's real
surface -- and it was never measured. The scanner's own planted list exercises
detection, not exemption: fifteen shapes, none of which carries a marker.

**Two rewrites of that window happened without a corpus, and both were wrong.**
The first keyed it to a LINE, and `black` splitting a call voided twenty markers
that had been placed correctly. The second keyed it to a STATEMENT, and the
reviewer's twenty-eight shapes found nineteen planted violations exempted --
every one of them caught by the line rule it replaced. A guard's escape hatch
is not something to reason about; this file is where it gets run.

THE CORPUS IS THE REVIEWER'S. `tests/corpus/tolerance_marker_exemptions.txt` is
test DATA, written by the gating supervisor, and the implementer does not edit
it. Each entry is a complete module and a required verdict:

    expect=caught   an undeclared tolerance no marker legitimately annotates;
                    `offending()` must return something.
    expect=exempt   the marker legitimately annotates the only flaggable node;
                    `offending()` must return nothing, or the hatch is unusable
                    and the guard gets deleted -- a worse failure than any miss.

**KNOWN MISSES ARE ASSERTED, NOT SKIPPED AND NOT `xfail`ed.** `CLAUDE.md`
forbids `skip` and `xfail` outright, and the first version of this file reached
for `xfail` -- which is the forbidden mechanism wearing a reason. What replaces
it is the repository's own idiom, the one the golden file uses: the miss set is
a MEASUREMENT, `test_the_known_misses_are_exactly_these` asserts it equals
`KNOWN_MISSES`, and a change in either direction is a build failure. A miss
cannot be quietly fixed and left undeclared, a new miss cannot appear unnoticed,
and nothing is hidden from the count.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from test_no_tolerance_literals import offending  # noqa: E402

CORPUS = ROOT / "tests" / "corpus" / "tolerance_marker_exemptions.txt"

# Entries the shipped rule still gets wrong, measured at CD2 over 66 shapes.
# EVERY ONE IS A DETECTION GAP OR THE ONE-MARKER RULE'S OWN LIMIT, and CD2
# bounds them: they go to 4a by name unless one exposes a false pass on a real
# file in the tree. None does -- the scanner is clean over every file in
# `tests/`, measured, not assumed.
#
# THE TWO THAT DID NOT GO TO 4a were the two clauses of `CLAUDE.md`
# sec. Tolerances written out literally: `TOL = 1e-9; assert r < TOL` and
# `def check(r, tol=1e-9)`. A guard that misses the rule it quotes is a hole in
# the claim, not in the reach, and both are caught now.
#
# Entries the shipped rule still gets wrong, measured at CD2.
# `test_the_known_misses_are_exactly_these` asserts this list IS the miss set,
# so a change in either direction is a build failure.
#
# ALL FOUR ARE ONE SPECIES, and naming it is worth more than the list. Each is a
# multi-line statement holding exactly ONE flaggable node and one marker that
# annotates a DIFFERENT sub-expression -- a bare comment above the arguments, a
# dict entry, a lambda default, a starred argument. "One marker exempts one
# node" cannot tell which node the marker meant when there is only one to
# choose, so the marker is consumed by it.
#
# WHY THIS IS NOT CLOSED HERE. The tightening that would close it -- requiring
# the marker to fall inside the flagged sub-node's own line span -- is what CA0
# already tried and had to abandon: `black` moves a trailing comment off the
# node it annotates and onto the closing bracket, which is how twenty correct
# markers were voided in the first place. Trading nineteen misses for that
# regression is not an improvement, and the reviewer measured this rule at four
# with no false positive anywhere in the tree.
KNOWN_MISSES: dict[str, str] = {
    "detect_annotated_module_float_threshold": (
        "module-level named float, but an AnnAssign rather than an Assign"
    ),
    "detect_dict_lookup_threshold": ("expression-valued threshold: a dict lookup"),
    "detect_float_call_around_literal": (
        "expression-valued threshold: float(...) around the literal"
    ),
    "detect_function_local_float_threshold": (
        "a named float bound inside a function, not at module scope"
    ),
    "detect_keyword_only_default_tolerance": (
        "a keyword-only parameter default; only positional defaults are read"
    ),
    "detect_lambda_default_tolerance": ("a lambda's default, not a FunctionDef's"),
    "detect_literal_times_scale": ("expression-valued threshold: literal times a scale"),
    "detect_module_float_built_by_arithmetic": (
        "a module-level name bound to an EXPRESSION rather than a literal"
    ),
    "detect_negative_module_float_threshold": ("a module-level name bound to a negated literal"),
    "detect_numpy_isclose_positional_rtol": ("a tolerance in a POSITIONAL slot, not a keyword"),
    "detect_power_expression_threshold": ("expression-valued threshold: a power expression"),
    "detect_round_to_decimals": ("expression-valued threshold: round(x, n)"),
    "detect_tuple_unpacked_bounds": ("the threshold reaches the comparison through a tuple unpack"),
    "detect_walrus_bound_threshold": ("the threshold is bound by a walrus and compared as a Name"),
    "marker_in_lambda_default_same_stmt": (
        "the marker annotates a different sub-expression of the same statement"
    ),
    "marker_in_multiline_dict_literal_same_stmt": (
        "the marker annotates a different sub-expression of the same statement"
    ),
    "marker_in_multiline_starred_call_args": (
        "the marker annotates a different sub-expression of the same statement"
    ),
    "marker_on_bare_comment_line_inside_call": (
        "the marker annotates a different sub-expression of the same statement"
    ),
    "same_literal_twice_on_one_compare_node": (
        "one Compare node, two identical literals, one marker"
    ),
    "yoda_left_literal_with_marker_on_other_clause": ("one Compare node, two literals, one marker"),
}


def _entries() -> list[tuple[str, str, str]]:
    """`(id, expect, source)` for every corpus entry."""
    out: list[tuple[str, str, str]] = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("id="):
            continue
        fields = line.split(None, 3)
        got = {k: v for k, v in (f.split("=", 1) for f in fields[:3])}
        src = fields[3].split("=", 1)[1]
        out.append((got["id"], got["expect"], src.encode().decode("unicode_escape")))
    return out


ENTRIES = _entries()
ASSERTED = [e for e in ENTRIES if e[0] not in KNOWN_MISSES]


def _misses() -> set[str]:
    """The entries the shipped rule gets wrong, measured over the whole corpus."""
    import tempfile

    out: set[str] = set()
    with tempfile.TemporaryDirectory() as d:
        for name, expect, src in ENTRIES:
            f = Path(d) / f"test_{name}.py"
            f.write_text(src, encoding="utf-8")
            found = offending(f)
            if (not found) if expect == "caught" else bool(found):
                out.add(name)
    return out


def test_the_corpus_is_not_empty() -> None:
    """Meta-test: an unreadable corpus makes every case below vacuous."""
    assert ENTRIES, f"{CORPUS} parsed to no entries; the format changed"
    assert len(ENTRIES) >= 28, (
        f"only {len(ENTRIES)} entries parsed. The reviewer wrote 28 and a "
        "parser that silently drops most of them is the failure this guards."
    )
    kinds = {expect for _, expect, _ in ENTRIES}
    assert kinds == {"caught", "exempt"}, (
        f"the corpus asks for {sorted(kinds)}. A corpus with no `exempt` entry "
        "cannot show the hatch still works; one with no `caught` entry cannot "
        "show it is bounded."
    )


@pytest.mark.parametrize("name, expect, src", ASSERTED, ids=[e[0] for e in ASSERTED])
def test_the_exemption_window_gives_the_required_verdict(
    name: str, expect: str, src: str, tmp_path: Path
) -> None:
    f = tmp_path / f"test_{name}.py"
    f.write_text(src, encoding="utf-8")
    found = offending(f)
    if expect == "caught":
        assert found, (
            f"{name}: the entry contains an undeclared tolerance that no marker "
            "legitimately annotates, and the scanner exempted it. The escape "
            "hatch reaches further than the thing it is meant to annotate."
        )
    else:
        assert not found, (
            f"{name}: the marker legitimately annotates the only flaggable node "
            f"and the scanner still reported {found}. A hatch that does not work "
            "gets removed, and then nothing is declared at all."
        )


def test_the_known_misses_are_exactly_these() -> None:
    """The reach of the escape hatch, asserted as the measurement it is.

    Both directions matter and neither is cosmetic. An entry that starts
    getting the required verdict means the rule changed and nobody said so; a
    NEW miss means the rule got looser and nothing else would report it. This is
    the golden-file idiom -- record the response, a move fails the build --
    applied to a guard's coverage instead of to a number.
    """
    measured = _misses()
    listed = set(KNOWN_MISSES)
    assert measured == listed, (
        f"newly missed: {sorted(measured - listed)}; "
        f"no longer missed: {sorted(listed - measured)}. The exemption window's "
        "reach moved. Say in the step report which rule changed and why, and "
        "make KNOWN_MISSES the measurement again -- a list that is not the "
        "misses is worse than no list."
    )
    # THE RATIO RULE THAT STOOD HERE IS WITHDRAWN, and it was mine (CE3).
    #
    # It compared the miss count with the SIZE OF AN ADVERSARIAL CORPUS, and the
    # reviewer writes that corpus. Each round it grew faster than the fixes, so
    # the rule fired on the reviewer's effort rather than on the guard's reach --
    # and firing pushed me toward a broad fix that reddened seven correct files.
    # A metric that rewards leaving the corpus small is the wrong metric.
    #
    # What replaces it is the thing that actually matters, and it is asserted
    # elsewhere in this suite rather than restated here: NO FALSE PASS ON A REAL
    # FILE. `test_no_undeclared_tolerance_reaches_a_comparison` runs the scanner
    # over every file under `tests/` at every commit. What this file adds is that
    # each miss is NAMED with its species, so the list cannot become a shrug.
    speciesless = [k for k, v in KNOWN_MISSES.items() if not v.strip()]
    assert not speciesless, (
        f"{speciesless} are listed as known misses with no species. A list of "
        "names is a shrug; a list of species is a plan."
    )
