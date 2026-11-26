---
{
  "module": "ThreeSumApsp/RunningTimes/Sec5/Corollary40.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary40.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40 on the word RAM

The route, as in the paper.  Each of the three hinted problems is solved in phases by programs that
use a data structure for a thin matrix product: the phase after the hint preprocesses, the last
phase asks queries.  For `τ < 1/18` it is the data structure of Corollary 26
(`wordRam_corollary_40_times`), for `τ < ε*` ("General τ") that of Corollary 31 with suitable
parameters (`wordRam_corollary_40_general_times`); for uMv-hinted uMv the conditions are
`τ₁ < τ₂/18` and `τ₁ < ε* τ₂`.  "In each case the phases beat the conjectured
bounds whatever the value of ω": every exponent is below the conjectured one, and larger exponents
are easier to achieve (`AchievesVHinted.mono` and its two companions).  So the three conjectures
fail for `τ < ε*`, by `not_conjecture52_of_achieves` and its two companions, and with them for
`τ < 1/18 < ε*` (`Corollary40.fail_mono`, `wordRam_corollary_40_fail`).


 ## Larger exponents are easier to achieve 

### `Within.mono`

 A bound `O(n^a)` is also a bound `O(n^{a'})` for `a ≤ a'`, with a constant that is not negative.


### `AchievesVHinted.mono`

 v-hinted Mv: larger exponents for Phases 2 and 3 are easier to achieve. 

### `AchievesMvHinted.mono`

 Mv-hinted Mv: larger exponents for Phases 2 and 3 are easier to achieve. 

### `AchievesUMvHinted.mono`

 uMv-hinted uMv: larger exponents for Phases 2, 3 and 4 are easier to achieve. 

 ## The running times 

### `wordRam_corollary_40_times`

 **Corollary 40**, on the word RAM: the running times for `τ < 1/18`. 

### `wordRam_corollary_40_general_times`

 **The proof of Corollary 40**, paragraph "General τ", on the word RAM: the running times for
`τ < ε*`. 

 ## The conjectures fail 

### `Corollary40.fail_mono`

 Conjectures that fail up to `τ₀` fail up to every smaller bound. 

### `Corollary40.fail_general`

 For `τ < ε*` every exponent is below the conjectured one. 

### `wordRam_corollary_40_fail`

 **Corollary 40**, on the word RAM: the three conjectures fail for `τ < 1/18`, and more
generally for `τ < ε*`. 
