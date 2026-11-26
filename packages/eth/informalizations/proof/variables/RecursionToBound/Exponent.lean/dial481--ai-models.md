---
{
  "module": "proof/variables/RecursionToBound/Exponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Exponent.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Exponent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the walk, and the whole exponent

* `walkCost`: the exponent of the walk is ⌈εn⌉ + 2 plus the number of binary digits of the bound on
  the stack. That bound is a product of (32α)^(2k), of powers of n and 2 with exponents O(k), and of
  k; the number of binary digits of a product or a sum is at most the sum of those of its parts
  (`size_stack_le`, `size_inLen_le`). With 32α ≤ (8k/ε)³
  (`SparsificationLemma.Cal.StAlphaLe`) this gives εn + 29·k·(log n + log(8k/ε)).
* `exponentIsWithinTheBound`: the bound of Step 5 of Appendix D, 2^(2en)·n^{O(k)}·2^{O(ekn·log Δ)} =
  2^{O(k²·e·n·log(k/e))}. With w = log(k/e) ≥ 1 and X = k²·e·n·w, every Δ in the list has log Δ ≤
  3k·log(8k/e) + 2 ≤ 14·k·w
  (`outputsAreWithinTheSetting`), so one output costs at most 14·A·X (`oneOutputCost`). The walk
  costs at most 2en + c·k·log n + 4c·k·w ≤ (2 + 5c)·X, because k·log n ≤ en
  (`MainTheoremForms.StepSparsifyLargeStmt`), en ≤ X and k·w ≤ X. 

 ### The walk 

### `size_inLen_le`

 The number of binary digits of the bound on the number of clauses of the input: at most k·s + 4k +
s + 5, s the number of binary digits of n. 

### `size_stack_le`

 The number of binary digits of the bound on the stack of the walk, for a formula of at most m
clauses. 

### `walkCost`

 Step 5: the sparsification «produces at most 2^(εn) outputs in time 2^(εn)·n^{O(k)}» (Appendix
D); here with an extra factor (8k/ε)^{O(k)}: the exponent for the walk is at most εn + 29·k·(log n +
log(8k/ε)). 

 ### The whole exponent 

### `foldr_max_zero_le`

 A maximum over a list of natural numbers is at most b if every member is. 

### `of_mem_deltas`

 The numbers in the list of the Δ are at least 2 and at most the bound on the occurrences. 

### `exponentIsWithinTheBound`

 «The time is 2^(2en)·n^{O(k)}·2^{O(ekn·log Δ)} = 2^{O(k²·e·n·log(k/e))}, because k·log n ≤ en
for large n» (Step 5 of Appendix D): the exponent of the padding string where there is a plan is at
most A·k²·e_ℓ·n·log(k/e_ℓ). 
