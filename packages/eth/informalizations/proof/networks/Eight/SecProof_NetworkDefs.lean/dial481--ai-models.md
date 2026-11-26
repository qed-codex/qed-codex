---
{
  "module": "proof/networks/Eight/SecProof_NetworkDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_NetworkDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecProof_NetworkDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6 of the paper, «Proof of Theorem 2»: definitions for the sentences on the network of Φ

The words of the paragraph «Clusters, occurrences, equality tests» in which the statements of
proof/networks/Eight/SecProof_Network.lean are written: the variables that occur in Φ, the
assignments of these variables and the number of those that satisfy
Φ, the occurrences, and the equality tests. This file has definitions only; nothing is proved or
assumed here. A formula is `Paper.Formula`: a list of clauses, a clause being a list of literals
(variable, value that makes the literal
true). 

 ## The variables that occur, and their assignments 

### `occurring`

 The set of the variables that occur in Φ. A literal is a pair (variable, value that makes the
literal true). 

### `Assignment`

 An assignment of the variables that occur in Φ: one bit for each of them, and for no other
variable. 

### `Satisfies`

 The assignment a satisfies Φ: every clause has a literal (v, b) with a(v) = b. 

### `numSat`

 The number of assignments of the variables occurring in Φ that satisfy Φ. 

### `continued`

 An assignment of the occurring variables, continued by 0 to all variables. 

 ## Occurrences and equality tests 

### `occurrencesOf`

 The occurrences, for g clusters of μ clauses with k positions each: the positions (cluster,
clause of the cluster, place in the clause) that hold a literal. The paper: «An occurrence is a pair
o = (E, ω) of a clause E ∈ Φ and a
literal ω ∈ E, that is, one position of one clause.» 

### `testsOf`

 The equality tests: the pairs (o, o') of consecutive occurrences of a variable, the occurrences
of each variable being listed in reading order (`Groundwork.SatNet.Link`). The paper: «any order
will do». A test is written here as the
ordered pair with the earlier occurrence first. 

### `occurrences`

 The occurrences in Φ, when Φ is cut into g clusters of m̄ = ⌈m/g⌉ clauses with 3 positions each,
as in `Paper.networkOf g Φ`. 

### `tests`

 The equality tests of Φ, for the same clusters. 
