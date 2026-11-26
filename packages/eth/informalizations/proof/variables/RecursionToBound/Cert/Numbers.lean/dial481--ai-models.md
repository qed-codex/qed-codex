---
{
  "module": "proof/variables/RecursionToBound/Cert/Numbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Numbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Numbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers of Step 5 in natural numbers and lists

The definitions of proof/variables/RecursionToBound/Defs.lean follow Step 5 of Appendix D: ε =
min(a/b, 1) is rational, α = ⌈2(k−1)²·ε⁻¹·⌈log₂(32(k−1)²/ε)⌉⌉ (the paper has no ceilings), the
occurrence bound is a finite sum
and Δ is a finite supremum. A certificate of polynomial time needs them from natural numbers and
lists; this file proves the equalities, **for ALL arguments** (also k = 0, a = 0, b = 0): Theorem D (a)
needs all inputs.

* `epsOf_eq`: ε = min(a, b)/b. (For b = 0 both sides are 0, by Mathlib's convention x/0 = 0.)
* `ceil_natCast_div`: ⌈m/p⌉ = ⌊(m + p − 1)/p⌋ =: `ceilDiv m p`, for all natural numbers m and p.
  (For p = 0 both sides are 0.)
* `alphaC_epsOf`: α = `alphaN k r` = ⌈2·s·b·L / min(a, b)⌉ with L = `logN k r` = ⌈log₂ ⌈32·s·b /
  min(a, b)⌉⌉ and s = `sqPred k` = (k − 1)², which is 1 for k = 0 because the subtraction is that of
  rational numbers.
* `ceil_epsOf_mul`: ⌈ε·n⌉ = ⌈min(a, b)·n / b⌉.
* `occBound_eq`, `DeltaOf_eq`, `widthOr3F_eq`: the sum, the supremum and the width as functions of
  lists.
* `foldr_bind_max`: the maximum of a list of numbers of which some may be missing, computed from the
  right as in `needOutputsC`, is missing if one of them is, and else is the maximum of the list. 

 ### Fractions 

### `sqPred`

 (k − 1)² as a natural number, where the subtraction is that of integers: 1 for k = 0. 

### `ceilDiv`

 m/p rounded up; 0 for p = 0. 

### `logN`

 ⌈log₂ x⌉ for x = 32(k−1)²/ε and ε = min(a/b, 1), r = (a, b). 

### `alphaN`

 α = ⌈2(k−1)²·ε⁻¹·⌈log₂ x⌉⌉ for ε = min(a/b, 1), r = (a, b). 

### `ceil_natCast_div`

 The ceiling of a quotient of natural numbers, for all m and p. 

### `epsOf_eq`

 ε = min(a/b, 1) = min(a, b)/b, for all a and b. 

### `sqPred_cast`

 (k − 1)², computed in the rational numbers, is `sqPred k`. 

### `logC_epsOf`

 ⌈log₂ x⌉ of the thresholds, without fractions. 

### `alphaC_epsOf`

 **α of the thresholds, without fractions**: `Cal.alphaC k (epsOf r)` = ⌈2·(k−1)²·b·L / min(a,
b)⌉, for all k and r = (a, b). 

### `ceil_epsOf_mul`

 **⌈ε·n⌉ without fractions**: ⌈min(a, b)·n / b⌉, for all r = (a, b) and n. 

 ### Finite sets as lists 

### `sum_range_eq_list`

 A sum over the numbers below k is the sum of a list. 

### `occBound_eq`

 The bound on the occurrences as the sum of a list. 

### `sup_toFinset_eq`

 A supremum over the members of a list is the maximum of a list. 

### `DeltaOf_eq`

 The Δ of a formula as the maximum of a list. 

### `widthOr3F_eq`

 The width of Step 5 as the maximum of a list. 

 ### The maximum of numbers that may be missing 

### `foldr_bind_max`

 The maximum computed from the right, where every number may be missing: it is missing if one of
the numbers is, and else it is the maximum of the list. 

### `foldr_bind_max_of_some`

 If every number is there, so is the maximum. 

### `exists_none_of_foldr_bind_max`

 The maximum is missing only if one of the numbers is. 

### `isSome_of_foldr_bind_max`

 If the maximum is there, so is every number. 
