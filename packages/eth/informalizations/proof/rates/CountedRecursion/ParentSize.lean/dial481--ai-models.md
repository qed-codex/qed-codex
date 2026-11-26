---
{
  "module": "proof/rates/CountedRecursion/ParentSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ParentSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ParentSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The size of a parent

The procedure that computes an entry of a callee's tables keeps the parent (K, g, λ, B, the lists 𝓘,
c^row_i, c^col_i, the direction, the numbers y of the pattern and x of the grouping) in all its
states. `size_mkParent_le`: its size is at most Ξ^{2c+4}, Ξ = g²(λ + B). By Definition 7 (c) the
list of 𝓘 has at most (2λ)^c elements of at most (2λ)^c bits;
c^row_i, c^col_i ≤ 2λ; y < |𝓘|^{|ℛ|} has at most (2λ)^c·g⁴ bits and x < K^g at most g² bits. 

### `size_list_bound`

 The size of a list of at most k elements of size at most s. 

### `size_unary_eq`

 The size of n in unary. 

### `size_nat_of_lt`

 A number below 2^k has size at most k + 1. 

### `size_listsOf_le`

 The three lists: at most (2λ)^c elements each; an element of 𝓘 has at most (2λ)^c bits, and
c^row_i, c^col_i ≤ 2λ. 

### `parent_arith`

 The arithmetic: with X = g²(λ + B) ≥ 8 and m = (2λ)^c ≤ X^c. 

### `size_mkParent_le`

 **The size of a parent** is at most Ξ^{2c+4}. 
