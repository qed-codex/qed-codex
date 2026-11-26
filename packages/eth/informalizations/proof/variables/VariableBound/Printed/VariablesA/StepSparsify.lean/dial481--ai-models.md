---
{
  "module": "proof/variables/VariableBound/Printed/VariablesA/StepSparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/StepSparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/VariablesA/StepSparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The end of Step 5, and the «In particular» of Theorem D (a)

* `stepSparsifyFacts`: log K > (log n)/(17C₀) and log(k/e) ≤ (C₀ + 1/4)·log log n.
* `stepSparsifyLarge`: k·log n ≤ e·n for large n. `stepSparsifySmall`: for the finitely many smaller
  n, n and k·log n are O(k²·e·n·log(k/e)).
* `thmVariablesAInParticular`: if e_ℓ ≤ c·(log K_ℓ)^(−α′), a machine with the bound of Theorem D (a)
  takes at most 2^{O(k²·n·log log n/(log n)^α′)} steps. 

### `stepSparsifyFacts`

 Step 5: «log K > (log n)/(17C₀), and log(k/e) ≤ (C₀ + 1/4)·log log n», for the level ℓ of n, K =
K_ℓ, e = e_ℓ and 1 ≤ k ≤ (log n)^(1/4). 

### `lg_le_self`

 log n ≤ n. 

### `stepSparsifyLarge`

 Step 5: «k log n ≤ en for large n», where n is large if it exceeds a bound that depends only on
C₀; for k ≤ (log n)^(1/4) and e ≥ (log n)^(−C₀). 

### `stepSparsifySmall`

 Step 5: «For the finitely many smaller n …, trying all assignments is within the bound»: n ≤
c·k²·e·n·log(k/e) and k·log n ≤ c·k²·e·n·log(k/e) for 2 ≤ n < n₁, k ≥ 3 and (log n)^(−C₀) ≤ e ≤ 1,
with c depending on C₀ and n₁ only. 

### `thmVariablesAInParticular`

 Theorem D (a), last sentence: if e_ℓ ≤ c·(log K_ℓ)^(−α′) for all ℓ, with α′ > 0, then a machine
with the bound of Theorem D (a) takes at most 2^{C'·k²·n·log log n/(log n)^α′} steps, for n ≥ K₀^17
and 3 ≤ k ≤ (log n)^(1/4). 
