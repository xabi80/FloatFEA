# The directive record (FP0)

Every directive from Xabier is committed here **verbatim**, one file per directive, as the
**first commit of the turn that receives it** — a standalone `plan:` commit. Plans and
reports cite these files rather than paraphrasing them.

**Why this exists, and it is C25.** Directives were being implemented and cited as the
governing rule without their text existing anywhere in the repository. Measured at the
interim check on R1 step 1: `FO0`, `FO1` and `FO2` were cited as the governing rule in five
shipped files, and `grep -c "FO0\|FO1\|FO2\|FO3" docs/milestones/R1.md` was **0**. FM0 had
got a plan section, FN2 and FN3 had got `process:` commits, FO had got neither — and a
blocking finding's repair condition was "what FO0 actually requires", which no file said.

A rule cited by five files and recorded in none is a rule nobody can check a repair
against.

## Provenance, stated per file

Each file records where its text came from. **This is not uniform and the record says so:**

* `FM.md`, `FN.md`, `FO.md`, `FP.md`, `FQ.md`, `FR.md`, `FS.md`, `FT.md`, `FU.md`,
  `FV.md`, `FW.md`, `GB.md`, `GC.md` — **verbatim** from the directive message.
  (`GB.md` was listed twice here until GC's commit — R1152.)
* `GG.md` — **verbatim** from the directive message. Issued by Xabier, 2026-11-10.
  Its own file, as its `Record:` line asks. The R1 tidy-up, and **the last directive before
  R2 opens**: GG1 took the dead corpus-pause clause out of both reviewer instruction files
  and fixed the `CLAUDE.md` heading that no longer resolved (R1193), GG2 made the review
  branch name derive from the judged sha so that `git` itself refuses a second review of one
  commit, GG3 made the CI concurrency group per-commit, and GG4 parked the milestone.
  **GG1–GG3 are one `process:` commit, which GG asks for and SR-72 did not permit for GF3**
  — measured rather than assumed: no test reads the concurrency `group`, only
  `cancel-in-progress`, which GG3 keeps, so no `tests/` change was forced into a commit
  carrying the reviewer's instruction files.
* `GF.md` — **verbatim** from the directive message. Issued by Xabier, 2026-11-09.
  Its own file, as its `Record:` line asks. It is the directive that **closes R1**: GF1
  measured that `docs/milestones/R1.md` lists no step 5, GF2 supplied the base case for the
  CZ1 recursion and tagged `R1`, GF3 authorised one `process:` commit for five items
  (written as two, under SR-72), and GF4 asked for the final digest.
  **`FP.md` is NOT edited for GF3 (b)**, because that file's text is verbatim and GF3 asks
  for FP1's *rule* to cite GC2; the amendment is in `CLAUDE.md` § *The judged commit always
  has a CI run*, where FP1's operative text lives.
* `GE.md` — **verbatim** from the directive message. Issued by Xabier, 2026-11-08.
  Its own file, as its `Record:` line asks. The file also carries the one reading GE
  needed and did not state: GE says "revision 2" where revision 2 is already reviewed,
  so the work it names is done as **revision 3**, resolved under FZ rule 7 rather than
  escalated, because no published number differs between the two readings.
* `GD` — **verbatim, and it has no file of its own.** GD's own `Record:` line said to
  append it to `GC.md` rather than open a new file, so its text is at
  `GC.md:109-144` and `GC.md` says where it begins. R1164 was that this roll did not
  mention GD at all, so a reader looking for `GD.md` found neither a file nor a
  pointer; the rule itself was never missing, which is the difference between this
  and C25.
* `GA.md` — **verbatim, but REISSUED rather than received in its own turn.** GA was issued
  in the supervisor channel and never delivered to this session; its text reached the
  repository inside `GC.md` as GC0, and `GA.md` holds that text. Two consequences the
  record states rather than smooths over: **`GA6` has no text here**, because GC0 replaced
  it with GC5 and did not reproduce it; and GB1's reference to "my GA5" quotes a different
  sentence from GC0's GA5, which `GA.md` notes and does not reconcile.
* `GB.md` — verbatim. Its section headed "GA IS MISSING FROM THIS RECORD" was true when
  written and is **superseded by `GA.md`**; the section carries a pointer and its text is
  left standing rather than rewritten. GB cited `GA4` and `GA5` with GA recorded nowhere,
  which was C25 one directive letter after FP0 was adopted for C25.
* `FZ.md` — **verbatim** from the directive message. Issued by Xabier, 2026-10-31.
  **It also carries the running SR log**: FZ asks that every self-ruling taken under its
  standing rulings be recorded as `SR-<n>`, and SR-1 is the ruling that they all go in that
  one file rather than scattering across later directive files.
* `FY.md` — **verbatim** from the directive message. Issued by Xabier, 2026-10-31.
  Carries FY and FY5; FY5.1 supersedes FY1's heading range.
* `FX.md` — **verbatim, but the directive arrived as a SELECTION rather than as a message.** Issued by Xabier, 2026-10-30; **accepted at FY4.**
  Xabier was asked a question with three options and chose one; what is reproduced
  word-for-word is the question and all three options, including the two not taken, so a
  later reader can see what the ruling was chosen *against*. There is no free-text
  instruction to quote and the file says so rather than inventing one. **This is the first
  directive in this record with that provenance**, and it is distinguished here because
  "verbatim from the directive message" would be false of it.
* `FL.md` — **reconstructed from the session summary.** FL arrived before a context
  compaction, so the implementer no longer had the original message when the record was
  backfilled. The summary's rendering is faithful in substance and is not guaranteed
  word-for-word; the original is in the session transcript named in that file.

Earlier directives (through FK) are not backfilled here. They were implemented and are
recorded where they were adopted — `CLAUDE.md`'s own clauses quote most of them verbatim,
which is why the gap only became visible at FO.
