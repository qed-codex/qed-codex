---
{
  "module": "proof/sparsification/UniformInK/Top/End.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/End.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/End.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas on the time bounds of the statement for all widths k

Four lemmas on the bounds of the statement for all widths k: the bound in n with k² in the exponent
grows with the constant (`boundNK_mono`); the bound with the minimum of the two exponents is the
bound in n
when that exponent is the smaller one (`boundBothK_of_le`) and the bound in m otherwise
(`boundBothK_of_ge`); and if every variable occurs and n ≥ 1, there is a clause (`one_le_length`). 

### `boundNK_mono`

 The bound in n with k² in the exponent grows with the constant. 

### `boundBothK_of_le`

 If the exponent in n is the smaller one, the bound with the minimum is the bound in n. 

### `boundBothK_of_ge`

 If the exponent in m is the smaller one, the bound with the minimum is the bound in m. 

### `one_le_length`

 If every variable occurs and there is a variable, there is a clause. 
