---
{
  "module": "Paper/Groups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Groups.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Groups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "The contracting case: unitriangular groups", from the first estimate on


### `kappa`

 The constant κ_n of the first estimate. 

### `lem_first_rank_one`

 The proof of Lemma lem:first, rank one in the upper right block (Lemma lem:words). 

### `lem_first_block`

 The proof of Lemma lem:first: "By Lemmas lem:growth and lem:words the first [the upper right block] contributes at
most 18μ(d+1)s^d ∑_j |x_j|." Here the mean square over the block is bounded, with the sum in place of the mean. 

### `lem_first_double`

 The proof of Lemma lem:first, the step of the induction: "A uniform element is a product of a uniform element of
the abelian upper right block and uniform elements of the two diagonal blocks", and these "use disjoint sets of
generators". 

### `kappa_small`

 κ_n² n = o(n²). 

### `lem_first`

 **Paper: Lemma lem:first.** "There are κ_n with κ_n² n = o(n²) such that every contracting length on U_n satisfies
(E_g|g|²)^(1/2) ≤ κ_n ∑_j|x_j|." Here κ_n is the explicit kappa μ s n. 

### `windowConst`

 C(n) = κ_n² n. 

 ### Windows 

### `segment_fixed`

 A point of a segment between fixed points is fixed: the point in Lemma lem:toolkit(a) is the only one with these
distances. 

### `fixed_closed_convex`

 "These form a closed convex set, which contains the barycenter of every orbit." In the project P z is that
barycenter; projection_var shows that it is the nearest point. 

### `projection_var`

 Lemma lem:toolkit(d) for the fixed set: |z Pz|² + |Pz q|² ≤ |zq|² for every fixed q. 

### `projection_nearest`

 The P of the windows is the nearest-point projection to the fixed set: P z is fixed, is at least as near to z as every
fixed point, and is the only fixed point with this property. 

### `projection_sq_le`

 "So |z Pz|² ≤ E_g|z,gz|²." 

### `projection_segment`

 "q projects to v": a point between v = Pa and a has the projection v. 

### `windows_commute`

 "For disjoint windows the projection of one maps the fixed set of the other into itself, as the two groups
commute." 

### `eq_window`

 The inequality (eq:window) of the paper: |z Pz|² ≤ C(n) ∑ e_j(z)² over the generators of the window. "By Lemma
lem:first and the Cauchy–Schwarz inequality." 

### `lem_tele_generator`

 The proof of Lemma lem:tele: "By Lemma lem:toolkit(c) each generator moves the barycenter by at most 1/n times
the sum of what it moves the n points." 

### `lem_tele`

 **Paper: Lemma lem:tele.** "Let u ≥ 2, p+3u ≤ h, ζ ≥ 0 and 4C(3u) ≤ ζ²(u−1)². If a is fixed by [p,p+2u), then
|a, P_{[p+u,p+3u)}a| ≥ (1−ζ)R, where R = |a, P_{[p,p+3u)}a|." 

### `lem_angle_projections`

 The proof of Lemma lem:angle for any two fixed sets with a common point v. If every point q that divides [v,a], a the
first projection of z, is at squared distance at least (1−c²)|qv|² from the second fixed set, then
|aa′|² ≤ |za|² + |za′|² + 2c|za||za′|. 

### `lem_angle`

 **Paper: Lemma lem:angle.** "Let u, p, ζ be as in Lemma lem:tele, 0 ≤ ζ ≤ 1, and 1−c² ≤ (1−ζ)², c > 0. If a, a′
are the projections of z for [p,p+2u) and [p+u,p+3u), then |aa′|² ≤ |za|² + |za′|² + 2c|za||za′|." 

### `thm_poincare_far`

 The proof of Theorem thm:poincare: "If the windows of i, i′ do not meet and y is fixed by that of i, then the
point nearest to y among those fixed by that of i′ is fixed by both. So this point can serve as v in the proof of Lemma
lem:angle, with ζ = 0 and any c > 0, and gives |Q_iz Q_{i′}z|² ≤ r_i² + r_{i′}²." 

### `windowSum`

 F(z) = ∑_i r_i², r_i = |z Q_iz|, Q_i the projection for the window [iu, iu+2u), i < L. 

### `thm_poincare_pairs`

 The proof of Theorem thm:poincare: "For neighbours Lemma lem:angle allows c(r_i²+r_{i′}²) more", so
∑_{i,i′} |Q_iz Q_{i′}z|² ≤ 2(L−1+2c)F(z). 

### `thm_poincare_step`

 The proof of Theorem thm:poincare: for the barycenter b of the points Q_iz, "F(b) ≤ ∑_i|b Q_iz|² ≤ (1 − (1−2c)/L)F(z)
and L|zb|² ≤ F(z) − F(b)", by Lemma lem:toolkit(c). 

### `thm_poincare_limit`

 The proof of Theorem thm:poincare: "Iterate: F decreases geometrically and the steps add up to at most
2√(F(z)/(1−2c)), so the points converge to one fixed by every window, hence by U_h. So |z P_{[0,h)}z|² ≤ 4F(z)/(1−2c)." 

### `thm_poincare_windows`

 The proof of Theorem thm:poincare: "(eq:window) for n = 2u, each generator lying in at most two windows, bounds
F(z) by 2C(2u) ∑_j e_j(z)²." 

### `thm_poincare_action`

 The Poincaré bound for every isometric action of U_h, h = lu, on a CAT(0) space with contracting lengths, from the
proof of Theorem thm:poincare, with ζ = 1/32 and c = 1/4: "|z,gz| ≤ 2|z P_{[0,h)}z|", so E_g|z,gz|² ≤ 32C(2u)/(1−2c) ∑_j e_j(z)². 

### `thm_poincare_size`

 The proof of Theorem thm:poincare: "Since C(n) = o(n²), some u has 4C(3u) ≤ (u−1)²/32²; fix it." 

### `thm_poincare`

 **Paper: Theorem thm:poincare.** "There are u ≥ 2 and C₀ such that for every l ≥ 2, h = lu, and every price on U_h,
E_{g,k}|k,gk|² ≤ C₀ ∑_{j<h−1} E_k|k,x_jk|²." In the proof Z = L²(U_h,Y) has the sum for the mean; this scales all
distances by one factor. C₀ = 32C(2u)/(1−2c). 

### `PoincareBound`

 The inequality of Theorem thm:poincare for the numbers u and C₀: for every l ≥ 2, h = lu, and every price on U_h,
E_{g,k}|k,gk|² ≤ C₀ ∑_j E_k|k,x_jk|². 
