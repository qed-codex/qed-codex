---
{
  "module": "proof/rates/ClauseBound/Both/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Both/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Monotonicity of the bound in m and of the number of steps of the padding machine

Two monotonicity facts: the bound in the number m of clauses grows with its constant (`bound_mono`),
and the number of steps q·(L + 2^E + 1)^q of the padding machine grows with the length L of the
input and with the exponent E (`steps_mono`). 

### `bound_mono`

 The bound in m grows with the constant. 

### `steps_mono`

 The number of steps of the padding machine grows with the length of the input and with the
exponent. 
