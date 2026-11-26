---
{
  "module": "proof/machines/ToTuring/TM/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/TM/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The universal data of the machines: binary trees whose leaves are bits or empty, written with
two brackets. A word read
from the other end, its brackets exchanged, is the code of the mirrored tree; so an item that was
moved symbol by symbol to
another stack is again an item. 

### `Sym`

 Bits and two brackets. 

### `V`

 Binary trees whose leaves are bits or empty. 

### `code`

 The code of a tree: ⟨⟩ for nil, the bit for a bit, ⟨ code x, code y ⟩ for cons x y. 

### `Sym.flip`

 The other bracket. 

### `mirror`

 A word read from the other end, its brackets exchanged. 

### `V.mir`

 The mirrored tree. 

### `code_mir`

 The code of the mirrored tree is the mirrored code. 
