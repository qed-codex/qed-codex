---
{
  "module": "proof/sparsification/SparsificationLemma/Cal/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Cal/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The theorem on sparsification with Calabro's thresholds, parts (a), (b), (c)

This file proves `SparsABC` of proof/sparsification/SparsificationLemma/Cal/Defs.lean. It takes as
hypotheses four statements proved in other files: `StAlpha` and `StDegLe` (Cal/Alpha.lean), `StYLe`
(Cal/Real.lean), and `StNodup` (Side.lean: no output has a clause twice).
The procedure runs on φ without the clauses that contain a variable together with its negation; this
formula is a k-CNF with the same satisfying assignments (`stNoTaut`).
(a) By `factIIIy` there are at most 2^(yn) outputs, and y ≤ ε by `StYLe`, whose hypotheses on x and
    α are in `StAlpha`. (b) is `stExactlyOne`, which holds for all thresholds. (c) By `gen` a
    variable occurs in at
most 2·(θ₀ + … + θ_{k−1}) + 2 clauses of an output, where the θ_i are the thresholds `thetaC`; the
sum is at most 2 + 4α·(32α)^(k−2) by `stDegSum`, and this is at most (8k/ε)^(3k) by `StDegLe`. 

### `sparsABC`

 The sparsification statement `SparsABC`, parts (a), (b), (c) (the changed algorithm of Appendix
C with Calabro's thresholds; the bounds used in Step 5 of Appendix D), from `StNodup`, `StAlpha`,
`StYLe` and `StDegLe`. 
