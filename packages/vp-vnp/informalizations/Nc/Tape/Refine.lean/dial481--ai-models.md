---
{
  "module": "Nc/Tape/Refine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Refine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Refine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Common refinement of two factorisations of a word

Two sequences of words have the same concatenation if and only if there is a matrix of words with staircase
support whose rows concatenate to the first sequence and whose columns concatenate to the second; the matrix
is unique.


### `cat`

 Concatenation. 

### `Stair`

 Staircase support. 

### `IsRef`

 `X` is a common refinement of `A` (rows) and `B` (columns). 

### `upd`

 Replace one entry. 

### `IsRef.first`

 The first letter of a refinement. 
