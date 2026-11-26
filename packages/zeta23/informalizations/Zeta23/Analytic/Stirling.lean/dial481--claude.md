---
{
  "module": "Zeta23/Analytic/Stirling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Analytic/Stirling.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Analytic/Stirling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Analytic/Stirling.lean — shared Stirling/digamma asymptotics.

This is the shared home for complex Stirling-type asymptotics of Γ, log Γ and ψ = Γ'/Γ.
Consumers:
  • Zeta23/GammaFacts/Mu.lean: ψ on the vertical line Re = 1/4, error O(1/τ²);
    the trigamma series for the μ′ bound;
  • the Riemann–von Mangoldt argument: Im log Γ(1/4 + iT/2) main term; |Γ| growth
    in strips;
  • the explicit-formula argument: digamma growth on vertical strips.
Builds on Zeta23.GammaFacts.Series: digamma_series, hasSum_digamma_series,
summable_digamma_series, inv_gamma_eq_prod (Weierstrass product for 1/Γ).
-/
```

### `differentiableAt_digamma`

 ψ is differentiable on the integer complement (Γ is analytic and nonvanishing there). 

### `hasSum_trigamma`

 Trigamma termwise series (used in Zeta23/GammaFacts/Mu.lean, deriv_bound).
ψ′(z) = Σ_{n≥0} 1/(z+n)², differentiating the digamma series termwise.   
