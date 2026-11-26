---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/UMvHinted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/UMvHinted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/UMvHinted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# uMv-hinted uMv over a kit: the four phases

Proof of Corollary 40.  A kit is a data structure for the entries of a thin matrix
product that can be placed anywhere in the memory.  Phases 1 and 2 return at once.  Phase 3 computes
the addresses (`uMvAddr_spec`), writes Y := N_{I,J}, and builds the structures of the blocks and the
table of first rows (`uMvPhase3_meets`).  Phase 4 reads i and j, looks up the first row s of the
block of row i, asks the structure of that block, and writes the result (`uMvPhase4_meets`).
`uMv_lightPhases` puts the phases together.


 ## The scratch space 

### `uMvY`

 The address of Y = N_{I,J}, t₁ t₂ cells. 

### `uMvS`

 The table of the first rows of the blocks, n cells. 

### `uMvBase`

 The address of the structure of a block with the first row 0. 

### `uMvSz`

 The distance of the structures of two blocks whose first rows differ by 1; A is a numeral in the
program text. 

### `uMvFr`

 The address of the structure of the block with the first row s. 

### `uMvTop`

 An address above all cells that are used. 

### `UMvLim`

 The limits that the four phases need. 

### `uMvAddresses`

 How the addresses follow one another. 

 ## The procedures 

### `Size`

 The locals of Phases 3 and 4.  Locals 0 and 1 are the arguments of the main procedure, which are
not used.  Then the sizes n, t₁, t₂; the addresses of N, V, I, J, of Y, of the table and of the
structures; the distance of the structures.  In Phase 3 two results that are not used follow.  In
Phase 4: i, j, the first row of the block of row i, and the result. 

### `uMvAddr`

 The start of Phases 3 and 4: n, t₁ and t₂ are read from cells 0, 1 and 2, and the addresses are
computed from them. 

### `uMvPhase3Body`

 Phase 3: gather(n, t₁, t₂, aN, aI, aJ, aY), then blocks(n, t₁, t₂, aY, aS, base, Sz). 

### `uMvPhase4Body`

 Phase 4: i and j are read from their cells and the first row s of the block of row i from the
table; the result of scan(i - s, j, t₂, t₁, 3 + s t₁, aY, base + s Sz, aV, n) goes to the output
cell. 

### `UMvProcs`

 The procedures of the four phases and their three routines are in the program. 

### `uMvLoc`

 The local variables after the addresses have been computed. 

### `uMvAddr_spec`

 **Sizes and addresses.**  `uMvAddr` leaves the list `uMvLoc A n t₁ t₂` in the locals and changes
no cell. 

### `UMvPhase3Post`

 What Phase 3 leaves: for every row the table has the first row of its block, and the structure
of this block is ready. 

### `uMvPhase3_meets`

 **Phase 3** writes Y and builds the structures of the blocks and the table of their first rows.
It changes no cell below Y. 

### `uMvPhase4_meets`

 **Phase 4** writes the entry (i, j) of U N_{I,J} V, as 0 or 1, into the output cell. 

### `UMvPhase3Post.keep`

 What Phase 3 leaves stays if neither U nor a cell from Y on changes. 

### `uMv_lightPhases`

 **The four phases of uMv-hinted uMv over a kit.** 
