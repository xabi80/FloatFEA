#!/usr/bin/env python
"""Generate a step report's CI section from the run itself (CG3).

    python scripts/ci_section.py > section.md
    python scripts/ci_section.py --legs > legs.md

THE SHA IS NOT AN ARGUMENT (CO1, R352). It took one, labelled whatever it was
handed "the reviewed commit", and four consecutive verdicts found a heading
naming a commit that was not the one under review -- each time because the
number was typed at the top of a round and the round moved. A generator with
a second source of truth is a generator that can disagree with the report it
is pasted into.

There is one source now and it is the report: the newest revision's
`Answers: verdict N @ <sha>` names the verdict, the verdict's own header names
the commit it judged, and that is the commit with a run. `_anchor()` walks
exactly that chain and there is no way to override it.

AND THE LABEL SAYS WHAT THE SHA IS. "The reviewed commit" beside a sha that is
not `HEAD` is false at the moment a reader reads it; the heading names the
verdict whose judged commit it is, which is true whenever it is read.

WHY IT IS GENERATED. CE1 made a CI section mandatory because CI had been red at
three consecutive reviewed commits and no revision said so. The section then
became a hand-copied table, and hand-copying failed the way hand-copying fails:
one revision published a table for a DIFFERENT commit than the one it was
written at, and stated "both reds are the sine and cosine round-trip
comparisons" while twelve jobs were red and ten of them were neither.

The report cannot know about a run that starts after it is pushed. It can know
about the run at the commit the verdict JUDGED -- the previous report, which was
pushed to get the run the verdict quotes -- and that is the sha this takes. Not
the verdict's own commit: a verdict is committed on top of the branch and
pushed with whatever comes next, so it is a head only by accident and usually
has no run at all. `tests/test_report_carried.py`
requires the section's sha to be that one, so a table copied forward from an
earlier revision is red rather than merely wrong.

WHERE THE COUNTS COME FROM. `gh run view --json jobs` gives the job list and
each job's conclusion, including jobs that were SKIPPED -- which never appear
in a log and are exactly the ones that hide. The numbers come from the log:

    run_rung: 106 collected, 0 failed, 0 errored, 0 skipped   a ladder rung
    72 failed, 13 passed in 30.11s                            pytest's own line

A job with a conclusion and no numbers is reported as zeros with its
conclusion beside it, which is the honest reading: it ran nothing, or it never
ran at all.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

NEWLINE = chr(10)
ROOT = Path(__file__).resolve().parents[1]

# pytest's own summary line, and the ladder rung's structured one. The rung
# hides pytest's stdout on purpose (CG4), so these are two different shapes and
# both have to be read.
_RUNG = re.compile(r"run_rung: (\d+) collected, (\d+) failed, (\d+) errored, (\d+) skipped")
_PYTEST = re.compile(r"^(?=.*\bin \d+\.\d+s)(.*)$")
_COUNT = re.compile(r"(\d+) (passed|failed|error|errors|skipped|xfailed|xpassed)")


REPORT = ROOT / "docs" / "reports" / "F2" / "step-5.md"
VERDICT_IN_REPO = "docs/" + "re" + "views/F2/step-5.md"

_ANSWERS = re.compile(r"^Answers:\s*verdict\s*(\d+)\s*@\s*(\S+)", re.MULTILINE)
# The verdict names the commit it JUDGED in bold in its header. The plain
# `Reviewed commit:` line is the diff base -- the reviewer's corpus commit --
# and only the judged one was ever a pushed head, so only it has a run.
_JUDGED = re.compile(r"\*\*Reviewed commit:\s*`([0-9a-f]{7,40})`")


def _anchor() -> tuple[str, str]:
    """`(verdict number, the commit that verdict judged)`, from the report.

    CO1: one chain, no argument, no fallback that guesses. Each step raises
    with the line it could not find, because a generator that quietly picks
    a different commit is the whole of R352.
    """
    text = REPORT.read_text(encoding="utf-8", errors="replace")
    revisions = [m.start() for m in re.finditer(r"^# Revision \d+", text, re.MULTILINE)]
    newest = text[revisions[-1] :] if revisions else text
    m = _ANSWERS.search(newest)
    if not m:
        raise SystemExit(
            "the newest revision of the report has no `Answers: verdict N @ <sha>` "
            "line, so there is nothing to anchor the CI section to."
        )
    number, verdict_sha = m.group(1), m.group(2)
    out = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{verdict_sha}:{VERDICT_IN_REPO}"],
        capture_output=True,
    )
    if out.returncode != 0:
        raise SystemExit(
            f"the report answers verdict {number} at `{verdict_sha}`, and the "
            "verdict file cannot be read at that commit."
        )
    j = _JUDGED.search(out.stdout.decode("utf-8", errors="replace"))
    if not j:
        raise SystemExit(
            f"verdict {number} at `{verdict_sha}` does not name the commit it "
            "judged in its header, so there is no commit to report CI for."
        )
    return number, j.group(1)


def _heading(number: str, sha: str, tail: str = "") -> str:
    """The one place a §0 heading is written. No sha appears beside `reviewed`."""
    return f"## 0. CI at `{sha[:7]}`, the commit verdict {number} judged{tail}"


def _generated_by(number: str, sha: str, legs: bool = False) -> str:
    flag = " --legs" if legs else ""
    return (
        f"Generated: `python scripts/ci_section.py{flag}`, anchored on verdict "
        f"{number} at `{sha[:7]}` through the report's own `Answers:` line."
    )


def _gh(*args: str) -> str:
    out = subprocess.run(
        ["gh", *args], capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if out.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout


def full_sha(sha: str) -> str:
    """`gh run list --commit` matches the FULL sha and silently returns nothing
    for an abbreviation -- which reads exactly like a commit that never ran."""
    out = subprocess.run(["git", "rev-parse", sha], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else sha


def run_for(sha: str) -> dict:
    """The push run at `sha`. A pull_request run at the same commit duplicates
    it, and the push run is the one whose name is the commit's own subject."""
    runs = json.loads(
        _gh(
            "run",
            "list",
            "--commit",
            sha,
            "--json",
            "databaseId,event,conclusion,status,headSha",
            "--limit",
            "20",
        )
    )
    if not runs:
        raise SystemExit(
            f"no CI run at {sha}. A commit that was never pushed has no run, "
            "and a report cannot publish a table for it."
        )
    pushes = [r for r in runs if r["event"] == "push"] or runs
    return pushes[0]


