---
{
  "module": "proof/networks/Paper/SecNetworks_Model.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_Model.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecNetworks_Model.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Conventions of the paper (start of Section 3): what "time" and "operations" mean here. Nothing in this file depends on the pieces of Lemma 2 or on ρ.

The paper counts time in *operations*: operations on words, and table queries. The formal proof
makes this precise in two
stages.

1. An algorithm is a **step machine** (`Groundwork.Stepped`): a set of states, a function `init`
   that turns the input into the first
   state, a function `step` from a state to the next, and a function `out` that tells whether a
   state is final and with which
   result. `M.Runs a t S b` says: started on `a`, the machine halts with result `b` after at most
   `t` steps, and all its states
   have size at most `S`. (The size is a measure that comes with the machine; for the machines of
   this proof it is about the
   number of bits needed to write the state down.) Sections 3 to 6 count steps.
2. A step may be any function, so a number of steps means nothing by itself. `PolyTimeSteps M` says
   that `init`, `step` and `out` of
   `M` are computed in polynomial time by Mathlib's multi-stack Turing machines, the states being
   written as words of at most
   7 · size symbols. A machine with this property that makes T steps on states of size at most S
   runs in time T · poly(S) on a
   Turing machine (`Groundwork.exists_tm`). `steps_to_time` is the case of 3-SAT, the place where
   one Turing machine is put together.

So "X operations" in the paper becomes "X steps, each of them polynomial time in the size of a
state, and all states of
polynomial size". The polynomial factor is paid at the very end, by proving the bound in steps for
δ/2. 

### `StepMachine`

 An algorithm with inputs in `α` and results in `β`, cut into steps. 

### `PolyTimeSteps`

 The functions `init`, `step`, `out` of the step machine `M` are computable in polynomial time on
Mathlib's multi-stack Turing
machines, for some way of writing the states of `M` as words whose length is at most linear in the
size of the state. 

### `DecidesInSteps`

 `M`, started on the input string of an instance of 3-SAT on n variables, halts after at most c ·
2^{δn} steps with the bit
"satisfiable", and all its states have size at most c · (length of the input + 1)^c. 

### `steps_to_time`

 **From steps to time.** A step machine with polynomial-time steps that decides 3-SAT within c ·
2^{(δ/2)n} steps, on states of
polynomial size, gives a Turing machine that decides 3-SAT in time O(2^{δn}). (No counterpart in the
paper, which counts
operations informally.) 
