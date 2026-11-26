---
{
  "module": "proof/machines/StepMachines/Prog/Side.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Side.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Side.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Procedures on words for the weights and the factors of the row network (tr = false) or the
column network (tr = true) of a term Z_ι
in the proof of Proposition 3 (Section 5). A part is one merged row or column. Context (c, y): the
number y encodes ι. 

 ### The weights 

### `sideChk`

 The half-edges from a node to itself are 0…0 and the edges inside the part agree. 

### `sideLabels`

 The labels at the node number i of the part a, as the state z has them. 

### `sideQuery`

 The query to the instance at the node number p.2 of the part. 

### `sideG`

 The number of nodes of a part. 

### `sideWP`

 The weight of a part: the product of the tensors' entries at its g nodes, or 0 if sideChk fails. 

### `sideWv`

 What sideWP computes. 

### `sideWP_runs`

 sideWP computes sideWv; its steps and sizes, given those of the procedure R of the instance. 

 ### The factors 

### `viewAt`

 The input of the procedure of one rectangle: the rectangle on the nodes number i, i' of the
parts a, b, seen from a. 

### `length_he_le`

 A half-edge read off any word has at most ℓ bits. 

### `sideEdges`

 The edges between nodes of the same number agree with the label. 

### `sideIsRect`

 The counter j stands for the pair i = j / g, i' = j % g; is i < i'? 

### `sideView`

 The input of the procedure of the rectangle of the counter. (i is taken modulo g; for every
counter of the loop, j < g·g,
this changes nothing.) 

### `sideNN`

 The range of the counter. 

### `sideFP`

 The factor of two parts: the product over their rectangles of the procedure cutP, or 0 if
sideEdges fails. 

### `sideFv`

 The value meant for sideFP: the product of sideItem over the counters j < g·g with j / g < j %
g, or 0 if edges is false. 
