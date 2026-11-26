---
{
  "module": "proof/rates/ClauseBound/Inst/HalfTabSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabSpec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The matrices of the operators as tables: correctness

If the list of monomials is in order (`FlatOK`), all parts are at most W and the pad is long enough,
then the tables of proof/rates/ClauseBound/Inst/HalfTab.lean hold the matrices they are meant to
hold;
for the table of a[·], the matrices of the operators a[r], this is `tabOp_rep`, with `padOp` as a
sufficient length of the pad. 

 ### Tables and look-ups 

### `getD_flatMap_map`

 The entry number i·(length of M) + j of a table with rows L and columns M. 

### `lookT_tab`

 Looking up in the table of a function gives its value. 

### `rep_tab`

 The table of a function holds a family of matrices if the function has their entries. 

### `length_tab`

 A table has (length of the list)² entries. 

### `len_int_le`

 The length of the word of an integer of absolute value at most 2^B. 

### `len_tab_le`

 The length of the word of a table with entries of absolute value at most 2^B. 

 ### One round 

### `betF_eq`

 The coefficient of the series of t_n. 

### `sum_toFinset_coe`

 A sum over the distinct members of a list. 

### `nopE_eq`

 One round: the entries of the normally ordered product with the series of t_n. 

 ### The tables 

### `oneT_rep`

 The table of the identity. 

### `tabOp_cons`

 The table of (n :: a)[·] is made from that of a[·] by one round. 

### `padOp_mono`

 The sufficient length of the pad grows with the number of parts. 

### `tabOp_rep`

 The table of a[·] holds the matrices of a[r]. 
