---
{
  "module": "proof/machines/ToTuring/Lib/List1.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List1.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List1.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for lists: reverse, append, foldr, map, filter, all, any, flatMap, filterMap,
find?. Each lemma tagged
`fun_prop` says that one function of `List` preserves `PolyT`. Everything comes from the fold. 

### `len_bound`

 The length of the result of a polynomial-time function has a monotone polynomial bound. 

### `len_bound_mem`

 A function of the context and of a member of a polynomial-time list has values of polynomial
length. 

### `comp₂`

 A two-argument function after polynomial-time arguments. 

### `reverseAppend`

 Pushing the members of one list, first to last, on another. 

### `foldr`

 The fold from the right when the fold of every suffix of the list has length at most t(len x). 

### `foldr_add`

 The fold from the right when every step adds at most b(len x) to the length. 
