---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Tile.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Tile.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Tile.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The trie of one tile

Lemma 29: "Given the two encodings of a tile, we can compute the values of all these boxes, and
store them in the trie for that tile". Its proof: "We compute the values of the boxes in increasing
order of their number of stars." The routine takes a root for the trie of the tile and writes it
into the table of roots (Tile.Mem.newRoot). Then, for e = 0, …, m - t, it puts the boxes with e
stars into the trie (tileRound); for e ≥ 1 their values are sums of values looked up in the trie.
The invariant Tile.Inv says what the memory holds before the boxes with e stars; Tile.round takes it
from e to e + 1, and tile_spec is the root and the loop.


 ## The program 

### `EncA`

 The local variables of tile: the arguments aA, aB, ra, tr, fp, cur, box, L, mt; the number e of
stars, the root of the trie of the tile, and a local for a result that is not used. 

### `tileRound`

 The boxes with e stars go into the trie; on to the next number of stars. 

### `tileBody`

 tile(aA, aB, ra, tr, fp, cur, box, L, mt): a root for the trie of the tile, noted in the cell
ra; then the boxes with 0, 1, …, mt stars. The number of stars starts at 0, as all locals that are
not arguments. 

 ## The pure side 

### `room`

 Behind the root and the boxes with fewer than e stars there is room for the boxes with e
stars. 

### `time_le`

 The time: the sum over the rounds, each with the test of the loop (6 steps). 

 ## The memory during the loop 

### `Mem`

 What the memory μ' holds during the loop: the trie array T, the roots, with that of the tile
behind the older ones, and the two encodings; the cells that the routine does not own are as in
μ. 

### `Mem.newRoot`

 After the root of the tile has been taken and written behind the older roots. 

### `Mem.fill`

 After the boxes with some number of stars have been put into the trie. 

 ## The invariant and one round 

### `trieAt`

 The trie array once the root of the tile has been taken and the boxes with fewer than e stars
are in the trie. 

### `fillArgs`

 The arguments of the call of fillList for the boxes with e stars. 

### `Inv`

 The state before the boxes with e stars: the root is in its local and in its cell, and the trie
holds the boxes with fewer stars. 

### `round`

 One round puts the boxes with e stars into the trie. 

### `tile_spec`

 **tile** meets its specification. 
