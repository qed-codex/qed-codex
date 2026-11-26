---
{
  "module": "proof/rates/PaddedDescent/F/Expand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Expand.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Expand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One level (StE)

The children of an instance on g·g nodes have Z summing to its Z (the sum of the Z_ι over all ι, by
`ZW_eq_sum`), they are well-formed, and there are at most
(Λ+1)^R of them, where R = `nRect` of the side g is the number of rectangles of the g×g grid and Λ
is a given bound on the t of the pieces A_0, …, A_t. 

### `filterMap_spec`

 A filterMap all of whose values are `some`. 

### `stE`

 `StE`, one level of the recursion: the children of an instance on g·g nodes are well-formed,
their Z sum to its Z, and there are at most (Λ+1)^R of them (R and Λ as in the module docstring). 
