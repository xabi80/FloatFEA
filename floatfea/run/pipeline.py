"""One configured run: build, solve, member forces, code check (FL1(b)).

This module is orchestration. Every number it reports comes from code that existed
before it -- `build_superstructure`, `compute_rows`, `check_member` -- and FL1(c)'s
"reproduces F4's envelope and F6's governing U EXACTLY" is a consequence of calling that
code rather than of agreeing with it.

**WHERE THE CONFIGURATION ACTUALLY REACHES, AND WHERE IT DOES NOT.** This is the honest
part and it is not symmetric. Four declared things reach the model today:

    sections D, t        -> `build_superstructure(measurement_sections=...)`
    mass fraction f      -> `build_superstructure(measurement_fraction=...)`
    E, Fy                -> `check_member(e=..., fy=...)`
    governing periods    -> `compute_rows(governing_periods=...)`

Two do not, and a run that declared them would otherwise report a number nobody asked
for, so they are CHECKED AND REFUSED rather than ignored:

    rho   the builder BACK-COMPUTES an equivalent density per body so that `rho * A` is
          the deck's own line mass whatever the section is. It is an OUTPUT. A declared
          value is compared against the nominal and reported, never injected.
    G     the builder's `Material` carries `nu`, fixed at 0.3, and derives G. A declared
          G that implies a different `nu` would be used by nothing, so it is refused.

And the stiffness and the code check must never disagree about the same constant: if a
configuration declared `E = 200e9`, `check_member` would use it while every element
stiffness used 210e9, and the utilisation would be computed for a structure that was not
the one solved. That is refused, by name, in `_check_material`.
"""

from __future__ import annotations

import json
import math
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final

import numpy as np
from numpy.typing import NDArray

from floatfea.checks.api_wsd import check_member
from floatfea.loads.period_band import CaseBand, classify_case
from floatfea.model.material import Section
from floatfea.model.platform import (
    _outer_diameter,
    admissible,
    build_superstructure,
)
from floatfea.post.forces_table import Row, compute_rows
from floatfea.run.config import (
    FROUDE_LAMBDA,
    HEADING,
    WAVE_HEIGHT,
    Bound,
    ConfigError,
    RunConfig,
    checked_recorded_periods,
    is_recorded_number,
    recorded_spelling,
)

__all__ = [
    "RunResult",
    "build_model",
    "exported_froude_lambda",
    "run",
    "validated_export_scale",
    "refuse_cases_that_cannot_govern",
    "refuse_disagreeing_period_records",
    "wave_basis_from_sidecar",
]

STATIONS_CHECKED = ("ROOT", "TIP")
"""FA3. The MID column waits on R730's discharge: its closed form is a measured 4.0%
approximation on bending, unverified against a refined mesh."""


@dataclass(frozen=True)
class MassReport:
    """What the distribution accounts for, against what the deck declares (FL1(a))."""

    body: str
    deck_mass: float
    member_mass: float
    remainder_mass: float
    residual: float
    fraction: float
    equivalent_density: float
    psd_admissible: bool


@dataclass(frozen=True)
class RunResult:
    """Everything one `floatfea run` produced, plus how long each stage took."""

    config: RunConfig
    built: Any
    rows: list[Row]
    utilisations: list[dict[str, Any]]
    mass: tuple[MassReport, ...]
    timings: dict[str, float]
    wave_bases: tuple[tuple[str, dict[str, Any]], ...] = ()
    """(file name, that file's basis) for EVERY declared file, in order (R817, FT2.6).

    The heading and wave height each dynamic-inputs file was exported at, carried on the
    result so every artifact can state them. They are the subjects of two caveats the
    artifacts already carried -- EX3/R724 on the heading, EZ2/FA0 on the height's
    associated-period band -- and before R817 neither value appeared in any of them.

    **THERE IS NO SINGULAR `wave_basis` BESIDE THIS, AND THAT IS R1093.** One existed: the
    FIRST file's, kept so that a one-file run reproduced byte for byte. `report.md` read
    it, so a two-file run published file one's heading and height under the heading "the
    wave basis these loads were exported at" while naming a DIFFERENT file as governing
    twenty lines below. The one-file guarantee is a property of this tuple having one
    entry, not of a second field holding the first entry.
    """

    notes: tuple[str, ...] = ()
    band_screens: tuple[tuple[str, tuple[CaseBand, ...]], ...] = ()
    """FL2(d): (file name, that file's screen) for EVERY declared file, in order.

    One inner entry per case in that file. A file's inner tuple is EMPTY when its export
    recorded no wave height, in which case there is no band for it and the report says
    the screen was not performed for that file rather than printing one computed from an
    assumed height.

    **GROUPED BY FILE, AND THAT IS R1094 AND R1095.** The screen is a function of the
    file's OWN recorded height, so a flat concatenation published two things that were
    not true of it: one stated band over a table of every file's cases, with `outside by`
    figures no reader could derive from the band printed above them; and -- the worse
    half -- a file recording NO height contributed nothing to a flat tuple, so beside any
    screened file the aggregate was non-empty, the "the screen was NOT performed"
    disclosure the single-file path owns was skipped, and the table read as complete while
    omitting the file that set the envelope. R1007 measured that same skip at 63% high on
    the governing utilisation. An unscreened file is an EMPTY ENTRY here rather than no
    entry, which is what lets the report name it.
    """

    section_properties: dict[str, tuple[float, float, float, float, float]] = field(
        default_factory=dict
    )

    def governing(self) -> dict[str, Any]:
        """The worst utilisation over every checked station, and where it is.

        **NOT AN AVERAGE AND NOT A MEAN (`CLAUDE.md`).** The single governing row is
        reported with its member, station, period and clause, because an outlier hidden
        in a summary statistic is the specific thing this reporting exists to catch.
        """
        if not self.utilisations:
            raise ValueError("no utilisations were computed; there is no governing row.")
        return max(self.utilisations, key=lambda r: float(r["utilisation"]))


def _sections_for(cfg: RunConfig, body_names: tuple[str, ...]) -> dict[str, Section]:
    """The declared tube per body, or a refusal naming what is missing.

    **A GROUP THE DECK HAS AND THE CONFIG DOES NOT IS REFUSED, NOT DEFAULTED.** A default
    here would silently size a member with the stand-in tube and report the result as
    the configured one.

    Each body's members are ONE group, so the group names ARE the body names, and that
    is why this function is small and separate.

    **A PER-MEMBER SECTION GROUP IS A DEVIATION FROM THE LOCKED PLAN'S (a), RECORDED
    RATHER THAN BUILT (R870).** What stood here was a future-tense sentence promising that
    FL2(a) would replace this with per-member group labels -- written before FL2(a) landed,
    left in place after it landed, and never true of what it shipped. The deviation and its
    reason are in `docs/milestones/R1.md` under FT2.7, and not restated here, because a
    scope decision recorded in two places goes stale in one of them.

    The retired sentence is PARAPHRASED and not quoted, deliberately: reproducing it would
    leave a line in the tree that any future census for the false claim still matches, and
    the repair would read as the defect.
    """
    declared = set(cfg.sections.groups)
    missing = sorted(set(body_names) - declared)
    if missing:
        raise ConfigError(
            f"sections.groups is missing {missing}. The deck declares bodies "
            f"{sorted(body_names)} and every one needs a section; a missing group would "
            f"otherwise be built with the stand-in tube and reported as configured."
        )
    extra = sorted(declared - set(body_names))
    if extra:
        raise ConfigError(
            f"sections.groups declares {extra}, which the deck does not have. The deck's "
            f"bodies are {sorted(body_names)}. A group that matches no member is a typo, "
            f"and silently ignoring it would leave a real group on the stand-in tube."
        )
    return {
        name: Section.circular_tube(spec.d_outer, spec.wall)
        for name, spec in cfg.sections.groups.items()
    }


def _fraction_for(cfg: RunConfig, body_names: tuple[str, ...]) -> float | None:
    """The one fraction the builder can take, or a refusal explaining why not.

    `build_superstructure` takes a SCALAR `measurement_fraction` applied to every body.
    The configuration is per body, because FL1(a) asks for it per body and because a
    final configuration may well want different splits. Until the builder can express
    that, a config declaring different fractions is REFUSED rather than silently run at
    one of them.
    """
    specs = [cfg.mass_distribution.get(name) for name in body_names]
    missing = sorted(name for name, spec in zip(body_names, specs, strict=True) if spec is None)
    if missing:
        raise ConfigError(
            f"mass_distribution is missing {missing}. Every body the deck declares needs "
            f"a distribution; there is no default split."
        )
    modes = {spec.mode for spec in specs if spec is not None}
    if modes != {"fraction"}:
        raise ConfigError(
            "mass_distribution: only the `f` (fraction) mode is wired to the builder in "
            "R1 step 1. An explicit line-mass and lumped-mass distribution is declared, "
            "validated and recorded by the schema, but nothing consumes it yet -- so a "
            "run would report masses it did not use. FL2 wires it; until then this is "
            "refused rather than half-applied."
        )
    # **ONE FRACTION FOR THE WHOLE MODEL, AND THE REFUSAL NO LONGER PROMISES OTHERWISE
    # (R870).** The message used to end by naming FL2(a) as the milestone that would give
    # the builder per-body fractions -- which FL2(a) did not do, so a user who read it was
    # told to wait for something that had already shipped without it. What it says now is
    # what they can act on. Per-body fractions are a deviation from the locked plan's (a)
    # recorded in `docs/milestones/R1.md` under FT2.7. Paraphrased, not quoted, for the
    # same reason as the docstring above.
    values = {spec.fraction for spec in specs if spec is not None}
    if len(values) != 1:
        raise ConfigError(
            f"mass_distribution declares different fractions per body "
            f"({sorted(v for v in values if v is not None)}). "
            f"`build_superstructure` applies ONE fraction to every body, so a per-body "
            f"split cannot be honoured today and running at one of them would report a "
            f"mass distribution the configuration did not ask for. Declare ONE "
            f"fraction, or the same fraction for every body."
        )
    return next(iter(values))


