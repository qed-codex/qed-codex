---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Sort.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Sort.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Sort.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: sorting the wanted positions

sortWanted(w, L, nT, tid, dgt, perm): "sort the sets W_T" (Section 2.4.4), by a radix sort of the
indices 0, …, w - 1, in O((L + 1) (w + 10) + nT) steps.  The routine writes the list 0, …, w - 1 to
perm (swInit_ends).  Then, unless w = 0, it makes L stable passes on the stored digits of the codes,
the last digit first: after r of them the list is sorted by the last r digits (swDigit_ends for one
pass, swDigits_ends for all).  One more pass, on the numbers of the tiles, sorts the list by tile
and code and leaves the number of positions in the tiles below s, for every s (swTiles_ends).
sortWantedBody_ends puts the parts together, and sortWanted_entry is the specification
SortWantedSpec that the callers use.


 ## The program 

### `Num`

 The local variables of sortWanted: the arguments w (Num), L (Levels), nT (Tiles), tid (TileOf),
dgt (Digits), perm (Perm); a counter (Idx); the unused results of the calls (Res).  A pass
(radixPass) reads w and perm from the locals 0 and 5 and writes to local 7, which are Num, Perm and
Res. 

### `swInit`

 perm[i] := i for i < w. 

### `swDigit`

 The pass on the digit whose index is in the counter. 

### `swDigits`

 The passes on the digits L - 1, …, 0. 

### `swTiles`

 The pass on the numbers of the tiles. 

### `sortWantedBody`

 sortWanted(w, L, nT, tid, dgt, perm).  For w = 0 there are no passes on the digits: only for
w > 0 do the assumptions say that L fits in a word. 

 ## What is assumed, and the state between the passes 

### `Args.state`

 A state of sortWanted: the arguments, the counter i, the last result r, and the memory. 

### `SwSorted`

 The list π at perm is a rearrangement of 0, …, w - 1 that is sorted by g, and only the room
cells from perm on have changed. 

### `SwState`

 The state between two passes: the counter is i, and the list at perm is sorted by g. 

### `SwSorted.length`

 The list has w entries. 

### `SwSorted.lt`

 The entries of the list are below w. 

 ## The list 0, …, w - 1 

### `SwInitInv`

 The first j cells of perm hold 0, …, j - 1, and nothing outside the w cells from perm has
changed. 

### `swInit_ends`

 swInit: the list 0, …, w - 1 stands at perm; it is sorted by the last 0 digits. 

 ## The passes on the digits 

### `digit_from_end`

 The digit with index L - 1 - r is the digit number r from the least significant. 

### `SortWanted.Args.digitPass`

 The layout of the pass on digit number r from the least significant. 

### `SwSorted.digitPre`

 What the pass on digit number r assumes: the digits still stand where they stood. 

### `SwSorted.digit_succ`

 After the pass on digit number r, a list that was sorted by the last r digits is sorted by the
last r + 1 digits. 

### `swDigit_ends`

 One pass: the counter holds the index L - 1 - r of digit number r. 

### `swDigits_ends`

 swDigits: after the L passes the list is sorted by the codes. 

 ## The pass on the tiles 

### `SortWanted.Args.tilePass`

 The layout of the pass on the numbers of the tiles. 

### `SwSorted.tilePre`

 What the pass on the tiles assumes: the numbers of the tiles still stand where they stood. 

### `SwDone`

 What sortWanted achieves: the list at perm sorts the positions by tile and code, the cell s
after the scratch space holds the number of positions in the tiles below s, and only the room cells
from perm on have changed. 

### `SwSorted.tile_succ`

 After the pass on the tiles, a list that was sorted by the codes is sorted by tile and code, and
the counters of the pass count the positions in the tiles below s. 

### `swTiles_ends`

 swTiles: the last pass. 

 ## The routine 

### `sortWantedBody_ends`

 The body of sortWanted achieves SwDone; the time is the sum of the times of the three parts and
of the test. 

### `sortWanted_entry`

 **sortWanted** meets its entry of the map, with the constant 97. 
