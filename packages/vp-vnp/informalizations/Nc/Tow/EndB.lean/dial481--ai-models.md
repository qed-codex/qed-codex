---
{
  "module": "Nc/Tow/EndB.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/EndB.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/EndB.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tower plan: units between a node and its parent


### `parN`

 The parent of a chamber, as a node. 

### `chd`

 The chamber below: which end of the edge of a relay. 

### `done_hold`

 A chamber and its parent hold the units of a channel without target. 

### `sum_le_one`

 A sum over at most one element. 

### `IsCh`

 The channel is between the chamber `s` and its parent. 

### `OfEd`

 The relay belongs to an edge. 

### `ofEd_unique`

 At most one channel of an edge and an end has alive units. 

### `sum_edge_end`

 The alive units of an edge at one end. 

### `sum_child_lt`

 The alive units between a chamber of a level before the last and its parent. 

### `sum_child_last`

 The alive units between a chamber of the last level and the root. 

### `sum_child`

 **The alive units between a chamber and its parent.** 
