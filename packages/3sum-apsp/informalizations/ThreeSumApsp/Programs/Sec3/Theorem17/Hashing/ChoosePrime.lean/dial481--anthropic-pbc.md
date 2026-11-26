---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ChoosePrime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ChoosePrime.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/ChoosePrime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The choice of the prime (proof of Theorem 17, "Hashing modulo a prime")

"We reduce the weights modulo a prime p ∈ [√D/2, √D), chosen deterministically. […] For every prime
p in the range we count the triples with S(a,b,c) ≡ 0 (mod p). […] We select the prime with the
smallest count".  Here S(a,b,c) is the weight of the triangle, the sum of its entries in the three
lists of weights ab, bc and ac, and D is the parameter of Theorem 17.

choosePrime(n, U, ab, bc, ac, D, w), where w is the address of the work area, lists the primes of
the range (`primesList D`) at w, computes the number len of binary digits of U and the numbers
K = ⌈log₂ n⌉ and 2^K (`chLevel_spec`), and goes through the primes once.  A round counts for one
prime, by a call of countPrime with the work area behind the list of the primes, and keeps the prime
if it is the first one or its count is smaller than the best so far (`chKeep_spec`,
`chRound_spec`).

On the pure side, `bestOf f L i` is the first of the first i primes with the smallest count, one
more prime changes it as the program does (`BestSoFar.step`), and at the end it is the chosen prime
(`bestOf_length`).  `choosePrime_spec` is the whole routine.


 ## The program 

### `ChNums`

 The numbers of the procedures that choosePrime calls. 

### `ChCtx`

 The program holds the procedures that choosePrime calls. 

### `Num`

 The local variables of choosePrime: the arguments n, U, ab, bc, ac, D, w; the number of primes;
len; K; 2^K; the address of the work area of countPrime; the number of the prime; the prime; its
count; the best prime so far; its count. 

### `chLevel`

 K = ⌈log₂ n⌉ and 2^K, by doubling. 

### `chKeep`

 The prime is kept if it is the first one or its count is smaller than the best so far. 

### `chRound`

 One round: the count for the prime number i. 

### `choosePrimeBody`

 choosePrime(n, U, ab, bc, ac, D, w). 

### `chooseCells`

 The number of cells that choosePrime may change, from w on: the list of the primes and the work
area of countPrime for the largest possible prime. 

### `chooseTime`

 An upper bound on the number of steps of choosePrime. 

### `ChoosePrimePre`

 What choosePrime needs: the three lists of n² weights of absolute value at most U lie below w,
the cells from w on lie in the memory, and the numbers that are formed fit in a word. 

 ## The pure side: the best prime so far 

### `countOf_nonneg`

 The count is not negative: it is a number of triples. 

### `BestSoFar`

 What the locals best and cnt hold after i primes: nothing yet, or the best prime so far and its
count c, where c q is the count for the prime q. 

### `BestSoFar.step`

 One more prime: it is kept if it is the first one or its count is smaller. 

 ## The parts of the program 

### `chFrame`

 The local variables of choosePrime during the loop over the primes. 

### `chLevel_spec`

 **K = ⌈log₂ n⌉ and 2^K.** 

### `chKeep_spec`

 **Keeping the better prime.** 

### `ChoosePrimePre.cells_le`

 The cells that choosePrime may change lie in the memory: the list of the primes, and the work
area of countPrime. 

### `ChoosePrimePre.countPre`

 What countPrime assumes holds for each prime q of the range, with the work area behind the list
of the primes, as long as only cells from w on have changed. 

### `ChInv`

 The state of choosePrime before round i: the best prime so far and its count are in their
locals, the list of the primes stands at w, and only cells from w on have changed. 

### `chRound_spec`

 **One round of choosePrime.** 

### `primes_meets`

 **primes** as a procedure. 

### `bitLen_meets`

 **bitLen** as a procedure. 

### `choosePrime_spec`

 **choosePrime** returns the first prime of the range with the smallest count (0 if the range has
no prime), and changes only cells of its work area. 

### `choosePrime_meets`

 **choosePrime** as a procedure. 
