---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/MvHinted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/MvHinted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/MvHinted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40: Mv-hinted Mv as a light program that runs in phases

Proof of Corollary 40, paragraph "Conjecture 5.7 of [vdBNS19]": "The proof is the same, with
X := N_{[n],I} and Y := V, which are both known in Phase 2".

The inputs of the phases lie one after the other: n in cell 0, t in cell 1, N from cell 2, V from
cell 2 + n², the t column indices I from 2 + n² + tn, the index j in the cell after them, then the n
cells of the output (`MvMem2`, `MvMem3`).  After the output come the nt cells of X.  The data
structure, an arbitrary kit, is built from the cell 3 + 2nt + 3n² on.  Phase 1 returns at once.
Phase 2 writes X, whose column k is column I_k of N (`mvGather_spec`), and preprocesses X and V
(`mvPhase2_meets`).  Phase 3 asks the n queries (`mvPhase3_meets`).  `mv_lightPhases` puts the
phases together.


### `Size`

 The locals of Phases 2 and 3.  Sizes: n, t, n², nt.  Addresses: of V, of I, of j, of the output,
of X, and the first cell of the data structure.  For the loops that write X: the row r (this local
also takes the results of the calls, which are not used), the addresses of row r of N and of X, and
the column. 

 ## Addresses 

### `mvX`

 The address of X. 

### `mvFr`

 The first cell of the data structure. 

### `mvAddresses`

 The addresses, written out. 

### `mvAddr`

 The start of Phases 2 and 3: n and t are read from cells 0 and 1, and the addresses are computed
from them. 

### `mvLoc`

 The local variables after the addresses have been computed. 

### `mvAddr_spec`

 **Sizes and addresses.**  `mvAddr` leaves the list `mvLoc n t` in the locals and changes no
cell. 

 ## The matrix of the selected columns 

### `mvGather`

 for r < n, c < t: X[r, c] := N[r, I_c].  N lies at 2. 

### `tMvGather`

 The time of `mvGather`: n rows of t entries. 

### `mvGather_spec`

 **The matrix of the selected columns** is written, and only its cells change. 

 ## The three phases 

### `mvPhase1Body`

 Phase 1 does nothing. 

### `mvPhase2Body`

 Phase 2: X is written; then pre(n, t, aX, aV, fr). 

### `mvPhase3Body`

 Phase 3: col(n, t, aX, aV, fr, j, out), where j is read from its cell. 

### `mvPhase2_meets`

 **Phase 2** writes X and preprocesses X and V: the data structure is ready, and no cell below X
has changed. 

### `mvPhase3_meets`

 **Phase 3** asks the n queries for column j: output cell r tells whether the entry (r, j) of the
product of X and V over the integers is positive. 

### `mv_lightPhases`

 **Mv-hinted Mv runs in phases**, with explicit numbers of steps. 
