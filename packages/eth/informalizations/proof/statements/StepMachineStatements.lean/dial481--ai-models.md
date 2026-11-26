---
{
  "module": "proof/statements/StepMachineStatements.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/StepMachineStatements.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/StepMachineStatements.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The algorithm as a step machine: definitions

The time of an algorithm for 3-SAT needs a model of computation. `NetworkStatements.lean` states
what
needs no machine. This file states what the step machines of proof/machines/StepMachines/ add: a
simple model of a computation cut into
steps, and what it means that such a machine decides 3-SAT within c·2^{δn} steps. It has definitions
only, and imports
`NetworkStatements` only (and through it `ThreeSatStatement` and Mathlib).

Read the warning at `DecidesInSteps` before quoting anything from this file. 

 ## Step machines 

### `HasSize`

 The size of a value: about the number of bits needed to write it down. 

### `Stepped`

 A computation cut into steps: a type `σ` of states with a measure of size (a part of the
machine), the state `init a` in which
the input `a` is handed over, the function `step` from a state to the next, and `out`, where
`out s = some b` means: halted with
result `b`. Nothing restricts `init`, `step`, `out` or the measure of size: they are arbitrary
functions. 

### `Reaches`

 From the state s: halts with b within t steps, all states of size ≤ S. 

### `Runs`

 From init a: halts with b within t steps, all states of size ≤ S. 

 ## 3-SAT on a step machine 

### `DecidesInSteps`

 The machine `M`, started on the code of an instance of 3-SAT on n variables, halts within
c·2^{δn} steps with the bit
«satisfiable», and all its states have size polynomial in the length of the input; one constant c
for all instances.

WARNING. `init`, `step` and `out` of a `Stepped` machine are arbitrary Lean functions, and only
applications of `step` are
counted. A machine may decide satisfiability while the input is handed over, in no step at all. The
measure of size is a
field of the machine too, so a machine may call all its states small. So «∃ M, DecidesInSteps M δ»
is trivially true for
every δ and says nothing. What this development
proves is that explicit machines have this property: for every δ > 0, one machine of an explicit
family has
it. These machines are defined in `StepMachines/Prog` and built from the algorithm of Theorem 2, and
their
states are measured by the `HasSize` instances of this file, not by a measure chosen for them. That
statement has content only
together with the definition of these machines: the reader has to look there to judge what the
hand-over, one step and the
reading of the result do (the hand-over, for one, decodes the input). This file does not say whether
each of the three can be done in
polynomial time on a Turing machine. 
