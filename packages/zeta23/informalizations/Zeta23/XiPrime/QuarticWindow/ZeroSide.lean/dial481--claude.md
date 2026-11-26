---
{
  "module": "Zeta23/XiPrime/QuarticWindow/ZeroSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/ZeroSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/QuarticWindow/ZeroSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/QuarticWindow/ZeroSide.lean — the zero side for a MODULATED window P.atV v, and the quartic instance.

§1 is GENERIC in the profile v: given an admissibility witness T ↦ AdmWindow (P.phiV v T) (P.L T) P.w cW and the lower
bound 1/2 ≤ a_V(T) (both for 8w ≤ L_T), it proves lem:poisson, prop:block, the H-EF bridge, prop:tail (from the local zero
count only) and the bundle
  windowZeroSide_atV_of : RiemannVonMangoldt Z → P.Valid → XiPrime.WindowZeroSide Z P (P.atV v)
(the general-profile family and the flat window can instantiate it as well).
§2 is the quartic instance: 1/2 ≤ a_Q ≤ 1 at 8w ≤ L (a_Q ≥ (27/40)(1 − 2w/L) ≥ 81/160) and windowZeroSide_atV.
-/
```

 ## §1. Generic profile 

 ### lem:poisson and prop:block 

 ### the H-EF bridge 

 ### prop:tail 

### `C1Vv_nonneg`

 C₁(T) := ‖φ_V″‖₁. 

 ### The generic bundle 

### `windowZeroSide_atV_of`

 **the zero side of a modulated window**, from an admissibility witness and a_V ≥ 1/2. 

 ## §2. The quartic instance 

 ### 1/2 ≤ a_V ≤ 1 

### `phiV_quartic_sq_ge`

 φ_Q² ≥ (27/40)·φ² pointwise (on the core v ≥ 27/40; off it both vanish). 

 ### the quartic exports (instances of §1) 

### `windowZeroSide_atV`

 **The quartic window's zero side.** 
