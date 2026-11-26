---
{
  "module": "proof/variables/ThmVariables/EveryMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/EveryMachine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/EveryMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) with the printed hypothesis, for every machine that runs the named algorithm

The step from counted operations to the padding string is
`QueryMachines.Bridge.SolverOfMachineLevels`, a hypothesis here: for every machine E with query
access as in the hypothesis of Theorem D (a), with any certificate that its steps are
polynomial-time, the NAMED solver `solverOfMachine E num C₀` is polynomial-time and has a sequence Q
of levels for K_ℓ and e′_ℓ = `cutNumber K num ℓ`, and the level is picked by
the named program `pickOf kf (K 0)`.
* `solverFromMachine_of`: the form that forgets the names follows.
* `partAForEveryMachineFrom`: Theorem D (a) for every machine that computes `RecursionToBound.count`
  (`RecursionToBound.ThmVariablesAForEveryMachine`, a hypothesis here) is applied to this solver, to
  Q and to the fraction `cutFraction num` (`numberBetween_cut`); `Q.pick` is rewritten to the named
  program; the bound at e′_ℓ is the bound at e_ℓ with twice the constant (`conclusion_of_cut`).
* `partAFromEveryMachine`: the form that says that there is a machine (`PartA`) follows, at n₁ = n₀. 

### `solverFromMachine_of`

 What the proof of `PartA` through the padding string takes from the step from counted operations
to the padding string (`SolverFromMachine`) follows from the statement on the named solver
(`QueryMachines.Bridge.SolverOfMachineLevels`). 

### `partAForEveryMachineFrom`

 Theorem D (a) for every machine that runs the named algorithm on the named solver, from the
statement on the named solver and Theorem D (a) for every machine that computes the function of
Steps 1 to 5. 

### `partAFromEveryMachine`

 Theorem D (a) in the form that says that there is a machine (`PartA`) follows from the form for
every machine (`PartAForEveryMachine`). 
