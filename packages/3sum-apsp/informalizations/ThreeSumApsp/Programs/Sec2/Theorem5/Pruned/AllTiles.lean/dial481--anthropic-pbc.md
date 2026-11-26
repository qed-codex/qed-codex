---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/AllTiles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/AllTiles.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/AllTiles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 as a program: the pruned recursion on every tile

Section 2.4.4: "for each tile T with W_T ≠ ∅, we run Pruned(W_T)".

The wanted positions have been sorted by tile and, within a tile, by code.  The codes of the tile
number t = β nB + β' are the cells START[t], …, START[t+1] - 1 of SC.  runTiles walks over all
tiles; for each tile with START[t] < START[t+1] it calls the pruned recursion on the encodings of
the row band β and of the column band β', and the values land in the same cells of SV.

* The memory.  `TilesInv` says which tiles are done.  What the call for a tile assumes holds
  (`TilesPre.tile`), and the call finishes the tile (`TilesInv.of_call`); a tile without wanted
  positions is finished as it is (`TilesInv.of_empty`).
* The program.  `runTile_ends` treats one tile, `runTilesInner_ends` the tiles of a row band,
  `runBand_ends` a row band, and `runTiles_entry` all of them.


 ## What the callers may assume

`RunTilesSpec` says what a call of procedure `pRunTiles` does, and in how many steps: a constant c
times a shape that depends on the sizes. 

### `tileWork`

 The work of the pruned recursion on a tile: nothing if the tile has no wanted position. 

### `tilesShape`

 The shape of the running time of runTiles. 

### `TilesArgs`

 The arguments of runTiles, with the data behind them.  EA β and EB β' are the encodings of the
bands, which stand at enca and encb, one behind the other; s t = START[t]; codes t are the codes of
tile t; w is the number of wanted positions; A and B bound the numbers in the encodings. 

### `TilesArgs.vals`

 The values of the arguments of runTiles. 

### `TilesPre`

 What runTiles assumes.  Everything that is read lies below SV; then come the w cells of SV and,
from sp on, the stack of the pruned recursion. 

### `RunTilesSpec`

 runTiles(nB, L, T, enca, encb, start, sc, sv, sp, p10), with T = 10^L: for every tile (β, β')
the values of the pruned recursion at the codes of the tile, in the cells of SV that correspond to
the cells of SC with these codes.  Only the w cells of SV and the stack may have changed. 

 ## The program 

### `NB`

 The number nB of bands. 

### `LL`

 The number L of levels. 

### `TT`

 T = 10^L, the length of an encoding. 

### `PEA`

 The encoding of the row band β. 

### `ENCB`

 The encodings of the column bands. 

### `PST`

 The address of START[t]. 

### `SC`

 The codes, sorted. 

### `SV`

 The values. 

### `SP`

 The stack of the pruned recursion. 

### `P10`

 The table of the powers of ten. 

### `CB`

 The row band β. 

### `CC`

 The column band β'. 

### `PEB`

 The encoding of the column band β'. 

### `S0`

 START[t]. 

### `S1`

 START[t + 1]. 

### `RES`

 A result that is not used. 

### `runTile`

 One tile: the pruned recursion is called if the tile has wanted positions; then the column band,
its encoding and the address of START[t] move on. 

### `runTilesInner`

 The tiles of one row band. 

### `runBand`

 One row band. 

### `runTilesBody`

 runTiles(nB, L, T, enca, encb, start, sc, sv, sp, p10). 

 ## The memory 

### `s_mono`

 The table START increases. 

### `s_le_w`

 The entries of START are at most w. 

### `keep`

 What runTiles reads lies below SV. 

### `lvals`

 The list of the values of a tile is as long as the list of its codes. 

### `window_le`

 The window of a tile that comes before the tile (β, i) ends at or before the window of that
tile. 

### `TilesInv`

 The memory when the tiles before (β, i) are done: only SV and the stack have changed, and the
windows of the tiles that are done hold their values. 

### `TilesPre.unchanged`

 What is read has not changed. 

### `TilesArgs.tile`

 The arguments of the call of pruned for the tile (β, i). 

### `TileSizes`

 The arithmetic of the tile (β, i): its window lies within the w cells, its two encodings within
the encodings of all bands, and its stack within the stack for w codes. 

### `TilesPre.sizes`

 The inequalities of the tile (β, i) follow from what runTiles assumes. 

### `TilesPre.tile`

 What the call for the tile (β, i) assumes holds. 

### `TilesInv.of_call`

 After the call the tile (β, i) is done. 

### `TilesInv.of_empty`

 A tile without wanted positions is done as it is. 

### `TilesInv.next_band`

 When the tiles of the row band β are done, the next row band begins. 

 ## One tile 

### `tilesState`

 The state of runTiles: pa, pt and pb are the addresses of the encoding of the row band, of
START[t] and of the encoding of the column band; s0, s1 and res are what the locals S0, S1 and RES
hold. 

### `TileLoop`

 The invariant of the loop over the tiles of the row band β, before the tile (β, i). 

### `runTileTail_ends`

 The end of a round: the column band, its encoding and the address of START[t] move on. 

### `runTile_ends`

 **One tile.** 

 ## The two loops 

### `innerTime`

 The time of the tiles of one row band. 

### `runTilesInner_ends`

 The tiles of one row band. 

### `BandLoop`

 The invariant of the loop over the row bands, before the row band β. 

### `runBand_ends`

 **One row band.** 

### `sum_innerTime_le`

 The time of the loop over the row bands is within the shape. 

### `runTiles_entry`

 **runTiles** does what `RunTilesSpec` says: for every tile the values of the pruned recursion
stand in SV, and only SV and the stack have changed.  The constant of the time is that of the pruned
recursion plus 60. 
