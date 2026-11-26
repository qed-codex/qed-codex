---
{
  "module": "Zeta23/RvM/Halving.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Halving.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/RvM/Halving.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/RvM/Halving.lean — the reflection-halving lemma.

For an abstract zero configuration Z (invariant under ρ ↦ 1 − ρ̄ with equal multiplicities,
Zeta23/Defs.lean), the zeros in a window T₁ < γ ≤ T₂ with β < 1/2 are mapped injectively by the
reflection onto zeros in the same window with β > 1/2, preserving multiplicity. Hence
    N(T₁,T₂) ≤ 2 · Σ_{window, β ≥ 1/2} m_ρ.
Used in Zeta23/RvM/LocalCount.lean — it lets the Jensen/ZerosBound disc (centre
2 + (t+½)i, radius 1.9·0.84) cover only {1/2 ≤ σ ≤ 1}, so ζ is never evaluated left of σ = 0.19
and the σ > 0 growth bound of Zeta23/RvM/ZetaGrowth.lean suffices (no functional equation / Stirling).
The statement is ℝ-valued to save casts downstream.
-/
```

### `N_le_two_mul_half`

 **Reflection halving.** N(T₁,T₂) ≤ 2 · Σ_{ρ ∈ window, Re ρ ≥ 1/2} m_ρ (as reals). 
