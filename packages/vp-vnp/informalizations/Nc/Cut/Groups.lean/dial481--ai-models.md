---
{
  "module": "Nc/Cut/Groups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Groups.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cut/Groups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Groups of parties

The value of a position whose joint weight is a product of tables of the parties is a sum, over common contents of
the current units whose holders are in different groups, of products of values of the groups.


### `cutUnits`

 The current units whose holders are in different groups. 

### `GContents`

 The contents of the copies held by the parties of the group `g`: only seen units, at their holders in `g`, are
not empty. 

### `GAgree`

 The copies of current units agree if both holders are in the group `g`, and they are `b` if one is. 

### `groupVal`

 The value of the group `g` for the contents `b` of the units shared with other groups. 

### `posVal_groups`

 **Groups.** 

### `posVal_move'`

 **One move**, for contents at which the joint weight is not zero. 
