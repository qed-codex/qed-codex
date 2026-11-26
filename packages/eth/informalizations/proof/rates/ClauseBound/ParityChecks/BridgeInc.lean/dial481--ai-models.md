---
{
  "module": "proof/rates/ClauseBound/ParityChecks/BridgeInc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/BridgeInc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/BridgeInc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The three layers at one assignment

An assignment σ of n + r variables is a pair (ξ, y): ξ assigns the n variables of ψ and y the r
dummy variables of the checks. For each of the three layers of clauses, the number of clauses of the
layer that σ violates is the number of elements of a finite set: the clauses of ψ that ξ violates
(first layer); the incidences that (ξ, y) violates (second layer); the clauses of ψ from number t on
that ξ violates (third layer). 

 ### Counting in lists 

### `countP_drop`

 The number of members from position t on with a property, as the number of their positions. 

### `countP_idx`

 The number of members with a property of a list of numbers below m without repetition, as the
number of elements of a subset of Fin m. 

 ### The two parts of an assignment 

### `xi`

 The assignment of the variables of ψ. 

### `yy`

 The assignment of the dummy variables. 

### `vio_ext`

 A clause in the variables of ψ sees only ξ. 

### `vio_getD`

 The same for the clause number e of ψ, whatever e. 

### `vio_append`

 A clause with the dummy literal of check j added is violated if and only if the clause is
violated and the dummy variable is 1. 

 ### The first and the third layer 

### `nvio_drop`

 The clauses from number t on that σ violates. 

### `nvio_all`

 The clauses that σ violates. 

 ### The second layer 

### `cnt`

 The number of clauses of check j that τ violates. 

### `nvio_incL_sum`

 The incidences that τ violates, check by check. 

### `wf_getD`

 Every check, and the empty list beyond the last check, is a list without repetition of numbers
of clauses. 

### `cnt_eq`

 The number of clauses of check j that σ violates, as the number of elements of a set. 

### `J1`

 The checks before j. 

### `J2`

 The check j. 

### `sum_checks`

 A sum over the checks, with the checks before j counted if their dummy variable is 1. 

### `nvio_incL`

 The incidences of the checks before j and of check j that σ violates. (For j = r there is no
check j.) 

### `cnt_take`

 The checks before j, cut out of the list of all checks. 

### `nvio_incL_take`

 The incidences of the checks before j that σ violates. 

 ### Products over the checks 

### `prod_J1`

 A product over the checks before j. 

### `prod_J2`

 A product over the one check j. 
