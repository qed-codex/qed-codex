---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Code.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Code.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Code.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Renaming the variables that occur: the program on the code of a formula

`renc_enc`: for k ≥ 1 and a formula φ with at most k literals in every clause, the front end `renc`
maps the code of (k, φ) to the code of (k, `ren φ`). So everything that is proved about codes of
formulas in which all variables occur applies to what the front end hands on. 

### `slotN_map`

 The number of a slot, with natural numbers as variables, is that of `Sat3.slot`. 

### `encN_toN`

 `encN` on k and n in unary and a formula over x₀ … x_(n−1), with natural numbers as variables,
is `SatM.enc`. 

### `renc_enc`

 The front end maps the code of (k, φ) to the code of (k, φ renamed), for k ≥ 1 and φ with at
most k literals in every clause. 
