---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Parameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Parameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Parameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The parameters of the reduction from 3SUM to Convolution-3SUM

Theorem 21(a), after [CH20, Theorem 5.1].  params(n, V, out) computes the
three parameters of the reduction for n numbers of absolute value at most V: the number Λ =
⌊log₂(2V)⌋ + 1 of binary digits (`ChanHe.Lam`), the bound m on the primes (`ChanHe.mPar`), and the
number of levels of the recursion tree (`ChanHe.fuel`).  The program follows the definitions of the
three numbers line by line, so the proof (`params_spec`) only has to check that each intermediate
value fits in a word: each is at most a small multiple of V, of m or of n + 2 (first section).


 ## The sizes of the intermediate values 

 ## The program 

### `Len`

 The locals of params.  The arguments: the number n of integers, the bound V on their absolute
values, and the address of the three cells for the results.  Then, in the order in which they are
computed: ⌊log₂(2V)⌋; Λ; ⌊√n⌋; w + 1 with w = 5Λ(⌊√n⌋ + 1); ⌊log₂(w + 1)⌋; m; ⌊log₂ n⌋;
⌈log₂(⌊log₂ n⌋ + 2)⌉; the number of levels. 

### `paramsBody`

 params(n, V, out), over the procedures pLog2, pClog2 (logarithms, rounded down and up) and pSqrt
(the integer square root): writes Λ, m and the number of levels to the three cells from out. 

### `params_spec`

 **params** meets its specification. 
