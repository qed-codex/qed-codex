---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Primes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Primes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Primes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The primes of the window (proof of Theorem 17)

The hashing of the proof of Theorem 17 uses "a prime p ∈ [√D/2, √D)".  primes(dst, D) lists these
primes in increasing order and returns their number (`primes_spec`).

* It computes s = ⌊√D⌋ and calls the sieve of Eratosthenes, which writes all primes up to s to dst.
  The sieve gets the s + 1 cells behind these s cells for its table.
* One pass keeps the primes p with D ≤ 4p² and p² < D and moves them to the front (`pass_spec`, with
  the round `keep_spec`).  What it keeps is the list of the window (`filter_primesBelow`).


 ## The pure side 

### `InWindow`

 The number p lies in the window: √D/2 ≤ p < √D, by integer comparisons. 

### `inWindow`

 The numbers of the list L that lie in the window. 

### `filter_primesBelow`

 The primes of the window are those of the primes up to ⌊√D⌋ that lie in the window. 

### `length_primesBelow_succ_le`

 There are at most s - 1 primes up to s. 

 ## The program 

### `Dest`

 The local variables of primes: the arguments dst and D; s = ⌊√D⌋; the number of primes up to s;
the number j of those that have been looked at; the prime p that is looked at and its square; the
number cnt of primes that have been kept. 

### `primesKeep`

 The prime number j of the list is kept if it lies in the window. 

### `primesPass`

 The pass over the primes up to s; the result is the number of primes that are kept. 

### `primesBody`

 primes(dst, D), with the numbers of the procedure sqrt and of the sieve. 

### `tPrimes`

 The number of steps of primes(dst, D). 

### `Sifted`

 The first j primes of the list L have been looked at: those in the window stand at the front of
dst, the primes from number j on are still in their places, and no cell outside the list has
changed. 

### `keep_spec`

 One round of the pass. 

### `pass_spec`

 The pass keeps the numbers of the list that lie in the window, and returns how many they are. 

### `Ctx`

 What primes needs of the program: the procedures sqrt and the sieve of Eratosthenes. 

### `time_le`

 The square root, the sieve up to s, and a pass over n ≤ s - 1 primes. 

### `primes_spec`

 **primes** writes the primes of the window, in increasing order, to dst, and returns their
number.  Only the 2 ⌊√D⌋ + 1 cells from dst may change. 
