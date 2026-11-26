---
{
  "module": "ThreeSumApsp/Sec4/Lemma27_28.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Lemma27_28.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Lemma27_28.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemmas 27 and 28: the boxes of an output string (Section 4.2)

Let `η` be an output string (the paper's w) with inner set `Q` of `m` levels. A leaf `τ`
contributing to `η` chooses `P₀` at the set `Z` of levels of `Q`; `V` is `Z` padded from the bottom
to `m - t` levels; `F_V` is the longest initial segment of `Q` contained in `V`; and `𝓑_V` is the
set of the cubes with stars at `F_V`, with `P₀` at `V ∖ F_V`, with one of the nine terms `P_ij` at
each level of `Q ∖ V`, and with the terms of the private leaf of `η` outside `Q`. The file follows
the paper's order, except that Figure 10 comes after the definitions that it illustrates.

* *The sets `Z`, `V`, `F_V`.* The set `V` has `m - t` levels (`card_Vof`). The definition of `F_V`
  is the printed one (`FV_eq`). The condition `V ∖ F_V ⊆ Z` says that every level of `V ∖ Z` is
  below every level of `Q ∖ V` (`sdiff_FV_subset_iff`); this carries Lemma 27.
* *The sets `𝓑_V`.* They have `9^t` cubes (`card_BV`), which are boxes (`BV_isBox`), and they are
  disjoint (`BV_pairwiseDisjoint`). The box of a leaf is in `𝓑_V` for the `V` of the leaf
  (`boxOfLeaf_mem_BV`). A leaf contributing to `η` is a leaf of a box of `𝓑_V` if and only if
  `V ∖ F_V ⊆ Z ⊆ V` (`exists_mem_BV_leaf_iff`), and then of exactly one (`BV_leaf_unique`).
* *Figure 10*, for `m = 4` and `t = 2` (`figure_10_counts`, `figure_10_rows`, `figure_10_Vof`).
* **Lemma 27** (`lemma_27`): for `|Z| ≤ m - t`, the only `V` of `m - t` levels with
  `V ∖ F_V ⊆ Z ⊆ V` is `Z` padded from the bottom.
* **Lemma 28**: the leaves of order at least `t` contributing to `η` are the leaves of the boxes of
  the sets `𝓑_V` (`lemma_28_leaves`), and each of them lies in exactly one box (`lemma_28_unique`).
  So a sum over the leaves contributing to `η` splits into the leaves of order below `t` and the
  boxes (`Lemma28.sum_contributing`). For the products at the leaves this is the equation of the
  lemma (`lemma_28`), and for the constant 1 it counts the leaves (`Lemma28.card_leaves`). The
  numbers of terms are `∑_{d < t} α_d` and `α_t` (`lemma_28_counts`).


 ### The sets `Z`, `V` and `F_V` (Section 4.2) 

### `Zof`

 Section 4.2: "Z := {ℓ ∈ Q : τ_ℓ = P₀} (the levels at which τ chooses P₀)". 

### `contributes_iff_eq_privateLeaf`

 Section 2.4.3: a leaf contributes to `η` exactly if it agrees with the private leaf of `η`
outside the inner set. 

### `privateLeaf_ne_P0`

 Outside the inner set the private leaf does not choose `P₀`. 

### `Zof_subset`

 `Z` is a set of levels of `Q`. 

### `P0Levels_eq_Zof`

 A leaf contributing to `η` chooses `P₀` exactly at the levels of `Z`. 

### `order_eq_sub_card_Zof`

 Section 4.2: "the order of τ is m - |Z|", for a leaf `τ` contributing to an output string `η`
with inner set `Q`. 

### `card_Zof_le`

 A leaf of order at least `t` contributing to `η` chooses `P₀` at most `m - t` times. 

### `Vof_subset`

 `V` is a set of levels of `Q`. 

### `card_Vof`

 Section 4.2: "the set V has exactly m - t levels". 

### `Vof_sdiff_lt`

 `V` is `Z` "padded from the bottom" (Section 4.2): the levels added to `Z` are below the levels
of `Q` that are left out. 

### `FV_eq`

 Section 4.2: the definition `FV` agrees with the paper's two cases: "F_V := {ℓ ∈ Q : ℓ < min(Q ∖
V)}", "with F_V := Q if V = Q". 

