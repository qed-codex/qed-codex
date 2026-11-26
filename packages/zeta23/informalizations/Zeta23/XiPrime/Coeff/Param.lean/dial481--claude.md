---
{
  "module": "Zeta23/XiPrime/Coeff/Param.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Param.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Coeff/Param.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Coeff/Param.lean — the complex parameter Λ⋆ = l/2 + it, |t| ≤ 1, versus l/2
([XF′ Remark 4.3] in the form the H3 assembly consumes).

For Λs : ℂ with Λs.re = l/2, |Λs.im| ≤ 1 and 2 ≤ l:
  l/2 ≤ ‖Λs‖,   l²/4 ≤ ‖Λs‖² ≤ l²/4 + 1,
  |Re(Λs⁻¹) − 2/l| ≤ 8/l³,   |‖Λs‖⁻² − 4/l²| ≤ 16/l⁴,   |‖Λs‖^{−2k} − (4/l²)^k| ≤ k·(4/l²)^{k+1}.
-/
```

 Every lemma takes the same three hypotheses (hl) (hre) (him), used or not, so the consumer's call
shape is uniform. 

### `inv_re_param`

 |Re(Λs⁻¹) − 2/l| ≤ 8/l³  (indeed 0 ≤ 2/l − Re(Λs⁻¹) = 2t²/(l(l²/4+t²)) ≤ 8t²/l³). 

### `inv_normSq_param`

 |‖Λs‖⁻² − 4/l²| ≤ 16/l⁴  (indeed 0 ≤ 4/l² − ‖Λs‖⁻² = 4t²/(l²A) ≤ 16t²/l⁴). 

### `inv_normSq_param_le`

 0 ≤ 4/l² − ‖Λs‖⁻²  (the sign: ‖Λs‖² ≥ l²/4). 

### `mul_pow_sub_pow_le`

 elementary: for 0 ≤ x ≤ y,  y·(y^k − x^k) ≤ k·(y − x)·y^k. 

### `inv_normSq_pow_param`

 |‖Λs‖^{−2k} − (4/l²)^k| ≤ k·(4/l²)^{k+1}. 
