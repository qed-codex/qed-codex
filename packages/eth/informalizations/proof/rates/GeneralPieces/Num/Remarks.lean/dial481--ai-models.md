---
{
  "module": "proof/rates/GeneralPieces/Num/Remarks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/Remarks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/Remarks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Small assertions of Appendix A

Sentences of Appendix A that assert something and that no proof of the end theorems uses, because
the cost of an algorithm is
rendered here by the length of a pad and not by a count of operations:
small facts before the count of operations in the proof of part (b) (K ≤ Ξ, K^g ≤ Ξ^g and (2|𝓘| + 2)·2^{cλ}
≤ Ξ^{c+1}·τ); and, in the proof of part (c), that the conditions of the theorem in n hold for all
but finitely many n
when k is fixed, and that a formula with k ≤ 2 is read as a 3-CNF.
Each theorem quotes its sentence. 

 ## Before the count of operations in the proof of part (b) 

### `K_le_Xi`

 K_ℓ ≤ Ξ = g²(λ + B). 

### `K_pow_le`

 «K^g ≤ Ξ^g». 

### `card_term_le`

 «(2|𝓘| + 2)·2^{cλ} ≤ Ξ^{c+1}·τ», where |𝓘| ≤ (2λ)^c, τ = 2^{cλ}·Ξ^{C₂} and Ξ = g²(λ + B) with g
≥ 2. 

 ## The proof of part (c): the bound in n 

### `conditions_eventually`

 «… whose conditions n ≥ K₀^17 and k ≤ (log n)^{1/4} hold for all but finitely many n when k is
fixed». 

### `read_as_three`

 «… and a formula with k ≤ 2 is read as a 3-CNF.» 
