---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/TimeBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/TimeBound.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/TimeBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The arithmetic of the reduction from 3SUM to Convolution-3SUM

Theorem 21(a), after [CH20, Theorem 5.1]. Two statements about the time and
the need of the host (`chTime`, `chNeed`), which are explicit expressions in the number n of
integers and the bound on their absolute values.

* The need is polynomially bounded if the need of the solver of Convolution-3SUM is
  (`polyNeed_chNeed`).
* For inputs of absolute value at most n^κ, the host's own work is n^{3/2} times a polylogarithm, it
  calls the solver polylogarithmically often, and all calls are at the same length, which is n times
  a polylogarithm, and with the same bound on the numbers, which is polynomial in n. This gives the
  transfer of running times (`claim_CH20_Theorem_5_1_of_host`).

Both are proved by following the expressions, in the calculus `Scale.SoftO` of orders of growth:
`SoftOSqrtPow F i` says that F(n) is at most a polylogarithm times (⌊√n⌋ + 1)^i, and `PolyBounded F`
that F(n, U) is at most a polynomial in (n + 1)(U + 1).


 ## The host on inputs of absolute value at most `n^k` 

### `boundAt`

 The bound `V = 2 n^k` with which the host works. 

### `ownAt`

 The host's own work. 

### `callsAt`

 The number of calls of the solver. 

### `magAt`

 The bound on the numbers of the instances that the solver is asked. 

### `chTime_eq`

 The time of the host is its own work plus the calls of the solver, which are all at one length
and with one bound. 

 ## The time functions at the bound `V = 2 n^k`

In `SoftOSqrtPow F i` the index 0 stands for a polylogarithm, 1 for `Õ(√n)`, 2 for `Õ(n)` and 3 for
`Õ(n^{3/2})`.  The bound `m` on the primes has the index 1 (`softO_mPar`). 

### `numPrimes`

 The number of candidate primes, which is at most the bound `m` on the primes. 

### `softO_numPrimes`

 The number of candidate primes is `Õ(√n)`. 

### `softO_tEmod`

 One remainder takes a step for each binary digit. 

### `softO_tResid`

 The remainders of `n` numbers. 

### `softO_tTally`

 One pass over `n` remainders. 

### `softO_tColl`

 The colliding pairs of a set of `n` numbers modulo one prime. 

### `softO_tHeavy`

 The heavy elements of a set of `n` numbers. 

### `softO_tSearch`

 One search goes through the `Õ(√n)` candidate primes, at `Õ(n)` steps each. 

### `softO_tModulus`

 The modulus of a node: two searches. 

### `softO_tNodeArray`

 The array of a node has `O(m²) = Õ(n)` cells. 

### `softO_nodeOwn`

 One call of the recursive procedure, without the call of the solver. 

### `softO_callsB`

 The recursive procedure is called polylogarithmically often for one three-set input. 

### `softO_tSetup`

 The routines params and prep cost `Õ(n)`. 

### `softO_ownAt`

 The host's own work is `Õ(n^{3/2})`. 

### `softO_callsAt`

 The host calls the solver polylogarithmically often. 

### `polyNeed_chNeed`

 **The need of the host is polynomially bounded** if the need of the solver is.  The number of
binary digits and the number of levels of the recursion are at most linear. 

### `claim_CH20_Theorem_5_1_of_host`

 [CH20, Theorem 5.1] for programs of the light language, from the host: 3SUM from
Convolution-3SUM.  For inputs of absolute value at most `n^κ` the host is taken with the parameter
`k = ⌈κ⌉`. 
