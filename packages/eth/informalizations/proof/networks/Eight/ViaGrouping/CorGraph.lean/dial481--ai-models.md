---
{
  "module": "proof/networks/Eight/ViaGrouping/CorGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorGraph.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/CorGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7: proper colorings, from a procedure for #k-SAT that is a parameter

As in the paper, Corollary 7 applies Corollary 6 to formulas made from the graph.
proof/networks/Eight/Cor/Graph.lean proves the places at which the procedure for #k-SAT enters for a
procedure E that is a parameter (among them `Eight.color_counts`).
This file draws two steps towards Corollary 7 from a family of such procedures:
* `EngineCounts En` (proof/networks/Eight/ViaGrouping/CorDefs2.lean) says of a family of machines En
  k ℓ τ what Corollary 6 for machines cut into steps says: for every k ≥ 1 and δ > 0 some En k ℓ τ
  has polynomial-time steps and serves as the procedure for #k-SAT with the exponent δ;
* `COLOR_counts_of`: the machine of Corollary 7 that counts proper colorings, with the procedure
  named, En k ℓ τ;
* `stEngine_of`: from `EngineCounts En`, the statement `Eight.StEngine`, in which the procedure is
  left open.
The proofs in this file name no algorithm for cliques or for networks. 

### `stEngine_of`

 `EngineCounts En` gives Corollary 6 for machines cut into steps with the machine left open
(`Eight.StEngine`). 

 ### Colorings 

### `COLOR_counts_of`

 **Counting the proper colorings, with the procedure named.** For every k ≥ 1 and δ > 0 there are
a level ℓ and a threshold parameter τ such that the reader `readC k` followed by `En (max k 2) ℓ τ`
has polynomial-time steps and returns, on the code of a graph G on
n vertices, the number of proper colorings of G with k colors in n·k + 1 bits, within c·2^{δn}
steps. 