def _check_material(cfg: RunConfig, built: Any) -> tuple[str, ...]:
    """The declared material against the one the model actually uses, or a refusal.

    Returns the notes a report must carry about what was declared and not injected.
    """
    material = built.bodies[0].material
    declared = cfg.sections.material
    notes: list[str] = []

    if declared.e != float(material.E):
        raise ConfigError(
            f"sections.material.E = {declared.e!r} Pa, but every element stiffness in "
            f"this model is built at E = {float(material.E)!r} Pa, which "
            f"`floatfea.model.platform` fixes. `check_member` would use the declared "
            f"value while the solve used the built one, so the utilisation would describe "
            f"a structure that was never solved. Declare E = {float(material.E)!r}, or "
            f"changing the model's material is a reviewed change to the builder."
        )
    if declared.fy != float(material.fy):
        raise ConfigError(
            f"sections.material.Fy = {declared.fy!r} Pa, but the model's material carries "
            f"Fy = {float(material.fy)!r} Pa. The grade is assumed throughout (S355) and "
            f"both the screen and the model must use one value. Declare Fy = "
            f"{float(material.fy)!r}."
        )

    # G: the builder's material carries `nu` and DERIVES G, so a declared G that
    # disagrees reaches nothing. Compared EXACTLY, against G computed the way the model
    # computes it.
    #
    # **NO EPSILON, ON PURPOSE.** The first version of this compared the implied `nu`
    # with `math.isclose(..., abs_tol=5.0e-4)`, which is a comparison epsilon -- exactly
    # what `CLAUDE.md` means by "anything that functions as a tolerance under another
    # name", and it had no entry in `floatfea/tolerances.py` and no justification. There
    # is nothing to be approximate about here: both sides are declared constants, the
    # model's G is a pure function of two of them, and the refusal below prints the exact
    # value to declare. A configuration that writes `repr()` of that double round-trips
    # through YAML bit-for-bit, which is verified in the step report.
    model_g = float(material.E) / (2.0 * (1.0 + float(material.nu)))
    if declared.g != model_g:
        raise ConfigError(
            f"sections.material.G = {declared.g!r} Pa, and the model derives "
            f"G = E / (2 (1 + nu)) = {model_g!r} Pa from E = {float(material.E):g} Pa and "
            f"nu = {float(material.nu):g}, which `floatfea.model.platform` fixes. A "
            f"declared G that disagrees would be used by nothing while appearing in the "
            f"report as if it were. Declare G = {model_g!r}."
        )
    notes.append(
        f"G = {model_g!r} Pa is DERIVED by the model from E and nu = {float(material.nu):g}; "
        f"the declared value was checked for exact agreement, not injected."
    )

    # rho: an OUTPUT of the build, not an input. Reported against the declared nominal.
    equivalents = {b.name: float(b.equivalent_density) for b in built.bodies}
    notes.append(
        "rho was declared as {:g} kg/m^3 (nominal) and is BACK-COMPUTED per body so that "
        "rho * A is the deck's own line mass whatever the section is. Equivalent "
        "densities: {}.".format(
            declared.rho,
            ", ".join(f"{name} {value:.1f}" for name, value in sorted(equivalents.items())),
        )
    )
    above = sorted(name for name, value in equivalents.items() if value > declared.rho)
    if above:
        notes.append(
            "DZ5 / ER1(e): {} carry an equivalent density ABOVE the declared nominal, so "
            "the deck's mass does not fit inside the declared section at this fraction. "
            "This is a recorded finding about the configuration, not an error.".format(
                ", ".join(above)
            )
        )
    return tuple(notes)


def _refuse_inadmissible(cfg: RunConfig, built: Any) -> None:
    """Refuse a mass distribution that is not a structure (R810, FN1, corrected by FO0).

    **EXACTLY TWO CASES, AND NEITHER IS A THRESHOLD:**

    (a) `admissible(body)` is false -- DY0(d): `m_r >= 0` and no eigenvalue of `J_r` below
        `-tol`. A body whose remainder inertia is not PSD is not a body. The tolerance
        inside that predicate is `tolerances.py`'s, declared and justified there.

    (b) a body's equivalent density is EXACTLY `0.0`, which is `f = 0`: the members carry
        no mass at all. A frame whose members weigh nothing produces member forces that
        mean nothing, and the test is equality rather than a bound because zero is the
        only degenerate value.

    **WHAT THIS REPLACED, AND WHY IT WAS WRONG (R814).** The first version compared the
    COMPUTED `equivalent_density` against `DENSITY[1] = 100.0 kg/m^3` -- the bound declared
    in `config.py` for the DECLARED NOMINAL. Verdict 1 ruled that the config's ranges are
    not tolerances *precisely because no result is compared against one*, and this repair
    crossed that line: a range bound became a comparison on a computed quantity, which is a
    tolerance under another name with a local literal and no entry in `tolerances.py`.

    Three measurements say how bad it was. At `f = 0.0106` the equivalent density is
    `100.9963`, so the guard ACCEPTED it and the run published `U = 2.15615` unlabelled
    while the platform's members carried `26500 kg` of a `2.5e+06 kg` body. **Nothing held
    the threshold**: patching `100` to `1e-300` -- 302 decades -- left every counter-case
    and its control green, because the only case pinned was `f = 0.0`, where the density is
    exactly zero. And the refusal's own sentence was false of a value it refused: `f = 0.0`
    is `MASS_FRACTION_LADDER`'s LAST RUNG with `admissible()` true on all five bodies, so
    the shipped builder reaches it by construction.

    **SMALL `f` IS A LEGITIMATE INPUT (FO0).** `f = 0.0106` runs normally now and its mass
    table shows the split, which is the honest output: the configuration is unusual and the
    report says what it is rather than a guard deciding it is inadmissible on a number
    nobody justified.

    **AND THE NON-MONOTONICITY IS WHY (a) IS ASKED PER BODY.** The platform is `PSD = False`
    at `f = 0.999999` and `True` again at `f = 1.0`, so no interval of `f` describes the
    admissible set. The question is asked of each built body, every time.
    """
    bad_psd = [b.name for b in built.bodies if not admissible(b)]
    massless = [b.name for b in built.bodies if float(b.equivalent_density) == 0.0]
    if not bad_psd and not massless:
        return

    trouble: list[str] = []
    if bad_psd:
        trouble.append(
            f"the remainder inertia is not PSD on {bad_psd} (DY0(d): m_r >= 0 and no "
            f"eigenvalue of J_r below -tol), so those bodies are not bodies"
        )
    if massless:
        trouble.append(
            f"the members carry no mass at all on {massless} (equivalent density exactly "
            f"0.0, which is f = 0), so their member forces would mean nothing"
        )

    if not cfg.study_only:
        # THE MESSAGE IS TRUE OF EVERY VALUE IT REFUSES (FO0). It used to open "this mass
        # distribution is one the shipped builder would never have reached", which is
        # false of `f = 0`: that is the ladder's last rung and `admissible()` holds on all
        # five bodies there. A refusal that misdescribes its own cause teaches the reader
        # the wrong thing about their configuration.
        raise ConfigError(
            "this mass distribution is not a structure: "
            + "; and ".join(trouble)
            + ". Set `study_only: true` to run it anyway -- every output will then carry "
            "`STUDY -- NOT FOR DESIGN` -- or declare a distribution whose bodies are "
            "admissible and whose members have mass."
        )


def build_model(cfg: RunConfig) -> Any:
    """The superstructure this configuration describes, or a refusal.

    Built ONCE here and handed to every stage, so the forces, the code check and any
    report are all talking about the same model.
    """
    probe = build_superstructure(path=cfg.floatsim.deck, froude_lambda=cfg.floatsim.froude_lambda)
    body_names = tuple(b.name for b in probe.bodies)

    sections = _sections_for(cfg, body_names)
    fraction = _fraction_for(cfg, body_names)

    # FL2(a): the declared topology, or the star when `topology` is absent. The PROBE
    # above is built with the default star deliberately -- it exists only to read the
    # deck's body NAMES for `_sections_for` and `_fraction_for`, and those are a fact
    # about the deck rather than about which members join its nodes.
    return build_superstructure(
        path=cfg.floatsim.deck,
        froude_lambda=cfg.floatsim.froude_lambda,
        measurement_fraction=fraction,
        measurement_sections=sections,
        platform_members=cfg.topology.members,
    )


def _mass_report(built: Any) -> tuple[MassReport, ...]:
    """Per body: what the split accounts for against the deck's own total.

    **THE RESIDUAL IS FORMED FROM ITS OWN TERMS (G4.1).** `deck - member - remainder`,
    not by subtracting two large numbers and reporting the difference as a small one.
    Per body, never summed or averaged -- a body that is 10 t out and another that is
    10 t the other way would cancel in a total.
    """
    out: list[MassReport] = []
    for body in built.bodies:
        deck = float(body.deck_mass)
        member = float(body.member_mass)
        remainder = float(body.remainder_mass)
        out.append(
            MassReport(
                body=body.name,
                deck_mass=deck,
                member_mass=member,
                remainder_mass=remainder,
                residual=deck - member - remainder,
                fraction=float(body.mass_fraction),
                equivalent_density=float(body.equivalent_density),
                psd_admissible=bool(admissible(body)),
            )
        )
    return tuple(out)


def _section_properties(section: Any) -> tuple[float, float, float, float, float]:
    """`(A, W, W_t, D, t)`, all derived from the section itself (AS1).

    `t` is recovered from `A` and `D` rather than carried, because `Section` does not
    store it -- the same route `scripts/measure/api_wsd_utilisation.py` takes.
    """
    d_outer = _outer_diameter(section)
    area = float(section.A)
    wall = 0.5 * (d_outer - math.sqrt(d_outer * d_outer - 4.0 * area / math.pi))
    return (
        area,
        2.0 * float(section.I_y) / d_outer,
        2.0 * float(section.J) / d_outer,
        d_outer,
        wall,
    )


def _k_l_over_r(body: Any, k: float) -> float:
    """`K L / r` for a body's arms, with `r` and `L` read from the built model."""
    section = body.members[0].section
    r = math.sqrt(float(section.I_y) / float(section.A))
    return k * float(body.members[0].length) / r


def _utilisations(cfg: RunConfig, built: Any, rows: list[Row]) -> list[dict[str, Any]]:
    """The API RP 2A-WSD screen on the per-instant rows (R740).

    Reads `total_instant` only: `total_max` / `total_min` max each component
    INDEPENDENTLY over the window, so their six values do not occur together and a
    utilisation from them is an upper bound, not a stress at any instant.
    """
    if cfg.code_check.one_third_increase:
        raise ConfigError(
            "code_check.one_third_increase is true, and section 3.1.2's increase is NOT "
            "implemented in floatfea/checks/api_wsd.py -- EZ4 Q2 locked it off, because "
            "the increase is written for a declared extreme environmental event and these "
            "are screening design waves with no return period. Accepting the flag and "
            "ignoring it would report allowables a third lower than the configuration "
            "asked for. Set it false, or reopen EZ4 Q2."
        )

    by_name = {b.name: b for b in built.bodies}
    governing = set(cfg.load_cases.governing_periods)
    out: list[dict[str, Any]] = []

    for row in rows:
        if row.station not in STATIONS_CHECKED or row.basis != "total_instant":
            continue
        if row.period_full_s not in governing:
            continue
        body = by_name[row.body]
        member = next(m for m in body.members if m.label == row.member)
        area, w_bend, w_tors, d_outer, wall = _section_properties(member.section)
        values = row.values
        common = dict(
            axial_n=float(values[0]),
            shear_y_n=float(values[1]),
            shear_z_n=float(values[2]),
            torsion_nm=float(values[3]),
            moment_y_nm=float(values[4]),
            moment_z_nm=float(values[5]),
            area_m2=area,
            section_modulus_m3=w_bend,
            torsional_modulus_m3=w_tors,
            d_outer_m=d_outer,
            wall_m=wall,
            fy=cfg.sections.material.fy,
            e=cfg.sections.material.e,
        )
        locked = check_member(
            k_l_over_r=_k_l_over_r(body, cfg.code_check.k), cm=cfg.code_check.cm, **common
        )
        record: dict[str, Any] = {
            "body": row.body,
            "member": row.member,
            "station": row.station,
            "period_full_s": row.period_full_s,
            "basis": row.basis,
            # **FROM THE ROW, NOT LOOKED UP LATER (FT2.6, FW1).** My first attempt had
            # the report find the governing row by matching its five identifying fields,
            # and with several files those five do NOT identify a row -- both files
            # produce the same (body, member, station, period, basis) -- so the match
            # returned the FIRST file and the report named it beside the SECOND file's
            # number. That is `npz_files[0]` reintroduced one layer up, which is why FW1
            # put the provenance on `Row`: carried, it cannot be mismatched.
            "source": row.source,
            "heading_deg": row.heading_deg,
            "f_a_MPa": locked.f_a / 1e6,
            "F_a_MPa": locked.allow_axial / 1e6,
            "f_b_MPa": locked.f_b / 1e6,
            "F_b_MPa": locked.allow_bending / 1e6,
            "f_v_MPa": locked.f_v / 1e6,
            "f_vt_MPa": locked.f_vt / 1e6,
            "axial_branch": locked.axial_branch,
            "bending_branch": locked.bending_branch,
            "interaction_form": locked.interaction_form,
            "u_axial": locked.u_axial,
            "u_bending": locked.u_bending,
            "u_shear": locked.u_shear,
            "u_torsion": locked.u_torsion,
            "u_combined": locked.u_combined,
            "utilisation": locked.utilisation,
            "governing_clause": locked.governing,
        }
        # The sensitivities, each ONE VARIABLE MOVED from the locked case (BG0).
        if cfg.code_check.k_sensitivity is not None:
            record["utilisation_K_sens"] = check_member(
                k_l_over_r=_k_l_over_r(body, cfg.code_check.k_sensitivity),
                cm=cfg.code_check.cm,
                **common,
            ).utilisation
        if cfg.code_check.cm_sensitivity is not None:
            record["utilisation_Cm_sens"] = check_member(
                k_l_over_r=_k_l_over_r(body, cfg.code_check.k),
                cm=cfg.code_check.cm_sensitivity,
                **common,
            ).utilisation
        out.append(record)

    if not out:
        raise ConfigError(
            f"no checked station fell on a governing period. The configuration's "
            f"governing_periods are {sorted(governing)} and the computed rows carry "
            f"{sorted({r.period_full_s for r in rows if r.basis == 'total_instant'})}. "
            f"A screen over nothing would otherwise report no utilisation at all."
        )
    return out


