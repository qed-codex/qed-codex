---
{
  "module": "proof/rates/GeneralPieces/GenF/Assemble.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Assemble.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Assemble.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), paragraph "One Laurent polynomial": comparing the coefficients of x^μ·x'^ν in display (51), which writes the two orders of the product as e^κ·𝒩 in 𝓛₊ and e^{κ'}·𝒩 in 𝓛₋ (below: the display on the two orders)

"Comparing the coefficients of x^μ·x'^ν in (51) gives f_± = μ!·ν!·Σ
Γ_{μ',ν'}·ε_±^{|μ'|+|ν'|}·n_{μ'',ν''}, summed over all pairs of partitions μ', μ'' with union μ and
ν', ν'' with union ν"
(`compare_plus`, `compare_minus`). Here a and b list the parts of μ and ν, the monomial x^μ·x'^ν is
its exponent `ex a b`, and a pair of splittings is a pair (β, γ) of exponents with
β + γ = `ex a b`: β is the exponent of x^{μ'}·x'^{ν'} and γ that of x^{μ''}·x'^{ν''}.
Taken as hypotheses (the statements `StTwoOrders`, `StY`, `StN1`, `StN2`, `StN3`): display (51);
that ⟨Y(a,ω₁)·Y(b,ω₂)⟩ and ⟨Y(b,ω₂)·Y(a,ω₁)⟩ are μ!·ν! times the coefficients of x^μ·x'^ν on its
left sides;
that the coefficients of ⟨𝒩⟩ lie in 𝓛 and are the same in both readings; n_{∅,∅} = [σ = σ']; and ⟨𝒩⟩ =
1 for E = 0. The coefficients of e^κ and e^{κ'} are those of `coeff_expW_kap_false`,
`coeff_expW_kap_true`.
The result is the statement `GeneralPieces.Series.StExpansion`, from which the later paragraphs of
the proof start (`stExpansion_of`). 

 ### The exponent of x^μ·x'^ν 

### `ex`

 The exponent of x^μ·x'^ν, for the lists a, b of the parts of μ, ν. 

### `ex_false`

 In the `false` case (the first order, Y(a,ω₁)·Y(b,ω₂)) the parts of a enter through `xi` and
those of b through `xo`; the sum is the exponent of x^μ·x'^ν. 

### `ex_true`

 In the `true` case (the second order, Y(b,ω₂)·Y(a,ω₁)) the roles are exchanged: b enters through
`xi` and a through `xo`. 

### `wtX_ex`

 |μ| + |ν| = h' + h. 

### `aL_apply_ne_zero`

 Only the variables with an index in the list occur. 

### `eq_zero_of_wtX`

 A divisor of x^μ·x'^ν of weight 0 is 1, because all parts are positive. 

### `snd_eq_zero`

 In a splitting of x^μ·x'^ν the first factor has the full weight only if the second is 1. 

 ### Comparing coefficients 

### `fM_eq_fP`

 f₋ is f₊ with the names exchanged. 

### `mul2_eq_zero_of_sum_ne`

 A product a[r]∘b[−r] has no entries between monomials of different weights. 

### `fP_eq_zero`

 So f₊ = 0 if the two monomials have different weights. The paper takes both of weight E. 

### `compare_plus`

 Comparing the coefficients of x^μ·x'^ν in the first half of display (51). 

### `compare_minus`

 Comparing the coefficients of x^μ·x'^ν in the second half. 

 ### The expansion 

### `sum_filter_map`

 A sum over the terms of a list that pass a test. 

### `stExpansion_of`

 The expansion of f₊ and f₋ from display (51): the terms are indexed by the splittings (β, γ) of
x^μ·x'^ν, with Γ_c = μ!·ν!·Γ_β, N_c the weight of β, and n_c the coefficient of γ in ⟨𝒩⟩;
the number G is μ!·ν!·Γ_{μ,ν}. For monomials of different weights, which the paper does not
consider, f₊ = f₋ = 0 and one term with n_c = 0 serves. 
