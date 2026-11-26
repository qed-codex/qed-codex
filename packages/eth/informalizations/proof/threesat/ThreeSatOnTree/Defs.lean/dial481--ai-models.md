---
{
  "module": "proof/threesat/ThreeSatOnTree/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatOnTree/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatOnTree/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The machine for 3-SAT that walks the recursion tree of a sparsification procedure: definitions

`satC τ Mc` is the machine `satMK` of proof/consequences/WidthK/Top/Sat.lean at width 3, on the tree
of a sparsification procedure in the style of Appendix C, with thresholds of this development, θ 0 =
1, θ i = 4·τ^(2i−1) (`UniformInK.thetaU τ`): decode the input, answer «no» if there is an empty
clause, walk the tree depth first, and test the formula ψ at every leaf with the machine `Mc`.
This file has definitions only. 

### `satC`

 The machine for 3-SAT on the tree of Appendix C with parameter τ: decode the input, walk the
tree, test every leaf with `Mc`. 
