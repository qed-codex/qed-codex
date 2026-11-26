---
{
  "module": "Zeta23/XiPrime/Window/Quartic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window/Quartic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window/Quartic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Window/Quartic.lean — the quartic-window ratio limit, modulo the three window-moment estimates
(Zeta23/XiPrime/QuarticWindow/Moments.lean).

Shapes: for φ_V := P.phiV vQuartic T (Defs), with av/bv/gv the AdmWindow data
(Zeta23/ThmD/WindowCore.lean),
  aV_quartic_close : ∀ᶠ T, |av φ_V L − 2777/3000|     ≤ C·w/L,
  bV_quartic_close : ∀ᶠ T, |bv φ_V L − 518783/600000|  ≤ C·w/L,
  gV_quartic_close : ∀ᶠ T, ∀ y ∈ [0,L], |gv φ_V y − L·(v⋆v)(y/L)| ≤ C·w,   + gv φ_V continuous eventually.
This file turns ANY data satisfying those shapes into  cRatio(λ₁(T); a_T, b_T, J_T) → c_λ(vQuartic; D)
(tendsto_cRatio_quartic_of), and instantiates it with the estimates of QuarticWindow/Moments.lean:
tendsto_cRatio_quartic / tendsto_cRatio_quartic_D1, in the (P.atV vQuartic T).a/.b/.g spelling that
coeffMoments_atV consumes.
-/
```

### `tendsto_cRatio_quartic_of`

 **quartic-window ratio limit from the window-moment estimates.** 

### `cWin_vQuartic_pos`

 positivity of the limit constant (Endgame/CoeffMoments' hc0) for any D ≥ 0 on [0,1]. 

 ## instantiation with the window-moment estimates (see Zeta23/XiPrime/QuarticWindow/{Moments,Params}.lean) 

### `tendsto_cRatio_quartic`

 **The quartic-window ratio limit** (the `hc` hypothesis of `coeffMoments_atV`, with `JD` unfolded):
cRatio(λ₁(T); a_T, b_T, J_T) → c_λ(vQuartic; D) for the data of P.atV vQuartic, any continuous D ≥ 0 on [0,1]. 

### `tendsto_cRatio_quartic_D1`

 the D₁ instance, with the positivity the endgame wants. 
