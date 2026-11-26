---
{
  "module": "proof/variables/ThmVariables/Bound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/Bound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/ThmVariables/Bound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) with the printed hypothesis: the arithmetic on K_ℓ and e_ℓ

* `exists_level`: every n ≥ K₀^17 has a level, «the largest ℓ with K_ℓ ≤ n^(1/17)», because K_ℓ > ℓ.
* `e_pos`, `e_ge_n`, `lg_lt`: e_ℓ > 0; at the level ℓ of n, e_ℓ ≥ (log n)^(−C₀) and log n <
  17·C₀·log K_ℓ (Step 5 of Appendix D: «log K > (log n)/(17C₀)»).
* `boundAtANumberBetween`: for 0 < e ≤ e′ ≤ 2e, e′ ≤ 1 ≤ k: log(k/e′) ≤ log(k/e), so
  k²·e′·n·log(k/e′) ≤ 2·k²·e·n·log(k/e).
* `inParticular`: the last sentence of Theorem D (a).
  proof/variables/VariableBound/Printed/VariablesA/StepSparsify.lean proves it for a solver with a
  sequence of levels (`MainTheoremForms.ThmVariablesAInParticular`). That form cannot be called
  here: a sequence of levels holds a polynomial-time program that picks the level, and here K is any
  sequence with the printed inequalities. So the argument is repeated
  on K: e ≤ c·(log K)^(−α′) ≤ c·(17C₀)^α′·(log n)^(−α′) and log(k/e) ≤ (C₀ + 1)·log log n. 

 ### The levels 

### `exists_level`

 For K, e, C₀ with the printed inequalities (`CliqueLevels.Levels`), every n ≥ K₀^17 has a level:
an ℓ with K_ℓ^17 ≤ n < K_(ℓ+1)^17. 

### `e_pos`

 For K, e, C₀ with the printed inequalities (`CliqueLevels.Levels`): e_ℓ > 0. 

### `K_le_n`

 K_ℓ ≤ n at the level ℓ of n. 

### `e_ge_n`

 For K, e, C₀ with the printed inequalities (`CliqueLevels.Levels`): (log n)^(−C₀) ≤ e_ℓ at the
level ℓ of n. 

### `lg_lt`

 «log K > (log n)/(17C₀)»: for K, e, C₀ with the printed inequalities (`CliqueLevels.Levels`),
log n < 17·C₀·log K_ℓ at the level ℓ of n. 

 ### The bound at a number in [e, 2e] 

### `expVariablesA_le_two_mul`

 For 0 < e ≤ e′ ≤ 2e, e′ ≤ 1 ≤ k: k²·e′·n·log(k/e′) ≤ 2·k²·e·n·log(k/e). 

### `boundAtANumberBetween`

 The bound at a number in [e, 2e] is the bound at e with twice the constant: for 0 < e ≤ e′ ≤ 2e,
e′ ≤ 1 and k ≥ 1, 2^{C·k²·e′·n·log(k/e′)} ≤ 2^{2C·k²·e·n·log(k/e)}, both rounded down. 

 ### «In particular» 

### `inParticular`

 «In particular, if e_ℓ = O((log K_ℓ)^(−α′)) for a constant α′ > 0, the time is 2^{O(k²·n·log log
n/(log n)^α′)}» (Theorem D (a)), for every machine with the bound of Theorem D (a). 
