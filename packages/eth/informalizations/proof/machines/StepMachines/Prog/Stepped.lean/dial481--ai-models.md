---
{
  "module": "proof/machines/StepMachines/Prog/Stepped.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Stepped.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Stepped.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Computations cut into steps: lemmas on the model of StepMachineStatements.lean (HasSize,
Stepped, Reaches, Runs), what `Runs` means
for plain iteration of the step function, and basic ways to
build machines. 

### `next`

 One step of the iteration: a halted state stays as it is. 

### `run`

 The state after exactly n steps of the iteration. 

### `Reaches.iterate`

 What Reaches means for the iteration, run for a fixed number T ≥ t of steps. 

### `Runs.out_run`

 After exactly T ≥ t steps of the iteration the result is there. 

### `runs_of_run`

 The converse of `Reaches.iterate`: if the iteration has the result after t steps and all its
states have size ≤ S, then Runs holds. 

### `Runs.unique`

 The result is unique. 

 ### One step, pre- and post-composition 

### `ofFun`

 f in one step. 

### `mapIn`

 M on f a. No further step. 

### `mapOut`

 f applied to the result of M. No further step. 

 ### Composition 

### `bind`

 M, then N on the input together with the result of M. 

 ### The loop 

### `Orbit`

 Orbit nxt o xs: xs is the list x, nxt x, nxt (nxt x), … from o = some x up to the point where
nxt gives none;
xs = [] if o = none. 

### `foldGo`

 The loop's state with accumulator c and next point x: the body starts at x, or the loop halts
with c if x = none. 

### `foldWhile`

 The loop: run M at x = start a, fold its result into the accumulator by g, go on to nxt x; halt
at none. 

### `foldWhile_body`

 The body, run inside the loop. 

### `foldWhile_runs`

 The loop: steps = Σ over the orbit of (steps of the body + 1); result = the fold over the orbit. 
