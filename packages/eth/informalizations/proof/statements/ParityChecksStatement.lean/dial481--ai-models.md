---
{
  "module": "proof/statements/ParityChecksStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ParityChecksStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ParityChecksStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parity checks (pure mathematics; imports Mathlib only): definitions of Step 1 of Appendix D (σ_i, η, good checks, tuples of marks), and statements on a choice of the checks by conditional expectations that differs from its Step 2

Abstract setting: X is the finite set of assignments ξ, E the finite set of clauses, V ξ the set of
clauses that ξ violates. Nothing else about formulas is used. Checks are numbered
0, …, r − 1 (Appendix D of the paper: 1, …, r). 

### `ev`

 [q even]. 

### `sig`

 σ₀ = 1, σ_i = (−1)^i·2^{i−1} for i ≥ 1. 

### `eta`

 η(ξ): inclusion–exclusion over the violated clauses, cut off at nb marks. 

### `Good`

 The checks are good: every ξ that violates more than nb clauses violates an odd number of
clauses of some check. 

### `tuples`

 The tuples (S_j), j ∈ J, with S_j ⊆ Λ_j ∩ V(ξ) and at most M marks in all (S_j = ∅ for j < r
outside J). 

 ## The potential. A state: the checks before j are complete, Λ j is the part of check j chosen so far, D the clauses not yet decided for check j, later checks are empty. p = 1/nb. 

### `omega`

 ω(ξ) = C(|V(ξ)|, nb + 1). 

### `pr`

 p = 1/nb. 

### `undRow`

 The number of clauses not yet decided for check j'. 

### `undCol`

 The number of checks for which the clause e is not yet decided. 

### `Ups`

 The potential. 

### `tUpar`

 Υ_par with (1 − 2p)^u replaced by Σ_{i ≤ i₀} (−2p)^i·C(u,i). 

### `Aint`

 A = Σ_ξ ω(ξ)·∏_{j'<j} [|V_{j'}(ξ)| even]. 

### `Bint`

 B_i = Σ_ξ ω(ξ)·C(|D ∩ V(ξ)|, i)·(−1)^{|V_j(ξ)|}·∏_{j'<j} [|V_{j'}(ξ)| even]. 

### `IsState`

 A state in order. 

### `putIn`

 The clause e is put into check j. 

### `ChoiceByPotential`

 Choice of the checks clause by clause, by a potential of four terms (factor 5/8, p = 1/nb); Step
2 of Appendix D instead uses Lemma 13. These are properties of the potential; no algorithm that
makes the choices is stated here. 

### `ChoiceByPotential.nonneg`

 all four terms are nonnegative 

### `ChoiceByPotential.five_eighths`

 ½(1 + (1 − 2p)^v) < 5/8 for v > nb 

### `ChoiceByPotential.start`

 at the start the potential is at most 1/2 

### `ChoiceByPotential.martingale`

 one decision: p·Υ^in + (1 − p)·Υ^out = Υ 

### `ChoiceByPotential.boundary`

 from one check to the next the potential does not grow 

### `ChoiceByPotential.structure_`

 what Υ < 1 gives 

### `ChoiceByPotential.final`

 in the final state Υ < 1 makes the checks good 

### `ChoiceByPotential.approx`

 the error of the truncated series carries over to the potential 

### `ChoiceByPotential.compute`

 the truncated potential through the integers A and B_i 

### `ChoiceByPotential.abs_le`

 A and B_i are small 
