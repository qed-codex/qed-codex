---
{
  "module": "Zeta23/WeilEF/XiLogDeriv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/XiLogDeriv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/WeilEF/XiLogDeriv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/WeilEF/XiLogDeriv.lean
The completed zeta function Λ = completedRiemannZeta: log-derivative decomposition, functional equation
for logDeriv, zeros in the strip = nontrivial zeros of ζ with equal analytic order.

Mathlib normalization (verified): for s ≠ 0, riemannZeta s = completedRiemannZeta s / Gammaℝ s
(riemannZeta_def_of_ne_zero) and Gammaℝ s ≠ 0 for 0 < Re s (Gammaℝ_ne_zero_of_re_pos); hence on the
open right half-plane Λ = Γℝ · ζ on the nose (completedZeta_eventuallyEq_mul) — no pole bookkeeping is
needed for the three statements below (Λ's poles at 0, 1 are excluded by hypothesis).
-/
```

### `differentiableAt_Gammaℝ`

 Γℝ(s) = π^{−s/2} Γ(s/2) is complex-differentiable at every s with Re s > 0. 

### `analyticAt_Gammaℝ`

 Γℝ is analytic at every point of the right half-plane. 

### `completedZeta_eventuallyEq_mul`

 On the right half-plane, Λ = Γℝ · ζ (as germs). 

### `analyticAt_riemannZeta`

 ζ is analytic at every s ≠ 1. 

### `logDeriv_completedZeta`

 On the right half-plane away from 1 and from the zeros of ζ:  Λ'/Λ = Γℝ'/Γℝ + ζ'/ζ. 

### `logDeriv_completedZeta_one_sub`

 Functional equation for the log-derivative: Λ'/Λ(1−s) = −Λ'/Λ(s)  (from Λ(1−s) = Λ(s)). 

### `completedZeta_zeros_strip`

 In the open critical strip the zeros of Λ are exactly the nontrivial zeros of ζ, with the same
analytic order (Γℝ is analytic and nonvanishing there). 
