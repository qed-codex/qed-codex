---
{
  "module": "proof/threesat/Printed/LevelPoly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelPoly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/LevelPoly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The algorithm of the proof of Proposition 3 has polynomial-time steps
The counterpart of `Eight.ViaGrouping.stLevelKeepsP_of`
(proof/networks/Eight/ViaGrouping/LevelCert.lean) for `levelMachine`.
The certificates of the plain functions (the number of functions ι, the choice of the network, the
division, P_a, c_{a,a'}, Ψ_{a,a'}, f_{a,a'}, the check and the queries of W_a) are used here as
lemmas, such as `Eight.Level.Cert.numPat8_polyT` and `Eight.Level.Cert.factor_polyT`;
those of the constructions are in proof/machines/QueryMachines/Poly.lean; that of `networkOn` is in
proof/threesat/Printed/HandOver.lean. That the machine of Lemma 1 has polynomial-time steps is a
hypothesis here (`StGroupingPoly`). 

### `lamOf_unary`

 λ is given in unary. 

### `bitsOf_unary`

 B is given in unary. 

### `sideWQ_poly`

 The weight of a row or column, computed with queries to the tables, has polynomial-time steps. 

### `networkOn_gridProcs_poly`

 A machine for networks with polynomial-time steps, on the row network or the column network of
ι. 

### `levelLoop_poly`

 The loop over ι has polynomial-time steps. 

### `levelDiv_poly`

 The division at the end has polynomial-time steps. 

### `stLevelPoly_of`

 The machine of Proposition 3 has polynomial-time steps if M has. The hypothesis: the machine of
Lemma 1 has polynomial-time steps if M has. 
