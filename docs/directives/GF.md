# Directive GF — close R1

**Provenance: verbatim from the directive message. Issued by Xabier, 2026-11-09.**
Recorded as the first commit of the turn that received it, per FP0. Its own file, as its
`Record:` line asks.

---

DIRECTIVE GF — close R1
Record: docs/directives/GF.md.

GF1 — Step 5. Check docs/milestones/R1.md §3.
  - If it lists no step 5: there is no step 5. R1's scope is complete.
    Go to GF2.
  - If it lists a step 5: state in one line what it contains and stop.
    Do not start it.

GF2 — Base case for the CZ1 recursion: the milestone's final verdict
  (55, PASS, nothing blocking) closes R1.
  - The eight `guards and meta-tests` ids are EG3 state (2), recorded by
    id in docs/closure/R1.md as the known boundary state at closure.
  - Verdict 55's ledger rows carry into R2's first report, and that
    report answers verdict 55.
  - Confirm in one line that docs/closure/R1.md holds the witness
    transcript(s) and fixture results per GE1.
  - Then tag: `git tag -a R1 <closure sha> -m "R1: tool ready"` and push
    the tag.

GF3 — One standalone `process:` commit, authorised here (not yours to
  decide, yours to write):
  a. FV2 commit door. The reviewer works on a named branch, not a
     detached HEAD:
       `git worktree add -b review/<step>-<n> <path> <judged sha>`
     It writes and commits the verdict there and pushes that branch. The
     implementer runs `git merge --ff-only origin/review/<step>-<n>`.
     The implementer makes no commits on the work branch while a review
     is open, so the fast-forward always applies. Put this in
     docs/SUPERVISOR.md and the reviewer's agent file.
  b. FP1 vs CK0 (SR-70): already ruled in GC2 (ancestor run, with the
     diff listing showing only paths-ignored files). Amend FP1's text to
     cite GC2. Close SR-70.
  c. CI concurrency: set `cancel-in-progress: false`, so a push never
     voids a run a reviewer is reading.
  d. Abbreviated sha: in SUPERVISOR.md and the agent file, always pass
     the full 40-char sha to `gh run list --commit`, because a short sha
     returns [].
  e. CLAUDE.md corpus-pause clause: state that it expired on 28 Oct and
     was left expired by GC3.

GF4 — Final digest, one screen:
  - R1 tag sha
  - closure record path
  - the GF3 commit
  - R2 ledger count
  Then stop and wait for R2 direction.
