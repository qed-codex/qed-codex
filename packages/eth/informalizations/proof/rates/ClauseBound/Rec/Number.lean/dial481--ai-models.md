---
{
  "module": "proof/rates/ClauseBound/Rec/Number.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Number.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Rec/Number.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Numbering the terms of a sum by bit strings

A function F(z,z') that is a sum of at most 2^c products f_i(z)·f'_i(z') factors through c bits:
give each term a string θ of c bits of its own, let the two functions of the
factorization be f_i and f'_i at the string of term i, and 0 at the strings that number no term. A
bound on the values of the f_i and f'_i is kept. 

### `factorsThrough_of_sum`

 A sum of at most 2^c products f_i(z)·f'_i(z'), all values below b in absolute value, factors
through c bits with the bound b. 
