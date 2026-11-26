---
{
  "module": "proof/rates/ClauseBound/Alg/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The networks of one level on a grid with p rows and d columns, for any pieces

The interface statement `StGrid P` of proof/rates/ClauseBound/Alg/Interfaces.lean: the multiplier of
the pieces (the d of Definition 7, not the number of columns), raised to the power |R|, times the
sum Z of an instance on p·d nodes (p rows, d columns) is the sum of the terms of the patterns, and
for every pattern the plain functions `gridF P` present, with all rows merged and with all columns
merged, a network that has the value of the term, with its size, its total
and the bound on the bits that two parts share. The network is `gridN` of
proof/rates/ClauseBound/Alg/GridNet.lean. 

### `cutsOK_of_spec`

 What the networks use of the pieces follows from their specification, when the pad is long
enough. 

### `stGrid`

 The interface statement `StGrid` holds for all pieces `P`. 