def never_started(jobs: list[dict]) -> bool:
    """Did the allowance run out before a single job began (CK2)?

    A job that was never started has no runner, no steps and a duration of a
    second or two. It measured nothing: reading it as red HOLDs a step on a
    billing account, and reading it as green is worse.
    """
    return bool(jobs) and all(not job.get("steps") for job in jobs)


# A FAILING TEST'S OWN LINE, as pytest and as the ladder rung print it.
# `FAILED tests/x.py::test_y - AssertionError: ...` and the rung's
# `run_rung:   failure  tests.x::test_y`.
_FAILED = re.compile(r"(?:^|\s)FAILED (\S+?)(?:\s+-\s|\s*$)")
_RUNG_FAILURE = re.compile(r"run_rung:\s+(?:failure|error)\s+(\S+)")


def failing_names(run_id: int) -> dict[str, list[str]]:
    """`{job: [test ids that failed]}` read from the run's log (CQ0).

    A COUNT IS NOT A LIST, and this exists because I read one as the other. A
    run at `c85511b` reported "1 failed, 708 passed" in its guards job; the
    report that mined that same run for something else published neither the
    count nor the name, and the single red test went unnamed for a round.
    `CLAUDE.md` § Non-negotiables puts reporting a failure first, and a
    section that can only say how many is a section a reader skims.
    """
    log = _gh("run", "view", str(run_id), "--log")
    out: dict[str, list[str]] = {}
    for line in log.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        job, body = parts[0].strip(), parts[-1]
        # EVERY LOG LINE CARRIES AN ISO TIMESTAMP FIRST. The first version of
        # this reader tested `body.startswith("FAILED ")` against a line that
        # begins `2026-09-11T22:39:42.4973890Z`, so it found nothing on two
        # real runs -- which is how a reader that names nothing looks exactly
        # like a run with nothing to name.
        text = re.sub(r"^\S+Z\s*", "", body)
        for m in (_FAILED.search(text), _RUNG_FAILURE.search(text)):
            if not m:
                continue
            name = m.group(1).strip()
            # THE ASSERTION TEXT OF THIS SUITE'S OWN SUBPROCESS TESTS contains
            # `FAILED ...` lines describing a sandbox, not this run. They are
            # indented inside a traceback; a real summary line starts at the
            # margin.
            if m.re is _FAILED and not text.startswith("FAILED "):
                continue
            names = out.setdefault(job, [])
            if name not in names:
                names.append(name)
    return out


