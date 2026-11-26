---
{
  "module": "Zeta23/XiPrime/Hardy/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/Basic.lean — analytic facts about χ, L₂ and W := ζ′ − ½(χ′/χ)ζ OFF THE REAL AXIS
(W zero side; [XF′ §9.0–9.1 (Z2)]).

Everything here is at points s with Im s ≠ 0, where Γℝ(s), Γℝ(1−s) are analytic and nonzero, ζ, ζ′ are analytic
(s ≠ 1), hence χ = Γℝ(1−s)/Γℝ(s) is an analytic unit, L₂ = −½ χ′/χ = ½[(Γℝ′/Γℝ)(s) + (Γℝ′/Γℝ)(1−s)] is analytic,
and W = ζ′ + L₂ζ is analytic.  Exports: ζ(s) = χ(s)ζ(1−s) (zeta_eq_chiFE_mul); L₂(1−s) = L₂(s), L₂(s̄) = conj L₂(s);
W(s̄) = conj W(s); the functional equation **W(s) = −χ(s)·W(1−s)**; hence IsWZero (reflect ρ) ↔ IsWZero ρ and
analyticOrderAt hardyW (reflect ρ) = analyticOrderAt hardyW ρ.
-/
```

 ### §1. Γℝ off the real axis 

### `differentiableAt_Gammaℝ_of_im_ne_zero`

 Γℝ is complex-differentiable at every non-real point. 

 ### §2. χ and L₂ 

### `logDeriv_chiFE`

 logDeriv χ = −(Γℝ′/Γℝ)(1−s) − (Γℝ′/Γℝ)(s). 

### `L2_eq`

 **L₂ = ½[(Γℝ′/Γℝ)(s) + (Γℝ′/Γℝ)(1−s)]** off the real axis. 

### `deriv_chiFE`

 χ′ = −2·L₂·χ. 

 ### §3. ζ(s) = χ(s)·ζ(1−s) off the real axis 

 ### §4. W off the real axis: analyticity, Schwarz reflection, the functional equation 

### `hardyW_analyticAt`

 W is analytic at every non-real point. 

### `deriv_conj_of_symm`

 generic: a derivative inherits Schwarz reflection symmetry (local version). 

### `hardyW_conj`

 **W(s̄) = conj W(s)** off the real axis. 

### `deriv_riemannZeta_eq`

 ζ′(s) = χ′(s)ζ(1−s) − χ(s)ζ′(1−s) off the real axis. 

### `hardyW_eq_neg_chiFE_mul`

 **The functional equation W(s) = −χ(s)·W(1−s)** off the real axis  [XF′ (Z2)]. 

### `isWZero_reflect_iff`

 the non-real zeros of W are invariant under ρ ↦ 1 − ρ̄. 

 ### §5. The analytic order of W under the two symmetries 

### `wMult_reflect`

 **m_{1−ρ̄} = m_ρ** for non-real ρ. 
