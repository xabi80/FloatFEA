"""The report carries every finding, and answers every site a finding names (BT0).

TWO GUARDS, BOTH AS TESTS RATHER THAN AS HOOKS, and the reason is measured: five
hook defects in this milestone, the last of them a `check_carried.py` call the
hook could never reach because the branch above it returns first. **A guard that
must run belongs where the reviewer runs it.** The supervisor runs `pytest`, so
an incomplete `Carried` is red inside the verdict that reads it.

AGAINST THE VERDICT THE REPORT CLAIMS TO ANSWER, NOT THE NEWEST ONE (BU1). The
newest revision carries a header line

    Answers: verdict <n> @ <sha>

and this file checks the report against THAT verdict. Comparing against the
newest one made a step boundary permanently red: between a verdict landing and
the report answering it, the report legitimately predates the findings, so
`pytest` at HEAD was `34 failed` by construction and "green" stopped meaning
anything at the moment it is most needed.

With the header, green means green: a report cannot claim to answer verdict `n`
without carrying verdict `n`'s findings, and the one thing left for a reader is
whether the header names the LATEST verdict -- which is `docs/SUPERVISOR.md`
item 1, one comparison, not a diff.

WHAT IS CHECKED
---------------
1. Every `R<n>` the answered verdict mentions -- its own findings AND its own
   `Carried` section, so an item carried forward keeps propagating instead of
   ageing out -- appears in the newest report revision's `Carried`.
2. Every `file:line` a finding names is either **inside a changed hunk** of
   `git diff <reviewed>..HEAD -U0`, or declared in the report as `no change`
   beside that exact site.

**AT LINE RESOLUTION, WHICH IS THE RESOLUTION FINDINGS ARE WRITTEN IN (BV0).**
The file-level version passed while a finding was answered at four of its eight
sites -- five consecutive rounds of the same species. What makes lines work: the
verdict's numbers are at the REVIEWED commit, and `-U0` hunks carry old-side
ranges in exactly those coordinates, so a named line is closed when it falls
inside one.

FOUR PARSER HOLES CLOSED HERE rather than deferred, because a guard is only as
good as its parser (R171): the site pattern no longer requires a `/`, so a bare
`test_corpus_configurations.py` is seen; a finding's block ends at the next
finding OR the next `##` heading, so the last one no longer absorbs every path to
end-of-file; a heading written `**R162 (recordable)` without the dot is caught;
and a range `:a-b` expands to every line in it rather than to its endpoints.

WHAT IS NOT CHECKED, stated so the guard is not trusted past its reach: whether
the status written beside a carried item is TRUE, and whether a touched file was
touched at the right line. Both are the reviewer's.
"""

from __future__ import annotations

import html
import importlib.util
import json
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "docs" / "reviews" / "F2"
REPORTS = ROOT / "docs" / "reports" / "F2"


def _steps(where: Path) -> set[int]:
    """Step numbers with a file under `where`.

    Does not raise for a directory that cannot be read, or for a filename this
    does not recognise as a step. Both are states the guard REPORTS; neither is
    one it dies on. The previous version said "never raises" and did, which is
    R246 -- a docstring is not a guarantee, and this one now matches what the
    two branches below actually cover.
    """
    # `[0-9]+`, NOT `str.isdigit()` (CC4). `isdigit()` admits a strictly larger
    # set than `int()` accepts -- superscripts, Kharosthi numerals, a dozen other
    # categories -- so `step-\N{SUPERSCRIPT ONE}.md` passed the filter, raised
    # `ValueError` inside the comprehension, and took the whole suite down at
    # collection: zero of 1656 tests. The repair before this one caught `OSError`
    # because `OSError` was the failure it had already seen.
    try:
        names = [q.stem for q in where.glob("step-*.md")]
    except OSError:
        return set()
    # THE CANONICAL FORM ONLY. `[0-9]+` accepted `step-06.md` and read it as
    # step 6, so a zero-padded file silently became a second name for a step
    # that already had one -- and with both present one of them was invisible.
    # A step number has one spelling.
    return {int(m.group(1)) for m in (re.fullmatch(r"step-(0|[1-9][0-9]*)", n) for n in names) if m}


def _step_files(where: Path) -> dict[int, list[str]]:
    """`{step: [filenames]}`, so two spellings of one step can be reported."""
    out: dict[int, list[str]] = {}
    try:
        names = [q.stem for q in where.glob("step-*.md")]
    except OSError:
        return out
    for n in names:
        m = re.fullmatch(r"step-0*([0-9]+)", n)
        if m:
            out.setdefault(int(m.group(1)), []).append(n)
    return out


