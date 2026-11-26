---
{
  "module": "proof/rates/CountedRecursion/Meets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Meets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Meets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver and the procedure meet the specification

`Tower.Spec.Meets` indexes the costs by the depth alone, while the label length of a callee depends
on the pattern. So the statements on one instance (`SolverBase`, `SolverStep`, `ProcedureCost`,
`ChildIsGood`) are taken at the bounds Λ_j, 𝔅_j that λ and B obey along the recursion from one
outermost instance (`boundsDown`): every bound grows with λ and B.
* `lamAt_step`, `bitsAt_step`: the bounds of the depth j from those of the depth j + 1.
* `bitsOne_mono`, `bitsOut_mono`, `askCost_mono`, `Xi_mono`: monotonicity.
* `room_term_le`: (K_i(λ' + B'))^{C'} is within `roomAll`, for an instance of the depth i within the
  bounds.
* `child_inBounds`: a callee is within the bounds.
* `recursionMeetsFrom`. 

### `lamAt_step`

 Λ_j from Λ_{j+1}. 

### `bitsAt_step`

 𝔅_j from Λ_{j+1} and 𝔅_{j+1}. 

### `bitsOne_mono`

 B₁ grows with λ and B. 

### `bitsOut_mono`

 B' grows with P and B₁. 

### `askCost_mono`

 The price of a query to the pieces grows with λ. 

### `Xi_mono`

 Ξ grows with λ and B. 

### `Xi_eq`

 Ξ = K_{j+1}(λ + B). 

### `room_term_le`

 A power of K_i(λ' + B'), for λ' and B' within the bounds of the depth i ≤ ℓ, is within the room
for all depths. 

### `lamAt_le_max`

 Λ_i is at most the largest label length. 

### `child_inBounds`

 A callee of an instance within the bounds is within the bounds. 

### `recursionMeetsFrom`

 **The solver and the procedure meet the specification.** From the statements on one instance
(`SolverBase`, `SolverStep`, `ProcedureCost`, `ChildIsGood`), taken at the bounds Λ_j, 𝔅_j, the
solver and the procedure meet `Tower.Spec.Meets`, with costs that depend on the depth alone. 
