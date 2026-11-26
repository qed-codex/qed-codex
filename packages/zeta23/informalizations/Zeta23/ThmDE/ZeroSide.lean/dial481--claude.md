---
{
  "module": "Zeta23/ThmDE/ZeroSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/ZeroSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/ZeroSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/ZeroSide.lean — the zero side for L(s,χ) with the
Montgomery–Taylor window, i.e. for the window-realizing family 'P.atD T' (Zeta23/ThmD/ParamsD.lean).

  * 'eventually_tailPackageD_of_localCount' — prop:tail for 'P.atD T' from an ABSTRACT two-sided
    local count N(t, t+1) ≤ A₀ log(|t|+3) (the χ local count, Zeta23.ThmE.*), rather than from
    'PaperInputs.RvM' as in Zeta23/ThmD/ZeroSideD.lean 'eventually_tailPackageD' (same proof);
  * 'eventually_GzGpDChi' — the H-EF(χ) bridge 'Z.Gz (P.atD T) T = GpChi (P.atD T) κ q c T'
    (ZeroConfig.Gz_eq_GpChi, Zeta23/ThmE/GzGpChi.lean, is generic in the parameter set; the C_c^2
    side conditions for φ_D come from the AdmWindow facts exactly as in ThmD.GzGpD_of);
prop:block needs nothing new: ThmD.eventually_blockInputsD is already generic in Z; the
identification of the χ-traces of 'P.atD T' with the abstract-layer χ-traces of the D-data lives
in Zeta23/ThmDE/Concrete.lean.
-/
```

 ### prop:tail for φ_D from an abstract local count 

 ### The H-EF(χ) bridge for φ_D 