# THE NEWEST REPORT AND THE NEWEST COMPLETE PAIR ARE DIFFERENT NUMBERS, and
# conflating them took the whole suite down (R234). CB2 made this module read
# `step-<newest report>` at import; `CLAUDE.md` guarantees the verdict is
# written AFTER the report is committed, so at every legitimate step boundary
# the verdict file does not exist yet -- and `read_bytes` on it raised during
# collection. `pytest -q` then reported `1 error` and ran ZERO of 1589 tests.
# That is item 1b's failure one level down and worse: 1b made a boundary red,
# this made it silent.
#
# The carry comparison runs against the newest COMPLETE pair, so it stays
# meaningful at the boundary, and `test_the_guard_reads_the_step_being_worked_on`
# is the one named test that carries the pending-verdict message.
REPORTED = _steps(REPORTS)
REVIEWED = _steps(REVIEWS)
STEP_REPORT = max(REPORTED) if REPORTED else 0
STEP = max(REPORTED & REVIEWED) if (REPORTED & REVIEWED) else 0
VERDICT = REVIEWS / f"step-{STEP}.md"
REPORT = REPORTS / f"step-{STEP}.md"

# `**R12.` and `**R12 ` both open a finding: the missing dot dropped one silently.
_FINDING = re.compile(r"^\*\*(R\d+)[.\s]", re.MULTILINE)
_MENTION = re.compile(r"\bR\d+\b")
# `path/to/file.py:123` or `:123-145`, as the verdicts write them.
# The leading dot of `.claude/...` is part of the path; `` before it would
# cut it off and the file would never match the diff.
# The directory part is OPTIONAL, because findings name bare files too and
# those were invisible to this pattern (R171). The optional `:line` and `:a-b`
# suffixes are what take the guard to line resolution.
_SITE = re.compile(r"((?:\.?[\w.-]+/)*[\w.-]+\.(?:py|md|sh|txt|json))(?::(\d+)(?:-(\d+))?)?")


def _read(path: Path) -> str:
    """Permissive in BOTH directions: a verdict written with a Windows-1252 dash
    must not make a guard raise, and neither must a file that is not there yet
    (R234). A guard that raises during collection is a guard that takes the
    suite with it -- and it did, at the one moment it was most needed."""
    try:
        return path.read_bytes().decode("utf-8", errors="replace")
    except OSError:
        return ""


def _section(text: str, heading: str) -> str:
    heads = list(re.finditer(rf"^##+ .*{heading}.*$", text, re.MULTILINE))
    if not heads:
        return ""
    start = heads[-1].end()
    nxt = re.search(r"^##+ ", text[start:], re.MULTILINE)
    return text[start : start + nxt.start()] if nxt else text[start:]


def _newest_revision(text: str) -> str:
    marks = [m.start() for m in re.finditer(r"^# Revision \d+", text, re.MULTILINE)]
    return text[marks[-1] :] if marks else text


def _reviewed_commit(text: str) -> str:
    m = re.search(r"^Reviewed commit:\s*(\S+)", text, re.MULTILINE)
    return m.group(1) if m else ""


def _answered_verdict(report_text: str) -> str:
    """The `Answers: verdict <n> @ <sha>` header of the newest revision.

    Returns the sha, or `""` when the header is absent -- which
    `test_the_report_names_the_verdict_it_answers` turns into a failure rather
    than a silent fall back to the newest verdict.
    """
    m = re.search(
        r"^Answers:\s*verdict\s*\d+\s*@\s*(\S+)", _newest_revision(report_text), re.MULTILINE
    )
    return m.group(1) if m else ""


def _verdict_text_at(sha: str) -> str:
    """The verdict file as it stood at `sha`, or the working copy if unknown."""
    if not sha:
        return _read(VERDICT)
    out = subprocess.run(
        ["git", "show", f"{sha}:docs/reviews/F2/step-{STEP}.md"], cwd=ROOT, capture_output=True
    )
    if out.returncode != 0:
        return _read(VERDICT)
    return out.stdout.decode("utf-8", errors="replace")


REPORT_TEXT = _read(REPORT)
ANSWERED = _answered_verdict(REPORT_TEXT)
VERDICT_TEXT = _verdict_text_at(ANSWERED)
CARRIED = _section(_newest_revision(REPORT_TEXT), "Carried")
EXPECTED = sorted(
    set(_FINDING.findall(VERDICT_TEXT)) | set(_MENTION.findall(_section(VERDICT_TEXT, "Carried"))),
    key=lambda r: int(r[1:]),
)


