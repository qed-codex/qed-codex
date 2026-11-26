---
{
  "module": "proof/machines/QueryMachines/Runs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Runs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Runs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Runs of machines with query access

Proofs of `StMono`, `StWithinRules`, `StUnique`, `StClose`, `StQueriesLe`, `StSlowDown`, `StSubst`,
`StPlug`, `StSubstWithin`, `StCloseSubst` (proof/machines/QueryMachines/Kernel.lean). Most rest on
one induction over a run of an arbitrary machine. 

 ## Bounds may be raised; the result and the queries are determined 

### `Reaches.mono`

 The bound on the own steps and the bound on the sizes may be raised; the list of queries stays. 

### `Runs.mono`

 The same for runs from the input. 

### `WithinFrom.mono`

 The cost and the bound on the sizes may be raised (from a state). 

### `Within.mono`

 The cost and the bound on the sizes may be raised. 

### `Reaches.unique`

 From one state and with one oracle, the result and the list of the queries are determined. 

### `sum_map_unitCost`

 At one operation per query, the queries of a list cost its length. 

### `sum_map_const`

 At t operations per query, the queries of a list cost its length times t. 

 ## The oracle built in 

### `close_step_none`

 With the oracle built in: a state that asks nothing makes its own step. 

### `close_step_some`

 With the oracle built in: a state that asks x goes on with the answer to x. 

### `close_step_stuck`

 With the oracle built in: a state that asks a query without an answer stays where it is. 

### `reaches_of_close`

 A run of the machine with the oracle built in is a run with query access; its steps are the own
steps and the queries. 

### `close_reaches`

 A run with query access is a run of the machine with the oracle built in; each query is one
step. 

 ## Queries answered by a machine 

### `subst_inner`

 The answering machine, run inside. 

### `subst_reaches`

 Queries answered by a machine with query access, from a state of the outer machine: own steps
add up, with two more for each query; the lists of queries of the answering runs are joined. 

### `subst_reaches_within`

 The same in costs: if the answer to x costs at most t x at the prices w', the whole costs at
most own + Σ (t x + 2). 

 ## Two step machines with the same states are equal if their parts agree 

### `stepped_eq`

 Two step machines with the same type of states and the same measure of size are equal if init,
step and out agree at every argument. 

### `close_subst`

 Building the outer oracle into a substitution is plugging in the answering machine with that
oracle built in. 

### `reaches_asksNothing`

 A step machine, seen as a machine that asks nothing, runs as it did. 

### `toStepped_reaches`

 A run without queries is a run of the step machine underneath. 

### `stMono`

 `StMono`. 

### `stUnique`

 `StUnique`. 

### `stWithinRules`

 `StWithinRules`. 

### `stClose`

 `StClose`: cost at one operation per query is the number of steps with the oracle built in. 

### `stQueriesLe`

 `StQueriesLe`: an algorithm that takes at most T operations makes at most T queries. 

### `stSlowDown`

 `StSlowDown`: at t ≥ 1 operations per query, T operations become at most T·t. 

### `stSubst`

 `StSubst`. 

### `stPlug`

 `StPlug`, as the case of `StSubst` in which the answering machine asks nothing. 

### `stSubstWithin`

 `StSubstWithin`. 

### `stCloseSubst`

 `StCloseSubst`. 
