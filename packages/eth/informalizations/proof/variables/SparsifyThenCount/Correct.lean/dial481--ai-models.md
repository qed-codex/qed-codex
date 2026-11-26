---
{
  "module": "proof/variables/SparsifyThenCount/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/SparsifyThenCount/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Correctness of the function `ADG`

`stCorrectDG : StCorrectDG` says that the function `ADG` is right, for any family of thresholds Θ
that serves with the bound Lc on the occurrences. The width k and the formula are read from the
input (`StDecM`). If the
plan is `none`, the exponent is n and the function counts exhaustively (`StBruteC`). Otherwise the
plan says that s ≥ s0U k, that Δ = 2^β ≤ n + 1, that n ≥ 29·⌈log₂(2Δ)⌉ + 19, and that the exponent
is `needD` and at most n. The plan, its tests and the
exponent are those of the namespace `VariableBound` and do not name the thresholds, so the lemma on
them, `planAtD_some`, serves here unchanged. Three things depend on the thresholds. The bound Lc k s +
2 ≤ Δ on the clauses per variable of
a leaf comes from `StepSparsify.Serves.par`. The pad suffices for the rounds of the walk because the
tree has at most 2^(⌊n/2^s⌋+1) leaves (`StRoundsDG`). The walk starts from the formula without the
clauses that contain a variable together with
its negation, and returns the number of satisfying assignments by `StepSparsify.StWalkCountG`. Every
leaf is counted by `VariableBound.countD`, which is right by `VariableBound.StCountD`. 

### `stRoundsDG`

 A number F ≥ 2^(`VariableBound.restD` k K n s) is at least 2·2^(⌊n/2^s⌋+1) − 1, which suffices
for the rounds of the walk: ⌊n/2^s⌋ + 2 is one of the four summands of `restD`. 

### `stCorrectDG`

 The function for the bound in n, run with thresholds that serve, is right on every k-CNF, for
every k ≥ 1 and every n, when the pad has length at least 2^(eD …); given the count of a sparse
formula (`VariableBound.StCountD`), the budgets
(`VariableBound.StBudgetD`, `StRoundsDG`), the walk through the counting tree
(`StepSparsify.StWalkCountG`), the decoders and exhaustive counting. 
