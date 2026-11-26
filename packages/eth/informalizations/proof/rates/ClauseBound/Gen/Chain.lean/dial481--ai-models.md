---
{
  "module": "proof/rates/ClauseBound/Gen/Chain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Chain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Chain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The general recursion: the smaller total of one level

For pieces with parameters (ρ, c) (Definition 7) and a pattern, that is, a choice of one piece for
every rectangle of the grid, the two prices (the bits that the rectangles contribute to the total of
the row network and to that of the column network) add up to at most twice the number of rectangles
times the largest sum of the two caps of a piece (its numbers of bits row-wise and column-wise). So
on a g×g grid the cheaper of the row network and the column network costs at most the average of the
two,
which is at most g(g−1)gλ plus the number of rectangles times that largest sum, as in the bound on
the smaller total in the proofs of Proposition 3 and Theorem A. 

### `price_add_le`

 The sum of the two prices of a pattern is at most twice the number of rectangles times the
largest sum of the two caps of a piece. 

### `total_min_le`

 On a square grid the cheaper of the two networks of a pattern costs at most the average. 
