---
{
  "module": "proof/networks/Groundwork/Grid/Expand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Expand.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/Expand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion, as identities: transposing the grid, which exchanges rows and
columns, does not change the sum;
and the value with the crossing on every rectangle is the sum over ι of the terms Z_ι. 

### `trHalf`

 Transposing a half-edge labelling: the coordinates of both nodes are exchanged. 

### `filter_mem_Ω`

 The rectangles, as the subset of all ω that lie in Ω. 

### `ZG_tr`

 Transposing the grid does not change the sum. 

### `ZG_cross_eq_sum`

 The value with the crossing `Cross.X` on every rectangle is the sum over ι of the terms Z_ι. 
