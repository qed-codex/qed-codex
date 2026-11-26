---
{
  "module": "Zeta23/XiPrime/Hardy/GramBridgeW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/GramBridgeW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/GramBridgeW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/GramBridgeW.lean — the pole-weight-2 Gram bridge for the W (= Z′) explicit formula
(adaptation of ExplicitFormula/GramBridge.lean (S2)/(S3) with ν ↦ nucW 2 = μ + 2·Π_X + P_c
[XF′ Prop 9.1 / Thm 9.2(a): the pole weight doubles]).

  literatureRHSW k := 2·(ĥ(i/2) + ĥ(−i/2)) − Σ_n Λ(n)n^{-1/2}(k(log n) + k(−log n)) + (1/2π)∫ ĥ·γ-bracket
                   = literatureRHS k + (ĥ(i/2) + ĥ(−i/2))                                  (literatureRHSW_eq)
  literatureRHSW (kfun) = ∫ ĥ(τ)·nucW 2 X (−Λ) (τ) dτ                                       (literatureRHSW_eq_integral_nucW)
  nucW ϖ X (C(·;Λ⋆)) = nucW ϖ X (−Λ) + P_{C+Λ}(X)                                            (nucW_xiCoeff_eq')
  M^𝒵_{kl} = GentryW1 = literatureRHSW (kfun) + ∫ ĥ·P_{cJ}  given the density split         (GentryW1_eq)
-/
```

### `literatureRHSW`

 the literature right-hand side with POLE WEIGHT 2 (the W / Z′ explicit formula). 

### `nucW_xiCoeff_eq'`

 ν with pole weight ϖ for the ξ′/W coefficients splits off the ζ density:
nucW ϖ X (C(·;Λ⋆)) = nucW ϖ X (−Λ) + P_{C+Λ}(X). 

### `nucW_two_neg_vonMangoldt`

 nucW 2 X (−Λ) = ν_X + Π_X pointwise. 

### `literatureRHSW_eq_integral_nucW`

 **literatureRHSW (f_k ⋆ f̃_l) = ∫ ĥ(τ)·[μ + 2Π_X + P_X](τ) dτ**, X = e^L. 

### `integrable_paperFT_pairTest_mul_nucW2`

 integrability of ĥ·nucW 2 X (−Λ). 

### `GentryW1_eq`

 **M^𝒵_{kl} = literatureRHSW + J-term**: the entry-dependent W main term splits as the pole-weight-2 literature
RHS plus ∫ ĥ·P_{cJ}, given the density decomposition nucW 2 X (C(·; L_{2⋆})) = nucW 2 X (−Λ) + P_{cJ}(X). 
