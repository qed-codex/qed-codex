---
{
  "module": "proof/rates/ClauseBound/Inst/CertHalfPart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfPart.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/CertHalfPart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers of partitions and the table of all partitions are polynomial-time

Certificates (`PolyT`, `Unary`) for the functions of proof/rates/ClauseBound/Inst/HalfPart.lean.
Without a pad: the table p(0), …, p(W) with W in unary (`pTab_polyT`; its entries have at most W + 1
binary digits
because p(E) ≤ 2^E), the number `hF c₀ lam` with lam in unary (`hF_unary`), the sums `RrowF`,
`RcolF` with h in unary (`RrowF_polyT`, `RcolF_polyT`). With the pad: the table of all partitions
(`allTabF_polyT`), a fold inside a fold, each with its state cut off by the pad after every step. 

 ### Without a pad 

### `nextP_polyT`

 The next entry of the table of numbers. 

### `len_pTab_le`

 The word of the table p(0), …, p(j) has length at most (j + 1) * (3 * (j + 1) + 4) + 2. 

### `pTab_polyT`

 The table p(0), …, p(W) is polynomial-time in W in unary. 

### `pzF_polyT`

 Reading a table of numbers at an integer. 

### `hF_polyT`

 `hF c₀ lam` is polynomial-time in lam in unary. 

### `hF_unary`

 `hF c₀ lam` is given in unary if lam is. 

### `RrowF_polyT`

 The sum of the row-wise pieces is polynomial-time in h in unary and s. 

### `RcolF_polyT`

 The sum of the column-wise pieces is polynomial-time in h in unary and s. 

 ### With the pad 

### `initT_polyT`

 The table before the first round. 

### `stepE_polyT`

 One step of a round. 

### `roundF_polyT`

 One round with the pad. 

### `allTabF_polyT`

 The table of all partitions of 0, …, W with the pad is polynomial-time in the pad and W in
unary. 
