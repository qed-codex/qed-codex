---
{
  "module": "Zeta23/WeilEF/FullLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/FullLine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/FullLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/FullLine.lean — the R → ∞ limit of the rectangle identity
(Zeta23.WeilEF.rectangle_identity, proved): along good heights R_j ∈ [j, j+1] the horizontal
sides vanish (‖H‖ ≪_k 1/R², ‖Λ'/Λ‖ ≪ log²j on them, reflecting Λ'/Λ(1−s) = −Λ'/Λ(s) for
re s < 1/2), the vertical sides converge to the full-line integral (dominated convergence; the
left side is folded onto the right by the functional equation and t ↦ −t), and the zero sums
over |γ| < R_j converge to the absolutely convergent tsum (EF_zero_sum_summable).  The
resulting statement is consumed by Zeta23/WeilEF/Main.lean.
-/
```

 ## Majorant pack 

### `Hfn_apply`

 `H(σ+it)` as a paper Fourier transform at `t + i(1/2 − σ)`. 

### `norm_Hfn_le`

 **Uniform decay of H on the strip −1 ≤ re ≤ 2**: `‖H(σ+it)‖ ≤ C_k/(1+t²)`. 

### `continuous_Hfn_line`

 `H` is continuous along vertical lines (indeed paperFT k is entire). 

### `norm_logDeriv_zeta_le_of_one_lt_re`

 **ζ'/ζ is bounded on vertical lines to the right of 1**:
`‖ζ'/ζ(c+it)‖ ≤ Σ Λ(n) n^{−c}`. 

### `continuous_logDeriv_zeta_line`

 `t ↦ ζ'/ζ(c+it)` is continuous for `c > 1`. 

### `integrable_mul_logDeriv_zeta_of_decay`

 generic: a continuous `φ` with `‖φ(t)‖ ≤ C/(1+t²)` times `ζ'/ζ(c+it)` is integrable. 

### `integrable_Hfn_mul_logDeriv_zeta`

 **Integrability of `H(c+it)·ζ'/ζ(c+it)`** on `re = c ∈ (1, 3/2]`. 

### `log_two_add_le`

 elementary: `log(2+x) ≤ 5 (1+x²)^{1/4}` for `x ≥ 0`. 

### `continuous_logDeriv_Gammaℝ_line`

 `t ↦ Γℝ'/Γℝ(σ+it)` is continuous for `0 < σ ≤ 3/2`. 

### `integrable_mul_logDeriv_Gammaℝ_of_decay`

 generic: a continuous `φ` with `‖φ(t)‖ ≤ C/(1+t²)` times `Γℝ'/Γℝ(σ+it)`, `1/2 ≤ σ ≤ 3/2`,
is integrable (digamma growth ≪ log(2+|t|) on the strip). 

### `integrable_Hfn_mul_logDeriv_Gammaℝ`

 **Integrability of `H(σ+it)·Γℝ'/Γℝ(σ+it)`** for `1/2 ≤ σ ≤ 3/2`. 

 ## Good heights (indexed so that no side conditions remain: R_j ∈ [j+7, j+8]) 

### `completedZeta_ne_zero_on_horizontals`

 nonvanishing of Λ on the horizontal sides `im = ±R`, `1−c ≤ re ≤ c`, given ζ ≠ 0 on
`im = ±R`, `1/2 ≤ re ≤ 2` (the left half by the functional equation Λ(1−s) = Λ(s)). 

 ## The vertical sides 

### `Fline`

 the full-line integrand `F(t) := [H(c+it) + H(1−c−it)]·Λ'/Λ(c+it)`. 

### `continuous_Hfn_reflect`

 continuity of the reflected weight `t ↦ H(1 − c − it)` (= `H((1−c) + i(−t))`). 

### `logDeriv_completedZeta_line`

 on `re = c > 1`: `Λ'/Λ = Γℝ'/Γℝ + ζ'/ζ`. 

### `integrable_Fline`

 **Integrability of the full-line integrand.** 

### `verticals_eq`

 Folding the left vertical side onto the right one: for every `R`,
`V_f(c; −R, R) − V_f(1−c; −R, R) = I • ∫_{−R}^{R} F`,  `f := H·Λ'/Λ`. 

### `tendsto_interval_Fline`

 the truncated integrals converge to the full-line integral along any `R_j → ∞`. 
