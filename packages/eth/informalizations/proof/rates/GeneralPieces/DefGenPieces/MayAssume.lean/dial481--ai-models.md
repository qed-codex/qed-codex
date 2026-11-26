---
{
  "module": "proof/rates/GeneralPieces/DefGenPieces/MayAssume.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/MayAssume.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/MayAssume.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «We may and do assume c_row, c_col ≤ 2λ», for the definition as stated

The remark after the definition of pieces with parameters (ρ, c) in Appendix A, proved as there: any
F : {0,1}^{2λ} × X' → ℤ factors through 2λ bits, as F(z,z') = Σ_θ [z = θ]·F(θ,z'), and a longer
factorization is replaced by this one. The second function, F(θ,z'), is computed by the program for
the values of the pieces, which is part of the definition.

One thing differs. The paper replaces c by c + 2, «which pays for computing c_row or c_col first».
Here the two new programs do not compute these numbers: they look at the length of the label θ,
which on the labels of min(c_row, 2λ) bits is the same choice, except that a factorization through
exactly 2λ bits is replaced as well. So the constant c stays the same. The new programs, `trimV`,
are defined in `DefGenPieces/Progs.lean`. 

### `sum_min_words`

 Σ_θ [w = θ]·G(θ) = G(w) over the words of 2λ bits, and nothing changes over shorter words: a sum
t·b over the words of c₀ bits with the value V = G(w) is also the sum over the words of
min(c₀, 2λ) bits of the two functions that are [w = θ] and G on words of 2λ bits and t and b on all
others. 

### `trimV_isPieces`

 «We may and do assume c_row, c_col ≤ 2λ»: the new programs are pieces with the same parameters
(ρ, c), the same functions A_i and the same program for their values. 

### `trimV_cap_le`

 All numbers of bits of the new programs are at most 2λ. 

### `mayAssume`

 «We may and do assume c_row, c_col ≤ 2λ», as stated in `AppRunningTimeStatement.lean`: the same
constant c, the same d, 𝓘 and A_i and the same program for the values. 

### `exist_par_one`

 What the proof of Theorem A uses: if there are pieces with parameters (ρ, c), there are programs
`P` with `Par P ρ c`, `P.Keeps` and `P.m = 1` (here `m` is a field of `PiecesF`, not a number of
clauses), with the same constant c. 
