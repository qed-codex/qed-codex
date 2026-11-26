---
{
  "module": "proof/machines/QueryMachines/CombRuns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombRuns.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombRuns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # How the constructions run

Proofs of the statements of proof/machines/QueryMachines/CombRunsStatement.lean. Each follows the
corresponding proof for step machines (`Stepped`), with the list of queries carried along. 

### `lift_reaches`

 A step machine asks nothing (from a state). 

### `mapAsk_reaches`

 Queries rewritten by h (from a state). 

### `mapIn_reaches`

 A function applied to the input (from a state). 

### `mapOut_reaches`

 A function applied to the result (from a state). 

### `bind_reaches_inr`

 The second machine of `bind`, run inside. 

### `bind_reaches`

 `bind`, from a state of the first machine. 

### `both_reaches_inr`

 The second machine of `both`, run inside. 

### `both_reaches`

 `both`, from a state of the first machine. 

### `branch_reaches_inl`

 The left machine of `branch`, run inside. 

### `branch_reaches_inr`

 The right machine of `branch`, run inside. 

### `foldWhile_body`

 The body, run inside the loop. 

### `foldWhile_reaches`

 The loop, from the state with accumulator c and next point o. 

### `orbit_range`

 The points of the loop over y < N a. 

### `sum_map_range`

 A sum over a list of numbers 0, …, n − 1 as a sum over a range. 

### `foldRange_runs`

 The loop over a range. 

### `stLiftRuns`

 `StLiftRuns`. 

### `stQueryRuns`

 `StQueryRuns`. 

### `stMapAskRuns`

 `StMapAskRuns`. 

### `stMapInRuns`

 `StMapInRuns`. 

### `stMapOutRuns`

 `StMapOutRuns`. 

### `stBindRuns`

 `StBindRuns`. 

### `stBothRuns`

 `StBothRuns`. 

### `stBranchRuns`

 `StBranchRuns`. 

### `stFoldWhileRuns`

 `StFoldWhileRuns`. 

### `stFoldRangeRuns`

 `StFoldRangeRuns`. 
