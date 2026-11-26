---
{
  "module": "Zeta23/ThmE/ContourChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ContourChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ContourChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/ContourChi.lean — Rectangle identity for H·(completed L)'/(completed L)
(primitive χ mod q > 1): no pole terms (the completed L-function is entire), via the pole-free
weighted argument principle Zeta23.Analytic.rectangleIntegral'_mul_logDeriv.
Runs with f := completedLSym χ = q^{s/2}·completedLFunction χ (symmetrized form:
same zeros; cleanest functional equation completedLSym_one_sub).
-/
```

### `rectangle_identity_chi`

 **Rectangle identity for L(s,χ)** at a zero-free height R (no pole terms):
(1/2πi)∮_{[1−c,c]×[−R,R]} H·Λ'/Λ(·,χ) = Σ_{|γ|<R} m_ρ H(ρ). 
