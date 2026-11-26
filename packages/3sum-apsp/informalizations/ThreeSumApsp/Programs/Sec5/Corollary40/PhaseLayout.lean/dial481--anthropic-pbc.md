---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/PhaseLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/PhaseLayout.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/PhaseLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The three hinted problems: where the inputs of the phases lie

The statements about v-hinted Mv, Mv-hinted Mv and uMv-hinted uMv (Section 5.4) fix the layout: the
inputs of the phases lie one after the other from cell 0 on (`InputsAt`).  This file names the
addresses.  For each problem, and for each phase in which its program works, a structure says what
the memory holds in that phase, and a lemma reads the structure off the list of the inputs so far,
together with the address of the first cell after them.

Matrices are written row by row (`MatAt`), Booleans as 0 and 1 (`toInt`), and a vector of indices
cell by cell (`VecAt`).


 ## Matrices in the memory 

### `length_rowMajor_mat`

 The number of cells of a matrix. 

### `matAt_rowsFrom`

 The rows from the row s on lie where they lie in the matrix. 

 ## v-hinted Mv

n in cell 0, t in cell 1, M from cell 2 on, then V, the index i, and the n cells of the output. 

### `vV`

 The address of V. 

### `vI`

 The cell of the index i. 

### `vOut`

 The first cell of the output. 

### `VMem2`

 The inputs of Phases 1 and 2. 

### `VMem3`

 The inputs of Phases 1 to 3. 

### `vMem2_of_inputs`

 What the memory holds when the input of Phase 2 has been written. 

### `vMem3_of_inputs`

 What the memory holds when the input of Phase 3 has been written. 

 ## Mv-hinted Mv

n in cell 0, t in cell 1, N from cell 2 on, then V, the t indices I, the index j, and the n cells of
the output. 

### `mvV`

 The address of V. 

### `mvI`

 The address of I. 

### `mvJ`

 The cell of the index j. 

### `mvOut`

 The first cell of the output. 

### `MvMem2`

 The inputs of Phases 1 and 2. 

### `MvMem3`

 The inputs of Phases 1 to 3. 

### `mvMem2_of_inputs`

 What the memory holds when the input of Phase 2 has been written. 

### `mvMem3_of_inputs`

 What the memory holds when the input of Phase 3 has been written. 

 ## uMv-hinted uMv

n, t₁, t₂ in cells 0, 1, 2; U from cell 3 on; then N, V, I, J, the two indices i and j, the output
cell, and the free cells. 

### `uMvN`

 The address of N. 

### `uMvV`

 The address of V. 

### `uMvI`

 The address of I. 

### `uMvJ`

 The address of J. 

### `uMvQ`

 The address of the indices i and j. 

### `uMvOut`

 The output cell. 

### `uMvFree`

 The first free cell. 

### `UMvMem3`

 The inputs of Phases 1 to 3. 

### `UMvMem4`

 The inputs of Phases 1 to 4. 

### `uMvMem3_of_inputs`

 What the memory holds when the input of Phase 3 has been written. 

### `uMvMem4_of_inputs`

 What the memory holds when the input of Phase 4 has been written. 
