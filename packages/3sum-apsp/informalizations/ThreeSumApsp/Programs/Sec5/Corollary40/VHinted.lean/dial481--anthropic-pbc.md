---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary40/VHinted.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/VHinted.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary40/VHinted.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40: v-hinted Mv as a light program that runs in phases

Proof of Corollary 40, paragraph "Conjecture 5.2 of [vdBNS19]": "we preprocess X := M and Y := V
[...]  In Phase 3, the n entries of column i of MV are n queries".

The inputs of the phases lie one after the other: n in cell 0, t in cell 1, M from cell 2, V from
cell 2 + nt, the index i in cell 2 + 2nt, and the n cells of the output from 3 + 2nt on (`VMem2`,
`VMem3`).  The data structure, an arbitrary kit, is built from the cell 3 + 2nt + 3n on.  Phase 1
returns at once.  Phase 2 preprocesses M and V where they lie (`vPhase2_meets`).  Phase 3 asks the n
queries (`vPhase3_meets`).  `v_lightPhases` puts the phases together.


### `vFr`

 The first cell of the data structure. 

### `vAddresses`

 The addresses, written out. 

### `Size`

 The locals of Phases 2 and 3: n, t, the number nt of cells of a matrix, the address of V, the
first cell of the data structure, and the result of the call, which is not used. 

### `vPhase1Body`

 Phase 1 does nothing. 

### `vAddr`

 The start of Phases 2 and 3: n and t are read from cells 0 and 1, and the addresses are computed
from them. 

### `vPhase2Body`

 Phase 2: pre(n, t, 2, aV, fr). 

### `vPhase3Body`

 Phase 3: col(n, t, 2, aV, fr, i, out), where i is read from the cell after V. 

### `vAddr_spec`

 **Sizes and addresses.**  `vAddr` leaves n, t, nt, the address of V and the first cell of the
data structure in the locals, and changes no cell. 

### `vPhase2_meets`

 **Phase 2** preprocesses M and V where they lie: the data structure is ready, and only its cells
have changed. 

### `vPhase3_meets`

 **Phase 3** asks the n queries for column i: output cell r tells whether the entry (r, i) of the
product of M and V over the integers is positive. 

### `v_lightPhases`

 **v-hinted Mv runs in phases**, with explicit numbers of steps. 
