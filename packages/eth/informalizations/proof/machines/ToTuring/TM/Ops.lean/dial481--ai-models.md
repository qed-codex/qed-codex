---
{
  "module": "proof/machines/ToTuring/TM/Ops.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Ops.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Ops.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The operations on the items on top of the main stack from which the fragments of Closure/ are
built, with bounds on their
numbers of steps: drop, duplicate, swap, make a pair, take a pair apart, push a constant,
park an item on stack a or b and fetch it back. The parking stacks are used above their contents and
left as they were. 

### `pushSeq`

 Push the symbols of a word on the main stack, one after the other. 

### `pushW`

 Push a fixed word: afterwards it lies on top of the main stack, its first symbol on top. 

### `pop1`

 Pop one symbol off the main stack and forget it. 

### `dropF`

 Drop the item on top. 

### `dupF`

 Duplicate the item on top. 

### `swapF`

 Exchange the two items on top. 

### `consF`

 The two items on top become one: their pair. 

### `unconsF`

 A pair on top becomes its two items. 

### `stepAux_pushSeq`

 What the pushing statement does: the word arrives reversed. 

### `toA_within`

 Park the item on top of main on stack a (mirrored). 

### `toB_within`

 Park the item on top of main on stack b (mirrored). 

### `fromA_within`

 Fetch an item back from stack a. 

### `fromB_within`

 Fetch an item back from stack b. 
