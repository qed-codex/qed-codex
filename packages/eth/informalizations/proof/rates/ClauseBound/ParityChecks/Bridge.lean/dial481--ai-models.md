---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sums over marks in three layers (for B_i) and in two layers (for A and the count) are 2^r times B_i, A and the count, modulo 2^{M+1}

An assignment of the n + r variables is a pair (ξ, y) of an assignment of the variables of the
formula and of values of the dummy variables. The numbers of violated clauses of the three layers
for B_i are
the numbers of elements of V(ξ), of D ∩ V(ξ), where D = `Dof` ψ t is a set of clauses, and of the
set of the violated incidences; the two layers for A and the count are the first and the last of
these. A sum Σ_{q ≤ M} w^q·C(c, q) is the sum of w^|S| over the subsets S with at most M elements of
a set with c elements.
So each sum is the right side of a form of the Cut-off lemma (Lemma 12) with dummy variables,
`Dummy.cutoff_dummy`, for f = ω·C(|D ∩ V(ξ)|, i), f = ω and f = η, where ω(ξ) = C(|V(ξ)|, n̄ + 1)
and η(ξ) is the sum of (-1)^|S| over the sets S ⊆ V(ξ) with |S| ≤ n̄, as in Step 1 of Appendix D.
B_i is `Bint`, and A is the sum over ξ of ω(ξ) times the parity brackets of the checks before j. For
the count, the identity `StepOne.product` of Step 1 of Appendix D turns the left side into the
number of satisfying assignments. 

 ### Sums and products 

### `sum_Icc_choose`

 Σ_{q ≤ M} w^q·C(|T|, q) is the sum of w^|S| over the subsets S of T with at most M elements. 

### `sum_Icc_self`

 The sum with one value of q and the weight 1. 

### `sum_split`

 A sum over the assignments of n + r variables is a sum over the two parts. 

### `truncW3`

 The sum over marks in three layers, written out. 

### `truncW2`

 The sum over marks in two layers, written out. 

 ### The three sums 

### `stBridgeB`

 The sum for B_i is 2^r·B_i modulo 2^{M+1}. 

### `two_layers`

 A sum over marks in two layers, the second one the incidences of the complete checks before j,
is 2^r·Σ_ξ f(ξ)·∏_{j' < j} [|V_j'(ξ)| even] modulo 2^{M+1}. 

### `stBridgeA`

 The sum for A is 2^r·A modulo 2^{M+1}. 

### `not_vio_iff`

 A clause is not violated iff one of its literals is true. 

### `Vof_eq_empty_iff`

 ξ violates no clause iff it satisfies the formula. 

### `stBridgeF`

 The sum for the final count is 2^r times the number of satisfying assignments modulo 2^{M+1}, if
the checks are good. 
