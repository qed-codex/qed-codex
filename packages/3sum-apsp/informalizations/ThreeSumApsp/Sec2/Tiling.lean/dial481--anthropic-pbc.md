---
{
  "module": "ThreeSumApsp/Sec2/Tiling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Tiling.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Tiling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tiling of the `N × D × N` product

Section 2.3.4. One run of `Full` computes `K` products of shape `N₀ × D × N₀` (Lemma 9).
To multiply an `N × D` matrix `X` by a `D × N` matrix `Y`, cut `X` into row blocks and `Y` into
column blocks of size `N₀`, group the blocks into bands of `K₀ = ⌊√K⌋` blocks, and call a row band
together with a column band a tile. Each tile is one run of `Full`, on a `K₀ × K₀` grid of block
products.

* The numbers: `K₀² ≤ K ≤ 4 K₀²` (`K0_sq_le_K`, `K_le_four_mul_K0_sq`), padding `N ≥ K₀ N₀` to
  a multiple of `K₀ N₀` at most doubles it (`le_padN`, `padN_lt_add_bandSize`, `padN_le_two_mul`),
  and there are at most `4N²/M` tiles, where `N` is the padded size (`card_tiles_mul_M_le`).
* A table of `K₀²` distinct subsets of size `m` exists (`nonempty_layout`; no later proof uses
  this).
* One run computes all the block products of a tile (`Full_bandArray_eq_block_mul`, from Lemma 9),
  and the entry `(XY)[I, J]` is the output of the run on the tile of `(I, J)` at the output string
  of `(I, J)` (`Full_bandArray_eq_mul`).
* Different positions of a tile have different output strings (`outStrOfPos_injective`).


 ### The numbers 

### `K0_sq_le_K`

 Section 2.3.4: "K₀² ≤ K". 

### `K_le_four_mul_K0_sq`

 Section 2.3.4: "K₀ ≥ √K / 2", squared. 

### `bandSize_pos`

 A band has at least one row. 

### `bandSize_dvd_padN`

 Section 2.3.4: "we first pad N to a multiple of K₀ N₀". 

### `le_padN`

 The padded size is at least `N`.

NOTE. `m ≤ L` is left implicit in the paper. For `m > L` there is no subset of size `m` and
`K₀ = 0`. 

### `padN_lt_add_bandSize`

 The padded size is the least multiple of `K₀ N₀` that is at least `N`: it is less than
`N + K₀ N₀`.

NOTE. `m ≤ L` is left implicit in the paper. 

### `padN_le_two_mul`

 Section 2.3.4: the padding "at most doubles N since N ≥ K₀ N₀". 

### `card_tiles`

 The number of tiles is the square of the number of bands. 

### `card_tiles_mul_M_le`

 Section 2.3.4: "there are (N / K₀N₀)² ≤ 4N²/M tiles", where `N` is the padded size.  The
inequality is multiplied out. 

 ### The table of subsets and the matrices of a tile 

### `nonempty_layout`

 Section 2.3.4: "We fix K₀² ≤ K distinct subsets of {1, …, L} of size m": this can be done.

NOTE.  `m ≤ L` is left implicit in the paper; it is a field of `Layout`. 

### `sum_table_eq`

 The subsets in the table are distinct, so a sum over the table that selects the subset of the
block product `gh` has one term. 

### `bandFamilyL_table`

 Section 2.3.4: "In a tile, let X_Q and Y_Q be the row block and the column block of the block
product with subset Q".  For `X_Q`: it is the `g`-th row block of the row band. 

### `bandFamilyR_table`

 The matrix `Y_Q` of the block product in position `(g, h)` is the `h`-th column block of the
column band. 

### `bandFamilyL_eq_zero`

 Section 2.3.4: "and let X_Q = Y_Q = 0 for the other subsets Q."  For `X_Q`. 

### `bandFamilyR_eq_zero`

 Section 2.3.4: "and let X_Q = Y_Q = 0 for the other subsets Q."  For `Y_Q`. 

 ### One run of `Full` for each tile 

### `Full_bandArray_eq_block_mul`

 Section 2.3.4: "Then one run of Full computes all K₀² block products of the tile (Lemma 9)".
The tile is that of the row band `β` and the column band `β'`; the block product in position `(g,
h)` of its grid is the product of the row block `β K₀ + g` by the column block `β' K₀ + h`. 

### `position_decomp`

 A row (or column) is recovered from its band, the position of its block in the band and its
position in the block. 

### `Full_bandArray_eq_mul`

 Section 2.3.4: "and running it on every tile computes all of XY." The entry `(XY)[I, J]` is the
output of the run on the tile of `(I, J)` at the output string of `(I, J)`. 

### `Mult_bandArray_eq_mul`

 The entry `(XY)[I, J]` as a value of `Mult`, that is, as a sum over leaves (equation (2)). This
is the form in which Section 4 uses the tiling ("by (2) and Lemma 9, (X_Q Y_Q)[w] is the sum of the
products at the leaves contributing to w"). 

### `bandOf_lt_numBands`

 Every row and every column lies in one of the bands.

NOTE.  `m ≤ L` is left implicit in the paper. 

 ### The output string of a position 

### `innerSetO_outStrOfPos`

 Section 2.4.4: the inner set of the output string of a position is "the subset Q of the block
product containing (I, J)". 

### `card_innerSetO_outStrOfPos`

 The inner set of the output string of a position has exactly `m` elements. 

### `outStrOfPos_injective`

 Used implicitly in Section 2.4.4 ("is indexed by one output string of T", "report […] the value
at its output string"): different positions of the same tile have different output strings. 
