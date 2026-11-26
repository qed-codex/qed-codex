---
{
  "module": "proof/rates/ClauseBound/Boson/Size.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Size.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Size.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Sizes of the entries of the matrices

The entry of the matrix of a[r] at monomials t^π, t^σ of weight at most W (the coefficient of t^π in
a[r] t^σ), for a monomial a with parts at most W, is at most 2^{(4W+1)·(number of parts of a)} in
absolute value
(`abs_op_le`). The proof is an induction on the list of the parts. One step of the recursion is a
sum over the different parts l of π, of which there are at most W + 1, and a sum
over the different parts k of σ with the factors k·(number of parts equal to k), which add up to the
weight of σ. All binomial coefficients that occur are at most 2^{2W}. So one
step multiplies the bound by at most (2W + 1)·2^{2W} ≤ 2^{4W+1}. 

### `abs_bet_le`

 |C(r − 1, n − 1)| ≤ 2^{2W} for n ≤ W and |r| ≤ W. 

### `le_sum_of_mem`

 A part of a monomial is at most its weight. 

### `sum_erase_le`

 Taking a part away does not raise the weight. 

### `card_toFinset_le`

 A monomial of weight at most W has at most W + 1 different parts. 

### `sum_mul_count`

 The weight of a monomial is the sum of k·(number of parts equal to k). 

### `abs_nop_le`

 One step of the recursion multiplies a bound B for the entries by at most 2^{4W+1}. 

### `abs_op_le`

 If all weights and parts are at most W, an entry of the matrix of a[r] is at most
2^{(4W+1)·(number of parts of a)} in absolute value. 
