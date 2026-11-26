---
{
  "module": "Zeta23/ThmD/AssemblyD.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/AssemblyD.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/AssemblyD.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/AssemblyD.lean — the parametric fixed-T core and the TracesBoundsD interface
(produced by Traces.lean/Concrete.lean, consumed by Endgame.lean).

§6 of the paper with the window-general ratio constant ([eq:ratio-general]):
  (tr G~)²/tr G~² = (λ₁ a²/(b + λ₁² J)) · N(T,2T) · (1 + O(E_T)),
replacing F(λ₁) (the flat-top case a=b→1, J→1/3).  The ONLY place Assembly.lean's fixed-T §6
endgame uses the flat top is the literal (1/λ₁ + λ₁/3) in N0star_lower_H's hfr hypothesis;
the abstract-constant copy below is proved by the same argument.
-/
```

### `cRatio`

 the window-general ratio constant of [eq:ratio-general]: c(λ₁; a, b, J) := λ₁a²/(b + λ₁²J).
Flat top (a = b = 1, J = 1/3): c = F(λ₁); Montgomery–Taylor window: c → cStar λ + O(w/L + 1/l). 

### `cRatio_flat`

 flat-top sanity: cRatio λ₁ 1 1 (1/3) = F(λ₁). 

 ### The fixed-T endgame with an abstract constant (parametric copy of
Assembly.lean's N0star_lower_H; same proof) 

### `N0star_lower_c`

 §6, Thm A-line, window-general: with cinv in the role of 1/λ₁ + λ₁/3 = 1/F(λ₁):
if 4trG^ − ‖G^‖² − 2N − 3N(I′∖I) − B(4+2‖G^‖+B) ≤ N₀*, |trG^ − N| ≤ R₁, ‖G^‖² ≤ cinv·N + R₂,
then (2 − cinv)N − [4R₁ + R₂ + 3NII + B(4 + 2√(cinv·N + R₂) + B)] ≤ N₀*. 

### `two_sub_inv_cStar`

 link to the Theorem-D constant: 2 − 1/cStar λ = HD λ by definition. 

 ### The D-interface for the traces (produced by Traces.lean, consumed by Endgame.lean)

Mirrors Zeta23.TracesBounds (PrimeSideTemp.lean) with the window moments (a, b, J) as data and the
ratio constant cRatio(λ₁; a, b, J) in place of F(λ₁).  tr1 is [eq:tr1] verbatim (prop:trace is
window-general); ratio/frhat carry the [eq:ratio-general] main terms. 

### `TracesBoundsD.tr1`

 [eq:tr1] first equality (window-general prop:trace): tr G~ = a L N + O(L√X). 

### `TracesBoundsD.ratio`

 [eq:ratio-general]: (tr G~)²/tr G~² = cRatio(λ₁; a, b, J) N (1 + O(E_T)). 

### `TracesBoundsD.frhat`

 hat-units form consumed by the Thm-A-line endgame: the positive part of
  tr G~²/(aL)² − (1/cRatio)·N is O(E_T · (1/cRatio) N).  (Recorded separately since the
  division by (aL)² and the inversion are where TracesD does real work.) 

 The ε-form wrappers live in Zeta23/ThmD/Endgame.lean (abstract) and Zeta23/ThmD/Final.lean (ζ). 
