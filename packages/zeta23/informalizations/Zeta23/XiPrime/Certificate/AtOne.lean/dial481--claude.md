---
{
  "module": "Zeta23/XiPrime/Certificate/AtOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/AtOne.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/AtOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Certificate/AtOne.lean — the certified window constants at λ = 1.

[XF′ Thm 8.2 "Certified constants"]:  κ₁(1, v) = 1/c₁^{(1)}(v) = (∫v² + 𝒥_{D₁}(1;v))/(∫v)²  with the
FULL series D₁ (Defs.kappaXi) is sandwiched using  D1trunc 9 ≤ D₁ ≤ D1trunc 9 + ε₉ on [0,1]
(Certificate/D1.lean) and the exact rational values of Certificate/Poly.lean:
  flat     κ₉ = 100905635384/88388425125,                            κ₉ ≤ κ₁(1,vFlat)    ≤ κ₉ + ε₉,
  quartic  κ₉ = 277244140547469154168336/245053976636191319722125,    κ₉ ≤ κ₁(1,vQuartic) ≤ κ₉ + ε₉,
whence the SHARP certified decimals (the interface Props CertFlat/CertQuartic of
Statement.lean carry five digits and are discharged in Certificate.lean via continuity in λ):
  2 − κ₁(1,vFlat) ≥ 0.85838371,   3/2 − κ₁(1,vFlat)/2 ≥ 0.92919185,
  2 − κ₁(1,vQuartic) ≥ 0.86864017, 3/2 − κ₁(1,vQuartic)/2 ≥ 0.93432008   (eight digits; all margins ≥ 6·10⁻⁹
  in exact rational arithmetic).
The tail ε₉ enters with the sign that makes 1/c LARGER (the correct-side requirement for a lower bound).
-/
```

 ### generic λ = 1 algebra 

### `jWin_one_le_of_le`

 comparison of 𝒥 at λ = 1 under a pointwise bound with constant slack on [0,1]. 

 ### 2∫₀¹(v⋆v) = (∫v)² for the two windows (Fubini instances, by direct evaluation) 

 ### the sandwich for the two windows 

### `kap9Flat`

 the flat κ₉. 

### `kap9Quartic`

 the quartic κ₉. 

### `kappaXi_one_vFlat_mem`

 **flat window:** κ₉ ≤ κ₁(1, vFlat) ≤ κ₉ + ε₉. 

### `kappaXi_one_vQuartic_mem`

 **quartic window:** κ₉ ≤ κ₁(1, vQuartic) ≤ κ₉ + ε₉. 

 ### the sharp certified decimals at λ = 1 

### `cert_flat_one`

 **2 − κ₁(1, flat) ≥ 0.85838371**  [XF′: "≥ 0.858383"]. 

### `cert_flat_dist_one`

 **3/2 − κ₁(1, flat)/2 ≥ 0.92919185**  [XF′: "≥ 0.929191"]. 

### `cert_quartic_one`

 **2 − κ₁(1, quartic) ≥ 0.86864017**  [XF′: "≥ 0.868640"]. 

### `cert_quartic_dist_one`

 **3/2 − κ₁(1, quartic)/2 ≥ 0.93432008**  [XF′: "≥ 0.934320"]. 

### `cert_flat_one_strict`

 strict forms at the FIVE-decimal interface constants (used with continuity in λ to produce
CertFlat / CertQuartic of Statement.lean). 
