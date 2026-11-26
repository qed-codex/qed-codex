---
{
  "module": "proof/rates/CountedRecursion/PolyEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The recursion has polynomial-time steps

`recursionPolyFrom : RecursionPolyFrom`: the tower of the solver and the procedure.
`recursionPoly_of`: `RecursionPoly` from the certificate of the procedure of the lemma on groupings
up to its call (the first half of `GroupingPoly`). `recursionWithPoly_of`: `RecursionWithPoly` from
the fact that `recursion c x₀` has polynomial-time steps for all `c x₀`. 

### `recursionPoly_of`

 `RecursionPoly`, given the certificate of `groupingCall`. 

### `recursionPolyFrom`

 `RecursionPolyFrom`. 

### `withAlgorithm_poly`

 A machine with the queries to the pieces answered by an algorithm with polynomial-time steps. 

### `recursionWithPoly_of`

 `RecursionWithPoly`, given that the recursion has polynomial-time steps. 

### `recursionWithPolyFrom`

 `RecursionWithPolyFrom`. 
