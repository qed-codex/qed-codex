---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/EntryError.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/EntryError.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/EntryError.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/EntryError.lean — the entry-error integral of the ξ′ explicit formula.
PURE REAL ANALYSIS, no ζ:  for a weight w (a two-bump product concentrated at
a, b ≥ T — in the application w(t) = H(5/4+it) = φ̂·φ̂ with bumps at τ_k, τ_l) and a function g
(in the application g = E′/E − B/(L⋆−A) on the line, from Expansion.lean) with
   ‖g‖ ≤ C_g everywhere  and  ‖g(t)‖ ≤ ε(|t − (a+b)/2| + 1) for t ≥ T/4,
   ‖w(t)‖ ≤ W·K_a(t)K_b(t),   (|t−a|+|t−b|)‖w(t)‖ ≤ W′·K_a(t)K_b(t),   K_c(t) := 1/(1+(t−c)²),
one gets  ‖∫ w·g‖ ≤ ε(W + W′/2)·8π/(4+(a−b)²) + C_g·W·16π/(9T²)   [XF′ Thm 4.2 proof (b),(c)].
The Cauchy convolution bound ∫ K_a K_b ≤ 8π/(4+(a−b)²) is the Δ⁻²-decay of the entry error.
-/
```

 ## 1. Cauchy kernels 

### `cauchyK`

 K_a(t) := 1/(1 + (t−a)²). 

### `cauchyK_mul_le`

 the pointwise product bound behind the Δ⁻²-decay:
K_a K_b ≤ 4/(4+(a−b)²)·(K_a + K_b). 

### `integral_cauchyK_mul_le`

 **Cauchy convolution**: ∫ K_a K_b ≤ 8π/(4 + (a−b)²). 

### `cauchyK_far`

 far region: for a ≥ T > 0 and t ≤ T/4, K_a(t) ≤ 16/(9T²). 

### `setIntegral_cauchyK_mul_far`

 ∫_{t ≤ T/4} K_a K_b ≤ 16π/(9T²) for a ≥ T > 0. 

 ## 2. The core entry-error estimate 

### `abs_sub_midpoint_le`

 |t − (a+b)/2| ≤ (|t−a| + |t−b|)/2. 

### `entry_core`

 **core estimate** (see file header). 

### `entry_core_mirror`

 the mirrored core estimate: bumps at −a, −b and the ε-bound for t ≤ −T/4
(reduce to entry_core by t ↦ −t). 
