---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/Convolution/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Convolution-3SUM from Exact Triangle: the host

Theorem 21(a), after [VW13, Theorem 4.3]: whether an array of N integers is a yes-instance of
Convolution-3SUM is decided by asking O(√N) times whether there is a zero triangle, each time in an
instance with O(√N) vertices in each part whose weights are entries of the array, up to sign, or a
filler. c3(N, U, x, fr) computes t = ⌊√N⌋ + 1 and runs an arbitrary solver of Exact Triangle once
for each of the 2t instances, which have t vertices in each part and weights of absolute value at
most 2U + 1.  The three matrices of the current instance are written at the free pointer.  There is
no early exit.

One round writes instance s and asks the solver (`round_spec`); after s rounds the local Found says
whether one of the first s instances has a zero triangle.  By `convolution3SUM_vecOf_iff` the answer
after 2t rounds is the answer to Convolution-3SUM (`c3_spec`).  The need of the host is polynomially
bounded if the solver's is (`polyNeed_c3Need`).  The host with its time and its need is `isHost_c3`.


 ## The program 

### `Len`

 The local variables of c3: the arguments N (Len; as local 0 it also takes the result), U
(Bound), x (Input), fr (Free); then t (Side), the number s of the instance (Inst), the answer so far
(Found), the result of a call (Answer), t² (Area) and the filler 2U + 1 (Filler). 

### `c3Round`

 One round: writes instance number Inst at the free pointer and asks the solver. 

### `c3Body`

 c3(N, U, x, fr), over the procedures pET (a solver of Exact Triangle), pSqrt (the integer square
root) and pFill (convFill).  The result is returned in local 0. 

### `c3RoundTime`

 The time of one round: it writes 3t² cells and runs the solver on t vertices per part with the
bound 2U + 1. 

### `c3Time`

 The time of the host: the square root, and 2t rounds with t = ⌊√N⌋ + 1. 

### `c3Need`

 The need of the host: 3t² cells more than the solver, one level of calls more, and words for the
square root (3N + 4), the filler (2U + 1) and the indices (2t² + 2t). 

 ## One round 

### `Ctx`

 What the host assumes about the program: it begins with the solver's program and holds the two
helpers. 

### `Ready`

 What the rounds assume: the input lies below the free pointer, N < t², and the limits allow for
the need of the host, written with t. 

### `fillArgs`

 The arguments of convFill for instance number s: the three matrices follow each other at the
free pointer, and the filler is 2U + 1. 

### `inst`

 Instance number s of the reduction, at the free pointer. 

### `Hit`

 Instance number s has a zero triangle. 

### `locals`

 The local variables in round s. 

### `Ready.one_le`

 There is at least one vertex per part. 

### `Ready.input_le`

 The numbers of the input are bounded by 2U + 1. 

### `abs_filler_le`

 The filler is bounded by 2U + 1. 

### `fill_ctx`

 convFill can be called in every round. 

### `inst_pre`

 After convFill the instance lies in the memory. 

### `solver_ok`

 The limits allow for the solver, after the three matrices and one level of calls down. 

### `round_spec`

 **One round**: if Found says whether one of the instances before s has a zero triangle, then
afterwards it says so of the instances up to s.  No cell below the free pointer changes. 

 ## The host 

### `LoopInv`

 The invariant of the loop: before round s, Found says whether one of the instances before s has
a zero triangle, and no cell below the free pointer has changed. 

### `ready`

 The need of the host allows for the rounds. 

### `c3_spec`

 **The host is correct**, in every program that begins with the solver's and contains the two
helpers. 

 ## The need is polynomially bounded 

### `polyNeed_c3Need`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_c3`

 **Convolution-3SUM from Exact Triangle**: the host makes a solver of Convolution-3SUM from every
solver of Exact Triangle. 
