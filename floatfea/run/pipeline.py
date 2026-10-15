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
from typing import Any

import numpy as np
from numpy.typing import NDArray

from floatfea.checks.api_wsd import check_member
from floatfea.model.material import Section
from floatfea.model.platform import (
    _outer_diameter,
    admissible,
    build_superstructure,
)
from floatfea.post.forces_table import Row, compute_rows
from floatfea.run.config import ConfigError, RunConfig

__all__ = [
    "RunResult",
    "build_model",
    "exported_froude_lambda",
    "run",
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
    notes: tuple[str, ...] = ()
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

    For the current star each body's members are one group, so the group names ARE the
    body names. FL2(a) replaces this with a member list carrying its own group labels;
    that is why this function is small and separate.
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
    values = {spec.fraction for spec in specs if spec is not None}
    if len(values) != 1:
        raise ConfigError(
            f"mass_distribution declares different fractions per body "
            f"({sorted(v for v in values if v is not None)}). "
            f"`build_superstructure` applies ONE fraction to every body, so a per-body "
            f"split cannot be honoured today and running at one of them would report a "
            f"mass distribution the configuration did not ask for. FL2(a) is where the "
            f"builder gains per-body fractions."
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

    return build_superstructure(
        path=cfg.floatsim.deck,
        froude_lambda=cfg.floatsim.froude_lambda,
        measurement_fraction=fraction,
        measurement_sections=sections,
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
    written. The committed `data/f4/dynamic_inputs.npz` predates the npz key and its
    sidecar records `run.lambda = 50.0`, so the scale of the one file this repository
    ships is a RECORDED FACT about its export and not a default anyone chose.
    """
    try:
        with np.load(npz, allow_pickle=False) as raw:
            if "froude_lambda" in raw.files:
                return float(np.asarray(raw["froude_lambda"]).reshape(()).item()), "the npz"
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
    return float(value), f"{sidecar.name} (`run.lambda`)"


@dataclass(frozen=True)
class _Inputs:
    """The minimum `compute_rows` needs from a dynamic-inputs file.

    Read straight from the npz rather than through `scripts/f4_dynamic_residual`, so the
    library does not depend on the scripts directory. That script's provenance checks
    belong to the EXPORT path, which is what writes the file.
    """

    periods_full_s: tuple[float, ...]


def run(cfg: RunConfig, progress: Callable[[str], None] | None = None) -> RunResult:
    """Build, solve, member forces, code check. Wall time per stage (FL1(d))."""
    timings: dict[str, float] = {}
    say = progress or (lambda _line: None)

    if cfg.load_cases.npz is None:
        raise ConfigError(
            "load_cases declares wave `cases` but no `npz`. `floatfea run` does not "
            "invoke FloatSim -- that is `floatfea export`, which needs the HSP worktree. "
            "Run the export first and point `npz` at its output."
        )

    t0 = time.perf_counter()
    built = build_model(cfg)
    timings["build"] = time.perf_counter() - t0
    say(f"  built {len(built.bodies)} bodies in {timings['build']:.2f} s")

    _refuse_inadmissible(cfg, built)
    notes = _check_material(cfg, built)
    mass = _mass_report(built)

    t0 = time.perf_counter()
    raw: Any = np.load(cfg.load_cases.npz, allow_pickle=False)

    # ONE SOURCE FOR THE SCALE (R805, FN0). The configuration's lambda reaches the deck
    # build, every Froude conversion and the provenance -- and a dynamic-inputs file
    # exported at a DIFFERENT scale cannot be mixed with it, because the joint reactions
    # in that file are already scaled. Refused, naming both, rather than silently applying
    # one scale to the geometry and another to the loads.
    exported, where = exported_froude_lambda(cfg.load_cases.npz)
    if exported is None:
        raise ConfigError(
            f"{cfg.load_cases.npz.name}: {where}, so there is no way to know what scale "
            f"its joint reactions are at. The configuration declares "
            f"floatsim.froude_lambda = {cfg.floatsim.froude_lambda!r}. Re-export the file "
            f"-- `floatfea export` records the scale from FN0 onward -- rather than "
            f"assuming it matches, which is exactly the defect FN0 closed."
        )
    if exported != cfg.floatsim.froude_lambda:
        raise ConfigError(
            f"scale mismatch. floatsim.froude_lambda = {cfg.floatsim.froude_lambda!r} in "
            f"{cfg.source.name}, and {cfg.load_cases.npz.name} was exported at "
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

    periods = tuple(float(x) for x in raw["periods_full_s"])
    unknown = sorted(set(cfg.load_cases.governing_periods) - set(periods))
    if unknown:
        raise ConfigError(
            f"load_cases.governing_periods names {unknown} s, which "
            f"{cfg.load_cases.npz.name} does not contain. It carries {sorted(periods)} s. "
            f"A governing period with no case behind it would silently drop out of the "
            f"envelope."
        )
    timings["load"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    computed = compute_rows(
        built,
        _Inputs(periods_full_s=periods),
        raw,
        cfg.load_cases.governing_periods,
        cfg.floatsim.froude_lambda,
        progress=say,
    )
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
        rows=computed.rows,
        utilisations=utilisations,
        mass=mass,
        timings=timings,
        notes=notes,
        section_properties={
            body.name: _section_properties(body.members[0].section) for body in built.bodies
        },
    )


def static_moments(result: RunResult) -> dict[tuple[str, str], NDArray[np.float64]]:
    """The static rows, keyed by `(member, station)`. FL1(c)'s analytic fixture."""
    return {(row.member, row.station): row.values for row in result.rows if row.basis == "static"}
