---
{
  "module": "proof/machines/StepMachines/Math/SideNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/SideNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The network of a term Z_ι of one level of the recursion, with all rows merged (tr = false) or
all columns merged (tr = true),
on words; n is the paper's λ, a part is a merged row or column, and ι is written by the digits of
the number y.
A label of the parts a < b: g blocks of n bits (the edges between nodes of the same number), then
one chunk for each of
their rectangles, in the order κ = tri i i', each of rectLen bits (coded by Code.sparse). 

### `rectDig`

 ι at the rectangle number κ of the pair of parts number p. 

### `rectLen`

 The length of the chunk of that rectangle. 

### `sideCnt_rectDig_le`

 A label of a rectangle has at most n states other than the frequent one. 

### `rectLen_le`

 A chunk has at most 3n + 1 bits. 

### `sideCuts`

 The cuts of the rectangles of the grid (of the transposed grid if tr). 

### `bell0`

 The default label of a rectangle. 

### `sideNet`

 The network of the term, with states and labels as in `rowNet`, before they are written as
words. 

### `rectC`

 The code of the labels of the rectangle number κ of the pair of parts number p. 

### `rectsC`

 The code of the labels of the rectangles of the parts a, b: their chunks one after the other. 

### `sum_pairs_tri`

 A sum over the pairs i < i' is the sum over their numbers. 

### `sideNet_c_eq`

 The capacity (number of label bits) of the parts a < b. 

### `sideNet_Θ`

 The label set of the parts a < b: the edges between nodes of the same number, and a label for
each rectangle. 

### `sideNet_Θ_empty`

 Label sets are kept at a < b only. 

### `sideCl`

 The code of the labels of two parts. 

### `sideN`

 The network on words. 

### `sideZ`

 The term Z_ι, ι written by y. 

### `ZW_eq_sum`

 On words, the value Z is the sum of the terms Z_ι over all ι, each ι written by a number y. 

### `value_sideN`

 In each term all rows or all columns are merged (Step 2 of Section 2.3): either network on words
has the value Z_ι. 

### `sideNet_sized`

 The network before words has size 2g³λ (at most 2^(2g³λ) states and 2g³λ label bits at a node),
and values of at most g·B + g²·λ bits. 

### `sideN_sized`

 The network on words has size 2g³λ, and values of at most g·B + g²·λ bits. 

### `U_sideN_row`

 The number of bits on the wires of the row network (every wire counted twice): the straight
edges (inside a row or a column),
and the cost `priceRow` of the rectangles. 

### `U_sideN_col`

 The number of bits on the wires of the column network (every wire counted twice). 

### `sideCap`

 The length of the labels of the parts a, b. 

### `sideN_c`

 The capacity of two parts is the length of their labels. 

### `sideN_lab`

 The labels of two parts are all words of that length. 

### `sideCap_le`

 Labels have at most g·λ + 2g²·λ bits. 
