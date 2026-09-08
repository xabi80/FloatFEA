# F2 figures — GENERATED, do not edit

Produced by `scripts/regen_figures.py` from the shipped runner.
`docs/milestones/F2.md` references these by name as `{{fig:NAME}}`, and
`tests/test_plan_figures.py` fails if a referenced name is missing or if
this file is not what a fresh run produces.

| name | value |
|---|---|
| `corpus_entries` | 145 |
| `corpus_solved` | 121 |
| `clean_worst_ratio` | 0.0887x |
| `clean_worst_entry` | band_edge_isotropic_bracing |
| `margin_dropped_flip` | 6.264e+05x |
| `margin_dropped_flip_at` | shear_edge_L4000_aniso_weak (L/r_min 192370) |
| `below_ceiling_dropped_flip` | 0 of 121 |
| `margin_wrong_dof_index` | 1486x |
| `margin_wrong_dof_index_at` | bs_boundary_aniso1e6_L414590 (L/r_min 1993866) |
| `below_ceiling_wrong_dof_index` | 0 of 121 |
| `margin_dropped_shear_parameter` | 0.0006932x |
| `margin_dropped_shear_parameter_at` | shear_defect_live_thin_L1990 (L/r_min 114845) |
| `below_ceiling_dropped_shear_parameter` | 7 of 121 |
| `margin_one_element_scaled` | 8.698e+06x |
| `margin_one_element_scaled_at` | br2_floor_thick_iy1e6_L1000 (L/r_min 991) |
| `below_ceiling_one_element_scaled` | 0 of 121 |
| `exempt_total` | 54 of 484 |
| `exempt_by_defect` | dropped_flip 11, dropped_shear_parameter 28, wrong_dof_index 15 |
| `exempt_detected` | 47 |
| `calibration_ulp_worst` | 2.000 ULP |
| `detection_edge` | 3.9459e-14 |
| `detection_edge_at` | aaa_band_edge_twin |
| `counter_defect_over_edge` | 2.534e+07x |
| `counter_headroom_room` | 2.37x |
| `boundary_margin_min` | 7630.16x |
| `boundary_margin_max` | 23918.6x |
| `boundary_margin_spread` | 3.135x |
| `boundary_margin_min_at` | boundary_kilo_L414p6 |
| `boundary_margin_max_at` | band_edge_thickwall_free_dir |
| `boundary_margin_bases` | 116 converged |
| `boundary_margin_unbracketed` | 0: none |
| `boundary_margin_refused` | 5: all_three_extras_free_dir (DegenerateMemberOrientation), onode_and_aniso_together (DegenerateMemberOrientation), onode_just_outside (DegenerateMemberOrientation), vertical_onode (DegenerateMemberOrientation), vertical_onode_y (DegenerateMemberOrientation) |
| `calibration_ulp_histogram` | 0 ULP x4760, 1 ULP x137, 2 ULP x103 |

Generated at `ba3a93c`.