def _ratio(a: float, b: float) -> float:
    """The discrepancy between two scales as a factor >= 1, direction stated separately.

    EH4: a boundary is solved in both directions. `a / b` alone reports `0.125x on force`
    when the declared scale is the smaller one, which is arithmetically right and the
    reciprocal of what the reader is trying to find out -- how big the error would have
    been.
    """
    return max(a, b) / min(a, b)


def uncovered_headings(
    declared: tuple[float, ...], covered: tuple[float, ...]
) -> tuple[float, ...]:
    """The declared headings the BEM dataset does not cover, in declaration order (FL2(c)).

    FL(c): "`export` refuses a heading the BEM database does not cover, naming what is
    missing." This is the naming half, and it is a pure function of two sets.

    **THE COVERED SET IS PASSED IN, AND THAT IS NOT AN ACCIDENT OF THE SIGNATURE.** Which
    headings the BEM dataset carries is a fact about the PINNED HSP STATE, not about
    FloatFEA: the datasets and `readers/capytaine.py` live in HSP (docs/hsp-coupling.md),
    this repository contains none of them, and the committed dynamic-inputs npz records a
    single heading in its sidecar rather than a coverage list. A hard-coded list of
    covered headings here would be FloatFEA asserting a fact it cannot check -- the same
    error as inventing a load distribution, one level up.

    So `export` reads the set from the dataset it opens and calls this; the refusal is
    tested against a set the test supplies.

    An EXACT comparison, because a heading is a declared input and not a measurement. A
    run that asked for 45 deg and silently got 44.9 would publish an envelope for a sea
    state nobody declared, so "near enough" is the wrong question and there is no
    tolerance here to choose.
    """
    # **360 AND 0 ARE THE SAME WAVE DIRECTION, AND EXACT EQUALITY SAID OTHERWISE (R872).**
    # `docs/conventions.md` defines `heading_deg` as a direction of travel measured from
    # +X, so the quantity is an ANGLE and `360` names the direction `0` names. `HEADING`'s
    # declared domain is inclusive at both ends, `(0.0, 360.0)`, so `headings: [360.0]`
    # is a legal declaration -- and against an export at `0` it was refused.
    #
    # Measured through the real CLI before this: `EXIT=2`, no directory created, for a
    # configuration asking for the heading the file actually carries.
    #
    # **THIS IS ARITHMETIC AND NOT SLACK, WHICH IS WHY THERE IS NO TOLERANCE HERE.** The
    # question is whether two names denote one direction, not whether two directions are
    # close enough. `h % 360.0` is exact for every value in the declared domain: `360.0
    # % 360.0` is `0.0` and `45.0 % 360.0` is `45.0`, with no rounding introduced. A
    # near-miss is still refused -- `44.9 % 360.0` is `44.9` -- so the comparison stays
    # the exact one `refuse_uncovered_headings` documents.
    #
    # The direction of the previous round's conclusion is worth keeping: exact equality
    # OVER-refuses and cannot under-refuse, so this was safe and wrong rather than
    # dangerous and wrong.
    have = {c % 360.0 for c in covered}
    return tuple(h for h in declared if h % 360.0 not in have)


def _recorded_heading(basis: dict[str, Any]) -> float | None:
    """The export's own heading as a number, `None` if absent, or a refusal (R873, R874).

    **THE DECLARED SIDE REFUSES A BOOL BY NAME IN ELEVEN PLACES AND THE RECORDED SIDE
    COERCED ONE.** `{"heading_deg": True}` against a declared `[1.0]` was ACCEPTED,
    because `float(True)` is `1.0` -- so a run published `heading True deg` and the one
    check that compares declared against covered agreed with it. That is the R834/R837
    family on the other side of the same comparison, and this repository refuses
    `isinstance(x, bool)` for every declared number precisely because YAML reads `yes`
    and `on` as `True`.

    **AND A NON-SCALAR MADE THE CHECK ABSTAIN RATHER THAN REFUSE (R873).** A sidecar
    whose `heading_deg` is a LIST -- which is what FL(c)'s mechanism half would write if
    a multi-heading export recorded its set -- raised `TypeError` inside `float()`, so
    the check crashed out of the one comparison it exists to make. Refused by name
    instead, and the message says what the shape means, because a list here is a
    multi-heading file meeting a single-heading reader.
    """
    # A READ, NOT A CHECK (R877). `exported_wave_basis` validates every field at the
    # single reader, so this cannot be the only place a bad value is caught -- which is
    # exactly what it was when the check lived here and the shipped example, declaring no
    # `headings`, returned before reaching it.
    recorded = basis.get("heading_deg")
    if recorded is None:
        return None
    if isinstance(recorded, bool) or not isinstance(recorded, (int, float)):
        raise ConfigError(
            f"the dynamic-inputs file's recorded `heading_deg` is {recorded!r} "
            f"({type(recorded).__name__}), which is not a single heading in degrees. A "
            f"LIST here is a multi-heading export meeting a reader that compares one "
            f"heading, and a boolean is what YAML makes of `yes`, `on` or `true` -- "
            f"neither can be compared against a declared heading, and coercing either "
            f"would publish an envelope attributed to a direction nobody exported. Fix "
            f"the sidecar beside the npz: this value is refused at the READER whether or "
            f"not any heading is declared (R877), so there is no configuration under "
            f"which the run proceeds with it."
        )
    return float(recorded)


def refuse_headings_no_file_covers(
    declared: tuple[float, ...], bases: list[tuple[Path, dict[str, Any]]]
) -> None:
    """A declared heading that NO declared file covers is refused (FT2.6, R809's rule).

    **THE SINGLE-FILE RULE IS UNCHANGED AND IS NOT RELAXED TO ADMIT A SECOND FILE.** The
    old call asked `refuse_headings_this_run_cannot_cover` whether ONE basis covered the
    declared set. With several files the question is whether the UNION does, and the way
    to get that wrong is to ask the first file and trust the rest -- which is the
    `npz_files[0]` defect. So each declared heading is matched against every file's
    recorded heading, and only a heading no file records is refused.

    The refusal names which headings ARE covered and by which file, because "declared 45
    and nothing covers it" is not actionable without knowing what the files do carry.
    """
    if not declared:
        return
    # **ONE FILE DELEGATES, AND THAT IS NOT A SHORTCUT -- IT IS THE GUARANTEE.** EH4's
    # one-file boundary asks that a one-tuple reproduce today's behaviour exactly; handing
    # straight to the single-basis function makes that true by construction rather than by
    # a second implementation that happens to agree. It also keeps that function on a
    # PRODUCTION path: a rename that left it called from nowhere would be R866/R877's own
    # shape, a correct and well-tested function nothing reaches.
    if len(bases) == 1:
        refuse_headings_this_run_cannot_cover(declared, bases[0][1])
        return
    covered: dict[float, str] = {}
    unrecorded: list[str] = []
    for path, basis in bases:
        recorded = _recorded_heading(basis)
        if recorded is None:
            unrecorded.append(path.name)
            continue
        covered.setdefault(recorded, path.name)
    # **ONE RULE FOR BOTH PATHS, WHICH IS R1100.** This asked its own question with a
    # plain `==` while the single-file path asks `uncovered_headings`, which is modulo
    # 360 -- so `headings: [360.0]` against an export at 0 was ACCEPTED at one file and
    # REFUSED at two, with the number of declared files the only variable. 360 is inside
    # `HEADING`'s declared domain and names the direction 0 names, so the modulo is the
    # correct rule and the duplicate was the defect: two checks of one question is the
    # shape where one of them quietly stops being the one that runs. No epsilon enters
    # with it -- `uncovered_headings` is exact, and its own comment says why.
    missing = list(uncovered_headings(declared, tuple(covered)))
    if not missing:
        return
    if not covered:
        raise ConfigError(
            f"load_cases.headings declares {list(declared)} deg and NO declared "
            f"dynamic-inputs file records a heading at all "
            f"({', '.join(unrecorded) or 'none listed'}). A declared heading with no file "
            f"behind it is refused, not assumed to be heading 0: the envelope would be "
            f"taken over whatever was exported while the configuration claimed the "
            f"declared set. Export a file per heading, or drop the declaration."
        )
    have = ", ".join(f"{h:g} deg ({name})" for h, name in sorted(covered.items()))
    # **BOTH BRANCHES OF THE AGREEMENT PAIR (R1101).** One file is `records`, several are
    # `record`; the fourth instance of this class in this step (L36, R1085, R1089).
    verb = "records" if len(unrecorded) == 1 else "record"
    extra = (
        f" {', '.join(unrecorded)} {verb} no heading at all and cover nothing."
        if unrecorded
        else ""
    )
    raise ConfigError(
        f"load_cases.headings declares {list(declared)} deg and no declared "
        f"dynamic-inputs file covers {missing} deg. The declared files carry: "
        f"{have}.{extra} A declared heading with no file behind it would leave the "
        f"envelope short of what the configuration claims, so it is refused before "
        f"anything is built or written (R809)."
    )


