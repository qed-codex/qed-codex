---
{
  "module": "proof/consequences/Sat3Graph/Split.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Split.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Split.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Splitting long clauses into clauses of 3 literals with new variables

General facts used by the proofs of the statements of proof/consequences/Sat3Graph/Defs.lean.
* `splitN_spec`: for a formula x with variables below n, the formula with its long clauses split is
  a 3-CNF on n + `numFresh x` variables, no clause twice, and it is satisfiable exactly if x is.
  This is the argument of `SplitSat.stLeaf` without its bound on the number of clauses.
* The number of new variables `numFresh`: it adds up over `++`, is 0 at width 3 (from
  `Eight.Width.numFresh_le`: at most (w − 3)·(number of clauses) at width w), and striking out
  repeated clauses does not make it larger.
* `sat_iff_cntN`: a formula with variables below N is satisfiable exactly if its number of
  satisfying assignments on N variables is not 0. `cntN_of_dedup`: striking out repeated clauses
  does not change that number.
* `exists_bounds`: if the 3-CNF has N ≤ A·(n+1) variables and δ₃·A ≤ δ, then c·2^{δ₃N} steps are at
  most c'·2^{δn} steps, and states of size c·(N+2)^c have size at most c'·(n+2)^{c'}. 

### `splitN_spec`

 For a formula x with variables below n: the formula with its long clauses split has at most 3
literals per clause, variables below n + (number of new variables), no clause twice, and is
satisfiable exactly if x is. 

### `numFresh_append`

 The numbers of new variables of two formulas add up. 

### `numFresh_eq_zero`

 At width 3 there is no new variable. 

### `numFresh_dedup_le`

 Striking out repeated clauses does not make the number of new variables larger. 

### `sat_iff_cntN`

 A formula with variables below N is satisfiable exactly if its number of satisfying assignments
on N variables is not 0. 

### `cntN_of_dedup`

 Striking out repeated clauses does not change the number of satisfying assignments. 

### `exists_bounds`

 **The arithmetic of all bounds.** Let δ₃ ≥ 0 and δ₃·A ≤ δ. There is c' such that, whenever N ≤
A·(n+1) and T ≤ c·2^{δ₃N}: c·(N+2)^c ≤ c'·(n+2)^{c'} and T ≤ c'·2^{δn}. 
