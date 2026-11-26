---
{
  "module": "proof/sparsification/StepSparsify/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/StepSparsify/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The walk that adds up, for arbitrary thresholds

This file proves `StWalkSG` of proof/sparsification/StepSparsify/Defs.lean.
`stWalkSG`: `walkSG`, which makes one round for each unit of the pad and cuts off states that are
too long, returns the sum of the values of the leaves if the pad is long enough, for any thresholds
θ;
the lemma `roundS_iterate_of_le` that the proof uses holds for every step function. 

### `stWalkSG`

 If the procedure has stopped at every node that is listed when the paths are cut after d steps,
the pad has at least 2·(number of these nodes) − 1 units and the word of every state of the walk
fits under the pad, then `walkSG` returns the sum of the
values of these nodes. 
