---
{
  "module": "Zeta23/XiPrime/Coeff/ReexpansionGen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/ReexpansionGen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/ReexpansionGen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/ReexpansionGen.lean — the δ-re-expansion of C(N; L + δ) about a GENERAL base L = Lb(T) with
Re Lb(T) = l(T)/2, and the (H1)–(H3)-type bounds for its coefficients  [XF′ §6; §9.3(ii)]
(the generic API; Coeff/ReexpansionW.lean and Coeff/Reexpansion.lean are its instances).

  eGen Lb T r N := Σ_{j<Ω N} (−1)^r C(r+j, j) Lb(T)^{−(j+1+r)} [(Λ·log)∗Λ^{∗j}](N)
  eGen_expand : C(N; Lb T + δ) − C(N; Lb T) = Σ_{r≥1} eGen Lb T r N · δ^r     (l(T) ≥ 2, 0 ≤ δ ≤ 1/2)
  eGen_H1/H2/H3 : the Reexpansion-shaped bounds with ρ₀ = 4, A = CF, threshold T0re (l ≥ 128eK + 2).
Instances: Coeff/Reexpansion.lean (ξ′: Lb = LT = l/2 + iπ/4), Coeff/ReexpansionW.lean (Z′: Lb = l/2 real).
Every step uses only Re Lb = l/2 (⇒ ‖Lb‖ ≥ l/2, Lb ≠ 0, Lb + δ ≠ 0).
-/
```

 ### shared elementary helpers 

### `T0re`

 the height threshold: l(T) ≥ 128eK + 2. 

 ### elementary facts about a base with Re Lb(T) = l(T)/2 

### `eGen`

 e_r(N) := Σ_{j<Ω N} (−1)^r · C(r+j, j) · L^{−(j+1+r)} · [(Λ·log)∗Λ^{∗j}](N), about the base L = Lb T. 

 ### e_r(1) = 0 

 ### the expansion identity 

### `eGen_block_eq`

 the n-th Taylor block: g_n := Σ_j L^{−(j+1)} conv_j · C(n+j,j)(−δ/L)ⁿ = e_n(N)·δⁿ. 

### `eGen_expand`

 **the δ-expansion**: for l(T) ≥ 2 and 0 ≤ δ ≤ 1/2,
C(N; L_T + δ) − C(N; L_T) = Σ_{r≥1} e_r(N) δ^r. 

 ### the pointwise majorant ‖e_r(N)‖ ≤ (2/‖L‖)^r · log N · F_{2/‖L‖}(N) 

 ### the core sum bound 

### `sum_norm_eGen_sq_div_le`

 **core**: Σ_{N≤x} ‖e_r(N)‖²/N ≤ CF·(4/l)^{2r}·log²x for 2 ≤ x ≤ e^{l}, T ≥ T0re. 

 ### (H3), (H2), (H1) 
