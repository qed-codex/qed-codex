---
{
  "module": "proof/rates/ClauseBound/Gen/PartA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/PartA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/PartA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponents x_ℓ of the numbers K_ℓ of Theorem A (Appendix A)

The numbers K_ℓ of Theorem A are powers of two; their exponents x_ℓ satisfy x_{ℓ+1} = 2·x_ℓ + 6ℓ +
2·x₀. This file proves K_ℓ = 2^{x_ℓ}, log K_ℓ = x_ℓ,
x_ℓ ≥ x₀ + 2ℓ, ζ_ℓ > 0, and 2^10·(3x₀+6) ≤ 2^{x₀} for x₀ ≥ 18. 

### `x`

 x_ℓ, the exponent of K_ℓ. 

### `K_eq`

 K_ℓ = 2^{x_ℓ}. 

### `x_ge`

 x_ℓ ≥ x₀ + 2ℓ. 

### `K_cast`

 The real number K_ℓ is 2^{x_ℓ}. 

### `logb_K`

 log K_ℓ = x_ℓ. 

### `zeta_pos`

 ζ_ℓ > 0. 

### `pow_x₀`

 2^10·(3x₀+6) ≤ 2^{x₀} for x₀ ≥ 18. 