def test_the_report_names_the_verdict_it_answers() -> None:
    """BU1. Without the header this file silently checks the wrong verdict.

    A missing header would make it fall back to the newest verdict -- which is
    the behaviour BU1 replaces -- so the absence is a failure, not a default.
    """
    assert ANSWERED, (
        "the newest report revision has no `Answers: verdict <n> @ <sha>` "
        "header. Without it there is no way to tell a report that predates a "
        "verdict from one that ignores it."
    )
    out = subprocess.run(["git", "cat-file", "-e", ANSWERED], cwd=ROOT, capture_output=True)
    assert out.returncode == 0, (
        f"the report answers verdict `{ANSWERED}`, which `git cat-file -e` "
        "cannot resolve. Either the sha is wrong, or the clone does not contain "
        "it -- a shallow checkout resolves nothing older than its depth, and "
        "that is a different fault from a typo (R273)."
    )
    assert len(re.findall(r"^Answers:", _newest_revision(REPORT_TEXT), re.MULTILINE)) == 1, (
        "the newest revision carries more than one `Answers:` header, so which "
        "verdict it claims to answer is ambiguous."
    )


def _blocking() -> set[str]:
    """Findings the verdict marks as blocking, read from its own headings."""
    out: set[str] = set()
    for m in re.finditer(r"^\*\*(R\d+)\.?\s*\(([^)]*)\)", VERDICT_TEXT, re.MULTILINE):
        if "block" in m.group(2).lower():
            out.add(m.group(1))
    return out


def test_a_blocking_item_is_not_routed_to_4a() -> None:
    """CF2. The verdict's classification of an item is authoritative.

    Four of eight blocking items were recorded `open -- 4a` in one revision.
    A report may say it has not answered an item; it may not re-file the
    verdict's ruling about which step that item belongs to.
    """
    blocking = _blocking()
    assert blocking, (
        f"no blocking finding parsed from {VERDICT.name}. The heading format "
        "changed and this check passes on anything."
    )
    misrouted = [
        i for i, st in _status_cells() if "4a" in _plain(st) and set(_MENTION.findall(i)) & blocking
    ]
    assert not misrouted, (
        f"{misrouted} are recorded at 4a and {VERDICT.name} marks them "
        "blocking. Where they are answered is the verdict's call, not the "
        "report's."
    )


def test_the_answered_verdict_is_the_NEWEST_one() -> None:
    """Item 1b, mechanically. It was the reviewer's eye and nothing else.

    A header naming a real but older verdict commit passed every check: the sha
    resolves, the findings parse, and the carry table is complete about a list
    that has been superseded.
    """

    def _newest_commit_touching(path: Path) -> str:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", str(path.relative_to(ROOT))],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        return out.stdout.strip() if out.returncode == 0 else ""

    head_verdict = _newest_commit_touching(VERDICT)
    head_report = _newest_commit_touching(REPORT)
    if not head_verdict or not head_report or not ANSWERED:
        return

    # THE LEGITIMATE BOUNDARY IS NOT A FAILURE, and the first version of this
    # test made it one (R282). `CLAUDE.md` § Step gating writes the report
    # first and the verdict after, so between them the report NECESSARILY names
    # an older verdict than the newest -- which is exactly the state at every
    # step boundary, and the state this file's own item 1b paragraph records as
    # the reason a machine was not given this job.
    #
    # ANCESTRY IS THE DISCRIMINATOR. If the newest verdict commit descends from
    # the newest report commit, the verdict landed AFTER the report and the
    # report legitimately predates it. If the report is the later of the two, it
    # was written with the newest verdict available and must name it.
    verdict_is_newer = subprocess.run(
        ["git", "merge-base", "--is-ancestor", head_report, head_verdict],
        cwd=ROOT,
        capture_output=True,
    )
    if verdict_is_newer.returncode == 0 and head_report != head_verdict:
        return

    assert ANSWERED.startswith(head_verdict[: len(ANSWERED)]) or head_verdict.startswith(
        ANSWERED
    ), (
        f"the report at `{head_report[:7]}` is newer than the verdict at "
        f"`{head_verdict[:7]}` and names `{ANSWERED[:7]}`. Written with the "
        "newest verdict available, it must answer that one."
    )


