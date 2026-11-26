---
{
  "module": "Zeta23/WeilEF/VerticalLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/VerticalLine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/VerticalLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/VerticalLine.lean.  Vertical-line integrals for the EF contour.

KEY DEVICE (no contour shifting needed on the prime side): for s = c + it on a vertical line,
H(s) := h((s−1/2)/i) = paperFT k (t − i·b) with b := c − 1/2, and
  paperFT k (t − i·b) = paperFT k_b t,  where k_b(u) := k(u)·e^{b·u}  (the TILTED test function,
still C_c²).  Hence the line integral (1/2π)∫ H(c+it)·n^{−c−it} dt is, by Fourier inversion of
k_b (Zeta23.EF.paper_inversion, proved in Zeta23/ExplicitFormula.lean, with integrability from
Zeta23/ExplicitFormula/Bridge.lean's integrable_fourier_of_contDiff_two),
  n^{−c}·k_b(log n) = n^{−c}·k(log n)·n^{b} = n^{−1/2}·k(log n).
Summing against −ζ'/ζ(c+it) = Σ Λ(n)n^{−c−it} (Mathlib LSeries, 1 < c) with a dominated
tsum/integral swap (domination: ‖paperFT k_b t‖(1+t²) ≤ ‖k_b‖₁+‖k_b''‖₁ from
Zeta23.EF.norm_paperFT_mul_one_add_sq_le × Σ Λ(n)n^{−c} < ∞) gives the prime side.
-/
```

### `Hfn`

 The test function on vertical lines: H(s) := h((s − 1/2)/i). 

### `tilt`

 The tilted test function k_b(u) := k(u)·e^{b u}. 

### `Hfn_line`

 On the line Re s = c: H(c+it) = paperFT (tilt k (c − 1/2)) t. 

### `tilted_inversion`

 Tilted inversion: (1/2π)∫ paperFT (tilt k b) t · e^{−i t y} dt = k(y)·e^{b y}. 

### `integrand_eq_tsum`

 Step 1 (pointwise on the line): the integrand is the tsum of tilted-transform × L-series
terms.  −ζ'/ζ = LSeries ↗Λ on Re s > 1 (Mathlib), then distribute paperFT (tilt k b) t. 

### `per_n_line_integral`

 Step 2 (per-n line integral): (1/2π)∫ paperFT(tilt k b) t · term_n(c+it) dt
  = Λ(n) n^{−1/2} k(log n). 

### `line_integral_swap`

 Step 3 (tsum/integral swap): dominated by ‖paperFT (tilt k b)‖ ∈ L¹ × Σ Λ(n)n^{−c} < ∞. 

### `prime_side_line`

 **Prime side on Re s = c ∈ (1, 3/2]**:
(1/2π)∫_ℝ H(c+it)·(−ζ'/ζ)(c+it) dt = Σ_{n≥1} Λ(n) n^{−1/2} k(log n). 

### `digamma_growth_strip`

 Coarse digamma growth on the right half-plane strip (consumed by the Γℝ line shift and the
horizontal-segment estimates; any polynomial bound works — dischargeable via a Stirling-type
estimate or directly). 

### `integrable_line`

 continuity ⇒ integrability on vertical lines under a majorant (used by vertical_line_shift). 

### `vertical_line_shift`

 General vertical-line shift for an analytic function with an integrable, uniformly-decaying
majorant on a closed strip (Cauchy on rectangles + horizontal vanishing + dominated limits).
Proof route: RectangleIntegral machinery (HolomorphicOn.vanishesOnRectangle). 

### `differentiable_paperFT`

 paperFT of a continuous compactly supported function is entire (differentiation under the
integral sign); needed for all contour arguments (H = Hfn k analytic in s). 

### `log_two_add_div_le`

 log(2+x)/(1+x²) ≤ 6 (1+x)^{−3/2} for x ≥ 0. 

### `norm_paperFT_le_uniform`

 uniform decay of H = paperFT k near the real axis: for |Im z| ≤ 1,
‖paperFT k z‖ ≤ 2 e^{Lam} (‖k‖₁ + ‖k″‖₁)/(1 + (Re z)²). 

### `norm_logDeriv_Gammaℝ_le`

 growth of logDeriv Γℝ on 1/2 ≤ Re s ≤ 3/2. 

### `gamma_line_shift`

 **Archimedean line shift**: the Γℝ'/Γℝ-part of the two
vertical lines shifts to the critical line (rectangle with no poles of Γℝ'/Γℝ in Re s > 0,
horizontal pieces vanish by digamma growth × [eq:hfbound] decay of paperFT k). 
