---
{
  "module": "ThreeSumApsp/Sec5/Corollary39/Definitions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary39/Definitions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary39/Definitions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39: the graph `H` of the reduction from k-Clique to triangles

The objects of the proof of Corollary 39.  The first `t = k - 3⌊k/3⌋` parts are the fixed parts
(`numFixed`, `fixedPart`), and the others form three groups of `⌊k/3⌋` consecutive parts (`width`,
`groupPart`).  A `k`-clique splits into its fixed vertices and its vertices in the three groups
(`fixedOf`, `groupOf`).  For a choice of the fixed vertices, `graphH` is the complete tripartite
graph on the choices of one vertex in each part of a group, with the edge weights `weightH`.  Last
come maximum and minimum weight triangles and the negated weights. 

### `KPartiteGraph`

 Corollary 39: "a complete k-partite graph with parts of n vertices and integer edge
weights". `w p u q v` is the weight of the edge between vertex `u` of part `p` and vertex `v` of
part `q`.  The graph is undirected, which is the field `symm`.  The values `w p u p v` (no such edge
exists) are never used. 

### `KPartiteGraph.w`

 The edge weights. 

### `KPartiteGraph.symm`

 The graph is undirected. 

### `KPartiteGraph.cliqueWeight`

 Corollary 39: a "k-clique, with one vertex in each part" is a choice `v : Fin k → Fin n` of a
vertex in each part; its "total edge weight" is the sum of the weights of its (k choose 2) edges. 

### `KPartiteGraph.HasZeroClique`

 Corollary 39: "some k-clique ... has total edge weight zero". 

### `KPartiteGraph.IsMinWeightClique`

 Corollary 39: "a k-clique of minimum ... total edge weight". 

### `KPartiteGraph.IsMaxWeightClique`

 Corollary 39: "a k-clique of ... maximum, total edge weight". 

### `width`

 Proof of Corollary 39.  ⌊k/3⌋, the number of parts in each of the three groups. 

### `numFixed`

 Proof of Corollary 39: "let t := k - 3⌊k/3⌋ ∈ {1, 2}" (and t = 0 when k is divisible by 3): the
number of fixed vertices. 

### `numFixed_eq_mod`

 Proof of Corollary 39: "t := k - 3⌊k/3⌋ ∈ {1, 2}" when k is not divisible by 3: t is the
remainder of k modulo 3. 

### `three_width_add`

 The t fixed parts and the three groups of ⌊k/3⌋ parts are all the k parts. 

### `fixedPart`

 Proof of Corollary 39: "fixing one vertex in each of the first t parts".  The `a`-th of the
first t parts. 

### `groupPart_lt`

 Proof of Corollary 39.  The number of the `j`-th part of group `i` (see `groupPart`) is less
than k. 

### `groupPart`

 Proof of Corollary 39: "Split the k parts into three groups of k/3 parts each", applied to "the
remaining 3⌊k/3⌋ parts".  The paper does not say which parts form a group; we take consecutive
parts. `groupPart i j` is the `j`-th part of group `i`. The paper's groups 1, 2, 3 are `i = 0, 1,
2`. 

### `fixedOf`

 Proof of Corollary 39.  The fixed vertices of a k-clique: its vertices in the first t parts. 

### `groupOf`

 Proof of Corollary 39.  The vertices of a k-clique in the parts of group `i`: the "vertices in
the ith part ... are the k/3-cliques of the original graph with one vertex in each part of the ith
group". 

### `weightH`

 Proof of Corollary 39: "Let U be a vertex of H in part i and V a vertex in part i+1.  The weight
of the edge UV of H is the total weight of the edges of the original graph between a vertex of U and
a vertex of V, of the edges inside U, of the edges between U and the fixed vertices, and, if i = 1
and t = 2, of the edge between the two fixed vertices." The four lines below are these four
contributions.  The parts of H are indexed by ℤ₃, so `i + 1` is taken modulo 3; the paper's i = 1 is
`i = 0` here.  The last line sums over the pairs of fixed vertices: there is one pair when t = 2 and
none when t ≤ 1. `f` is the choice of the fixed vertices. 

### `graphH`

 Proof of Corollary 39: the graph H, "the complete tripartite graph with" N := n^⌊k/3⌋ "vertices
per part", for the choice `f` of the fixed vertices, as an instance of Exact Triangle.  Vertex
number `finFunctionFinEquiv U` of a part is the tuple `U`. The parts A, B, C of the instance are the
parts 1, 2, 3 of H; the edge between C and A goes from part 3 to part 3 + 1 = 1. 

### `IsMaxWeightTriangle`

 Proof of Corollary 39: a "maximum weight triangle". 

### `IsMinWeightTriangle`

 Proof of Corollary 39: a "minimum weight triangle". 

### `negate`

 Proof of Corollary 39: "the negated weights". 
