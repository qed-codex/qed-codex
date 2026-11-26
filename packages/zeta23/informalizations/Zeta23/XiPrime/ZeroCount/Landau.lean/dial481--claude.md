---
{
  "module": "Zeta23/XiPrime/ZeroCount/Landau.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Landau.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/Landau.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/Landau.lean — Landau's partial fraction for Y′/Y on discs centred at 2+it, and the
LOCAL COUNT of zeros of ξ′.

These are the f := Y = ξ′/Γℝ instances of the generic two-line machine Zeta23/XiPrime/ZeroCount/Generic.lean
(which packages Zeta23.WeilEF.logDeriv_partial_fraction_disk, the halving ρ ↦ 1−ρ̄ and the window geometry);
the Y-specific inputs are ZeroCount/Y.lean's Yfn_analyticOnNhd_disc, Yfn_growth (‖Y‖ ≤ C|Im|⁴ on
1/8 ≤ Re ≤ 4) and two_line_lower (‖Y(2+it)‖ ≥ 1).
Outputs:
  * Yfn_logDeriv_partial_fraction — for |t| ≥ t₁: the zeros of Y within 22/25·91/50 of 2+it form a finite
    set Z with Σ_Z ord ≤ C log(|t|+3), and Y′/Y(s) = Σ_Z ord/(s−ρ) + O(log(|t|+3)) on the 3/2-ball;
  * half_count_large, xiDeriv_local_count (hF2) (hs) — N_{ξ′}(t, t+1] ≤ A₀ log(|t|+3) for all real t.
-/
```

### `Yfn_generic_inputs`

 the generic two-line data (hfa, hgrow, hlow') for f := Y, packaged. 

### `Yfn_logDeriv_partial_fraction`

 **Landau partial fraction for Y′/Y around 2+it** (|t| ≥ t₁). 

 ### the local count 

### `xiDerivZeros_link`

 the link between the configuration xiDerivZeros and f := Y: every configuration point with β ≥ 1/2 is a
zero of Y of the same order. 

### `half_count_large`

 the β ≥ 1/2 half of the window (t, t+1] counted with multiplicity is ≪ log(|t|+3), for |t + 1/2| ≥ t₁. 

### `xiDeriv_local_count`

 **Local count for ξ′** ([XF′ (F3)], the ξ′-analogue of [Tit86, Thm 9.2]): N_{ξ′}(t,t+1] ≤ A₀ log(|t|+3)
for all real t. 
