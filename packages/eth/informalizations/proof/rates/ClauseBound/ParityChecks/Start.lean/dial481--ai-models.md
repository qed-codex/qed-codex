---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Start.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Start.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Start.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The potential: its sign, its value at the start, and the passage from one check to the next

The checks are chosen one clause at a time so that a potential Υ = Υ_par + Υ_inc + Υ_row + Υ_col
(`ParityChecks.Ups`) does not grow. Here, for p = 1/nb with nb ≥ 2:

* all four terms are nonnegative (`nonneg`);
* ½(1 + (1 − 2p)^v) < 5/8 for v > nb (`five_eighths`), because (1 − 2p)^v ≤ exp(−2v/nb) < exp(−2) ≤
  1/4;
* before the first decision the last three terms are 1/8 each and Υ_par ≤ (5/8)^r·Σ_ξ ω(ξ), where
  ω(ξ) = C(|V(ξ)|, nb + 1) (`omega`), so Υ ≤ 1/2 if (5/8)^r·|X|·C(|E|, nb + 1) ≤ 1/8 (`start`);
* the state in which all clauses are decided for check j, seen as the state in which check j + 1
  begins, has the same last three terms and a Υ_par that is not larger (`boundary`).

These are four of the fields of `ParityChecks.ChoiceByPotential`. 

 ### The number p and the two factors 

### `pr_pos`

 p > 0. 

### `one_sub_nonneg`

 0 ≤ 1 − 2p. 

### `one_sub_le_one`

 1 − 2p ≤ 1. 

### `half_ev`

 ½(1 + (−1)^q) = [q even]. 

### `ev_nonneg`

 [q even] ≥ 0. 

### `factor_nonneg`

 ½(1 ± t^u) ≥ 0 for 0 ≤ t ≤ 1. 

### `pow_lt_quarter`

 (1 − 2/nb)^v < 1/4 for v > nb ≥ 2, in the real numbers. 

### `five_eighths`

 ½(1 + (1 − 2p)^v) < 5/8 for v > nb. 

### `term_le`

 The term of one ξ with v violated clauses when a check begins: the factor ½(1 + (1 − 2p)^v) may
be replaced by 5/8. 

### `sum_omega_le`

 Σ_ξ ω(ξ) ≤ |X|·C(|E|, nb + 1). 

### `Upar_fresh_le`

 Υ_par when check j begins. 

### `Upar_done`

 Υ_par when all clauses are decided for check j. 

### `undRow_next`

 The clauses not yet decided, check by check: the same before and after the passage to the next
check. 

### `undCol_next`

 The checks not yet decided, clause by clause: the same before and after the passage to the next
check. 

 ### The four statements 

### `nonneg`

 All four terms of the potential are nonnegative. 

### `start`

 At the start the potential is at most 1/2. 

### `boundary`

 From one check to the next the potential does not grow. 
