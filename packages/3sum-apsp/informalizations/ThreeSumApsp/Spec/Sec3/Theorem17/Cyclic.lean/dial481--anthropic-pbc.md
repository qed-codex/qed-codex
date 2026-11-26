---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Cyclic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Cyclic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Cyclic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The ring `ℤ[x]/(x^p − 1)` as vectors of `p` integers

The proof of Theorem 17 computes with matrices over the ring `ℤ[x]/(x^p − 1)`.  For a program an
element of the ring is the list of its `p` coefficients (`cycVec`).  This file shows that the
operations of the ring are operations on lists that use no division:

* zero, sums and differences are entrywise (`cycVec_zero`, `cycVec_add`, `cycVec_sub`);
* a power of `x` is a unit vector (`cycVec_x_pow`);
* multiplication is cyclic convolution, "O(p²) word operations" (`cycVec_mul`).  For the proof both
  factors are expanded in powers of `x` (`eq_sum_coeff`), and `x^i x^j` contributes to the
  coefficient of `x^r` exactly if `i + j ≡ r (mod p)`.


### `cycVec`

 An element of `ℤ[x]/(x^p − 1)` as the list of its coefficients of `x^0, …, x^{p-1}`. 

### `vadd`

 Entrywise sum. 

### `vsub`

 Entrywise difference. 

### `vunit`

 The vector of `x^k`, for `k < p`. 

### `cconv`

 Cyclic convolution: entry `r` is the sum of `u_i v_j` over `i + j ≡ r (mod p)`.  The index `j`
is `r - i` or `r + p - i`. 

 ## Coefficients 

### `coeff_eq_zero_of_le`

 The representative of degree less than `p` has no coefficients from `p` on. 

### `eq_sum_coeff`

 An element of the ring is the combination of the powers of `x` with its coefficients. 

### `eq_add_mod_iff`

 For `i, j, r < p`: `i + j ≡ r (mod p)` exactly if `j` is `r - i` or `r + p - i`. 

 ## Vectors 

### `length_cycVec`

 A vector has `p` entries. 

### `getD_cycVec`

 Entry `r` of the vector is the coefficient of `x^r`. 

### `cycVec_zero`

 The vector of 0. 

### `cycVec_add`

 The vector of a sum. 

### `cycVec_sub`

 The vector of a difference. 

### `cycVec_x_pow`

 The vector of a power of `x`. 

### `cycVec_mul`

 Multiplication in the ring is cyclic convolution. 
