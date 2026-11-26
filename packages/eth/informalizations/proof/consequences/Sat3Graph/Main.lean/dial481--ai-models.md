---
{
  "module": "proof/consequences/Sat3Graph/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7 (the decision problems): parts of the proof

Proofs of the statements `StSets` and `StCert` of proof/consequences/Sat3Graph/Defs.lean, and a
lemma that turns a hosted decider into a decider in time O(2^{δn}).
Hosting with polynomial overhead is in Host.lean. 

### `stSets`

 **`StSets`.** Independent Set, Clique and Vertex Cover from 3-SAT, for every procedure D with an
exponent δ₃ ≥ 0 such that δ₃·(a+1) ≤ δ. 

### `stCert`

 **`StCert`.** The steps of the five deciders are polynomial time if those of D are and the
circuits are computed in polynomial time. 

### `decidesInTime_of_hosted`

 A property that a hosted decider decides is decided in time O(2^{δn}). 
