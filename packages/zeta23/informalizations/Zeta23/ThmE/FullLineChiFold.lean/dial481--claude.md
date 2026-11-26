---
{
  "module": "Zeta23/ThmE/FullLineChiFold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiFold.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/FullLineChiFold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/FullLineChiFold.lean — auxiliary pieces for full_line_identity_chi
(Zeta23/ThmE/FullLineChi.lean), the χ-analogues of verticals_eq (FullLine.lean) and
zero_sum_limit (ZeroSumLimit.lean):
 • the two vertical sides of the rectangle [1−c,c]×[−R,R] for H·Λ_sym'/Λ_sym(·,χ) fold onto the
   line Re s = c: the left side is the χ⁻¹-term, by (Λ_sym'/Λ_sym)(1−s̄,χ) = −conj(Λ_sym'/Λ_sym)(s,χ)
   (FoldChi.logDeriv_completedLSym_one_sub_conj) and conj(Λ_sym'/Λ_sym)(s,χ) = (Λ_sym'/Λ_sym)(s̄,χ⁻¹)
   (FoldChi.logDeriv_completedLSym_inv_conj), then y ↦ −t;
 • the finite zero sums Σ_{|γ|<R_j} m_ρ H(ρ) → the absolutely convergent tsum over LZeros
   (EF_zero_sum_summable_chi).
-/
```

### `FlineChi`

 the folded full-line integrand for χ: H(c+it)·(Λ_sym'/Λ_sym)(c+it,χ) + H(1−c−it)·(Λ_sym'/Λ_sym)(c+it,χ⁻¹). 

 ## (V) the vertical sides 

### `continuous_logDeriv_completedLSym_line`

 Λ_sym'/Λ_sym(·,χ) is continuous along Re s = c > 1 (Λ_sym entire, zero-free there). 

### `verticals_eq_chi`

 **(V) verticals fold for χ.** 

 ## (Z) the zero-sum limit 

### `zero_sum_limit_chi`

 **(Z) zero-sum limit for χ.** 
