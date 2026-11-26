---
{
  "module": "Nc/WidePerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/WidePerm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/WidePerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Grid sums and sums of products of wide clauses as projections

A wide clause is a weight that applies when all literals of a list hold. A sum over bits of a product of wide
clauses is a grid sum, so it is a projection of every family that is complete for grid sums. Grid sums are
permanents if 2 ≠ 0.


### `wideSum`

 The sum over the hidden bits `a` of the product over the clauses: a clause contributes its weight when all
its literals hold, and 1 otherwise. 

### `mlExtC`

 The extension with weights `X i` (bit 1) and `1 - c * X i` (bit 0). 
