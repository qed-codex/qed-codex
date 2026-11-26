---
{
  "module": "Zeta23/PairCeiling/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Grid.lean — closed forms of E = ∫₀ˣ D at the grid points (consumed by Bridge.lean):
  Efun s N (m/N) = Σ_{i<m} ( Csum s i / N − (((i+1)/N)³ − (i/N)³)/6 ),   m ≤ N.
-/
```

### `Dfun_ae_cell`

 a.e. on a cell, D is the polynomial C_i − t²/2. 

### `integral_Dfun_cell`

 the cell integral of D. 

### `Efun_grid`

 **E at the grid points.** 

### `Dfun_grid`

 D at the grid points (right value): D(m/N) = C_m − (m/N)²/2, m ≤ N. 
