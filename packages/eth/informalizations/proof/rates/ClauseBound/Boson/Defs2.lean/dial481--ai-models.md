---
{
  "module": "proof/rates/ClauseBound/Boson/Defs2.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Defs2.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Defs2.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The dual families and the operators Q_s: definitions

A combination of monomials with integer coefficients is a list of pairs (coefficient, list of
parts). Definitions only. 

### `FA`

 A combination of monomials. 

### `yl`

 (−1)^{n−1}·y_n, where y_n = Σ_{j=1}^{n} C(n,j)·t_j. 

### `aFam`

 a^μ = ∏_i (−1)^{μ_i−1}·y_{μ_i}, multiplied out. 

### `zz`

 z_ν = ∏_k k^{m_k}·m_k!, where m_k is the number of parts equal to k. 

### `Qk`

 Q_s(a,b) = Σ_{i=0}^{2h} (−1)^i·a^{⟨i⟩}[s−h+i]∘b[h−s−i], h the weight of b. 

### `Qk'`

 The same with the two factors of every product exchanged. 

### `FA.Ok`

 All monomials of the combination have positive parts and weight at most h. 

### `lst`

 The parts of a partition, as a list. 
