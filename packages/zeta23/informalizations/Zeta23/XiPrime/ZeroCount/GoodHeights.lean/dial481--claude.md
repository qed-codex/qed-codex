---
{
  "module": "Zeta23/XiPrime/ZeroCount/GoodHeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/GoodHeights.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ZeroCount/GoodHeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ZeroCount/GoodHeights.lean — good heights for ξ″/ξ′ (used by the explicit-formula contour for ξ′;
cf. Zeta23/WeilEF/GoodHeights.lean for the ζ analogue).

  xiDeriv_good_heights (hF2) : ∃ C > 0, ∃ j₀, ∀ j ≥ j₀, ∃ R ∈ [j, j+1], on Im s = ±R, −1 ≤ Re s ≤ 2:
      ξ′(s) ≠ 0  and  ‖ξ″/ξ′(s)‖ ≤ C·log²(j+3).
Proof: on 1/2 ≤ Re s ≤ 2 this is the generic two-line machine
ZeroCount/Generic.good_heights_two_line at f := Y = ξ′/Γℝ (Landau partial fraction about 2 ± iR, local count,
exists_far_point) giving Y ≠ 0 and ‖Y′/Y‖ ≪ log², plus ξ″/ξ′ = Γℝ′/Γℝ + Y′/Y with Γℝ′/Γℝ ≪ log (Stirling,
ZeroCount/Y.norm_logDeriv_Gammaℝ_le_log); on −1 ≤ Re s < 1/2 reflect through s ↦ 1 − s (ξ″/ξ′(1−s) = −ξ″/ξ′(s)).
-/
```

### `xiDeriv_good_heights`

 **Good heights for ξ″/ξ′.** 
