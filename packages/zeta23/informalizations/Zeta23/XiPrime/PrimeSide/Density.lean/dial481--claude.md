---
{
  "module": "Zeta23/XiPrime/PrimeSide/Density.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Density.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Density.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Density.lean — generalised-coefficient prime side: the density
ν = μ + cΠ·Π_X + P_c (XiPrime.nucW), its Gram entries / traces / 𝓜, and the §5 sub-results that
need no new idea: [lem:ends] via the ν-generic lem_ends_nu (NuBound for ν), [eq:Msplit]
(bilinearity), and the three sup-bound cross terms [prop:cross](ii)–(iv).
All statements are non-asymptotic in the coefficients: they hold for every coefficient sequence
c : ℕ → ℂ, with the coefficient size entering only through S₁(c) := Σ_{N≤X} ‖c_N‖/√N.
-/
```

 ## Gram entries, traces and 𝓜 for the density ν = nucW cPi X c 

### `GentryW`

 `G_{kl} = ∫ φ̂(τ−τ_k) φ̂(τ−τ_l) ν(τ) dτ` at abstract taper data (= `PrimeSide.GentryNu` for
`ν = nucW cPi p.X c`): the entries of [XF′]'s fixed-coefficient matrix `Mᵀ`. 

### `trGtW`

 `tr M̃ᵀ = L⁻¹ Σ_{k<d} G_{kk}` (shape of `PrimeSide.trGtA`). 

### `trGt2W`

 `tr (M̃ᵀ)² = L⁻² Σ_{k,l<d} G_{kl}²` (shape of `PrimeSide.trGt2A`). 

### `MtotalW`

 `𝓜 = 𝓜[ν, ν]` (= `PrimeSide.MtotalNu`). 

### `S1`

 `S₁(c; X) := Σ_{1≤N≤X} ‖c_N‖/√N` — the only coefficient quantity the sup-bounds see. 

 ## P_c: triangle inequality and continuity 

### `abs_re_cos_add_im_sin_le`

 `|Re c · cos θ + Im c · sin θ| ≤ ‖c‖`. 

### `Pc_abs_le`

 `|P_c(X; τ)| ≤ (1/π) S₁(c; X)` for every τ. 

 ## [eq:Bdef] for ν: NuBound 

### `BcW`

 the ν-version of `B`: `B_c := (l + 4√X) + (3|cΠ − 1| + 1)√X + (1/π) S₁(c; X)`. 

### `nuBoundW_eventually`

 **[eq:Bdef] for ν = μ + cΠ·Π_X + P_c**: for `T ≥ T₀(λ)`, every `c`, every `τ`,
`|ν(τ)| ≤ B_c + log⁺(|τ|/4T)`.  From the ζ bound `nuX_abs_le` (H-Γ + the Chebyshev bound) by
`ν − ν_X = (cΠ−1)Π_X + (P_c − P_X)`. 

 ## [lem:ends] for ν 

### `lem_ends_W`

 **[lem:ends] for ν = μ + cΠ·Π_X + P_c** (from `lem_ends_nu`): for `T ≥ T₀` and every `c`,
`|tr G̃² − 𝓜| ≤ C · L · l · log l · B_c²`,  `B_c = l + O(√X) + (1/π)Σ‖c_N‖/√N`. 

### `BcW_sq_le`

 size of `B_c²` under the crude first-moment hypothesis `S₁ ≤ C₁ √X · l`:
`B_c² ≤ K · l² (1 + X)` with `K = 2(6 + 3|cΠ−1| + C₁)²`. 

 ## [eq:Msplit] for ν 

### `eq_Msplit_W`

 **[eq:Msplit] for ν = μ + cΠ·Π_X + P_c**: the six-term bilinear expansion, with the pole
weight riding on the Π-terms. 

 ## [prop:cross] (ii)–(iv) for ν: the sup-bound terms 

### `cross_PcPi_le`

 **[prop:cross](iii) for P_c**: `|𝓜[P_c, Π_X]| ≤ 6 S₁(c) · L √X` (sup bounds `|P_c| ≤ S₁/π`,
`|Π_X| ≤ 3√X/T` on `I`, `∫Φ² ≤ 2πL`). 
