---
{
  "module": "proof/rates/PaddedDescent/F/CertEval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertEval.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/CertEval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The evaluations and the choice of the layers are polynomial-time

Certificates (`PolyT`) for the part of the function `A` of proof/rates/PaddedDescent/F/Prog.lean
that works on one sparse formula: the value of a network (`valF`), one
evaluation (`evalF`), the test that puts a clause into a layer (`dropE`), the placing of a clause
(`placeAt`, `placeE`), the layers (`layersF`) and the count
(`countM`). They prove the interface statement `StCertValF` of
proof/rates/PaddedDescent/F/Interfaces.lean, and certificates for an evaluation, the layers and the
count
whose arguments are polynomial-time functions of a context; the certificates of the rebalancing, the
descent through the levels, the brute force at the bottom and the network of marks are hypotheses. 

 ### The value of a network 

### `certValF`

 The top rebalancing, all levels and the brute force at the bottom are polynomial-time, for every
network whose four functions are. 

 ### One evaluation 

### `cls_polyT`

 The list of all clauses with the index of their layer is polynomial-time. 

### `nProf_polyT`

 The number of profiles is polynomial-time, for g and the number of layers in unary and a
polynomial-time number of clauses. 

### `evalF_polyT`

 One evaluation, with the pad, the schedule, the parameters and the layers as arbitrary functions
of a context. 

 ### The choice of the layers, for any polynomial-time evaluation function 

### `dropE_polyT`

 The test that puts a clause into layer i. 

### `placeAt_polyT`

 A clause added to layer i. 

### `placeE_polyT`

 A clause put into the first layer whose test holds. 

 ### The layers and the count 

### `empty_polyT`

 R + 1 empty layers. 

### `layersF_polyT`

 The layers of a formula, with the number of layers in unary. 

### `countM_polyT`

 The count of one sparse formula, with the number of layers in unary. 
