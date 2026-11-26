---
{
  "module": "proof/variables/PairsToBound/Width.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Width.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/Width.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The width of Step 6, and the number of clauses

**The sentences answered** (Step 6 of Appendix D). «As in Step 5, k is the largest number of
literals in a clause, or 3 if that is larger, which multiplies k² by at most 9.» «… as there are
fewer than (2n+1)^k ≤ n^(2k) clauses …»

**What is proved.** `widthOr3Stmt : WidthOr3Stmt`: the number `widthOr3 φ` is at least 3; a formula
φ without a repeated clause is a k-CNF for k = `widthOr3 φ`; and if φ is a k-CNF for some k ≥ 1,
then `widthOr3 φ` ≤ max(k, 3) and its square is at most 9k².
`clauseCountPowStmt : ClauseCountPowStmt`: (2n+1)^k ≤ n^(2k) for n ≥ 3.

**How.** `widthOr3 φ` is the largest number in a list, computed from the right with the start value 3.
Three lemmas on such a maximum (it is at least the start value, at least every member, and at most
every common upper bound) give the first statement; max(k, 3) ≤ 3k for k ≥ 1 gives the factor 9.
The second statement is a sentence of Step 5 too and is taken from there
(`SparsificationLemma.StepSparsify.pow_le`). 

 ### The largest number of a list, with a start value 

### `start_le_foldr_max`

 The maximum of a list, computed from the right with the start value a, is at least a. 

### `mem_le_foldr_max`

 The maximum of a list, computed from the right with any start value, is at least every member of
the list. 

### `foldr_max_le`

 A number that is at least the start value and at least every member of the list is at least the
maximum. 

 ### The width 

### `three_le_widthOr3`

 The width of Step 6 is at least 3. 

### `length_le_widthOr3`

 No clause has more literals than the width of Step 6. 

### `widthOr3_le_max`

 If no clause of φ has more than k literals, the width of Step 6 is at most max(k, 3). 

### `widthOr3Stmt`

 «k is the largest number of literals in a clause, or 3 if that is larger, which multiplies k² by
at most 9.» 

 ### The number of clauses 

### `clauseCountPowStmt`

 «(2n+1)^k ≤ n^(2k)», for n ≥ 3. 
