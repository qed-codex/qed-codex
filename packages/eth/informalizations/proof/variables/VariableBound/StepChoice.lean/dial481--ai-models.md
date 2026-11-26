---
{
  "module": "proof/variables/VariableBound/StepChoice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/StepChoice.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/StepChoice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix D, Step 2 (finding the checks): the mathematics

Proves `AppVariables.StepChoice`, for an abstract family Γ_u, u ∈ Ω, with the properties (a), (b), (c)
of Lemma 13 (`AppVariables.IsFamily`). The argument is the one of the text:

* appending Γ_u multiplies the term of ξ in X(𝓛) by [ |Γ_u ∩ V(ξ)| even ]; a nonzero term has |V(ξ)| >
  n̄, so by (c) the average of X(𝓛, Γ_u) is at most (3/4)·X(𝓛) (`avgX`);
* by (b) the average of 2^[E ∈ Γ_u] is at most 1 + p (`avgCol`);
* so, for a list of fewer than r̄ checks, the average of Υ(𝓛, Γ_u) is at most Υ(𝓛) (`avgUps`), and
  so is the minimum (`minUps`);
* for the empty list both terms of Υ are at most 1 (`ups_nil`);
* Υ(𝓛) ≤ 2 gives X(𝓛) ≤ (3/4)^r·2^β (`x_of_ups`) and load(E) ≤ t̄ + 1 (`load_of_ups`); a list with
  X(𝓛) > 0 and this bound has fewer than r̄ checks (`lt_rb`);
* hence, by induction along the algorithm, every reached list has at most r̄ checks and Υ ≤ 2
  (`reached`); if Ω is not empty, the algorithm can go on while X(𝓛) > 0 (`progress`).

The text defines Υ for lists of at most r̄ checks and bounds r after Υ; here the two bounds are
proved together, because the step from 𝓛 to (𝓛, Γ_u) uses r < r̄. The condition m > n̄ of the text
and the
minimality of r̄ and t̄ are not used. 

 ### The factors [q even] and the sum X(𝓛) 

### `ev_nonneg`

 0 ≤ [q even]. 

### `allEven_nonneg`

 0 ≤ ∏_j [ |V_j(ξ)| even ]. 

### `allEven_append`

 Appending the check Γ multiplies the product of ξ by [ |Γ ∩ V(ξ)| even ]. 

### `Xsum_nonneg`

 0 ≤ X(𝓛). 

### `Xsum_nil_le`

 For the empty list, X ≤ 2^n·C(m, n̄+1), if there are at most 2^n assignments. 

 ### The two averages 

### `sum_ev_le`

 For a family as in Lemma 13 with v = n̄, by its part (c): for a set W of more than n̄ clauses, [ |Γ_u
∩ W| even ] is 1 for at most three quarters of the u ∈ Ω. 

### `avgX`

 Step 2, «the average of X(𝓛, Γ_u) over u ∈ Ω is at most (3/4)·X(𝓛)», for a family as in Lemma 13
with v = n̄. 

### `pp_nonneg`

 0 ≤ p. 

### `avgCol`

 Step 2, «the average of 2^[E ∈ Γ_u] is at most 1 + p», for a family as in Lemma 13 with v = n̄ ≥ 1. 

 ### The potential Υ 

### `load_append`

 load(E) for the list (𝓛, Γ) is load(E) for 𝓛 plus [E ∈ Γ]. 

### `avgUps`

 Step 2, «the average of Υ(𝓛, Γ_u) is at most Υ(𝓛)», for a list of fewer than r̄ checks and a
family as in Lemma 13 with v = n̄ ≥ 1. 

### `minUps`

 Step 2, «and so is the minimum»: under the hypotheses of `avgUps`, a list (𝓛, Γ_u), u ∈ Ω, with
the smallest Υ has Υ(𝓛, Γ_u) ≤ Υ(𝓛). 

### `first_nonneg`

 The first term of Υ is not negative. 

### `second_nonneg`

 The second term of Υ is not negative. 

### `ups_nil`

 Step 2, «for the empty list both terms are at most 1, by X ≤ 2^(β−1) and the choice of t̄»: Υ ≤
2 for the empty list, if there are at most 2^n assignments, β is the β of the text and
m·(1+p)^r̄ ≤ 2^t̄. 

### `x_of_ups`

 Step 2, «hence X(𝓛) ≤ (3/4)^r·2^β»: from Υ(𝓛) ≤ 2 and β ≥ 1. 

### `lt_rb`

 A list with X(𝓛) > 0, at most r̄ checks and X(𝓛) ≤ (3/4)^r·2^β has fewer than r̄ checks, because
3^r̄·2^β < 4^r̄. 

### `load_of_ups`

 Step 2, «also 2^(load(E)−t̄) ≤ 2 for every clause E»: from Υ(𝓛) ≤ 2, load(E) ≤ t̄ + 1. 

 ### Along the algorithm 

### `one_le_beta`

 1 ≤ β. 

### `reached`

 Step 2, «every list that is reached has Υ(𝓛) ≤ 2», together with r ≤ r̄. Hypotheses: at most 2^n
assignments, n̄ ≥ 1, β, r̄, t̄ as in the text, a family as in Lemma 13 with v = n̄. 

### `reached_mem`

 Every check of a reached list is one of the Γ_u, u ∈ Ω. 

### `progress`

 If 𝓛 is reached, X(𝓛) > 0 and Ω is not empty, the algorithm can go on: among the lists (𝓛, Γ_u),
u ∈ Ω, one has the smallest Υ, and it is reached. 

### `stepChoice`

 Step 2 of Appendix D (finding the checks): the averages of X, 2^[E ∈ Γ_u] and Υ, r ≤ r̄ and Υ ≤
2 on reached lists, X(𝓛) ≤ (3/4)^r·2^β, the loop's progress and end, and the bounds on r, |Λ_j|,
load(E). 
