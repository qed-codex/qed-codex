---
{
  "module": "proof/machines/StepMachines/Math/SideX.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideX.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideX.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The weights and the factors of the network `sideN`, in explicit form: what the procedures have
to compute. `sideN` is
the network of one term Z_ι of the expansion in the proof of Proposition 3 (Section 5), with all
rows or all columns (the parts) merged, that is, the row or the column network there; its states and
labels are words of bits. 

### `sideN_W`

 The weight of the part a at a state z: the product of the tensor entries of its g nodes (0
unless the slot of a node
for itself is all zeros), times the tests that the two ends of every edge inside a agree. 

### `sideChunk`

 The chunk of the rectangle number κ in the label θ of the parts a, b; the first g * n bits of θ
belong to the g edges
between nodes of equal number. 

### `sideItem`

 The factor of the rectangle on the nodes number i < i' of the parts a, b, on the side of a: z is
the state of a and
θ the label. 

### `side_core`

 Both factors of two parts a < b at once: o is the other part, top says which of the two parts of
the cuts is taken. 

### `sideN_f`

 The factor of the parts a ≠ b on the side of a: the tests on the g edges between nodes of equal
number, times the
factors `sideItem` of the rectangles. 
