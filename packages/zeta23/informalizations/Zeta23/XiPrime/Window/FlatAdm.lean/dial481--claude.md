---
{
  "module": "Zeta23/XiPrime/Window/FlatAdm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window/FlatAdm.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Window/FlatAdm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Window/FlatAdm.lean — the tree's own ramp taper P.phi is an admissible window
(Zeta23.AdmWindow, Zeta23/ThmD/WindowCore.lean) with c = c_ϱ.

WindowCore's header asserts this ("so is the flat window with c = cRho ϱ"); since the
coefficient-generalised prime side is stated over AdmWindow uniformly (one code path for the flat and the
quartic windows), we record it as a lemma.  Every field is a Taper/ fact: [eq:phinorms] ‖φ′‖₁ = ‖(φ²)′‖₁ = 2,
‖φ″‖₁ = 2‖ϱ″‖₁/w ≤ c_ϱ/w, ‖(φ²)″‖₁ ≤ c_ϱ/w (Zeta23/Taper/Norms.lean).
Also: 1/2 ≤ bv (indeed 3/4 ≤ b, Zeta23/Taper/Params.lean three_quarters_le_b); the rfl-bridge
AdmWindow.localFun (P.phi T) (P.L T) = P.localFun T is Zeta23/ThmD/ParamsD.lean's localFun_eq_admWindow.
-/
```

### `admWindow_taperPhi`

 the ramp taper φ = ϱ((L/2 − |u|)/w) is an AdmWindow with constant c_ϱ (generic parameters). 

### `admWindow_taper`

 **the flat taper of a valid parameter set is an admissible window** (eventually 8w ≤ L). 

### `half_le_bv_taper`

 1/2 ≤ bv for the taper (in fact 3/4 ≤ b). 

### `admFamily_taper`

 **The flat admissible family**, in the `AdmFamily` shape:
∃ T₀, ∀ T ≥ T₀, AdmWindow (P.phi T) (P.L T) P.w c_ϱ ∧ 1/2 ≤ bv. 
