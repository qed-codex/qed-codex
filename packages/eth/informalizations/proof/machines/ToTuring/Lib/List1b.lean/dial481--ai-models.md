---
{
  "module": "proof/machines/ToTuring/Lib/List1b.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List1b.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List1b.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for lists: heads and tails, flatten, zip, options, and equality of lists.
Every lemma tagged `fun_prop` says that the operation it is named after preserves `PolyT`. 

### `zipStep`

 One step of the zip: the state holds what is left of the second list and the pairs made so far,
last pair first. 

### `zipStep_poly`

 The step of the zip is polynomial-time. 

### `foldl_zipStep`

 What the fold of the step computes. 

### `zip`

 The zip is a fold of `zipStep`, then a reversal. 

### `eqStep`

 One step of the comparison of two lists: the state holds "equal so far" and what is left of the
second list. 

### `eqStep_poly`

 The step of the comparison is polynomial-time. 

### `foldl_eqStep`

 What the fold of the step computes. 

### `instance [DecidableEq β] [EqT β] : EqT (List β)`

 Equality of lists is polynomial-time if equality of their elements is: a fold of `eqStep`. 
