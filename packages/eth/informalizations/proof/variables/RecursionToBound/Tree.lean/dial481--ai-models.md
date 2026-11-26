---
{
  "module": "proof/variables/RecursionToBound/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the tree, its outputs, and the input

Four statements of proof/variables/RecursionToBound/Defs.lean are proved here.
* `walkTreeIsSparsify`. The tree that `countAll` walks starts with the n clauses xᵢ ∨ ¬xᵢ on the
  side list; the outputs do not change if it starts with the empty side list
  (`SparsificationLemma.stOutputsSame`). By `SparsificationLemma.Cal.factI` the procedure has
  stopped on every path after `Cal.depthC` steps, a bound computed from Calabro's thresholds, so
  cutting the paths later gives the
  same leaves (`StepSparsify.leaves_eq_of_le`).
* `outputsAreFew`. ε = min(r, 1) lies in [e, 2e] and is at most 1, because e ≤ r ≤ 2e and e ≤ 1; the
  bound 2^(εn) on the number of outputs is `SparsificationLemma.StepSparsify.outputs_le`.
* `ownDeltaIsBounded`. The general theorem on the sparsification at Calabro's thresholds
  (`SparsificationLemma.Cal.gen`) says that a variable occurs in at most 2·(θ₀ + … + θ_(k−1)) + 2
  clauses of an output; Δ is the larger of 2 and the largest of these numbers.
* `widthOnTheCode`. The reader gives n and the clauses back (`ClauseBound.Alg.Decode.stDecM`);
  clauses keep their lengths; and `Q.pick` at ⌊n^(1/17)⌋ gives the level of n
  (`VariableBound.VariablesA.pick_eq`, `VariableBound.VariablesA.level_eq_pick`).
Correct.lean uses the lemmas on ε in the namespace `RecursionToBound.Eps`. Numbers.lean has lemmas
of the same kind under other names (`epsOf_pos`, `epsOf_le_one`, `epsOf_cast`), which Exponent.lean
uses. 

 ### The number ε 

### `pos`

 ε is positive if numerator and denominator of r are. 

### `le_one`

 ε ≤ 1. 

### `cast`

 ε as a real number: min(r, 1). 

### `pos_of_le`

 If 0 < e ≤ r, then numerator and denominator of r are positive. 

### `one_le_alpha`

 α ≥ 1 for k ≥ 3 and 0 < r. 

 ### The tree and its outputs 

### `walkTreeIsSparsify`

 The outputs at the leaves of the tree that `countAll` walks are the outputs of
`SparsificationLemma.Cal.sparsify`. 

### `outputsAreFew`

 «… each of the at most 2^(2en) outputs», and e ≤ ε ≤ 2e, ε ≤ 1. 

### `ownDeltaIsBounded`

 In every output a variable occurs in at most `occBound k r` clauses, so the Δ of the output is
at most this number. 

 ### What the function reads from the code of (k, φ) 

### `widthOr3F_toN`

 «the largest number of literals in a clause, or 3» can be read from the formula with natural
numbers as variables. 

### `widthOnTheCode`

 On the code of (k, φ) the function reads this k, the number for the level of n, and the index of
that level. 
