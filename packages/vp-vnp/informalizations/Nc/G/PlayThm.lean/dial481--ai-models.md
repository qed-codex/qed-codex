---
{
  "module": "Nc/G/PlayThm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/PlayThm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/PlayThm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The play, for general laws


### `mem_seenAt_end`

 The units seen in the end. 

### `tabUpTo`

 The joint weight before move `x`. 

### `tabUpTo_ne_none`

 Units that are present if the joint weight is not zero. 

### `tabUpTo_congr`

 The joint weight before move `x` does not depend on the copies of later units. 

### `outSet`

 The units given in a move. 

### `_root_.Paper.thm_tree_move`

 **Paper: Units.** "Each choice of indices and bits occurs for exactly one outcome, so the value does not change":
one move, as a sum over outcomes that are good. 

### `_root_.Paper.thm_tree_moves`

 **Paper: Units.** "Every possible outcome is good ...; so the sum may be restricted to good outcomes": a whole plan
of moves keeps the value. 
