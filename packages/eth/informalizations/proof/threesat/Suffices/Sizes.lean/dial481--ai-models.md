---
{
  "module": "proof/threesat/Suffices/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Suffices/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sizes

What lines 1 to 4 of Algorithm 1 keep in memory has size polynomial in N, the length of the input
plus 1: a formula with at most m clauses of at most 3 literals, a node (ψ, 𝒩) of the recursion tree
of the sparsification algorithm in the proof sketch of Theorem C (Appendix C), the stack of the
walk.
The counts follow the size part of `Groundwork.Prog.SatTopK.sat_correct`, here for nodes with a side
list. Also here: `tested` under a map (line 2 of Algorithm 1): the formulas tested are the outputs
of the leaves tested. 

### `tested_map`

 The entries of a mapped list that are tested are the images of the entries tested by the
composed test. 

### `length_tested_le`

 No more entries are tested than there are. 

### `size_clauses_le`

 A formula of at most m clauses of at most 3 literals on variables below n ≤ N has size at most
14·m·N + 1. 

### `size_node_le`

 A node (ψ, 𝒩) within the bounds of `Enumerate.Enumerates.stack` has size at most 142·N². 

### `size_stack_le`

 A stack of at most D·n + 1 such nodes has size at most (143·(D + 1) + 1)·N³. 

### `loop_bound`

 The bound on the stack, plus 4, is at most c·N^c for c = 143·(D + 1) + 5. 

### `size_input_le`

 The input as it is held after decoding, (1ⁿ, ψ) with at most N clauses, has size at most 18·N². 

### `size_sparse_le`

 A formula of at most M·n clauses, together with n, has size at most (14·M + 2)·N². 

### `main_bound`

 For c = c₁ + A·(14M + 2)^A + 2A + c₂ + 22: the bound on the states of the loop plus that on the
states of the machine for sparse formulas, and 20·N², are each at most c·N^c (used in
`stSufficesOf`). 
