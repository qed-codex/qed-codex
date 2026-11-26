---
{
  "module": "Nc/Grp/RoleProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/RoleProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/RoleProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The program of a role: the loop


### `we`

 A formula for an element of the ring. 

### `slList`

 Slots of a role, as a list. 

### `cnList`

 Channels of a role, as a list. 

### `slIdx`

 The number of a slot. 

### `roleTab`

 The transducer of a role. 

### `yardF`

 The yardstick: argument (yardstick `num ub`, (trie, (num t, …))). 

### `roleSem`

 What a role does with a trie with the contents `ct`. 

### `roleEnd`

 The last part: argument ((yardstick, (trie, (num t, (slots, keys)))), state of the transducer). 

### `ex_role`

 **The program of a role.** 
