---
{
  "module": "proof/networks/Eight/SecLevel_GridDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_GridDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_GridDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 5 «One level of the recursion», the mathematics of one level: definitions only

The objects of the proof of Proposition 3 up to display (36), for the functions A_0, …, A_t, t =
⌈λ/3⌉, of Lemma 2 (`Eight.A`): the functions ι : ℛ → {0, …, t}; the term Z_ι of display (34); the
two factorizations of
Lemma 2(b) in the form in which a network of merged rows takes them; the row network and the column
network of ι; a function ι written as a number. Nothing is proved here. The statements are in
proof/networks/Eight/SecLevel_Grid.lean and SecLevel_GridWords.lean.
The grid and its rectangles (`Paper.Rectangle`, `Paper.rectangles`, `Paper.Settings`,
`Paper.RowSetting`) do not depend on the pieces and are taken from
proof/networks/Paper/SecLevel_Grid.lean; the sum over a grid and the network of merged rows, for any
functions at the
rectangles and any factorizations of them, are in proof/networks/Groundwork/ (`Groundwork.Grid.ZG`,
`Groundwork.Grid.rowNet`). λ is written `lam`; a string of λ bits has the type `Bits lam` (=
`Fin lam → Bool`); rows and columns are numbered by `Fin g`. 

 ## The expansion (34) 

### `patterns`

 The functions ι : ℛ → {0, …, t} of display (34), t = ⌈λ/3⌉. In Lean ι is defined on all ((a,
a'), (j, j')) and is 0 off ℛ. 

### `Zι`

 The term Z_ι of display (34), for tables W on the grid:
Z_ι = ∑_z ∏_w W_w(z_w) · ∏_{straight edges {w,w'}} [z_w(w') = z_{w'}(w)] · ∏_{q ∈ ℛ} A_{ι(q)}(x_q,
y_q, u_q, v_q). 

 ## The two networks of a term Z_ι 

### `rowCut`

 The first factorization of Lemma 2(b): A_i as a function of (x,y) and (u,v). The index θ is a
word of c_i^row bits, and the two functions are `fTop` and `fBot` of the proof of Lemma 2(b),
row-wise. 

### `colCut`

 The second factorization of Lemma 2(b): A_i as a function of (x,u) and (y,v). The index θ is a
word of c_i^col bits, and the two functions are `fTop` and `fBot`, column-wise. 

### `RowIndex`

 The index θ of the factorization of Ψ_{a,a'}: one string for each of the g straight edges
between the two rows, and one word for each rectangle on the two rows. 

### `rowNetwork`

 **The row network of ι** (proof of Proposition 3). Its nodes are the g rows; a setting of row a
is the tuple of the settings of its g grid points.
Different from the paper: a setting of a row has g · g² strings (one of them, for each grid point,
is the dummy of `eqExpansion`), that is g³λ bits, where the paper has g(g² − 1)λ ≤ g³λ. 

### `colNetwork`

 **The column network of ι**: «defined in the same way with rows and columns exchanged». In Lean:
the row network of the transposed grid, with the second factorization of Lemma 2(b). 

 ## A function ι written as a number 

### `digOf`

 The function ι written by the number y: ι(q) is the digit of y in base t + 1 at the number of
the rectangle q. (Defined by the same formula off ℛ.) 

### `patOf`

 The same function, made 0 off ℛ, as the functions of display (34) are in Lean. 
