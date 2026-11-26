---
{
  "module": "proof/sparsification/SparsificationLemma/StepSparsify.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/StepSparsify.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/StepSparsify.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 5 of Appendix D («sparsification»)

Theorems for some sentences of Step 5 of Appendix D of the paper on the sparsification (the number
of outputs, exactly one output for each satisfying assignment, counting), in the order of the text;
each docstring quotes its sentence.
Where a theorem needs them, k ≥ 3, ε is a rational number in (0,1] and φ is a k-CNF on n variables.
The thresholds are Calabro's (proof/sparsification/SparsificationLemma/Cal/Defs.lean): α =
`alphaC k ε`, θ = `thetaC α`; paths are cut after `depthC α k n` steps.
The procedure runs on φ without the clauses that contain a variable together with its negation
(`noTaut φ`), and `Cal.sparsify` lists the outputs, one for each leaf of its tree of recursive
calls.
**Where Lean differs from the text.** The text has α = 2(k−1)²ε⁻¹·log₂ x with x = 32(k−1)²/ε, a real
number. Thresholds have to be integers, so Lean has α = ⌈2(k−1)²ε⁻¹·⌈log₂ x⌉⌉; all bounds of
the text hold for it. The text cites Calabro's dissertation for the number of leaves and for the
number of occurrences of a literal; the bounds on the number of outputs and on the occurrences of a
variable that rest on these are proved here.
The first sentence, «The change made in Appendix C … uses nothing about clauses of 3 literals», has
no theorem of its own: the statements on the change (`StExactlyOne`, `StSide`, `StUnchanged`;
proof/sparsification/SparsificationLemma/Defs.lean) hold for every width k.
**Not here.** The running time («in time 2^(εn)·n^(O(k))», «the work at a node … is polynomial») is
the subject of proof/sparsification/SparsificationLemma/Mach. The sentences on the choice of ε and
on the total time of Appendix D are not about the sparsification.
Most theorems are corollaries of `sparsABC` (the statement `Cal.SparsABC`). 

 ### The theorem that most sentences come from 

### `sparsABC`

 The theorem on sparsification with Calabro's thresholds (`Cal.SparsABC`): the outputs are k-CNFs
on the same variables without a repeated clause, there are at most 2^(εn) of them, every satisfying
assignment of φ satisfies exactly one and
no other assignment satisfies any, and in each of them every variable occurs in at most
2·(8k/ε)^(3k) + 2 clauses. 

### `one_le_alpha`

 α ≥ 1. 

 ### The number of outputs 

### `outputs_le`

 «Applied to a k-CNF on n variables and ε ∈ (0,1], the changed algorithm produces at most 2^(εn)
outputs …»; the time is in proof/sparsification/SparsificationLemma/Mach. 

 ### The formula at a node 

### `pow_le`

 «(2n+1)^k ≤ n^(2k)», for n ≥ 3. 

 ### The outputs 

### `exactly_one`

 «Each satisfying assignment of the input satisfies exactly one output, and no other assignment
satisfies any.» 

 ### Counting 

### `count_no_clause`

 «An output without clauses counts 2^n.» 

### `count_eq_sum`

 «Run Steps 2–4 on each of the … outputs and add the results»: the number of satisfying
assignments of φ is the sum of those of the outputs. 
