---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/XiEFAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/XiEFAssembly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/XiEFAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/XiEFAssembly.lean — the (EF4) assembly [XF′ Thm 4.2].
Inputs that live in other files are taken here as explicit Prop-valued hypotheses
(GramBridgeFacts — GramBridge.lean; TestWeightFacts — TestWeight.lean; CoeffFacts —
Coeff/LSeries.lean), so that this file is complete independently of those files;
ExplicitFormula/Main.lean instantiates them.
Everything else is proved here: xiPrime_EF_lit_corr' (EF1+EF2+EF3, F2 from ZeroFree),
Jcorr_estimate (Expansion + EntryError + DirichletLine), prime_term_complex (PrimeTermJ),
FamilyHyps.perT / pow_log_absorb (FamilyFacts).
-/
```

 ## The ξ′ explicit formula, literature form with correction (hypothesis-free) 

### `xiPrime_EF_lit_corr'`

 Σ' m_{ρ₁} h_k(γ_{ρ₁}) = literatureRHS k + Jcorr k, with (F2) from ZeroFree, (EF1) and the rational
line from FullLine. 

 ## The input Props 

### `xiCoeffJ'`

 The j-part of the coefficients: C_J(N;Λ⋆) := C(N;Λ⋆) + Λ(N) (= `xiCoeffJ`). 

### `CoeffFacts`

 The inputs (C1)+(C2) at Re s = 5/4 and (C3), in consumer shape. 

### `GramBridgeFacts`

 GramBridge inputs (S1, S2, S3', S4). 

### `TestWeightFacts`

 The TestWeight inputs W0–W3, in consumer (cauchyK) shape. 

 ## Small helpers 

### `k_log_eq_zero`

 a compactly supported k vanishes at ±log N for N > e^L. 

 ## The assembly 

### `xiEF_of`

 **(EF4)** assembled from the preceding pieces and the three input Props. 
