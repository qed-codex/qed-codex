---
{
  "module": "proof/rates/PaddedDescent/F/ArithGlob.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithGlob.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithGlob.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers that stay fixed during the descent (definitions only)

For precision s and n variables: the bounds Ub and Pb of the network of marks, and the values of X,
Z, Qm, Wm, L with which the invariant `Inv` of
`PaddedDescent/F/ArithInv.lean` is used. 

### `Xof`

 X = ⌊n/2^s⌋ + 1. The padding string, which the algorithm takes besides the formula, has length
2^(C₀·X) for a constant C₀. 

### `Zof`

 Z = Y², with Y = `Ytop s`: the part of the bound on K_j²·Λ_j (K_j nodes, Λ_j bits on an edge of
the clique at level j) that does not decay with j. 

### `Ubof`

 The bound on the number of shared bits of the network of marks at the top, for width k. 

### `Pbof`

 The bound on the size of the network of marks at the top, if every variable occurs in at most Δ
clauses. 

### `Qmof`

 Qm = Ub + X + Z: a bound on K_j²·Λ_j at all levels. 

### `Wmof`

 Wm = 17·Qm·K³, where K = `Ktop s` is the number of nodes at the top level: a bound on the number
of bits of an entry at all levels. 

### `Lof`

 L = 6s + 24 + (binary digits of n): Qm + 1 ≤ 2^L. 
