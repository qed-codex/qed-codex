---
{
  "module": "proof/networks/Groundwork/Cross/Cuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Cross/Cuts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Cross/Cuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The pieces A_i of the decomposition of the crossing bit by bit, a variant that the paper does
not state (Section 4 of the paper uses blocks of three bits): A_i factors across rows through the
strings with at least i singlets, and across
columns through the strings with at most i states other than Φ⁺. Here the factorisations are over ℤ
with no factor 2^λ: in
place of the (orthogonal) Bell basis we use a basis of integer vectors that contains the singlet (rows)
or Φ⁺ (columns),
and its dual basis. The label sets `rowLabels` and `colLabels`, and hence the numbers of bits of the
two factorisations, are those of this bit-by-bit decomposition. These are the factorisations the
networks use. 

### `BitCut`

 Three tables for a cut of one bit. They are meant to factor the two one-bit functions that are
multiplied out, D⁰ (here I)
and D¹ (here −s⊗s): D⁰ = Σ_h top_h ⊗ bot0_h and D¹ = Σ_h top_h ⊗ bot1_h. The structure does not ask
this: it is the hypothesis of
`BitCut.expand`, and `A_rows`, `A_cols` check it for the tables `rowBit`, `colBit`. 

### `BitCut.Top`

 The part of a string β on the first side of the cut. 

### `BitCut.Bot`

 The part of a string β on the second side of the cut, for the term with i factors D¹. 

### `ind`

 [p = a][q = b]. 

### `rowBit`

 Rows, cut (x,y | u,v). Basis e₀₀, e₁₁, e₁₀, s named Φ⁺, Φ⁻, Ψ⁺, singlet; dual basis e₀₀, e₁₁,
[u≠v], e₀₁. 

### `colBit`

 Columns, cut (x,u | y,v). Basis φ = e₀₀+e₁₁, e₁₁, e₀₁, e₁₀ named Φ⁺, Φ⁻, Ψ⁺, singlet. 

### `prod_mul_prod_compl_eq_ite`

 A product over S times a product over the complement of S, as one product over all positions. 

### `BitCut.expand`

 Multiplying out: one lemma for both cuts (and for the Bell basis). a, b are the two ends on one
side, c', d those
on the other. 

### `rowBot_eq_zero`

 With fewer than i singlets in β, every set of i positions has one where β is no singlet, and the
term vanishes. 

### `colBot_eq_zero`

 With more than i states other than Φ⁺ in β, every set of i positions misses one of them, and the
term vanishes. 

### `A_rows`

 Across rows, over ℤ: A_i factors through the strings with at least i singlets. 

### `A_cols`

 Across columns, over ℤ: A_i factors through the strings with at most i states other than Φ⁺. 

### `abs_rowTop_le`

 Across rows, the factors on the first side of the cut are 0 or ±1. 

### `abs_colTop_le`

 Across columns, the factors on the first side of the cut are 0 or ±1. 

### `abs_rowBot_le`

 Across rows, the factors on the second side of the cut have absolute value at most 2^λ. 

### `abs_colBot_le`

 Across columns, the factors on the second side of the cut have absolute value at most 2^λ. 
