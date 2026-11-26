---
{
  "module": "proof/rates/GeneralPieces/Series/Constant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Constant.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Constant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "The constant"

The number G of the expansion does not depend on the two partitions σ, σ' of E at which the
coefficient is read, so it can be found at E = 0, that is σ = σ' = 0, the empty partition (the
monomial 1). There ⟨𝒩⟩ = 1, so f₊ = G·ε₊^H (`fP_vac`), in which ω₂^0 has the
coefficient G·ω₁^{−H}. In f₊ = Σ_r ⟨a[r]∘b[−r]⟩·ω₁^{r−h'}·ω₂^{−r−h} it has the coefficient
a[−h](b[h]·1)·ω₁^{−H}, and b[h]·1 = b (`op_vac`). Hence G = a[−h]b (`Expansion.const`), which in the
language of matrices is the entry `op a (−h) 0 b`. 

### `op_cons_vac`

 On the monomial 1 only multiplications act: (t_n·b)[r]·1 = Σ_l C(l−1, n−1)·t_l·(b[r−l]·1). 

### `bet_eq_zero`

 C(l−1, n−1) = 0 for l < n. 

### `bet_self`

 C(n−1, n−1) = 1. 

### `op_vac_eq_zero`

 b[r]·1 = 0 for r < h: every part ν_i of b needs an l_i ≥ ν_i. 

### `op_vac`

 b[h]·1 = b: the sum of the l_i is h, which forces l_i = ν_i. 

### `mul2_vac`

 a[−h](b[h]·1) = a[−h]b. 

### `terms_vac`

 For a list of terms c = (q, N, n) with N ≤ H, n = 0 when N < H and n = 1 when N = H, the sum of
q·e^N·φ(n) is (the sum of the q of the terms with N = H)·e^H. 

### `Expansion.fP_vac`

 For E = 0: f₊ = G·ε₊^H. 

### `cfP_epsP_pow`

 In ε₊^N the coefficient of ω₁^{−N}·ω₂^0 is 1. 

### `Expansion.const`

 The constant: G = a[−h]b. 
