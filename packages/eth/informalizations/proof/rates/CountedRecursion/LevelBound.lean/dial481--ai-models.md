---
{
  "module": "proof/rates/CountedRecursion/LevelBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LevelBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/LevelBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound of the theorem, from one depth to the next
Proof of Theorem A (b): 𝒯 = 2^{eK²L}(K(L + B'))^{C₀K²} ≤ 2^{e(ρ+3ζ)N}·Ξ^{cg⁴/4+K²+(c+5)C₀K²}; here
it is proved at the bounds Λ_j, 𝔅_j for λ and B (`level_le`, `boundBelowFrom`, `boundBelow`),
from the hypotheses `ChainLabel`, `ChainBase` and `ChainExponent`. The exponent of 2 is written
e_{j+1}N − 3N/K_j, which is e_j(ρ + 3ζ_j)N, with N = K_{j+1}²Λ_{j+1}.
From `BoundBelow` and the sentence on the exponent of Ξ (`ExponentFits`), both hypotheses here, it
follows that the bound of the depth j is at most that of the depth j + 1, for C₀ ≥ 2(c + 1)
(`levelBound_le_succ`, `levelBound_le_top`). 

### `pos_of_chainLabel`

 1 ≤ Λ_j, 𝔅_j for j ≤ ℓ, from `ChainLabel` (for j < ℓ) and the hypotheses on λ and B (for j = ℓ). 

### `baseAt_cast`

 The base of the polynomial factor, as a real number. 

### `four_mul_le_xiAt`

 4·Λ_{j+1} ≤ Ξ and 4 ≤ Ξ, for x₀ ≥ 1. 

### `four_mul_div_g`

 4 divides g⁴, for x₀ ≥ 1. 

### `level_le`

 𝒯 = 2^{eK²L}(K(L + B'))^{C₀K²} ≤ 2^{e(ρ+3ζ)N}·Ξ^{cg⁴/4+K²+(c+5)C₀K²}, at the bounds for λ and B. 

### `boundBelowFrom`

 `level_le` in the form of the statement `BoundBelowFrom`. 

### `boundBelow`

 **By the induction hypothesis and e ≤ 1, the 𝒯 of Lemma 8 may be taken as 𝒯 = 2^{eK²L}(K(L +
B'))^{C₀K²} ≤ 2^{e(ρ+3ζ)N}·Ξ^{cg⁴/4+K²+(c+5)C₀K²}.** 

### `levelBound_succ`

 The bound of the depth j + 1, with Ξ for its base. 

### `levelBound_le_succ`

 The bound of the depth j is at most that of the depth j + 1, for C₀ ≥ 2(c + 1). 

### `levelBound_le_top`

 So the bound of every depth j ≤ ℓ is at most the bound of the theorem for the outermost
instance. 
