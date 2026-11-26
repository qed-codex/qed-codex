---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Martingale.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Martingale.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Martingale.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One decision does not change the potential on average

A state consists of the checks chosen so far and of the set D of the clauses that are not yet
decided for check j. One decision takes a clause e out of D and either puts it into check j or
leaves it out. For each of the four terms of the potential, p times the value after «in» plus 1 − p
times the value after «out» is the value before the decision. In the first term only the ξ
that violate e count; in the second the numerator changes by 1 − p or by −p; in the third only the
summand of check j, and in the fourth only the summand of e, changes: it is multiplied by
2/(1 + p) or by 1/(1 + p). 

 ### The check after «in», and small facts 

### `putIn_same`

 After «in», check j has the clause e in addition. 

### `putIn_ne`

 After «in», the other checks are as before. 

### `one_add_pr_ne`

 1 + p ≠ 0. 

### `notMem_of_mem`

 A clause that is not yet decided for check j is not in check j. 

### `card_eq_succ`

 D has one clause more than D without e. 

### `average`

 2p + (1 − p) = 1 + p, with the common factor x/(1 + p)^{k+1}. 

 ### The four terms 

### `upar`

 One decision, first term. 

### `sum_card_putIn`

 After «in», the checks have one pair more. 

### `undRow_self`

 For check j the clauses of D are not yet decided. 

### `undRow_ne`

 For the other checks D does not matter. 

### `sum_undRow`

 Before the decision, one pair more is not yet decided. 

### `uinc`

 One decision, second term. 

### `urow`

 One decision, third term. 

### `card_col_putIn_self`

 After «in», the clause e is in one check more. 

### `card_col_putIn_ne`

 After «in», the other clauses are in the same checks. 

### `ucol`

 One decision, fourth term. 

 ### The potential 

### `martingale`

 One decision: p·Υ^in + (1 − p)·Υ^out = Υ. 
