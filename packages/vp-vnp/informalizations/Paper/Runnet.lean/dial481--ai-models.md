---
{
  "module": "Paper/Runnet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Runnet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Runnet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Cutting computations": runs as networks


### `lem_runnet`

 **Paper: Lemma lem:runnet.** "Let K, T ≥ 1, let T′ ≤ T, and let an input word of at most KT′ symbols be cut into K
consecutive parts of T′ symbols, the last ones possibly shorter or empty. Order the 2K nodes: the K blocks of T steps,
then the K parts; regard the input as one more tape, written by the parts and read by the blocks. Data ρ say, for every
tape and every node, whether the node writes nothing on the tape, and otherwise the first and the last node that read
its symbols. They are valid if on every tape the first reader of a node is not before the last reader of the node
before it; a node that writes nothing repeats that last reader, so that ρ is determined by the sequence. For the first
node, the first node itself takes the place of that last reader. The value in KT steps is the sum, over boundary states
q ∈ Q^(K+1) with q₀ = q⁻ and q_K = q⁺, over valid ρ, and over the numbers of units of ℓ bits between any two nodes,
each at most (T+|S|+1)c/ℓ+1, of the values of networks on these 2K nodes; here S is the set of tapes, and symbols and
an end mark are coded by c bits. A node whose table is not 0 has at most 2((T+2K(|S|+1))c/ℓ+2K) units." Here ub is the
paper's ℓ, and the parts are consecutive parts of ℓ = T′ symbols (Cut.parts), the only cuts stated. The numbers run up
to any U0 ≥ (T+|S|+1)c/ub+1. 
