---
{
  "module": "Zeta23/XiPrime/Coeff/Tail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Tail.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Tail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Tail.lean — the K-tail of the dyadic majorant is uniformly small (used in
the H3 assembly in Coeff/DiagLaw.lean).

Per-term input (Coeff/Upper.lean, Fmaj_term_le): under x·u ≤ 4 and 32eK·x ≤ 1,
  2^{i+1} x^{2(i+1)} u^{i+1} Σ_{N≤e^u}Λ^{∗(i+1)}(N)/N ≤ 64^{i+1}/(i+1)! + 2^{−(i+1)} =: tailMaj i,
a summable sequence independent of (x,u).  Hence for every ε > 0 there is K with
  Σ_{K ≤ i < X} (term i) ≤ Σ_{i ≥ K} tailMaj i ≤ ε   uniformly in x, u, X.     (Fmaj_tail_small)
-/
```

### `tailMaj`

 the (x,u)-free summable majorant of the dyadic terms. 

### `tailMajFrom`

 the truncated majorant 𝟙_{K ≤ i}·tailMaj i. 

### `tsum_tailMajFrom`

 Σ' i, 𝟙_{K≤i} tailMaj i = Σ' j, tailMaj (j + K). 

### `Fmaj_tail_small`

 **the K-tail of the dyadic majorant is uniformly small.** 
