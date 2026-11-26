---
{
  "module": "proof/consequences/WidthK/Poly/Decode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Poly/Decode.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/WidthK/Poly/Decode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `decK k` of WidthK/Decode.lean, which reads a formula of width k from the input word, is
polynomial-time (`decK_polyT`). The width k is a
constant of the function, not part of its input. The file follows
proof/machines/ToTuring/Poly/Decode.lean line by line, with a parameter k for its width 3, and uses
that file's lemmas `width_polyT` and `slotDec_polyT`. 

### `clauseDec_polyT`

 Reading one clause from a block of k slots of w bits is polynomial-time. 

### `clauses_polyT`

 Reading the list of clauses from the body b of the input, one block of k·w bits per clause, is
polynomial-time. This is the
second component of `decK k`. 

### `decK_polyT`

 The decoder `decK k`, which reads the input of the algorithm, is polynomial-time. 
