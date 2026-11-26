---
{
  "module": "proof/sparsification/SparsificationLemma/Len.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Len.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Len.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The number of clauses of a k-CNF in which every variable occurs in few clauses

This file proves `StLenOfOcc`, with the list lemma `length_le_sum_countP`: a k-CNF on n variables in
which every variable occurs in at most Δ clauses has at most Δ·n clauses.
`StLenOfOcc`: every clause has a variable v < n, so it is counted in the number of occurrences of at
least one v < n. Hence the number of clauses is at most the sum of these n numbers, each of which is
at most Δ. 

### `length_le_sum_countP`

 If every member of a list has one of the properties p 0, …, p (n−1), the length of the list is
at most the sum over v < n of the number of members with the property p v. 

### `stLenOfOcc`

 A k-CNF on n variables in which every variable occurs in at most Δ clauses has at most Δ·n
clauses. 
