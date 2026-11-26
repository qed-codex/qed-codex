---
{
  "module": "proof/rates/GeneralPieces/GenF/Coeff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Coeff.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Coeff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Multi-index factorials and the linear form Σ_v x_v·c_v

Tools for "Expanding the exponentials" (Appendix B, the paragraph on generating functions): α! = ∏_v
α_v! (`fac`), its value at 0 and its change when one variable is added (`fac_zero`,
`fac_add_single`); induction on a multi-index, one variable at a time (`induction_single`);
the identity a·(n + 1) = (n + 1)•a in a ℚ-algebra (`mul_natCast_succ`); and ∂/∂x_i Σ_v x_v·c_v = c_i
(`pderiv_lin`). 

 ### Multi-indices 

### `fac`

 α! = ∏_v α_v!. 

### `induction_single`

 Induction on a multi-index: one more variable at a time. 

 ### The linear form Σ_v x_v·c_v 

### `pderiv_lin`

 ∂/∂x_i Σ_v x_v·c_v = c_i. 
