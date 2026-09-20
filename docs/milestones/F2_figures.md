# F2 figures — GENERATED, do not edit

Produced by `scripts/regen_figures.py` from the shipped runner, on the
machine named in the `stamp_*` rows. Q8 makes CI canonical for this
file; a stamp that is not CI's pinned environment fails the build.
`docs/milestones/F2.md` references these by name as `{{fig:NAME}}`, and
`tests/test_plan_figures.py` fails if a referenced name is missing or if
this file is not what a fresh run produces.

| name | value |
|---|---|
| `stamp_platform` | win32 |
| `stamp_python` | 3.13.11 |
| `stamp_numpy` | 2.4.0 |
| `stamp_scipy` | 1.17.1 |
| `stamp_openblas_coretype` | unset |
| `rigid_body_mode_ratio` | 1.6009e-14 |
| `rigid_body_subspace_loss` | 5.3061e-15 |
| `rigid_mode_residual` | 7.8658e-17 |
| `rigid_mode_seventh_over_epsilon` | 2.4027e+13 |
| `rigid_mode_seventh_orders` | 12.381 |
| `rigid_mode_mechanism_ceiling` | 1.5243 |
| `rigid_mode_mechanism_cell` | 22 units x 39 spans, subdiv 1 |
| `rigid_mode_mechanism_count` | 350 |
| `rigid_mode_residual_worst_over_corpus` | 1.3502e-16 |
| `rigid_mode_smallest_decided` | 2.0481e+02 |
| `rigid_mode_seventh_orders_smallest_decided` | 1.311 |
| `rigid_mode_largest_refused` | 1.9951e+02 |
| `rigid_mode_largest_rigid_eigenvalue` | 1.4614 |
| `rigid_mode_corpus_frames` | 126 |
| `rigid_mode_corpus_refused` | 33 of 126 |
| `rigid_mode_corpus_decided_clear` | 88 |
| `rigid_mode_corpus_refused_clear` | 25 |
| `rigid_mode_corpus_in_the_window` | 13 |
| `rigid_mode_corpus_window_members` | rb_brace_mm_span_x1000 rb_brace_unit_1um rb_cm_span_x10000 rb_heavy_unit_1um rb_mm_span_x1000 rb_subdiv48_span_x10000 rb_unit_1um rb_window_l7_180 rb_window_l7_188 rb_window_l7_195 rb_window_l7_200 rb_window_l7_205 rb_window_l7_215 |
| `retired_ratio_over_ceiling_on_corpus` | 91 of 126 |
| `rigid_mode_counter_seventh` | 1.2445e+02 |
| `rigid_body_counter_ratio` | 3.0612e-11 |
| `rigid_body_counter_loss` | 7.4708e-12 |
| `corpus_entries` | 203 |
| `corpus_solved` | 164 |
| `clean_worst_ratio` | 0.2765x |
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
| `detection_edge` | 3.6275e-14 |
| `detection_edge_at` | ch_edgemin_D0p0758_roll1p05_aniso9p4e5, ci_plateau_D0p0689_roll1p017_aniso9p6e5 |
| `detection_edge_tie_set` | 2 within 1.01x |
| `counter_defect_over_edge` | 2.757e+07x |
| `counter_headroom_room` | 2.18x |
| `counter_defect_boundary` | 2.174e-06 passes, 2.179e-06 fails |
| `boundary_margin_min` | 7630.16x |
| `boundary_margin_max` | 23918.6x |
| `boundary_margin_spread` | 3.135x |
| `boundary_margin_min_plateau` | 60 bases |
| `boundary_margin_max_at` | band_edge_thickwall_free_dir |
| `boundary_margin_bases` | 157 converged |
| `boundary_margin_unbracketed` | 1: ck_cleanmax_x1e8 |
| `boundary_margin_refused` | 6: all_three_extras_free_dir (DegenerateMemberOrientation), ck_vertical_down_onode (DegenerateMemberOrientation), onode_and_aniso_together (DegenerateMemberOrientation), onode_just_outside (DegenerateMemberOrientation), vertical_onode (DegenerateMemberOrientation), vertical_onode_y (DegenerateMemberOrientation) |
| `calibration_ulp_histogram` | 0 ULP x147, 1 ULP x6, 2 ULP x11 |
