---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Pack.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Pack.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Pack.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): triples (kind, time, position) and numbers of variables

`stPack`: the formula of a table, whose variables are numbers, is satisfiable if and only if the
clauses of the table, read with triples as variables, are satisfiable in all shifts. The number of a
triple determines the triple, the numbers of the
clauses are the triples (place in the table, t, q), and the places beyond the end of the table only
say that the variable 0, which is no triple of the table, is false. 

### `vidx_eq`

 The number of a variable of the table, without reductions. 

### `clauseAt_pack`

 The number of the clause at the place r of the table in the shift (t, q). 

### `exists_pack`

 Every number of a clause is of this form. 

### `stPack`

 Triples and numbers of variables. 
