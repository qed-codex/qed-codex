---
{
  "module": "proof/sparsification/UniformInK/Tree/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Tree/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Tree/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The counting tree for the geometric thresholds: definitions and interface statements

The counting tree of `stepC (thetaU τ) k` for width k with the thresholds `thetaU τ`: the bound
`stackLenCU` on the length of the word of a state, and the statements `StTreeU` and `StStateLenU`.
This file has definitions only. The statements `St…` are propositions. 

### `stackLenCU`

 An upper bound for the length of the word of a state (a stack of nodes and a number): at most
bsumU τ k · n + 1 nodes, each a formula of at most 2^k·m clauses of at most k literals and a side
list of at most 2n clauses of at most 2 literals, all on variables below n; and a number below
2^(n+1). 

### `StTreeU`

 The sparsification lemma for counting at width k ≥ 1, for τ ≥ k² and τ ≥ 8k, for the tree of
`stepC (thetaU τ) k` of depth bsumU τ k · n: a bound on the number of leaves, the shape of the
leaves,
the count of ψ as the sum of the counts of the leaves, and bounds on the stacks of the rounds. 

### `StStateLenU`

 The word of a state, a stack of at most bsumU τ k · n + 1 nodes of bounded size and a number
below 2^(n+1), has length at most `stackLenCU k τ n m`. 
