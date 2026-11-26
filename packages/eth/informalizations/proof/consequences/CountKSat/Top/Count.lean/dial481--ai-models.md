---
{
  "module": "proof/consequences/CountKSat/Top/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Top/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/Top/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Facts for the program that counts the satisfying assignments of a k-CNF in c·2^{δn} steps
(decode the input, walk the sparsification tree depth-first, count
the satisfying assignments of every leaf, add the counts up, and write the sum as n + 1 bits): there
are at most 2ⁿ satisfying assignments, a formula with an
empty clause has none, and the output function `outW` writes the count as the n + 1 bits
`SatK.binary n v`. 

 ### The number of satisfying assignments 

### `numSat_le`

 There are at most 2ⁿ satisfying assignments. 

### `numSat_of_nil`

 A formula with an empty clause has no satisfying assignment. 

### `outW_eq`

 The output function `outW` of the machine writes the count v as the n + 1 bits `SatK.binary n v`
that the statement of #k-SAT asks for. 
