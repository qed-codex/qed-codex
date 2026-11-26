---
{
  "module": "Zeta23/XiPrime/FamilyFlat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyFlat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/FamilyFlat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/FamilyFlat.lean — the window-regularity class FamilyHyps (Zeta23/XiPrime/ExplicitFormula.lean §7)
holds for the FLAT taper family T ↦ paramsOf ϱ λ at a Gevrey profile ϱ.

FamilyHyps asks, from some T₀ on: φ_T := (Pf T).phi T is C³, tsupport φ_T ⊆ [−L/2, L/2], even, |φ_T| ≤ 1, and
‖φ_T^{(j)}‖_{L¹} ≤ C for j = 1,2,3 with C INDEPENDENT of T.  For the ramp taper φ(u) = ϱ((L/2−|u|)/w) the
derivatives live on the two ramps of width w and scale like w^{−j}, so the L¹ norms are O_w(1) uniformly in L:
Zeta23/Taper/GevreyRamps.lean proves exactly  ∫|φ^{(k)}| ≤ 2B·w·(A/w)^k·k^{sk}  for a GevreyProfile
(s, A, B) ϱ, and Zeta23/Taper/Gevrey.lean supplies the instance rhoTwo (gevreyProfile_rhoTwo).  That is all the
unconditional headline needs (Final.lean instantiates at ϱ := rhoTwo).  The generic C³-TaperProfile version
is not treated here. -/
```

### `hasCompactSupport_iteratedDeriv`

 derivatives of every order of a compactly supported function are compactly supported. 

### `familyHyps_flat_gevrey`

 **FamilyHyps for the flat family at a Gevrey taper profile** (λ ∈ (0,1), w = 1). 
