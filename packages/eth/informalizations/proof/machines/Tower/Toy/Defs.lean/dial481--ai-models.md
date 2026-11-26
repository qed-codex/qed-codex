---
{
  "module": "proof/machines/Tower/Toy/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A toy recursion: definitions and statements

Definitions and statements only; nothing is proved here. The toy shows that the hypotheses of
`TowerRuns` and `TowerPoly` can be met by explicit machines, with the depth as a part of the input.

F(0, f) = f(ε), F(ℓ+1, f) = F(ℓ, q ↦ f(0q)) + F(ℓ, q ↦ f(1q)): the sum of f over all bit strings of
length ℓ. A context is a pair (ℓ, b): the depth, and the bit that the instance puts in front of its
queries to the tables of its caller.
The solver on (0, b) asks its tables for the entry of the empty string. On (ℓ+1, b) it calls (ℓ, 0)
and (ℓ, 1), and adds the two results in one step of its own. The procedure on ((ℓ, b), q) asks the
tables of the caller for the entry of bq.
There is no query of the second kind. All ten functions are written with eliminators and, in two
places, «if», so that the tactic `fun_prop` proves the certificates as they stand.

The specification is chosen for an outermost instance of depth at most ℓ0 whose entries are at most
M0, as the comment on `Spec` allows. 

### `encEmpty`

 The empty type has nothing to write. The instance is active only where this namespace is open. 

 ### The two machines 

### `Ph`

 Where the solver stands: at the start; with the first result; with both results; done. 

### `solInit`

 The solver starts with the depth. 

### `solStep`

 Its one step of its own: the two results are added. 

### `solOut`

 Its result, when it is done. 

### `solAsk`

 At the start: at depth 0 the entry of the empty string, else the call of (ℓ − 1, 0). With the
first result: the call of (ℓ − 1, 1). 

### `solResume`

 How it goes on with an answer. 

### `Sol`

 The solver. 

### `innInit`

 The procedure starts with the bit of the callee and the callee's query. 

### `innOut`

 Its result, when it has the answer. 

### `innAsk`

 Its one query: the entry of bq in the tables of the caller. 

### `innResume`

 The answer is the result. 

### `Inn`

 The procedure. 

 ### The specification 

### `sumF`

 F(0, f) = f(ε), F(ℓ+1, f) = F(ℓ, q ↦ f(0q)) + F(ℓ, q ↦ f(1q)). A missing entry counts 0. 

### `words`

 All bit strings of length ℓ. 

### `spec`

 The specification, for outermost instances of depth at most ℓ0 with entries at most M0. 

### `TS`

 The cost of the solver: one query at depth 0; two calls and one step above. 

### `TI`

 The cost of the procedure: one query. 

### `SS`

 The bound on the sizes of the states of the solver. 

### `SI`

 The bound on the sizes of the states of the procedure. 

### `SC`

 The bound on the sizes of the contexts. 

### `noG`

 No query of the second kind: no answers. 

### `noW`

 No query of the second kind: no prices. 

 ### What is claimed 

### `ToyPoly`

 The tower of the toy has polynomial-time steps; the depth is part of its input. 

### `ToyMeets`

 The two machines meet the specification, so the hypotheses of `TowerRuns` are not empty. 

### `ToyRuns`

 ONE machine, on the input (ℓ, b), with query access to a table f whose entries for the bit
strings of length ℓ are at most M0, at t operations per query: it returns the sum of f over all bit
strings of length ℓ within 2^ℓ·(t + 2ℓ + 5) operations. 
