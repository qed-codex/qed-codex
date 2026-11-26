---
{
  "module": "Zeta23/XiPrime/ZeroCount/Y.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Y.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Y.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Y.lean — analytic estimates for Y := ξ′/Γℝ.

Y (Zeta23.XiPrime.Yfn, Seam.lean §3) is analytic on Re s > 0 with the zeros/multiplicities of ξ′.  Here:
  * Yfn_growth      : ‖Y(s)‖ ≤ C·|Im s|⁴ on 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2  (closed form + ζ linear growth
                      Zeta23.RvM.zeta_growth + Cauchy estimate for ζ′ + vertical Stirling for ψ);
  * two_line_lower  : for |t| ≥ t₁:  3 ≤ Re (L + ζ′/ζ)(2+it)  and  1 ≤ ‖Y(2+it)‖
                      (Re ψ(1+it/2) ≥ log(|t|/2) − 4 from Zeta23.StirlingVert.digamma_stirling, against the
                      t-uniform bound ‖ζ′/ζ(2+it)‖ ≤ ‖ζ′(2)/ζ(2)‖, and ‖ζ(2+it)‖ ≥ 1/3).
These are exactly the two inputs (growth on a disc inside Re s > 0, lower bound at its centre 2+it) that
Jensen/Landau need; cf. Zeta23/RvM/LocalCount.lean and Zeta23/WeilEF/Landau.lean for ζ.
-/
```

 ### crude digamma bounds from vertical Stirling 

### `norm_digamma_le`

 ‖ψ(w)‖ ≤ ‖w‖ + 8 for Re w > 0, |Im w| ≥ 1. 

### `re_digamma_ge`

 Re ψ(w) ≥ log |Im w| − 4 for Re w > 0, |Im w| ≥ 1. 

 ### growth of Y 

### `norm_deriv_zeta_le`

 Cauchy estimate for ζ′ from the linear growth of ζ:  ‖ζ′(s)‖ ≤ 24·C_ζ·|Im s| for Re s ≥ 1/8, |Im s| ≥ 2. 

### `norm_logDeriv_Gammaℝ_le`

 ‖Γℝ′/Γℝ(s)‖ ≤ 4|Im s| for 0 < Re s ≤ 4, |Im s| ≥ 2 (crude). 

### `Yfn_growth`

 **Polynomial growth of Y**: ‖Y(s)‖ ≤ C·|Im s|⁴ for 1/8 ≤ Re s ≤ 4, |Im s| ≥ 2. 

### `Yfn_analyticOnNhd_disc`

 analyticity of Y on a closed disc of radius r < 2 about 2 + it. 

 ### the line Re s = 2 

### `norm_logDeriv_zeta_two_le`

 t-uniform bound for ζ′/ζ on Re s = 2: ‖ζ′/ζ(2+it)‖ ≤ ‖ζ′(2)/ζ(2)‖. 

### `re_Lfn_two_ge`

 Re L(2+it) ≥ ½ log(|t|/2) − 3 for |t| ≥ 2. 

### `two_line_lower`

 **Lower bounds on the line Re s = 2, far up**: there is t₁ ≥ 2 such that for |t| ≥ t₁,
  3 ≤ Re (L + ζ′/ζ)(2+it)   and   1 ≤ ‖Y(2+it)‖. 

 ### ‖Γℝ′/Γℝ‖ ≪ log (second-order Stirling) 

### `norm_logDeriv_Gammaℝ_le_log`

 ‖Γℝ′/Γℝ(s)‖ ≤ log(|Im s|+3) + 5 for 0 < Re s ≤ 4, |Im s| ≥ 2. 
