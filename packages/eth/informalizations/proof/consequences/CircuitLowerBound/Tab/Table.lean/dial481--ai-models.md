---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Table.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Table.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Table.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the conditions on the rows are the shifts of a table

`table N` lists, with atoms as kinds, a 3-literal clause for each condition of `Spec`; all its
shifts hold iff the conditions do (`spec_of_table`, `table_of_spec`). `stSpecTab` numbers the atoms. 

### `YLit`

 A literal with an atom as its kind. 

### `YCl`

 A clause of three such literals. 

### `holdsY`

 The literal holds in the shift by (t, q). 

### `HoldsC`

 The clause holds in all shifts. 

### `taut`

 A clause that always holds. 

### `en`

 The elements of a finite type as a list. 

### `fam`

 A family of clauses over a finite type as a list. 

### `table`

 The table, with atoms as kinds. 

### `spec_of_table`

 If all shifts of the clauses of the table hold, the conditions hold. 

### `table_of_spec`

 If the conditions hold, all shifts of the clauses of the table hold. 

### `table_dq`

 The numbers added to positions are at most 2d. 

### `num`

 The number of an atom: at least 1. 

### `nl`

 A literal with the number of its atom as kind. 

### `codeTab`

 The table with numbers as kinds. 

### `stSpecTab`

 The conditions are the shifts of a table. 
