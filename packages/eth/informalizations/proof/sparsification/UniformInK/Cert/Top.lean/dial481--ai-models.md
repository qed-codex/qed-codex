---
{
  "module": "proof/sparsification/UniformInK/Cert/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parameters of the bound in n, given in unary or polynomial-time jointly in the width

Here the width k is read from the input, in unary. The numbers β, 2^β, 2^β cut off at n + 1, the
width cut off at ⌊log₂(n+1)⌋ and 2 to this width are shown to be given
in unary or to be polynomial-time, jointly in k, n and s; and 2 to the width cut off is shown to be
at most n + 1. 

 ### The parameters, jointly in the width 

### `betaU_unary`

 β is given in unary if k and s are. 

### `powBetaU_polyT`

 2^β is polynomial-time if k and s are given in unary. 

### `blockU_unary`

 2^β cut off at n + 1 is given in unary if k, n and s are. 

### `kcU_unary`

 The width cut off at ⌊log₂(n+1)⌋ is given in unary if k is and n is polynomial-time. 

### `two_pow_kcU_le`

 2 to the width cut off is at most n + 1. 

### `powKcU_unary`

 2 to the width cut off is given in unary if k and n are. 