def test_the_guard_reads_the_step_being_worked_on() -> None:
    """Meta-test: a guard pointed at the wrong step is green for free, and a
    guard that dies at a step boundary is worse than either.

    It named step 4 while step 5 was open. CB2 made it follow the newest report
    and that took the suite down whenever a report had no verdict yet, which is
    every legitimate boundary. This is the one named test that carries both
    states, and it is a test rather than a collection error precisely so the
    other 1588 still run while it fires.
    """
    assert REPORTED, (
        f"no step report found under {REPORTS} -- the directory is missing, "
        "unreadable, or the naming changed. Every assertion in this file is "
        "about a report, so none of them means anything in this state."
    )
    assert STEP > 0, (
        f"reports exist for steps {sorted(REPORTED)} and verdicts for "
        f"{sorted(REVIEWED)}; no step has both. There is no carry list to check."
    )
    assert STEP_REPORT - STEP <= 1, (
        f"the newest report is step {STEP_REPORT} and the newest step with a "
        f"verdict is {STEP}. More than one step has been opened on top of an "
        "unreviewed one, which `CLAUDE.md` § Step gating forbids."
    )
    for step, spellings in sorted(_step_files(REPORTS).items()):
        assert len(spellings) == 1, (
            f"step {step} is spelled {sorted(spellings)} under {REPORTS}. Two "
            "files for one step means the guard reads one of them and the "
            "other is invisible; a step number has one spelling."
        )
    assert STEP_REPORT == STEP, (
        f"step {STEP_REPORT} has a report and no verdict yet. That is the "
        "legitimate boundary -- the verdict is written after the report is "
        f"committed -- and until it lands this guard checks step {STEP}, so "
        f"step {STEP_REPORT}'s carry list is UNCHECKED. Invoke the "
        "gating-supervisor."
    )


def test_the_parse_found_something_to_check() -> None:
    """Meta-test: zero parsed findings is a parse failure, not a clean bill."""
    assert _FINDING.findall(VERDICT_TEXT), (
        "no `**R<n>.` finding heading parsed from the verdict -- the format "
        "changed and every assertion below would pass on anything"
    )
    assert CARRIED.strip(), (
        "the newest report revision has no Carried section, so there is nothing " "to check against"
    )
    assert len(EXPECTED) >= 5, (
        f"only {EXPECTED} expected; the verdict carries more than that and the "
        "pattern is missing most of them"
    )


# A PARAMETRISED TEST WITH AN EMPTY LIST IS A COLLECTION ERROR, and this repo
# sets `empty_parameter_set_mark = "fail_at_collect"` (R234). An empty or
# unreadable verdict parses to no findings, and the whole file then failed to
# collect -- the same "no tests ran" failure the module-scope read had. The
# placeholder keeps collection alive so a NAMED test carries the message.
_NOTHING = "(no finding parsed from the verdict)"


@pytest.mark.parametrize("finding", EXPECTED or [_NOTHING])
def test_the_report_carries_the_finding(finding: str) -> None:
    if finding == _NOTHING:
        pytest.fail(
            f"{VERDICT} parsed to no `R<n>` finding at all -- it is empty, "
            "unreadable, or its format changed. Every carry assertion in this "
            "file is about that list, so none of them means anything here."
        )
    assert finding in _MENTION.findall(CARRIED), (
        f"{finding} is in the newest verdict -- as a finding or as an item it "
        "carries forward -- and the newest report revision's Carried section "
        "does not mention it. CLAUDE.md: the dependency list is part of what "
        "gets re-read at every step, by a reader that was not the one who "
        "skipped it."
    )


# CC1: THE VOCABULARY. A report says what IT did; a verdict says where the item
# stands. The two were the same word and a false status went unnoticed for a
# round -- the report recorded an item closed at a verdict whose own text read
# "MECHANISM VERIFIED, CLOSING CONDITION NOT MET. Carried, not closed."
#
# The guard below cannot check whether a status is TRUE -- its own docstring
# says so, and that is still true. What it can do is make the strongest word
# unavailable to the party that does not get to use it, so a report can no
# longer make a ruling at all. `closed` is the verdict's, and only the verdict's.
REPORT_WORDS = ("answered", "open", "withdrawn", "4a", "later", "carried")

# SYNONYMS ENUMERATED, because banning one spelling bans one spelling. The
# reviewer got the word past the first version four ways out of five: a bolded
# first cell, a backticked one (the adjacent table backticks every first cell,
# seventy times over), a third column, and `**resolved**, nothing open`.
VERDICT_ONLY = (
    "closed",
    "resolved",
    "settled",
    "complete",
    "finished",
    # R297's corpus, third layer: five spellings of closure that were not in
    # the tuple. `done` and `fixed` say the same thing the banned word says,
    # and `no longer open` said it while SATISFYING the report-word check,
    # because `open` is a substring of it.
    "done",
    "fixed",
    "no longer open",
)

