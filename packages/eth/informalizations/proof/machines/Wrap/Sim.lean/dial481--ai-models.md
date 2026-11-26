---
{
  "module": "proof/machines/Wrap/Sim.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Sim.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Sim.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a coding of the configurations of a machine to a machine around it

Given a coding `K` of the configurations of a machine M (`Wrap.Coding`) and polynomial-time
functions `pre`, `post` on bit strings, `sim K pre post` is the computation cut into steps that
starts with the value
for the start configuration of M on `pre x`, applies the coded step of M, and ends, once M has
halted, with `post` of M's output. All three of its parts are polynomial-time (`sim_isPolyT`). After
j steps its state is the value for
the configuration of M after j steps (`run_sim`), and each step adds at most a constant to the size
of that value (`size_rep_iterate_le`). So a run of M on `pre x` of at most t steps with output y is
a run of `sim K pre post` on x of at most t steps with
result `post y` and with states of size linear in |pre x| + t (`sim_runs`). The host machine
(`CountKSat.exists_tmW`) carries out such a computation on one of Mathlib's machines with a
polynomial overhead; this gives `wraps_of_coding`.
`everyMachineCanBeWrapped_of`: if every machine with finite alphabets has a coding, then every such
machine can be wrapped. 

### `sim`

 The simulation of M as a computation cut into steps. Its states are the values that stand for
configurations of M. It starts with the value for the start configuration of M on `pre x`; one step
is the coded step of M; it has a result
once the value stands for a halted configuration, and the result is `post` of M's output. 

### `sim_init_polyT`

 The start of the simulation is polynomial-time if `pre` is. 

### `sim_out_polyT`

 Reading the result of the simulation is polynomial-time if `post` is. 

### `sim_isPolyT`

 The start, the step and the reading of the result of the simulation are polynomial-time if `pre`
and `post` are. The states are encoded and measured by the library's instances for pairs, lists and
numbers. 

### `next_sim`

 One step of the iteration of the simulation, on the value for the configuration c, gives the
value for the next configuration of M; a halted configuration stays as it is on both sides. 

### `run_sim`

 After j steps the state of the simulation on x is the value for the configuration of M after j
steps on `pre x`. 

### `size_rep_iterate_le`

 j steps of M add at most j times the constant of the coding to the size of the value. 

### `sim_runs`

 If M puts out y on `pre x` within t steps, then the simulation ends on x with `post y` within t
steps, and all its states have size at most a·(|pre x| + 1) + a·t, where a is the constant of the
coding. 

### `Outputs.mono`

 A bound on the number of steps may be made larger. 

### `exists_bound`

 The numbers: for all q₀, a, c there is a q such that q₀·(t + 1)·(n + (a·(p + 1) + a·t) + 1)^q₀ ≤
q·(t + n + 1)^q whenever p ≤ c·(3n + 3)^c. (3n + 3 bounds the length of the word that stands for a
bit string of length n, plus 1; `pre` is polynomial in that length.) 

### `wraps_of_coding`

 The composition lemma, from a coding: if the configurations of M have a coding, then for all
polynomial-time `pre`, `post` there are a machine N with finite alphabets and a number q such that,
whenever M puts out y on `pre x` within t steps, N puts out
`post y` on x within q·(t + |x| + 1)^q steps. 

### `everyMachineCanBeWrapped_of`

 If every machine with finite alphabets has a coding of its configurations, then every such
machine can be given a polynomial-time front end and a polynomial-time last step. 
