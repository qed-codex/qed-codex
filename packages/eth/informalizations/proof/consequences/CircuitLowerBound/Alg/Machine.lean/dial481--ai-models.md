---
{
  "module": "proof/consequences/CircuitLowerBound/Alg/Machine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Machine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Machine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the nondeterministic algorithm as a computation cut into steps

On the input 1^m 0 y the algorithm writes down a formula with clauses of at most three literals
(`pre`) and accepts if and only if this formula is UNSATISFIABLE, which it finds out by counting the
satisfying assignments with the
engine for #3-SAT. Before the last place of a chain, and if there is room, y is read as a circuit on
m inputs, and the formula says «some clause of `Phi m` is violated by the assignment that the
circuit computes»; if y does not code such a circuit, the formula is the empty formula (the
algorithm rejects). In all other
cases `Phi m` is [] or [[]], and the formula is the constant formula with the opposite answer. The
file proves: the formula always has the shape that the engine asks for (`shaped_pre`); if it is
unsatisfiable, `Phi m` is
satisfiable (`sat_Phi_of_pre`); if a circuit computes a satisfying assignment of `Phi m`, then for
the code y of this circuit the formula is unsatisfiable and has few variables (`exists_guess`); the
computation ends on every input with
the right answer (`runs_algo`); and a machine of Mathlib has at most one output (`outputs_unique`). 

 ### The formula 

### `uOf`

 The number of ones at the start of x, in unary. 

### `preG`

 The formula of the algorithm, with the functions of the schedule as parameters: (number of
variables in unary, formula). 

### `pre`

 The formula of the algorithm. 

### `isZ`

 Are all bits of a word 0? 

### `algo`

 The algorithm: the formula, the engine, «is the number 0?». 

### `uOf_eq`

 It is 1^m in unary, m the number of ones at the start of x. 

### `pre_cases`

 The six cases of the definition. 

### `shaped_nil`

 The empty formula has the shape. 

### `shaped_false`

 The formula with the empty clause has the shape. 

### `sat_nil`

 The empty formula is satisfiable. 

### `not_sat_false`

 The formula with the empty clause is not satisfiable. 

### `FormOK`

 What `StForm` says about F. 

### `FlipOK`

 What `StFlip` says about fb. 

### `shaped_pre`

 The formula always has the shape that the engine asks for. 

### `sat_Phi_of_pre`

 If the formula is unsatisfiable, `Phi m` is satisfiable. 

### `exists_guess`

 If a circuit computes a satisfying assignment of `Phi m`, then for the code y of this circuit
the formula is unsatisfiable and has few variables. 

 ### Counting and satisfiability 

### `cntN_eq_zero_iff`

 The number of satisfying assignments is 0 if and only if the formula is unsatisfiable. 

### `cntN_lt`

 There are at most 2^N assignments. 

### `isZ_binary`

 All N + 1 bits of a number below 2^(N+1) are 0 if and only if the number is 0. 

### `EngineOK`

 What the engine for #3-SAT is asked to do with E, for clauses of at most three literals: output
the number of satisfying assignments in binary, within c·2^{δN} steps. 

### `runs_algo`

 The algorithm ends on every input, and its answer is «the formula is unsatisfiable». 

 ### Polynomial time 

### `preG_polyT`

 The formula is computed in polynomial time, if the functions of the schedule are. 

### `pre_polyT`

 The formula is computed in polynomial time. 

### `isZ_polyT`

 The test for 0 is polynomial-time. 

### `isPolyT_algo`

 All parts of the algorithm are polynomial-time. 

 ### A machine has at most one output 

### `iterate_halt`

 From a halted configuration there is no step. 

### `outputs_unique`

 Two runs of a machine on the same input that end with an output end with the same output. 
