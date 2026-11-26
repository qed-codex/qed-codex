---
{
  "module": "proof/rates/GeneralPieces/Half/Size.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Size.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Size.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sizes of the numbers that the programs for the pieces with ρ = 1/√2 return, from the sizes of Appendix B

The programs return entries of the integer matrices `ClauseBound.Boson.topK` and
`ClauseBound.Boson.botK`, which are the factors of displays (54) and (55), the first with the sign
(`GeneralPieces.Half.topK_eq`, `botK_eq`), and their sums of products are the pieces A_s
(`GeneralPieces.ApcL_eq_piece`).
So the bounds of the paragraph «Sizes and operations» hold for them: 2^{3h}·2^{12h²} for a factor
with a^⟨i⟩ (`GeneralPieces.Sizes.abs_factor_a_le`), h!·2^{12h²} for a factor with b
(`abs_factor_b_le`), and Δ times the product of the two for A_s
(`GeneralPieces.ThmHalfPieces.abs_piece_le`). The programs work with one bound for all numbers,
2^{40(h+1)² + ⌈log Δ⌉}, which the appendix does not name (it has 2^{O(h²)}); all three numbers are
below it (`GeneralPieces.ThmHalfPieces.bound_lt_big` for A_s, and `factor_lt_big` for the two
factors). 

### `factor_lt_big`

 Each of the two bounds for a factor is at most the bound for A_s, so it is below the one bound
of the programs. 

### `abs_topK_lt`

 The entries of the matrix that carries a^μ, at listed partitions, are below 2^{big h}, the one
bound of the programs. 

### `abs_botK_lt`

 The entries of the matrix that carries b^ν, at listed partitions, are below 2^{big h}. 

### `abs_valK_lt`

 The values that the two programs of a factorization return, at a label that stands for a pair
(j, τ) with a listed partition τ, are below 2^{big h}. 

### `abs_ApcL_lt`

 «And A_s is a sum of at most Δ products of two factors»: the size of the integer functions that
the programs factorize. 
