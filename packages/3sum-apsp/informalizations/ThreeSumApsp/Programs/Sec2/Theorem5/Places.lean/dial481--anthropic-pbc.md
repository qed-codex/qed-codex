---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Places.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Places.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Places.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: sizes and places

The sizes of the tables and arrays of Theorem 5's program, and their places in the memory. No
program occurs here.

The program for Theorem 5 (the solver) and the data structure of Section 4 begin with the same
stage, the shared stage, which fills the shared block: a directory of 32 cells with the sizes and
the addresses of the areas (`dirList`), then the tables, then the encodings of all bands, then two
scratch areas. The solver has a private block behind it. The areas lie one after the other:
`Par.places` (the shared block) and `Par.places5` (the private block) say where every area begins
and ends. `Par.sizes` collects the inequalities between the sizes, each of which has a name of its
own.


 ## Sizes 

### `Par`

 The parameters of the recursion and of the matrices: `L` levels, `m` of them inner, matrices
`N × D` and `D × N` with `D = 4^m`. 

### `Par.L`

 The number of levels of the recursion. 

### `Par.m`

 The number of inner levels. 

### `Par.N`

 The number of rows of `X` and of columns of `Y`. 

### `D`

 `D = 4^m`. 

### `Lo`

 The number `L - m` of outer levels. 

### `N0`

 `N₀ = 3^{L-m}`. 

### `K`

 `K = binom(L, m)`. 

### `K0`

 `K₀ = ⌊√K⌋`. 

### `KK`

 The number `K₀²` of subsets in the table. 

### `nB`

 The number of row bands, and of column bands. 

### `nT`

 The number of tiles. 

### `T`

 The number `10^L` of leaves: the length of an encoding. 

### `S7`

 The number `7^L` of left strings: the length of an input array. 

 ## The shared block, from its base address `b0` on 

### `aDIR`

 The directory: 32 cells, see `dirList`. 

### `aP3`

 Powers of 3: `L + 1` cells. 

### `aP4`

 Powers of 4: `L + 1` cells. 

### `aP7`

 Powers of 7: `L + 1` cells. 

### `aP10`

 Powers of 10: `L + 1` cells. 

### `aPAS`

 Scratch for a row of Pascal's triangle: `L + 2` cells. 

### `aPHI`

 The coefficients `φ_λ(s)`: 70 cells, row `λ` at `7 λ`. 

### `aPSI`

 The coefficients `ψ_λ(t)`: 70 cells. 

### `aMASK`

 The table of subsets: `K₀²` rows of `L` bits, the subset of the block product `(g, h)` in row
`g K₀ + h`. 

### `aBAND`

 The band of every row: `N` cells. 

### `aBLOCK`

 The block, within its band, of every row: `N` cells. 

### `aDIG3`

 The base-3 digits of the offset of every row within its block: `N` rows of `L - m` cells, most
significant digit first. 

### `aDIG4`

 The base-4 digits of every column of `X`: `D` rows of `m` cells, most significant digit first.


### `aENCA`

 The encodings of the row bands: band `β` at `β 10^L`. 

### `aENCB`

 The encodings of the column bands. 

### `aARR`

 The input array of the band that is being encoded: `7^L` cells.  Dead after the shared stage.


### `aZS`

 Scratch of the recursive encoding: `7^L` cells (`7^{L-1} + … + 1` are used). Dead after the
shared stage. 

### `sharedEnd`

 The first address after the shared block. 

### `dirList`

 The content of the first 31 cells of the directory (the shared stage does not use the last one);
`aX` and `aY` are the addresses of `X` and `Y`. 

 ## The private block of Theorem 5

The solver receives `N`, `D`, the number `w` of wanted positions, a bound `U` on the entries, the
addresses of `X`, `Y` (row by row), of the rows `WI` and the columns `WJ` of the wanted positions
and of the output, and as last argument the free pointer `fr`. All inputs and the output lie below
`fr`. The solver may write the output and the cells from `fr` on, and nothing is assumed about these
cells: a routine clears what it needs cleared. The shared block starts at `fr`, the private block
follows it. 

### `aTID`

 The tile number `band(I) nB + band(J)` of every wanted position: `w` cells. 

### `aCODE`

 The code of the output string of every wanted position: `w` cells. 

### `aDGT`

 The `L` digits of the code of the output string of every wanted position, most significant
first: `w` rows of `L` cells. 

### `aPERM`

 The permutation that sorts the wanted positions by tile and, within a tile, by code: `w` cells.


### `aPERM2`

 The second buffer of the sort: `w` cells. 

### `aCNT`

 The counters of the sort: `nT + 11` cells. 

### `aSTART`

 For every tile the number of wanted positions in earlier tiles: `nT + 1` cells. 

### `aSC`

 The codes in sorted order: `w` cells. 

### `aSV`

 The values in sorted order: `w` cells. 

### `aSTK`

 The stack of the pruned recursion: `L` frames of at most `3 w + 11` cells. 

### `end5`

 The first address that Theorem 5's program does not use. 

### `cells5`

 The number of cells, from the free pointer on, that Theorem 5's program uses. 

 ## The places and the sizes, as equations and inequalities 

### `Par.places`

 The places of the shared block: each area begins where the one before it ends. 

### `two_pow_le_T`

 `2^L ≤ 10^L`. 

### `KK_le_K`

 `K₀² ≤ K`. 

### `sizes`

 The sizes: 1, `L`, `2^L`, `K`, `N₀` and `D` are at most `T = 10^L`; `K₀` and `K₀²` are at most
`K`; `K₀` and `N₀` are positive; and the definition of `Lo`. 

### `Par.places5`

 The places of the private block of Theorem 5, which follows the shared block. 
