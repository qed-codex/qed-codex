---
{
  "module": "Zeta23/WeilEF/GammaRBracket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/GammaRBracket.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/GammaRBracket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/GammaRBracket.lean — the critical-line Γℝ bracket; proves
`Zeta23.WeilEF.gammaR_bracket`:

  logDeriv Γℝ(1/2+it) + logDeriv Γℝ(1/2−it) = Re ψ(1/4 + it/2) − log π      (t ∈ ℝ),

from Γℝ(s) = π^{−s/2}Γ(s/2) (Mathlib `Complex.Gammaℝ`), logDeriv Γℝ(s) = −(log π)/2 + ψ(s/2)/2
for re s > 0, and the conjugation symmetry ψ(conj z) = conj ψ(z) (from the partial-fraction
series Zeta23.DigammaSeries.hasSum_digamma_series).
-/
```

### `digamma_conj`

 conjugation symmetry of the digamma function off the poles. 

### `logDeriv_Gammaℝ`

 `logDeriv Γℝ(s) = −(log π)/2 + ψ(s/2)/2` for `re s > 0`. 

### `gammaR_bracket`

 **The critical-line Γℝ bracket** is EF_lit's Γ-integrand: for real t,
logDeriv Γℝ(1/2+it) + logDeriv Γℝ(1/2−it) = Re ψ(1/4+it/2) − log π  (ψ = digamma;
Γℝ(s) = π^{−s/2}Γ(s/2), logDeriv Γℝ(s) = −(log π)/2 + ψ(s/2)/2, conj symmetry). 
