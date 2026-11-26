---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/ChanHe/Recursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Recursion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Recursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a), the reduction of Chan and He: one node, and the recursion for three sets

This file proves that the reduction for three sets, `reduction n U`, is correct and makes
polylogarithmically many instances.  It follows the proof of [CH20, Theorem 5.1], one of the
reductions behind Theorem 21(a).  A node of the recursion tree consists of three sets and a
modulus `M`.

* One node.  The elements that are alone in their residue class modulo `M` are called light.  The
  first two arrays hold each light element of the first two sets at the index of its remainder.  The
  third array holds `-c`, for each light element `c` of the third set, at the remainder of `-c` and
  once more `M` cells further on.  All other cells hold padding.  Padding is too large to take part
  in a solution, and `a + b + c = 0` makes the remainders of `a` and `b` add up to that of `-c`, or
  to that plus `M`.  So the Convolution-3SUM instance of the node has a solution iff the light
  elements of the three sets have a 3SUM solution (`node_correct`).
* The recursion.  A 3SUM solution consists of three light elements, or one of its elements is heavy
  (`hasSol_split`).  The three children of a node replace one set each by its heavy elements.
* The depth.  A set that has been replaced `j` times has at most `n / d_j` elements, where `d₀ = 1`
  and `d_{j+1} = 2 d_j²` (`Replaced.heavy`).  Since `d_j > n` for `j = height n` (`lt_dSeq_height`),
  it is then empty (`Replaced.eq_empty`), so no node lies below the `fuel n` levels of the tree that
  are built.  This gives `nodes_correct`, by induction on the number of levels, and
  `reduction_correct`, whose hypotheses on the three sets are collected in `Admissible`.
* The size.  A ternary tree with `fuel n` levels has at most `3 ^ fuel n ≤ (2⌊log₂ n⌋ + 2)⁵` nodes
  (`length_reduction_le`).  The entries of the arrays are bounded in `abs_arrXY_le` and
  `abs_arrZ_le`, and the count for the searches of one node in `scan_node_le`.


 ## Light elements and the cells of the arrays 

### `light`

 The elements of `S` that are alone in their residue class modulo `M`.  They play the role of
the good elements of [CH20]. 

### `mem_light`

 An element is light iff it collides with no other element. 

### `light_subset`

 Light elements are elements. 

### `heavy_subset`

 Heavy elements are elements. 

### `Bdd.mono`

 A subset of a bounded set is bounded. 

### `bucket_of_light`

 The bucket of a light element contains nothing else. 

### `arr_of_light`

 A light element sits in the cell of its remainder. 

### `arr_mem_light_or_eq`

 A cell of the array holds a light element or padding. 

### `neg_mem_light_neg`

 Negation preserves lightness. 

### `arrXY_cases`

 A cell of the first or second array holds a light element or `pad U`. 

### `arrZ_cases`

 A cell of the third array holds `-c` for a light element `c`, or `-pad U`. 

### `arrZ_of_light`

 For a light element `c`, the third array holds `-c` in the two cells below `2M` whose index is
congruent to `-c`. 

### `abs_pad`

 The padding value has absolute value `2U + 1`. 

### `abs_arrXY_le`

 The entries of the array made from the first or the second set of a node have absolute value at
most `2U + 1`. 

### `abs_arrZ_le`

 The entries of the third array of a node have absolute value at most `2U + 1`. 

 ## One node 

### `node_correct`

 **Correctness of one node.**  Its Convolution-3SUM instance, read at any length `N ≥ 2M`, has a
solution iff the light elements of the three sets have a 3SUM solution. 

 ## The sizes of the sets along the recursion 

### `dSeq`

 The sequence `d₀ = 1`, `d_{j+1} = 2 d_j²` of [CH20], in closed form. 

### `dSeq_succ`

 The recurrence `d_{j+1} = 2 d_j²`. 

### `dSeq_mono`

 The sequence `dSeq` is nondecreasing. 

### `lt_dSeq_height`

 `d_h > n` at `h = height n`. 

### `height_pos`

 `height n` is at least 1, so the subtraction in `fuel` does not truncate. 

### `two_pow_height_le`

 `2^(height n) ≤ 2⌊log₂ n⌋ + 2`. 

### `Replaced`

 What is known about a set `T` that has been replaced `j` times by its heavy elements: its
elements have absolute value at most `U`, and there are at most `n / d_j` of them. 

### `Replaced.bdd`

 The elements have absolute value at most `U`. 

### `Replaced.card`

 There are at most `n / d_j` elements. 

### `zero`

 At the root no set has been replaced. 

### `heavy`

 One more replacement: if at most `|T|²/(2n)` elements of `T` are heavy, then these are at most
`n / d_{j+1}`. 

### `eq_empty`

 After `height n` replacements a set is empty. 

### `exists_eq_empty`

 After `3 (height n) - 2` replacements in all, one of the three sets is empty. 

 ## The recursion tree 

### `HasSol.mono`

 A solution stays a solution when the sets grow. 

### `not_hasSol_of_empty`

 If one of the three sets is empty there is no solution. 

### `hasSol_split`

 A solution consists of three light elements, or it contains a heavy one.  The brackets are those
of the list of the children in `nodes`. 

### `length_nodes_le`

 The first `f` levels of the tree have at most `(3^f - 1)/2` nodes. 

### `nodes_subset`

 The sets of a node are subsets of the sets at the root. 

### `Candidates`

 The hypotheses on the set `Q` of candidates for the two searches: primes, all at most `m`, and
enough of them for `card_heavy_modulus_le`. 

### `Candidates.prime`

 The candidates are primes. 

### `Candidates.le`

 The candidates are at most `m`. 

### `Candidates.card`

 There are at least `√(18n) Λ` candidates. 

### `candidates_primesLE`

 The primes up to `mPar n U`, among which `reduction n U` searches, meet the hypotheses. 

### `nodes_correct`

 The induction behind `reduction_correct`.  If the `i`-th set has been replaced `j_i` times, then
`f` levels of the tree are enough as soon as `f + j₁ + j₂ + j₃ ≥ 3 (height n) - 2`. 

 ## The reduction for three sets 

### `Admissible`

 The hypotheses on an input of `reduction n U`: each of the three sets has at most `n` elements,
all of absolute value at most `U`. 

### `Admissible.card₁`

 The first set has at most `n` elements. 

### `Admissible.card₂`

 The second set has at most `n` elements. 

### `Admissible.card₃`

 The third set has at most `n` elements. 

### `Admissible.bdd₁`

 The elements of the first set have absolute value at most `U`. 

### `Admissible.bdd₂`

 The elements of the second set have absolute value at most `U`. 

### `Admissible.bdd₃`

 The elements of the third set have absolute value at most `U`. 

### `Admissible.of_mem`

 The sets of a node satisfy the hypotheses that the sets at the root satisfy. 

### `reduction_correct`

 **Correctness of the reduction for three sets.**  Let the three sets have at most `n ≥ 1`
elements each, all of absolute value at most `U`, and let `N ≥ 2 * mPar n U ^ 2`.  Then 3SUM has a
solution iff the Convolution-3SUM instance of some node has one at length `N`. 

### `three_pow_fuel_le`

 A ternary tree with `fuel n` levels has polylogarithmically many nodes. 

### `length_reduction_le`

 **The reduction makes at most `(2⌊log₂ n⌋ + 2)⁵` nodes**, and each node is one instance. 

### `scan_node_le`

 The two searches of a node go through at most `m = mPar n U` primes each, and its three sets
have at most `3n` elements in all.  This bounds a number of pairs (candidate prime, element), not a
running time. 
