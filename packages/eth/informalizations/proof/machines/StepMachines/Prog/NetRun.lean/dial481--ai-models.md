---
{
  "module": "proof/machines/StepMachines/Prog/NetRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetRun.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/NetRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The merging of the g nodes into K classes in the proof of Lemma 1: the program of
proof/machines/StepMachines/Prog/NetProg.lean that computes an entry of the
merged tensor of a class (a table of the clique whose nodes are the classes) computes the intended
value, with explicit bounds on the
number of steps and on the size. 

 ### Plain facts 

 ### The hypotheses of mergedM_runs, and the factors 

### `termM_runs`

 One factor of the product in an entry of the merged tensor of class G. The index i < g * g codes
the pair of nodes
(i / g, i % g); the factor is 1, a weight W, an interaction Ψ inside the class (a sum over the
labels of the pair), or a
factor f towards a node of another class. It has absolute value at most 2 ^ B. 

### `mergedM_runs`

 `mergedM` computes one entry of the tensor of class G of the merged instance, by brute force
over the states of the
members of G. Here x is a colouring in which any two classes share at most β label bits (β is the
length of the labels in
the query) and every class has at most m members. 
