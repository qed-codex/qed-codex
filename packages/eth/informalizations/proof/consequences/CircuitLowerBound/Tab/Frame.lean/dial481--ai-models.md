---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Frame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Frame.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Frame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # For the circuit lower bound for E^NP (Section 7): one step of a multi-stack machine sees and changes only the tops of the stacks

`stepAux_frame`: a statement with at most d stack operations, run on stacks A k ++ R k with A k of
length at least d (or R k empty), does to the A k what it does to them alone, and leaves the R k
alone. `stay_eq`: the step of the machine
(a halted machine stays as it is) written with the case of the configuration. `stay_of_evals`,
`evals_of_stay`: runs of Mathlib's step function and runs of the step function that stays. 

### `stepAux_frame`

 What lies below the top d symbols is neither seen nor changed. 

### `length_stepAux_le`

 A statement with d stack operations makes a stack longer by at most d. 

 ### Cells 

### `pref_ofFn`

 The first d cells of a stack give back its top d symbols. 

### `getElem`

 In a list of cells in which a blank is followed by blanks only, the symbols up to the first
blank have the cells as their entries. 

 ### The step that stays 

### `caseOf`

 The case of a configuration. 

### `stay`

 One step; a halted machine stays as it is. 

### `stay_eq`

 The step, written with the case of the configuration. 

### `length_nxt_le`

 The new top of a stack has at most 2d symbols. 

### `stay_of_evals`

 A run of n steps of Mathlib's step function is a run of the step that stays. 

### `evals_of_stay`

 What the step that stays reaches in T steps, Mathlib's step function reaches in at most T steps. 
