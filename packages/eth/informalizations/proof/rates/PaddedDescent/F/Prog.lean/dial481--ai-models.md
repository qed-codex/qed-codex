---
{
  "module": "proof/rates/PaddedDescent/F/Prog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Prog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Prog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The definitions, part 3: the program

The pure function `A : List Bool × U → Bool` that decides 3-SAT when the pad is long enough, and, at
the end of the file, the predicates (`Bud`, `Fits`,
`Chain`, `NetFits`, `MarkFits`) and bounds (`lamG`, `Ub`, `Pb`, `layLen`, `schedLen`, `stackLen`) in
which the arithmetic says that a pad is long enough. K, g, the label lengths and the list of
levels are data, in unary.

There are two rebalancings. At the top, a network of marks (F/MarkNet.lean) on 3K⁸ nodes is
rebalanced by `rebalF`, with the label length `betaC` and the test `goodB` of
StepMachines/Prog/NetProg.lean. At the levels below, where any two nodes of a network share a
bounded number of label bits, `rebalG` works on a grid of side
g = K·L with a small factor L; its label length is handed in. The sparsification tree is that of
proof/sparsification/SparsifyWidthK at width 3, whose leaves have at most (2 + 8τ + 96τ²)·n clauses.
The clauses of a leaf are divided into layers (F/MarkMath.lean), and the number of its satisfying
assignments is one evaluation `evalF`: a sum of values of
networks of marks, whose number of shared label bits grows only with the square of the logarithm of
the number of clauses per variable. 

 ### The rebalancing on explicit data 

### `termF`

 The counterpart of `NetE.termM` / `NetE.termVal` for an explicit `FNet`, with its sums taken
over the pad. 

### `mergedF`

 The counterpart of `NetE.mergedM` / `NetE.mergedVal` for an explicit `FNet`, with its sums taken
over the pad: one entry of the merged instance. 

### `rebalF`

 From a network on g nodes, given by plain functions in the context c, to the explicit instance
on K nodes: the first good colouring,
the new label length (in unary), the whole new table. `none` if no good colouring is found. 

### `goodG`

 Is the colouring x good for the label length β? Every class has fewer than 2g/K members and any
two classes share at most β label bits. This is
`NetE.goodB` with β in place of `betaC`. 

### `rebalG`

 `rebalF` with the new label length β handed in: the first colouring that is good for β, β in
unary, the whole new table. 

 ### The network of one term of one level of the recursion, read off an explicit table 

### `cutF`

 The counterpart of `Grid.cutW` on explicit words, with its sums taken over the pad. 

### `itemF`

 The counterpart of `Grid.sideItem` on explicit words, with its sums taken over the pad. 

### `SideCtx`

 ((pad, g in unary, tr), (ℓ in unary, pattern y, table)); tr = false: rows merged, tr = true:
columns merged. 

### `sideWF`

 The counterpart of `sideWP` / `sideWv`, read off an explicit table. 

### `sideFF`

 The counterpart of `sideFv` on explicit data, with its sums taken over the pad. 

 ### One level, all levels, the bottom 

### `sideCtx`

 The context of the side network for the instance I on g·g nodes and the pattern y: the cheaper
side. 

### `capM`

 An upper bound for the number of label bits that two nodes of a side network share
(`Grid.sideCap_le`). 

### `Ubar`

 An upper bound for U of the cheaper side network. 

### `lamNext`

 The label length one level down: U/K² with the relative error of the colouring, rounded up. 

### `childF`

 The instance on K nodes that the pattern y of the instance I on g·g nodes leads to. 

### `expand`

 One level: an instance on g·g nodes becomes the list of its (ℓ+1)^R children on K nodes; Z is
the sum of theirs. 

### `descend`

 All levels, breadth first: the work list after the steps of sched. 

### `bruteF`

 Brute force on K nodes: the counterpart of `brute`, read off an explicit table, with the sum
taken over the pad. 

 ### The schedule 

### `gU`

 3K⁸ in unary: the number of nodes of the network of a formula. 

### `mulU`

 g = K·L in unary: the side of the grid at a level. 

### `sqU`

 g² in unary. 

### `schedF`

 After t rounds: ([(K_{t−1}, g_{t−1}), …, (K₀, g₀)], K_t, L_t), with K₀ = 256, g_j = K_j·L_j,
K_{j+1} = g_j², L_{j+1} = 2·L_j. 

 ### One sparse formula, the sparsification tree, the whole function 

### `valF`

 The top rebalancing, all levels and exhaustive search at the bottom, for any network given by
plain functions: the value of the network, if the pad is
long enough. S = (steps of the schedule, K_t). 

### `evalF`

 One evaluation: the sum of the values of the networks of marks over the admissible profiles. It
is `Mark.trunc n w Ls` under the hypotheses of `StEval`.
p = (n, w, β, b), in unary: number of variables, cap, and the two parameters of the code of the
labels. k is the width of the clauses. 

### `layersF`

 The clauses of ψ, placed one after the other into R + 1 layers; every decision takes two
evaluations. 

### `countM`

 The number of assignments of the n variables that satisfy ψ, under the hypotheses of `StCountM`. 

### `markPar`

 The parameters (n, w, β, b) of the evaluations for n variables and precision s, in unary. 

### `walkF`

 The depth-first walk of the sparsification tree for width k, one round for each unit of the pad. 

### `A`

 THE function, for 3-SAT. 

 ### The interface between the programs and the arithmetic 

### `Pn`

 P of `sideN_sized`. 

### `bNext`

 An upper bound for the bit length of the entries one level down. 

### `instLen`

 An upper bound for (length of the word of an instance) + 2. 

### `Bud`

 What one step «g·g nodes, labels ≤ lam → K nodes» needs of the length F of the pad. 

### `Fits`

 The pad of length F suffices for a work list of at most cnt instances on Kup nodes, labels ≤ Λ,
entries ≤ 2^B, and all steps of the
schedule below it. 

### `ColOK`

 A network on g nodes in which any two nodes share a bounded number of label bits has a good
colouring with K colours: g is at least about
4·Dcol²·K·log₂(g·K). 

### `Chain`

 The schedule is a chain of steps g·g → K that ends at 256 nodes. 

### `schedL`

 The steps of the schedule of depth t, as a mathematical object: what `schedF` computes when the
pad is long enough. 

### `schedLen`

 An upper bound for the length of the word of every state of `schedF pad t`. 

### `lamG`

 An upper bound for the label length of the top instance of a network with U ≤ Ub and size P. 

### `NetFits`

 The pad of length F suffices for one network on 3K_t⁸ nodes with U ≤ Ub, size P and entries 0,
1, −1, under the schedule S = (steps, K_t). 

### `Ub`

 An upper bound for U of the network of marks of an admissible profile: width k, R₁ layers, cap
w, code parameter β, at most b·(n + 1) clauses. 

### `Pb`

 An upper bound for the size P of the network of marks: every variable occurs in at most Δ
clauses. 

### `layLen`

 An upper bound for the length of the word of a division of at most m clauses, of at most k
literals on variables below n, into R + 1 layers. 

### `MarkFits`

 The pad of length F suffices for all evaluations for one formula: width k, n variables, at most
m clauses, every variable in at most Δ of them, R + 1 layers,
code parameters β and b, cap n + 2. 

### `stackLen`

 An upper bound for the length of the word of a state of the walk: at most bsum τ k · n + 1
formulas of at most 2^k·m clauses of at most k
literals on variables below n, and a flag. 

### `inLen`

 An upper bound for the length of the code of an instance of k-SAT on n variables, plus 1, and so
for its number of clauses. 
