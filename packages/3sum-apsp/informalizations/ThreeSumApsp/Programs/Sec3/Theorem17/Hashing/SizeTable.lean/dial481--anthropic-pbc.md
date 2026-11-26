---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/SizeTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/SizeTable.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/SizeTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The table of the sizes of Strassen's recursion

szTable(dst, p, J) writes the sizes p, 4p, …, 4^J p of the matrices of Strassen's recursion, the
list `szList p J`, and changes nothing else (`szTable_spec`, `szTable_meets`).


### `szList`

 The table of the sizes: 4^i p for i ≤ J. 

### `length_szList`

 The table of the sizes has J + 1 entries. 

### `Dst`

 The local variables of szTable: the arguments dst, p, J; the exponent; the entry. 

### `szTableBody`

 szTable(dst, p, J). 

### `tSzTable`

 An upper bound on the number of steps of szTable. 

### `szList_succ`

 One more entry of the table. 

### `SzInv`

 The state of szTable before round j: the entries p, …, 4^j p are written, the last of them is in
a local, and no cell outside the table has changed. 

### `szTable_spec`

 **szTable** writes p, 4p, …, 4^J p and changes nothing else. 

### `szTable_meets`

 **szTable** as a procedure. 
