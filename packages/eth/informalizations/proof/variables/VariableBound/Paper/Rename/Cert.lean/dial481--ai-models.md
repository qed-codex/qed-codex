---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Renaming the variables that occur is polynomial-time

`renc_polyT : PolyT renc`. Every step of the program is an operation on lists for which
proof/machines/ToTuring/Lib has a closure lemma. 

### `occL_polyT`

 The list of the variables that occur is polynomial-time. 

### `renL_polyT`

 Replacing every variable by its position in a list is polynomial-time. 

### `renF_polyT`

 The renamed formula is polynomial-time. 

### `slotN_polyT`

 The number of a slot is polynomial-time. 

### `encN_polyT`

 Writing (k, n, ψ) as a bit string is polynomial-time, with k and n in unary. 

### `renc_polyT`

 `renc` is polynomial-time: it decodes the input, replaces every variable by its position in the
list of the variables that occur, and writes the result as a bit string. 
