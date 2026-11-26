---
{
  "module": "proof/rates/ExplicitCost/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One certificate for the machine that reads K and g

`entryPoly : EntryPoly`. The certificates of the constructions are those of
proof/machines/QueryMachines/Poly.lean; those of the plain functions, jointly in K, g and the input,
are those of proof/rates/PaddedDescent/F/CertNet.lean. Here: the numbers P_a and c_{a,b} are lengths
of lists in the input (`keepsU_askedData`), K and g are lengths of lists in the input
(`kOf_unary`, `gOf_unary`), and the two queries (b, z_b) and ((a, b), (z_a, z_b)) jointly in K and g
(`qMb_joint`, `qPsi_joint`). 

 ## The plain functions 

### `keepsU_askedData`

 The numbers P_a and c_{a,b} are given in unary: they are lengths of lists in the input. 

### `kOf_unary`

 K is given in unary. 

### `gOf_unary`

 g is given in unary. 

### `qMb_joint`

 The query (b, z_b), jointly in K, g and the input. 

### `qPsi_joint`

 The query ((a, b), (z_a, z_b)), jointly in K, g and the input. 

### `isYes_polyT`

 The test whether the answer is not 0 is polynomial-time. 

### `qW_data`

 The query (a, z_a) with the K and g of the input. 

### `qF_data`

 The query ((a, b), (z_a, θ_{a,b})) with the K and g of the input. 

### `qMb_data`

 The query (b, z_b) with the K and g of the input. 

### `qPsi_data`

 The query ((a, b), (z_a, z_b)) with the K and g of the input. 

 ## The machines 

### `memCert`

 The test for membership: one query. 

### `wCert`

 W_a: one query. 

### `psiCert`

 Ψ_{a,b}: one query. 

### `fCert`

 f_{a,b}: one query. 

### `wDataCert`

 [z_a ∈ S_a]·W_a(z_a). 

### `psiDataCert`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b). 

### `fDataCert`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}). 

### `termDataCert`

 One factor of a term. 

### `entryDataCert`

 One entry. 

### `entryPoly`

 **One certificate**: the machine that reads K and g from its input has polynomial-time steps. 
