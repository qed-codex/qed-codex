---
{
  "module": "Nc/Grp/GrpSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/GrpSteps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/GrpSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The value of a group as a sum over executions

Steps: the base parties of the group (blocks and input parties) write their initial units, then the roles, in the
order of the moves, write the new units.


### `isInit`

 Is it an initial unit? 

### `isNewOf`

 Is it a unit made by the move `x`? 

### `Cell`

 Cells. 

### `dom`

 The cells of the group. 

### `initV`

 Contents of initial units. 

### `InitC`

 The conditions on what a base party writes and reads. 

### `baseStep`

 The step of a base party. 

### `Bk`

 What a role chooses in a block. 

### `chS`

 The string of a channel. 

### `roleV`

 The contents that a role writes. 

### `roleStep`

 The step of a role. 

### `baseList`

 The base parties of the group. 

### `allRoles`

 All roles, in the order of the moves. 

### `roleList`

 The roles of the group. 

### `steps`

 The steps of a group. 

### `exists_role`

 A cell of a new unit is written by a role. 

### `exists_cnAt`

 The channels of a role. 

### `wrs_steps`

 **All cells of the group are written.** 

### `seq_steps`

 **The steps of a group are a sequence.** 