_MARKUP = re.compile(r"[`*_~]+")
# Renderings of a word that are not spellings of it. A soft hyphen, an empty
# HTML comment and a numeric entity all render as `closed` in the published
# report and none of them contains the letters in order. Measured by the
# reviewer, three entries, all three got the word past the strip.
_INVISIBLE = re.compile(
    # soft hyphen, zero-width space, ZWNJ, ZWJ, BOM -- then an HTML
    # comment, which renders as nothing and can split a word in two.
    "[\u00ad\u200b\u200c\u200d\ufeff]"
    "|<!--.*?-->"
)


def _plain(cell: str) -> str:
    """Cell text AS RENDERED, lowercased -- not as typed.

    A status cell is read by a person looking at rendered markdown, so the
    check has to see what they see. Stripping markup was one third of that;
    the other two are characters that render as nothing and entities that
    render as a letter.
    """
    text = _INVISIBLE.sub("", cell)
    text = html.unescape(text)
    return _MARKUP.sub("", text).lower()


# THE FIRST CELL MAY BE DECORATED AND THE STATUS MAY BE IN ANY CELL AFTER IT.
# Three of the four formattings the reviewer tried went past the first version:
# a bolded first cell, a backticked one -- the adjacent table backticks every
# first cell, seventy times -- and a third column. Revision 5 said this edit had
# been made and it had not, which is why the claim now carries the cell it is
# checked by.
#
# AND THE ROW MAY BE INDENTED, AND THE NUMBER MAY BE SPACED. Two more of the
# reviewer's spellings: `  | R230 | ... |` did not anchor, and `| R 230 |`
# renders as the item and matches neither `_ROW` nor `_MENTION`. Both produced
# no status cell at all, which is the failure mode this pair of tests exists to
# prevent -- banning a word must not become saying nothing.
_ROW = re.compile(r"^[ \t]*\|([^|]*R\s*\d+[^|]*)\|(.+)\|\s*$", re.MULTILINE)
_LOOSE_MENTION = re.compile(r"\bR\s*\d+\b")


def _status_cells() -> list[tuple[str, str]]:
    """`(items, status)` for EVERY cell after the first, per Carried row."""
    out: list[tuple[str, str]] = []
    for items, rest in _ROW.findall(CARRIED):
        if not _LOOSE_MENTION.findall(items):
            continue
        for cell in rest.split("|"):
            if cell.strip():
                out.append((items.strip(), cell.strip()))
    return out


def test_a_report_does_not_say_CLOSED(capsys) -> None:
    """CC1. Only a verdict closes an item.

    Not a style rule. The report that prompted this recorded an item closed
    while the verdict it answered said the closing condition was not met, and
    nothing could catch it: a status is prose, and the carry guard checks that a
    status EXISTS, never that it is true. Taking the word away removes the
    failure mode rather than detecting it.
    """
    cells = _status_cells()
    assert cells, (
        "no status cell parsed from the newest revision's Carried table. The "
        "table format changed and every check below passes on anything."
    )
    guilty = [(i, st) for i, st in cells if any(w in _plain(st) for w in VERDICT_ONLY)]
    with capsys.disabled():
        print(f"\n  {len(cells)} status cells parsed, {len(guilty)} say `closed`")
    assert not guilty, (
        f"{[g[0] for g in guilty]} are recorded with a word only a verdict may "
        "use. A report says what it DID -- answered, open, withdrawn -- and the "
        "verdict says where the item stands. The report that made this rule "
        "recorded an item closed at a verdict reading 'Carried, not closed'."
    )


def test_every_carried_item_carries_one_of_the_report_words() -> None:
    """The other half: a status that says nothing is not better than a wrong one."""
    by_item: dict[str, list[str]] = {}
    for i, st in _status_cells():
        by_item.setdefault(i, []).append(st)
    # One ROW must carry a report word, not every cell of it.
    silent = [
        i
        for i, cells in by_item.items()
        if not any(w in _plain(c) for c in cells for w in REPORT_WORDS)
    ]
    assert not silent, (
        f"{silent} have a status that is none of {list(REPORT_WORDS)}. Banning "
        "one word is not the point; saying which of the three applies is."
    )


