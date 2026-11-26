---
{
  "module": "ThreeSumApsp/Sec4/Theorem30.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Theorem30.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Theorem30.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Equation (7) and Theorem 30: the data structure (Section 4.3)

The running times of Theorem 30 on the word RAM are `wordRam_theorem_30` and
`wordRam_theorem_30_wanted`; the expressions inside their `O(·)` are `cost8`, `cost9` and
`costQuery`. This file has the mathematics of the paper's proof, in the paper's order.

* *The decay rate.* `ρ = 9m/(L-m+1)` is less than 1 (`sec4_rho_lt_one`), the ratio `β_d/β_{d-1}` is
  at most `ρ` (`eq_7_ratio`), and so `β_d ≤ ρ^d M` (`eq_7`). This is equation (7).
* *Preprocessing: the count behind (8).* Here `sqrtKN0 L m` is `√K N₀`. Padding at most doubles `N`
  (`Theorem30.padding`; nothing else rests on this lemma). The list of subsets takes `K L ≤ 10^L`
  operations (`Theorem30.subsets`), which the last term of (8) absorbs
  (`Theorem30.subsets_absorbed`). There are at most `4N/(√K N₀)` bands (`Theorem30.bands`), with `N`
  the given size, by a slightly finer count than `K₀ ≥ √K/2` gives (`Theorem30.numBands_mul_le`);
  the input array of a band has at most `K N₀ D ≤ 7^L` nonzero entries
  (`Theorem30.K_mul_N0_mul_D_le`), and `L · 7^L ≤ 2 · 10^L` (`Theorem30.form_array`). There are at
  most `4N²/M` tiles (`Theorem30.tiles`) with at most `(m+1) ∑_{d ≥ t} β_d` boxes each (Lemma 29),
  and `∑_{d ≥ t} β_d ≤ M ρ^t/(1-ρ)` by (7) (`Theorem30.sum_beta`), which bounds the number of all
  boxes (`Theorem30.boxes_total`). The boxes (`Theorem30.boxes_cost`), the bands
  (`Theorem30.bands_cost`) and the list add up to at most a constant times the expression in (8)
  (`Theorem30.cost8_assembly`).
* *Query.* The sum of Lemma 28 for the output string of the position `(I, J)` is `(XY)[I, J]` by
  Section 2.4.4 (`Theorem30.query`). Each box of that sum is a box of the tile (`Theorem30.lookup`),
  and the dynamic program of Lemma 29 has stored its value (`dpValue_card_starLevels`); so the query
  returns `(XY)[I, J]` (`Theorem30.correct`). Expression (9) is `|W|` queries on top of (8)
  (`Theorem30.cost9_eq`).
* *Word size.* `10^L ≤ N^{5/2}` (`Theorem30.ten_pow_le`).

Here `N` is the given size throughout, and the padded size is `padN L m N`.


 ### The decay rate `ρ` and equation (7) 

### `sec4_rho_lt_one`

 Section 4.3: `ρ = 9m/(L-m+1)` "is less than 1 since L ≥ 10m". 

### `rho_nonneg`

 The decay rate `ρ` is not negative when `L ≥ 10m`. 

### `rho_pow_div_nonneg`

 The factor `ρ^t/(1 - ρ)` of (8) is not negative when `L ≥ 10m`. 

### `eq_7_ratio`

 Equation (7), first half: for `1 ≤ d ≤ m`,
`β_d / β_{d-1} = 9(m-d+1)/(L-m+d) ≤ 9m/(L-m+1) = ρ`. 

### `eq_7`

 Equation (7), second half: "so β_d ≤ ρ^d M" (for `0 ≤ d ≤ m`). 

 ### Theorem 30, "Preprocessing": the count behind (8) 

### `sqrtKN0`

 The number `√K N₀` of the hypothesis "N ≥ √K N₀" of Theorem 30 and of the last term of (8). 

### `sqrtKN0_pos`

 `√K N₀` is positive when `m ≤ L`. 

### `sqrtKN0_sq`

 `(√K N₀)² = K N₀² = M`. 

### `sqrtKN0_le`

 `√K N₀ ≤ K N₀`, because `K ≥ 1`. 

### `cost8_eq`

 The expression (8), with `√K N₀` under its name. 

### `cost8_first_term_nonneg`

 The first term of (8) is not negative when `L ≥ 10m`. 

### `Theorem30.padding`

 Proof of Theorem 30, "Preprocessing": "padding N to a multiple of K₀ N₀, which at most doubles
it since N ≥ √K N₀ ≥ K₀ N₀". 

### `Theorem30.subsets`

 Proof of Theorem 30, "Preprocessing": "we store the K₀² subsets, in O(KL) ≤ O(10^L) operations".
Read as the inequality `K L ≤ 10^L` (constant 1). 

### `Theorem30.subsets_absorbed`

 Proof of Theorem 30, "Preprocessing": the `O(10^L)` operations for the list of subsets, which
are spent once, are within the last term of (8), because `N ≥ √K N₀`. 

### `le_choose_of_le_half`

 `binom(L, r) ≥ L` for `1 ≤ r ≤ L/2`: up to the middle the binomial coefficients increase. 

### `three_le_K0`

 `K₀ ≥ 3` in the range of Theorem 30, because `K = binom(L, m) ≥ L ≥ 10`. 

### `Theorem30.numBands_mul_le`

 The number `b` of row bands, `N/(K₀ N₀)` rounded up, satisfies `b √K N₀ ≤ 2N`. The two bounds of
the paper's proof on the numbers of bands and of tiles rest on this. If `b ≤ 2` it is the hypothesis
`N ≥ √K N₀`. If `b ≥ 3` then `(b - 1) K₀ N₀ < N`, `b ≤ 3(b - 1)/2`, and `√K ≤ K₀ + 1 ≤ 4K₀/3`. 

### `Theorem30.bands`

 Proof of Theorem 30, "Preprocessing": "all row bands and column bands, at most 4N/(√K N₀) of
them". There are `numBands L m N` row bands and as many column bands. Here `N` is the given size,
not the padded one, and the bound comes from `Theorem30.numBands_mul_le`. 

### `Theorem30.K_mul_N0_mul_D_le`

 Proof of Theorem 30, "Preprocessing": "K N₀ D ≤ 7^L". This bounds the number of nonzero entries
of the input array of a band, which is why forming it takes `O(L · 7^L)` operations. 

### `Theorem30.form_array`

 Proof of Theorem 30, "Preprocessing": forming the input array of a band takes "O(L · 7^L)
operations", which is within the "O(10^L) operations" of its encoding ("This is the last term of
(8)"). Read as the inequality `L · 7^L ≤ 2 · 10^L`; the constant 1 fails at `L = 3`. From `L = 3`
on, one more level multiplies the left-hand side by `7(L+1)/L ≤ 10`. 

### `Theorem30.tiles`

 Proof of Theorem 30, "Preprocessing": "the at most 4N²/M tiles, where M = K N₀² is the number of
output entries of a tile". There are `(numBands L m N)²` tiles. Here `N` is the given size, and the
bound comes from `Theorem30.numBands_mul_le`. 

### `Theorem30.sum_beta`

 Proof of Theorem 30, "Preprocessing": "∑_{d ≥ t} β_d ≤ M ρ^t / (1 - ρ) by (7)". The sum is over
`t ≤ d ≤ m`, as in Lemma 29. 

### `Theorem30.boxes_total`

 Proof of Theorem 30, "Preprocessing", "which gives the first term": the number of boxes of all
tiles together is at most `4 (m+1) ρ^t/(1 - ρ) N²`. 

### `Theorem30.boxes_cost`

 The first term of (8): `L` operations for each box of each tile. 

### `Theorem30.bands_cost`

 The last term of (8): `10^L + L · 7^L` operations for each row band and each column band. 

### `Theorem30.cost8_assembly`

 **Theorem 30**, expression (8), as a count: the three parts of the preprocessing added up. `L`
operations for each box of each tile, `10^L + L · 7^L` for each row band and column band, and `K L`
for the list of subsets, are together at most 13 times the expression inside the `O(·)` of (8). The
count uses the hypotheses `m ≥ 1` (for `m + 1 ≤ 2m`, and for the numbers of bands and of tiles) and
`N ≥ √K N₀` of Theorem 30. 

 ### Theorem 30, "Query": a query returns `(XY)[I, J]` 

### `Theorem30.query`

 Proof of Theorem 30, "Query". "Given (I, J), we find its tile from the bands of row I and column
J, the subset Q of its block product, and its output string w […]. We then compute (X_Q Y_Q)[w] as
the sum in Lemma 28 […]. By Section 2.4.4, the sum is (XY)[I, J]." Here `a` and `b` are the input
arrays of the row band of `I` and of the column band of `J`, and `lay` is any choice of the indexing
bijections and of the subsets of the block products; it carries `m ≤ L`. (The hypotheses `m ≥ 1`,
`L ≥ 10m` and `N ≥ √K N₀` of Theorem 30 are not needed for correctness.) 

### `Theorem30.lookup`

 Proof of Theorem 30, "Query": "for every V ⊆ Q with |V| = m - t and every box of 𝓑_V, we look up
its value in the trie of the tile." It is there: it is a box. 

### `dpValue_card_starLevels`

 What the dynamic program of Lemma 29 computes for a box, at the number of stars of the box, is
the value of the box. 

### `queryValue`

 A query, as in the proof of Theorem 30, for the output string `η` of the queried position,
reading only the two encodings of the tile and the stored values of its boxes: "for each such leaf τ
we look up its two numbers Φ_τ(a) and Ψ_τ(b) in the encodings of the tile and multiply them. The
second part is the sum of the values of the boxes of w: for every V ⊆ Q with |V| = m - t and every
box of 𝓑_V, we look up its value in the trie of the tile." The value stored for a box `π` with `e`
stars is the one that the dynamic program computed, `dpValue encA encB e π`. 

### `Theorem30.correct`

 **Theorem 30**, correctness of the data structure from end to end: the preprocessing computes
the encodings of the bands and, from them, the values of the boxes of every tile by the dynamic
program of Lemma 29; a query for `(I, J)` reads only the two encodings of its tile and the stored
values of boxes, and returns `(XY)[I, J]`. 

### `Theorem30.cost9_eq`

 Proof of Theorem 30, "Query": "For a set W, we ask |W| queries, which gives (9)." 

 ### Theorem 30, "Word size" 

### `Theorem30.ten_pow_le`

 Proof of Theorem 30, "Word size": "Since N ≥ N₀ = 3^{L-m} and L ≥ 10m, we have 10^L ≤ N^{5/2}".
Stated after squaring, to stay in the natural numbers. 
