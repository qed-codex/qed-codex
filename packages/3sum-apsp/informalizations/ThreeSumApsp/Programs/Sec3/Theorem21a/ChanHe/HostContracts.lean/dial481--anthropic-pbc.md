---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/HostContracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/HostContracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/HostContracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM from Convolution-3SUM: the memory map of core; specifications of params, prep, core

Theorem 21(a), after [CH20, Theorem 5.1].  core decides 3SUM with a solver
of Convolution-3SUM.  It first calls params, which computes the three parameters of the reduction,
and prep, which fills the arrays that the rest of core works on.  The arrays stand one after the
other from a base address `b`.  This file fixes their layout (`Map`) and the specifications of
params, prep and core.


 ## The memory map 

### `Map`

 The addresses of the arrays of core, for the base address `b`, `n` numbers, `Λ` binary digits
and primes up to `m`. 

### `Map.b`

 The base address. 

### `Map.n`

 The number of integers of the input. 

### `Map.Λ`

 The number of binary digits of a label. 

### `Map.m`

 The bound on the primes. 

### `cx`

 The block of parameters of the recursive procedure, 6 cells. 

### `pr`

 The primes, `m` cells. 

### `cnt`

 The count table, `m²` cells. 

### `srt`

 The sorted copy of the input, `n` cells. 

### `val`

 The distinct values, `n` cells. 

### `mul`

 How often they occur, `n` cells. 

### `bt`

 The binary digits of the labels, `n Λ` cells. 

### `A`

 The three sets of a splitting, `3n` cells. 

### `tw`

 The doubles of the repeated values, `n` cells. 

### `one`

 One cell that holds 0: the set {0}. 

### `top`

 The free pointer behind the arrays. 

### `layout`

 The arrays stand one after the other: each address is the one before plus the length of the
array that stands there.  A proof begins with `have hmap := a.layout`, which states the whole
map. 

 ## params 

### `ParamsSpec`

 params(n, V, out) writes `Lam V`, `mPar n V` and `fuel n` to the three cells from `out`. 

 ## prep 

### `prepNeed`

 What prep needs: the size of a word, the number of cells behind the arrays (the sieve's table
and the scratch space of sorting stand there), and the depth of calls. 

### `Prep.Ctx`

 What prep assumes about its arguments: the input `X` has `n` numbers of absolute value at most
`V` and stands below the base; `Λ` is the number of binary digits for `V`; and the limits allow for
what prep needs behind the arrays. 

### `Prep.Ctx.len`

 The input has `n` numbers. 

### `Prep.Ctx.bounded`

 They have absolute value at most `V`. 

### `Prep.Ctx.below`

 The input stands below the base. 

### `Prep.Ctx.bound_pos`

 `V` is not 0. 

### `Prep.Ctx.digits`

 `Λ` is the number of binary digits for `V`. 

### `Prep.Ctx.ok`

 The limits allow for what prep needs. 

### `Map.front`

 What the routines that run through the splittings are given, for the arrays of a map and the
distinct values `D`. 

### `PrepSpec`

 prep(n, V, Λ, m, x, b): the input `X` stands at `x`.  Fills the arrays of the map `a` with base
`b`: the primes, zeros in the count table, the distinct values `D` and how often they occur, the
binary digits of their labels, the block of parameters, and 0 in the cell `one`.  Returns the number
of distinct values. 

 ## core 

### `CoreSpec`

 core(n, V, x, b), with `V = 2U`: the input `X`, `n` numbers of absolute value at most `U`,
stands at `x`, below the free pointer `b`.  Returns 1 if three of the numbers, at different
positions, sum to 0, and 0 if not.  `T` and `r` are the time and the need of the Convolution-3SUM
solver. 
