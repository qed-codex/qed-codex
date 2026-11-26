---
{
  "module": "proof/machines/Tower/Cost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Cost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Cost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The recursion `cost`

It is monotone in the cost of a query if the costs of the solver and of the procedure are
(`costMono`); for costs of the shape own + calls·tc + queries·tq and own' + q'·t it is written out
for these shapes (`costShape`), and queries that cost x times as much make the whole cost at most x
times as much (`costSlowDown`). 

### `costMono`

 Dearer queries make the tower dearer, if they make the solver and the procedure dearer. 

### `shapeS_mono`

 The shape of the solver's cost is monotone in the two prices. 

### `shapeI_mono`

 The shape of the procedure's cost is monotone in the price. 

### `costShape`

 The recursion written out for these shapes. 

### `costSlowDown`

 For these shapes, queries that cost x times as much make the whole cost at most x times as much. 
