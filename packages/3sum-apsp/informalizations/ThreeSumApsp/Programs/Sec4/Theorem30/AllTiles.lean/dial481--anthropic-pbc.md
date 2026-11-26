---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/AllTiles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/AllTiles.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/AllTiles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tries of all tiles

Proof of Theorem 30, "Preprocessing": "Finally, we compute the values of all the boxes of each of
the at most 4N²/M tiles". The routine `tile` builds the trie of a tile, and this routine calls it
for every tile. The tiles are taken in row-major order. Three pointers move along: the address of
the encoding of the row band, that of the column band, and the cell for the root of the tile. The
text has three parts, one inside the other: one tile (`allTilesStep`), one row of tiles
(`allTilesRow`), all rows (`allTilesBody`). The invariant `AllTiles.Inv` says what the memory holds
before the tile (β, β'); there is one lemma for each part.


 ## The program 

### `EncA`

 The local variables of `allTiles`: the arguments aENCA, aENCB, nB, T, aR, tr, fp, cur, box, L,
mt; the row band β, the column band β', the cell for the root of the tile, the address of the
encoding of the row band, that of the column band, and a local for a result that is not used. 

### `allTilesStep`

 One tile, and on to the next column band. 

### `allTilesRow`

 One row of tiles, and on to the first tile of the next row band. 

### `allTilesBody`

 allTiles(aENCA, aENCB, nB, T, aR, tr, fp, cur, box, L, mt). 

 ## The invariant and one tile 

### `triesBefore`

 The tries and the roots of the tiles before the tile (β, β'). 

### `Mem`

 What the memory μ' holds before the tile (β, β'): the tries and the roots of the tiles before
it; nothing below cur or behind the trie area has changed since μ. 

### `Inv`

 The state before the tile (β, β'): the three pointers stand at this tile, and the memory is as
Mem says. 

### `tileArgs`

 The arguments of the call of `tile` for the tile (β, β'), and the data behind them. 

### `tileCtx`

 The surroundings of the tile (β, β'). 

### `length_roots_triesBefore`

 Each tile before (β, β') has one root. 

### `tileArgs_pre`

 Before the tile (β, β') the memory holds what tile assumes. 

### `tries_tileArgs`

 The tries after the tile (β, β'). 

### `tile_meets`

 The call of `tile` for the tile (β, β') leads from the memory before this tile to the memory
before the next one. 

### `step_spec`

 One tile: the call, and the pointers move on. 

 ## One row, and all rows 

### `row_spec`

 One row of tiles. 

### `time_le`

 The time of all rows. 

### `allTiles_spec`

 **`allTiles`** meets its specification. 
