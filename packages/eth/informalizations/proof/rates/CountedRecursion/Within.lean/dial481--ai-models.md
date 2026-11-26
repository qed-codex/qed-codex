---
{
  "module": "proof/rates/CountedRecursion/Within.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Within.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Within.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The cost of a machine from the costs of its parts

The run statements of the machines with query access
(proof/machines/QueryMachines/CombRunsStatement.lean) give, for each way to build such a machine,
the own steps and the LIST of the queries of the whole from those of the parts. Here the same in
costs (`QueryMachine.Within`: own steps plus the prices of the queries asked), for any prices w: one
lemma for each construction.
Counting one operation for each query would not give a bound for every price of a query (for example
the price 0). So these lemmas count own steps and the prices of the queries separately, and the
lists are never named. 

### `lift_within`

 A step machine asks nothing. 

### `query_within`

 One query: its price. 

### `mapIn_within`

 A function applied to the input. 

### `mapOut_within`

 A function applied to the result. 

### `mapAsk_within`

 Queries rewritten by h: oracle and prices are read through h. 

### `readAs_within`

 Answers read by r. 

### `branch_within_inl`

 A choice, first machine. 

### `branch_within_inr`

 A choice, second machine. 

### `ite_within_true`

 M if p a. 

### `ite_within_false`

 N if not p a. 

### `bind_within`

 M, then N: the costs add up, with one more step for the hand-over. 

### `sum_map_flatMap_range`

 The prices of the queries of all rounds. 

### `foldRange_within`

 The loop over y < N a: the costs of the rounds add up, with one more step for each round. 

### `sumRange_within`

 Σ_{y < N a} M(a, y); V bounds every |v y|. 

### `prodRange_within`

 ∏_{y < N a} M(a, y); V ≥ 1 bounds every |v y|. 
