"""Every number in a report is sourced, or it is not written (CI2, R311).

Nine rounds, one species. A figure is correct when it is taken, the thing
underneath it moves, and nothing re-takes it: `62x` of headroom measured on a
laptop, `11 of 47` rows where the denominator was a line count, `23 of 23`
where the corpus held twenty-two, a ten-leg table labelled with one commit and
taken from another run, `all nine` spreads where the code prints eight. Every
one was refuted by a single command, and every one sat beside a repair that
worked.

`CLAUDE.md` § "Every claim carries its command" says the rule already. This is
the mechanical half of it, for numbers:

  * a number inside a fenced block is **sourced** -- that is where the
    `claim / cmd / out / rule / cell / judge` triples live, and the block is
    the command that produced it;
  * a number in a table is sourced when its section shows a `cmd`, or when the
    table declares itself `Generated:` by a named script;
  * a number in prose is sourced when the same number appears inside a fenced
    block **in the same section** -- the prose may repeat what the command
    printed, and may not introduce a figure the section never measured;
  * some numeric tokens are not figures at all and are exempt by form: item
    numbers (`R311`), section references, commit shas, dates, versions, and
    `{{fig:NAME}}` references, which are resolved by
    `tests/test_plan_figures.py`.

WHAT IT DOES NOT DO. It cannot tell a right number from a wrong one, and it
does not read the command to see whether it produces the figure beside it.
Those are the reviewer's. What it removes is the number with no command
anywhere near it, which is the shape all five of the last round's refutations
had.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "docs" / "reports" / "F2"


def _newest_report() -> Path:
    steps = []
    for q in REPORTS.glob("step-*.md"):
        m = re.fullmatch(r"step-(0|[1-9][0-9]*)", q.stem)
        if m:
            steps.append((int(m.group(1)), q))
    assert steps, f"no numbered step report under {REPORTS}"
    return max(steps)[1]


REPORT = _newest_report()
TEXT = REPORT.read_text(encoding="utf-8", errors="replace")
BODY = TEXT[TEXT.rindex("# Revision ") :] if "# Revision " in TEXT else TEXT

# A number, at its widest: digits with separators and an optional exponent.
# A number, at its widest, ENDING IN A DIGIT. Allowing a trailing comma made
# `R321,` match as `321,`, which no exempt span contains, so a list of item
# numbers read as a list of unsourced figures.
_NUMBER = re.compile(r"\d(?:[\d,]*\d)?(?:\.\d+)?(?:[eE][-+]?\d+)?")
# Forms that are not figures. A token is exempt when it is PART OF one of
# these, never when one merely sits near it (R320).
_EXEMPT_CONTEXT = (
    re.compile(r"\bR\d+\b"),  # a finding
    re.compile(r"§\s*\d+"),  # a section reference
    re.compile(r"\b[0-9a-f]{7,40}\b"),  # a commit
    re.compile(r"\b20\d\d-\d\d-\d\d\b"),  # a date
    re.compile(r"\{\{fig:[a-z0-9_]+\}\}"),  # a generated figure by name
    re.compile(r"\bstep-\d+\b"),
    re.compile(r"\brevision \d+\b", re.IGNORECASE),
    re.compile(r"\bverdict \d+\b", re.IGNORECASE),
    re.compile(r"\bQ\d+\b"),  # a lock question
    re.compile(r"\bCH\d\b|\bCI\d\b|\bC[A-G]\d\b|\bB[A-Z]\d\b"),  # a directive
    re.compile(r"\bpython[ -]?3\.\d+\b", re.IGNORECASE),
    re.compile(r"\brung ?\d\b|\bladder ?\d\b|\bstep ?\d\b", re.IGNORECASE),
    re.compile(r"\bitem ?\d[a-z]?\b", re.IGNORECASE),
    # A GATE OR A VERIFICATION ITEM: G1.5, V1.1, G2.2. A name, not a
    # measurement, and the numbering is the plan's.
    re.compile(r"\b[GV]\d+\.\d+\b"),
)


def _sections() -> list[tuple[str, list[str]]]:
    """`(heading, lines)` for every `##` section of the newest revision."""
    out: list[tuple[str, list[str]]] = []
    heading, lines = "(preamble)", []
    for line in BODY.splitlines():
        if line.startswith("## "):
            out.append((heading, lines))
            heading, lines = line.strip("# ").strip(), []
        else:
            lines.append(line)
    out.append((heading, lines))
    return out


def _split(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    """`(fenced, table, prose)` lines of one section."""
    fenced: list[str] = []
    table: list[str] = []
    prose: list[str] = []
    inside = False
    for line in lines:
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if inside:
            fenced.append(line)
        elif line.lstrip().startswith("|"):
            table.append(line)
        else:
            prose.append(line)
    return fenced, table, prose


SECTIONS = _sections()


def test_the_report_parsed_into_sections() -> None:
    """A parse that finds nothing agrees with everything."""
    assert len(SECTIONS) > 3, f"{REPORT.name}'s newest revision parsed to {len(SECTIONS)} sections"
    assert any(_split(lines)[0] for _, lines in SECTIONS), (
        "no fenced block in the whole revision, so every number would be "
        "unsourced and this file would report the format rather than the figures."
    )


def _inside_an_exempt_span(line: str, start: int, end: int) -> bool:
    """Is this token PART OF an exempt form, rather than merely near one?

    The first version searched a twenty-four character window on either side,
    so any number within a few words of a commit sha was exempt -- and the
    round's headline figure passed only because a sha happened to sit ten
    characters to its left. A window is proximity; membership is the property
    that was meant.
    """
    for pattern in _EXEMPT_CONTEXT:
        for hit in pattern.finditer(line):
            if hit.start() <= start and end <= hit.end():
                return True
    return False


def _unsourced(lines: list[str]) -> list[tuple[str, str]]:
    fenced, table, prose = _split(lines)
    sourced = "\n".join(fenced + table)
    out: list[tuple[str, str]] = []
    for line in prose:
        # A LINE THAT NAMES ITS OWN GENERATOR IS A TRIPLE ON ONE LINE. The
        # whole-suite line reads `... Generated by `python scripts/suite_count.py``
        # beside its three numbers: the command is there, in the sentence, and
        # requiring it to be repeated inside a fence would be requiring the
        # form rather than the content.
        if re.search(r"`python scripts/[a-z_]+\.py", line):
            continue
        for m in _NUMBER.finditer(line):
            token = m.group(0)
            if _inside_an_exempt_span(line, m.start(), m.end()):
                continue
            if token in sourced:
                continue
            # A bare small integer in a sentence is a count of things the
            # sentence itself lists -- "five scenarios", "two commits" -- and
            # the list is the source. Only figures are in scope here.
            if token.isdigit() and len(token) <= 2 and float(token) <= 20:
                continue
            out.append((token, line.strip()))
    return out


@pytest.mark.parametrize(
    "heading, lines", SECTIONS, ids=[h[:40] for h, _ in SECTIONS] or ["(none)"]
)
def test_every_number_in_prose_is_sourced_in_its_own_section(
    heading: str, lines: list[str]
) -> None:
    bad = _unsourced(lines)
    assert not bad, (
        f"in `{heading}`, {len(bad)} number(s) appear in prose and nowhere in "
        "a command block or table of the same section:\n"
        + "\n".join(f"  {t!r} in: {ln[:110]}" for t, ln in bad[:6])
        + "\nEither show the command that produced it in this section, or "
        "cite a generated figure by name. Nine rounds of refuted figures were "
        "all this shape."
    )


@pytest.mark.parametrize(
    "heading, lines", SECTIONS, ids=[h[:40] for h, _ in SECTIONS] or ["(none)"]
)
def test_a_table_of_numbers_shows_where_it_came_from(heading: str, lines: list[str]) -> None:
    """A table is an output; the section says what produced it."""
    fenced, table, prose = _split(lines)
    # A TABLE WHOSE ONLY NUMBERS ARE EXEMPT FORMS IS NOT A TABLE OF NUMBERS.
    # The commit list in the closing section is shas and prose; requiring a
    # `cmd` beside it would be requiring the form rather than the content.
    figures = [
        row
        for row in table
        for m in _NUMBER.finditer(row)
        if not _inside_an_exempt_span(row, m.start(), m.end())
    ]
    if not figures:
        return
    blob = "\n".join(fenced + prose)
    assert re.search(r"^\s*cmd\b", "\n".join(fenced), re.MULTILINE) or re.search(
        r"generated", blob, re.IGNORECASE
    ), (
        f"`{heading}` publishes a table of numbers and the section shows no "
        "`cmd` and does not declare the table generated. A table is a "
        "measurement; the command that took it belongs beside it."
    )
