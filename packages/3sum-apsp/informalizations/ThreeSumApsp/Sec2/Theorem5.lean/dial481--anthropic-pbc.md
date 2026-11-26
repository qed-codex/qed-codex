---
{
  "module": "ThreeSumApsp/Sec2/Theorem5.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Theorem5.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 2.4.4: the algorithm of Theorem 5, its correctness and its three totals

The algorithm encodes the input arrays of all bands and then runs `Pruned(W_T)` on every tile `T`
with `W_T ≠ ∅`, where `W_T` is the set of the output strings of the wanted positions in `T`.

* Correctness (`Theorem5.correctness`): by Lemmas 10 and 7 the run on a tile returns the output of
  `Full` at the strings of `W_T`, and by Lemma 9, through the tiling, that output is the entry of
  `XY`.
* The encodings have `O(N² / D^{1/18})` entries in all, by equation (6)
  (`encodings_total_le`).
* The runs visit `O(N² / D^{1/18})` leaves in all (`Theorem5.total_leaves`): sum the second
  inequality of Lemma 11 over the tiles (`sum_card_Leaves_le`), with `∑_T |W_T| ≤ |W|`
  (`sum_card_wantedStrings_le`) and `∑_T M ≤ 4N²` (`sum_M_le`).
* The sets passed to the calls have total size at most `L + 1` times that, by Lemma 10
  (`Theorem5.total_sets`; no later proof uses this).


### `tile_mem_tiles`

 Section 2.4.4: "Each wanted position (I, J) ∈ W lies in one tile T": the tile of a position is
one of the tiles. 

### `outStrOfPos_mem_wantedStrings`

 Section 2.4.4: a wanted position "is indexed by one output string of T": its output string is in
the set `W_T` of its tile. 

### `card_innerSetO_of_mem_wantedStrings`

 Section 2.4.3: the sets passed to `Pruned` "consist only of […] output strings of length L whose
inner sets […] have exactly m elements". 

### `Theorem5.correctness`

 **Proof of Theorem 5**, correctness of the algorithm.  "for each tile T with W_T ≠ ∅,
we run Pruned(W_T), and report, for each (I, J) ∈ W, the value at its output string. This is correct
by Lemmas 9 and 10." The run on the tile of `(I, J)` reads the encodings of the input arrays of its
row band and its column band.  This holds for all `m ≤ L`. 

### `le_sq_div_sqrt_D_iff`

 Theorem 5 and Section 2.4.4: "|W| ≤ N²/√D = 2^{-m} N²".  In the statements below this
hypothesis is written without a square root, as `|W| · 2^m ≤ N²`. 

### `numBands_mul_N0_le`

 The number of bands times `N₀` is at most the padded size, because `K₀ ≥ 1`. 

### `encodings_total_le`

 Section 2.4.4: "By (6), the encodings cost (2N/K₀N₀) · O(10^L) = O(2^{-m/9} N²) operations": the
encodings of the input arrays of all row bands and all column bands have at most `4 N² / D^{1/18}`
entries in all.  Here `N` is the size of the input, which the padding at most doubles. 

### `sum_card_wantedStrings_le`

 Section 2.4.4: "Each position of W lands in one set W_T, so ∑_T |W_T| ≤ |W|". 

### `sum_M_le`

 Section 2.4.4: "there are at most 4N²/M tiles, so ∑_T M ≤ 4N²", where `N` is the padded size. 

### `sum_card_Leaves_le`

 Section 2.4.4, the display: "by Lemma 11 summed over the tiles",
`∑_T |Leaves(W_T)| ≤ 2^{-m/9} (2^m |W| + 2 ∑_T M)`. 

### `Theorem5.total_leaves`

 **Proof of Theorem 5**, the number of leaves in terms of the `N` and `D` of the theorem (`N` is
the size of the input, not the padded size).  Since `N ≥ D^18 ≥ K₀ N₀`, the padding at most doubles
`N`, so `2^m |W| + 2 ∑_T M ≤ N² + 32 N²`. 

### `sum_totalSize_le`

 Lemma 10 summed over the tiles: the total size of the sets handled by the pruned recursions is
at most `L + 1` times the total number of leaves. 

### `Theorem5.total_sets`

 **Proof of Theorem 5**, the total size of the sets, in the `N` and `D` of the theorem. 
