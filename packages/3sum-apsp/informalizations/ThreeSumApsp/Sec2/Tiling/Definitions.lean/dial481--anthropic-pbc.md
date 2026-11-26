---
{
  "module": "ThreeSumApsp/Sec2/Tiling/Definitions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Tiling/Definitions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Tiling/Definitions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Definitions for the tiling of the `N × D × N` product

* Section 2.3.4: `K₀`, the choices that the paper makes once and for all (`Layout`), bands, padding,
  row and column blocks, the matrices `X_Q` and `Y_Q` and the input arrays of a tile, and the
  position of a row or column in its band and block.
* Section 2.4.4: the output string of a position, the wanted strings of a tile, and the set of all
  tiles.


### `K0`

 Section 2.3.4: "K₀ := ⌊√K⌋". 

### `N0_pos`

 `N₀ = 3^{L-m}` is positive. 

### `K0_pos`

 `K₀ = ⌊√binom(L, m)⌋` is positive when `m ≤ L`. 

### `Layout`

 The choices that the paper makes once and for all without naming them.

* `hmL`: `m ≤ L`. The paper never states this; it follows from `L = 19m` (Section 2) and from
  `L ≥ 10m` (Section 4). It makes `K₀ ≥ 1`.
* Section 2.3.3: "we index its N₀ rows by the N₀ strings of L - m outer left variables, and its D
  columns by the D strings of m inner left variables", and similarly for a `D × N₀` matrix.
  `rowIdx`, `colIdx` and `innerIdx` say which string indexes which row or column, counted from 0.
* Section 2.3.4: "We fix K₀² ≤ K distinct subsets of {1, …, L} of size m, one for each block product
  of the grid, the same in every tile." `table (g, h)` is the subset of the block product of the
  `g`-th row block of a row band and the `h`-th column block of a column band.

Every statement about the tiling holds for every such choice. 

### `bandSize`

 The number `K₀ N₀` of rows of a row band (Section 2.3.4: a band is `K₀` consecutive blocks of
`N₀` consecutive rows), which is also the number of columns of a column band. 

### `numBands`

 The number of row bands (and of column bands) after padding: `N / (K₀ N₀)` rounded up. 

### `padN`

 Section 2.3.4: "we first pad N to a multiple of K₀ N₀".  The padded size. 

### `padRows`

 Section 2.3.4: `X` padded "with zero rows".  Rows are numbered from 0. 

### `padCols`

 Section 2.3.4: `Y` padded with "zero columns".  Columns are numbered from 0. 

### `rowBlock`

 Section 2.3.4: "Cut X into row blocks of N₀ consecutive rows".  The `B`-th row block (counted
from 0) consists of the rows `B N₀, …, B N₀ + N₀ - 1`. 

### `colBlock`

 Section 2.3.4: "and Y into column blocks of N₀ consecutive columns". 

### `bandFamilyL`

 Section 2.3.4: "In a tile, let X_Q and Y_Q be the row block and the column block of the block
product with subset Q, and let X_Q = Y_Q = 0 for the other subsets Q." The row band `β` (counted
from 0) consists of the row blocks `β K₀, …, β K₀ + K₀ - 1`. The subsets in the table are distinct,
so at most one summand is nonzero. 

### `bandFamilyR`

 The matrices `Y_Q` of a tile; they depend only on its column band `β`. 

### `bandArrayL`

 Section 2.3.4: "the left input array of a tile depends only on its row band". 

### `bandArrayR`

 Section 2.3.4: "and the right one only on its column band". 

### `bandOf`

 The band that contains row (or column) `I`. 

### `blockOf`

 The position, within its band, of the block that contains row (or column) `I`. 

### `offsetOf`

 The position of row (or column) `I` within its block. 

### `outStrOfPos`

 Section 2.4.4: "Each wanted position (I, J) ∈ W lies in one tile T and is indexed by one output
string of T, the string whose inner set is the subset Q of the block product containing (I, J) and
whose row and column are those of (I, J) within that block product". The tile is the pair
`(bandOf L m I, bandOf L m J)`, and this is the output string. 

### `wantedStrings`

 Section 2.4.4: "For each tile T, let W_T be the set of the output strings of the wanted
positions in T."  The tile `T` is given by its row band `β` and its column band `β'`. 

### `tiles`

 All the tiles: pairs of a row band and a column band. 
