---
{
  "module": "proof/rates/CountedRecursion/PolyProcedure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyProcedure.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PolyProcedure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The procedure has polynomial-time steps

One certificate for each of `rowWeight`, `rowPair`, `rowFactor`, for the four procedures as one
machine, and for `procedure c`. Each is written along the definition of the machine
(GridProcedures.lean) with the rules of PolyRules.lean; the plain functions are those of
PolyQueries.lean; `entryData` has its certificate from proof/rates/ExplicitCost/Poly.lean. 

### `rowWeight_poly`

 W_a. 

### `rowPair_poly`

 Ψ_{a,a'}. 

### `rowFactor_poly`

 f_{a,a'}. 

### `rowMem_poly`

 The membership test, which answers yes to every string of g³λ bits, has polynomial-time steps. 

### `gridProcsData_poly`

 The four procedures as one machine. 

### `procedure_poly`

 **The procedure for an entry has polynomial-time steps.** 
