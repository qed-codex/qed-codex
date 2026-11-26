---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/LineBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/LineBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/LineBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/LineBound.lean — bounds and continuity for E = ξ′/ξ and ξ″/ξ′ on the line Re s = 5/4
(consumed by the contour `hline` hypothesis and the EF integrability).

  norm_Efn_line                    : ‖E(5/4+it)‖ ≤ C log(2+|t|)
  norm_logDeriv_xiDeriv_line (hF2) : ‖ξ″/ξ′(5/4+it)‖ ≤ C log(2+|t|)
  continuous_Efn_line, continuous_logDeriv_xiDeriv_line (hF2).
Route: E = L + ζ′/ζ with ‖L(5/4+it)‖ ≤ ‖Γℝ′/Γℝ‖ + ‖1/s‖ + ‖1/(s−1)‖ ≤ C_Γ log(2+|t|) + 4/5 + 4
(Zeta23.WeilEF.norm_logDeriv_Gammaℝ_le) and ‖ζ′/ζ‖ = ‖A‖ ≤ A₀ (Expansion.norm_Afn_le); then ξ″/ξ′ = E + E′/E
(Expansion.logDeriv_xiDeriv_eq_Efn) with ‖E′/E‖ ≤ CE (Expansion.derivE_div_E_uniform); log(2+|t|) ≥ log 2
absorbs the constants.
-/
```

### `norm_Lfn_line`

 ‖L(5/4 + it)‖ ≤ C log(2 + |t|). 

### `norm_Efn_line`

 **‖E(5/4 + it)‖ ≤ C log(2 + |t|)**, E = ξ′/ξ = L + ζ′/ζ. 

### `norm_logDeriv_xiDeriv_line`

 **‖ξ″/ξ′(5/4 + it)‖ ≤ C log(2 + |t|)** under (F2) (ξ′ ≠ 0 on the line). 

### `continuous_Efn_line`

 E is continuous along the line Re s = 5/4. 

### `continuous_logDeriv_xiDeriv_line`

 ξ″/ξ′ is continuous along the line Re s = 5/4 (ξ′ entire and zero-free there under (F2)). 
