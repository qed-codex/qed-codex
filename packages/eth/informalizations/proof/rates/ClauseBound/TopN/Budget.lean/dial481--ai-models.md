---
{
  "module": "proof/rates/ClauseBound/TopN/Budget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Budget.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Budget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Products and sums below powers of two, and the parameters for width k

`mul_le_pow`, `add_le_pow`: products and sums of numbers below powers of two. `stParN : StParN`: 2^β
bounds the number of clauses per variable of a leaf (`leafC_le`),
and the number of layers is large enough (`last_le`). Statements about natural numbers. 

### `mul_le_pow`

 A product of numbers below powers of two. 

### `add_le_pow`

 A sum of two numbers below powers of two. 

### `leafC_le`

 leafC τ k + 2 ≤ 2^β. 

### `last_le`

 After 2β + 4 divisions, each of which keeps at most two thirds of the clauses, fewer than n + 2
of 2^β·n clauses are left. 

### `stParN`

 The parameters are large enough for width k. 