def refuse_scale_disagreement(cfg: Any, npz: Path) -> None:
    """ONE SOURCE FOR THE SCALE (R805, FN0), asked of EVERY declared file.

    **NOT `validated_export_scale`, WHICH ALREADY EXISTS AND DOES A DIFFERENT JOB.**
    That one resolves the scale a PUBLISHER may use and returns it, and R919's gate
    holds every publishing path to it. This one asks whether a file's recorded scale
    AGREES WITH THE CONFIGURATION and refuses if not. My first version of this helper
    took the other name and `mypy` caught the redefinition; two checks sharing one
    name is how one of them silently stops being called.

    The configuration's lambda reaches the deck build, every Froude conversion and the
    provenance -- and a dynamic-inputs file exported at a DIFFERENT scale cannot be mixed
    with it, because the joint reactions in that file are already scaled. Refused, naming
    both, rather than silently applying one scale to the geometry and another to the loads.

    **PER FILE, AND THIS IS THE HAZARD OF THE WHOLE OF FT2.6.** Two files at different
    scales would mix forces at `lambda^3` with a locked moment at `lambda^4` against one
    deck. Asking only the first file is the shape that would do it, so every file is
    asked and the message names WHICH file disagreed.
    """
    exported, where = exported_froude_lambda(npz)
    if exported is None:
        raise ConfigError(
            f"{npz.name}: {where}, so there is no way to know what scale "
            f"its joint reactions are at. The configuration declares "
            f"floatsim.froude_lambda = {cfg.floatsim.froude_lambda!r}. Re-export the file "
            f"-- `floatfea export` records the scale from FN0 onward -- rather than "
            f"assuming it matches, which is exactly the defect FN0 closed."
        )
    if exported != cfg.floatsim.froude_lambda:
        raise ConfigError(
            f"scale mismatch. floatsim.froude_lambda = {cfg.floatsim.froude_lambda!r} in "
            f"{cfg.source.name}, and {npz.name} was exported at "
            f"{exported!r} according to {where}. The deck would be built at one scale "
            f"while the joint reactions in that file carry another: the yaw-locked "
            f"composite goes as lambda^3 on force and lambda^4 on the locked moment. The "
            f"declared scale is "
            f"{'larger' if cfg.floatsim.froude_lambda > exported else 'smaller'} by a "
            f"factor of {_ratio(cfg.floatsim.froude_lambda, exported):g}, which is "
            f"{_ratio(cfg.floatsim.froude_lambda, exported) ** 3:g}x on every force and "
            f"{_ratio(cfg.floatsim.froude_lambda, exported) ** 4:g}x on the locked "
            f"moment. Declare the file's own scale, or export a file at this one."
        )


def _band_screen_over_files(
    cfg: Any, per_file: list[tuple[Path, Any, tuple[float, ...], Any]]
) -> tuple[tuple[str, tuple[CaseBand, ...]], ...]:
    """FL2(d)'s screen, per file, KEYED BY FILE rather than concatenated (FT2.6, R1094).

    The screen is a function of the file's own recorded HEIGHT, so one file's basis cannot
    answer for another's. `refuse_cases_that_cannot_govern` refuses on the spot, so a run
    that reaches the end of this loop has every file's cases screened and no file's screen
    standing in for another's.

    **EVERY DECLARED FILE GETS AN ENTRY, INCLUDING ONE THAT WAS NOT SCREENED (R1095).** A
    file with no recorded height screens to `()`, and the first version of this helper
    concatenated, so such a file simply vanished from the result -- which made the
    "not performed" disclosure a property of whether ANY file had a height. Keyed, a file
    that was not screened is an empty entry and the report can name it.
    """
    return tuple(
        (npz.name, refuse_cases_that_cannot_govern(cfg, periods_one, basis_one))
        for npz, _raw, periods_one, basis_one in per_file
    )


@dataclass(frozen=True)
class _ComputedAll:
    """The concatenated rows of every declared file. `compute_rows`' shape, one field."""

    rows: list[Row]


def refuse_headings_this_run_cannot_cover(
    declared: tuple[float, ...], basis: dict[str, Any]
) -> None:
    """A declared heading this run does not cover is refused BEFORE any output (R866).

    **THE DEFECT THIS CLOSES WAS MINE AND IT WAS EXACTLY THE SHAPE R809 ALREADY REFUSES
    TWELVE LINES ABOVE ITS CALL SITE.** `load_cases.headings` was parsed, range-checked
    and repeat-checked, and then read by nothing. Measured through the real CLI on the
    shipped example with `headings: [0.0, 45.0, 90.0]` and nothing else changed:

        EXIT=0   wrote member_forces.csv (1248 rows) / utilisation.csv (32) / report.md
        governing U = 1.71167 at platform:hub4_arm ROOT
        report.md  * **heading** -- 0.0 deg

    So `utilisation.csv` and `report.md` shipped as the output of a configuration
    declaring three headings, with `U = 1.71167` presented as THE governing utilisation,
    when it is the envelope over heading 0 alone. The EX3/R724 caveat is true of the run
    and false of the configuration, and nothing named the two headings that never
    happened. Under FR1 that is an input accepted and used other than as declared.

    **THE FACT NEEDED TO CHECK IT IS LOCAL.** `exported_wave_basis` already reads the
    heading the npz was exported at, with no HSP worktree -- which is why this is not the
    multi-heading envelope FL(c) also asks for, and why it did not have to wait for the
    export path. A declared set this run cannot cover is refused; it is not reconciled,
    narrowed, or noted in a caveat.

    A sidecar-less npz records no heading at all, and a declared set against it is refused
    for the same reason rather than assumed to be heading 0 -- FL1(a) admits such a file,
    and `_header_lines` already says "NOT RECORDED by the export" when it arrives.
    """
    if not declared:
        return
    recorded = _recorded_heading(basis)
    if recorded is None:
        raise ConfigError(
            f"load_cases.headings declares {list(declared)} deg and this run's "
            f"dynamic-inputs file records NO heading, so nothing here can show that any "
            f"of them was covered. Remove the declaration to run at whatever the export "
            f"used -- the artifacts state that it is not recorded -- or point "
            f"`load_cases.npz` at a file whose export recorded its heading. Refused "
            f"before any output is written, so nothing on disk describes a run that did "
            f"not happen."
        )
    covered = (recorded,)
    missing = uncovered_headings(declared, covered)
    if not missing:
        return
    raise ConfigError(
        f"load_cases.headings declares {list(declared)} deg and this run covers "
        f"{covered[0]} deg -- the one heading its dynamic-inputs file was exported at. "
        f"{list(missing)} deg would never be computed, and the governing utilisation "
        f"would be published as THE envelope while being the envelope over "
        f"{covered[0]} deg alone. An envelope over several headings needs a "
        f"multi-heading npz, which `floatfea export` produces; `floatfea run` does not "
        f"invent the loads for a heading it was not given. Refused before any output is "
        f"written, so nothing on disk describes a run that did not happen."
    )


def refuse_uncovered_headings(declared: tuple[float, ...], covered: tuple[float, ...]) -> None:
    """Raise naming every declared heading the dataset does not carry (FL2(c))."""
    missing = uncovered_headings(declared, covered)
    if not missing:
        return
    raise ConfigError(
        f"load_cases.headings asks for {list(missing)} deg, which the BEM dataset does "
        f"not cover. It carries {sorted(covered)} deg. Every missing heading is named "
        f"above rather than the first one, because a reader fixing a configuration needs "
        f"the whole list; and the comparison is exact, because a heading is a declared "
        f"input -- exporting 44.9 deg for a declared 45 would publish an envelope for a "
        f"sea state nobody asked for."
    )


WAVE_BASIS_KEYS: Final[tuple[str, ...]] = (
    "heading_deg",
    "wave_height_full_m",
    "wave_height_model_m",
    "lambda",
    "window",
)
"""The five fields a recorded wave basis carries, and every published artifact states.

**`lambda` JOINED THEM AS R903.** It was read raw by
`scripts/measure/f6_results_report.py` and published in the SAME PRINTED SENTENCE as the
two heights this module validates -- so `Froude lambda = fifty`, `= -50.0`, `= True` and
`= 1e9` each reached a deliverable at exit 0. It is also the one recorded field whose
configured counterpart genuinely exists (`FROUDE_LAMBDA`, `config.py:196`, applied by
`_checked` at `:733`), which is what made `RECORDED_BOUNDS`' original justification true
of the one key that was not in it.

A height is meaningless without the scale it was measured at, so the scale belongs to the
basis rather than beside it.
"""

RECORDED_PROVENANCE_NUMERIC: Final[tuple[str, ...]] = ("rho_inf", "dt", "ramp_s")
"""Recorded numbers the generator PUBLISHES but no computation here consumes (R903).

They get a type check and a finiteness check and **deliberately no range**. There is no
declared counterpart for any of them in `config.py`, and inventing one would repeat
exactly the error R895 found in `RECORDED_BOUNDS` -- a bound presented as its configured
quantity's when no such quantity exists. A type check is what stops
`rho_inf = True` or `dt = "fast"` being printed into a deliverable, and that is the whole
claim being made here.

Checked only when present, because unlike the wave basis these are not a
complete-or-empty set: a sidecar from an export that records no integrator settings is
not a partial record of them.
"""

RECORDED_BOUNDS: Final[dict[str, Bound]] = {
    "heading_deg": HEADING,
    "wave_height_full_m": WAVE_HEIGHT,
    "wave_height_model_m": WAVE_HEIGHT,
    "lambda": FROUDE_LAMBDA,
}
"""The declared domain each RECORDED numeric field is checked against (R881, R895).

**THIS ENTRY'S FIRST JUSTIFICATION WAS FALSE FOR ONE OF ITS THREE KEYS (R895).** It said
each recorded value is checked against "the same bound its CONFIGURED counterpart gets in
`config.py`". That holds for `heading_deg` (`load_cases.headings`, and each case's
`heading`) and for `wave_height_full_m` (each case's `H`, which `WaveCase` documents as
"Full scale, SI"). It is false for `wave_height_model_m`, which **has no configured
counterpart at all** -- no declaration anywhere expresses a model-scale wave height.

So `WAVE_HEIGHT` is a FULL-scale domain, and applying it unchanged to the model-scale
field is a bound that is correct at the configuration R881 chose and loose by exactly
`froude_lambda` at the other: at `lambda = 50` the declared model headroom is `207x`
where the legal headroom is `4.1x`, and `FROUDE_LAMBDA` admits `lambda` up to `1000`.

**IT IS STILL A CEILING AND IT IS STILL NOT THE CHECK THIS PAIR NEEDS.** A ceiling on one
member cannot police a relation between two: a legal model value beside a wrong full value
passes, and so does a pair that is individually legal and jointly off by `3.9x`. The
relation (`full = model * lambda`, which the export writes) is tracked as R895 and is NOT
closed by this mapping. What this mapping does close is R881 -- a NEGATIVE height, or one
outside every admissible scale, reaching a published artifact.

`window` is absent because it is not a number; it keeps its own `isinstance` check below.
"""


def _recorded_height(basis: dict[str, Any]) -> float | None:
    """The export's own full-scale wave height, or `None` when none was recorded.

    **NO TYPE CHECK HERE, DELIBERATELY, AND R994 IS WHY.** `_validated_wave_basis` is
    the single door (R896): it refuses a partial basis, refuses a bool or a non-number
    by name, refuses a non-finite value, and range-checks against `WAVE_HEIGHT` -- all
    at the reader, so the guarantee does not depend on what the configuration declared
    (R877). A second type check on the same field here could not fire, and a refusal
    that cannot fire is dead code dressed as rigour. I shipped exactly that once in this
    step and the reviewer was right to name it.

    **R1011: `_recorded_heading` CARRIES SUCH A GUARD AND THE REASON THIS DOCSTRING GAVE
    FOR THE ASYMMETRY WAS FALSE.** It said that function "is reached by
    `refuse_headings_this_run_cannot_cover`, which the CLI calls with a basis it did not
    get from this module's door". Measured: that function has exactly ONE production call
    site, `run()` in this same module, and the basis it is handed is
    `exported_wave_basis(cfg.load_cases.npz)` -- this module's door. So the stated reason
    inverted the conclusion drawn from it: on the true graph `_recorded_heading`'s guard is
    the one that cannot fire in production, which is what the paragraph above calls dead
    code dressed as rigour.

    It is kept rather than deleted, and the reason is a property of the CALLER and not of
    the guard: `refuse_headings_this_run_cannot_cover` and `_recorded_heading` are reached
    directly by `tests/unit/test_headings_and_bem_coverage.py` with dicts no door has
    seen, so the guard is the contract those cells are written against. The honest
    statement is that it is a contract on a public helper and not a production refusal.
    What it must not claim is that production reaches it, which is what this paragraph
    claimed.
    """
    recorded = basis.get("wave_height_full_m")
    return None if recorded is None else float(recorded)


