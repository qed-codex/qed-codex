---
{
  "module": "proof/machines/StepMachines/Prog/GridDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/GridDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/GridDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One level of the recursion as a program, the boundary between the loop over the patterns and the
two networks of a term:
patterns ι ∈ {0,…,λ}^R as numbers y < (λ+1)^R, where R = C(g,2)² is the number of rectangles (the
digits of y in base λ+1
are the numbers ι_q); what the rectangles cost in the row and in the column network; and what the
loop needs of the two
networks. 

 ### Patterns as numbers, and what a rectangle costs 

### `nRect`

 R = C(g,2)², the number of rectangles of the g × g grid. 

### `digit`

 ι_q, the digit number q of the counter y in base n + 1. 

### `tb`

 The number of binary digits of 3^c: enough to write any number below 3^c (for c ≥ 1 no fewer
will do; tb 0 = 1, one bit to
spare). 

### `capW`

 The number of bits of the name of a string of n symbols out of four of which at most c differ
from a fixed one:
n bits for the set of these positions, then one number below 3^c. 

### `priceRow`

 What the rectangles cost in the row network of the pattern y (strings with at most n − ι_q
symbols other than the
singlet). Every rectangle counts twice, since `Network.U` sums over ordered pairs of nodes. 

### `priceCol`

 What the rectangles cost in the column network of the pattern y (strings with at most ι_q
symbols other than Φ⁺). 

### `min_price_le`

 The cheaper total is at most the average: at most ρ·g⁴λ + g⁴/2 bits. 

 ### The boundary between the loop and the two networks 

### `PNet.Presents.mono`

 Presents is monotone in the bounds. 

### `NetFormer`

 From the length function and the procedure of an instance on g² nodes, a network on g nodes
given by procedures,
in the contexts (c, y), y the pattern. 

### `SideNet`

 The row or the column network, with bit strings as states and labels, as a function of λ, of the
instance and of the
pattern y. 

### `BoundedInst`

 The entries of Rm are at most 2^B in absolute value at the queries that are asked: labels of
length n, the empty word at
the node itself. 

### `sum_digits`

 The counters y < (n+1)^R are the patterns: summing over y is summing over all families of R
digits. 
