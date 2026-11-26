---
{
  "module": "proof/machines/StepMachines/Prog/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The interfaces of the programs in this folder. States and labels are words (List Bool) of
prescribed lengths; the default
word (the label at the node itself, the entries of a tuple off its index set) is []. Lengths are
plain functions of the
context c : C. (For each step to take time polynomial in the input, the context must hold these
lengths in unary; nothing here needs that.)

* an instance of the problem on a clique (K nodes, a λ-bit label on every edge, an integer tensor at
  every node)
given by a procedure that answers queries for tensor entries, and what an evaluator of instances
must do: compute Z in
about 2^{εK²λ} steps (ε = 1/2 is brute force);
* a network (`Network`: nodes with states and integer weights, for every pair of nodes an
  interaction that factors
through labels) given by procedures, and what an evaluator of networks must do: the rebalancing of a
network on g nodes into K groups. 

 ### Instances given by a procedure 

### `IQ`

 A query to an instance: the node v and the list (θ_u), u = 0, …, K-1, of the labels of the edges
{v,u} ([] at u = v). 

### `ServesInst`

 In the context c the procedure R presents the instance Rm on K nodes with ℓ-bit labels: every
well-formed query (a label of
ℓ bits for each other node, [] at the node itself) is answered within t steps and size S, and the
entry of Rm at such a query is
at most 2^B in absolute value. Nothing is asked at other arguments. 

### `Evaluator`

 An algorithm for instances: from the length function lam and a procedure R (any type of
contexts) a computation
on contexts. 

### `Evaluator.Correct`

 E solves the problem on a clique with K nodes with exponent ε: Z within A·2^{εK²λ}·(B+λ)^A·t
steps, in size
S + polynomial (ε = 1/2 is brute force). 

 ### Networks given by procedures 

### `WQ`

 A query for a weight: (a, z). 

### `FQ`

 A query for a factor: ((a, b), (z, θ)) asks for f_ab(z,θ). 

### `PNet`

 A network given by procedures: n c a is the length of the states of a, cap c a b the length of
the labels of {a,b}. 

### `PNet.Presents`

 In the context c the procedures present the network N on Fin g; every answer within t steps and
size S. 

### `NetEvaluator`

 An algorithm for networks: from procedures (any type of contexts) a computation on contexts. 

### `NetEvaluator.Correct`

 NE does the rebalancing of a network into K groups: the value of every network on Fin g of size
P (at most 2^P states and at
most P label bits at a node) within A·2^{εU + b·gP/K}·(P+B)^A·t steps; U is the sum of the label
lengths over ordered
pairs. 
