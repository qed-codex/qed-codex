---
{
  "module": "proof/machines/ToTuring/Enc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Enc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Enc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 How the data of the algorithm are written as trees, hence as words on a stack. There is no
decoding: the machines are only
ever asked to turn the word of a value into the word of another value. 

### `Enc`

 Data as trees. 

### `Enc.toV`

 the tree of a value 

### `instance : Enc ℕ`

 A number is the list of its binary digits, lowest first, no leading zero; 0 is the empty list. 

### `instance : Enc ℤ`

 An integer is «negative?» and its absolute value. 

### `wd`

 The word that stands for x on a stack. 

### `len`

 The length of the word of x. 

### `Carried`

 The word of a value is at most linear in its size (`HasSize`, the measure in which the states of
the algorithm are bounded):
len x + 2 ≤ 7·size x. 
