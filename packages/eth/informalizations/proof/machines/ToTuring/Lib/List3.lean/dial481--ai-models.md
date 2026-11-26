---
{
  "module": "proof/machines/ToTuring/Lib/List3.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List3.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List3.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for lists: membership, duplicates, longest prefix passing a test, products of
lists. 

### `elem`

 Membership in the form `elem`. The test `==` may be any lawful one: on pairs, options and lists
it is not the one made
from `DecidableEq`. 

### `contains`

 Membership in the form `contains`. 

### `decide_mem`

 Membership in the form `decide (b ∈ l)`. `BEq` and `LawfulBEq` are needed because the instance
`Decidable (b ∈ l)` of Lean's
core library is built from them. 

### `dedup`

 Removal of duplicates: a fold from the right that adds an element unless the result already has
it. 

### `takeWhile`

 The longest prefix whose elements pass a test; the test may depend on the input `x`. 

### `dropWhile`

 The list without its longest prefix whose elements pass a test. 

### `product`

 The list of all pairs of an element of the first list and an element of the second. 

### `sprod`

 The product of two lists in the notation ×ˢ. 
