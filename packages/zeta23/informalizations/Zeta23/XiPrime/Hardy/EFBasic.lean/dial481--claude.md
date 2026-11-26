---
{
  "module": "Zeta23/XiPrime/Hardy/EFBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFBasic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/EFBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/EFBasic.lean — basic objects of the W explicit formula [XF′ §9.0–9.1].
 * analyticity of Γℝ, χ = chiFE, L₂, W at the REAL points of the strip away from the poles (Hardy/Basic.lean
   has everything off the real axis);
 * E₂ := L₂ + ζ′/ζ ( = W/ζ where ζ ≠ 0 ) and F_𝒵 := L₂ + W′/W;  [XF′ (Z1)]  F_𝒵 = E₂ + E₂′/E₂ on 1 < Re s < 3/2
   wherever W ≠ 0;  E₂ = L₂ − A, E₂′ = L₂′ + B;
 * [XF′ (Z2)]  F_𝒵(1−s) = −F_𝒵(s),  E₂(s̄) = conj E₂(s),  F_𝒵(s̄) = conj F_𝒵(s)  (off ℝ);
 * the low zeros of W in a compact box of the half-plane Re s > 1 are finitely many, hence a line Re s = c,
   c ∈ [9/8, 5/4], carrying no zero of W of height < t₀ exists  (the "choice of c" of Hardy/EFMain).
-/
```

 ## 1. Analyticity at real points away from the poles 

### `differentiableAt_Gammaℝ_of_ne`

 Γℝ is differentiable at s unless s/2 is a non-positive integer. 

### `GoodStrip`

 points of the vertical strip 1 < Re s < 3/2: no pole of Γℝ(s), Γℝ(1−s) and s ≠ 0, 1. 

 ## 2. E₂ and F_𝒵 

### `E2fn`

 E₂ := L₂ + ζ′/ζ  (= W/ζ wherever ζ ≠ 0; = L₂ − A on Re s > 1). 

### `FZfn`

 F_𝒵 := L₂ + W′/W  [XF′ §9.0]. 

### `FZfn_eq`

 **[XF′ (Z1)]**  F_𝒵 = E₂ + E₂′/E₂ on 1 < Re s < 3/2 wherever W ≠ 0. 

### `derivE2_div_E2_eq`

 E₂′/E₂ = F_𝒵 − E₂. 

 ## 3. Symmetries (off the real axis) 

### `logDeriv_hardyW_one_sub`

 W′/W(1−s) = −W′/W(s) − 2L₂(s)  [XF′ (Z2)], wherever W(s) ≠ 0, off ℝ. 

### `FZfn_one_sub`

 **[XF′ (Z2)]**  F_𝒵(1−s) = −F_𝒵(s), off ℝ, wherever W(s) ≠ 0. 

 ## 4. Finitely many low zeros to the right of Re s = 1; a zero-free line 

### `finite_lowZeros_right`

 the compact box [9/8, 5/4] × [−t₀, t₀] carries finitely many zeros of W. 

### `exists_zeroFree_line`

 **choice of the line**: some c ∈ [9/8, 5/4] such that W has no zero of height < t₀ on Re s = c. 

### `hardyW_ne_zero_reflect_line`

 … and then also none on Re s = 1 − c (off ℝ by W(1−s) = 0 ↔ W(s) = 0; at the real point via
the reflection identity extended to the real point by continuity). 
