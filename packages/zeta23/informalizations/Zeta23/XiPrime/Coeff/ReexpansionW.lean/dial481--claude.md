---
{
  "module": "Zeta23/XiPrime/Coeff/ReexpansionW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/ReexpansionW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/ReexpansionW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/ReexpansionW.lean — the δ-re-expansion of C(N; L + δ) about a GENERAL base L = Lb(T) with
Re Lb(T) = l(T)/2, and its instance at the REAL base ½l for the Z′ (Hardy W) coefficients  [XF′ §6 at §9.3(ii)]
(discharges ReexpansionW wCoeffFamily of Zeta23/XiPrime/Transfer/InputsW.lean).

This is Coeff/Reexpansion.lean (base L_T = l/2 + iπ/4) made base-generic: every step there uses only
Re L = l/2 (⇒ ‖L‖ ≥ l/2, L ≠ 0, L + δ ≠ 0), so the same e_r(N) := Σ_{j<Ω N}(−1)^r C(r+j,j) L^{-(j+1+r)}[(Λlog)∗Λ^{∗j}](N),
the same expansion C(N;L+δ) − C(N;L) = Σ_{r≥1} e_r δ^r (0 ≤ δ ≤ 1/2, l ≥ 2) and the same bounds (ρ₀ = 4, A = CF, T₀ = T0re)
hold verbatim.  The generic section lives in Coeff/ReexpansionGen.lean; this file is the Z′ instance.
-/
```

 ### the Z′ instance: base ½l (real) 

### `halfL`

 the real base of the Z′ coefficients: ½ l(T). 

### `eW`

 e_r(N) for the Z′ family. 

### `wReexpansion_eW`

 **ReexpansionW for the Z′ coefficient family** with e = eW, ρ₀ = 4, A = CF, T₀ = T0re. 

### `wReexpansion`

 **ReexpansionW for the Z′ coefficient family**, ∃-e form (the sentence InputsW.lean asks for). 
