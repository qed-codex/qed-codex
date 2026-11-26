---
{
  "module": "proof/machines/StepMachines/Prog/Brute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Brute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Brute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Brute force for the sum Z over all labellings of the edges of the complete graph on K nodes:
`brute` computes Z, the sum over all labellings of the product of the tensors'
entries, by a loop over all labellings. A labelling is a counter y below 2^(K(K-1)/2 · λ), read as a
word and cut into
K(K-1)/2 blocks of λ bits. 

### `Inst.ZW`

 The sum Z, over all labellings of the edges, of the product of the tensors R; the labels are
words of ℓ bits, kept as plain lists. 

### `labelling`

 The labelling written by the word w. 

### `query0`

 The query at the node v: v and the labels of the edges {v,u}, u = 0, …, K-1 (d at u = v). 

### `bruteBound`

 The number of labellings. 

### `bruteQuery`

 The query sent to R at the point ((c, y), v): context c, labelling y, node v. 

### `brute`

 Brute force: the sum over all labellings of the product over the nodes of the answers of R. R
answers the queries
(context, node, labels at the node). 

### `brute_runs`

 `brute` computes Z in 2^(K(K-1)/2 · λ) · (K (t + 1) + 1) steps if R answers every query in t
steps. 

### `brute_runs_pow`

 The same with |R| ≤ 2^B and the size bound written out. 
