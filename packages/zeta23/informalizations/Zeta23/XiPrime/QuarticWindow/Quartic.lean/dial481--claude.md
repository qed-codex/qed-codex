---
{
  "module": "Zeta23/XiPrime/QuarticWindow/Quartic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Quartic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/Quartic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/QuarticWindow/Quartic.lean — the quartic profile gives a modulated-taper factor; hence
P.phiV vQuartic T is an admissible window.

f_Q(u) := √(max 0 (vQuartic(u/L))) (so that P.phiV vQuartic T = phiM f_Q φ by rfl) satisfies `ModFactor f_Q L (3/2) 12`:
on the core |u| ≤ L/2 (s = u/L ∈ [−1/2,1/2]) one has 27/40 ≤ vQuartic s ≤ 1 (Zeta23/XiPrime/Certificate/Poly.lean), so
f_Q ≥ 4/5 and, with h(u) := vQuartic(u/L) = f_Q², |h′| ≤ (58/25)/L, |h″| ≤ (64/5)/L²:  f_Q′ = h′/(2f_Q),
f_Q″ = (h″ − 2f_Q′²)/(2f_Q) (differentiate f_Q·f_Q = h twice) give |f_Q′| ≤ (29/20)/L ≤ (3/2)/L and
|f_Q″| ≤ (5/8)(64/5 + 2·(3/2)²)/L² < 12/L².  Smoothness: vQuartic > 0 on |s| < 3/5, so f_Q = √∘vQuartic∘(·/L) is C^∞
on |u| < (3/5)L ⊇ [−L/2, L/2] + margin L/10.
-/
```

### `fQ`

 the quartic modulating factor in the u-variable. 

### `hQ`

 h := vQuartic(u/L), in expanded form. 

### `vQuartic_pos_of_abs_le`

 vQuartic is positive on |s| ≤ 3/5 (indeed ≥ 1 − (7/25)(9/25) − (102/25)(81/625) > 9/25). 

### `vQuartic_antitoneOn`

 vQuartic is nonincreasing in |s| on [0, ∞). 

### `core_mem`

 on the core: u/L ∈ [−1/2, 1/2]. 

### `fQ_core_ge`

 on the core, f_Q = √h (no max) and f_Q ≥ 4/5. 

### `hQ_pos_of_mem`

 the smooth region U := (−3L/5, 3L/5): there h > 0 and f_Q = √h. 

### `fQ_mul_self_of_mem`

 f_Q · f_Q = h on U. 

 ### derivatives of h 

 ### derivatives of f_Q on the core, through f_Q · f_Q = h 

 ### the ModFactor instance and the admissible window 

### `cQ`

 the window constant of the quartic window. 

### `phiV_quartic_eq`

 P.phiV vQuartic T is the modulated taper with factor f_Q (rfl). 

### `admWindow_phiV_quartic`

 **The quartic window is admissible.** 
