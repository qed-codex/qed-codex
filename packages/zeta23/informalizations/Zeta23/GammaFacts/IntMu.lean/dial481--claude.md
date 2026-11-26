---
{
  "module": "Zeta23/GammaFacts/IntMu.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/IntMu.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/GammaFacts/IntMu.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/GammaFacts/IntMu.lean — the [eq:muints] Γ-half integrals.
Paper: "∫_T^{2T} μ(τ)dτ = Tℓ₁/(2π) + O(1/T)", "∫_T^{2T} μ(τ)² dτ = (Tℓ₁²/4π²)(1 + O(l⁻²))",
via "(eq:muints) follows from (eq:mufacts) … and ∫_T^{2T} log²(τ/2π) dτ = T(ℓ₁² + 1 − 2log²2)".
Both theorems take the Stirling field as a hypothesis (hst); the Stirling asymptotic itself is
proved elsewhere in the repository, so GammaFacts assembles with no Γ-hypothesis beyond it.
-/
```

### `StirlingHyp`

 The Stirling-field statement, as a standing hypothesis (same statement as
GammaFacts.stirling). 

### `integral_main_eq`

 FTC anchor: ∫_T^{2T} (1/2π)·log(τ/2π) dτ = T·ℓ₁/(2π) for T > 0. 

### `int_mu_of_stirling`

 **[eq:muints].1 given Stirling**: ∫_T^{2T} μ = Tℓ₁/(2π) + O(1/T). 

### `integral_main_sq_eq`

 FTC anchor: ∫_T^{2T} log²(τ/2π) dτ = T(ℓ₁² + 1 − 2log²2) for T > 0. 

### `int_mu_sq_of_stirling`

 **[eq:muints].2 given Stirling**: ∫_T^{2T} μ² = (Tℓ₁²/4π²)(1 + O(l⁻²)). 