def refuse_cases_that_cannot_govern(
    cfg: Any, periods: tuple[float, ...], basis: dict[str, Any]
) -> tuple[CaseBand, ...]:
    """FL2(d): the band check, per case, and the refusal of a set that cannot govern.

    Returns the screen for EVERY case in the file -- that is the "and reported" half --
    and refuses before the solve when a DECLARED governing period is inadmissible at the
    recorded height and the configuration has not said otherwise.

    **THE CAVEAT WAS ALREADY PUBLISHED AND NOTHING ENFORCED IT.** `floatfea/cli.py`'s
    `EZ2` caveat has shipped on every artifact since F4 -- in the wording it carried THEN,
    which R1103 has since made plural: "only the declared governing
    periods may set the envelope. Cases outside the associated-period range for this
    wave height -- and any exceeding the deep-water breaking steepness -- are reported
    as SENSITIVITY ONLY and cannot govern" -- while no code checked that the declared
    set was inside the range. One variable moved on the shipped example, the breaking
    wave added to `governing_periods` and everything else held:

        governing_periods: [12.5, 14, 15, 16.2]        EXIT=0   U = 1.71167
        governing_periods: [10, 12.5, 14, 15, 16.2]    EXIT=0   U = 2.78942

    `T = 10 s` at `H = 24.2 m` has `H/lambda = 0.155`, above `1/7`. It set the governing
    utilisation 63% high at exit 0, in a `utilisation.csv` carrying the caveat that
    denied it could. Under FR1 that is a wrong number in a published deliverable.

    **WHAT HAPPENS WITH NO RECORDED HEIGHT, STATED RATHER THAN ASSUMED.** The band is a
    function of the wave height, which lives in the npz's provenance sidecar. FL1(a)
    admits an npz with no sidecar, and for such a file there is no height and therefore
    no band -- so the check cannot be performed and this returns an empty screen. It
    does NOT fall back to an assumed height: `CLAUDE.md` forbids inventing a
    distribution, and a band computed from a guessed height is the R902 defect exactly
    (a module constant decided a band while the header printed a recorded value). The
    artifacts already say "wave basis: NOT RECORDED by the export" in that case, and the
    report's band section says the screen was not performed and why -- **naming the file,
    since R1095, because beside a file that WAS screened an empty screen used to vanish
    into a concatenation and the disclosure with it.**
    """
    height = _recorded_height(basis)
    if height is None:
        return ()
    screen = tuple(classify_case(T, height) for T in sorted(periods))

    by_period = {case.period_full_s: case for case in screen}
    declared = set(cfg.load_cases.governing_periods)
    override = set(cfg.load_cases.out_of_band_governing)

    # A STALE OVERRIDE IS REFUSED, NOT IGNORED. An entry that has become vacuous --
    # because the recorded height moved and the period is now inside the band -- would
    # stop protecting the case it was written for, silently, and would then admit that
    # period again the next time the height moved back.
    # **R1012: THE GUARANTEE WAS A PROPERTY OF THE CALLER.** Both refusals below are
    # guarded by `T in by_period`, so a declared period with no case in the file was
    # passed over in silence. Through `floatfea run` that is unreachable -- `unknown`
    # fires thirteen lines above the call site -- but this function is in `__all__`, and a
    # public entry point whose guarantee holds only because of where it happens to be
    # called is the shape R896 exists to close. Asserted here so the two refusals below
    # can be read as covering the whole declared set.
    absent = sorted((set(declared) | set(override)) - by_period.keys())
    if absent:
        raise ConfigError(
            f"refuse_cases_that_cannot_govern was given {absent} s as declared or "
            f"overridden, and this file carries {sorted(by_period)} s. A period with no "
            f"case behind it cannot be screened, and passing it over in silence would "
            f"leave the two refusals below covering less than the declared set. Through "
            f"`floatfea run` the `unknown` check refuses this first; a direct caller gets "
            f"it here."
        )
    vacuous = sorted(T for T in override if T in by_period and by_period[T].may_govern)
    if vacuous:
        detail = "; ".join(by_period[T].describe() for T in vacuous)
        raise ConfigError(
            f"load_cases.out_of_band_governing names {vacuous} s, which at the recorded "
            f"H = {height:g} m is INSIDE the band: {detail}. An override for a case "
            f"inside the band admits nothing, and carrying it would hide the day it "
            f"starts admitting something again. Remove it -- the period stays in "
            f"`governing_periods` and governs on the band's own terms."
        )

    inadmissible = sorted(
        T for T in declared if T in by_period and not by_period[T].may_govern and T not in override
    )
    if inadmissible:
        detail = "; ".join(by_period[T].describe() for T in inadmissible)
        raise ConfigError(
            f"load_cases.governing_periods declares {inadmissible} s, which cannot set "
            f"an envelope at the recorded H = {height:g} m: {detail}. A case outside the "
            f"associated-period band, or above the deep-water breaking steepness, is "
            f"SENSITIVITY ONLY -- which is what every artifact's EZ2 caveat already "
            f"says, and what nothing checked until now. Remove it from "
            f"`governing_periods` to report it as sensitivity, or -- if it is admitted "
            f"deliberately, as FA0 admits T = 12.5 s at 0.3% below the lower edge -- "
            f"name it in `load_cases.out_of_band_governing` as well, which records the "
            f"decision in every artifact. Refused before the solve, so nothing on disk "
            f"describes an envelope a breaking wave set."
        )
    return screen


def _validated_wave_basis(present: dict[str, Any], sidecar: Path) -> dict[str, Any]:
    """The recorded basis, validated AT THE READER, or a refusal (R877, R878, R879).

    **R877: VALIDATING AT THE COMPARISON PUT THE CHECK BEHIND A DECLARATION.** The first
    repair validated `heading_deg` inside `refuse_headings_this_run_cannot_cover`, which
    returns early when no `load_cases.headings` is declared -- and the shipped example
    declares none. One variable moved, the same sidecar with `heading_deg = true`, through
    the real CLI:

        no headings declared  -> EXIT=0, report.md `* **heading** - True deg`
        headings: [1.0]       -> EXIT=2, refused by name

    So the defect published on the path where nothing was declared, and the refusal's own
    closing clause -- "or remove `load_cases.headings` so no comparison is claimed" --
    routed a reader from the refusal to the publication. **Validation belongs at the
    single READER, where it cannot depend on what the configuration asked for**, and the
    other three fields get it for the same reason: `wave_height_full_m: true` published
    `True m full scale` at exit 0.

    **R878: COMPLETE OR EMPTY, because the two consumers disagreed about which.**
    `cli.py` subscripts all four keys in `_header_lines` and `.get`s the same four in
    `_write_report`. A sidecar with a heading and no wave height made the dict truthy,
    took the subscripting branch and raised `KeyError` AFTER the solve -- exit 1, with a
    zero-byte `member_forces.csv` already in the outputs directory. That is R829/FQ3's
    single-branch repair never reaching the report path. A partial sidecar is refused by
    name rather than downgraded to "not recorded", because a sidecar missing one field is
    WRONG and not ABSENT, and the committed one carries all four.

    **R879: the declared side's discipline is three checks, not one.** `config.py`'s
    `_checked` rejects a bool by name, rejects a non-number, and range-checks. The first
    repair had the first two; a recorded `450.0` against a declared `90.0` was accepted,
    outside `HEADING`'s domain. NaN and infinity are refused here BY NAME rather than one
    line later by the coverage message, and `10**400` is caught before `float()` raises
    `OverflowError`.
    """
    if not present:
        return {}
    missing = [k for k in WAVE_BASIS_KEYS if k not in present]
    if missing:
        raise ConfigError(
            f"{sidecar.name} records a PARTIAL wave basis: {missing} missing from "
            f"{sorted(present)}. Every published artifact states all five, and the report "
            f"header subscripts them, so a partial record raised `KeyError` after the "
            f"solve and left a zero-byte CSV behind. A sidecar missing a field is wrong "
            f"rather than absent -- delete the sidecar to run with the basis NOT RECORDED, "
            f"which every artifact then says, or record the missing field."
        )
    for key, (unit, low, high) in RECORDED_BOUNDS.items():
        value = present[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is {value!r} ({type(value).__name__}), not "
                f"a number. A LIST here is a multi-heading export meeting a "
                f"single-heading reader; a boolean is what YAML and JSON make of `true`. "
                f"Coercing either would publish `{value} deg` or `{value} m` in all three "
                f"artifacts, which is what this refusal replaces."
            )
        # **R883: THE SENTENCE IN THIS DOCSTRING WAS FALSE AND THIS IS THE REPAIR.** It
        # said `10**400` "is caught before `float()` raises `OverflowError`". It was not:
        # `isinstance(10**400, (int, float))` is True, so the type check above passes, and
        # `float(10**400)` then raised `OverflowError` out of this very line -- a traceback
        # rather than a named refusal, for a value a JSON sidecar can carry. Repaired by
        # catching it, so the claim becomes true rather than deleted; CW0 allows either,
        # and a clean refusal is worth more than a sentence.
        try:
            as_float = float(value)
        except OverflowError as exc:
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is an integer too large to represent as a "
                f"float ({type(value).__name__} with {len(str(abs(value)))} digits). "
                f"Refused by name here rather than as an `OverflowError` traceback out of "
                f"the conversion below."
            ) from exc
        if not math.isfinite(as_float):
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is {value!r}, which is not finite. It is "
                f"refused here by name rather than further down, where only a comparison "
                f"would have noticed and only when one was asked for."
            )
        # **THE RAW VALUE, NOT A NORMALISED OR ABSOLUTE ONE, AND I GOT THIS WRONG TWICE.**
        # The first version tested `heading % 360.0`, so a recorded `450.0` passed --
        # `450 % 360` is `90`, inside the domain -- and the run published `450.0 deg` in
        # all three artifacts at exit 0. Measured: `member_forces.csv` 193718 bytes
        # against the control's 193716, the two extra bytes being the digits.
        #
        # The second version range-checked the HEADING ONLY and left both wave heights
        # with a type check and no domain (R881). One variable moved, the committed
        # sidecar with its two heights negated, through the real CLI:
        #
        #     wave_height_full_m =  24.2  ->  EXIT=0, "24.2 m full scale (0.484 m model)"
        #     wave_height_full_m = -24.2  ->  EXIT=0, "-24.2 m full scale (-0.484 m model)"
        #
        # with `member_forces.csv` at 193716 against the control's 193714. A negative
        # wave height is not a wave, and it reached all three published artifacts.
        #
        # The two uses of 360 pull in opposite directions and both are right, which is the
        # reason this check is on the raw value for EVERY field rather than the heading's
        # own special case:
        #   * COMPARING two headings asks whether they are the same DIRECTION, so it
        #     normalises -- `uncovered_headings` does, and the reviewer measured `450`
        #     against a covered `90` as correctly the same direction of travel.
        #   * RANGE-CHECKING a recorded value asks whether it is a value the configuration
        #     could legally have declared. `HEADING` bounds that to `0..360` RAW and
        #     `WAVE_HEIGHT` to `0..100` m, so a sidecar recording `450.0` deg or `-24.2` m
        #     records something no declaration could express.
        if not low <= float(value) <= high:
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is {float(value):g}, outside the declared "
                f"domain {low:g}..{high:g} {unit} that every declared value of this "
                f"quantity is checked against. One domain per quantity, not one per side "
                f"-- a recorded value the configuration could not legally declare cannot "
                f"describe the run that produced these artifacts."
            )
    for key in RECORDED_PROVENANCE_NUMERIC:
        if key not in present:
            continue
        value = present[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is {value!r} ({type(value).__name__}), not "
                f"a number. Nothing here computes with it, but the deliverable PRINTS it "
                f"-- `rho_inf = True` and `dt = fast` each reached a published artifact "
                f"at exit 0 before this (R903). No range is checked: there is no declared "
                f"counterpart for this field, and inventing one is the error R895 found."
            )
        if not math.isfinite(float(value)):
            raise ConfigError(
                f"{sidecar.name}: `run.{key}` is {value!r}, which is not finite, and is "
                f"printed verbatim into a published artifact."
            )
    if not isinstance(present["window"], str):
        raise ConfigError(
            f"{sidecar.name}: `run.window` is {present['window']!r} "
            f"({type(present['window']).__name__}), not the rule text every artifact "
            f"publishes."
        )
    return dict(present)


