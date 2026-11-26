---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/ChanHe/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a), the reduction of Chan and He: inputs of absolute value at most n ^ κ

From n integers bounded by a power of n, the reduction after [CH20, Theorem 5.1] computes
polylogarithmically many arrays of length Õ(n), in Õ(n^{3/2}) time.  This file puts `n ^ κ` for the
bound `U` on the input and proves the three bounds, the last one for the count `scanPairs` in place
of a running time.

* The numbers have `Lam (2 n^κ) = O(log n)` binary digits (`Lam_pow_le`).  So the bound `mPar` on
  the primes is `√n` times a polylogarithm (`softO_mPar`).
* The reduction is correct (`threeSum_iff_exists_convolution3SUM`), there are at most `numBound κ n`
  instances (`length_instances_pow_le`) with entries of absolute value at most `120 n^κ + 40`
  (`abs_instances_pow_le`), and the searches look at no more than `workBound κ n` pairs
  (`scanPairs_pow_le`).
* `numBound κ n` is a polylogarithm, the length `lenOf κ n` of the instances is `n` times a
  polylogarithm, and `workBound κ n` is `n^{3/2}` times a polylogarithm (`isPowPolylog_numBound`,
  `isPowPolylog_lenOf`, `isPowPolylog_workBound`).  These three bounds and `softO_mPar` follow the
  definitions of the parameters through the calculus `SoftOSqrtPow`.


 ## The parameters 

### `Lam_pow_le`

 `Lam (2 n^κ) ≤ κ(⌊log₂ n⌋ + 1) + 3`. 

### `softO_Lam`

 The number of binary digits is a polylogarithm. 

### `softO_wPar`

 The number of primes that we want to choose from is `√n` times a polylogarithm. 

### `softO_mPar`

 **The bound on the primes is `√n` times a polylogarithm.** 

### `one_le_lenOf`

 The instances are not empty arrays. 

 ## Correctness, the number of instances, their entries, and the count for the searches 

### `length_instances_pow_le`

 **The number of instances is at most `numBound κ n`.** 

### `scanPairs_pow_le`

 **The searches look at no more than `workBound κ n` pairs.**  This bounds the count
`scanPairs`, which we define; it is not a running time. 

### `abs_instances_pow_le`

 **The entries of the instances have absolute value at most `120 n^κ + 40`.** 

### `convolution3SUM_iff_convOne`

 `Convolution3SUM` on the first `N` cells of an array `y : ℕ → ℤ` is the problem
`ConvOne N y`. 

### `threeSum_iff_exists_convolution3SUM`

 **The reduction is correct**: three of the numbers, at different positions, sum to 0 iff one of
the instances, read at the length `lenOf κ n`, is a yes-instance of Convolution-3SUM. 

 ## The three bounds in asymptotic form 

### `softO_numBound`

 The bound on the number of instances, in the calculus. 

### `isPowPolylog_numBound`

 The bound on the number of instances is a polylogarithm. 

### `isPowPolylog_lenOf`

 The length of the instances is `n` times a polylogarithm. 

### `isPowPolylog_workBound`

 The bound on the number of pairs that the searches look at is `n^{3/2}` times a polylogarithm.
It bounds a count of pairs, not a running time. 
