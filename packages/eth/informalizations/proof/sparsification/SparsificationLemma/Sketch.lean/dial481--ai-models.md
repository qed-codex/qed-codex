---
{
  "module": "proof/sparsification/SparsificationLemma/Sketch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Sketch.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Sketch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix C («Counting satisfying assignments as a function of n», proof sketch): the number of clauses of an output

The theorem here is the sentence of the proof sketch of Appendix C on the number of clauses of an
output of the sparsification; its docstring quotes the sentence.
The sketch is written for clauses of 3 literals and Calabro's thresholds. The theorem here holds for
every width k and all thresholds with the four conditions `ThrC`; 2·(θ 0 + … + θ (k−1)) plays the
role of M(ε) of the text.
A node is a pair x = (ψ, 𝒩); `out x` is the list 𝒩 followed by ψ, with every clause written once.
**Not here.** The sentence «Φ has Z·2^(n−v) satisfying assignments» is about the count of one sparse
formula, and the sentences on the running time are the subject of
proof/sparsification/SparsificationLemma/Mach.
The clause «there are at most 2^(εn) outputs» is `StepSparsify.outputs_le`
(proof/sparsification/SparsificationLemma/StepSparsify.lean) with k = 3.


 ### The tree 

### `clauses_le`

 «and each has at most (M(ε)+2)n clauses, as there are only 2n clauses with one literal.» For
thresholds with `ThrC`, 1 ≤ k, 1 ≤ τ, paths cut after at least (β 0 + … + β (k−1))·n steps, and 2·(θ
0 + … + θ (k−1)) as M(ε):
the formula at a leaf has at most M(ε)·n clauses, the side list, every clause written once, at most
2n, and the output at most (M(ε)+2)·n. 
