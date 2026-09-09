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

import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "docs" / "reviews" / "F2"
REPORTS = ROOT / "docs" / "reports" / "F2"


def _newest_step() -> int:
    """The highest step number that has a report.

    HARDCODED TO STEP 4 UNTIL CB2. Step 5 opened, a report and two verdicts were
    written for it, and this guard went on reading step 4's pair -- so every
    assertion below stayed green about a step nobody was working on, which is
    the most expensive way for a guard to pass. It follows the newest report
    now.
    """
    steps = [
        int(q.stem.split("-")[1])
        for q in REPORTS.glob("step-*.md")
        if q.stem.split("-")[1].isdigit()
    ]
    return max(steps) if steps else 0


STEP = _newest_step()
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
    """Permissive: a verdict written with a Windows-1252 dash must not make a
    guard raise, because a guard that raises is a guard that gets removed."""
    return path.read_bytes().decode("utf-8", errors="replace")


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
        f"the report answers verdict `{ANSWERED}`, which is not a commit in " "this repository."
    )
    assert len(re.findall(r"^Answers:", _newest_revision(REPORT_TEXT), re.MULTILINE)) == 1, (
        "the newest revision carries more than one `Answers:` header, so which "
        "verdict it claims to answer is ambiguous."
    )


def test_the_guard_reads_the_step_being_worked_on() -> None:
    """Meta-test for CB2: a guard pointed at the wrong step is green for free.

    It named step 4 while step 5 was open, so it checked a report that could not
    change against a verdict that had already been answered. Both files have to
    exist for the step this guard claims to cover.
    """
    assert STEP > 0, f"no step report found under {REPORTS}"
    assert REPORT.is_file(), f"{REPORT} is the newest report and does not exist"
    assert VERDICT.is_file(), (
        f"{REPORT.name} is the newest step report and {VERDICT} does not exist. "
        "A step with no verdict file is a step whose carry list this guard "
        "cannot check at all."
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


@pytest.mark.parametrize("finding", EXPECTED)
def test_the_report_carries_the_finding(finding: str) -> None:
    assert finding in _MENTION.findall(CARRIED), (
        f"{finding} is in the newest verdict -- as a finding or as an item it "
        "carries forward -- and the newest report revision's Carried section "
        "does not mention it. CLAUDE.md: the dependency list is part of what "
        "gets re-read at every step, by a reader that was not the one who "
        "skipped it."
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
        return {}
    out = subprocess.run(["git", "diff", "-U0", reviewed], cwd=ROOT, capture_output=True)
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
    return touched


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
TOUCHED = _changed_lines()


@pytest.mark.parametrize(
    "finding, path, line", SITES, ids=[f"{f}-{p}" + (f":{n}" if n else "") for f, p, n in SITES]
)
def test_every_named_site_is_touched_or_declared(finding: str, path: str, line: int) -> None:
    """A finding that names lines is answered at all of them, or says which not.

    FIVE consecutive rounds closed a site-naming condition at some of its sites
    and recorded it as answered -- four of eight in the last one, at file
    resolution. The escape hatch is deliberate and explicit: the report may write
    `no change` beside the exact site, which is a claim a reviewer can check,
    rather than an omission nobody sees.
    """
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
