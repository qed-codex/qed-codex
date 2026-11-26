---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The function that writes the outputs is polynomial-time in (input, pad)

This file proves `polyT_BL : PolyT BL` and `polyT_eL : PolyT eL` (definitions in
proof/sparsification/SparsificationLemma/Mach/Walk.lean). These are the two hypotheses of the
padding machine `CountKSatRate.StPaddedW`.
The proof for one round of the walk follows `CountKSatRate.Cert.polyT_roundS`; the whole walk needs
the width k and 2^k given in unary.
In `BL` the width is cut off at ⌊log₂(length of the pad)⌋, so 2^k is at most the length of the pad. 

### `round_eq`

 `round` with its case distinctions written by eliminators. 

### `polyT_round`

 One round of the collecting walk is polynomial-time, for a step function that may depend on the
context. 

### `polyT_walkL`

 The collecting walk is polynomial-time jointly in k, the pad, τ and the root, if k and 2^k are
given in unary. 

### `polyT_codeNatP`

 The code of a number, cut off at the length of the pad, is polynomial-time. 

### `polyT_codeClP`

 The code of a clause, cut off, is polynomial-time. 

### `polyT_codeFmlP`

 The code of a formula, cut off, is polynomial-time. 

### `polyT_codeP`

 The code of a list of formulas, cut off, is polynomial-time. 

### `unary_sL`

 The precision written in the input is given in unary. 

### `unary_kL`

 The width written in the input is given in unary. 

### `polyT_dL`

 The number of variables and the formula written in the input are read in polynomial time. 

### `polyT_eL`

 The exponent of the length of the pad is polynomial-time. 

### `polyT_BL`

 The function that writes the outputs is polynomial-time in (input, pad). 
