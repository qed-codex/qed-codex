---
{
  "module": "proof/rates/CountedRecursion/Chain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Chain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/Chain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The chain: from one depth to the next
With X_j = K_j(Λ_j + 𝔅_j): X_j ≤ X_{j+1}^{c+5} (`chainBase`: the last of the crude bounds in the
proof of Theorem A(b), «K(L + B') ≤ Ξ^{c+5}», at the bounds for λ and B),
and the exponents of 2 (`chainExponent`): the bound for K_j²Λ_j of `chainLabel`, multiplied by e_j ∈
[0, 1], with e_{j+1} = (ρ + 3ζ_j)e_j + 3/K_j and K_{j+1}² = g_j⁴. 

### `baseAt_succ`

 X_{j+1} is the Ξ of the callers of the depth j + 1. 

### `chainBaseFrom`

 `ChainBaseFrom`. 

### `chainBase`

 `ChainBase`. 

### `exponent_real`

 The arithmetic of `ChainExponent`. 

### `chainExponentFrom`

 `ChainExponentFrom`. 

### `chainExponent`

 `ChainExponent`. 
