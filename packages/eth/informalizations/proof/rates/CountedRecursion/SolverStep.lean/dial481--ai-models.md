---
{
  "module": "proof/rates/CountedRecursion/SolverStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverStep.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The solver at a level ℓ + 1

Proof of Theorem A (b): the set 𝓘 and the numbers d, c^row_i, c^col_i are computed once, and each of
the following takes at most Ξ^{C₃} operations: finding the numbers c_{a,a'} and the totals of both
networks for one ι; adding one Z_ι; computing d^{|ℛ|} and dividing by it.
* `pieces_ask`: what the oracle of the pieces answers to a question about strings of λ bits, 1 ≤ λ ≤
  Λ.
* `division_exact`: «d^{|ℛ|}Z = Σ_ι Z_ι», so the division at the end returns Z.
* `solverStepOf`: the statement `SolverStep` from the numbers of the level, the expansion, the
  number |𝓘|^{|ℛ|} of functions ι : ℛ → 𝓘 (called patterns here), Lemma 8 up to the call with its L
  and «whose value is that of the network», the two networks, case (ii), the crude bounds and the
  rule of substitution. 

### `pieces_ask`

 The oracle of the pieces, asked about strings of λ bits, 1 ≤ λ ≤ Λ. 

### `pieces_cap`

 The question for c^row_i or c^col_i, i the element number j of 𝓘. 

### `division_exact`

 «Thus d^{|ℛ|}Z = Σ_ι Z_ι»: the sum of the Z_ι, divided by d^{|ℛ|}, is the value of the instance. 

### `solverStepOf`

 **The solver at a level ℓ + 1.** 

### `solverStepFrom`

 `solverStepOf`, in the form of the statement `SolverStepFrom`. 
