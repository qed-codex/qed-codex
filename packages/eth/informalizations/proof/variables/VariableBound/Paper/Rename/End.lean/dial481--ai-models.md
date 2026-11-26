---
{
  "module": "proof/variables/VariableBound/Paper/Rename/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The last step that turns a counting machine into a deciding one

`anyBit` maps a word of bits to the word of one bit that says whether some bit of the word is 1. It
is polynomial-time, and on a number c < 2^(n+1) written in n + 1 bits it says whether c ≠ 0;
so applied to the number of satisfying assignments, written in binary, it gives the bit that says
whether the formula is satisfiable. 

 ### The last step for deciding 

### `anyBit`

 The word of one bit that says whether some bit of w is 1. 

### `anyBit_polyT`

 `anyBit` is polynomial-time. 

### `anyBit_binary`

 On a number c < 2^(n+1) written in n + 1 bits, `anyBit` says whether c ≠ 0. 
