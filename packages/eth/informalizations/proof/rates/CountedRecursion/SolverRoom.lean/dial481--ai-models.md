---
{
  "module": "proof/rates/CountedRecursion/SolverRoom.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverRoom.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/SolverRoom.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The room of the solver

«each of the following takes at most Ξ^{C₃} operations …»: here the sizes. Everything that the
solver of the level ℓ + 1 holds (ℓ, λ, B, K and g in unary; the list of 𝓘, d, the numbers c^row_i,
c^col_i; the number of a pattern; the sum of the Z_ι; the context of a call) has size at most a
power of Ξ = g²(λ + B) whose exponent depends on c only (and on the constants of the loop for K and
g and of the lemma on groupings).
* `pw_add`, `pw_mul`, `pw_num`, `pw_pow`, `pw_up`: sums, products, constants and powers of numbers
  that are at most powers of X ≥ 2.
* `room_arith`: the arithmetic, for plain numbers.
* `solver_room`: the bound for the solver. 

### `pw_add`

 A sum of two numbers that are at most powers of X ≥ 2. 

### `pw_mul`

 A product of two numbers that are at most powers of X. 

### `pw_num`

 n ≤ X^n for X ≥ 2. 

### `pw_pow`

 A power of a number that is at most a power of X. 

### `pw_up`

 A larger exponent. 

### `room_arith`

 The arithmetic of the sizes. 

 ### Sizes of numbers and lists 

### `size_of_le_two_pow`

 A number n ≤ 2^k has size at most k + 2. 

### `pow_le_two_pow`

 X^e ≤ 2^{Xe}. 

### `size_of_abs_lt`

 An integer below 2^m in absolute value has size at most m + 1. 

### `size_of_elements`

 A list of k elements, each of size below s, has size at most ks + 1. 

### `solver_room`

 **The room of the solver**, and the two small counts: one exponent for all, which depends on c,
Cn, Cg only. 
