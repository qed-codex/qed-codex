---
{
  "module": "proof/machines/ToTuring/Lib/List2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Lib/List2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial time for lists indexed by numbers: drop, take and lookup at a binary position; range
with a unary
length; words of binary digits and chunks. 

### `foldl_drop`

 The loop behind drop: a counter that goes down and a list that loses its head as long as the
counter is positive. 

### `foldl_range`

 The loop behind range: append the length. 

### `range`

 The length must be given in unary, since the result is that long. 

### `ofWord'`

 The number whose binary digits are the word, lowest digit first. 

### `toWord'`

 The n lowest binary digits of y, lowest digit first; the length n must be given in unary. 

### `foldl_chunks`

 The loop behind chunks: what is left of the word, and the chunks cut so far, last one first. 

### `chunks'`

 Cutting a word into consecutive pieces of the given lengths. 
