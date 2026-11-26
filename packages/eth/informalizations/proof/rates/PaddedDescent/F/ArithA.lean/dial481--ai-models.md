---
{
  "module": "proof/rates/PaddedDescent/F/ArithA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # `StA` and `StAW`: the pad of length 2^(8·(⌊n/2^(sOf n)⌋ + 1)) suffices for everything

`stA : StA` puts together the pieces of the arithmetic that do not know the width of the clauses,
for sOf n ≥ 1: the schedule is a chain; the pad suffices for the
rebalancing of a network of marks at the top and for the whole descent (`NetFits`), for the list of
profiles and for the word of the layers; the number of layers is
large enough (`MarkFits`); the pad suffices for the computation of the schedule. `stAW : StAW` has
what depends on the width k, for sOf n ≥ s0K k: the parameters are large
enough for width k, and the pad suffices for the rounds of the walk through the sparsification tree
and for its stack. No programs occur here: these are statements about
natural numbers. 

### `stA`

 The arithmetic that does not know the width. 

### `stAW`

 The arithmetic that knows the width. 
