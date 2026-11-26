---
{
  "module": "proof/rates/CountedRecursion/ParentNumbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ParentNumbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ParentNumbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers in a parent

* `pG_mk`, …: the g, λ, B, lists, direction and pattern number of `mkParent D K g λ B tr y x`;
* `digG_ofLists`, `lenG_ofLists`, `capG_ofLists`: the plain functions of
  proof/rates/ClauseBound/Alg/Data.lean give the same numbers for the lists as for the pieces (from
  the statement `ListsAgree`, a hypothesis here, and the congruence lemmas of GridLemmas.lean);
* `netData_eq`: the input of Definition 2(iii) that the procedure writes from the parent is the
  input that belongs to the network of the pattern. 

 ## The parts 

### `pG_mk`

 The g of the parent for these numbers. 

### `pLam_mk`

 Its λ. 

### `pB_mk`

 Its B. 

### `pLists_mk`

 Its lists. 

### `pTr_mk`

 Its direction. 

### `pY_mk`

 The number of its pattern. 

 ## The lists give the numbers of the pieces 

### `lists_agree`

 What the congruence lemmas ask. 

### `digG_ofLists`

 ι at a rectangle, from the lists and from the pieces. 

### `lenG_ofLists`

 The length of the chunk of a rectangle, from the lists and from the pieces. 

### `capG_ofLists`

 c_{a,a'}, from the lists and from the pieces. 

 ## The input that the procedure writes 

### `netData_eq`

 **The input that the procedure writes is the input that belongs to the network.** 
