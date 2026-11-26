---
{
  "module": "proof/rates/ClauseBound/Inst/HalfTab.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTab.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTab.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The matrices of the operators as tables: definitions

A monomial is written as a list of its parts. `flat` is a list of such lists (in the use: all
partitions of 0, …, W as nonincreasing lists). The matrix of an operator, restricted to the
listed monomials, is a table: a list of integers with the entry for (π, σ) at the position (index of
π)·(length of flat) + (index of σ). The index r of a[r] is not stored: an entry
can only be different from 0 for r = (weight of π) − (weight of σ), and the table holds the entry
for this r. The tables are built part by part, with the recursion that defines a[r];
after each round the table is cut off by `cap` according to `pad`, a padding string of ones given
beside the input (as in Appendix E of the paper). Numbers that are lengths of loops are cut off at
W. Definitions only. 

### `betF`

 The coefficient `ClauseBound.Boson.bet n r`, for n ≤ W. 

### `tab`

 The table of a function of two listed monomials. 

### `lookT`

 The entry of a table for (π, σ). 

### `nopE`

 The entry for (π, σ) of the normally ordered product of the series of t_n with the family whose
table is T. 

### `oneT`

 The table of the identity. 

### `tabOp`

 The table of a[·]. 

### `kfInit`

 The tables of the parts of weight 0, …, h of the empty product. 

### `kfStep`

 One more factor (−1)^{n−1}·y_n: from the tables S of the parts of weight 0, …, h of a^μ to those
of a^{n :: μ}. 

### `tabKF`

 The tables of (the part of weight w of a^μ)[·], w = 0, …, h. 

### `zzF`

 z_ν. 

### `topF`

 `ClauseBound.Boson.topK μx h i r` at (π, σ). 

### `botF`

 `ClauseBound.Boson.botK μv h r` at (π, σ). 

### `FlatOK`

 What the tables need of the list of monomials: different lists are different monomials, the list
is closed under erasing a part, and all weights are at most W. 

### `Rep`

 The table T holds the matrices of the family F: the entry for (π, σ) is that of F r with r =
(weight of π) − (weight of σ). 

### `padOp`

 A length of the pad that suffices for the table of a[·]: Δ listed monomials, L parts. 

### `padKF`

 A length of the pad that suffices for the tables of the parts of weight 0, …, h of a^μ: Δ listed
monomials, μ has the sum s and L parts. 
