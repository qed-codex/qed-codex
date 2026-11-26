---
{
  "module": "Zeta23/RvM/GammaSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/GammaSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/GammaSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/GammaSide.lean — the Γ-factor side of the folded contour is
EXACTLY the paper's ∫μ:  (1/π)·Im ∫_L Γℝ'/Γℝ ds = ∫_{T₁}^{T₂} μ(t) dt  for 0 < T₁,
because Γℝ'/Γℝ is holomorphic on Re s > 0 (Cauchy–Goursat on [½,2]×[T₁,T₂] moves L to the critical-line
segment) and Re Γℝ'/Γℝ(½+it) = ½ Re ψ(¼+it/2) − ½ log π = π·μ(t)  (Γℝ(s) = π^{−s/2}Γ(s/2), μ = Zeta23.mu).
-/
```

### `rightHalfPlane`

 the open right half-plane 

### `logDeriv_Gammaℝ_differentiableOn`

 logDeriv Γℝ is holomorphic on Re s > 0. 

### `logDeriv_Gammaℝ`

 logDeriv Γℝ(s) = −(log π)/2 + ½ ψ(s/2) on Re s > 0 (ψ = Complex.digamma = Γ'/Γ). 

### `re_logDeriv_Gammaℝ_half`

 on the critical line: Re(logDeriv Γℝ(½+it)) = π·μ(t). 

### `gamma_side`

 (M4) the Γ-side identity: for 0 < T₁ and any T₂,
(1/π)·Im(halfContour (logDeriv Γℝ) T₁ T₂) = ∫_{T₁}^{T₂} μ. 

 ### helpers for the assembly 

### `mu_continuous`

 μ is continuous (given H-Γ's smoothness field). 

### `mu_le_log`

 |μ(τ)| ≪ log(τ+3) for τ ≥ 1, from H-Γ's Stirling field. 