def exported_wave_basis(npz: Path) -> dict[str, Any]:
    """The heading and wave height a dynamic-inputs file was exported at (R817).

    **THE ARTIFACTS CARRIED CAVEATS ABOUT THESE TWO FACTS AND NOT THE FACTS.** The
    EX3/R724 caveat is about the heading and the EZ2/FA0 caveat is about the wave height's
    associated-period band, and neither value appeared anywhere in the published report or
    either CSV. The committed deliverables they replaced said "all cases are heading 0
    degrees" and "H = 24.2 m" outright; my reworded caveat said "every case carries the
    heading its load cases declare", which in a file that declares no heading is a
    tautology.

    Read from the provenance sidecar the export has always written, which
    `run()` already opens for the scale. A provenance line, not a measurement: nothing
    here is computed, and a file that records neither returns an empty mapping so the
    report can say "(not recorded)" rather than invent one.
    """
    sidecar = npz.with_suffix(".provenance.json")
    if not sidecar.is_file():
        return {}
    return wave_basis_from_sidecar(sidecar)


def wave_basis_from_sidecar(sidecar: Path) -> dict[str, Any]:
    """The validated wave basis from a provenance sidecar PATH (R896).

    **THE SAME INPUT HAD TWO READERS AND ONLY ONE OF THEM VALIDATED.**
    `scripts/measure/f6_results_report.py` read `prov["run"]` straight out of the JSON and
    published `wave_height_full_m`, `wave_height_model_m` and `heading_deg` from it,
    calling neither this module's validator nor `config.py`'s `_checked`. One sidecar, two
    readers, one variable moved:

        full=-24.2 model=-0.484   `floatfea run`        -> REFUSED by name
                                  f6_results_report.py  -> EXIT=0, and published
            "wave height, full scale  : -24.2 m (-0.484 m model, Froude lambda = 50.0)"

    That generator is a PUBLISHED DELIVERABLE under EZ0 -- it is the `GENERATOR` in
    `tests/regression/test_f6_deliverable_agrees_with_itself.py`, whose repair instruction
    is to re-run it -- so R881's subject, "every recorded numeric field has a declared
    domain", was false at the reader that writes the deliverable.

    This function is the single door. A caller holding an npz goes through
    `exported_wave_basis`; a caller holding the sidecar itself comes here. Neither reads
    the `run` block directly, and a reader that does is the defect, not a shortcut.
    """
    # **R1007: `ABSENT` AND `COULD NOT BE READ` WERE THE SAME RETURN VALUE, AND THE
    # SECOND SILENTLY DISABLED A GATE.** A sidecar that exists and cannot be parsed came
    # back `{}`, which every consumer reads as "the export recorded no wave basis": all
    # three artifacts published "wave basis: NOT RECORDED by the export of this
    # dynamic-inputs file", and FL2(d)'s `refuse_cases_that_cannot_govern` took its
    # `if height is None: return ()` exit, so the whole sea-state screen was skipped at
    # EXIT 0 beside the EZ2 caveat denying that a breaking case can govern. An ABSENT
    # sidecar is legitimate -- FL1(a) admits an npz without one -- and a PRESENT one that
    # cannot be read is a defect in the file, so the two stop sharing a return value here.
    if not sidecar.exists():
        return {}
    try:
        recorded = json.loads(sidecar.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(
            f"{sidecar.name} exists and cannot be read as JSON ({type(exc).__name__}: "
            f"{exc}). It is the only record of the wave height and heading these loads "
            f"were exported at, and an unreadable record is NOT an absent one: returning "
            f"'not recorded' here published that sentence on all three artifacts and "
            f"skipped the sea-state screen that decides whether a declared period may set "
            f"the envelope. Repair the file, or delete it to run with the basis genuinely "
            f"not recorded -- which every artifact then says."
        ) from exc

    # **R884: A MALFORMED CONTAINER WAS REPORTED AS AN ABSENT ONE.** `key in run_block` is
    # a MEMBERSHIP test on a list and a SUBSTRING test on a string, so for any non-mapping
    # `run` block every key came back "absent", `present` was empty, `_validated_wave_basis`
    # returned `{}` on its first line, and the same false publication followed. Six
    # malformed containers were measured; `run: 5`, `run: true` and `run: null` instead
    # raised `TypeError` out of the comprehension, so one defect gave a traceback for three
    # shapes and a silent wrong answer for the other three. Both are refusals now, and they
    # are HERE -- before the comprehension -- because that is the only place either can
    # fire: `_validated_wave_basis` takes its own `if not present: return {}` exit on an
    # empty mapping, so a type check added inside it cannot see this input.
    #
    # THE DISTINCTION THIS RESTORES IS THE ONE THE VALIDATOR ALREADY DRAWS FOR A PARTIAL
    # BASIS: "a sidecar missing a field is WRONG rather than ABSENT". A sidecar whose `run`
    # block is not a mapping is wrong in exactly that way.
    if not isinstance(recorded, dict):
        raise ConfigError(
            f"{sidecar.name}: the provenance sidecar's top level is "
            f"{type(recorded).__name__}, not an object. Every artifact states the wave "
            f"basis from this file's `run` block, and a non-object has none -- so the run "
            f"would have published the basis as NOT RECORDED although the file is present "
            f"and merely malformed, and the sea-state screen would have been skipped. "
            f"Delete the sidecar to run with the basis genuinely not recorded, which every "
            f"artifact then says, or fix its shape."
        )
    run_block = recorded.get("run", {})
    if not isinstance(run_block, dict):
        # The multi-heading sentence is TRUE OF A LIST ONLY, so it is attached to a list
        # only. It read as a flat clause first and arm 6 of my own measurement printed
        # "`run` is int, not an object. A LIST here is a multi-heading export ..." -- a
        # refusal explaining a shape the input does not have.
        because = (
            " A LIST here is a multi-heading export meeting a single-heading reader, "
            "which is the same shape `run.heading_deg` is refused for one level down."
            if isinstance(run_block, list)
            else ""
        )
        raise ConfigError(
            f"{sidecar.name}: `run` is {type(run_block).__name__}, not an object.{because} "
            f"Membership of a key in a non-mapping is not key lookup, so every field would "
            f"have read as absent: the run would have published the wave basis as NOT "
            f"RECORDED at exit 0 although this file records one, and skipped the screen "
            f"that refuses a breaking wave from setting the envelope. Delete the sidecar to "
            f"run with the basis genuinely not recorded, or fix its shape."
        )
    present = {
        key: run_block[key]
        for key in (*WAVE_BASIS_KEYS, *RECORDED_PROVENANCE_NUMERIC)
        if key in run_block
    }
    return _validated_wave_basis(present, sidecar)


def validated_export_scale(npz: Path, sidecar: Path | None = None) -> float:
    """The ONE scale a reader of this file may publish at (R919, R908).

    **`exported_froude_lambda` IS A READER, NOT A CHECK, AND I MISTOOK IT FOR ONE.** R906
    moved `f6a_premise_check.py` off a sibling script's module constant and onto that
    function, and the commit message called it "the validated door". It is the FN0 door: it
    reports WHERE it read a value and validates nothing about WHAT it read. Measured
    through the real generator at `froude_lambda = 25.0`, legal inside `FROUDE_LAMBDA`:
    78 diff lines in `results/F6a/premise_check.json`, `max_u_shipped` platform
    `0.995780 -> 0.602180` and hubs `0.972580 -> 0.819713`, with `max_u_change` about
    `1e-8` both times -- **so the premise still read HELD while every utilisation under it
    was some 40% low.**

    And the domain is not enforced anywhere downstream either:
    `froude_factor("force", lam)` refuses `0.0`, a negative and a non-finite, and ADMITS
    `0.5`, `1e-3`, `1e6` and `1e9` -- four decades outside the range the same quantity is
    held to when it arrives from a configuration.

    Two checks, both EXACT and neither a tolerance:

    **(1) The declared domain, applied to the npz key.** `FROUDE_LAMBDA` is the range a
    configured `floatsim.froude_lambda` is held to by `_checked`; a scale read out of a
    file is the same quantity and gets the same range.

    **(2) The two sources must AGREE when both carry one.** `exported_froude_lambda`
    PREFERS the npz key, deliberately and by FN0 -- a sidecar can be separated from its
    npz by a copy and the key cannot -- and
    `test_FN0_the_npz_key_is_PREFERRED_over_the_sidecar` gives them different values on
    purpose to prove which wins. That preference is about which to READ. It is not a
    licence to PUBLISH from one while the other says something else, which is the state
    R908 names: two `scripts/measure/` readers resolving the same quantity for the same
    file from different sources. A disagreement means the pair has been separated or one
    was edited, and that is precisely the state that must not reach a CSV silently.

    So this function is additive: `exported_froude_lambda` keeps its contract and its
    test, and everything that PUBLISHES comes through here. The comparison is `!=`, the
    same form `run()` already uses at the config/npz door, and the period check below is a
    set difference -- give either a margin instead and it becomes a tolerance under
    another name, and goes to `tolerances.py` with a justification.
    """
    exported, where = exported_froude_lambda(npz)
    if exported is None:
        raise ConfigError(
            f"{npz.name}: {where}, so there is no way to know what scale its joint "
            f"reactions are at. A reader that assumes one publishes every force and "
            f"stress at a scale nobody declared, which is the defect FN0 closed."
        )
    unit, low, high = FROUDE_LAMBDA
    if not low <= exported <= high:
        raise ConfigError(
            f"{npz.name}: the exported scale is {exported:g} {unit} according to {where}, "
            f"outside the admissible range [{low:g}, {high:g}] {unit} that a configured "
            f"`floatsim.froude_lambda` is held to. One domain per quantity, whichever "
            f"side of the I/O boundary it arrives from: `froude_factor` admits four "
            f"decades beyond this range without complaint, and every force and stress "
            f"published downstream would carry the error (R919)."
        )

    # **R927: THE CALLER SAYS WHICH RECORD TO COMPARE AGAINST, BECAUSE IT MAY BE READING
    # TWO.** `member_forces_table.py` declares `--provenance` as "the authority for the
    # scale and the height" and R919's repair took the scale off it: the height came from
    # `args.provenance` and the scale from this function, which opened
    # `npz.with_suffix(...)` -- a DIFFERENT file whenever `--provenance` is overridden. A
    # deliverable then had its band, its breaking verdicts and its printed `H` from one
    # provenance record and its Froude scale from another, with nothing comparing them.
    # Measured at an H = 50 m run, and the repair is what created it.
    #
    # Defaulting to the npz's own sidecar keeps every other caller unchanged.
    sidecar = sidecar if sidecar is not None else npz.with_suffix(".provenance.json")
    if sidecar.is_file():
        try:
            recorded = json.loads(sidecar.read_text(encoding="utf-8")).get("run", {})
        except (OSError, json.JSONDecodeError):
            recorded = {}
        beside = recorded.get("lambda")
        # **R1042, SECOND HALF.** `float(beside)` decided whether the two records AGREE, so
        # a bool-typed sidecar scale compared EQUAL to a `1.0` npz key and the disagreement
        # check could not see it either. A record that is not a number is refused here
        # rather than compared, because "they agree" is a claim about two recorded numbers
        # and one of them is not one.
        if beside is not None and not is_recorded_number(beside):
            raise ConfigError(
                f"{npz.name}: {sidecar.name} records `run.lambda` as {beside!r} "
                f"({recorded_spelling(beside)}), which is not a recorded number, so the "
                f"two records of the export scale cannot be compared. The npz key says "
                f"{exported:g} (read from {where}). Re-export the file (R1042)."
            )
        if beside is not None and float(beside) != exported:
            raise ConfigError(
                f"{npz.name}: scale disagreement between the two records of it. The npz "
                f"key says {exported:g} (read from {where}) and {sidecar.name} records "
                f"`run.lambda = {float(beside):g}`. Both are published -- the CSV header "
                f"states the scale and the report prints it in the wave-basis line -- so "
                f"a reader taking one while an artifact states the other cannot tell "
                f"which the numbers are at. The npz key WINS when they agree (FN0); when "
                f"they differ the pair has been separated or edited, and that is refused "
                f"rather than resolved by preference (R908)."
            )
    return exported


def exported_froude_lambda(npz: Path) -> tuple[float | None, str]:
    """The scale a dynamic-inputs file was EXPORTED at, and where that was read from.

    Returns `(None, reason)` when the file records no scale anywhere, so the caller can
    refuse rather than assume one. **Assuming one is R805's failure mode with a different
    coat on**: the whole point of FN0 is that a scale nobody declared cannot be inferred.

    Two places are consulted, in order:

    `froude_lambda` IN THE NPZ, which `scripts/export_f4_dynamic_inputs.py` writes from
    FN0 onward. Preferred because it travels with the array data and cannot be separated
    from it by a file copy.

    `run.lambda` IN THE PROVENANCE SIDECAR beside it, which that script has always
    written. Either way the scale of the one file this repository ships is a RECORDED FACT
    about its export and not a default anyone chose.

    **THE SENTENCE THAT STOOD HERE WAS FALSE, AND IT IS PART OF WHY R1042 HAPPENED
    (R1045).** It said the committed `data/f4/dynamic_inputs.npz` "predates the npz key and
    its sidecar records `run.lambda = 50.0`". Measured:

        'froude_lambda' in raw.files   True
        raw['froude_lambda']           array(50.) float64 ndim 0
        git log -1 -- the npz          62a8281 "R1 step 1 revision 3: ... the scale recorded"

    The committed npz CARRIES the key, so the npz branch below is the live one for the file
    this repository ships. The false clause made the SIDECAR branch read as dead code --
    and the sidecar branch is exactly the one R1041 left unrepaired and R1042 then found.
    A docstring that misreports which branch a reader will reach is how a repair stops one
    line short.
    """
    try:
        with np.load(npz, allow_pickle=False) as raw:
            if "froude_lambda" in raw.files:
                recorded = raw["froude_lambda"]
                # **R1041: THE SAME DEFECT AS R1033, AT THE THIRD SITE NEITHER OF US
                # NAMED.** This read converted whatever was there, so a bool-typed
                # `froude_lambda` became `1.0` -- which is the BOTTOM of `FROUDE_LAMBDA`'s
                # domain, so the range check admits it, and a sidecar recording
                # `lambda: 1.0` agrees with it. Driven:
                #
                #     exported_froude_lambda  -> (1.0, 'the npz')
                #     validated_export_scale  -> ADMITTED lambda = 1.0
                #
                # `lambda = 1` is NO Froude scaling: every full-scale force equals the
                # model-scale one, in the scale both EZ0 generators resolve through
                # `validated_export_scale`. The decision is the shared one, so this site
                # cannot drift from the other two (R983).
                if not is_recorded_number(recorded):
                    return None, (
                        f"the npz records `froude_lambda` as {recorded!r} "
                        f"({recorded_spelling(recorded)}), which is not a recorded number. "
                        f"A scale that is not a number cannot be range-checked as one: a "
                        f"bool converts to 1.0, which is both inside the admissible range "
                        f"and NO Froude scaling at all (R1041). Re-export the file."
                    )
                return float(np.asarray(recorded).reshape(()).item()), "the npz"
    except (OSError, ValueError) as exc:  # pragma: no cover - unreadable npz
        return None, f"the npz could not be read ({exc})"

    sidecar = npz.with_suffix(".provenance.json")
    if not sidecar.is_file():
        return None, f"the npz records no `froude_lambda` and {sidecar.name} is absent"
    try:
        recorded = json.loads(sidecar.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"{sidecar.name} could not be read ({exc})"
    value = recorded.get("run", {}).get("lambda")
    if value is None:
        return None, f"neither the npz nor {sidecar.name} records the export scale"
    # **R1042: THE SIDECAR BRANCH CONVERTED UNCONDITIONALLY, FOUR LINES BELOW R1041.** The
    # npz branch above was repaired and this one was not, in the same function, so the
    # defect simply moved to whichever record the file happens to carry. Measured on a pair
    # whose npz has no `froude_lambda` key:
    #
    #     run.lambda = true    -> exported 1.0, validated_export_scale ADMITTED 1.0,
    #                             froude_factor force x1 and moment x1 -- NO scaling
    #     run.lambda = "50"    -> exported 50.0, a STRING used as a declared number
    #     run.lambda = 50.0    -> exported 50.0 (the control), force x125000
    #
    # And `wave_basis_from_sidecar` REFUSES that same file by name, because `lambda` is in
    # `WAVE_BASIS_KEYS`. One input, two readers, two answers (R896). What shadowed it is
    # not a guarantee: `member_forces_table.py:334` and `f6_results_report.py:458` happen
    # to call the basis validator before resolving the scale, `f6a_premise_check.py:189`
    # does not, and `run()` is covered only because `exported_wave_basis` runs earlier.
    if not is_recorded_number(value):
        return None, (
            f"{sidecar.name} records `run.lambda` as {value!r} "
            f"({recorded_spelling(value)}), which is not a recorded number. A scale that "
            f"is not a number cannot be range-checked as one: a bool converts to 1.0, "
            f"which is inside the admissible range and is NO Froude scaling at all, and "
            f"this value is cubed on every published force (R1042). Re-export the file."
        )
    return float(value), f"{sidecar.name} (`run.lambda`)"


@dataclass(frozen=True)
class _Inputs:
    """The minimum `compute_rows` needs from a dynamic-inputs file.

    Read straight from the npz rather than through `scripts/f4_dynamic_residual`, so the
    library does not depend on the scripts directory. That script's provenance checks
    belong to the EXPORT path, which is what writes the file.
    """

    periods_full_s: tuple[float, ...]


def refuse_disagreeing_period_records(npz: Path, periods: tuple[float, ...], raw: Any) -> None:
    """R1005: the file's two records of each case's period must agree, INDEX BY INDEX.

    `periods_full_s[i]` is the array `run()` reads; `case{i}/period_full_s` is written
    beside each case's own loads by `scripts/export_f4_dynamic_inputs.py` and was read by
    nothing. Everything downstream matches the two BY POSITION --
    `post/forces_table.py` enumerates `periods_full_s` and subscripts `case{i}/lam` with
    the same `i` -- so the top-level array decides the FL2(d) verdict, the published label
    and which rows are in the envelope, while the `case{i}/` groups supply the forces.

    ONE VARIABLE MOVED: indices 0 and 2 of the top-level array permuted, every `case{i}/`
    group byte-identical, the sidecar unchanged, the same configuration, a real `run()`:

        EXIT=0, governing U = 2.78942 at platform:hub2_arm ROOT, LABELLED T = 14.0 s
        band table  | 10 | 0.1550 | breaking | -2.542 | sensitivity only |
                    | 14 | 0.0791 | in band  | -      | governing        |
        control, unpermuted, same code: EXIT=0, U = 1.71167 at T = 12.5 s

    That is the breaking case's utilisation -- 63% above the shipped figure -- published
    under an admissible period's label, with no artifact saying anything is off.

    **COMPARED POSITIONALLY, NOT AS A SET.** At the set level the permutation is invisible
    (the six periods are the same six), so neither the FL2(d) screen nor `unknown` can see
    it, and a set comparison is green on exactly this input -- measured.

    **THE SECOND RECORD IS REQUIRED FOR EVERY CASE, NOT ABSTAINED ON (R1021).** The first
    version of this check abstained at an index whose per-case key was absent, on
    `validated_export_scale`'s `beside is not None` shape, and said so in this docstring as
    its weak direction. Abstention is an EXIT, and THE REVIEWER drove it (R1021, and the
    figures are theirs): deleting `case0/` and `case2/period_full_s` alongside the same
    permutation gave EXIT=0, `U = 2.78942` at a published `T = 14.0 s`, all three artifacts
    written, and a band table byte-identical to the correct run's. That the state is
    refused now is asserted by
    `tests/regression/test_fl2d_band_check.py::test_END_TO_END_R1021_...`, end to end
    through `run()`. A check that can be turned off by deleting the thing it reads is not
    a check, and the non-vacuity assertion that guarded it covers ONE file -- `run()` is
    handed any npz, and FT2.6's heading envelope is in this step's own gate.

    So: every case carries the second record, or the file is refused. That is R878's
    complete-or-empty with the empty half removed.

    Whether that is a NEW demand on the format is the question a reader should ask, and it
    is answered by a cell rather than by a sentence here:
    `tests/unit/test_run_pipeline_refusals.py::`
    `test_R1005_the_COMMITTED_npz_carries_the_SECOND_RECORD_for_EVERY_CASE` asserts the
    shipped file already satisfies it, six cases and six records, and is the EH4 weakening
    direction for this rule. An earlier draft of this paragraph argued the point instead,
    by asserting what the export script writes and what `load()` requires -- two claims
    about other modules that nothing in this repository checks (CW0).

    **ABSENCE IS THE READ FAILING, NOT A DEFAULT (R1021 half two).** This read
    `set(getattr(raw, "files", ()))`, so an object with no `.files` compared 0 of N and
    returned clean -- including a mapping carrying all N correct second records. There is
    no attribute and no default here now: `raw[key]` raising `KeyError` is what absence
    means, so `raw` need only support `__getitem__` and nothing can stand in for "nothing
    is recorded".
    """
    missing: list[int] = []
    mistyped: list[tuple[int, Any]] = []
    disagree: list[tuple[int, float, float]] = []
    for i, top in enumerate(periods):
        key = f"case{i}/period_full_s"
        try:
            value = raw[key]
        except KeyError:
            missing.append(i)
            continue
        # A `str` second record would `float()` to a number and compare EQUAL, so the two
        # records would "agree" while one of them is not a recorded quantity at all --
        # R825's family, a declared field arriving as a different type and being used.
        #
        # **R1033: THIS LISTED THE FORBIDDEN TYPES AND THE LIST WAS WRONG.** It read
        # `isinstance(value, (bool, str, bytes))`, and `np.bool_` is not a `bool` subclass
        # though `np.str_` is a `str` one -- so a bool-typed npz was admitted as `1.0` at
        # every index. The decision is `is_recorded_number`, shared with the configuration
        # reader and with the scale reader, so the three cannot drift, and it asks the
        # DTYPE because what arrives here is a ZERO-DIMENSIONAL array for which
        # `numbers.Real` is False.
        if not is_recorded_number(value):
            mistyped.append((i, value))
            continue
        try:
            beside = float(value)
        except (TypeError, ValueError, OverflowError):
            mistyped.append((i, value))
            continue
        if beside != top:
            disagree.append((i, top, beside))

    if missing:
        raise ConfigError(
            f"{npz.name}: {len(missing)} of {len(periods)} cases carry no "
            f"`case{{i}}/period_full_s` -- indices {missing}. This format records every "
            f"case's period TWICE, and the second record is what makes it possible to tell "
            f"that the top-level array still describes the cases beside it. Without it the "
            f"file is accepted with nothing cross-checking the label the results are "
            f"published under: a permuted `periods_full_s` with the second records deleted "
            f"publishes one case's forces under another case's period at exit 0 (R1021). "
            f"Absence is refused rather than abstained on. Re-export the file with "
            f"`python scripts/export_f4_dynamic_inputs.py`."
        )
    if mistyped:
        rows = "; ".join(
            f"index {i}: `case{i}/period_full_s` = {v!r} ({recorded_spelling(v)})"
            for i, v in mistyped
        )
        raise ConfigError(
            f"{npz.name}: {len(mistyped)} of {len(periods)} second period records are not "
            f"numbers -- {rows}. A text record converts to a float and compares EQUAL to "
            f"the top-level array, so the two records would agree while one of them is not "
            f"a recorded quantity (R825). Re-export the file."
        )
    if not disagree:
        return
    rows = "; ".join(
        f"index {i}: `periods_full_s[{i}]` = {top:g} s against "
        f"`case{i}/period_full_s` = {per:g} s"
        for i, top, per in disagree
    )
    raise ConfigError(
        f"{npz.name}: the file disagrees with itself about which case is which. It records "
        f"every case's period TWICE and the two records differ at {len(disagree)} of "
        f"{len(periods)} indices -- {rows}. The loads are taken from the `case{{i}}/` "
        f"groups BY POSITION while the sea-state screen, the governing-period selection "
        f"and the published `period_full_s` label all come from `periods_full_s`, so a "
        f"disagreement publishes one case's forces under another case's period. Both "
        f"records are published, so a reader cannot tell which the numbers are at. The "
        f"pair has been separated or edited, and that is refused rather than resolved by "
        f"preference (R908). Re-export the file."
    )


def run(cfg: RunConfig, progress: Callable[[str], None] | None = None) -> RunResult:
    """Build, solve, member forces, code check. Wall time per stage (FL1(d))."""
    timings: dict[str, float] = {}
    say = progress or (lambda _line: None)

    # **REFUSED, NOT DEFAULTED AND NOT SKIPPED (FT2.6, EH4).** An empty set of
    # dynamic-inputs files is an error and not a run with no dynamic loads: the
    # alternative would solve gravity alone and publish it as an envelope.
    if not cfg.load_cases.npz_files:
        raise ConfigError(
            "load_cases declares wave `cases` but no `npz`. `floatfea run` does not "
            "invoke FloatSim -- that is `floatfea export`, which needs the HSP worktree. "
            "Run the export first and point `npz` at its output."
        )

    # **R866: THE DECLARED HEADING SET IS CHECKED BEFORE ANYTHING IS BUILT OR WRITTEN.**
    # Earliest possible point, for R809's recorded reason -- a refusal that arrives after
    # the outputs is a warning with a non-zero exit code. The npz's own recorded heading
    # is the only fact needed and `exported_wave_basis` reads it without the HSP
    # worktree.
    # **OVER THE UNION OF THE FILES, which is what makes a declared heading coverable by
    # a file other than the first (FT2.6).** `refuse_headings_this_run_cannot_cover` takes
    # ONE basis, so it is asked once per file and a heading is refused only when NO file
    # covers it -- R809's rule unchanged, applied to a set.
    bases = [(p, exported_wave_basis(p)) for p in cfg.load_cases.npz_files]
    refuse_headings_no_file_covers(cfg.load_cases.headings, bases)

    t0 = time.perf_counter()
    built = build_model(cfg)
    timings["build"] = time.perf_counter() - t0
    say(f"  built {len(built.bodies)} bodies in {timings['build']:.2f} s")

    _refuse_inadmissible(cfg, built)
    notes = _check_material(cfg, built)
    mass = _mass_report(built)

    t0 = time.perf_counter()
    # ===================================================================== FT2.6
    # **EVERY CHECK BELOW RUNS PER FILE AND NOT ONE OF THEM IS RELAXED.** The union is
    # taken of what they produce; it is never taken of whether they passed.
    #
    # **THE HAZARD IS A FIRST-FILE READ, AND IT TYPE-CHECKS.** `per_file[0]` is legal
    # everywhere below, so what holds this is a cell whose answer DIFFERS from the first
    # file's alone -- `test_the_union_is_not_either_file_alone` and
    # `test_R1093_the_BASIS_SECTION_states_EVERY_declared_file_and_not_the_FIRST`, each of
    # which goes red when a first-file read is put back. **A comment COUNTING the reads is
    # what used to be here, and it was wrong (R1093):** it generalised `ruff`'s proof about
    # the raw ARRAY to the whole function, while `wave_basis=per_file[0][3]` was publishing
    # the first file's heading as the run's sea state a hundred lines below it.
    per_file: list[tuple[Path, Any, tuple[float, ...], Any]] = []
    for npz in cfg.load_cases.npz_files:
        raw_one: Any = np.load(npz, allow_pickle=False)
        refuse_scale_disagreement(cfg, npz)
        periods_one = checked_recorded_periods(
            raw_one["periods_full_s"], f"{npz.name}: `periods_full_s`"
        )
        refuse_disagreeing_period_records(npz, periods_one, raw_one)
        per_file.append((npz, raw_one, periods_one, exported_wave_basis(npz)))

    # The UNION of the recorded periods, which is what a declared governing period is
    # checked against now: a period carried by the second file is carried by the run.
    periods = tuple(sorted({p for _n, _r, ps, _b in per_file for p in ps}))
    # There is deliberately NO `raw = per_file[0][1]` here. The first draft kept one and
    # `ruff` reported it unused, which at that commit was a mechanical proof about the raw
    # ARRAY and nothing wider. **AN EARLIER VERSION OF THIS COMMENT MADE IT WIDER, AND
    # THAT IS R1093:** it read "therefore no `npz_files[0]` survives in this function",
    # while `wave_basis=per_file[0][3]` survived a hundred lines from here and `report.md`
    # published it as the run's sea state. Keeping the binding would have re-created the
    # array hazard for the next person who needed "the" raw array; the cells named above
    # are what holds the rest.

    unknown = sorted(set(cfg.load_cases.governing_periods) - set(periods))
    if unknown:
        # **ONE FILE KEEPS THE ORIGINAL MESSAGE, WORD FOR WORD.** Same reason the heading
        # check delegates: EH4's one-file boundary is that a one-tuple behaves exactly as
        # today, and a refusal message is part of the behaviour. Several files get a
        # message that names them all, because "which file was it missing from" is the
        # first thing a reader asks and a union cannot answer it from one name.
        if len(cfg.load_cases.npz_files) == 1:
            raise ConfigError(
                f"load_cases.governing_periods names {unknown} s, which "
                f"{cfg.load_cases.npz_files[0].name} does not contain. It carries "
                f"{sorted(periods)} s. A governing period with no case behind it would "
                f"silently drop out of the envelope."
            )
        names = ", ".join(p.name for p in cfg.load_cases.npz_files)
        raise ConfigError(
            f"load_cases.governing_periods names {unknown} s, which no declared "
            f"dynamic-inputs file contains. Between them, {names} carry "
            f"{sorted(periods)} s. A governing period with no case behind it would "
            f"silently drop out of the envelope."
        )
    # FL2(d), beside its sibling: both ask whether the DECLARED governing set is
    # supportable by this file. `unknown` asks whether the case EXISTS; this asks whether
    # it is an ADMISSIBLE SEA STATE. Here rather than earlier because the periods are in
    # hand and no third open of the npz is needed, and before the solve and before any
    # output, which is R809's requirement -- a refusal after the artifacts is a warning
    # with a non-zero exit code.
    # Per file, because the screen is a function of that file's own recorded HEIGHT: one
    # basis cannot answer for another. The screens are combined, not replaced.
    band_screens = _band_screen_over_files(cfg, per_file)
    timings["load"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    # **PER FILE, AND EVERY ROW CARRIES WHICH FILE AND WHICH HEADING (FW1).** The rows of
    # several files are concatenated, so the envelope a consumer takes over them is the
    # envelope over the union -- and each row says where it came from, so the report's
    # attribution is read off the same object as the number.
    all_rows: list[Any] = []
    for npz, raw_one, periods_one, basis_one in per_file:
        if len(per_file) > 1:
            say(f"  {npz.name}:")
        heading = float(basis_one["heading_deg"]) if basis_one else float("nan")
        computed_one = compute_rows(
            built,
            _Inputs(periods_full_s=periods_one),
            raw_one,
            cfg.load_cases.governing_periods,
            cfg.floatsim.froude_lambda,
            progress=say,
            source=npz.name,
            heading_deg=heading,
        )
        # The STATIC rows are gravity alone and identical for every file, so they are
        # taken from the first file's computation and not repeated -- otherwise a
        # two-file run would publish each static row twice and a consumer taking a
        # maximum would be unaffected while one taking a COUNT would be wrong.
        kept = (
            computed_one.rows
            if not all_rows
            else [r for r in computed_one.rows if r.basis != "static"]
        )
        all_rows.extend(kept)
    computed = _ComputedAll(rows=all_rows)
    timings["solve"] = time.perf_counter() - t0
    say(f"  {len(computed.rows)} member-force rows in {timings['solve']:.1f} s")

    t0 = time.perf_counter()
    utilisations = _utilisations(cfg, built, computed.rows)
    timings["code_check"] = time.perf_counter() - t0
    say(f"  {len(utilisations)} checked stations in {timings['code_check']:.2f} s")

    timings["total"] = sum(
        timings[k] for k in ("build", "load", "solve", "code_check") if k in timings
    )
    return RunResult(
        config=cfg,
        built=built,
        wave_bases=tuple((p.name, b) for p, _r, _ps, b in per_file),
        rows=computed.rows,
        utilisations=utilisations,
        mass=mass,
        timings=timings,
        notes=notes,
        band_screens=band_screens,
        section_properties={
            body.name: _section_properties(body.members[0].section) for body in built.bodies
        },
    )


def static_moments(result: RunResult) -> dict[tuple[str, str], NDArray[np.float64]]:
    """The static rows, keyed by `(member, station)`. FL1(c)'s analytic fixture."""
    return {(row.member, row.station): row.values for row in result.rows if row.basis == "static"}
