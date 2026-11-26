---
{
  "module": "proof/rates/GeneralPieces/DefGenPieces/Progs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/Progs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/DefGenPieces/Progs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces with parameters (ρ, c): the operations on programs. Definitions only

The programs and predicates that the files on «we may and do assume c_row, c_col ≤ 2λ» and on the
definition of pieces speak of; nothing is proved here.
* `valF P`, `valOf P`: the value of a piece, added up from P's own factorization.
* `trimV P val c`: the pieces of the programs P, read at h = 0, with every factorization through 2λ
  bits or more replaced by F(z,z') = Σ_θ [z = θ]·F(θ,z'), with their program `val` for F. This is
  the form that the theorem on the general recursion uses.
* `atZero P c m`: the programs read at the parameter h = 0, in the form that the recursion reads.
* `Realizes P h lam A`: the functions A are the pieces of the programs P. 

### `VQ`

 The argument of `valF`: ((pad, column-wise?), (parameter h in unary, index i), four strings).
The first two strings are the arguments of `top`, the other two those of `bot`: they are
x, y, u, v row-wise and x, u, y, v column-wise. λ is the length of the first string. 

### `valF`

 The value of the piece number i: the sum of top·bot over all words of `cap` bits, cut off by the
pad. 

### `isLong`

 Is the label of the query a word of 2λ bits? 

### `Realizes`

 The functions A are the pieces of P at (h, λ): what `PiecesF.Spec` says of some A. 

### `valOf`

 The program for the value of a piece: `valF` at h = 0, from the row-wise factorization. It reads
λ off the first string. 

### `atZero`

 The programs of P read at h = 0 for every h, with the exponent c·λ of the pad, the bound (2λ)^c
for the number of bits of the values, and the constant m. 

### `askAt`

 The four strings at which the second function of the new factorization asks for the value of the
piece: the halves of the label θ take the places of the arguments of the first function, which are
x, y row-wise and x, u column-wise. 

### `trimV`

 The pieces of P, read at h = 0, with every factorization through 2λ bits or more replaced by
F(z,z') = Σ_θ [z = θ]·F(θ,z'), where F(θ,z') is computed by `val`. 
