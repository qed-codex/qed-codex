---
{
  "module": "proof/rates/ClauseBound/Alg/CertCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertCount.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/CertCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Polynomial-time certificates (`PolyT`, `Unary`) for those plain functions of the network of a
k-CNF that do not depend on the width k (`mu`, `rows` of StepMachines/Prog/CountNet.lean), with the
number g of groups as part of the data. 

### `mu_polyT2`

 The number of clauses of a group, jointly in g and the formula. 

### `rows_polyT2`

 The list 0, …, μ - 1 of the clauses of a group, jointly in g and the formula. 

### `mu_unary2`

 The number of clauses of a group is given in unary, jointly in g and the formula. 
