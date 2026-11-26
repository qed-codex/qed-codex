---
{
  "module": "ThreeSumApsp/Sec5/Lemma37.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma37.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Lemma37.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 37, after Matoušek

Comparison counts reduce to the wanted entries of one thin matrix product: `γ(r,c) = (XY)[r,c] +
γ₂(r,c)` for `(r,c) ∈ P` (`lemma_37`), where `X` and `Y` have entries in `{0,…,d}` and inner
dimension `D'' = ⌈2nd/s⌉ + d`.  The time `O(nD'' + (|P| + nds + ds²) log n)` is not stated here,
only the number of pairs that the algorithm enumerates.  The steps are the paper's.
* Sort the numbers of each color, with the tie-breaking rule (such an order exists:
  `lemma_37_order_exists`).  Then `x < y` if and only if `pos(x) < pos(y)` (`holds_iff_pos_lt`), if
  and only if `blk(x) < blk(y)`, or `blk(x) = blk(y)` and `pos(x) < pos(y)` (`holds_iff_blk_lt_or`).
* Different blocks.  There are at most `2nd` numbers (`card_item_le`), so at most `2nd/s + d ≤ D''`
  pairs (color, block) (`card_blockPairs_le`, `div_add_le_D''`), which index the columns of `X` and
  the rows of `Y` (`lemma_37_index_exists`).  Then `(XY)[r,c]` is a sum over these pairs
  (`mul_apply_eq_sum`) and counts the pairs of the first kind (`mul_apply_eq_card`).  The entries of
  `X` and `Y` are between 0 and `d` (`entry_bounds`).
* Same block.  `γ₂` counts the pairs of the second kind (`sameBlockCount_eq_card`).  A block has
  `|I| + |J| ≤ s` numbers (`card_blockItems_le`), so at most `nds + ds²` pairs are enumerated
  (`lemma_37_enumerated`).

The steps are lemmas of the namespace `Lemma37`.


 ### The sorted order 

### `tieRank`

 The tie-breaking rule of the sort (proof of Lemma 37).  For `<`, numbers from column lists come
first among equal numbers; for `≤`, numbers from row lists come first. 

### `key`

 The key by which the numbers are sorted: the number, then the tie-breaking rule, then an
arbitrary numbering of all the numbers of the lists, which breaks the remaining ties. 

### `key_injective`

 Different numbers of the lists have different keys. 

### `pos`

 The position of `x`: the number of numbers of its color with a smaller key. 

### `pos_lt_pos`

 Among numbers of the same color, a smaller key means a smaller position. 

### `lemma_37_order_exists`

 Proof of Lemma 37: the sort can be carried out, that is, an order as described
exists. 

### `holds_iff_pos_lt`

 Proof of Lemma 37: "For x from a row list and y from a column list of the same color,
x < y holds if and only if pos(x) < pos(y).  (For ≤, we reverse the tie-breaking rule.)" 

### `holds_iff_blk_lt_or`

 Proof of Lemma 37: "Then x < y holds if and only if either blk(x) < blk(y), or blk(x) =
blk(y) and pos(x) < pos(y)." 

 ### Different blocks 

### `card_item_le`

 Proof of Lemma 37: "The lists contain at most 2nd numbers in all". 

### `sum_numOfColor`

 The numbers of the `d` colors together are all the numbers of the lists. 

### `card_blockPairs_le_sum`

 A color with `N` numbers has at most `⌊N/s⌋ + 1` blocks, so there are at most
`∑_k (⌊N_k/s⌋ + 1)` pairs (color, block). 

### `card_blockPairs_le`

 Proof of Lemma 37: "so there are at most 2nd/s + d ≤ D'' pairs (color, block)", the first
inequality. 

### `div_add_le_D''`

 Proof of Lemma 37: "2nd/s + d ≤ D''". 

### `lemma_37_index_exists`

 Proof of Lemma 37: "and we index the columns of X and the rows of Y by the pairs": an indexing
exists. 

### `sum_filter_idx`

 The column of `X` (or row of `Y`) with the index of a pair (color, block) belongs to that pair
only. 

### `mul_apply_eq_sum`

 Proof of Lemma 37: "Then (XY)[r,c] = ∑_{(k,β)} X[r,(k,β)] Y[(k,β),c] ...". 

### `card_eq_sum_card_blockPairs`

 Pairs of places in `R_r` and `C_c`, grouped by the color and the block of the number in `R_r`.


### `mul_apply_eq_card`

 Proof of Lemma 37: "... is the number of pairs (x,y) of the same color with blk(x) <
blk(y), as required". 

### `entry_bounds`

 "the entries of X and Y are between 0 and d because a list has at most d numbers": an entry is
one of the counts, or zero (padding). 

 ### Same block 

### `mem_blockRowItems`

 An entry of a row list is in `blockRowItems o s kβ` if and only if it has the color and the
block of the pair `kβ`. 

### `mem_blockColItems`

 An entry of a column list is in `blockColItems o s kβ` if and only if it has the color and the
block of the pair `kβ`. 

### `sameBlockCount_eq_card`

 Proof of Lemma 37: "Then γ₂ counts the pairs of the second kind", for the pairs (r,c) ∈
P. 

### `card_blockItems_le`

 Proof of Lemma 37: "so that |I| + |J| ≤ s".  The positions of the numbers of a block
are different and lie among `s` consecutive positions. 

### `lemma_37_enumerated`

 Proof of Lemma 37: "Since |I||J| ≤ s²/4 and there are at most 2nd/s + d blocks, we
enumerate at most (2nd/s + d)s²/4 ≤ nds + ds² pairs (x,y)". 

 ### Lemma 37 

### `lemma_37`

 **Lemma 37** (after Matoušek), the part that is not a running time.  "Let s ≥ 1 be an
integer and D'' := ⌈2nd/s⌉ + d.  Given row lists R_r and column lists C_c as above and a set P ⊆
[n]², we can build matrices X ∈ {0,…,d}^{n×D''} and Y ∈ {0,…,d}^{D''×n} and compute integers
γ₂(r,c), (r,c) ∈ P, with γ(r,c) = (XY)[r,c] + γ₂(r,c) for every (r,c) ∈ P ...  The same holds with ≤
in place of < in the definition of γ." The matrices and the integers γ₂ depend on the real numbers
only through the positions `o.pos`, in accordance with "The only operations on real numbers are the
comparisons made when sorting the numbers of each color." 
