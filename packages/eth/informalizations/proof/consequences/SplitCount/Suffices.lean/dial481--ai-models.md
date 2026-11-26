---
{
  "module": "proof/consequences/SplitCount/Suffices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Suffices.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Suffices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Corollary 6: «By the work of Dell et al. … this case suffices»

`engineBy step D`: on (n in unary, ψ), 0 if there is an empty clause; otherwise walk the tree of the
sparsification for counting, at each leaf apply the width reduction and then D, and add up; write
the sum in n + 1 bits.
`engineBy_runs`: it returns the number of satisfying assignments of ψ on n variables within c·2^{δn}
steps, on states of size at most c·M^c, for every M ≥ 1 that bounds n and the number of clauses of
ψ.
There are at most 2^{(δ/3)n} leaves, whose numbers add up (`SparsifiesPlain`), and each leaf takes
at most A·2^{(δ/3)n} steps (`leaf_runs`); the run of the walk that adds up is `CountKSat.stWalkSum`.
`stSuffices`: a formula with at most k literals per clause, variables below N and no clause twice
has polynomially many clauses, which gives `Eight.Serves`. 

### `hasNil_iff`

 There is an empty clause exactly if `hasNil` says so. 

### `engineBy_runs`

 The procedure counts: under the hypotheses of `StSuffices` there is a constant c such that, on
(n in unary, ψ) for ψ with clauses of at most k literals on x₀ … xₙ₋₁, `engineBy step D` returns the
number of satisfying assignments of ψ on n variables in n + 1 bits within c·2^{δn} steps, on states
of size at most c·M^c, for every M ≥ 1 with n ≤ M and at most M clauses in ψ. 

### `stSuffices`

 **«By the work of Dell et al. … this case suffices», for every procedure D that counts the
satisfying assignments of a 3-CNF as `CountsThree` says.** Under the hypotheses of `StSuffices`,
`engineBy step D` serves as the procedure for #k-SAT with the exponent δ. 
