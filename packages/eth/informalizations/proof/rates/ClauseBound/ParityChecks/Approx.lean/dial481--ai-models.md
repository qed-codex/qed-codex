---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Approx.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Approx.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Approx.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The truncated potential

Three fields of `ParityChecks.ChoiceByPotential`, as theorems of their own, on the term `Upar` of a
potential for the choice of checks (Step 2 of Appendix D; not the Υ printed there). In `Upar` the
power (1 − 2p)^u
is replaced by the first i₀ + 1 terms of its binomial series (`tUpar`). If that changes every power
with u ≤ |E| by at most ε, it changes `Upar` by at most ½·ε·|X|·C(|E|, nb + 1) (`approx`).
The truncated term is (5/8)^(r−1−j)·½·(A + Σ_{i ≤ i₀} (−2p)^i·B_i) with integers A and B_i
(`compute`), and |A| ≤ |X|·C(|E|, nb + 1), |B_i| ≤ |X|·C(|E|, nb + 1)·C(|E|, i) (`abs_le`). 

 ### Sizes of the factors 

### `ev_nonneg`

 [q even] is 0 or 1. 

### `ev_le_one`

 [q even] is 0 or 1. 

### `abs_prod_ev_le`

 A product of numbers [q even] has absolute value at most 1. 

### `abs_prod_ev_cast_le`

 The same for the rational numbers. 

### `omega_le`

 ω(ξ) ≤ C(|E|, nb + 1). 

### `choose_card_le`

 C(|s|, i) ≤ C(|E|, i) for every set s of elements of E. 

 ### The three fields 

### `approx`

 The error of the truncated series carries over to the potential. 

### `compute`

 The truncated potential through the integers A and B_i. 

### `abs_le`

 A and B_i are small. 
