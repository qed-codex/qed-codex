---
{
  "module": "Zeta23/ThmD/PsiC.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/PsiC.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/PsiC.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

### `psiC`

 `ψ_c(r) := min(L, 2/|r|, c/(w r²))` (value `L` at `r = 0`), i.e. `psiA c p` with
`(p.L, p.w) = (L, w)`. 

 #### Measurability / integrability of ψ 

### `psi_le_rpow_neg_two`

 For r > 0: ψ(r) ≤ (c_ϱ/w) · r^{−2} (rpow form). 

### `psiMaj`

 The integrable majorant of ψ: L on [−1,1] and (c_ϱ/w)|r|⁻² outside. 

 ### [eq:psiints].  We record upper bounds — every downstream citation of [eq:psiints] in §5 is
"≪ log L" or "≤ 8L".  (Paper: "a direct computation (split at |r| = 2/L and |r| = c_ϱ/2w; note
c_ϱ L/4w ≥ 1 by [eq:wrange]) gives Ψ₀ = 4 + 2 log(c_ϱ L/4w), ∫ψ²|r| = 8 + 8 log(c_ϱ L/4w),
∫ψ² ≤ 8L".) 

### `psiints_consts`

 Constants for [eq:psiints]: A := 2/L ≤ B := c_ϱ/(2w) ("note c_ϱ L/4w ≥ 1 by
[eq:wrange]"), B/A = c_ϱ L/(4w). 

### `indicator_psi_le`

 On (0, ∞), ψ is dominated by the three-piece majorant L·1_{(0,A]} + (2/r)·1_{(A,B]} +
(c_ϱ/w) r⁻²·1_{(B,∞)} (in fact with equality; ≤ is all we use). 

### `integral_psi_Ioi_le`

 [eq:psiints]: Ψ₀ := ∫₀^∞ ψ(r) dr ≤ 4 + 2 log(c_ϱ L/(4w)) (paper: "="). 

### `integral_psi_sq_mul_abs_le`

 [eq:psiints]: ∫_ℝ ψ(r)²|r| dr ≤ 8 + 8 log(c_ϱ L/(4w)) (paper: "="): split (0,2/L],
(2/L, c/2w], (c/2w, ∞): ∫₀^∞ ψ² r ≤ L²(2/L)²/2 + 4 log(cL/4w) + (c/w)²/(2(c/2w)²) = 2 + 4 log + 2. 

### `integral_psi_sq_le`

 [eq:psiints]: "∫_ℝ ψ² ≤ 8L". Uses only ψ ≤ min(L, 2/|r|):
∫ = 2∫₀^∞ ≤ 2(∫₀^{2/L} L² + ∫_{2/L}^∞ 4r⁻²) = 2(2L+2L). 

 #### Generic moment bounds from |F| ≤ ψ-type information 

### `integral_sq_mul_abs_le_of_le_psi`

 If |F| ≤ ψ pointwise then ∫ F²|r| ≤ ∫ ψ²|r| ≤ 8 + 8 log(c_ϱ L/4w). 

### `momMaj`

 The integrable majorant for the r²-moments: 4 on [−1,1] and C²|r|⁻² outside. 

### `sq_mul_sq_le_momMaj`

 Pointwise: |F(r)|·|r| ≤ 2 and |F(r)|·r² ≤ C give F(r)² r² ≤ momMaj C r. 
