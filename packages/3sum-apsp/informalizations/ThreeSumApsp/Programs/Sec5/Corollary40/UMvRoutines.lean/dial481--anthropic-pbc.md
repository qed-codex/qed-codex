---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/UMvRoutines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/UMvRoutines.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/UMvRoutines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# uMv-hinted uMv: the routines of Phases 3 and 4

Proof of Corollary 40.  Phase 3 writes Y := N_{I,J} and builds, for blocks of t₂
consecutive rows of U, the data structure for the product of the block with Y.  Phase 4 asks it for
the entries (i, ℓ) of U N_{I,J} with V[ℓ, j] = 1.

The blocks are aligned at the end: block number k has the rows from n - (k + 1) t₂ on, and the last
block starts at row 0, so that it may overlap the one before.  So every block is a contiguous piece
of U, and nothing is copied or padded.  The structure of the block with the first row s lies at
base + s Sz, where Sz is an upper bound on the number of cells of a structure.  The blocks are
handled in the order of decreasing first rows, so that a new structure lies below all earlier ones.
A table tells for every row the first row of its block.

* gather(n, t₁, t₂, aN, aI, aJ, aY) writes N_{I,J} (`gather_meets`).
* blocks(n, t₁, t₂, aY, aS, base, Sz) builds the structures and the table (`blocks_meets`).
* scan(off, j, t₂, t₁, aX, aY, fr, aV, n): off is a row, counted from the first row of its block;
  aX, aY, fr are the addresses of the block, of Y and of the structure of the block.  It returns 1
  if for some ℓ < t₂ both V[ℓ, j] = 1 and the entry (off, ℓ) of the product of the block with Y is
  not 0, and 0 if not (`scan_meets`).


 ## Writing a submatrix 

### `Size`

 The locals of gather(n, t₁, t₂, aN, aI, aJ, aY).  The arguments: the size n of N, the numbers t₁
of rows and t₂ of columns of the submatrix, the addresses of N, I, J and of the submatrix Y.  Then
the row a and the column b, and the addresses of row I_a of N and of row a of Y. 

### `gatherBody`

 gather(n, t₁, t₂, aN, aI, aJ, aY): for a < t₁, b < t₂: Y[a, b] := N[I_a, J_b]. 

### `tGather`

 The time of gather: t₁ rows of t₂ entries. 

### `gather_meets`

 **gather** writes the submatrix N_{I,J} and changes nothing else. 

 ## The blocks 

### `Size`

 The locals of blocks(n, t₁, t₂, aY, aS, base, Sz).  The arguments: the sizes n, t₁, t₂, the
addresses of Y, of the table and of the structures, and the distance of the structures.  Then the
first row of the block before (n at the beginning), the first row s of the block, a counter, a
result that is not used, and the number and the address of the cells of the table that belong to the
block. 

### `blocksBuild`

 The block with the first row s: build its structure, and write s into the cells s, …, prev - 1
of the table. 

### `blocksBody`

 blocks(n, t₁, t₂, aY, aS, base, Sz): the blocks in the order of decreasing first rows. 

### `BlockReady`

 The structure of the block with the first row s is ready. 

### `BlockReady.keep`

 The structure of a block stays ready if neither U, nor Y, nor the cells from its address on
change. 

### `Served`

 The rows from lo on are served: the table has the first row s ≥ lo of a block that contains the
row, and the structure of this block is ready. 

### `tBlocks`

 The time of blocks: ⌈n / t₂⌉ rounds, each with one preprocessing and at most t₂ entries of the
table. 

### `BlocksPre`

 What blocks asks of its arguments and of the memory: 1 ≤ t₁ and 1 ≤ t₂ ≤ n; U lies at 3 and Y at
aY, with entries of absolute value at most 1; then follow the table and the structures, which are Sz
cells apart and have at most Sz cells each; the limits suffice for all of them. 

### `BlocksPre.input`

 What the routines of the kit are given for the block with the first row s. 

### `Served.step`

 **What a round does to the memory.**  The rows from prev on are served.  The structure of the
block with the first row s is built below the earlier ones, and s is written into the cells
s, …, prev - 1 of the table.  Then the rows from s on are served. 

### `BlocksInv`

 The state before round c of blocks: the first row of the block before is n - c t₂, the rows from
there on are served, and no cell below the table has changed. 

### `blocksBuild_spec`

 **One block.**  The first row n - (c + 1) t₂ of the block has been computed.  The structure of
the block is built, and its first row is written into the table for the rows that it serves. 

### `blocks_meets`

 **blocks** builds the structures of the blocks and the table of their first rows.  It changes no
cell below the table. 

 ## The queries of Phase 4 

### `HitBelow`

 Some ℓ below l is a hit. 

### `not_hitBelow_zero`

 There is no hit below 0. 

### `hitBelow_succ`

 A hit below l + 1 is a hit below l or a hit at l. 

### `hitBelow_all`

 A hit below t is any hit. 

### `RowOff`

 The locals of scan(off, j, t₂, t₁, aX, aY, fr, aV, n).  The arguments: the row off of the block
(this local also takes the result), the column j, the sizes t₂ and t₁, the addresses of the block,
of Y, of the structure and of V, and the size n.  Then ℓ, the result so far, and the answer to a
query. 

### `scanStep`

 One ℓ: if V[ℓ, j] = 1 and the entry (off, ℓ) of the product is not 0, then the result is 1. 

### `scanBody`

 scan(off, j, t₂, t₁, aX, aY, fr, aV, n): the steps for ℓ < t₂. 

### `tScan`

 The time of scan: t₂ rounds with at most one query each. 

### `scanLoc`

 The locals of scan in the round for ℓ: the arguments, ℓ, the result b so far, and the answer q
to the last query. 

### `scanStep_spec`

 **One ℓ.**  The result so far tells whether there is a hit below ℓ; afterwards it tells whether
there is one below ℓ + 1.  Only cells of the structure change, and it stays ready. 

### `scan_meets`

 **scan** returns 1 if some ℓ has V[ℓ, j] = 1 and (XY)[off, ℓ] ≠ 0, and 0 if not.  It changes
only cells of the structure. 
