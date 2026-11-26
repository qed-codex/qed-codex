---
{
  "module": "proof/rates/GeneralPieces/Num/Between.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/Between.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/Between.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas on the proviso of the second sentence of Theorem A(c): numbers between 0.85·ρ^ℓ and ρ^ℓ for ρ = 11/12 and for ρ = 1/√2

«… provided that a number between 0.85·ρ^ℓ and ρ^ℓ can be computed from ℓ in time polynomial in K_ℓ,
as is the case for ρ = 11/12 and for ρ = 1/√2.» For ρ = 11/12 such a number is ρ^ℓ = 11^ℓ/12^ℓ
itself (`eleven_pow`).
For ρ = 1/√2 it is `num ℓ`/`den ℓ`, that is 2^{−ℓ/2} for even ℓ and (7/5)·2^{−(ℓ+1)/2} for odd ℓ,
because 0.85·√2 ≤ 7/5 ≤ √2 (`between_half`); numerator and denominator are computed from ℓ in unary
in time polynomial in ℓ (`num_den_polyT`),
which is stronger than what the text asks for, because ℓ < K_ℓ. The proof of the second sentence of
Theorem A(c) in this development does not use these lemmas. 

### `eleven_pow`

 11^ℓ/12^ℓ = (11/12)^ℓ. 

### `num`

 The numerator for ρ = 1/√2: 5 for even ℓ, 7 for odd ℓ. 

### `den`

 The denominator for ρ = 1/√2: 5·2^{⌈ℓ/2⌉}. 

### `half_pow_even`

 (1/√2)^{2j} = 2^{−j}. 

### `between_half`

 0.85·(1/√2)^ℓ ≤ num ℓ/den ℓ ≤ (1/√2)^ℓ. 

### `num_den_polyT`

 Numerator and denominator are computed from ℓ, in unary, in polynomial time. 
