---
{
  "module": "proof/machines/StepMachines/Prog/CutProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/CutProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/CutProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One rectangle as a procedure: the part of the cut of the piece A_i on one side, evaluated
literally. The top part is
a loop over the λ positions; the bottom part a loop over all 2^λ sets of positions, with a loop over
the positions inside.
The input holds all that is needed and nothing of the grid; λ is the length of the word x. 

### `CutQ`

 ((top?, i), (x, y, w)): the side, the number i of A_i, the words of the two ends on this side,
the name of the label
(one value of the index summed over across the cut). 

### `cutLen`

 λ, the length of the word x. 

### `cutValid`

 Does w name a label? 

### `cutTop`

 Is the top part asked for? 

### `topE`

 One factor of the top part; the input comes with the counter of the loop over the positions. 

### `cutPow`

 The number 2^λ of sets of positions. 

### `cutPop`

 Does the set of positions encoded by the counter have exactly i elements? 

### `cutLen'`

 λ again, inside the loop over the sets. 

### `botE`

 One factor of the bottom part; the input comes with the two loop counters: the set of positions,
then the position. 

### `cutP`

 The part of the cut on one side. 
