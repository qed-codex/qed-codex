---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/SortedFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/SortedFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/SortedFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# After the sort: the codes of a tile are a segment (pure)

Section 2.4.4: "locate the output strings, and sort the sets W_T".  The wanted positions are (I i, J
i) for i < w.  Routine wanted gives each of them the number of its tile and the code of its output
string; routine sortWanted gives a permutation π of the numbers 0, …, w - 1 that sorts them by tile
and, within a tile, by code, and the table START of the numbers of positions in earlier tiles.  This
file shows what the rest of the program uses: the codes of tile number z stand, in the order of π,
in the places START[z], …, START[z+1] - 1; they are the strictly increasing list Spec.codesOf W_T;
and the value that the pruned recursion finds at such a place is the wanted entry of X Y.  No
program occurs here.


 ## A list that is sorted by a key 

### `eq_filter_append`

 A list sorted by t is the entries with t < z followed by the others. 

### `segment_eq_filter`

 In a list sorted by t, the entries with t = z are a segment. 

 ## The setting 

### `tileNo`

 The number of the tile of position number i. 

### `codeNo`

 The code of the output string of position number i. 

### `startNo`

 START[z]: the number of positions in tiles with a number below z. 

### `tileCodes`

 The codes in the places START[z], …, START[z+1] - 1 of the sorted order. 

### `wantedSet`

 The set W of the wanted positions. 

### `SortedPre`

 What is known after wanted and sortWanted: w different positions, and a permutation that sorts
them by tile and code. 

### `tileNo_lt_nT`

 The number of a tile is below nT. 

### `codeNo_lt_pow`

 A code is below 10^L. 

### `startNo_zero`

 No position lies in a tile with a number below 0. 

### `startNo_succ`

 START[z + 1] counts the positions of tile z as well. 

### `startNo_mono`

 The table START increases. 

 ## Tiles and codes 

### `band_lt`

 The number of a band is below nB. 

### `tileNo_lt`

 The number of a tile is below nT. 

### `decodeO_codeNo`

 The code of a position is the code of its output string. 

### `codeNo_lt`

 A code is below 10^L. 

### `index_eq`

 Two positions of the same tile with the same code have the same number. 

### `mem_iff`

 π lists the numbers below w. 

### `length_eq`

 π has w entries. 

### `nodup`

 No number occurs twice in π. 

### `sorted_tile`

 π is sorted by tile. 

### `length_filter_lt`

 START[z] is also the number of entries of π in tiles with a number below z. 

### `segment`

 The numbers of the positions of tile z, in the sorted order, are a segment of π. 

### `tileCodes_eq`

 The codes of tile z are the codes of the entries of π in tile z. 

### `mem_tileCodes`

 The codes of tile z are the codes of the positions in tile z. 

 ## The table START 

### `startNo_last`

 All w positions lie in tiles with a number below nT. 

 ## The codes of a tile 

### `length_tileCodes`

 Tile z has START[z + 1] - START[z] codes. 

### `tileCodes_lt`

 The codes of a tile are below 10^L. 

### `tileCodes_sorted`

 The codes of a tile are strictly increasing. 

### `tileCodes_eq_codesOf`

 The codes of the tile (β, β') are the increasing list of the codes of the set W_T. 

### `getElem_tileCodes`

 The place START[z] + k of the sorted order holds the position whose code is the k-th code of
tile z. 

 ## The value 

### `tile_value`

 The value that the pruned recursion on the tile (β, β') finds at the k-th code of the tile is
the entry of X Y at the position whose number stands at the place START[z] + k of the sorted order,
where z = β nB + β' is the number of the tile (β, β'). 

### `length_prunedList`

 The pruned recursion on a tile returns one value for each code. 

### `exists_place`

 Every place of the sorted order lies in the segment of one tile. 