### `FV_subset`

 Section 4.2: `F_V` "is the longest initial segment of Q contained in V". Here: it is contained
in `V`. 

### `mem_FV_of_le`

 Section 4.2: `F_V` "is the longest initial segment of Q contained in V". Here: it is an initial
segment of `Q`. 

### `sdiff_FV_subset_iff`

 The core of the proof of Lemma 27: "V ∖ F_V ⊆ Z says that every level of V ∖ Z is below" the
lowest level, that is every level, of `Q ∖ V`. The paper's case `V = Q` needs no separate treatment:
then `Q ∖ V` is empty. 

 ### The sets `𝓑_V` (Section 4.2) 

### `BV_star`

 A cube of `𝓑_V` has a star at each level of `F_V`. 

### `BV_P0`

 A cube of `𝓑_V` has `P₀` at each level of `V ∖ F_V`. 

### `BV_nine`

 A cube of `𝓑_V` has one of the nine terms `P_ij` at each level of `Q ∖ V`. 

### `BV_outside`

 A cube of `𝓑_V` has the term of the private leaf of `η` at each level outside `Q`. 

### `level_cases`

 Every level is of one of the four kinds in the definition of `𝓑_V`. 

### `BV_starLevels`

 The stars of a cube of `𝓑_V` are at the levels of `F_V`. 

### `BV_P0Levels`

 The symbols `P₀` of a cube of `𝓑_V` are at the levels of `V ∖ F_V`. 

### `BV_starLevels_union_P0Levels`

 The levels at which a cube of `𝓑_V` has a star or `P₀` are those of `V`. 

### `BV_ext`

 Two cubes of `𝓑_V` with the same symbols at the levels of `Q ∖ V` are equal. 

### `BV_eq_term_of_leaf`

 At a level of `Q ∖ V`, a cube of `𝓑_V` has the term of each of its leaves. 

### `allowed`

 The symbols allowed at level `ℓ` in a cube of `𝓑_V`. 

### `BV_eq_piFinset`

 `𝓑_V` is the set of all cubes with an allowed symbol at every level. 

### `card_allowed`

 Nine symbols are allowed at a level of `Q ∖ V`, and one at every other level. 

### `card_BV`

 Section 4.2: `𝓑_V` is "the set of the 9^t cubes π with" the symbols above. 

### `BV_isBox`

 Section 4.2: "Every cube in 𝓑_V is a box: it satisfies condition (i) of the definition because
it has |V| = m - t symbols P₀ or stars, and condition (ii) because its stars are below its symbols
P₀, since F_V is an initial segment of Q." 

### `BV_pairwiseDisjoint`

 The sets `𝓑_V` for different `V` are disjoint, so that the double sum `∑_V ∑_{π ∈ 𝓑_V}` of Lemma
28 runs over each box of `⋃_V 𝓑_V` once. 

### `starAt_mem_BV`

 If `τ` contributes to `η` and `V ∖ F_V ⊆ Z ⊆ V`, then `τ` with stars at the levels of `F_V` is a
cube of `𝓑_V`. 

### `boxOfLeaf`

 Section 4.2: the box of a leaf `τ` of order at least `t` contributing to `η`: "The box of τ then
agrees with τ everywhere, except that it has a star at every level of Q below the level where we
stopped", these levels being those of `F_V` for the `V` of `τ`. 

### `mem_leaves_boxOfLeaf`

 A leaf is a leaf of its box. 

### `boxOfLeaf_mem_BV`

 Section 4.2: "When V is the set defined above from a leaf τ, the box of τ is the one in 𝓑_V with
the terms of τ at the levels of Q ∖ V": it is a cube of `𝓑_V`, for the set `V` of `τ`. 

### `exists_mem_BV_leaf_iff`

 Section 4.2: "A leaf contributing to w that chooses P₀ at the set Z of levels is a leaf of a box
of 𝓑_V if and only if it chooses P₀ at every level of V ∖ F_V and at no level of Q ∖ V, that is, V ∖
F_V ⊆ Z ⊆ V". 

### `BV_leaf_unique`

 Section 4.2: "Furthermore, it is a leaf of exactly one of these boxes, namely, the one with its
terms at the levels of Q ∖ V." 

 ### Figure 10 

### `figure_10_counts`

 Figure 10, for `m = 4` and `t = 2`: "these 6 · 81 = 486 = α₂ boxes contain each of the
