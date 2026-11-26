---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Union.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Union.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Pruned/Union.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The merge of two lists (Section 2.4.4: "a union of slices is a merge")

union(pa, na, pb, nb, pc) writes the merge of the list of na numbers at pa and the list of nb
numbers at pb to pc, a number that heads both lists being taken once, and returns its length.  The
program follows Spec.mergeUnion step by step.

union_entry shows that a call does this in at most 70 (na + nb + 1) steps and changes no cell
outside the output.  Both loops keep UnionInv.  What writing one number does to the data is
union_emit.  The three bodies are unionBoth_ends, unionLeft_ends and unionRight_ends, and
union_entry treats the two loops.


 ## The program 

### `ListA`

 The first list, A in the comments of the proofs. 

### `LenA`

 The length na of the first list. 

### `ListB`

 The second list, B in the comments of the proofs. 

### `LenB`

 The length nb of the second list. 

### `Dest`

 Where the merge is written, C in the comments of the proofs. 

### `TakenA`

 The number i of entries taken from the first list. 

### `TakenB`

 The number j of entries taken from the second list. 

### `Written`

 The number len of entries written. 

### `HeadA`

 The head a of what is left of the first list. 

### `HeadB`

 The head b of what is left of the second list. 

### `unionBoth`

 Both lists have a head: the smaller one is written and its list advances; if they are equal, the
number is written once and both lists advance. 

### `unionLeft`

 The head of the first list is written. 

### `unionRight`

 The head of the second list is written. 

### `unionBody`

 union(pa, na, pb, nb, pc); it returns len. 

 ## The invariant 

### `UnionPre`

 What union assumes: the two lists lie below the output, and the output fits in the memory. 

### `UnionInv`

 What both loops keep: i and j numbers of the two lists have been taken; the list done has been
written to pc; together with the merge of what is left it is the merge of the two lists; no cell
outside the output has changed. 

### `unionState`

 The state of the two loops. 

### `UnionLoop`

 The invariant of both loops.  In the second loop the first list is used up: i₀ = la.length. 

### `unionRest`

 What is still to be taken. 

### `UnionNext`

 What a round that starts in σ achieves: the invariant holds again, and less is left. 

### `mergeUnion_nil_right`

 The merge with the empty list. 

### `UnionPre.readA`

 The first list lies outside the output, so it can be read at any time. 

### `UnionPre.readB`

 The second list lies outside the output, so it can be read at any time. 

### `union_emit`

 **One number is written.**  If x heads the merge of what is left, and what is left afterwards
starts at i' and j', then after writing x the invariant holds again, and less is left. 

 ## The three bodies 

### `unionBoth_ends`

 Both lists have a head. 

### `unionLeft_ends`

 The second list is used up. 

### `unionRight_ends`

 The first list is used up. 

 ## The procedure 

### `union_entry`

 **union**: a call writes the merge of the two lists to pc, returns its length and changes no
cell outside the output, in at most 70 (na + nb + 1) steps. 
