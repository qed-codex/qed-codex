---
{
  "module": "proof/variables/VariableBound/Paper/Rename/Math.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Math.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Paper/Rename/Math.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Renaming the variables that occur: the mathematics

For a formula φ over x₀ … x_(N−1) in which n variables occur, `ren φ` is φ with every variable
replaced by its position in the list `occL` of the variables that occur: a formula over x₀ …
x_(n−1).
* `toN_ren`: with natural numbers as variables, it is what the program `renL` computes.
* `isKCNF_ren`, `allOccur_ren`, `length_ren`: it is a k-CNF if φ is, all its variables occur, and it
  has as many clauses as φ.
* `numSat_ren`: its number of satisfying assignments is the number of satisfying assignments of φ,
  as assignments of the variables that occur.
* `numSat_eq`: the sentence after Corollary 11, numSat φ = 2^(N−n)·numSatOcc φ. `allOccurStmt`: if
  all variables occur, the two ways of counting agree. 

 ### The list of the variables that occur 

### `mem_occL`

 A number is in `occL ψ` if and only if it is the variable of a literal of a clause of ψ. 

### `nodup_occL`

 No number is twice in `occL ψ`. 

### `val_mem_occL`

 The variables in the list, for a formula over x₀ … x_(N−1), are those that occur. 

### `exists_of_mem_occL`

 Every number in the list is a variable of φ that occurs. 

### `pos0`

 The position of a variable that occurs. 

### `pos0_bijective`

 The position is a bijection from the variables that occur to the positions of the list. 

### `length_occL`

 The length of the list is the number of variables that occur. 

### `pos`

 The renaming: a bijection from the variables that occur to 0, …, n − 1. 

### `val_pos`

 The new name of a variable is its position in the list. 

 ### The renamed formula 

### `ren`

 φ with the variables that occur renamed to 0, …, n − 1. 

### `toN_ren`

 With natural numbers as variables, the renamed formula is what the program computes. 

### `length_ren`

 The renamed formula has as many clauses as φ. 

### `map_back`

 Putting the old names back: the inverse of the renaming on clauses all of whose variables are in
the list L. 

### `isKCNF_ren`

 If φ is a k-CNF, so is the renamed formula. 

### `sat_ren_iff`

 An assignment a of x₀ … x_(n−1) satisfies the renamed formula if and only if the assignment «a
at the new name» of the variables that occur satisfies φ. 

### `allOccur_ren`

 All variables of the renamed formula occur. 

### `numSat_ren`

 The number of satisfying assignments of the renamed formula is the number of satisfying
assignments of φ, as assignments of the variables that occur. 

 ### The sentence after Corollary 11 

### `numOcc_le`

 At most N variables occur in a formula over x₀ … x_(N−1). 

### `card_not_occurs`

 The number of variables that do not occur. 

### `numSat_eq`

 The sentence after Corollary 11: for a formula on N variables of which n occur, the number of
satisfying assignments of all N variables is 2^(N−n) times the number of satisfying assignments as
assignments of the n variables that occur. 

### `allOccurStmt`

 If all variables occur, n is the number of all variables, and the number of satisfying
assignments, as assignments of the variables that occur, is `SatK.numSat`. 
