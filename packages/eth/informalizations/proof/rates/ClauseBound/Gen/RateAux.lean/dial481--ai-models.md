---
{
  "module": "proof/rates/ClauseBound/Gen/RateAux.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/RateAux.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/RateAux.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Arithmetic for the rate of the general recursion

Bit lengths of sums, products and powers; the bit length of a number below a power of X in terms of
log X; and the polynomial inequalities
between natural numbers by which lower-order quantities of one level are bounded by powers of X =
g²·(λ + B). 

 ### Bit lengths 

### `size_le_self`

 size n ≤ n. 

### `size_mul_le`

 size (a·b) ≤ size a + size b. 

### `size_add_le`

 size (a + b) ≤ size a + size b. 

### `size_two_mul_le`

 size (2·a) ≤ size a + 1. 

### `size_eight_mul_le`

 size (8·a) ≤ size a + 3. 

### `size_two_pow_mul_le`

 size (2^k·b) ≤ k + 1 + size b. 

### `size_pow_le`

 size (a^n) ≤ n·size a + 1. 

### `size_cast_le`

 If n ≤ X^k then size n ≤ k·log X + 1. 

 ### The length of an instance 

### `size_first_le`

 The bit length of the first budget, with the parts that depend on cnt and z split off. 

### `small_le_sq`

 The two small numbers of the first budget are below X², X = K·(λ + B). 

 ### Polynomial inequalities of one level 

### `four_nRect_le`

 4·(number of rectangles) ≤ g⁴. 

### `rest_le`

 What is added to z + size cnt at one level, apart from a doubling, is at most X^(c+3). 