def test_no_status_claims_more_than_the_verdict_allows() -> None:
    """`withdrawn` is a ruling, and a report does not make rulings.

    It is the one report word that claims finality -- it says the item is gone,
    not that it was answered -- so it is the one that can contradict a verdict.

    THE DOMAIN IS EVERY ROW THAT SAYS IT. Two earlier versions built a domain
    and the word escaped both: three lines of twenty-one findings the first
    time, and every finding of the ANSWERED verdict the second -- which left an
    item from an older round outside the domain entirely, so a report could
    retire R241 by writing `withdrawn by me` and nothing looked. The reviewer
    measured exactly that. There is no domain to get wrong here: a row may say
    `withdrawn` when a verdict withdrew that item, and otherwise it may not.
    """
    # The WHOLE review file, every round of it, because a withdrawal ruled two
    # verdicts ago is still a withdrawal -- and the item is still carried.
    ruled: set[str] = set()
    for line in _read(VERDICT).splitlines():
        if "withdraw" in line.lower():
            ruled.update(_MENTION.findall(line))
    claiming = [
        (i, st)
        for i, st in _status_cells()
        if "withdrawn" in _plain(st) and not (set(_MENTION.findall(i)) & ruled)
    ]
    assert not claiming, (
        f"{[c[0] for c in claiming]} are reported as withdrawn and no verdict "
        f"in {VERDICT.name} withdraws them. A report says what it DID; whether "
        "an item is gone is the verdict's to say. If the withdrawal is of the "
        "report's own claim rather than of the finding, say `answered` and "
        "state what was withdrawn."
    )


# R296 / R301: THE TABLE IS THE GENERATOR'S OUTPUT, OR IT IS NOT THE TABLE.
#
# `scripts/carried_table.py` was written because two revisions in a row wrote
# statuses under the wrong numbers. It was then committed, correct, and run by
# NOTHING -- so the next revision's table was shifted by one in three rows
# while a script that would not have shifted them sat in the repository. A
# generator nothing executes is a comment.
ANSWERS = REPORTS / f"step-{STEP}-answers.json"


