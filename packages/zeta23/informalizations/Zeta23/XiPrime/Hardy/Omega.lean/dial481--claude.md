---
{
  "module": "Zeta23/XiPrime/Hardy/Omega.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Omega.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/Omega.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/Omega.lean — the completed object Ω := Γℝ·W.

W(s) = −χ(s)W(1−s) with χ = Γℝ(1−s)/Γℝ(s) says exactly that Ω(s) := Γℝ(s)·W(s) is ODD under s ↦ 1−s off the real
axis: Ω(1−s) = −Ω(s); also Ω(s̄) = conj Ω(s).  So Ω plays for W the role ξ′ plays for itself in
Zeta23/XiPrime/ZeroCount/Contour.lean: logDeriv Ω (1−s̄) = −conj logDeriv Ω (s) (the fold), Ω is analytic off ℝ with the
same zeros and orders as W there, and logDeriv Ω = Γℝ′/Γℝ + W′/W (the split; Γℝ′/Γℝ gives the main term).
-/
```

### `omegaW`

 Ω := Γℝ · W. 

### `analyticOrderAt_omegaW`

 Ω and W have the same order at non-real points. 

### `omegaW_one_sub`

 **Ω(1−s) = −Ω(s)** off the real axis. 

### `deriv_omegaW_one_sub`

 Ω′(1−s) = Ω′(s). 

### `logDeriv_omegaW_one_sub_conj`

 **the fold identity**: logDeriv Ω (1 − s̄) = −conj (logDeriv Ω s) off the real axis. 

### `logDeriv_omegaW_eq`

 **the split**: logDeriv Ω = Γℝ′/Γℝ + W′/W where W ≠ 0 (off the real axis). 
