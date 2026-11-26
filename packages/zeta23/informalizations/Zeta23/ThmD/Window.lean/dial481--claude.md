---
{
  "module": "Zeta23/ThmD/Window.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Window.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Window.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Window.lean — [thm:D], the concrete window.  A summary of the statements
proved is given at the bottom of the file.

The concrete Montgomery–Taylor window of the [thm:D] proof (paper §7.1):
  φ_D(u) := √(cos(√2 λ u/L)) · φ_flat(u),   φ_flat = Zeta23.Taper.phi ϱ L w (the §2.2 ramp taper),
i.e. the paper's "cos(√2 u/l)^{1/2} ϱ(L/2−|u|)" at general 0 < λ ≤ 1 (we avoid the λ = 1
endpoint; the paper's display is the λ = 1 case with w = 1) and with the ramp width w kept
free as everywhere else in this project.

On the support [−L/2, L/2] the cosine argument is ≤ √2λ/2 = ϑ ≤ 1/√2 < π/2, so cos ≥ cos ϑ ≥ 3/4
> 0 there and √cos is smooth on a neighbourhood; off the support φ_flat kills everything
(and Real.sqrt of a negative is 0, so φ_D is total and 0 outside [−L/2, L/2] regardless).

WHY THESE STATEMENTS (paper §7.1, first paragraph): "Nothing in Sections 4–5 used that φ is
flat-topped, only: φ ∈ C_c² even, 0 ≤ φ ≤ 1, supp φ = [−L/2,L/2], φ nonincreasing in |u|
(so ‖φ'‖₁ ≤ 2, ‖(φ²)'‖₁ ≤ 2), and ‖φ''‖₁, ‖(φ²)''‖₁ ≪ 1" + the moments [eq:abJ] "differ from
those of v*_λ by O(1/L)".
-/
```

### `phiD`

 the Montgomery–Taylor window: φ_D(u) := √(v*_λ(u/L)) · (ramp taper). 

 ### pointwise / support facts (sentence 1 of §7.1) 

### `cos_factor_ge`

 on the support, the cosine factor is bounded below: for |u| ≤ L/2 (0 < λ ≤ 1, L > 0),
cos(√2 λ u/L) ≥ 3/4. 

### `phiD_contDiff`

 φ_D ∈ C² (product of the C³ ramp with √cos, smooth near the support; glued with 0 off it). 

### `phiD_antitoneOn`

 φ_D is nonincreasing in |u|: antitone on [0, ∞). 

 ### derivative norms (sentence 1 of §7.1, parenthetical + last clause) 

### `integral_abs_deriv_le_two`

 generic: an even C¹ function, nonincreasing on [0,∞), with values in [0,1] and support in
[−M, M], has total variation ∫|f'| ≤ 2 (= 2(f(0) − f(M))).  Used for φ_D and φ_D². 

### `integral_abs_deriv_phiD_le`

 ‖φ_D'‖₁ ≤ 2 (even, nonincreasing in |u|, 0 ≤ φ_D ≤ 1, compact support). 

### `integral_abs_deriv_phiD_sq_le`

 ‖(φ_D²)'‖₁ ≤ 2 (same mechanism for φ_D²). 

### `cDT`

 ‖φ_D''‖₁ ≤ C(ϱ, λ)/w: explicit window-constant (the §7.1 "≪ 1" with w-dependence kept,
matching [eq:phinorms]'s shape; cDT plays the role of c_ϱ for this window). 

### `phiD_sq_eq`

 φ_D² = (cosine factor) · φ², with no square root: (√v)² = v wherever φ ≠ 0 (there v ≥ 3/4),
and both sides vanish elsewhere. 

### `integral_abs_eq_setIntegral`

 restriction of ∫|g| to the support interval (g vanishing outside). 

### `deriv2_eq_zero_outside`

 second derivatives vanish beyond the support. 

 ### the moments [eq:abJ] vs their scale-free limits (last sentence of the [thm:D] proof:
"Its constants [eq:abJ] differ from those of v*_1 by O(1/L)") 

### `edge_estimate`

 shared edge estimate for the moment comparisons: for |h| ≤ 1 and a plateau function
0 ≤ p ≤ 1 with p = 1 on [−L/2+w, L/2−w] and p = 0 off [−L/2, L/2],
|∫ h·p − ∫_{[−L/2,L/2]} h| ≤ 2w (the integrands differ only on the two ramps). 

### `integral_scale`

 substitution: ∫_{−L/2..L/2} v(u/L) du = L · ∫_{−1/2..1/2} v. 

### `aD_close`

 a_D := L⁻¹∫φ_D²;  |a_D − a*_λ| ≤ 4w/L. 

### `bD_close`

 b_D := L⁻¹∫φ_D⁴;  |b_D − b*_λ| ≤ 4w/L. 

 #### jD_close: the J-moment of the window vs J* (no Fubini — everything is one-variable:
the sharp-window autocorrelation has a trigonometric closed form (product-to-sum + explicit
antiderivatives), its y-moment evaluates to (L³/2)·(the closed form of J*) [jStar_closed], and
the ramp only moves the autocorrelation by 4w pointwise). 

### `Cfun`

 the sharp-cutoff comparison autocorrelation, in closed form:
Cfun y := (L−y)/2 · cos(ω̃y) + sin(ω̃(L−y))/(2ω̃), ω̃ := √2λ/L. 

### `integral_cos_overlap`

 product-to-sum evaluation: for 0 ≤ y ≤ L,
∫ u in −L/2..(L/2−y), v(u/L)·v((u+y)/L) du = Cfun y. 

### `integral_Cfun_moment`

 the y-moment of the sharp autocorrelation, in closed form:
∫_0^L Cfun(y)·y dy = (L³/2)·(sin(2ϑ)/(8ϑ³) − cos(2ϑ)/(4ϑ²))  (explicit antiderivatives). 

### `sharpW`

 the sharp window k := 1_{[−L/2,L/2]}·v(·/L). 

### `sharp_autocorr_eq`

 the sharp-window autocorrelation (full line) equals the overlap integral, i.e. Cfun. 

### `integral_abs_phiDsq_sub_sharp`

 the window and the sharp cutoff differ by at most 2w in L¹. 

### `autocorr_phiDsq_close`

 pointwise comparison of the window autocorrelation with the sharp one: ≤ 4w on [0, L]. 

### `jD_close`

 J_D := (2/L³)∫_0^L g_D(y)·y dy, g_D = φ_D² ⋆ φ_D² [eq:abJ];  |J_D − J*_λ| ≤ 16w/L. 

 #### C¹ facts for the autocorrelation (the g_D-side hypotheses of ThmD/PP.sumA2g_close):
for h C¹ with compact support and |h| ≤ 1, the autocorrelation is differentiable with
deriv = h ⋆ h' and |deriv| ≤ ∫|h'|.  Via Mathlib's convolution calculus. 

### `gD_deriv_facts`

 the φ_D²-instance: g_D := autocorr(φ_D²) is C¹ with |g_D'| ≤ 2 (the paper's
"|g'| ≤ ‖(φ²)'‖₁ ≤ 2"), the exact hypotheses of ThmD/PP.sumA2g_close. 


Summary of the statements proved in this file:
cos_factor_ge, phiD_contDiff, phiD_antitoneOn, integral_abs_deriv_phiD_le,
integral_abs_deriv_phiD_sq_le, integral_abs_deriv2_phiD_le, integral_abs_deriv2_phiD_sq_le,
aD_close, bD_close, jD_close (via the 1-D route: jStar_closed [Functional.lean] + the
sharp-window autocorrelation closed form integral_cos_overlap/sharp_autocorr_eq + the
y-moment closed form integral_Cfun_moment + the 4w ramp comparison
integral_abs_phiDsq_sub_sharp/autocorr_phiDsq_close — no Fubini anywhere).

