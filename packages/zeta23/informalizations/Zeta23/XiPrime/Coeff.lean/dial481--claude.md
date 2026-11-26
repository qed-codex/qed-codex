---
{
  "module": "Zeta23/XiPrime/Coeff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff.lean — the ξ′ coefficient development, assembled.

The two coefficient families of [XF′]:
  theorem xiCoeffFamily_hyps : xiCoeffFamily.Hyps      (b_N = C(N; L_T), L_T = l/2 + iπ/4  — ξ′)
  theorem wCoeffFamily_hyps  : wCoeffFamily.Hyps       (b_N = C(N; l/2)                    — Z′)
from
  Coeff/Basic      pointwise algebra of C(N;Λ⋆), majorant ‖C‖ ≤ Λ + log·F;
  Coeff/Abel       Mertens/Abel step (the one analytic input: Cheb.mertensFirst);
  Coeff/PowerSums  Σ_{N≤e^u}Λ^{∗m}(N)/N ≤ (u+mK)^m/m!;
  Coeff/Upper      S(u) ≤ C(1+u)²  ⇒ (H1), (H2);
  Coeff/DiagLaw    (H3): S(y) = l²∫₀^{y/l}D₁ + o(l²)   [XF′ Lemma 7.1]  (uses Coeff/NonSquarefree, Coeff/MainTerm);
  Certificate/D1   continuity / nonnegativity / truncation of D₁.
  Also here: Coeff/LSeries (L(C_J,s) = B/(Λ⋆−A), for the explicit-formula modules).
-/
```

### `norm_real_half_l_ge`

 ‖(l/2 : ℂ)‖ ≥ l/2. 

### `xiCoeffFamily_hyps`

 **[XF′ Lemma 7.1 + Remark 7.2] for the ξ′ family b_N = C(N; L_T).** 

### `wCoeffFamily_hyps`

 **the same for the Z′ family b_N = C(N; l/2) (real parameter).** 
