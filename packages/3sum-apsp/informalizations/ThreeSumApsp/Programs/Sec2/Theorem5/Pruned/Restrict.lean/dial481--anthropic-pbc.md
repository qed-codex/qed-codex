---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Restrict.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Restrict.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Restrict.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Restricting an array on a set of codes to a subset (step (4) of Pruned, Section 2.4.2)

pick walks once through an increasing list of codes (big), which has a value for each of its codes,
and through an increasing list of some of these codes (small).  It writes the values of the codes of
the second list, or adds them to what is there.

* The lists.  `PickInv` says where the walk stands.  If the two heads agree, the value is taken and
  both lists advance (`PickInv.hit`); if not, the head of the large list is skipped
  (`PickInv.miss`).
* The memory.  `PickMem` says which cells of the destination are finished; `PickMem.write` finishes
  one more.
* The program.  `pickTake_ends` treats the round in which a value is taken, `pickBody_ends` the
  loop, for both modes.  `pickSet_entry` and `pickAdd_entry` are the results for the callers: a call
  of procedure `pPick` does what `PickSetSpec` (writing) or `PickAddSpec` (adding) says, in at most
  `cPick` steps for each entry of the two lists.


 ## The program 

### `PSUB`

 The small list. 

### `NSUB`

 The length of the small list. 

### `PU`

 The large list. 

### `PVAL`

 The values of the codes of the large list. 

### `PDST`

 The destination. 

### `ADD`

 The mode: 0 for writing, otherwise adding. 

### `CI`

 The position i in the small list. 

### `CJ`

 The position j in the large list. 

### `pickTake`

 The two heads agree: the value is written or added, and both lists advance. 

### `pickBody`

 pick(pSub, nSub, pU, nU, pVal, pDst, add).  The length nU of the large list, local 3, is not
read: the large list cannot end before the small one. 

### `cPick`

 The constant of the running time. 

 ## The lists 

### `PickInv`

 The state of the walk: position i in the small list, position j in the large one. 

### `PickInv.zero`

 Before the walk. 

### `PickInv.lt`

 As long as the small list is not exhausted, neither is the large one. 

### `PickInv.hit`

 The two heads agree: the value is taken. 

### `PickInv.miss`

 The two heads differ: the head of the large list is skipped. 

### `length_restrictList_le`

 pick gives at most one value for each number of the small list. 

 ## The memory 

### `pickTarget`

 What cell i of the destination holds in the end: entry i of the list res, added to what the cell
held if add is not 0. 

### `PickMem`

 The first i of the n cells of the destination are finished, and nothing else has changed. 

### `PickMem.write`

 One more cell is finished. 

### `PickPre.readSub`

 The small list lies above the destination, so it can be read at any time. 

### `PickPre.readBig`

 The large list lies above the destination, so it can be read at any time. 

### `PickPre.readVal`

 The values lie above the destination, so they can be read at any time. 

 ## The walk 

### `pickState`

 The state of the loop. 

### `PickLoop`

 The invariant of the loop. 

### `pickRest`

 What is left of the large list. 

### `PickNext`

 What a round that starts in σ achieves: the invariant holds again, and less is left. 

### `PickFits`

 The sums that are formed in the mode that adds fit in a word. 

### `pickTake_ends`

 The round in which the two heads agree. 

### `pickBody_ends`

 **The walk**, for both modes. 

 ## The two results for the callers 

### `pickSet_entry`

 **pick, writing**: a call with add = 0 writes the values of the codes of the small list to pDst
and changes no other cell, in at most cPick (small.length + big.length + 1) steps. 

### `pickAdd_entry`

 **pick, adding**: a call with add = 1 adds the values of the codes of the small list to the
cells from pDst on and changes no other cell, in at most cPick (small.length + big.length + 1)
steps. 
