---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Offline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Offline.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Offline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 30, the offline form (9): preprocess, then one query for each wanted position

Theorem 30: "In particular, for every set W of positions of an N × N matrix, the entries (XY)[I, J],
(I, J) ∈ W, can be computed deterministically in time
O(L |W| ∑_{d=0}^{t} α_d + L m ρ^t/(1 - ρ) N² + N · 10^L/(√K N₀))."

wantedCore is relocatable: it receives the addresses of the matrices, of the two lists of indices,
of the output and of the free block. It meets its specification `WantedCoreSpec` in every program
that meets those of preCore and queryAt (`wantedCore_spec`): one call of preCore, then a loop whose
round asks one query and stores the answer (`wantedAsk_ends`), with the invariant `Answered`.


 ## One query for each wanted position: the invariant 

### `Answered`

 The invariant of a loop that asks one query after the other and stores the answers ans from the
address out on, before query i.  The memory is Ready for a query, the first i answers are in place,
and the cells in Kept outside these i cells are as in the memory μ at the start. 

### `Answered.step`

 One round: a query that leaves the cells in Quiet alone, among them the output and the cells in
Kept, and the store of its answer behind the answers that are there. 

### `Answered.read`

 A cell of a list that stood in the memory at the start, away from the answers and in Kept, still
holds its entry. 

### `Answered.all`

 After the last round all answers are in place. 

 ## The routine 

### `Levels`

 The locals of wantedCore. The first twelve are its arguments: L, m, t, N, D, the addresses of X,
of Y, of the rows and of the columns of the wanted positions, the number of positions, and the
addresses of the output and of the free block. Then come the number of the current position and the
result of a call. 

### `wantedAsk`

 One round of wantedCore: ask the query for the current position and store its answer. 

### `wantedCoreBody`

 wantedCore(L, m, t, N, D, aX, aY, aI, aJ, w, out, b0): preprocess, then ask one query for each
wanted position and store its answer. 

### `tWantedCore`

 The time of wantedCore. 

### `WantedInput`

 Where the input of wantedCore stands: the two matrices, the rows and the columns of the wanted
positions and the output all lie below the free block, and the output does not meet the two lists.


### `WantedCoreSpec`

 wantedCore writes the wanted entries of XY to out.  It changes only the output and the block
from b0 on, about whose content nothing is assumed. 

### `wantedAsk_ends`

 **One round**: the answer for position i joins the answers that are there. 

### `wantedCore_spec`

 **wantedCore** meets its specification. 
