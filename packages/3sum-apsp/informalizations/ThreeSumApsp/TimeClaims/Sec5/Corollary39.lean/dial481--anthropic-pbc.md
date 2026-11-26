---
{
  "module": "ThreeSumApsp/TimeClaims/Sec5/Corollary39.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec5/Corollary39.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec5/Corollary39.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39 from Theorem 19

All lemmas are about an arbitrary interpretation `M : DetTimeModel5` of "is solved in time T".

A `k`-clique is a triangle in one of `n^t` graphs `H` on `N = n^⌊k/3⌋` vertices per part, with
weights up to `binom(k, 2) n^κ` (`κ` is the paper's ν).  For constant `k` and `κ` all times are
functions of `n` alone, bounded from above up to logarithms:

1. Theorem 19 decides whether `H` has a triangle of weight zero in time `Õ(N^{3-ε'})`
   (`upperPowPolylog_exactTriangle`);
2. a maximum weight triangle costs `O(log² n)` times as much, and a minimum weight triangle is a
   maximum weight triangle for the negated weights (`upperPowPolylog_maxTriangle` and the first
   lines of `minMaxClique_of_theorem_19_VW13`);
3. building a graph costs `Õ(N²)` (`isPowPolylog_sq_mul_one_add_logU`), and the `n^t` graphs
   together cost `Õ(n^t N^{3-ε'}) ⊆ O(n^{k-ε_T ⌊k/3⌋})` (`upperBigOPow_clique`,
   `exists_clique_of_triangle`).


### `isBigOPow_cast_pow`

 `N = n^w` is `O(n^w)`. 

### `isPowPolylog_sq_mul_one_add_logU`

 Writing a graph on `N = n^w` vertices per part costs `N² (1 + log U) = Õ(N^{3-ε'})`. 

### `upperPowPolylog_exactTriangle`

 "Theorem 19 decides whether H has a triangle of weight zero in O(N^{3-ε'} log N) time": the
explicit bound of Theorem 19 at `N = n^w` vertices per part and weights up to `U(n) ≤ n^κ`. 

### `upperPowPolylog_maxTriangle`

 "Finding a maximum weight triangle costs O(log² n) times as much": the time that the cited
reduction gives on `N = n^w` vertices per part. 

### `upperBigOPow_clique`

 "The n^t graphs together cost O(n^t N^{3-ε_T}) = O(n^{k-ε_T ⌊k/3⌋})": if one graph costs
`F(n) = Õ(N^{3-ε'})`, apart from building it. 

### `exists_clique_of_triangle`

 The reduction from a clique problem to a triangle problem, on weights up to `n^κ`: if the
triangle problem on one graph `H` costs `Õ(N^{3-ε'})`, the clique problem costs
`O(n^{k-ε_T ⌊k/3⌋})`. 

### `isPowPolylog_logU_weights`

 The weights of the graphs `H`: `log (binom(k, 2) n^κ) = Õ(1)`. 

### `zeroClique_of_theorem_19`

 The deduction of the Zero-Weight part of Corollary 39 from Theorem 19 (in the explicit form of
`Claim.Theorem_19_explicit`): "Theorem 19 decides whether H has a triangle of weight zero
in O(N^{3-ε'} log N) time ... so each graph H costs O(N^{3-ε_T}) time, and the n^t graphs together
cost O(n^t N^{3-ε_T}) = O(n^{k-ε_T⌊k/3⌋})." 

### `minMaxClique_of_theorem_19_VW13`

 The deduction of the Min-Weight and Max-Weight parts of Corollary 39 from Theorem 19 and the
cited [VW13, Theorem 3.3].  The paper: "finding a maximum weight triangle costs O(log² n) times as
much, and a minimum weight triangle is a maximum weight triangle for the negated weights.  Since
ε' > ε_T, the logarithmic factors are absorbed". 
