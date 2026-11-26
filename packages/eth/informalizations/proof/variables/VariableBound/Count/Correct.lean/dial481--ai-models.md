---
{
  "module": "proof/variables/VariableBound/Count/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Count/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One sparse formula counted as in Steps 1 to 4 of Appendix D: the count is right

Proves `VariableBound.StCountD` from the statements on the parts: the parameters (`StParamSpec`,
`ParamIneq`), display (63) and the remark on the empty list of Step 1, Lemma 13 for the listed
family (`Fld.StFamD`), the search of
Step 2 (`StSearchD`), and the networks of Step 3 (`Net.StFit`, `Net.StTbMax`, `Net.StNPrMax`,
`Net.StEvXF`).

* From n ≥ 29·⌈log₂(2Δ)⌉ + 19: the computed n̄, r̄, t̄ are those of the text, and n̄ ≥ 2.
* If m ≤ n̄: β = n + 1, so M ≤ 14n; the empty list is fit for an evaluation and has X = 0.
* If m > n̄: display (61) and t̄ ≤ `tbMax`; every list with display (67) is fit for an evaluation,
  so the program computes its X, and its word fits under the pad (`len_le`); so the search finds a
  list with X = 0.
* In both cases the program computes F(𝓛), which is the number of ξ that violate no clause (display
  (63)), that is `nSat n ψ` (`card_Vof`). 

 ### Assignments that violate no clause 

### `not_vio_iff`

 A clause is not violated iff one of its literals is true. 

### `Vof_eq_empty_iff`

 ξ violates no clause iff it satisfies the formula. 

### `card_Vof`

 The number of ξ with V(ξ) = ∅ is the number of satisfying assignments. 

 ### Logarithms 

### `lg_le_LD`

 log(2Δ) ≤ ⌈log₂(2Δ)⌉, for Δ ≥ 1. 

### `sq_le`

 (2Δ)² ≤ 2^n, if 2·⌈log₂(2Δ)⌉ ≤ n. 

### `row_le`

 A check with n̄·|Λ| ≤ 16m has at most `sbMax Δ` clauses: s̄ = 16m/n̄ < 32Δ·log(2Δ). Hypotheses:
the inequalities of «Setting and parameters», 2 ≤ Δ, m ≤ Δn, n̄ the number of the text. 

 ### The word of a list of checks 

### `len_row`

 The word of a list l of numbers that are at most N has length at most |l|·(3·size(N) + 4) + 2. 

### `len_rows`

 The word of a list L of lists whose words have length at most c has length at most |L|·(c + 2) + 2. 

### `len_le`

 The word of a list of at most R lists of at most s numbers that are at most N has length at most
8(R + 1)(s + 1)(size(N) + 2) + 8. 

 ### The count 

### `evF_eq`

 If the list 𝓛 is fit for an evaluation, M ≥ β − 1 + r, M ≥ n + r and X(𝓛) = 0, the program's
F(𝓛) is the number of satisfying assignments. Further hypotheses: the statements on the evaluation,
on the number of
profiles and display (63); a correct solver with K ≥ 2; the pad fits. 

### `stCountD`

 Steps 1 to 4 of Appendix D: the count of one sparse formula is right, given the statements on
the evaluation by networks (`Net.StEvXF`, `Net.StFit`, `Net.StTbMax`, `Net.StNPrMax`), on the search
(`StSearchD`), on the listed
family of Lemma 13 (`Fld.StFamD`), on the parameters (`StParamSpec`, `ParamIneq`), display (63) and
the remark that the empty list has X = 0 if m ≤ n̄. 
