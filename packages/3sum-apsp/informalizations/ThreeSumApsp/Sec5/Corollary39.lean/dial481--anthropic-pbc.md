---
{
  "module": "ThreeSumApsp/Sec5/Corollary39.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary39.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary39.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39: from weighted k-Clique to triangles

Corollary 39 decides Zero-Weight k-Clique, and finds a k-clique of minimum or maximum weight, in
`O(n^{k-ε_T⌊k/3⌋})` time, by the reduction of Nešetřil and Poljak.  Fix one vertex in each of the
first `t = k - 3⌊k/3⌋` parts, split the other parts into three groups of `⌊k/3⌋` parts, and let `H`
be the complete tripartite graph whose vertices are the choices of one vertex in each part of a
group.  Running times are not defined here; this file proves that the reduction is correct, in the
paper's order:
* the fixed parts and the three groups are all the `k` parts (`partEquiv`), so a `k`-clique is a
  choice of the fixed vertices and a triangle of `H` (`bijective_fixedOf_groupOf`);
* "every edge of a k-clique is counted exactly once over the three edges of its triangle"
  (`sum_pairs_eq_sum_edgeSum`), so a triangle and its `k`-clique have the same weight
  (`S_graphH_eq_cliqueWeight`);
* `(k choose 2) n^ν ≤ N^{2ν}` for `n ≥ k²` (`choose_mul_rpow_le`; nothing else rests on it);
* hence the answers agree: weight zero (`hasZeroClique_iff`), maximum (`isMaxWeightClique_iff`),
  minimum (`isMinWeightClique_iff`), where a minimum weight triangle is a maximum weight triangle
  for the negated weights (`isMinWeightTriangle_iff_negate`).


 ### The `k` parts 

### `partEquiv`

 The `k` parts, listed: the `t` fixed parts, then the parts of the three groups. 

### `sum_parts`

 A sum over the `k` parts is a sum over the fixed parts plus a sum over the parts of the three
groups. 

### `bijective_fixedOf_groupOf`

 Proof of Corollary 39: "The triangles of H correspond bijectively to the k-cliques of the
original graph with one vertex in each part", and when k is not divisible by 3, "the triangles of H
correspond to the k-cliques through the t fixed vertices".  A k-clique is the same thing as a choice
of the t fixed vertices together with a triangle of H (one vertex of H in each part). 

 ### The order of the parts 

### `fixedPart_lt_fixedPart`

 The order of the fixed parts is the order of their indices. 

### `fixedPart_lt_groupPart`

 Every fixed part comes before every part of a group. 

### `groupPart_lt_groupPart`

 The parts of the groups are ordered by group, and inside a group by their index. 

 ### A triangle and its `k`-clique have the same weight 

### `edgeSum`

 The sum of the four contributions to the weight of an edge of `H` from part `i` to part `i + 1`
(proof of Corollary 39), for a table `W` of the weights of the edges of a `k`-clique: `W p q` is the
weight of its edge between the parts `p` and `q`. 

### `sum_pairs_eq_sum_edgeSum`

 Proof of Corollary 39: "every edge of a k-clique is counted exactly once over the three edges of
its triangle".  Both sides are split into sums over the fixed parts and the three groups; the edges
between the groups 0 and 2 are counted from group 2. 

### `weightH_eq_edgeSum`

 The weight of the edge of `H` between the vertices that the `k`-clique `v` defines in the parts
`i` and `i + 1`, in terms of the table of the weights of the edges of `v`. 

### `S_graphH_eq_cliqueWeight`

 Proof of Corollary 39: "We give H edge weights so that a triangle and its k-clique have the same
weight. ... In this way every edge of a k-clique is counted exactly once over the three edges of its
triangle, so there is no double-counting and the weights agree." 

 ### The size of the weights of `H` 

### `choose_mul_rpow_le`

 Proof of Corollary 39: "(k choose 2) n^ν ≤ N^{2ν} for n ≥ k²", because `(k choose 2) ≤ k² ≤ n`,
`n ≤ n^ν` for ν ≥ 1, and `n ≤ N`.  `κ` is the paper's ν. 

 ### The answers agree 

### `exists_cliqueWeight_eq`

 Every triangle of every graph `H` is the triangle of a `k`-clique, which has the same weight. 

### `hasZeroClique_iff`

 Corollary 39, Zero-Weight k-Clique, correctness of the reduction: some k-clique has
total weight zero if and only if, for one of the n^t choices of the fixed vertices, H has a triangle
of weight zero. 

### `isMaxWeightClique_iff`

 Corollary 39, Max-Weight k-Clique, correctness of the reduction: a k-clique has maximum weight
if and only if no triangle of any of the n^t graphs H is heavier. 

### `isMinWeightClique_iff`

 Corollary 39, Min-Weight k-Clique, correctness of the reduction: a k-clique has minimum weight
if and only if no triangle of any of the n^t graphs H is lighter. 

### `isMinWeightTriangle_iff_negate`

 Proof of Corollary 39: "a minimum weight triangle is a maximum weight triangle for the negated
weights". 
