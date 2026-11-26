---
{
  "module": "Zeta23/XiPrime/Coeff/H3.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/H3.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/H3.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/H3.lean — (H3) assembled  [XF′ Lemma 7.1].

  ∀ ε > 0 ∃ T₀ ∀ T ≥ T₀ ∀ y ∈ [0, l(T)]:  | Σ_{N≤e^y} ‖C(N;Λ⋆(T))‖²/N − l(T)²·∫₀^{y/l} D₁ | ≤ ε·l(T)²
from Coeff/DiagLaw (partition; remainder bound; layers ω = k ≥ 2), Coeff/LayerOne (layer ω = 1),
Coeff/Tail, Certificate/D1, and Coeff/MainTerm.
-/
```

### `dcoef_eq_D1coeff`

 d_{j+2} is the (j+1)-st integrated D₁ coefficient:  dcoef (j+2) = D1coeff (j+1)/(2(j+1)+4). 

### `l_ge_of_le`

 l(T) ≥ l₀ once T ≥ 2π·e^{l₀}. 

### `coeff_H3`

 **(H3) the diagonal law** [XF′ Lemma 7.1] for a parameter family with Re Λ⋆ = l/2, |Im Λ⋆| ≤ 1. 
