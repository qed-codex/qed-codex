---
{
  "module": "proof/networks/Eight/Cor/Graph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Graph.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Cor/Graph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7: the machine for colorings on a procedure E that is a parameter

As in the paper, Corollary 7 applies Corollary 6 to formulas made from the graph. The procedure for #k-SAT
enters the proofs of proof/consequences/GraphProblems/ at two places: the machine
`GraphProblems.sized b E`, which counts the satisfying assignments with exactly s true
variables by calls of E, and the machine for colorings, one call of E. Here the machine for
colorings is proved for a procedure E that is a parameter (`color_counts`; the lines are those of
proof/consequences/GraphProblems/ColorTM.lean), and E is
then the machine of Corollary 6 on CLIQUE(ℓ) of Algorithm 1. Everything else (the formulas, their
counts, the tree for dominating sets, the readers, the host) is that of
proof/consequences/GraphProblems/ and does not use Algorithm 1 or Lemma 2.



 ### Colorings 

### `color_counts`

 The machine for colorings on a procedure E that is a parameter: the reader
`GraphProblems.readC k`, which makes (n·k in unary, the formula of the colorings), followed by one
call of E. If E serves for width max(k, 2) with the exponent δ/k, the machine returns the
number of satisfying assignments of the formula, in n·k + 1 bits, within c'·2^{δn} steps, c' = c·k^c +
c. 
