---
{
  "module": "Nc/G/Move.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/Move.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/G/Move.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The identity of one move, for general laws


### `slotBits_eq_iff`

 Two copies of a slot agree if the units do. 

### `role_congr`

 The role depends on the units given and on the new units at its channels only. 

### `role_new_ne_none`

 The roles at the ends of a channel force its new units to be present. 

### `chCode`

 The code word of the string on a channel: its first `U1` units. 

### `Law.Le`

 A bound for the lengths of the strings of a law. 

### `outTab`

 The table of the law for an outcome; `X p k e` are the bits. 

### `sum_outTab`

 Tables with code words, summed over all outcomes. 

### `sum_codeTab_zero`

 Impossible outcomes contribute nothing. 

### `role_eq_codeTab`

 The role as a table with code words. 

### `upd`

 Set the outcome of move `x`. 

### `move_outcome`

 One outcome of a move, as a sum over code words. 

### `move_identity`

 **The identity of one move.** 

### `move_zero`

 Impossible outcomes of a move contribute nothing. 
