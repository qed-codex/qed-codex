---
{
  "module": "proof/rates/ClauseBound/Inst/HalfTabKF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabKF.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfTabKF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The tables of the parts of a^μ by weight: correctness

If the list of monomials is in order (`FlatOK`), all parts of μ are at most W and the pad has at
least `padKF` entries, then the table number w of `tabKF` holds the matrices of
(the part of weight w of a^μ)[r] (`tabKF_rep`), and `topF` computes the entries of
`ClauseBound.Boson.topK` (`topF_eq`). The proof goes part by part through μ: one round of the
program is the
recursion `KF_cons`, and the bound `abs_KF_le` on the entries shows that the pad does not cut the
tables off. 

### `sum_Icc_one`

 A sum over 1, …, n as a sum over 0, …, n − 1. 

### `getD_map_range`

 The member number w of a list made from 0, …, h. 

### `padKF_mono`

 `padKF` grows with the sum and with the number of parts. 

### `rep_cap`

 h + 1 tables that have the entries of the families F 0, …, F h, bounded by 2^B, are not cut off
by a pad of the length given, and hold these families. 

### `kfInit_eq`

 The tables at the start, as tables of functions. 

### `kfStep_entry`

 One round of the program is the recursion for one more factor. 

### `tabKF_rep`

 The table number w holds the matrices of (the part of weight w of a^μ)[r]. 

### `topF_eq`

 The program for the first factor of a term of a piece computes it. 
