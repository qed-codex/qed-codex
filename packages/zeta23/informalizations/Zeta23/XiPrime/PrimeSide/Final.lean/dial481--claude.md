---
{
  "module": "Zeta23/XiPrime/PrimeSide/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/PrimeSide/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization.

Zeta23/XiPrime/PrimeSide/Final.lean — ξ′ prime side: discharge of the named input
PPInput by Zeta23/XiPrime/PrimeSide/PP.lean (prop_PP_c', KPP), and the input-free
forms of the producer theorems; also the flat-window wiring to XiPrime/Window.
-/
```

### `coeffMoments_flat_cWin`

 **CoeffMoments for the flat window, instantiated**: for every coefficient family with
(H1)–(H3), `CoeffMoments Z (fun _ => P) Fam (cWin Fam.D P.lam vFlat)⁻¹`. 

### `coeffMoments_flat_one_div`

 the same with the `1 / cWin` spelling (`kappaXi`-shape). 

### `ppInput_of_PP`

 **[prop:PP] for P_c holds** (Zeta23/XiPrime/PrimeSide/PP.lean). 

### `coeffMoments_flat_final`

 **CoeffMoments, flat window — no prime-side input left.**  Visible hypotheses: P.Valid, λ < 1,
the coefficient family's (H1)–(H3), H-Γ, H-MV, H-RvM for Z. 

### `coeffMoments_flat_final'`

 the same with the `1 / cWin` spelling. 

### `momentsW_of_family_final`

 **MomentsW for any admissible family, input-free in PP** (general pole weight; for Assembly's
profile and Z′ instances). 

### `coeffMoments_quartic_final`

 **CoeffMoments, QUARTIC window v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴ — no prime-side input left.**
Window admissibility: admFamily_atV_quartic (Zeta23.XiPrime.QuarticWindow.Family); window
limit: tendsto_cRatio_quartic + cWin_vQuartic_pos (Zeta23.XiPrime.Window.Quartic). 

### `coeffMoments_quartic_final'`

 the same with the `1 / cWin` spelling. 

### `frobSq_Ppart_le_final`

 **PPUpper engine, input-free.** 
