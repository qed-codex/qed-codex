---
{
  "module": "proof/rates/GeneralPieces/Ring/ThmHalfPieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/ThmHalfPieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/ThmHalfPieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The theorem on the pieces with ρ = 1/√2, without the running time, from the statements about the ring

The proof of that theorem in Appendix B, from its first sentence to the sentence that Definition 7
holds with ρ = 1/√2 if c is large enough. The pieces are
A_s(x,y,u,v) = the coefficient of t^{μ(u)} in Q_s(a^{μ(x)}, b^{μ(v)})·t^{μ(y)}, with h the least
integer ≥ 2 with p(h) ≥ 2^λ and μ(x) the partition of h with number x in the lexicographic list.
Their sum, the two displays (54) and (55) and the integrality of the factors are taken from
`AppHalfPieces.PieceFacts`, which is a hypothesis here. From these: the pieces are integers
(`piece_row`);
they add up to h!·[x = v][y = u] (`sum_A`); numbering the pairs (i, σ) of (54) and of (55) gives
factorizations through ⌈log R^row_s⌉ and ⌈log R^col_s⌉ bits (`row_A`, `col_A`);
the number of terms of (55) is R^col_s (`card_terms_col`); all partitions in (55) are listed
(`wt_le_col`), and A_s is a sum of at most Δ products of two factors
(`Rcol_le_Delta`, `abs_piece_le`), so it is 2^{O(h²)} in absolute value (`bound_lt_big`,
`abs_A_lt`).
The sizes of the factors are those of `GeneralPieces.Sizes`; the bound on c^row_s + c^col_s, h =
O(λ²) and log Δ = O(λ) are those of `GeneralPieces.Bits`, with display (46) in the form proved in
`ClauseBound.Part.exists_bounds`, with B·log E in place of log E.
The choice of c and the lemma that a sum of R products factors through ⌈log R⌉ bits are those of
proof/rates/ClauseBound/Boson/Final.lean and proof/rates/ClauseBound/Boson/Half.lean; their
exponents 16h² + 4h and 17h² + h, which
are larger than 12h² + 3h and 13h², are used as bounds for the two factors. 

 ### The factors as integers 

### `cast_num_coef`

 A coefficient of an integer polynomial, as an integer. 

### `fa`

 The first factor of a term of (54) or (55), with the sign: (−1)^i times the coefficient of
t^{σ'} in a^⟨i⟩[r]·t^σ, for a = a^ξ. 

### `fb`

 The second factor: the coefficient of t^{σ'} in b[r]·t^σ, for b = b^ν. 

### `fam`

 The family of the appendix: d = h!, I = {−2h, …, 2h}, the pieces A_s, c^row_s = ⌈log R^row_s⌉,
c^col_s = ⌈log R^col_s⌉. A_s is written as the numerator of the coefficient that defines it, which
is an
integer (`cast_A`). 

### `abs_fa_le`

 The first factor is small at listed partitions. 

### `abs_fb_le`

 The second factor is small at listed partitions. 

 ### The pieces 

### `piece_row`

 Display (54) with integer factors. In particular the pieces are integers. 

### `piece_col`

 Display (55) with integer factors. 

### `cast_A`

 The integer A_s is the coefficient that defines the piece. 

### `A_row`

 Display (54) for the integers A_s, with the sum over the monomials of the matrices. 

### `A_col`

 Display (55) for the integers A_s, with the sum over the monomials of the matrices. 

### `sum_A`

 Σ_s A_s = h!·[x = v][y = u]. 

### `wt_map`

 The weight of a monomial of the matrices, as a partition. 

### `row_A`

 Numbering the pairs (i, σ) of (54), here in some order that is not specified, gives a
factorization through ⌈log R^row_s⌉ bits: the first function depends on (x,y), the second on (u,v). 

### `col_A`

 Numbering the pairs (i, σ) of (55), here in some order that is not specified, gives a
factorization through ⌈log R^col_s⌉ bits: the first function depends on (x,u), the second on (y,v). 

### `wt_le_col`

 All partitions in (55) are among the listed ones. 

### `Rcol_le_Delta`

 The sum (55) has at most Δ terms. 

### `card_terms_col`

 The number of terms of (55) is R^col_s. 

### `abs_piece_le`

 A_s is a sum of at most Δ products of two factors: |A_s| ≤ Δ·(2^{3h}·2^{12h²})·(h!·2^{12h²}),
which is 2^{O(h²)}. 

### `bound_lt_big`

 Δ·(2^{3h}·2^{12h²})·(h!·2^{12h²}) is below 2^{40(h+1)² + ⌈log Δ⌉}, the bound from which c is
chosen. 

### `abs_A_lt`

 Hence all values of the pieces are 2^{O(h²)} in absolute value: below the bound from which c is
chosen. 

### `thmHalfPiecesPure`

 The theorem on the pieces with ρ = 1/√2, with the construction of its proof and without the
running time, from the statements about the ring. 
