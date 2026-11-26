---
{
  "module": "proof/rates/CountedRecursion/PolyAll.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyAll.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyAll.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The certificates, closed

`recursionPoly : RecursionPoly` and `recursionWithPoly : RecursionWithPoly`, from PolyEnd.lean, the
certificate of the procedure of the lemma on groupings up to its call (`groupingPoly`,
proof/rates/ExplicitCost/GroupingPoly.lean) and that of the tower (`Tower.towerPoly`,
proof/machines/Tower/PolyTower.lean). 

### `recursionPoly`

 **`RecursionPoly`**: the solver and the procedure have polynomial-time steps, one certificate
each for all levels. 

### `recursion_poly`

 The one machine for all levels has polynomial-time steps. 

### `recursionWithPoly`

 **`RecursionWithPoly`**: so has the machine with the algorithm of the pieces built in, and the
algorithm of the theorem. 
