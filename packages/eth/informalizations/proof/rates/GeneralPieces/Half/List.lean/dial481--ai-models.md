---
{
  "module": "proof/rates/GeneralPieces/Half/List.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/List.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/List.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2: from the ring of Appendix B to the matrices that the programs compute

The programs write a partition as a list of natural numbers and compute entries of integer matrices:
`ClauseBound.Boson.topK` carries a^μ and `ClauseBound.Boson.botK` carries b^ν. This file shows that
these entries
are the factors in displays (54) and (55) of the proof of the theorem on pieces with ρ = 1/√2
(`topK_eq`, `botK_eq`), so that the integer function `ClauseBound.Boson.ApcL` is the piece A_s of
the appendix
(`ApcL_eq_piece`). Then the sum of the pieces and display (54) for the matrices are read off the
statements about the ring, `AppHalfPieces.PieceFacts`, which is a hypothesis here (`sum_ApcL`,
`ApcL_row_eq`).
Display (55) for the matrices is the definition of `ApcL` with the matrix product written as a sum
over σ (`ClauseBound.Boson.ApcL_col_eq`). 

 ### Lists of natural numbers as partitions 

### `toPNats`

 A list of natural numbers as a list of positive integers. 

### `ptn`

 The partition whose parts are listed. 

### `zz_eq`

 z_μ is the same number for the partition and for its multiset of natural numbers. 

 ### The factor that carries b^ν 

### `botK_eq`

 The entry (π, σ) of the matrix (h!/z_ν)·t^ν[r] is the coefficient of t^π in b^ν[r]·t^σ. 

 ### The factor that carries a^μ 

### `polyK`

 A combination of monomials, given as a list, as a polynomial; the coefficient of a term is given
by k. 

### `polyOf`

 A combination of monomials, given as a list, as a polynomial. 

### `polyOf_map_cons`

 One term c·t_j times a combination. 

### `polyOf_flatMap`

 A combination of variables times a combination of monomials, multiplied out. 

### `sum_Icc_eq_list`

 A sum over 1, …, n as the sum of a list. 

### `sum_yl`

 The list of the terms of (−1)^{n−1}·y_n. 

### `aFam_eq`

 a^μ, multiplied out. 

### `part_tpow`

 The part of weight h' of a monomial. 

### `angle_smul_tpow`

 (q·t^μ)^⟨i⟩ = C(|μ| + h, i)·q·t^μ for |μ| ≤ h. 

### `angle_polyOf`

 a^⟨i⟩ for a combination of monomials of weight at most h. 

### `coef_op_polyK`

 The coefficient of t^π in a[r]·t^σ for a combination a of monomials: the same combination of the
entries of the matrices. 

### `topK_eq`

 The entry (π, σ) of the matrix that carries a^μ is (−1)^i times the coefficient of t^π in
(a^μ)^⟨i⟩[r]·t^σ. 

 ### The pieces 

### `ApcL_eq_piece`

 The integer function that the programs factorize is the piece A_s of the appendix, for μ(x) the
partition listed in ℓ(x). By display (55). 

### `sum_ApcL`

 Σ_s A_s = h!·[x = v][y = u], from the statement about the ring. 

### `ApcL_row_eq`

 Display (54) for the matrices, from the statement about the ring. 
