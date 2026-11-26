---
{
  "module": "proof/sparsification/SparsificationLemma/Shrink.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Shrink.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Shrink.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Neither child has more clauses than its parent

This file proves `Shrink.card_light_le` and `Shrink.card_heavy_le` on finite sets, and
`Shrink.length_step_le`, the same for the lists of `stepC`.
The first child is H together with the clauses of F that do not contain H (`stLightEq`), and at
least θ(j−|H|) ≥ 1 clauses of F contain H: one clause comes, at least one goes.
The second child is the sets E ∖ H together with the clauses of F that contain none of them
(`stHeavyEq`). There are at most as many sets E ∖ H as clauses E, and every E goes, since it
contains E ∖ H.
On lists: a formula in normal form has as many clauses as its set of clauses has members, and
`stepC` computes the two children (`stRefines`). 

### `card_light_le`

 The first child has at most as many clauses as F. 

### `card_heavy_le`

 The second child has at most as many clauses as F. 

### `length_step_le`

 On lists: for thresholds at least 1, if x.1 is in normal form and none of its clauses contains
another, the formulas of both children of x have at most as many clauses as x.1. 
