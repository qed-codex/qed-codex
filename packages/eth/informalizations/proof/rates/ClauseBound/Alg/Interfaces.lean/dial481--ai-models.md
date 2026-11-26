---
{
  "module": "proof/rates/ClauseBound/Alg/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The interface lemmas, as PROPOSITIONS

As in proof/rates/PaddedDescent/F/Interfaces.lean: definitions `St… : Prop`; nothing is proved and
nothing is assumed here. One file proves `theorem … : St…`; a file that needs such a lemma imports
that
file or takes `(h : St…)` as a hypothesis, and the final assembly feeds the proofs in. 

### `WFe`

 I is an instance on K nodes with labels of exactly lam ≥ 1 bits and entries of absolute value at
most 2^B. 

 ### Enum.lean 

 ### Grid*.lean: the networks of the terms of one level on a p × d grid, for any pieces 

 ### The pad for a schedule of levels 

### `FitsG`

 The pad of length F suffices for a state with at most cnt instances on Kup nodes (labels lam,
entries ≤ 2^B), a sum and a factor of at most z bits, and for all steps below. 

### `needG`

 The exponent of a pad that suffices: the largest of the exponents of all the budgets of `FitsG`,
computed from the schedule. 

 The exponent `needG` can be huge for a senseless schedule, so the machine computes it under a
bound b: the state of the computation is cut off when its word gets longer than 100·(b+2). 

### `NState`

 ((label length in unary, B), (cnt, z), (number of nodes, largest exponent so far)). 

### `needStep`

 One step of the computation of `needG`. 

### `needFin`

 The end of that computation. 

### `needC`

 `needG P Kup lam B 1 1 sched` if it is at most the length of b, computed with cut-offs; `none`
otherwise. 

 ### The polynomial-time certificates 

 ### The clique solver: the form in which part (b) of Theorem A, and the hypothesis of Theorem D(a), are used 

### `Solver`

 One algorithm for the cliques on K i nodes, i in an index type that is data. `need` is the
exponent of a pad that suffices, as a function of (i, λ, B). 

### `Solver.needC`

 `need`, computed under a bound in unary: `none` if it is larger than the bound 

### `Correct`

 The algorithm is right when the pad is long enough. 

### `Poly`

 It is polynomial-time in (pad, index, instance); K is computed in unary, the exponent under a
bound. 

### `topK`

 The number of nodes at the top of a schedule. 

### `solverOf`

 The solver that a family of pieces gives: the index is (schedule, K₀ in unary). 

### `Solver.Seq`

 A sequence of indices of a solver with the hypotheses of Theorem D(a), and a way to pick the
right index. 

### `Solver.Seq.pick`

 from a bound in unary: the number l and the index of the largest l with K_l ≤ bound (l = 0 if
  there is none) 

 ### The top level in m 

### `satFk`

 The network of a k-CNF with g and k in the context: ((g, k) in unary, ψ). 
