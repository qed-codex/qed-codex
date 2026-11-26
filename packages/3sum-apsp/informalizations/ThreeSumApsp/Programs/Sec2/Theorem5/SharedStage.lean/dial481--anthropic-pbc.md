---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/SharedStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/SharedStage.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/SharedStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The shared stage: everything up to the encodings of all bands

shared(L, m, N, D, aX, aY, b0) fills the shared block of the memory map: the tables of powers, the
coefficients φ and ψ of Schönhage's identity (Section 2.2), the table of the K₀² subsets (Section
2.3.4), band, block and digits of every row, the digits of every column, the encodings of all row
bands of X and of all column bands of Y (Section 2.4.1), and the directory. Theorem 5 and the data
structure of Section 4 both start with it.

The body is a straight line of 36 statements and the 31 stores of the directory. It is cut into
three parts (sharedA, sharedB, sharedC). For each part there are two lemmas: one runs the text
(sharedA_spec, sharedB_spec, sharedC_spec), and one, about memories only, says that what the calls
have written is all there at the end, because each call writes above the areas of the calls before
it (SharedA.of_calls, SharedB.of_calls, SharedReady.of_calls). shared_entry puts the parts together:
if every callee meets its entry with the constant c, then shared runs within 12 c + 600 times
sharedShape (sharedTime_le). The places of the areas are those of Par.places, and their sizes those
of Par.sizes.


 ## The local variables 

### `Levels`

 Local 0 of shared: L. 

### `Inner`

 Local 1 of shared: m. 

### `Rows`

 Local 2 of shared: N. 

### `Cols`

 Local 3 of shared: D. 

### `AdrX`

 Local 4 of shared: the address of X. 

### `AdrY`

 Local 5 of shared: the address of Y. 

### `Base`

 Local 6 of shared: the base address b0 of the block. 

### `AdrP3`

 Local 7 of shared: the address of the powers of 3. 

### `AdrP4`

 Local 8 of shared: the address of the powers of 4. 

### `AdrP7`

 Local 9 of shared: the address of the powers of 7. 

### `AdrP10`

 Local 10 of shared: the address of the powers of 10. 

### `AdrPas`

 Local 11 of shared: the address of the scratch row of Pascal's triangle. 

### `AdrPhi`

 Local 12 of shared: the address of the coefficients φ. 

### `AdrPsi`

 Local 13 of shared: the address of the coefficients ψ. 

### `AdrMask`

 Local 14 of shared: the address of the table of subsets. 

### `AdrBand`

 Local 15 of shared: the address of the bands of the rows. 

### `AdrBlock`

 Local 16 of shared: the address of the blocks of the rows. 

### `AdrDig3`

 Local 17 of shared: the address of the base-3 digits. 

### `AdrDig4`

 Local 18 of shared: the address of the base-4 digits. 

### `AdrEncA`

 Local 19 of shared: the address of the encodings of the row bands. 

### `AdrEncB`

 Local 20 of shared: the address of the encodings of the column bands. 

### `AdrArr`

 Local 21 of shared: the address of the input array of a band. 

### `AdrZs`

 Local 22 of shared: the address of the scratch array of encode. 

### `AdrEnd`

 Local 23 of shared: the end of the block. 

### `Outer`

 Local 24 of shared: L - m. 

### `BlockRows`

 Local 25 of shared: N₀. 

### `Subsets`

 Local 26 of shared: K. 

### `Root`

 Local 27 of shared: K₀. 

### `Table`

 Local 28 of shared: K₀². 

### `Bands`

 Local 29 of shared: the number of bands. 

### `Leaves`

 Local 30 of shared: 10^L. 

### `Strings`

 Local 31 of shared: 7^L. 

### `Void`

 Local 32 of shared: takes the results of calls that return nothing. 

 ## The text 

### `storeLocals`

 Stores the locals of the list xs into the cells from b0 + i on. 

### `storeLocals_spec`

 **storeLocals** writes the values of the locals to the cells from base + i on, changes nothing
else, and takes 5 steps for each. 

### `sharedA`

 The first part of shared: the addresses of the first areas, the four tables of powers, and
L - m, N₀, 10^L, 7^L. 

### `sharedB`

 The second part of shared: K, K₀, K₀², the coefficients, the table of subsets, band, block and
digits of every row, the digits of every column. 

### `sharedBands`

 The number of bands: 0 if there is no row, and else one more than the band of the last row. 

### `sharedC`

 The third part of shared: the number of bands, the last addresses, the encodings of all bands,
and the directory. 

### `sharedBody`

 shared(L, m, N, D, aX, aY, b0). 

### `sharedTimeA`

 The time of the first part, if every callee meets its entry with the constant c. 

### `sharedTimeB`

 The time of the second part. 

### `sharedTimeC`

 The time of the third part. 

### `sharedLoc0`

 The locals at the start: the arguments, then zeros. 

### `sharedLocA`

 The locals after the first part; r is what the last call left in local 32. 

### `sharedLocB`

 The locals after the second part. 

### `SharedA`

 What the first part leaves in the memory. 

### `SharedB`

 What the second part leaves in the memory. 

### `SharedCallees`

 The entries of the routines that the shared stage calls, with their constants. 

### `Par.ten_T_le`

 The assumption on the word size, in terms of `T = 10^L`. 

### `SharedA.of_calls`

 What the four calls of the first part leave in the memory: each writes its own area, above the
areas of the calls before it. 

### `SharedCallees.powTable`

 The entry of pow, for a table of the powers b^0, …, b^L of a base b ≤ 10. 

### `sharedA_spec`

 **The first part of shared.** 

### `SharedB.of_calls`

 What the six calls of the second part that write to the memory leave in it (the square root
writes nothing): each writes its own area, above the areas of the calls before it, so that all the
tables are there at the end. 

### `sharedB_spec`

 **The second part of shared.** 

### `SharedTables.bandTables`

 What bandArray reads of the tables. 

### `Par.bandsArgs`

 The addresses that the shared stage hands to encodeBands: the coefficients stand at tab, and the
encodings are written from enc on. 

### `SharedTables.bandsPre`

 What encodeBands assumes holds once the tables are there, for either of the two areas enc of
encodings. 

### `nB_eq`

 The number of bands, from the band of the last row. 

### `sharedBands_spec`

 **The number of bands**: 0 if there is no row, and else one more than the band of the last
row. 

### `SharedReady.of_calls`

 What the two calls of encodeBands and the stores of the directory leave in the memory. 

### `sharedC_spec`

 **The third part of shared.** 

### `sharedTime_le`

 The time of the shared stage has the shape of its entry. 

### `SharedTables.of_parts`

 The tables of the first part are still there after the second part. 

### `shared_entry`

 **shared** meets its entry of the map: if every callee meets its entry with the constant c, then
shared does with the constant 12 c + 600. 
