---
{
  "module": "proof/consequences/CountKSat/InOut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/InOut.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSat/InOut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What the counting machine reads, and the count of what it reads

This file proves three of the interface statements of proof/consequences/CountKSat/Interfaces.lean.
For k ≥ 1, `decU k` turns the code `SatK.enc k φ` of a formula with at most k literals per clause
into n in unary and the formula with natural numbers
as variables (`stDecU`), in polynomial time (`stCertDecU`). They follow from `decK_enc` in
proof/consequences/WidthK/Decode.lean and `decK_polyT` in
proof/consequences/WidthK/Poly/Decode.lean, on the decoder `decK k`.
The formula with natural numbers as variables has the same number of satisfying assignments on n
variables (`stCntToN`). 

### `stDecU`

 For k ≥ 1, reading the code of a formula with at most k literals in every clause gives back n,
in unary, and the formula with natural numbers as variables. 

### `stCertDecU`

 The reader `decU k` is polynomial-time. 

### `stCntToN`

 The formula read with natural numbers as variables has the same number of satisfying
assignments. 
