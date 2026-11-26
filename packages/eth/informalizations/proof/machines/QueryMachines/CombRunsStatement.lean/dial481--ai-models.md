---
{
  "module": "proof/machines/QueryMachines/CombRunsStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombRunsStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombRunsStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # How the constructions run (statements only)

For ten constructions of proof/machines/QueryMachines/CombDefs.lean (lift, query, mapAsk, mapIn,
mapOut, bind, both, branch, foldWhile, foldRange): the run of the whole from the runs of the parts.
ite, const, optBind, sumRange, prodRange and gated are made from these.
For mapIn, mapOut, bind, both, branch, foldWhile and foldRange, own steps and sizes are those of the
lemma of the same name for step machines (proof/machines/StepMachines/Prog/Stepped.lean,
proof/machines/StepMachines/Prog/Comb.lean, proof/machines/StepMachines/Prog/Range.lean). lift keeps
the run of the step machine. query has the size bound of `ofFun_runs` and no own step. mapAsk keeps
the run with each query rewritten. The lists of queries are joined in the order of the runs. All
bounds are explicit.
The main text does not need these (it goes through `close`); they serve programs whose queries must
be told apart, as in Appendices A, B and D. This file has no proofs. 

### `StLiftRuns`

 A step machine asks nothing. 

### `StQueryRuns`

 One query, no own step. 

### `StMapAskRuns`

 Queries rewritten by h: the list of queries is mapped by h. 

### `StMapInRuns`

 A function applied to the input: the run is that of M. 

### `StMapOutRuns`

 A function applied to the result: the run is that of M. 

### `StBindRuns`

 M, then N: own steps add up, with one more for the hand-over; first the queries of M, then those
of N. 

### `StBothRuns`

 M, then N, on one input: as for `bind`. 

### `StBranchRuns`

 A choice: the run is that of the machine chosen; the size bound is one larger. 

### `StFoldWhileRuns`

 The loop: own steps Σ over the orbit of (own steps of the body + 1); the queries of the rounds
one after the other; the result is the fold over the orbit. 

### `StFoldRangeRuns`

 The loop over y < N a; the range is a function of the input. 
