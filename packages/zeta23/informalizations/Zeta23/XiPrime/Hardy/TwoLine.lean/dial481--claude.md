---
{
  "module": "Zeta23/XiPrime/Hardy/TwoLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/TwoLine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/TwoLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/TwoLine.lean — estimates for W on the line Re s = 2 and in the strip 1/8 ≤ Re ≤ 4, |Im| ≥ 2
(zero side; [XF′ (Z5), (Z6)(i), (Z7) local inputs]).  These are exactly the hypotheses
(hfa, hgrow, hlow') of Zeta23/XiPrime/ZeroCount/Generic.lean, for f := hardyW:
  * hardyW_analyticOnNhd_disc : W analytic on closedBall (2+it) (91/50) for |t| ≥ 2 (the disc misses ℝ);
  * re_L2_two_ge : Re L₂(2+it) ≥ ½log(|t|/2) − 3  (digamma Stirling at 1+it/2 and, via the shift Γℝ′/Γℝ(u) =
    Γℝ′/Γℝ(u+2) − 1/u twice, at (3−it)/2);
  * hardyW_two_line_lower : ∃ t₁ ≥ 2, ∀ |t| ≥ t₁, 1 ≤ ‖W(2+it)‖  (= ‖ζ(2+it)‖·‖L₂ + ζ′/ζ‖ ≥ (1/3)·3);
  * hardyW_growth : ‖W(s)‖ ≤ C·|Im s|² on 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2.
-/
```

 ### the shift Γℝ′/Γℝ(u) = Γℝ′/Γℝ(u+2) − 1/u off the real axis 

 ### Re L₂ on the line Re s = 2 

### `re_logDeriv_Gammaℝ_ge`

 Re Γℝ′/Γℝ(s) ≥ −1 + ½(log(|Im s|/2) − 4) for Re s > 0, |Im s| ≥ 2. 

### `re_L2_two_ge`

 **Re L₂(2+it) ≥ ½log(|t|/2) − 3** for |t| ≥ 2. 

 ### analyticity on the Landau discs 

 ### the lower bound on Re s = 2 

### `hardyW_eq_zeta_mul`

 W = ζ·(ζ′/ζ + L₂) where ζ ≠ 0. 

### `hardyW_two_line_lower`

 **‖W(2+it)‖ ≥ 1 for |t| ≥ t₁**, and Re(ζ′/ζ + L₂)(2+it) ≥ 3 there  [XF′ (Z6)(i)]. 

### `exists_hardyW_ne_zero_upper`

 W is not identically zero on either half-plane: W(2 ± it₁) ≠ 0. 

 ### polynomial growth of W in the strip 

### `norm_logDeriv_Gammaℝ_le_lin`

 ‖Γℝ′/Γℝ(s)‖ ≤ ‖s‖/4 + 5 for Re s > 0, |Im s| ≥ 2 (crude, from ‖ψ(w)‖ ≤ ‖w‖ + 8). 

### `norm_L2_le`

 ‖L₂(s)‖ ≤ 2|Im s| + 12 for 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2. 

### `hardyW_growth`

 **growth of W**: ‖W(s)‖ ≤ C·|Im s|² on 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2. 
