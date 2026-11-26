---
{
  "module": "proof/consequences/CountKSatRate/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The walk that adds up, in rounds

`proof/machines/StepMachines/Math/SparsifyTree.lean` walks the tree of a step function depth first,
in rounds: `round` lists the leaves, `roundB` keeps only whether some leaf passed a
test. `roundS` keeps only the sum of the values of the leaves. This file shows that `roundS` follows
`round`, that the sum is complete once the stack is empty, and that
`walkS`, which makes one round for each unit of the pad and cuts off states that are too long,
returns the sum over the leaves if the pad is long enough. The last proof
is that of `walk` in `proof/rates/PaddedDescent/F/Top.lean`. 

### `roundS_iterate`

 The state of the summing walk after i rounds: the stack of the plain walk, and the sum of the
values of the leaves that the plain walk has listed. 

### `roundS_iterate_of_le`

 After at least 2·(number of leaves) − 1 rounds the stack is empty and the number is the sum of
the values of the leaves. 

 ### The interface statements of `proof/consequences/CountKSatRate/Interfaces.lean` that this file proves 

### `stRoundS`

 `roundS_iterate`, as the interface states it. 

### `stRoundSEnd`

 `roundS_iterate_of_le`, as the interface states it. 

### `stWalkS`

 If the pad has at least 2·(number of leaves) − 1 units and the word of every state of the walk
fits under the pad, then `walkS` returns the sum of the values of the leaves. 
