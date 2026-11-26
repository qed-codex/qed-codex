---
{
  "module": "proof/consequences/SplitCount/Leaf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Leaf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Leaf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6: one leaf, and the stack
`leaf_runs` (the width reduction of the proof of Corollary 6, `stStepThree`, then a procedure D that
counts for 3-CNFs): at a leaf with at most Bl·n clauses of at most max(k, 2) literals on x₀ … xₙ₋₁,
this returns the number of satisfying assignments of the leaf on n variables, within A·2^{(δ/3)n}
steps if δ'·(1 + 3(max(k,3) − 3))·(Bl + 1) ≤ δ/3:
«The constants in O(n) depend on k and ε, so choosing ε = δ/3 first and then applying Theorem 2 with
a small enough value in place of δ gives time O(2^{δn}).»
`stack_size`: the stack of the walk has size polynomial in a number M that bounds n and the number
of clauses of the input. 

### `leafConst`

 The constant in the bound on the states of D at a leaf. 

### `leaf_size`

 The size of the input of D at a leaf: from n₃ ≤ n + q·m, m₃ ≤ m + 3q·m, m ≤ Bl·n and n ≤ M. 

### `leaf_runs`

 **One leaf.** Let D count for 3-CNFs (proof of Corollary 6, first sentence) with exponent δ' ≥ 0
and constant A, let δ'·(1 + 3(max(k,3) − 3))·(Bl + 1) ≤ δ/3, and let the node x carry n in unary and
have at most Bl·n clauses
of at most max(k, 2) literals on x₀ … xₙ₋₁. Then the width reduction followed by D returns its
number of satisfying assignments on n variables within ⌊A·2^{(δ/3)n}⌋ steps, on states of size ≤
A·(`leafConst k Bl`·M²)^A, for all M ≥ 1 with n ≤ M. 

### `stackConst`

 The constant in the bound on the size of the stack. 

### `clause_bound`

 A clause of at most w literals on variables below n ≤ M: the bound of `size_fml_le` for one
clause is at most (4w + 2)·M. 

### `stack_size`

 **The stack.** A stack of at most Dd·n + 1 nodes, each of which carries n in unary and has at
most (m + n)·Sk clauses of at most max(k, 2) literals on x₀ … xₙ₋₁, has size at most
`stackConst k Dd Sk`·M³, for every M ≥ 1 with n ≤ M and m ≤ M. 
