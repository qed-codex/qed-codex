---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/DirichletLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/DirichletLine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/DirichletLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
A Dirichlet series with general complex coefficients against the Weil test
weight on a vertical line:
    (1/2π) ∫_ℝ H(c+it) · Σ_N a_N N^{−(c+it)} dt = Σ_N a_N N^{−1/2} k(log N),
H = Zeta23.WeilEF.Hfn k, for k ∈ C_c²(ℝ), any real c, and Σ_N ‖a_N‖ N^{−c} < ∞.
[XF′ Thm 4.2 (e)].
-/
```

### `LSeries_term_line`

 the L-series term on the line, factored: a_N · N^{−c} · e^{−it log N}. 

### `norm_LSeries_term_line`

 norm of the L-series term on the line Re s = c. 

### `integrand_eq_tsum_gen`

 Step 1 (pointwise): H(c+it) · L(a, c+it) = Σ' paperFT(tilt k (c−1/2)) t · term_N. 

### `per_n_line_integral_gen`

 Step 2 (per-N line integral): (1/2π)∫ paperFT(tilt k (c−1/2)) t · term_N(c+it) dt
  = a_N N^{−1/2} k(log N). 

### `continuous_LSeries_term_line`

 continuity of each L-series term along the line. 

### `summable_coeff_bound`

 the summable majorant of the term norms. 

### `continuous_LSeries_line`

 continuity of t ↦ L(a, c+it) (uniformly convergent series of continuous functions). 

### `norm_LSeries_line_le`

 ‖L(a, c+it)‖ ≤ Σ' majorant. 

### `line_terms_integrable`

 integrability of each term and summability of the L¹ norms (the domination for Step 3). 

### `line_integral_swap_gen`

 Step 3 (tsum/integral swap). 

### `integrable_Hfn_mul_LSeries`

 integrability of H(c+it)·L(a, c+it) on the line. 

### `dirichlet_line`

 **(EF3)**: (1/2π)∫_ℝ H(c+it)·Σ_N a_N N^{−(c+it)} dt = Σ_N a_N N^{−1/2} k(log N). 

### `dirichlet_line_mirror`

 the mirrored weight: (1/2π)∫ H(1−c−it)·L(a,c+it) dt = Σ_N a_N N^{−1/2} k(−log N). 
