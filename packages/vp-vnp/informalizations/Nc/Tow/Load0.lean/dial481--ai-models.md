---
{
  "module": "Nc/Tow/Load0.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Load0.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Load0.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tower plan: the loads after the start


### `Bt`

 The number of units of a batch. 

### `steps_le`

 The steps of a path on an edge. 

### `load_start_le`

 The load of an edge after the start. 

### `batch_le`

 The batches on an edge. 

### `_root_.Paper.thm_tree_start`

 **Paper: Theorem thm:tree, Start.** "Every edge gets at most n₀ = 4L(N+M²) units": every edge of X^(0) gets at
most Uu (N/|X^(0)| + 2AA), where Uu ≤ 2|X^(0)|L bounds the routes through an edge (printed form: thm_tree_start_units). 
