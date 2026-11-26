---
{
  "module": "proof/rates/GeneralPieces/GenF/PDeriv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/PDeriv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/PDeriv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The derivatives with respect to the variables x_i of the two exponentials

∂/∂x_i e^w = (∂w/∂x_i)·e^w (`pderiv_expW`). For 𝒪 = Σ_v x_v·O_v: ∂/∂x_i ∘ 𝒪 = 𝒪 ∘ ∂/∂x_i + O_i
(`pderiv_opX`), hence, if the O_v commute, ∂/∂x_i (e^𝒪 f) = e^𝒪 (∂f/∂x_i) + e^𝒪 (O_i f)
(`pderiv_expOp`, `pderiv_expD`). 

### `pderiv_expN`

 ∂/∂x_i Σ_{n ≤ N} wⁿ/n! = (∂w/∂x_i)·Σ_{n < N} wⁿ/n!. 

### `pderiv_expW`

 ∂/∂x_i e^w = (∂w/∂x_i)·e^w. 

### `pderiv_mapE`

 ∂/∂x_i commutes with a linear map that is applied to every coefficient. 

### `pderiv_opX`

 ∂/∂x_i ∘ 𝒪 = 𝒪 ∘ ∂/∂x_i + O_i. 

### `mapE_opX`

 O_i, applied to every coefficient, commutes with 𝒪 if the O_v commute. 

### `pderiv_iterate`

 ∂/∂x_i 𝒪^{n+1} f = 𝒪^{n+1} ∂f/∂x_i + (n+1)·𝒪ⁿ O_i f. 

### `pderiv_expOp`

 ∂/∂x_i (e^𝒪 f) = e^𝒪 (∂f/∂x_i) + e^𝒪 (O_i f), if the O_v commute. 

### `pderiv_expD`

 The same for commuting derivations. 
