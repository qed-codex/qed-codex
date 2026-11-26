---
{
  "module": "Zeta23/XiPrime/Hardy/EFJTermW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFJTermW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFJTermW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFJTermW.lean — the W correction functional JcorrW c k on the line Re s = c, 1 < c ≤ 5/4, as the
W INSTANCE of the generic J-term theorem ExplicitFormula/JTerm.JcorrG_estimate.
[XF′ Thm 9.2 (b)–(e)]: E ↦ E₂, freezing parameter the REAL number L_{2⋆}(τ⋆) (so the mirrored weight freezes to the SAME
Dirichlet object — (G1) is vacuous).  Inputs: E2LineFacts c (EFLitCorrW) and FreezeFactsW c (below; corresponding to
EFExpansion X5, X6, X7-conj).  JcorrW_estimate is consumed by Hardy/EFMain.
-/
```

### `DfroC`

 The frozen Dirichlet object on the line c with real parameter L_{2⋆}(τ):
D_c(τ; t) := B(c+it)/(L2star τ − A(c+it))  (= DfroG c (L2star τ)). 

### `FreezeFactsW`

 The freezing facts for E₂ on the line c. 

### `JcorrW_estimate`

 **the W J-term estimate** — instance of JcorrG_estimate at (c, dE2 c, τ ↦ (L2star τ : ℂ)). 
