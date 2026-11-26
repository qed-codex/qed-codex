---
{
  "module": "proof/rates/GeneralPieces/GenF/Borel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Borel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Borel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Coefficients of a power series as derivatives at 0

α! times the coefficient of x^α in F is the constant term of the derivative of F with respect to the
variables of x^α, one after the other (`borel_zero`). Here the coefficients of the products of
exponentials in the proof of
Lemma 9 (Appendix B) are identified this way, by their differential equations in the variables x_n,
x'_n; the paper instead expands the exponentials and compares coefficients. 

### `expo`

 The exponent of the monomial ∏_{i ∈ L} x_i. 

### `pdL`

 The derivatives with respect to the variables of the list, the first of the list first. 

### `pderiv_pderiv`

 Two derivatives commute. 

### `borel_step`

 (β + e_i)!·(the coefficient of x^β·x_i in F) = β!·(the coefficient of x^β in ∂F/∂x_i). 

### `borel_zero`

 α! times the coefficient of x^α = ∏_{i ∈ L} x_i in F is the constant term of the derivative of F
with respect to the variables of L. 
