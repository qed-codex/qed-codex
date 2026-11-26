---
{
  "module": "proof/rates/ClauseBound/Inst/CertHalfTab.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfTab.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfTab.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The tables of the matrices of the operators are polynomial-time

Certificates (`PolyT`) for the functions of proof/rates/ClauseBound/Inst/HalfTab.lean, each with all
its arguments as functions of an input x. The numbers W and h are given in unary; the pad, the list
of
monomials, the partitions and all other numbers are data. The two folds (`tabOp`, `tabKF`) cut their
state off by the pad after every round, so they need no bound on its growth. The end
of the file: `topF_polyT` and `botF_polyT`. 

 ### Lists 

### `erase_polyT`

 Erasing the first occurrence of a number. 

### `count_unary`

 The number of occurrences in a list is given in unary. 

 ### Entries and tables 

### `betF_polyT`

 The coefficient of one term of the recursion. 

### `tab_polyT`

 The table of a polynomial-time function of two listed monomials. 

### `lookT_polyT`

 Reading an entry of a table. 

### `nopE_polyT`

 One entry of the normally ordered product with a family given by its table. 

### `oneT_polyT`

 The table of the identity. 

 ### The table of a[·] 

### `tabOp_polyT`

 The table of a[·], built part by part and cut off by the pad after every round. 

 ### The tables of the parts of a^μ 

### `kfInit_polyT`

 The tables before the first round. 

### `kfEntry_polyT`

 One entry of one table of the next round. 

### `kfStep_polyT`

 One round: the tables for one more factor. 

### `tabKF_polyT`

 The tables of the parts of weight 0, …, h of a^μ, cut off by the pad after every round. 

 ### The two functions of a factorization 

### `zzF_polyT`

 The number z_ν. 

### `chooseZ_clip`

 A binomial coefficient with a natural number on top vanishes when the lower number is larger. 

### `chooseZ_nat_polyT`

 A binomial coefficient with a natural number in unary on top; the lower number may be in binary. 

### `topF_polyT`

 The function on top of a factorization is polynomial-time; W and h are given in unary. 

### `botF_polyT`

 The function below of a factorization is polynomial-time; W and h are given in unary. 
