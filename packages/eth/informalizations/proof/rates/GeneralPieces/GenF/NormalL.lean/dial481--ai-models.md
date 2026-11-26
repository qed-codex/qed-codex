---
{
  "module": "proof/rates/GeneralPieces/GenF/NormalL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/NormalL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/NormalL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "One Laurent polynomial": the coefficients of ⟨𝒩⟩

"Only the ∇_k with |k| ≤ E contribute to ⟨𝒩⟩, so the coefficient n_{μ'',ν''} of x^{μ''}x'^{ν''} in
⟨𝒩⟩ lies in 𝓛; and n_{∅,∅} = [σ = σ']"; and, in the paragraph "The constant", "For E = 0 we have ⟨𝒩⟩ =
1".
Here these three sentences (`StN1`, `StN2`, `StN3`) are derived from the differential equation of
⟨𝒩⟩ in the variables x_n, x'_n, which is the hypothesis `StNeq`: the derivative of ⟨𝒩⟩ for (σ, σ')
with respect
to a variable is a combination, with monomials of 𝓛 as coefficients, of the ⟨𝒩⟩ for (σ − l, σ'), l a
part of σ, and for (σ, σ' − k), k a part of σ'. So by induction on the degree every coefficient is a
Laurent polynomial; and since the factors are the images of the same elements of 𝓛 in 𝓛₊ and in 𝓛₋
(`toP_cL`, `toM_cL`), so are the coefficients. The paper argues by inspection of 𝒩 instead. 

### `cS`

 The factor that comes with ∇_{−r} beside the variable x_i, in 𝓛₊ (`rd = false`) or in 𝓛₋
(`rd = true`): C(r−1, n−1)·ω₁^{r−n} for x_n and C(r−1, n−1)·ω₂^{r−n} for x'_n. 

### `StNeq`

 The differential equation of ⟨𝒩⟩: one term for every different part l of σ (from A⁺ or B⁺) and
one for every different part k of σ' (from A⁻ or B⁻). 

### `cL`

 The same factor as an element of 𝓛: C(r−1, n−1)·ω₁^{r−n} for x_n and C(r−1, n−1)·ω₂^{r−n} for
x'_n. 

### `toP_cL`

 In 𝓛₊ (`rd = false`) the factor is the image of that element of 𝓛. 

### `toM_cL`

 In 𝓛₋ (`rd = true`) it is the image of the same element of 𝓛. 

### `coeff_add_single`

 A coefficient from the derivative: (γ_i + 1) times the coefficient at γ + x_i is the coefficient
of the derivative at γ. 

### `stN2`

 "n_{∅,∅} = [σ = σ']". 

### `coeff_rhs`

 The coefficient at γ of the right side of the differential equation. 

### `stN1`

 "the coefficient n_{μ'',ν''} of x^{μ''}x'^{ν''} in ⟨𝒩⟩ lies in 𝓛": its forms in 𝓛₊ and in 𝓛₋ are
the images of one element of 𝓛. 

### `stN3`

 "For E = 0 we have ⟨𝒩⟩ = 1": for σ = σ' = ∅ all derivatives vanish. 
