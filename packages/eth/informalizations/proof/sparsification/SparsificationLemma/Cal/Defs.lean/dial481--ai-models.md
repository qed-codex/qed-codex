---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sparsification theorem with Calabro's thresholds: definitions and statements

The numbers x = 32(k−1)²/ε and α = ⌈2(k−1)²·ε⁻¹·⌈log₂ x⌉⌉ are those of Step 5 of Appendix D, here
with ceilings; θ₀ = 2, β₁ = 2, θ_c = α·β_c for c ≥ 1 and
β_c = Σ_{h=1}^{c−1} 4α·β_{c−h}·β_h for c ≥ 2 are Calabro's thresholds, which the paper does not
print. The statements include (i) a bound on the length of a path (`FactI`), (iii) a bound on the
number of leaves of the tree,
and (iv) a bound on β₁ + … + β_{k−1} (`FactIV`); Step 5 of Appendix D cites the bound on the leaves
from Calabro's dissertation.
(i) and (iii) follow from the general theorem `SparsificationLemma.StGen`, as these thresholds
    satisfy `SparsificationLemma.ThrC` with τ = α.
This file has definitions only; the statements are propositions, proved in other files. 

 ### The numbers 

### `xC`

 x = 32(k−1)²/ε. 

### `logC`

 ⌈log₂ x⌉, computed as the least m with x ≤ 2^m. 

### `alphaC`

 α = ⌈2(k−1)²·ε⁻¹·⌈log₂ x⌉⌉. 

### `betaC`

 β₁ = 2 and β_c = Σ_{h=1}^{c−1} 4α·β_{c−h}·β_h for c ≥ 2. (β₀ = 0 is a convention of this file.) 

### `thetaC`

 θ₀ = 2 and θ_c = α·β_c for c ≥ 1. 

### `depthC`

 (β₁ + … + β_{k−1})·n: no path of the tree has more steps. 

### `yC`

 y = 32(k−1)²·log₂(32α)/(32α). 

### `sparsify`

 The formulas Φ₁, …, Φ_s that the procedure outputs on k, n, ε and φ: clauses that contain a
variable together with its negation are deleted first. 

 ### The numbers: statements 

### `StLogC`

 `logC` is ⌈log₂ x⌉, for k ≥ 2 and ε ∈ (0,1] (then x ≥ 32). 

### `StBetaRec`

 The recursion for β_c in the form of the module docstring. 

### `StBetaCat`

 β_c = 2·(8α)^(c−1)·Cat_(c−1), for c ≥ 1. 

### `StCatLe`

 Cat_j ≤ 4^j. 

### `StBetaLe`

 β_c ≤ 2·(32α)^(c−1), for c ≥ 1. 

### `FactIV`

 Fact (iv): β₁ + … + β_{k−1} ≤ 4·(32α)^(k−2), for k ≥ 2 and α ≥ 1. 

### `StThrCal`

 Calabro's thresholds satisfy the conditions of `ThrC` with τ = α, for every k and every α ≥ 1. 

### `StAlpha`

 The facts on x and α that are used, for k ≥ 3 and ε ∈ (0,1]: x ≥ 128, α ≥ 2, 32α ≥ 2x·log₂ x,
32α ≤ 2x·⌈log₂ x⌉ + 32; and k² ≤ α. 

### `StYLe`

 y ≤ ε whenever 32α ≥ 2x·log₂ x, x = 32(k−1)²/ε ≥ 128. 

### `StSqrt`

 For x ≥ 128: log₂ x + 1 + 16/x ≤ √x. 

### `StAlphaLe`

 32α ≤ (8k/ε)³, for k ≥ 3 and ε ∈ (0,1]. 

### `StDegSum`

 θ₀ + … + θ_{k−1} = 2 + α·(β₁ + … + β_{k−1}) ≤ 2 + 4α·(32α)^(k−2), which is Calabro's bound on
the number of clauses of a leaf that contain a given literal; and 8·(2 + 4α·(32α)^(k−2)) = 16 +
(32α)^(k−1). 

### `StDegLe`

 2 + 4α·(32α)^(k−2) ≤ (8k/ε)^(3k), for k ≥ 3 and ε ∈ (0,1]. 

 ### Facts on the tree of the procedure 

### `FactI`

 Fact (i): the procedure has stopped at every node that is reached after at most (β₁ + … +
β_{k−1})·n steps, so no path is longer. 

### `FactIIIy`

 Fact (iii), first part (the second part, y ≤ ε, is `StYLe`): the tree has at most 2^(yn) leaves. 

 ### The theorem 

### `SparsABC`

 **Sparsification of k-CNFs with Calabro's thresholds, as Step 5 of Appendix D uses it.** For k ≥
3, every n, a rational ε ∈ (0,1] and a k-CNF φ on n variables, the outputs are k-CNFs on the same
variables, none with a clause written twice; (a) there are at most 2^(εn) of them; (b) every
assignment that satisfies φ satisfies exactly one of them, and every other assignment satisfies
none; (c) in each of them every variable occurs in at most
2·(8k/ε)^(3k) + 2 clauses. 
