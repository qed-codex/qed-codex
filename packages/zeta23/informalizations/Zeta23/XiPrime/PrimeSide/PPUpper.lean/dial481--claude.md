---
{
  "module": "Zeta23/XiPrime/PrimeSide/PPUpper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/PPUpper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/PPUpper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/PPUpper.lean — the Frobenius UPPER bound for the P-part Gram
matrix of an arbitrary Dirichlet polynomial (consumed by Lemma 6.1, where it is applied to the
re-expansion coefficients e_r of [XF′] §6).

  Σ_{k,l<d} Q_{kl}(e)²  ≤  K·L²·( T·L·Σ‖e‖²/N + L·Σ‖e‖² + L·S₁(e)² + L·l·log l·(l + S₁(e))² ),
  Q_{kl}(e) := ∫ φ̂(τ−τ_k) φ̂(τ−τ_l) P_e(X;τ) dτ = GentryNu (Pc p.X e) p F k l,
for T ≥ T₀ under LocalHypsCore, e 1 = 0.  Route: [lem:ends] for the density ν = P_e alone
(lem_ends_nu with B = l + S₁/π) turns Σ Q² into L²·𝓜[P_e,P_e] + O(L³ l log l B²), and [prop:PP]
for P_e (PPInput) with g ≤ L bounds 𝓜[P_e,P_e].
-/
```

### `nuBound_Pc'`

 NuBound for `P_e` (regime `l ≥ 0`). 

### `sumW2g_le`

 `Σ ‖e‖²/N · g(log N) ≤ L · Σ ‖e‖²/N` since `0 ≤ g ≤ A_φ ≤ L`. 

### `frobSq_Ppart_le`

 **Frobenius upper bound for the P-part Gram matrix of an arbitrary Dirichlet polynomial.** 