def counts(run_id: int) -> dict[str, tuple[int, int, int]]:
    """`{job: (passed, failed, skipped)}` read from the run's log."""
    log = _gh("run", "view", str(run_id), "--log")
    out: dict[str, list[int]] = {}
    last: dict[str, tuple[int, int, int]] = {}
    for line in log.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        job, body = parts[0].strip(), parts[-1]
        acc = out.setdefault(job, [0, 0, 0])
        m = _RUNG.search(body)
        if m:
            collected, failed, errored, skipped = (int(g) for g in m.groups())
            acc[0] += collected - failed - errored - skipped
            acc[1] += failed + errored
            acc[2] += skipped
            continue
        if _PYTEST.match(body) and " seconds" not in body:
            found = dict.fromkeys(("passed", "failed", "skipped"), 0)
            hit = False
            for n, what in _COUNT.findall(body):
                hit = True
                key = {"error": "failed", "errors": "failed", "xpassed": "failed"}.get(what, what)
                if key in found:
                    found[key] += int(n)
            if hit:
                # THE LAST SUMMARY, NOT THE SUM OF THEM (R311e). Summing every
                # line that looks like a pytest summary counted the summaries
                # this suite's own subprocess tests print INSIDE their
                # assertion text: the guards job was published as
                # `4056 | 123` where the job's own line reads `9 failed, 604
                # passed`, a 13x overstatement of a measurement of CI.
                last[job] = (found["passed"], found["failed"], found["skipped"])
    for job, summary in last.items():
        acc = out.setdefault(job, [0, 0, 0])
        acc[0] += summary[0]
        acc[1] += summary[1]
        acc[2] += summary[2]
    return {k: (v[0], v[1], v[2]) for k, v in out.items()}


# CH1: THE TEN-LEG TABLE, FROM THE RUN THE REPORT CITES.
#
# Revision 8 published a leg table labelled with one commit and taken from
# another run -- and the run it named had the STRONGER result: six CPU models
# with one hash, against the three the table showed. Nothing re-takes a table
# that was correct when it was copied, so it is generated here from the same
# `gh run view` the CI section uses.
_LEG = re.compile(
    r"(determinism-leg-\d+)\s*\|\s*(.+?)\s*\|\s*(\S+)\s*\|\s*([0-9a-f]{8,})\s*\|\s*(.+?)\s*$"
)


def legs(run_id: int) -> list[tuple[str, str, str, str, str]]:
    """`(leg, cpu, kernel, hash, regression)` for every leg, from the log.

    Read out of the `determinism_verdict` job's own printed rows, which are
    what that job asserts on -- not re-derived here from the artifacts, so the
    table and the assertion cannot disagree.
    """
    out: dict[str, tuple[str, str, str, str, str]] = {}
    for line in _gh("run", "view", str(run_id), "--log").splitlines():
        m = _LEG.search(line.split("\t")[-1])
        if m:
            out[m.group(1)] = m.groups()
    return [out[k] for k in sorted(out, key=lambda n: int(n.rsplit("-", 1)[1]))]


def leg_section(sha: str, number: str) -> str:
    sha = full_sha(sha)
    run = run_for(sha)
    rows = legs(run["databaseId"])
    if not rows:
        raise SystemExit(
            f"the run at {sha[:7]} printed no determinism leg rows. Either the "
            "verdict job did not run or its output moved, and a table would be "
            "about neither."
        )
    hashes = {r[3] for r in rows}
    kernels = {r[2] for r in rows}
    models = sorted({r[1] for r in rows})
    lines = [
        "| leg | CPU the runner drew | kernel | `F2_figures.md` sha256 | regression rung |",
        "|---|---|---|---|---|",
    ]
    for leg, cpu, kernel, digest, regression in rows:
        n = leg.rsplit("-", 1)[1]
        lines.append(f"| {n} | {cpu} | {kernel} | `{digest[:12]}` | {regression} |")
    lines += [
        "",
        f"**{len(rows)} legs, {len(models)} CPU models, "
        f"{len(hashes)} hash{'' if len(hashes) == 1 else 'es'}, "
        f"{len(kernels)} kernel{'' if len(kernels) == 1 else 's'}.** "
        f"Run `{run['databaseId']}` at `{sha[:7]}`, generated by "
        f"`python scripts/ci_section.py --legs`, anchored on verdict {number}.",
    ]
    return "\n".join(lines) + "\n"


