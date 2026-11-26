---
{
  "module": "proof/rates/GeneralPieces/Ring/OpFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/OpFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/OpFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Display (47) of Appendix B: the operators a[r] are well defined and linear

What the appendix says with display (47) (`GeneralPieces.opFacts`): "on f ∈ V_E a term vanishes if
its positive k_i add up to more than E, so only finitely many terms are nonzero" (`nordQ_eq_zero`,
`term_eq_zero_of_Bd`, `finite_terms`); the order in which the parts of μ are listed does not matter
(`opMon_perm`); a[r] is linear in f and in a. The tool is the sum of (47) over the lists of
nonzero integers between −M and M (`opWin`): it is a[r]·f for all large M (`opMon_eq_opWin`), and
sorting its terms by the integer chosen for the first part gives a recursion (`opWin_cons`), the
form of (O2) for these finite sums. 

 ### The terms are linear in f 

### `nablaL`

 ∇_k as a linear map. 

### `termL`

 One term of (47) as a linear map. 

 ### Only finitely many terms are nonzero 

### `Bd`

 Every monomial of f has weight at most E. 

### `nordQ_eq_zero`

 "A term vanishes if its positive k_i add up to more than E." 

### `term_eq_zero_of_Bd`

 A term of (47) vanishes on f unless all k_i lie between −M and M, if the monomials of f have
weight at most E, E ≤ M and E + r ≤ M. 

### `opWin`

 The sum of display (47) over the lists of nonzero integers between −M and M. 

### `opMon_eq_opWin`

 a[r]·f is the finite sum, for all large M. 

### `exists_window`

 A window that is large enough for f and r. 

### `finite_terms`

 "So only finitely many terms are nonzero." 

 ### a[r] is linear in f 

 ### Sorting the terms by the integer chosen for the first part 

### `term_cons_neg`

 A negative integer for the first part: one more multiplication, applied last. 

### `term_cons_pos`

 A positive integer for the first part: one more differentiation, applied first. 

### `opWin_cons`

 The recursion (O2) for the finite sums. 

 ### The order in which the parts are listed does not matter 

### `nordQ_perm`

 The multiplications commute, and so do the differentiations. 

 ### a[r] for all a 

### `op_eq_sum`

 The sum that defines a[r] may run over any finite set that contains the monomials of a. 

### `opFacts`

 What the appendix says with display (47). 
