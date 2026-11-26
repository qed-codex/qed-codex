---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Beta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Beta.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Beta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers β_c and θ_c

This file proves six statements of proof/sparsification/SparsificationLemma/Cal/Defs.lean on the
numbers β_c and θ_c of Calabro's dissertation, which the sparsification of Appendix C uses: the
recursion for β_c (`StBetaRec`);
the closed form β_c = 2·(8α)^(c−1)·Cat_(c−1) (`StBetaCat`), by induction with the recursion of the
Catalan numbers; Cat_j ≤ 4^j (`StCatLe`), since (j+1)·Cat_j is the central binomial coefficient;
hence β_c ≤ 2·(32α)^(c−1) (`StBetaLe`); the bound β₁ + … + β_{k−1} ≤ 4·(32α)^(k−2) (`FactIV`), a
geometric sum with ratio at least 2; and the sum of the θ_c (`StDegSum`). 

### `betaC_add_two`

 The defining equation of β_(c+2). 

### `betaC_one`

 β₁ = 2. 

### `betaC_zero`

 β₀ = 0, the convention of Cal/Defs.lean. 

### `thetaC_of_pos`

 θ_c = α·β_c for c ≥ 1. 

### `stBetaRec`

 The recursion for β_c written as a sum over h = 1, …, c−1 (the form of `StBetaRec`), rather than
over `Fin` as in the definition. 

### `stBetaCat`

 β_c = 2·(8α)^(c−1)·Cat_(c−1). 

### `stCatLe`

 Cat_j ≤ 4^j. 

### `catalan_pos`

 Cat_j ≥ 1. 

### `betaC_pos`

 β_c ≥ 1 for c ≥ 1, if α ≥ 1. 

### `stBetaLe`

 β_c ≤ 2·(32α)^(c−1). 

### `geom_le`

 2·(1 + q + … + q^m) ≤ 4·q^m for q ≥ 2. 

### `factIV`

 The bound `FactIV`: β₁ + … + β_{k−1} ≤ 4·(32α)^(k−2), for α ≥ 1 and k ≥ 2. 

### `sum_range_betaC`

 β₀ + β₁ + … + β_{k−1} = β₁ + … + β_{k−1}, for k ≥ 1. 

### `stDegSum`

 For α ≥ 1 and k ≥ 2: θ₀ + … + θ_{k−1} = 2 + α·(β₁ + … + β_{k−1}), which is at most 2 +
4α·(32α)^(k−2) by `FactIV`; and 8·(2 + 4α·(32α)^(k−2)) = 16 + (32α)^(k−1). 