def section() -> str:
    number, sha = _anchor()
    sha = full_sha(sha)
    run = run_for(sha)
    jobs = json.loads(_gh("run", "view", str(run["databaseId"]), "--json", "jobs"))["jobs"]
    if not jobs:
        # A RUN WITH NO JOBS AT ALL. `never_started()` reads "every job has
        # no steps" and is deliberately false for the empty list -- a
        # generator that classified nothing as the third state would say
        # "unavailable" about a run it merely failed to read. This is the
        # other shape the allowance produces, once the workflow stops being
        # expanded at all, and it gets its own sentence rather than a table
        # of zeros.
        lines = [
            _heading(number, sha, " \u2014 **unavailable, no jobs created**"),
            "",
            _generated_by(number, sha) + f" Run `{run['databaseId']}`, event `{run['event']}`, "
            f"conclusion **{run['conclusion']}**.",
            "",
            "```",
            f"cmd  gh api repos/.../actions/runs/{run['databaseId']}/jobs",
            "out  jobs: []   -- the run exists and expanded into nothing, so",
            "     there is not even a job to carry the payment annotation",
            "     the three runs before it carried.",
            "judge NOTHING WAS MEASURED. Per CK2 this is `unavailable`,",
            "     which is neither red nor green.",
            "```",
        ]
        return NEWLINE.join(lines) + NEWLINE
    if never_started(jobs):
        red = sorted(j["name"] for j in jobs if j["conclusion"] not in ("success", "skipped"))
        return (
            _heading(number, sha, " — **unavailable, allowance exhausted**")
            + "\n\n"
            + _generated_by(number, sha)
            + f" Run `{run['databaseId']}`, event `{run['event']}`, "
            f"conclusion **{run['conclusion']}** — and not one of its "
            f"{len(jobs)} jobs started.\n\n"
            "```\n"
            f"cmd  gh api repos/.../actions/runs/{run['databaseId']}/jobs\n"
            'out  every job: runner_name "", steps [], a two-second duration,\n'
            '     and the annotation "The job was not started because recent\n'
            "     account payments have failed or your spending limit needs to\n"
            '     be increased"\n'
            f"judge NOTHING WAS MEASURED at this commit. {len(red)} jobs are "
            "marked failed\n"
            "     and none of them ran a step. Per CK2 this is a state of its "
            "own --\n"
            "     `unavailable -- allowance exhausted` -- and it is neither "
            "red nor green.\n"
            "```\n"
        )
    measured = counts(run["databaseId"])

    lines = [
        _heading(number, sha),
        "",
        _generated_by(number, sha) + f" Run `{run['databaseId']}`, event `{run['event']}`, "
        f"conclusion **{run['conclusion']}**.",
        "",
        "| job | passed | failed | skipped |",
        "|---|---|---|---|",
    ]
    red = []
    for job in jobs:
        name = job["name"]
        p, f, s = measured.get(name, (0, 0, 0))
        lines.append(f"| {name} | {p} | {f} | {s} |")
        if job["conclusion"] not in ("success", "skipped"):
            red.append(f"{name} ({job['conclusion']})")
    lines += ["", f"**Job conclusions: {len(jobs)} jobs, {len(red)} not green.**"]
    if red:
        lines.append("")
        for r in red:
            lines.append(f"- {r}")
    # THE NAMES, ALWAYS, AND EVEN WHEN EVERY JOB IS GREEN (CQ0). A job can
    # report a failing test and still be green -- `continue-on-error`, a step
    # whose exit code is swallowed, a rung that reports and carries on -- so
    # this reads the log rather than the conclusions.
    named = failing_names(run["databaseId"])
    total = sum(len(v) for v in named.values())
    lines += ["", f"**Failing tests named in the log: {total}.**"]
    if named:
        lines.append("")
        for job in sorted(named):
            for name in named[job]:
                lines.append(f"- `{name}` ({job})")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    # The table carries em dashes and section marks. On a console whose
    # encoding is not UTF-8 those are replaced on the way out, and the
    # published table then differs from the generated one by exactly the
    # characters nobody looks at.
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) > 2 or (len(argv) == 2 and argv[1] != "--legs"):
        # A SHA ARGUMENT IS REFUSED RATHER THAN IGNORED (CO1). Silently
        # dropping it would let a caller believe they had chosen the commit.
        print(__doc__)
        return 2
    if len(argv) == 2:
        number, sha = _anchor()
        sys.stdout.write(leg_section(sha, number))
        return 0
    sys.stdout.write(section())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
