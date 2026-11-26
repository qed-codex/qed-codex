---
{
  "module": "proof/rates/CountedRecursion/Expansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Expansion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Expansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The expansion over the patterns

Proof of Theorem A (b), the step from ℓ to ℓ + 1: d^{|ℛ|}Z = Σ_ι Z_ι over the |𝓘|^{|ℛ|} ≤ Ξ^{cg⁴/4}
functions ι : ℛ → 𝓘, and each Z_ι is the value of the row network and of the column network.
* `expansion : Expansion`: by `Printed.stCliqueValue` (the clique of Definition 3 has the value of
  the plain picture, one string for each edge), `ClauseBound.Alg.GridNet.ZW_mul_eq_sum` (clause (a)
  of Definition 7 at every rectangle of the grid) and `ClauseBound.Alg.GridNet.value_gridN` (either
  network has the value of the term).
* `patternsFew : PatternsFew`: |ℛ| ≤ g⁴/4, |𝓘| ≤ (2λ)^c and 2λ ≤ Ξ. 

### `expansion`

 **d^{|ℛ|}Z = Σ_ι Z_ι over the |𝓘|^{|ℛ|} functions ι : ℛ → 𝓘, and each Z_ι is the value of the
row network and of the column network.** 

### `patternsFew`

 **There are |𝓘|^{|ℛ|} ≤ Ξ^{cg⁴/4} functions ι**: the inequality, raised to the fourth power; and |ℛ|
≤ g⁴/4. 
