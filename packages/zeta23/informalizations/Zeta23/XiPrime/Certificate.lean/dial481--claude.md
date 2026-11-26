---
{
  "module": "Zeta23/XiPrime/Certificate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Certificate.lean — **the ξ′ window certificates**: discharges the interface Props  CertFlat
and  CertQuartic  of Zeta23/XiPrime/Statement.lean §4, and re-exports the sharp constants.

[XF′ Thm 8.2 "Certified constants"]:
  flat window      1/c = κ₉ + (tail ≤ ε₉) ≤ 1.1416163  ⟹  simple∧on-line ≥ 0.858383,  distinct ≥ 0.929191;
  quartic window   1/c = κ₉ + (tail ≤ ε₉) ≤ 1.1313598  ⟹  simple∧on-line ≥ 0.868640,  distinct ≥ 0.934320.
Route:
  Certificate/D1.lean    D1trunc 9 ≤ D₁ ≤ D1trunc 9 + ε₉ on [0,1], ε₉ = 1024/2990212875 (tail on the side that
                         makes 1/c LARGER, so the bound is honest);
  Certificate/Poly.lean  exact rational ∫v, ∫v², (v⋆v), 2∫₀¹ D1trunc 9·(v⋆v) for v = vFlat, vQuartic;
  Certificate/AtOne.lean κ₉ ≤ κ₁(1,v) ≤ κ₉ + ε₉ and the sharp decimals at λ = 1 (cert_*_one);
  Window.lean            λ ↦ κ₁(λ,v) continuous on (0,1]  ⟹  the strict inequalities persist at some λ < 1.
-/
```

### `cert_of_strict_at_one`

 generic: two strict inequalities about κ₁(1,v) move to some λ ∈ [1/2,1) by continuity. 

### `certFlat`

 **CertFlat** (Statement.lean §4): ∃ λ ∈ [1/2,1), 0.85838 < 2 − κ₁(λ, flat) ∧ 0.92919 < 3/2 − κ₁(λ, flat)/2. 

### `certQuartic`

 **CertQuartic** (Statement.lean §4): ∃ λ ∈ [1/2,1), 0.86864 < 2 − κ₁(λ, quartic) ∧ 0.93432 < 3/2 − κ₁/2. 

### `certFlat_sharp`

 the sharp seven-digit versions, also at some λ < 1. 
