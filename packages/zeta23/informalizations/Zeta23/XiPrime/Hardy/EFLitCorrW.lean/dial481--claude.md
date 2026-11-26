---
{
  "module": "Zeta23/XiPrime/Hardy/EFLitCorrW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFLitCorrW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFLitCorrW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFLitCorrW.lean — the W explicit formula in "literature form with correction" on a line
Re s = c, 1 < c ≤ 5/4.  [XF′ Prop 9.1 + Thm 9.2 (a)]:
   Σ'_{ρ ∈ 𝒩_W} m_ρ h_k(γ_ρ) = literatureRHSW k + JcorrW c k − Σ_{ρ ∈ E₀} m_ρ H(ρ),
   literatureRHSW k = literatureRHS k + (H(0) + H(1))   (pole weight 2; GramBridgeW),
   JcorrW c k := (1/2π) ∫ [H(c+it) + H(1−c−it)]·(E₂′/E₂)(c+it) dt,
from three inputs taken as Props (discharged in Hardy/EFMain.lean): the full-line identity for
F_𝒵 = L₂ + W′/W, the L₋-line identity (1/2π)∫[H+H̃](L − L₂) = ½(H(0)+H(1)),
and the line facts for E₂; plus the c-generic ζ-side evaluation (1/2π)∫[H+H̃]·E = literatureRHS k
(ExplicitFormula/LitCorr.Efn_line_identity, with HwC and its integrability helpers).
Pointwise on the line: F_𝒵 = E₂ + E₂′/E₂ (EFBasic.FZfn_eq) and E₂ = E − (L − L₂) (EFBasic.E2fn_eq_Efn_add).
-/
```

 ## objects on the line Re s = c 

### `dE2`

 E₂′/E₂ on the line. 

### `JcorrW`

 the W correction functional JcorrW c k := (1/2π) ∫ [H(c+it)+H(1−c−it)]·(E₂′/E₂)(c+it) dt. 

 ## the three input Props 

### `WFullLineIdentityWith`

 The full-line identity for F_𝒵 = L₂ + W′/W with a GIVEN finite low-zero set E₀. 

### `WFullLineIdentity`

 The full-line identity for F_𝒵 = L₂ + W′/W, with the finite low-zero set E₀. 

### `LminusLineIdentity`

 The L₋-line identity. 

### `E2LineFacts`

 The E₂ facts on the whole line Re s = c (for the chosen c). 

 ## the W explicit formula, literature form with correction 

### `FZfn_line_split`

 pointwise on the line: F_𝒵 = E − (L − L₂) + E₂′/E₂. 

### `w_EF_lit_corr`

 **the W explicit formula, literature form with correction** (see file header). 
