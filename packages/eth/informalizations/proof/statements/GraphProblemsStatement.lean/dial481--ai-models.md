---
{
  "module": "proof/statements/GraphProblemsStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/GraphProblemsStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/GraphProblemsStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The statement of Corollary 7: counting in graphs

Corollary 7 of the paper: «For all δ > 0 and k ≥ 3 there are deterministic algorithms that, given a
graph on n vertices, with any number of edges, and an integer s,
compute in time O(2^{δn}) the number of its independent sets of size s, and likewise of its cliques,
vertex covers and dominating sets of size s and of its proper colorings with k
colors. In particular, they decide Independent Set, Clique, Vertex Cover, Dominating Set and
k-Coloring, since subsets of independent sets and of cliques, and supersets of vertex
covers and of dominating sets, are again such sets.»

This file has definitions only (no theorem, no proof) and imports Mathlib only: it can be read
without any other file of this development.

## How to read it

* A graph on n vertices is a `SimpleGraph (Fin n)` of Mathlib: the vertices are 0 … n−1, adjacency
  is symmetric, there are no loops. Any number of edges.
* Independent sets, cliques, vertex covers, proper colorings and «colorable» are Mathlib's notions
  (`IsNIndepSet`, `IsNClique`, `IsVertexCover`, `Coloring`, `Colorable`). Mathlib has no dominating
  sets; `IsDominating` below says that every vertex is in S or has a neighbor in S. A set of
  vertices is a `Finset (Fin n)`; `Set.ncard` is the number of elements of a (finite) set.
* The input is a word over {0,1}: n in unary (1ⁿ0), then, for the four problems with a size, s in
  unary (1ˢ0), then the n² entries of the adjacency matrix, row by row. Its length is
  n² + n + s + 2. Only 0 ≤ s ≤ n is asked for: a Mathlib machine has to pop all of its input, so no
  bound in n alone could hold for arbitrary s in unary; for s > n the four numbers are 0.
* The number k of colors is fixed before the machine, as in the paper; it is not part of the input.
* The output of a counting machine is the number in binary, LOWEST BIT FIRST, without leading zeros
  (Mathlib's `Nat.bits`); so the number 0 is the empty word. The output of a deciding
  machine is one bit.
* A machine is Mathlib's `Turing.FinTM2`: deterministic, finitely many labels and states, finitely
  many stacks. Mathlib does not ask that every stack has a finite alphabet, so the definitions
  below do. `TM2OutputsInTime` says: started with the input on the input stack, the machine halts
  within the given number of steps with exactly the output on its output stack, all other stacks
  empty and its internal state back at the initial one. One step runs the statement at the current
  label as far as a `goto` or `halt`: a bounded number of pushes and pops for a fixed machine.
* «Time O(2^{δn})» is: at most C·2^{δn} steps, rounded down, for EVERY n, with a constant C chosen
  together with the machine, after δ (and k) and before n, the graph and s.
* There is one machine for each of the problems, each δ, and (for colorings) each k.
* The decision problems are the usual ones: is there an independent set (a clique) with AT LEAST s
  vertices, a vertex cover (a dominating set) with AT MOST s vertices, a proper coloring
  with k colors.

## Where it differs from the paper's sentence, and what it does not say

* The paper counts time in operations on words and table queries, without fixing a machine or a code
  of graphs; here time is steps of a multi-stack Turing machine, and the code is fixed.
* The paper has «an integer s»; here 0 ≤ s ≤ n, for the reason given above.
* Nothing is said about input words that are not codes (a matrix that is not symmetric or has a one
  on its diagonal, s > n, a wrong length).
* The constants C are not explicit, and the bounds say something only for astronomically large n.
* The proof of these statements in this development differs from the paper's; among other things,
  the size s is not fixed by a circuit with O(n) gates but by a sum over the possible numbers of
  chosen vertices in each block of vertices. 

 ### The input 

### `unary`

 The number m in unary: 1ᵐ0. 

### `matrix`

 The n² entries of the adjacency matrix, row by row. 

### `code`

 A graph as a word: n in unary, then the adjacency matrix. 

### `codeWith`

 A graph and a number s as a word: n in unary, s in unary, then the adjacency matrix. 

 ### What is counted 

### `IsDominating`

 Every vertex is in S or has a neighbor in S. 

### `numIndepSets`

 The number of independent sets of size s. 

### `numCliques`

 The number of cliques of size s. 

### `numVertexCovers`

 The number of vertex covers of size s. 

### `numDominatingSets`

 The number of dominating sets of size s. 

### `numColorings`

 The number of proper colorings with the colors 0 … k−1. 

 ### Time on a Turing machine 

### `Outputs`

 `M`, started on the word x, halts within T steps with the word y as output. 

### `CountsInTime`

 A deterministic algorithm, given a graph on n vertices and an integer s, computes the number
f(G, s) in time O(2^{δn}) (the form of Corollary 7 for one count f). 

### `DecidesInTime`

 A deterministic algorithm, given a graph on n vertices and an integer s, decides p(G, s) in time
O(2^{δn}). 

### `CountsColoringsInTime`

 A deterministic algorithm, given a graph on n vertices, computes the number of its proper
colorings with k colors in time O(2^{δn}). 

### `DecidesColoringInTime`

 A deterministic algorithm, given a graph on n vertices, decides in time O(2^{δn}) whether it has
a proper coloring with k colors. 

 ### Corollary 7 

### `CorGraphsCount`

 Corollary 7, first sentence: the five numbers are computed in time O(2^{δn}), for every δ > 0
(and every k ≥ 3). 

### `CorGraphsDecide`

 Corollary 7, second sentence: Independent Set, Clique, Vertex Cover, Dominating Set and
k-Coloring are decided in time O(2^{δn}), for every δ > 0 (and every k ≥ 3). 

### `CorGraphs`

 Corollary 7. 
