---
{
  "module": "Zeta23/ThmD/ZeroSideD.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/ZeroSideD.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/ZeroSideD.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/ZeroSideD.lean

THE ZERO SIDE FOR THE MONTGOMERY–TAYLOR WINDOW.  The fixed-T zero-side producers
('ZeroSide.blockInputsAt', 'Tail.TailHyp.tailInputs', 'ZeroConfig.Gz_eq_Gp') are generic in the
parameter set, so they apply verbatim to the window-realizing family 'P.atD T' of
Zeta23/ThmD/ParamsD.lean (whose window AT HEIGHT T is φ_D, and whose L, X, d, τ_k are P's by rfl).
The analytic side conditions they ask for (φ̂ real/conj-symmetric, lem:poisson, [eq:hfbound],
φ ∈ C_c^2[−L/2, L/2], 1/2 ≤ a ≤ 1) are supplied for φ_D by Zeta23/ThmD/WindowCore.lean's generic
'AdmWindow' facts via 'ThmD.admWindow_params' (BridgeD.lean).  Exports, all eventually in T:

  * 'eventually_blockInputsD'  — prop:block + [eq:Ncount] for 'P.atD T';
  * 'eventually_tailPackageD'  — prop:tail with θ₀(T) ≤ C·l·T^{λ/2−1};
  * 'eventually_GzGpD'         — the H-EF bridge 'Z.Gz (P.atD T) T = (P.atD T).Gp T';
  * 'eventually_aD_range'      — 1/2 ≤ a_D ≤ 1.
-/
```

 ### Name bridges: the 'Params' Fourier data of 'P.atD T' are the 'AdmWindow' data of φ_D 

 ### Eventual side conditions in T 

 ### 1/2 ≤ a_D ≤ 1 

 ### lem:poisson for φ_D and prop:block 

 ### The H-EF bridge for φ_D 

 ### prop:tail for φ_D 

### `C1D`

 C₁(T) := ‖φ_D''‖₁ (the [eq:hfbound] constant for the window of height T). 

### `hdecayD`

 [eq:hfbound] for φ_D in the shape 'TailHyp.hdecay' asks. 
