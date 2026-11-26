---
{
  "module": "proof/consequences/GraphProblems/Color.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Color.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Color.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: the formula of the colorings

The satisfying assignments of `colorF k n (matrix G)` on n·k variables correspond to the proper
colorings of G with the colors 0 … k−1: the variable x_{v·k+c} is true if and only if the vertex v
has
the color c. That the entries of the matrix are the adjacencies of G is taken as a hypothesis
(`StAdj`). 

### `exists_mem_pair`

 A clause of two literals. 

### `sat_colorF`

 What `colorF k n m` says. 

### `asg`

 The assignment of a map from the vertices to the colors: x_{v·k+c} is true if and only if v has
the color c. 

### `sat_asg`

 The assignment of a proper coloring satisfies the formula. 

### `asg_injective`

 Different maps have different assignments. 

### `exists_coloring`

 Every satisfying assignment is the assignment of a proper coloring. 

### `stColor`

 The formula `colorF k n (matrix G)` has as many satisfying assignments as G has proper colorings
with k colors. 

### `stShapeColor`

 Width and variables of the formula of the colorings. 

### `stDecideColor`

 A graph can be colored with k colors if and only if its number of proper colorings with k colors
is not 0. 
