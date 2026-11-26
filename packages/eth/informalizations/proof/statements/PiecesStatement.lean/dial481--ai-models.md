---
{
  "module": "proof/statements/PiecesStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces with parameters (ρ, c), and blocks of bits (pure mathematics; definitions only; imports Mathlib only) 

### `Bits`

 A string of n bits. 

### `Four`

 A function of the four strings x, y, u, v. 

### `cross`

 [x = v][y = u]. 

### `FactorsThrough`

 Definition 1, with a bound: F(z,z') = Σ_θ f(z,θ)·f'(z',θ) over θ ∈ {0,1}^c, and all values of f
and f' are below b in absolute value. 

### `rowwise`

 A as a function of (x,y) and (u,v): «row-wise». 

### `colwise`

 A as a function of (x,u) and (y,v): «column-wise». 

 ## Pieces with parameters (ρ, c) (Definition 7): parts (a), (b) and the size bounds of (c); the running time is not stated here 

### `Family`

 The data for one λ. 

### `Family.Is`

 The family has the properties of pieces with parameters (ρ, c) at this λ. 

 ## Blocks of h positions, labels, and the mean μ (a construction that the paper does not state) 

### `Lab`

 A label β ∈ {00,01,10,11}^λ. 

### `nblk`

 ⌈n/h⌉, the number of blocks of h positions in a string of n bits. Position k lies in block k /
h. 

### `blk`

 The positions of block b. 

### `odd`

 The number of blocks b in which β has an odd number of entries 11. 

### `mu`

 μ: the mean of odd(β) over all β, rounded down. 
