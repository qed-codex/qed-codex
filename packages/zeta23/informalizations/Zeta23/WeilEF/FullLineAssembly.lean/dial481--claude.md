---
{
  "module": "Zeta23/WeilEF/FullLineAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/FullLineAssembly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/FullLineAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/FullLineAssembly.lean — the R → ∞ assembly of
`full_line_identity` from: rectangle_identity (Contour), the majorant pack + heights +
vertical limits (FullLine), horizontal_vanish (Horizontal), zero_sum_limit (ZeroSumLimit).
-/
```

### `corner_re_im`

 corners of the rectangle: real and imaginary parts. 

### `inv_two_pi_I_mul_I`

 `(1/(2πi))·(i·X) = (1/2π)·X`. 

### `full_line_identity`

 **Full-line identity** (R → ∞ along good heights; horizontal pieces vanish by
good_heights + digamma growth + the 1/R² decay of H):
(1/2π)∫ [H(c+it) + H(1−c−it)]·Λ'/Λ(c+it) dt = Σ_ρ m_ρ H(ρ) − H(0) − H(1),
with the zero-side sum the (absolutely convergent) tsum over the carrier. 
