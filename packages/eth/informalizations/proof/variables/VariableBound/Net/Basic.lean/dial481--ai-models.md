---
{
  "module": "proof/variables/VariableBound/Net/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3 of Appendix D: first facts on the list of objects

What the files of proof/variables/VariableBound/Net share and what has no counterpart in the network
with one kind of marks of `PaddedDescent.F`: which triples (κ, e, j) are objects, that no object
occurs twice, that every object has a clause of ψ, how many objects
there are of each kind. 

### `mem_objs`

 The objects are the triples (0, e, 0) with e < m and the triples (1, e, j) with j < r and e ∈
Λ_j. 

### `obAt_eq`

 At a place o below the number of objects, `obAt` is the entry of the list. 

### `obAt_mem`

 At a place o below the number of objects, `obAt` is an object. 

### `exists_obAt`

 Every object stands at some place of the list. 

### `kind_lt`

 There are two kinds. 

### `kind_cases`

 An object (at a place o below the number of objects) is of kind 0 or of kind 1. 

### `inc_mem`

 An incidence (E, j) has j < r and E ∈ Λ_j. 

### `getD_mem`

 Check number j < r is a member of the list of checks. 

### `cl_lt`

 For well-formed data (WfD), the clause of an object is a clause of ψ: its number is below m. 

### `clOf_mem`

 For well-formed data (WfD), the clause of an object is a member of ψ. 

### `clOf_wf`

 For well-formed data (WfD), the clause of an object has 1 to k literals on variables below n. 

### `nodup_objs`

 For well-formed data (WfD), no object occurs twice in the list. 

### `obAt_inj`

 For well-formed data (WfD), two places below the number of objects that hold the same triple are
equal. 

### `length_objs`

 I + m: the number of objects. 

### `obAt_of_lt`

 The first m objects are the clauses. 

### `kind_zero_iff`

 For well-formed data (WfD), an object is a clause iff it is among the first m. 

 ### Touches 

### `tchB_iff`

 An object touches the nodes that hold the variables of its clause; an incidence (E, j) also
touches h(j). 

### `tchB_home`

 An incidence (E, j) touches h(j). 

### `div_qv_lt`

 For g > 0, the node that holds the variable x < n is below g. 

### `tch_lt`

 For g > 0 and well-formed data (WfD), a node that an object touches is below g. 

### `exists_tch`

 For g > 0 and well-formed data (WfD), every object touches a node below g. 

### `card_touched_le`

 The object o touches at most (number of literals of its clause) + (kind of o) nodes below g.
With at most k literals (WfD) this gives the bound «at most k − 1 + κ tests» of Appendix D, Step 3
of the paper, which is not stated here. 
