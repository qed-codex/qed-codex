---
{
  "module": "Zeta23/XiPrime/Transfer/W.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/W.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/W.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/Transfer/W.lean — Z′ (Hardy W) case: **the W trace transfer**.
Target (StatementW.lean §W3): XiTraceTransfer Z Pf wCoeffFamily at Z = wZeros hZ hs, i.e. the SAME Prop as
for ξ′ — comparison matrix GpC (F.c T), pole weight 1 — starting from the W explicit formula WEF (main term GpW1:
coefficients C(N; L_{2⋆}(τ⋆_{kl})), L_{2⋆} REAL, pole weight 2).

ROUTE.  G − Mᵀ = (G − M^𝒵) + (M^𝒵 − M^{c,2}) + (M^{c,2} − M^{c,1}), each HatNegligible:
  • G − M^𝒵:     [XF′ 5.1] engine hatNegligible_of_entryBound fed by WEF;
  • M^𝒵 − M^{c,2}: [XF′ 6.1] engine hatNegligible_of_geom at the REAL base ½l (L_{2⋆}(τ⋆) = ½l + δ_{kl}, the same
                  δ_{kl} = ½log(τ⋆/T) ∈ [0, ½log 2]), input ReexpansionW (Transfer/InputsW.lean);
  • M^{c,2} − M^{c,1} = the Π-part Gram matrix (∫ φ̂_k φ̂_l Π_X)_{kl} ([XF′ §9.3(i)]): by |Π_X(t+r)| ≤ 6√X/t + 12√X r²/t²
                  (PrimeSide.PiX_shift_bound) every entry is ≤ 6√X·2πaL/T + 12√X(8+2(cϱ/w)²)/T², so the hat-trace
                  is ≪ √X = o(N) and the hat-Frobenius² is ≪ X = o(N) (X ≤ T, l → ∞; no λ < 1 needed here).
-/
```

### `L2T`

 the Z′ base point ½ l(T) ∈ ℂ (real; = Defs.L2star at τ⋆ = T). 

### `L2star_eq_L2T_add`

 L_{2⋆}(τ⋆) = ½l + ½log(τ⋆/T). 

### `GpW1_sub_GpCW_apply`

 the entries of M^𝒵 − M^{c,2}: P-part entries of the coefficient differences (μ, 2Π_X cancel). 

### `GpCW_two_sub_GpC_apply`

 the entries of M^{c,2} − M^{c,1}: the Π-part Gram matrix. 

 ### The Π-part entries are uniformly small 

### `integral_phiHat_sq_abs_PiX_le`

 ∫ φ̂(τ−t)² |Π_X(τ)| dτ ≤ 6√X·2πaL/t + 12√X(8+2(cϱ/w)²)/t²  for t ≥ 2. 

### `abs_gentryNu_PiX_le`

 the Π-part Gram entry is bounded by the same quantity, for τ_k, τ_l ≥ t ≥ 2 (2|ab| ≤ a² + b²). 

 ### The three HatNegligible pieces and the main W theorem 

### `hatNegligible_entryDependenceW`

 **M^𝒵 − M^{c,2} is HatNegligible** ([XF′ 6.1] at the real base ½l). 

### `hatNegligible_piPart`

 **the Π-part matrix M^{c,2} − M^{c,1} is HatNegligible** ([XF′ §9.3(i)]). 

### `wTraceTransfer_of`

 XiTraceTransfer Z Pf F from the W explicit formula WEF (main term M^𝒵, pole weight 2,
real base) + the Z′ re-expansion + the PP bound.  Instantiate at Z := wZeros hZ hs, F := wCoeffFamily. 
