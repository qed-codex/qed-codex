---
{
  "module": "proof/consequences/CountKSatRate/Leaf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Leaf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Leaf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The formula of a leaf as `countM` gets it

`PaddedDescent.F.StCountM` (proof/rates/PaddedDescent/F/Interfaces.lean) asks of a formula that no
clause is empty and that every variable occurs in a bounded number of clauses. The side list of a
node of the counting tree (proof/consequences/CountKSat/Defs.lean), the set 𝒩 of Appendix C, gets
the clauses {¬ω} for the literals ω of the chosen set H at every step to the second recursive call.
Nothing proved in this development excludes that the same literal comes again and again, so
there is no such bound for the side list as it stands.
`leafM x` (proof/consequences/CountKSatRate/Defs.lean) keeps of the side list only the clauses of
one literal, each of them once. This file proves `spec`: at a leaf, as `StTreeK` describes it,
`leafM x` has at most as many clauses as `leafF x`, its clauses have 1 to k literals on variables
below n, every variable occurs in at most c + 2 of them if it occurs in at most c clauses of the
main list x.1, and it has
as many satisfying assignments on n variables as `leafF x`. 

### `mem_sideU`

 The clauses of `sideU X` are the clauses of X of one literal. 

### `length_sideU_le`

 `sideU X` is not longer than X. 

### `length_occ_sideU_le`

 A variable occurs in at most two clauses of `sideU X`: the clause v and the clause ¬v. 

### `sat_leafM_iff`

 An assignment satisfies `leafM x` exactly if it satisfies `leafF x`: the clauses left out are of
the form xᵢ ∨ ¬xᵢ. 

### `spec`

 What `PaddedDescent.F.StCountM` asks of a formula holds of `leafM x`, and its count is that of
`leafF x`. The hypotheses are what `StTreeK` says of a leaf. 
