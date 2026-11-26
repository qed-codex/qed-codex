---
{
  "module": "proof/variables/VariableBound/Top/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent for all widths k, with the count of a sparse formula as in the printed Steps 1 to 4: definitions and interface statements

The twin of proof/sparsification/UniformInK/Top/Defs.lean. The input (1ᵏ 0 1ⁿ 0 and the clauses),
the level picked for n, the precision s, the sparsification with the thresholds `thetaU τ`, τ =
2^(4s+17), the walk through the counting tree, the number
Δ = 2^β with β = `betaU k s`, the cut-off of the width inside the walk, exhaustive counting, and the
merge with the algorithm for the bound in m are those of that file, and its definitions are used.
What differs:
* a leaf of the counting tree is counted by `countD` (Steps 1 to 4 of Appendix D as printed) in
  place of `countOL`;
* the plan has three tests in place of five: s ≥ `s0U k`; 2^β ≤ n + 1; n ≥ 29·⌈log₂(2Δ)⌉ + 19, which
  gives the bounds r̄ ≤ 10n and M ≤ 14n of the Setting of Appendix D. There is no parameter a.
The text assumes 3 ≤ k ≤ (log n)^(1/4) and n ≥ n₀ and falls back on exhaustive counting otherwise
(Step 6). A program must compute its tests, so these three take that place.
This file has definitions only. The statements `St…` are propositions; one file proves each of them. 

 ### The functions 

### `valD`

 The count of the formula of a node of the counting tree. Δ = 2^β, cut off at n + 1. 

### `restD`

 The exponent of a pad that suffices for everything but the networks: the list of profiles, the
list of checks, the rounds of the walk, the stack of the walk. 

### `needD`

 The exponent of a pad that suffices for n variables at the index i with precision s. 

### `planAtD`

 If s ≥ s0U k, 2^β ≤ n + 1 and n ≥ 29·⌈log₂(2·2^β)⌉ + 19 (β = betaU k s), and the exponent of the
networks, computed under the bound n, exists and plus `restD` is at most n: that sum (which is
`needD` for a polynomial-time solver,
`Correct.planAtD_some`). Otherwise `none`, and exhaustive counting is used. 

### `planD`

 The plan for the input x. 

### `eD`

 The exponent function for the bound in n: the exponent of the plan, or n. 

 ### The choice between the two algorithms by an «if» (proof of Corollary 11: «computing the two exponents … and running only the algorithm with the smaller one»; here the two exponents are computed exactly) 

### `useMD`

 Is the algorithm for the bound in m taken? Only if every variable occurs, there is a clause, and
its exponent is not the larger one. 

### `eBD`

 The exponent function of the choice: that for the bound in m where `useMD` holds, that for the
bound in n elsewhere. 

 ### The budgets 

### `StBudgetD`

 The budgets other than those of the networks, for k ≥ 1 and s ≥ s0U k: a pad of length at least
2^(restD …) suffices for the list of profiles, the list of checks, the rounds of the walk and its
stack. 

 ### The exponents 

### `StExpBD`

 For k ≥ 1 and a k-CNF: the exponent is at most that of the algorithm for n, and, if all
variables occur and there is a clause, at most that of the algorithm for m. 

 ### Steps 4 and 5: the exponent is O(k²·e·n·(s+1)), with an absolute constant, unless k² is larger than a multiple of log n

The text has 2^O(k²·e·n·log(k/e)) for 3 ≤ k ≤ (log n)^(1/4); here s+1 takes the place of log(k/e)
(the plan asks s ≥ 2·(bit length of k), and s ≥ log₂(1/e)), and the alternative ⌊log₂ n⌋ < B·k²
takes the place of the range of k. 

### `StPlanLeD`

 The exponent of a plan, or else n, is at most n. 

### `StArithD`

 For a polynomial-time solver S with a sequence of levels Q, and a precision s(l) (the length of
slU l) with 1/2^s(l) ≤ e_l and 2^s(l) ≤ (2/e_l)^C for every l: there are A and B, depending on
neither k nor n, such that for k ≥ 1 and
n ≥ K₀^17 (K₀ the number of nodes of the clique of level 0), with l the level picked for n and s =
s(l), the exponent of the plan, or n if there is none, is at most A·k²·n·e_l·(s+1), or ⌊log₂ n⌋ <
B·k². 

 ### Step 6: the running time of the padding machine against the bound in n 

### `StTimeD`

 For the exponent of the algorithm for n: q·(|x| + 2^e + 1)^q is within the bound in n with k² in
the exponent, for every q, with a constant D that does not depend on k; for k ≥ 1, n ≥ 1 and every
k-CNF. 
