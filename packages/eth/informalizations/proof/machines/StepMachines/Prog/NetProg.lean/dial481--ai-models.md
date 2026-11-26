---
{
  "module": "proof/machines/StepMachines/Prog/NetProg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetProg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetProg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Programs for the rebalancing of networks (Lemma 1): the test `goodB` of a good colouring of the
g nodes with K colours, and the procedure `mergedM`,
which computes an entry of the table of one class by brute force over the states of the class, with
the plain functions they use and the values they compute.
A network has, at every node a, states z with integer weights W_a(z), and for every pair of nodes
labels θ of c_ab bits
(the capacity `Np.cap`) and factors f_ab(z,θ). Its value is the sum over all states of the product
of the weights
and of the interactions Ψ_ab(z,z') = Σ_θ f_ab(z,θ)·f_ba(z',θ).
A colouring of the g nodes with K colours is a number x < K^g (digit a in radix K = the colour of
a). 

 ### The plain functions 

### `col`

 The colour of the node a. 

### `members`

 The nodes of colour G, in increasing order. 

### `stLens`

 The lengths of the states of the members of G. 

### `stLen`

 The length of a state of the class G. 

### `zAt`

 The state of the member a in the state z of the class G. 

### `prs`

 The pairs (a,b), a in G, b in G'. 

### `lbLens`

 The lengths of the labels of these pairs. 

### `lbLen`

 The capacity between the classes G and G'. 

### `lAt`

 The label of the pair p in the label θ of the classes G < G'. 

### `rowSum`

 The number of label bits at the node a: Σ_{b≠a} c_ab. 

### `Uc`

 U: the sum of c_ab over the ordered pairs a ≠ b. 

### `Pc`

 The largest row sum. 

### `betaC`

 β: the bound on the label bits between two classes in a good colouring. 

### `goodB`

 Is the colouring x good? Every class has fewer than 2g/K members and any two classes share at
most β label bits. 

### `X0`

 The input of the procedure of the merged instance: ((c, x), (G, θs)). 

### `validB`

 In every label at G the bits after the first `lbLen` (the length of a label of the two classes)
are 0. The length of the label
is not tested: it is a hypothesis of `validB_iff`. 

### `nStates`

 The number of states of the class. 

### `zOf`

 The state of the class with number y. 

### `zA`

 The state of the node a. 

### `labOf`

 The label of {a,b}, a in G, b in another class. 

### `isOne`

 The factor number i = a*g + b of the product is 1: a is not in G, or b ≤ a is another member of
G. 

### `isW`

 It is the weight of a. 

### `isPsi`

 It is the interaction of two members. 

### `qW`

 The query for the weight of a at its state, i = a*g + a. 

### `qF`

 The query for f_ab at the state of a and the label of {a,b}, b in another class. 

### `nLab`

 The number of labels of the pair (a,b), i = a*g + b. 

### `qP1`

 The query for f_ab at the state of a and the label with number y. 

### `qP2`

 The query for f_ba at the state of b and the same label. 

### `nPairs`

 The number of factors of the product: one for each i = a*g + b. 

### `nCol`

 The number of colourings. 

### `zeroOf`

 The constant result 0. 

 ### The programs 

### `psiM`

 Ψ_ab(z_a,z_b) by its definition. 

### `termM`

 The factor number i. 

### `mergedM`

 The procedure of the merged instance: the entry of the tensor of the class G at the labels θs,
by brute force over
the states of the class. 

 ### What the programs compute 

### `valW`

 The weights of a network on Fin g, as a function of numbers. 

### `valF`

 The factors of a network on Fin g, as a function of numbers. 

### `termVal`

 The result of termM. 

### `mergedVal`

 The result of mergedM. 
