---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Stages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Stages.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Stages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5: the solver, stage by stage

The text of the solver after the search for m ("The algorithm", Section 2.4.4), cut into six parts:
the shared stage; tiles, codes and digits of the wanted positions (the code of a position is its
output string, read as a number); the sort; the codes in sorted order; the pruned recursions; the
report. There is one lemma for each part together with everything that follows it (fromShared_ends
to reportCall_ends), so that each lemma ends with the lemma of the next part. The lemmas are stated
for arbitrary parameters p, matrices X, Y and positions (I i, J i) (WantedJob). The result is
fromShared_ends: from the state after the search for m the solver ends within timeFromShared steps,
with the entries of XY at the w wanted positions in the cells from out on, and nothing else below
the free pointer changed (Reported).

Every stage writes above everything that the stages before it have written, except the report, which
writes the output. So each lemma hands on what the earlier stages have left, in a memory that agrees
with the earlier one below the area just written.


 ## The local variables and the cells of the directory 

### `Expo`

 Local 10 of the solver: m. 

### `Pow4`

 Local 11 of the solver: a power of four. 

### `Levels`

 Local 12 of the solver: L = 19 m. 

### `Void`

 Local 13 of the solver: takes the results of the calls. 

### `AdrTid`

 Local 14 of the solver: the address of TID. 

### `Bands`

 Local 16 of the solver: the number of bands. 

### `AdrPerm`

 Local 22 of the solver: the address of PERM. 

### `Tiles`

 Local 23 of the solver: the number of tiles. 

### `AdrSc`

 Local 26 of the solver: the address of SC. 

### `DirOuter`

 Cell 4 of the directory: L - m. 

### `DirRoot`

 Cell 7 of the directory: K₀. 

### `DirBands`

 Cell 9 of the directory: the number of bands. 

### `DirLeaves`

 Cell 10 of the directory: 10^L. 

### `DirP10`

 Cell 17 of the directory: the address of the powers of ten. 

### `DirMask`

 Cell 21 of the directory: the address of the table of subsets. 

### `DirBand`

 Cell 22 of the directory: the address of the bands of the rows. 

### `DirDig3`

 Cell 24 of the directory: the address of the base-3 digits. 

### `DirEncA`

 Cell 26 of the directory: the address of the encodings of the row bands. 

### `DirEncB`

 Cell 27 of the directory: the address of the encodings of the column bands. 

### `DirEnd`

 Cell 30 of the directory: the end of the shared block. 

 ## The text 

### `reportCall`

 The report. 

### `fromTiles`

 The pruned recursions, and what follows. 

### `fromGather`

 The codes in sorted order, and what follows. 

### `fromSort`

 The sort, and what follows. 

### `fromWanted`

 Tiles, codes and digits of the wanted positions, and what follows. 

### `fromShared`

 The shared stage, and what follows. 

### `solverLocals`

 The local variables after the search for m.  Local 1 is D, which only the shared stage reads;
locals 3 (the bound on the entries) and 11 (a power of four) are never read.  The last seven
arguments are the values of Levels, Void, AdrTid, Bands, AdrPerm, Tiles and AdrSc. 

### `MainCallees`

 The entries of the procedures that the solver calls, all with one constant. 

### `StageLimits`

 What the stages ask of the limits; A bounds the encoded numbers. 

### `StageLimits.arith`

 What the proofs use of the limits. 

### `WantedJob`

 The task of the stages: the w wanted positions (I i, J i) are positions of the product, no two
are equal, V i is the entry of XY at the i-th of them, and the output lies below the free pointer.


### `Reported`

 What the solver has to reach: the values V are in the cells from out on, and nothing else below
the free pointer has changed since the memory μ of the call. 

 ## The times: each stage with everything that follows it 

### `timeReport`

 The report. 

### `timeFromTiles`

 The pruned recursions, whose work is at most work, and what follows. 

### `timeFromGather`

 The codes in sorted order, and what follows. 

### `timeFromSort`

 The sort, and what follows. 

### `timeFromWanted`

 Tiles, codes and digits of the wanted positions, and what follows. 

### `timeFromShared`

 The shared stage, and what follows. 

 ## The report 

### `reportCall_ends`

 **The report**: the values stand in sorted order in the cells from SV on, and π is the sorting
permutation. 

 ## The pruned recursions 

### `tilesPre`

 What the pruned recursions ask for is there after the sort: the encodings and the powers of ten
from the shared stage, the first position of each tile, and the codes in sorted order. 

### `sorted_values`

 After the pruned recursions the cells of SV hold the wanted entries in sorted order: the i-th
position in sorted order is the k-th of some tile, and there the pruned recursion returns the entry
of XY. 

### `fromTiles_ends`

 **The pruned recursions**, and what follows. 

 ## The codes in sorted order 

### `fromGather_ends`

 **The codes in sorted order**, and what follows. 

 ## The sort 

### `fromSort_ends`

 **The sort**, and what follows. 

 ## Tiles, codes and digits of the wanted positions 

### `fromWanted_ends`

 **Tiles, codes and digits of the wanted positions**, and what follows. 

 ## The shared stage 

### `fromShared_ends`

 **The shared stage**, and what follows: the whole solver after the search for m. 
