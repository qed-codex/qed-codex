---
{
  "module": "proof/consequences/FreeCode/ReaderCert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/ReaderCert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/ReaderCert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 with the code that does not depend on k: the reader is polynomial time

No sentence of the paper stands behind this file. `readFree` goes once through the bits with the
step `stepR`. One step adds at most the bit it reads and regroups the lists of the state, so it
makes the word of the state longer by at most a constant (`len_stepR_le`); this is what the closure
of `PolyT` under folds asks (`PolyT.foldl_add`). `stReader` proves `FreeCode.StReader`. 

### `len_stepR_le`

 One step of the reader makes the word of the state longer by at most 12 symbols. 

### `stepR_polyT`

 One step of the reader is polynomial time, with the number of bits of a literal as a part of the
input. 

### `scanR_polyT`

 Going through all bits is polynomial time. 

### `readFree_polyT`

 The reader is polynomial time. 

### `stReader`

 There is a polynomial-time reader: the statement `FreeCode.StReader`. The reader is `readFree`. 
