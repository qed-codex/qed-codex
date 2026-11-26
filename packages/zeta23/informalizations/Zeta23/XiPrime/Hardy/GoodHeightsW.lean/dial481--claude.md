---
{
  "module": "Zeta23/XiPrime/Hardy/GoodHeightsW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/GoodHeightsW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/GoodHeightsW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/GoodHeightsW.lean — good heights for the W contour integrand F_𝒵 := L₂ + W′/W
(consumed by Hardy/EFContour.lean; W-analogue of Zeta23/XiPrime/ZeroCount/GoodHeights.lean).

  hardyW_good_heights (hZ : WZerosInStrip t₀) (hs : WSeam t₀) :
    ∃ C > 0, ∃ j₀ ≥ t₀ + 1, ∀ j ≥ j₀, ∃ R ∈ [j, j+1], ∀ s, Im s = ±R → −1 ≤ Re s ≤ 2 →
      W(s) ≠ 0 ∧ ‖L₂(s) + W′/W(s)‖ ≤ C·log²(j+3).

Route: on 1/2 ≤ Re s ≤ 2 this is the GENERIC two-line machine (ZeroCount/Generic.good_heights_two_line) at f := W with
the inputs of Hardy/Count.hardyW_generic_inputs (W analytic on the discs about 2+it, ‖W‖ ≤ C|Im|²,
‖W(2+it)‖ ≥ 1) and the configuration wZeros hZ hs, plus ‖L₂(s)‖ ≤ log(|Im s|+3) + 6 there (Stirling via
ZeroCount.norm_logDeriv_Gammaℝ_le_log, the (1−s)-half shifted by Hardy/TwoLine.logDeriv_Gammaℝ_shift); on
−1 ≤ Re s < 1/2 by the ODD symmetry F_𝒵(1−s) = −F_𝒵(s), which is the logarithmic derivative of the functional
equation W(s) = −χ(s)W(1−s) (χ′/χ = −2L₂, L₂(1−s) = L₂(s)).
-/
```

 ### ‖L₂‖ ≪ log on 1/2 ≤ Re s ≤ 2 

### `norm_L2_le_log`

 ‖L₂(s)‖ ≤ log(|Im s| + 3) + 6 for 1/2 ≤ Re s ≤ 2, |Im s| ≥ 2. 

 ### the odd symmetry of F_𝒵 = L₂ + W′/W 

### `logDeriv_hardyW_eq_reflect`

 logarithmic derivative of W(s) = −χ(s)W(1−s):  W′/W(s) = −2L₂(s) − (W′/W)(1−s)  (off ℝ, W(s) ≠ 0). 

### `L2_add_logDeriv_hardyW_one_sub`

 **F_𝒵(1−s) = −F_𝒵(s)**, F_𝒵 := L₂ + W′/W (off ℝ, at points where W ≠ 0). 

 ### good heights 

### `hardyW_good_heights`

 **Good heights for F_𝒵 = L₂ + W′/W.** 
