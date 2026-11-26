---
{
  "module": "proof/rates/CountedRecursion/EndCounted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndCounted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndCounted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (b) with the pieces as a priced oracle that is asked only about strings of at most Λ bits, from the steps

* `top_inBounds`, `top_fits`: the outermost instance (ℓ, λ, B) with its tables is a well-formed
  instance of the specification, within its own bounds.
* `recursionCountedUpToFrom : RecursionCountedUpToFrom`: the solver and the procedure meet the
  specification (`RecursionMeets`), so the tower returns the value at the cost of the recursion
  (`QueryMachines.Tower.TowerRuns`), which is within the bound of the theorem (`TotalCount`), on
  states within the bound on the sizes (`TotalRoom`). The value of the clique reads the tables only
  on settings (`clique_readTables`). 

### `cLev_top`

 The level of the outermost instance. 

### `cLam_top`

 Its label length. 

### `cB_top`

 Its bound on the bits of the tables. 

### `top_inBounds`

 The outermost instance is within the bounds that hold along the recursion from it. 

### `top_fits`

 The outermost instance with its tables is «the (K_ℓ, λ)-clique with |W_w| < 2^B». 

### `recursionCountedUpToFrom`

 **How the steps give the theorem**, with the pieces asked only about strings of at most Λ bits. 
