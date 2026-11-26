---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Codes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Codes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Wanted/Codes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tile and the output string of each wanted position

Section 2.4.4: "Each wanted position (I, J) ∈ W lies in one tile T and is indexed by one output
string of T".  For the i-th wanted position (I, J) the routine wanted(w, L, Lo, N, K0, nB, aWI, aWJ,
band, dig3, mask, tid) writes the number BAND[I] · nB + BAND[J] of its tile to tid + i, the code
Spec.outCodeOfPos L m I J of its output string to tid + w + i, and the L digits of the code to
tid + 2 w + i L.  The code is formed by Horner's rule in base 10 while walking the mask of the
subset number BLOCK[I] · K₀ + BLOCK[J]: digit 9 at a level of the subset, and otherwise 3 x + y for
the next base-3 digits x, y of the offsets of I and J.  O(L) steps for each position.

In the paper's letters (Sections 2.3.3 and 2.3.4): D = 4^m, N₀ = 3^(L-m) is the side of a block,
K₀ = ⌊√binom(L, m)⌋ is the number of blocks along the side of a tile, and the offset of I is
I mod N₀, the place of I within its block.

A round of the loop over the positions has three parts, each with its lemma: `prepBlock_ends` (the
position, its tile and the three addresses), `levelLoop_ends` (the walk along the mask; one level is
`levelRound_ends`) and `finishBlock_ends` (the tile and the code are stored).  `wantedRound_ends`
puts them together, `wantedBody_ends` is the loop, and `wanted_entry` is the result for the callers:
a call of procedure `pWanted` does what `WantedSpec` says.


 ## The program 

### `WW`

 The number w of wanted positions. 

### `LL`

 The number L of levels. 

### `LO`

 Lo = L - m, the number of base-3 digits of an offset. 

### `NN`

 The size N. 

### `KK`

 K₀, the number of blocks along the side of a tile. 

### `NB`

 The number nB of bands. 

### `AWI`

 The rows of the wanted positions. 

### `AWJ`

 The columns of the wanted positions. 

### `BAND`

 The table BAND, followed by the table BLOCK. 

### `DIG3`

 The base-3 digits of the offsets. 

### `MASK`

 The masks of the subsets. 

### `TID`

 Where the numbers of the tiles, the codes and the digits are written. 

### `CI`

 The number i of the position. 

### `PI`

 The row I. 

### `PJ`

 The column J. 

### `AM`

 The address of the mask. 

### `AI`

 The address of the next digit of the offset of I. 

### `AJ`

 The address of the next digit of the offset of J. 

### `ACC`

 The number formed so far. 

### `LEV`

 The level. 

### `ROW`

 The address of the row of digits. 

### `DIG`

 The digit. 

### `TILE`

 The number of the tile. 

### `levelTail`

 The digit is stored and appended to the number, and the level moves on. 

### `levelDigit`

 The digit of the level: 9 at a level of the subset, and otherwise 3 x + y for the next digits
x, y of the two offsets. 

### `levelRound`

 One level of the walk along the mask. 

### `levelLoop`

 The walk along the mask. 

### `prepBlock`

 Before the walk: the position, the number of its tile, and the three addresses. 

### `finishBlock`

 After the walk: the number of the tile and the code are stored, and the counters move on. 

### `wantedBody`

 wanted(w, L, Lo, N, K0, nB, aWI, aWJ, band, dig3, mask, tid). 

### `tWanted`

 The time of wanted. 

### `Args`

 The twelve arguments of wanted. 

### `Args.w`

 The number of wanted positions. 

### `Args.L`

 The number of levels. 

### `Args.Lo`

 The number of base-3 digits of an offset. 

### `Args.N`

 The size. 

### `Args.K₀`

 The number of blocks along the side of a tile. 

### `Args.nB`

 The number of bands. 

### `Args.aWI`

 The rows of the wanted positions. 

### `Args.aWJ`

 The columns of the wanted positions. 

### `Args.band`

 The tables BAND and BLOCK. 

### `Args.dig3`

 The base-3 digits of the offsets. 

### `Args.mask`

 The masks. 

### `Args.tid`

 The output. 

### `wstate`

 The state of wanted: the arguments, the number i of the position, the address row of its row of
digits, and what the other locals hold. 

 ## The walk along one mask 

### `LevelPre`

 What the walk along one mask needs: the mask `mk` at `am`, with `m` levels in the subset and
`Lo` outside it, and the base-3 digits `rI` and `rJ` of the two offsets at `aI` and `aJ`, all below
the row of digits that it writes. 

### `LevelPre.sizes`

 The order of the regions of the memory. 

### `usedAt`

 The number of levels outside the subset among the first `l` levels: so many digits of each
offset have been used. 

### `accAt`

 The number formed by Horner's rule from the first `l` digits of the output string. 

### `digitAt`

 The digit of the output string at level `l`. 

### `LevelMem`

 The first l digits have been written, and nothing else has changed. 

### `LevelMem.write`

 One more digit is written. 

### `LevelPre.accAt_succ`

 One more digit, and the number formed from `l + 1` digits fits in a word. 

### `LevelInv`

 The invariant of the walk, before level l. 

### `levelTail_ends`

 The end of a level: the digit of level l is in DIG, and the two addresses have moved. 

### `LevelPre.readMask`

 The mask can be read at any time. 

### `levelDigit_outside`

 A level outside the subset: the digit is 3 x + y for the next digits x, y of the two offsets,
and the two addresses move on. 

### `levelDigit_ends`

 The digit of level l is formed. 

### `levelRound_ends`

 **One level of the walk.** 

### `levelLoop_ends`

 **The walk along one mask** writes the digits and leaves the number in ACC. 

 ## Before and after the walk 

### `PrepPre`

 What the block before the walk needs: the values it reads, and room for the numbers it forms.
(In, Jn) is the position, bI and bJ are its bands, gI and gJ its blocks. 

### `prepBlock_ends`

 **The block before the walk.** 

### `finishBlock_ends`

 **The block after the walk.** 

 ## One position 

### `wargs`

 The arguments of wanted. 

### `subsetNo`

 The number, among the K₀² subsets of the table, of the subset of the position (I, J). 

### `Row`

 What wanted leaves for the position number i. 

### `WantedMem`

 The first i positions are done, and only the output has changed. 

### `WantedPre.subsetNo_lt`

 The subset of a position is one of the K₀² subsets of the table. 

### `K0_mul_K0_le`

 K₀² is at most 10^(L+1), which fits in a word by the hypothesis of wanted. 

### `WantedPre.sizes`

 The order of the regions of the memory, as far as the position number i is concerned. 

### `WantedPre.prep`

 The block before the walk finds what it assumes. 

### `WantedPre.level`

 The walk finds what it assumes. 

### `WantedMem.next`

 After the walk and the two stores the position number i is done. 

### `WantedInv`

 The invariant of the loop over the positions, before the position number i. 

### `wantedRound_ends`

 **One position.** 

### `wantedBody_ends`

 **wanted** writes tile numbers, codes and digits, changes nothing else, and takes at most
tWanted w L steps. 

### `wanted_entry`

 **wanted**: in a program that has Wanted.wantedBody as procedure number pWanted, a call writes
the tile, the code and the digits of the code of each wanted position, changes no other cell, and
takes at most 86 (w + 1) (L + 1) steps. 