def _generator():
    """`scripts/carried_table.py` as a module, without a `scripts` package."""
    spec = importlib.util.spec_from_file_location(
        "carried_table", ROOT / "scripts" / "carried_table.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_the_Carried_table_is_what_the_generator_produces() -> None:
    """The published command, run here, against what was published."""
    assert ANSWERS.is_file(), (
        f"{ANSWERS.name} is not committed. The report publishes the command "
        "that builds its own table; a command whose input is untracked cannot "
        "be run by the person reading it, which is R296."
    )
    gen = _generator()
    answers = json.loads(ANSWERS.read_text(encoding="utf-8"))
    produced = gen.table(_read(VERDICT), answers)
    body = "\n".join(line.rstrip() for line in CARRIED.splitlines())
    missing = [ln for ln in produced.splitlines() if ln.rstrip() not in body.splitlines()]
    assert not missing, (
        f"{len(missing)} generated rows are not in the report's Carried "
        f"section, the first being:\n  {missing[0]}\n"
        f"Regenerate with:\n  python scripts/carried_table.py {VERDICT} "
        f"{ANSWERS}"
    )


def test_the_generator_would_catch_a_row_under_the_wrong_number() -> None:
    """The check that makes the generator worth running (R296).

    A status written under the wrong number is a status whose declared site
    belongs to a different finding's block. This is the ablation: move one
    row's site to a path its own block does not name, and the generator must
    refuse to print the table at all.
    """
    gen = _generator()
    answers = json.loads(ANSWERS.read_text(encoding="utf-8"))
    answered = dict(answers["answered"])
    victim = next(i for i in answered if i in gen.blocks(_read(VERDICT)))
    answered[victim] = dict(answered[victim], site="floatfea/does_not_appear.py")
    with pytest.raises(SystemExit) as caught:
        gen.table(_read(VERDICT), {"answered": answered})
    assert victim in str(caught.value)


# CE1: THE REPORT CARRIES CI, PER JOB, FROM THE RUN ITSELF.
#
# CI was red at three consecutive reviewed commits and no revision mentioned it.
# One of those reds was the report's own commit: the `guards` job had already
# run and finished red four minutes before the report was pushed, and the
# revision listed every other job and omitted the one it had just created.
#
# A reviewer reads CI because `docs/SUPERVISOR.md` item 3b tells them to. The
# person writing the report had no such instruction that anything enforced, so
# "the suite is green" meant the laptop.
_CI_ROW = re.compile(
    r"^\|\s*`?([\w .\-]+?)`?\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
    re.MULTILINE,
)


def _ci_section() -> str:
    """The CI section: the one whose body actually holds the per-job table.

    Matching the heading text alone took the LAST heading containing `CI`, and
    a revision that also discusses CI in prose has several. The table is what
    identifies the section, which is the thing being checked.
    """
    body = _newest_revision(REPORT_TEXT)
    best = ""
    for m in re.finditer(r"^##+ .*$", body, re.MULTILINE):
        nxt = re.search(r"^##+ ", body[m.end() :], re.MULTILINE)
        chunk = body[m.end() : m.end() + nxt.start()] if nxt else body[m.end() :]
        if len(_CI_ROW.findall(chunk)) > len(_CI_ROW.findall(best)):
            best = chunk
    return best


def _reported_ci() -> dict[str, tuple[int, int, int]]:
    """`{job: (passed, failed, skipped)}` as the newest revision states them."""
    return {
        job.strip(): (int(p), int(f), int(sk)) for job, p, f, sk in _CI_ROW.findall(_ci_section())
    }


def test_the_report_carries_a_CI_SECTION() -> None:
    """CE1. A red CI that no report mentions is a red CI nobody reads."""
    body = _ci_section()
    assert body.strip(), (
        "the newest report revision has no `## ... CI ...` section. Three "
        "consecutive reviewed commits were red on CI and no revision said so; "
        "one of the reds was the report's own commit."
    )
    rows = _reported_ci()
    assert rows, (
        "the CI section states no per-job row. The required shape is a table of "
        "`| job | passed | failed | skipped |`, taken from `gh run view` at the "
        "commit the report is written on -- not a sentence about the laptop."
    )
    assert len(rows) >= 3, (
        f"only {sorted(rows)} reported. Every job in the workflow has a row, "
        "including the ones that did not run: a job that never ran is the "
        "finding that hides best."
    )


_SHA_IN_SECTION = re.compile(r"\b[0-9a-f]{7,40}\b")


def test_the_CI_section_is_about_the_ANSWERED_commit() -> None:
    """CG3. A CI table is a measurement of one commit, and it says which.

    Revision 7 published a table for `73cf6ce` in a revision written at
    `a949709` and stated in the present tense that the only two reds were the
    sine and cosine comparisons. At the commit it was written on there were
    twelve red jobs and ten of them were neither. The report could not have
    known -- the run started after it was pushed -- which is exactly why the
    table must name the commit it describes.

    The commit it can describe is the one it ANSWERS: the verdict is pushed
    before the report is written, so its run has finished. `Answers:` already
    names that commit, so the two are checked against each other and a table
    carried forward from a previous revision is red.
    """
    body = _ci_section()
    found = _SHA_IN_SECTION.findall(body)
    assert found, (
        "the CI section names no commit. `python scripts/ci_section.py "
        f"{ANSWERED[:7]}` generates the section, header included."
    )
    assert found[0].startswith(ANSWERED[:7]) or ANSWERED.startswith(found[0]), (
        f"the CI section's first commit is `{found[0]}` and the report answers "
        f"`{ANSWERED[:7]}`. A table for another commit is a measurement of "
        "another state; regenerate it with `python scripts/ci_section.py "
        f"{ANSWERED[:7]}`."
    )


def test_the_reported_CI_counts_are_not_all_zero() -> None:
    """The other half: a table of zeros satisfies the shape and says nothing."""
    rows = _reported_ci()
    assert any(p or f for p, f, _ in rows.values()), (
        f"every CI row in {REPORT.name} reports zero passed and zero failed. "
        "That is the shape without the measurement."
    )


def _changed_lines() -> dict[str, set[int]]:
    """`{path: {old-side line numbers touched}}` since the reviewed commit.

    `-U0` so a hunk covers only what changed, and the OLD side because that is
    the coordinate system the verdict's line numbers are written in.

    Reviewed commit -> WORKING TREE, not -> HEAD: the step is answered before it
    is committed, and a check that only saw committed work would demand the
    answer be committed before it could be shown to be an answer.
    """
    reviewed = _reviewed_commit(VERDICT_TEXT)
    if not reviewed:
        return {}, "the verdict states no `Reviewed commit:` line"
    # THE RETURN CODE IS READ (CC3). It was not, so a `git diff` against a
    # commit the clone does not contain returned an empty touched-set --
    # indistinguishable from "the step changed nothing", and 23 site checks
    # passed for that reason on every shallow checkout. One machine, one commit,
    # one variable: full clone `122 passed`, `git clone --depth 1`
    # `23 failed, 99 passed`. A guard cannot report what it cannot tell apart.
    out = subprocess.run(["git", "diff", "-U0", reviewed], cwd=ROOT, capture_output=True)
    if out.returncode != 0:
        # RETURNED, NOT RAISED (CD1). Raising here runs at module scope, which
        # is R234 again: the import dies and nothing in the file is collected.
        # The message travels to a named test instead.
        return {}, (
            f"`git diff -U0 {reviewed}` failed with {out.returncode}: "
            f"{out.stderr.decode('utf-8', errors='replace').strip()}. The most "
            "likely cause is a shallow clone that does not contain the reviewed "
            "commit -- set `fetch-depth: 0`. An empty result here would be "
            "read as 'the step touched nothing', which is why it is reported."
        )
    text = out.stdout.decode("utf-8", errors="replace")
    touched: dict[str, set[int]] = {}
    path = ""
    for line in text.splitlines():
        if line.startswith("--- a/"):
            path = line[6:].strip()
        elif line.startswith("--- /dev/null"):
            path = ""
        elif line.startswith("+++ b/") and not path:
            path = line[6:].strip()
        elif line.startswith("@@") and path:
            m = re.match(r"@@ -(\d+)(?:,(\d+))? ", line)
            if m:
                start, count = int(m.group(1)), int(m.group(2) or 1)
                # A pure insertion has count 0 and sits AFTER `start`; count the
                # neighbouring lines so an answer that ADDS lines at a named site
                # closes it.
                span = range(start, start + count) if count else (start, start + 1)
                touched.setdefault(path, set()).update(span)
    return touched, None


def _sites_by_finding() -> list[tuple[str, str, int]]:
    """`(finding, path, line)` for every site a finding names; line 0 = no line.

    A finding's block ends at the next finding OR the next `##` heading, so the
    last finding no longer absorbs every path to end-of-file (R171).
    """
    blocks = list(re.finditer(r"^\*\*(R\d+)[.\s]", VERDICT_TEXT, re.MULTILINE))
    out: list[tuple[str, str, int]] = []
    for i, m in enumerate(blocks):
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(VERDICT_TEXT)
        nxt = re.search(r"^##+ ", VERDICT_TEXT[m.end() : end], re.MULTILINE)
        if nxt:
            end = m.end() + nxt.start()
        for path, first, last in _SITE.findall(VERDICT_TEXT[m.start() : end]):
            if not first:
                out.append((m.group(1), path, 0))
                continue
            lo, hi = int(first), int(last or first)
            for line in range(lo, hi + 1):  # ranges expand, not endpoints
                out.append((m.group(1), path, line))
    return sorted(set(out))


SITES = _sites_by_finding()
TOUCHED, TOUCHED_ERROR = _changed_lines()


def test_the_diff_the_site_check_needs_is_available() -> None:
    """CD1. A guard that cannot see the diff must SAY so, not report nothing.

    `git diff` against a commit the clone does not contain returns empty, which
    reads exactly like "the step changed nothing" -- so every site check passed
    for that reason on a shallow checkout. Measured on one machine, one commit,
    one variable: full clone `122 passed`, `git clone --depth 1`
    `23 failed, 99 passed`.

    This is a named test rather than a raise because a raise at module scope is
    R234: the import dies and none of the file is collected.
    """
    assert TOUCHED_ERROR is None, TOUCHED_ERROR


_NO_SITE = ("(no site parsed)", "", 0)


@pytest.mark.parametrize(
    "finding, path, line",
    SITES or [_NO_SITE],
    ids=[f"{f}-{p}" + (f":{n}" if n else "") for f, p, n in (SITES or [_NO_SITE])],
)
def test_every_named_site_is_touched_or_declared(finding: str, path: str, line: int) -> None:
    """A finding that names lines is answered at all of them, or says which not.

    FIVE consecutive rounds closed a site-naming condition at some of its sites
    and recorded it as answered -- four of eight in the last one, at file
    resolution. The escape hatch is deliberate and explicit: the report may write
    `no change` beside the exact site, which is a claim a reviewer can check,
    rather than an omission nobody sees.
    """
    if (finding, path, line) == _NO_SITE:
        pytest.fail(
            f"{VERDICT} names no file site at all. Either it is unreadable or "
            "the site pattern stopped matching; both make this check pass on "
            "anything."
        )
    if TOUCHED_ERROR is not None:
        # REPORTED ONCE, by `test_the_diff_the_site_check_needs_is_available`.
        # Asserting it here too turned one diagnosis into ninety identical
        # failures, which buries the sentence that says what actually happened.
        # This is not a pass being hidden: that test fails, by name, loudly.
        return
    hit = [p for p in TOUCHED if p.endswith(path)]
    if hit and (line == 0 or any(line in TOUCHED[p] for p in hit)):
        return

    site = f"{path}:{line}" if line else path
    for text_line in _newest_revision(REPORT_TEXT).splitlines():
        if not re.search(r"no change", text_line, re.IGNORECASE):
            continue
        if site in text_line or (line == 0 and path in text_line):
            return
    pytest.fail(
        f"{finding} names {site}, the step's diff does not touch it, and the "
        "newest report revision does not say `no change` beside that exact "
        "site. Either answer it or declare it unanswered by name -- half of an "
        "item is not the item."
    )
