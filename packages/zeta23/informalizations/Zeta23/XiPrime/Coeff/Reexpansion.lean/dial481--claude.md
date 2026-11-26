---
{
  "module": "Zeta23/XiPrime/Coeff/Reexpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Reexpansion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Reexpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Reexpansion.lean — the ξ′ instance (base L_T = l/2 + iπ/4) of the generic δ-re-expansion
Coeff/ReexpansionGen.lean; discharges `Reexpansion xiCoeffFamily` of Zeta23/XiPrime/Transfer/Inputs.lean
(consumed by Final.lean via xiReexpansion).  [XF′ §6, Lemma 6.1 input]

  eXi := eGen LT;   C(N; L_T+δ) − C(N; L_T) = Σ_{r≥1} eXi T r N · δ^r;   (H1)–(H3)_r with ρ₀ = 4, A = CF, T₀ = T0re.
-/
```

### `eXi`

 e_r(N) for the ξ′ family: the generic coefficients about the base L_T. 

### `xiReexpansion_eXi`

 **Reexpansion for the ξ′ coefficient family** with the explicit e = eXi, ρ₀ = 4, A = CF, T₀ = T0re. 

### `xiReexpansion`

 **Reexpansion for the ξ′ coefficient family**, in the ∃-e form. 
