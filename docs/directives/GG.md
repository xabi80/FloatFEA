# DIRECTIVE GG — R1 tidy-up, then park

*Recorded verbatim under FP0, 10 November 2026, as the first commit of the turn that acts on
it. The text below is the directive as received, unaltered. Provenance: pasted directive
message from Xabier. See `docs/directives/README.md`.*

---

DIRECTIVE GG — R1 tidy-up, then park
Record: docs/directives/GG.md. One standalone `process:` commit for
GG1–GG3, then GG4.

GG1 — R1193: remove the dead corpus-pause clause from both reviewer
  instruction files, or replace it with one line: "expired 28 Oct, left
  expired by GC3". Fix the reference to the missing CLAUDE.md heading.

GG2 — One reviewer per judged commit, detected by git rather than by new
  apparatus:
  - The review branch is named from the judged sha:
    `review/<first 12 chars of the judged sha>`.
  - `git worktree add -b` fails if that branch exists locally, and the
    push fails if it exists on origin. Either failure means "a review of
    this commit already exists": the reviewer stops and reports it.
  - The implementer stops every reviewer agent after its handback,
    before invoking the next.
  Put this in docs/SUPERVISOR.md and the reviewer's agent file.

GG3 — CI concurrency: change the group to per-commit,
  `group: ${{ github.workflow }}-${{ github.sha }}`, and keep
  `cancel-in-progress: false`. Runs on different commits run in
  parallel, and no run is ever voided. GA2's push batching still
  applies.

GG4 — Park:
  - Push, confirm `git rev-list --all --not --remotes=origin --count`
    is 0, and confirm the tree is clean.
  - One-line digest entry: GG commit sha, R1 tag sha (unmoved).
  - Stop. Do not write R2's first report or any R2 plan until a
    directive opens R2.
  - Note for that report: it answers the newest verdict BY SHA
    (currently 63affd1) and carries verdicts 55 onward, per R1202.
