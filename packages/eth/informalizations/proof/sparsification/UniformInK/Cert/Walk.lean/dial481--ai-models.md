---
{
  "module": "proof/sparsification/UniformInK/Cert/Walk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Walk.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Cert/Walk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One step of the walk of the counting tree is polynomial-time jointly in the width k

The two children of a node of the counting tree, for the thresholds `thetaU τ` and with the width k
a function of the context, given in unary together with 2^k,
are computed in polynomial time jointly in k, τ and the node. 

### `polyT_stepCU`

 The two children of a node of the counting tree are polynomial-time jointly in k, τ and the
node, if k and 2^k are given in unary. 
