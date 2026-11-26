---
{
  "module": "proof/variables/VariableBound/StepParity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/StepParity.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/StepParity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix D, Step 1, as printed: parity checks, and a cut-off modulo a power of 2

This file proves these statements of the section «Step 1» of `AppVariablesStatement.lean`:

* display (63): if X(𝓛) = 0, then F(𝓛) is the number of satisfying assignments;
* if m ≤ n̄, the empty list has X = 0;
* Lemma 12 (Cut-off);
* display (65);
* «The residues determine the numbers».

The proofs are the printed ones. The three cases of display (63) for one ξ and the cut-off for
checks numbered by `Fin r` are in `proof/rates/ClauseBound/ParityChecks/StepOne.lean`, the latter in
a more
general form (a second set of checks with weights (−2)^i, here empty); this file passes from a list
of checks to numbered checks, proves that X(𝓛) = 0 makes the product over j vanish at every ξ with
|V(ξ)| > n̄ (the terms of X(𝓛) are nonnegative), and writes φ(ξ) as a sum over sets Π_0. 

 ### From a list of checks to numbered checks 

### `allEven_eq_fin`

 The product over the checks of a list is the product over their numbers j : Fin r; check number
j is `L.getD j ∅`. 

### `allEven_eq_range`

 The product over the checks of a list is the product over their numbers j < r. 

### `ev_nonneg`

 [q even] is at least 0. 

### `ev_le_one`

 [q even] is at most 1. 

### `allEven_nonneg`

 The product over j is at least 0. 

### `allEven_le_one`

 The product over j is at most 1. 

### `choose_mul`

 C(|A|, c)·y as a sum of y over the subsets of A with c elements. 

 ### Display (63) 

### `term_nonneg`

 The terms of X(𝓛) are nonnegative. 

### `allEven_eq_zero`

 If X(𝓛) = 0, then for every ξ with |V(ξ)| > n̄ the product over j is 0. 

### `good_of_Xsum_eq_zero`

 If X(𝓛) = 0, then every ξ with |V(ξ)| > n̄ violates an odd number of clauses of some check. 

### `eta_mul_allEven`

 If X(𝓛) = 0, then η(ξ)·∏_j [ |V_j(ξ)| even ] = [V(ξ) = ∅] for every ξ. 

### `Fsum_eq`

 If X(𝓛) = 0, then F(𝓛) is the number of ξ with V(ξ) = ∅. 

 ### Lemma 12 (Cut-off) 

### `cutoff`

 Lemma 12 (Cut-off), with implicit arguments. Hypotheses: ν ≥ 1 and M' ≥ ν − 1 + r. 

### `product`

 Display (63): if X(𝓛) = 0, then F(𝓛) is the number of satisfying assignments of Φ. 

### `emptyList`

 Step 1, «If m ≤ n̄, the empty list has X = 0». 

### `lemCutoff`

 Lemma 12 (Cut-off): for a list 𝓛 of r checks, a function φ with integer values, ν ≥ 1 and M' ≥ ν
− 1 + r, the sum of φ(ξ)·∏_j [ |V_j(ξ)| even ] over ξ is congruent modulo 2^ν to the sum of
φ(ξ)·Σ ∏_j σ_{|Π_j|}, the inner sum over the tuples with Π_j ⊆ V_j(ξ) and at most M' marks in all. 

### `xf`

 Display (65), for a list of r checks, β ≥ 1, M ≥ β − 1 + r and M ≥ n + r: Lemma 12 with (φ, ν) =
(C(|V|, n̄ + 1), β) and with (φ, ν) = (η, n + 1), and φ(ξ) written as a sum over sets Π_0 ⊆ V(ξ). 

### `residues`

 Step 1, «The residues determine the numbers»: if there are at most 2^n assignments, then 0 ≤
X(𝓛) ≤ 2^n·C(m, n̄ + 1) ≤ 2^(β − 1), where β = n + ⌈log C(m, n̄ + 1)⌉ + 1,
and 0 ≤ F(𝓛) ≤ 2^n if X(𝓛) = 0. 
