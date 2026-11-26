---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Contracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Contracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Contracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26 and 31 in the light language: procedure numbers, time functions and interfaces

Proof of Corollary 26: "Setting up. Let m := ⌈log₄ D⌉, and pad the inner dimension to 4^m < 4D with
zero columns of X and zero rows of Y." Proof of Corollary 31: "We repeat the proof of Corollary 26
with L := ⌈cm⌉ and t := ⌈θm⌉"; "for smaller m the corollary again holds trivially". Here a query
then computes an inner product, which takes a bounded number of steps since D is bounded.

The routines are relocatable: they receive the addresses of X and Y and a free pointer fr. From fr
on they use

    flag (1) | b0 (1) | 4^m (1) | X' (N 4^m) | Y' (4^m N) | the block of Theorem 30 from b0 on

flag = 1 says that the data structure of Theorem 30 has been built for the padded matrices X', Y';
flag = 0 that m is below the threshold m₀ (a constant of the program text) and that queries compute
inner products. Nothing is assumed about the cells from fr on.


 ## Time functions 

### `tPadX`

 For each row: a copy, a fill, and the arithmetic of the addresses. 

 ## The small routines 

### `CopySpec`

 copy(src, dst, n). 

### `FillSpec`

 fill(dst, n, x). 

### `Log4Spec`

 log4(D, a) returns m = ⌈log₄ D⌉ and writes 4^m to the cell a. 

### `PadXSpec`

 padX(N, D, D', aX, aX') writes X, padded with zero columns to D' columns, to aX'. 

### `IpAtSpec`

 ipAt(I, J, N, D, aX, aY) returns (XY)[I, J] as an inner product. 

 ### copy and fill are those of the library 

 ### ⌈log₄ D⌉ 

### `Dim`

 The locals of log4: the argument D, which the result replaces; the address a; the power of 4;
and its exponent. 

### `log4Body`

 log4(D, a): multiply by 4 until D is reached; store the power at a and return the exponent. 
