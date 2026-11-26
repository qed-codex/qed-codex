---
{
  "module": "proof/networks/Groundwork/Grid/RowNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/RowNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Grid/RowNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion, with all rows merged (the row network in the proof of Proposition 3):
for any factorisation of the functions at the rectangles, the row
network has the value ZG. 

### `ZG_eq_rows`

 Regrouping the half-edges by the row of their source. 

### `prod_eq_factorised`

 An equality factors through the common value; for a family. 

### `rowΨ_eq`

 The interaction of two rows is factorised by rowTop and rowBot over rowΘ. 

### `rowNet_Ψ`

 The interaction of the row network is rowΨ. 

### `value_rowNet`

 The row network has the value ZG. 
