---
{
  "module": "proof/rates/CountedToPadded/SolverPoly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/SolverPoly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/SolverPoly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver is polynomial-time

Proof of `SolverOfMachinePolyFrom` (Defs.lean). The certificate of `onTables M` is
`QueryMachine.plug_isPolyT M lookup` over `lookupIsPoly`; its coding of the states is the one that
`solverOfMachine` uses. 

### `ceilMul_poly`

 Rounding up is polynomial-time. 

### `needOf_poly`

 The exponent is polynomial-time. 

### `onTablesIsPoly`

 The certificate of `onTables M`. Its coding of the states is the one in `solverOfMachine`. 

### `solverOfMachinePolyFrom`

 `SolverOfMachinePoly` follows from `RunForPoly`. 
