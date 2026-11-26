---
{
  "module": "Zeta23/XiPrime/PrimeSide/Trace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Trace.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Trace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Trace.lean — generalised-coefficient prime side:
[prop:trace] for the density ν = μ + cΠ·Π_X + P_c with ARBITRARY complex coefficients:
    |tr G̃(ν) − a L N| ≤ C · (L √X + L · S₁(c)),      S₁(c) = Σ_{N≤X} ‖c_N‖/√N,
for T ≥ T₀ and every N with |N − Tℓ₁/2π| ≤ A·l (C, T₀ depend on cϱ, λ, A, cΠ, H-Γ), c 1 = 0.

Route: BY DIFFERENCE from the ζ result PrimeSide.prop_trace (tr G̃(ν_X) = aLN + O(L√X), proved,
with the proved Chebyshev bound): ν − ν_X = (cΠ−1)Π_X + (P_c − P_X), and the grid sums of
the Π-part (Pi_part_bound), the P_X-part (sum_P_part_bound) and the P_c-part (complex grid kernel
Aphi_mul_norm_tauKernel_le of ThmE/PrimeSideChi, here with weights ‖c_N‖/√N) are each O(L²√X)
resp. O(L² S₁).
-/
```

### `Pc_part_integrable`

 Integrability of `φ̂(r)² P_c(t+r)` (bounded × integrable). 

### `Pc_part_eq`

 **P_c-part of [prop:trace] at one grid point** (mirror of ThmE.P_part_chi_eq):
`∫ φ̂(r)² P_c(t+r) dr = 2 Σ_{N≤X} (√N)⁻¹ A_φ(log N)·(Re c_N cos(t log N) + Im c_N sin(t log N))`. 

### `sum_Pc_part_bound`

 **Sum of the P_c-parts over the grid** (mirror of ThmE.sum_P_part_chi_bound with weights
`‖c_N‖/√N`): `|Σ_{k<d} ∫ φ̂(r)² P_c(τ_k + r) dr| ≤ (L²/log 2) · S₁(c; X)`, provided `c 1 = 0`. 

### `GentryW_diag_eq`

 **Decomposition of a diagonal entry for ν** (mirror of GentryA_diag_eq):
`G_kk(ν) = G^μ_kk + cΠ·G^Π_kk + G^{P_c}_kk` after translating `τ = τ_k + r`. 

### `prop_trace_W`

 **[prop:trace] for ν = μ + cΠ·Π_X + P_c** with arbitrary complex coefficients (`c 1 = 0`):
`|tr G̃(ν) − a L N| ≤ C · (L √X + L · S₁(c; X))` for `T ≥ T₀` and every `N` with
`|N − Tℓ₁/2π| ≤ A·l`.  Constants depend on (cϱ, λ, A, cΠ, H-Γ); the Chebyshev bound used is
`Zeta23.Cheb.chebyshevMertens`. 
