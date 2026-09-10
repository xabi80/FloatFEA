#!/usr/bin/env python
"""Generate a step report's CI section from the run itself (CG3).

    python scripts/ci_section.py <sha> > section.md

WHY IT IS GENERATED. CE1 made a CI section mandatory because CI had been red at
three consecutive reviewed commits and no revision said so. The section then
became a hand-copied table, and hand-copying failed the way hand-copying fails:
one revision published a table for a DIFFERENT commit than the one it was
written at, and stated "both reds are the sine and cosine round-trip
comparisons" while twelve jobs were red and ten of them were neither.

The report cannot know about a run that starts after it is pushed. It can know
about the run at the commit it ANSWERS -- the verdict commit named in its
`Answers:` header -- and that is the sha this takes. `tests/test_report_carried.py`
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

# pytest's own summary line, and the ladder rung's structured one. The rung
# hides pytest's stdout on purpose (CG4), so these are two different shapes and
# both have to be read.
_RUNG = re.compile(
    r"run_rung: (\d+) collected, (\d+) failed, (\d+) errored, (\d+) skipped"
)
_PYTEST = re.compile(r"^(?=.*\bin \d+\.\d+s)(.*)$")
_COUNT = re.compile(r"(\d+) (passed|failed|error|errors|skipped|xfailed|xpassed)")


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
    out = subprocess.run(
        ["git", "rev-parse", sha], capture_output=True, text=True
    )
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


def counts(run_id: int) -> dict[str, tuple[int, int, int]]:
    """`{job: (passed, failed, skipped)}` read from the run's log."""
    log = _gh("run", "view", str(run_id), "--log")
    out: dict[str, list[int]] = {}
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
                acc[0] += found["passed"]
                acc[1] += found["failed"]
                acc[2] += found["skipped"]
    return {k: (v[0], v[1], v[2]) for k, v in out.items()}


def section(sha: str) -> str:
    sha = full_sha(sha)
    run = run_for(sha)
    jobs = json.loads(_gh("run", "view", str(run["databaseId"]), "--json", "jobs"))["jobs"]
    measured = counts(run["databaseId"])

    lines = [
        f"## 0. CI at the answered commit `{sha[:7]}`",
        "",
        f"Generated: `python scripts/ci_section.py {sha[:7]}`. Run "
        f"`{run['databaseId']}`, event `{run['event']}`, conclusion "
        f"**{run['conclusion']}**.",
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
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    sys.stdout.write(section(argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