α₂ + α₃ + α₄ = 9963 leaves of order at least 2". 

### `figure_10_rows`

 Figure 10, the six rows, with the four levels `ℓ₁ < ℓ₂ < ℓ₃ < ℓ₄` of `Q` taken as
`0, 1, 2, 3`: the levels of `F_V`, which carry the stars; and the column "leaves per box" adds up,
over the 81 boxes of each row, to `81 · (10² + 10 + 10 + 1 + 1 + 1) = 9963`. (Here 81 and the powers
of ten are numerals.) 

### `figure_10_Vof`

 Figure 10, column "sets Z of its leaves": the row `V` in which each set `Z` of at most
one level appears. (A set `Z` of two levels appears in the row `V = Z`; these six cases are not
written out.) 

 ### Lemma 27 

### `lemma_27`

 **Lemma 27**. "Let Q be a set of m levels, and let 0 ≤ t ≤ m. For every Z ⊆ Q
with |Z| ≤ m - t, there is exactly one set V ⊆ Q with |V| = m - t and V ∖ F_V ⊆ Z ⊆ V, namely Z
together with the m - t - |Z| lowest levels of Q ∖ Z." This set is `Vof m t Q Z`. 

 ### Lemma 28 

### `lemma_28_leaves`

 **Lemma 28**, first sentence, first half. "Let w be an output string, with inner set
Q. The leaves of order at least t contributing to w are exactly the leaves of the boxes in ⋃_V 𝓑_V,
the union over all V ⊆ Q with |V| = m - t". 

### `eq_Vof_of_mem_leaves`

 Proof of Lemma 28: "By Lemma 27, exactly one V satisfies this condition": if a leaf of order at
least `t` contributing to `η` is a leaf of a box of `𝓑_V`, then `V` is the set of the leaf. 

### `lemma_28_unique`

 **Lemma 28**, first sentence, second half: "and each of them is a leaf of exactly one
of these boxes." 

### `Lemma28.sum_contributing`

 The equation of Lemma 28 for an arbitrary function `g` of the leaves in the place of the
products: the sum of `g` over the leaves contributing to `η` is the sum over the leaves of order
below `t` plus the sum over the leaves of the boxes. 

### `Lemma28.Mult_eq_querySum`

 **Lemma 28**, the displayed equation, for arbitrary input arrays: the sum of the products at the
leaves contributing to `η`, which is `Mult(a, b)[η]`, equals the sum over the leaves of order below
`t` plus the sum of the values of the boxes. See `lemma_28` for the form with `(X_Q Y_Q)[η]` on the
left. 

### `lemma_28`

 **Lemma 28**, the displayed equation. "Hence (X_Q Y_Q)[w] = ∑_{τ contributing to w, of
order < t} Φ_τ(a) Ψ_τ(b) + ∑_{V ⊆ Q, |V| = m - t} ∑_{π ∈ 𝓑_V} val(π)", for the input arrays `a`, `b`
built from the matrices `X_Q`, `Y_Q` as in Section 2.3.3. The right-hand side is `querySum`. 

### `Lemma28.card_leaves`

 The terms of the sum of Lemma 28 stand for the `10^m` leaves contributing to `η`, each of them
once: one leaf for each product, and its leaves for each box. The bound on the partial sums of a
query (word size, the proof of Theorem 30) rests on this count. 

### `lowLeaves_eq_biUnion`

 The leaves of order below `t` contributing to `η`, sorted by their order, which is at least 0.


### `lemma_28_counts`

 **Lemma 28**, last line: "a sum of ∑_{d=0}^{t-1} α_d products and α_t values of
boxes."  The third clause says that these α_t cubes are different, that is, that the sets 𝓑_V are
disjoint; Section 4.2 has it in the words "w has exactly α_t boxes". 

### `lemma_28_boxes`

 Section 4.2, on the cubes of 𝓑_V, which Lemma 28 calls "the boxes in ⋃_V 𝓑_V": "Every cube in
𝓑_V is a box: it satisfies condition (i) of the definition because it has |V| = m - t symbols P₀ or
stars, and condition (ii) because its stars are below its symbols P₀, since F_V is an initial
segment of Q."  Moreover "a box of 𝓑_V has stars at the levels of F_V", so it is one of the boxes
with |F_V| stars (`boxesWithStars`). 
