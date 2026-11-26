---
{
  "module": "proof/machines/ToTuring/Lib/Table.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Table.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/Table.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time: tables. Every function on a finite type whose equality can be tested is
polynomial-time, because it is a
finite chain of tests "is the argument this element?" with constant answers. `table₁`, `table₂`,
`table₃` take one to three
arguments; `table₃` serves, for instance, for functions of a few Booleans. 

### `lookup`

 The table of F on the elements of the list l, read from the left; d is the answer when the
argument is not in l. 

### `lookup_eq`

 On the elements of the list the table gives F. 

### `lookup_polyT`

 Reading a table is polynomial-time: the list is fixed, so this is a fixed chain of tests. 

### `table`

 Every function on a finite type with a polynomial-time equality test is polynomial-time. 

### `table₁`

 A table after a polynomial-time argument. 

### `table₂`

 A table with two arguments. 

### `table₃`

 A table with three arguments. 
