---
{
  "module": "proof/machines/Tower/Toy/Meets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Meets.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Toy/Meets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A toy recursion: the hypotheses of `TowerRuns` hold, and its conclusion

`toyMeets`: the two explicit machines meet the specification, so the hypotheses of `TowerRuns` are
not empty. `toyRuns`: ONE machine, on the input (ℓ, b), with query access to a table f at t
operations per query, returns the sum of f over all
bit strings of length ℓ within 2^ℓ·(t + 2ℓ + 5) operations; `toyPoly` (Toy/Machines.lean): that
machine has polynomial-time steps. 

### `size_start`

 The size of the solver's state at the start. 

### `size_one`

 With the first result. 

### `size_two`

 With both results. 

### `size_done`

 When it is done. 

### `oracle_call`

 A call one level down is answered by the sum over the strings that begin with the callee's bit. 

### `sol_within`

 The solver, with its calls and queries answered as specified, returns the value. 

### `inn_within`

 The procedure, with the caller's tables, returns the entries of the callee's tables. 

### `toyMeets`

 The two machines meet the specification. 

### `cost_toy`

 The recursion of the costs, solved. 

### `toyRuns`

 ONE machine, on the input (ℓ, b), with query access to a table f whose entries for the bit
strings of length ℓ are at most M0, at t operations per query: it returns the sum of f over all bit
strings of length ℓ within 2^ℓ·(t + 2ℓ + 5) operations. 
