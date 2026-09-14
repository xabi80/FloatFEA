# F2 figures — GENERATED, do not edit

Produced by `scripts/regen_figures.py` from the shipped runner, on the
machine named in the `stamp_*` rows. Q8 makes CI canonical for this
file; a stamp that is not CI's pinned environment fails the build.
`docs/milestones/F2.md` references these by name as `{{fig:NAME}}`, and
`tests/test_plan_figures.py` fails if a referenced name is missing or if
this file is not what a fresh run produces.

| name | value |
|---|---|
| `stamp_platform` | linux |
| `stamp_python` | 3.13.15 |
| `stamp_numpy` | 2.5.3 |
| `stamp_scipy` | 1.18.1 |
| `stamp_openblas_coretype` | Haswell |
| `rigid_body_mode_ratio` | 1.1986e-14 |
| `rigid_body_subspace_loss` | 5.5095e-15 |
| `rigid_mode_residual` | 7.8658e-17 |
| `rigid_mode_gap` | 2.4027e+13 |
| `rigid_mode_count` | 6 |
| `rigid_mode_residual_worst_over_corpus` | 9.2375e-17 |
| `rigid_mode_gap_smallest_over_corpus` | 6.0131e+07 |
| `rigid_mode_corpus_frames` | 28 |
| `rigid_mode_corpus_counts` | 6 |
| `retired_ratio_over_ceiling_on_corpus` | 10 of 28 |
| `rigid_body_counter_ratio` | 3.0612e-11 |
| `rigid_body_counter_loss` | 7.4709e-12 |
| `corpus_entries` | 203 |
| `corpus_solved` | 164 |
| `clean_worst_ratio` | 0.2564x |
| `clean_worst_entry` | ck_cleanmax_D18p8_tw0p499_aniso1e6 |
| `margin_dropped_flip` | 1217x |
| `margin_dropped_flip_at` | ck_length_thousand_km (L/r_min 4809249) |
| `below_ceiling_dropped_flip` | 0 of 164 |
| `margin_wrong_dof_index` | 299.1x |
| `margin_wrong_dof_index_at` | ck_length_thousand_km (L/r_min 4809249) |
| `below_ceiling_wrong_dof_index` | 0 of 164 |
| `margin_dropped_shear_parameter` | 0.0006932x |
| `margin_dropped_shear_parameter_at` | shear_defect_live_thin_L1990 (L/r_min 114845) |
| `below_ceiling_dropped_shear_parameter` | 8 of 164 |
| `margin_one_element_scaled` | 8.698e+06x |
| `margin_one_element_scaled_at` | br2_floor_thick_iy1e6_L1000 (L/r_min 991) |
| `below_ceiling_one_element_scaled` | 0 of 164 |
| `exempt_total` | 65 of 656 |
| `exempt_by_defect` | dropped_flip 14, dropped_shear_parameter 33, wrong_dof_index 18 |
| `exempt_detected` | 57 |
| `calibration_ulp_worst` | 2.000 ULP |
| `detection_edge` | 3.6425e-14 |
| `detection_edge_at` | ch_edgemin_D0p0758_roll1p05_aniso9p4e5, ci_plateau_D0p0689_roll1p017_aniso9p6e5 |
| `detection_edge_tie_set` | 2 within 1.01x |
| `counter_defect_over_edge` | 2.745e+07x |
| `counter_headroom_room` | 2.19x |
| `counter_defect_boundary` | 2.183e-06 passes, 2.188e-06 fails |
| `boundary_margin_min` | 7630.16x |
| `boundary_margin_max` | 23918.6x |
| `boundary_margin_spread` | 3.135x |
| `boundary_margin_min_plateau` | 60 bases |
| `boundary_margin_max_at` | band_edge_thickwall_free_dir |
| `boundary_margin_bases` | 157 converged |
| `boundary_margin_unbracketed` | 1: ck_cleanmax_x1e8 |
| `boundary_margin_refused` | 6: all_three_extras_free_dir (DegenerateMemberOrientation), ck_vertical_down_onode (DegenerateMemberOrientation), onode_and_aniso_together (DegenerateMemberOrientation), onode_just_outside (DegenerateMemberOrientation), vertical_onode (DegenerateMemberOrientation), vertical_onode_y (DegenerateMemberOrientation) |
| `calibration_ulp_histogram` | 0 ULP x147, 1 ULP x6, 2 ULP x11 |
