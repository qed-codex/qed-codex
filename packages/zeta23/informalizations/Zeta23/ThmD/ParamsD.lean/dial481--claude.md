---
{
  "module": "Zeta23/ThmD/ParamsD.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/ParamsD.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/ParamsD.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/ParamsD.lean

THE WINDOW-REALIZING PARAMETER FAMILY.  The zero side of the argument (Zeta23/ZeroSide.lean,
Zeta23/Tail.lean, the H-EF bridge Zeta23/Hypotheses/GzGp.lean) is written over 'P : Params', whose
window is hard-wired as the ramp taper 'P.phi T u = P.ϱ ((L/2 − |u|)/w)'.  The Montgomery–Taylor
window 'φ_D(u) = √cos(√2 λ u/L) · (ramp taper)' (the paper §7.1) is NOT of that form for any fixed
profile (its shape depends on L).  But every zero-side statement the §6 endgame consumes is a
statement AT ONE HEIGHT T ('BlockInputs Z P T', 'TailInputs Z P T θ₀', 'Z.Gz P T = P.Gp T'), and
their fixed-T producers ('ZeroSide.blockInputsAt', 'Tail.TailHyp.tailInputs',
'ZeroConfig.Gz_eq_Gp') are generic in P.  So for each height T we use the parameter set

    P.atD T := ⟨x ↦ φ_D^{(T)}(L/2 − w·x), λ, w⟩,

whose window AT HEIGHT T is exactly φ_D^{(T)} ('Params.atD_phi'), and whose λ, w — hence L, X,
λ₁, d, τ_k, h, 𝓔_T, toSetting — are those of P DEFINITIONALLY (all 'rfl' below).  The zero-side
Gram matrix 'Z.Gz (P.atD T) T' is then literally the paper's G for the Montgomery–Taylor window,
and no file outside Zeta23/ThmD/ is touched.  (A profile 'ϱ' of a 'Params' is only ever evaluated
through 'Params.phi', so the values of the realizing profile at x > L/(2w) are irrelevant.)
-/
```

### `atD`

 the parameter set realizing the Montgomery–Taylor window of height 'T' (see file header). 

### `atD_phi`

 **the window of 'P.atD T' at height 'T' is the Montgomery–Taylor window φ_D.** 

### `localFun_eq_admWindow`

 every 'Params'' abstract local data is the 'AdmWindow.localFun' of its window (rfl). 

### `atD_localFun`

 hence the abstract local data of 'P.atD T' at height T are the D-data 'P.localFunD T'. 

### `atD_trGtilde`

 the prime-side traces of 'P.atD T' at height T are the abstract-layer traces of the D-data. 
