---
{
  "module": "Nc/CaseI/Fkl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Fkl.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Fkl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The polynomials of complete networks

f_{k,ℓ} = Σ_σ ∏_a x_{a, σ|a}, the sum over all σ that give a string of ℓ bits to every pair of [k]. A table a
has variables x_{a,t}, t : [k] → strings (with t a = 0 for the variables that occur).


### `Pr`

 The pairs. 

### `Ix`

 The strings at a table. 

### `asm`

 Every end of a pair has a string; the strings at the tables. 

### `asm_congr`

 The strings at a table depend on the ends at this table only. 

### `fkl`

 **The polynomial of the complete network** of k tables with strings of ℓ bits. 

### `cf_fkl`

 The coefficients. 
