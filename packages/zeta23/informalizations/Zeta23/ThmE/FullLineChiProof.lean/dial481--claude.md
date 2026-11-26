---
{
  "module": "Zeta23/ThmE/FullLineChiProof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiProof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiProof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 ## ψ growth on the wide strip 1/4 ≤ re ≤ 2 (digamma_growth_strip with the rectangle
widened — needed for ψ((s+κ)/2) with re s ≤ 3/2, κ ≤ 1) 

 ## The archimedean log-derivative G_{q,κ} := logDeriv (s ↦ q^{s/2} Γℝ(s+κ)) 

### `exists_parity'`

 parity bookkeeping:
gammaFactor χ = Γℝ(· + κ) for κ = 0 (even) or 1 (odd). 

### `norm_logDeriv_archChi_le`

 growth of `logDeriv (archChi q κ)` on 1/2 ≤ re ≤ 3/2 (κ ≤ 1). 

### `differentiableAt_logDeriv_archChi`

 `logDeriv (archChi q κ)` is complex-differentiable on re > 0. 

### `archChi_bracket`

 **the critical-line bracket**: G(1/2+it) + G(1/2−it) = 2π·μ_{κ,q}(t). 

 ## Majorant pack for L(s,χ) and the arch factor 

### `norm_logDeriv_L_le_of_one_lt_re`

 **L'/L(χ) is bounded on vertical lines to the right of 1** (by Σ Λ(n) n^{−c}). 

### `continuous_logDeriv_L_line`

 `t ↦ L'/L(χ)(c+it)` is continuous for c > 1 (χ ≠ 1). 

### `integrable_mul_logDeriv_L_of_decay`

 generic: continuous `φ` with `‖φ t‖ ≤ C/(1+t²)` times `L'/L(χ)(c+it)` is integrable. 

### `integrable_Hfn_mul_logDeriv_L`

 **Integrability of `H(c+it)·L'/L(χ)(c+it)`** on re = c ∈ (1, 3/2] (`hintL`). 

### `integrable_mul_logDeriv_archChi_of_decay`

 generic: continuous `φ` with `‖φ t‖ ≤ C/(1+t²)` times `logDeriv (archChi q κ)(σ+it)`,
`1/2 ≤ σ ≤ 3/2`, `κ ≤ 1`, is integrable. 

### `gammaFactor_eq_parity`

 gammaFactor in terms of the parity: `gammaFactor χ s = Γℝ(s + parity χ)`. 

### `logDeriv_completedLSym_sub_L`

 **Λ_sym'/Λ_sym − L'/L = logDeriv (archChi q (parity χ))** on re s > 0, L(s,χ) ≠ 0. 

### `logDeriv_completedLSym_sub_L_inv`

 the arch difference is the same for χ and χ⁻¹ (equal gammaFactor) — `harchdiff`. 

### `integrable_Hsum_mul_archDiff`

 **Integrability of `(H₁+H₂)·(Λ_sym'/Λ_sym − L'/L)`** on the c-line (`hintΓ`). 

 ## The archimedean line shift 

### `line_shift_generic`

 **G-generic archimedean line shift** (gamma_line_shift with Γℝ'/Γℝ replaced by
any `G` holomorphic on re > 0 with ‖G(σ+it)‖ ≤ C_G log(2+|t|) on 1/2 ≤ σ ≤ 3/2). 

### `gamma_line_shift_chi'`

 **gamma_line_shift_chi**: the (Λ_sym'/Λ_sym − L'/L)-part of the
two vertical lines shifts to the critical line where the bracket is 2π·μ_χ. 
