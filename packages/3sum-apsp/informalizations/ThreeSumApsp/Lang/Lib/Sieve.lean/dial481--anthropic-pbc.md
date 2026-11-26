---
{
  "module": "ThreeSumApsp/Lang/Lib/Sieve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Sieve.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Lib/Sieve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The sieve of Eratosthenes

sieve(m, out, fr) writes the primes up to m in ascending order to the cells from out and returns
their number (`sieve_meets`).  It uses a table of m + 1 cells at the free pointer fr, about which
nothing is assumed.

* The table is cleared (`clear_ends`).
* The candidates i = 2, …, m are tried in turn (`round_ends`).  Before the round for i, cell fr + j
  holds 0 unless j is a proper multiple of a prime below i (`Sieved`, `Marked`); so i is a prime if
  and only if cell fr + i holds 0 (`prime_iff_not_marked`).
* A prime is appended to the list, and its proper multiples are marked (`take_ends`, `mark_ends`).

The number of steps, `sieveTime m`, is of the order m log m: a prime i costs m / i rounds of
marking, and the sum of m / i over all i ≤ m is at most m (⌊log₂ m⌋ + 1) (`sum_div_le`, `time_le`).

Everything but `sieveBody`, `sieveTime` and `sieve_meets` is in the namespace `Sieve`.


 ## The pure side 

### `primesBelow`

 The primes below c in ascending order. 

### `length_primesBelow_add_two_le`

 There are at most i - 2 primes below i. 

### `sort_primesLE`

 The list is the sorted list of the set of primes up to m. 

### `Marked`

 The number j is a proper multiple of a prime below c. 

### `prime_iff_not_marked`

 A number from 2 on is prime if and only if it is not a proper multiple of a smaller prime. 

### `sum_div_pow_le`

 The sum of m / i over 1 ≤ i < 2^k is at most k m. 

### `sum_div_le`

 The sum of m / i over 2 ≤ i ≤ m is at most m (⌊log₂ m⌋ + 1). 

 ## The program 

### `Bound`

 The local variables of sieve: the arguments m, out and fr, the candidate i, a multiple J of i,
and the number cnt of primes found. 

### `clear`

 Clearing the table: the cells fr, …, fr + m become 0. 

### `mark`

 Marking the proper multiples 2 i, 3 i, … of i. 

### `take`

 The candidate i is a prime: it is appended to the list, and its proper multiples are marked. 

### `round`

 The round for the candidate i, which is a prime if its cell of the table holds 0. 

### `_root_.Light.sieveBody`

 sieve(m, out, fr). 

### `_root_.Light.sieveTime`

 The time of sieve. 

### `Pre`

 What sieve asks of the limits and of its arguments: an address fits in a word, and so does
2 m + 2; the m cells from out lie before the table; the table lies within the memory. 

### `loopTime`

 The number of steps of the main loop: 6 for each test, 15 (m / i) + 30 for the candidate i. 

### `time_le`

 Clearing the table, two assignments, the main loop and the last assignment. 

### `Cleared`

 The first j cells of the table have been cleared, and no cell outside the table has changed. 

### `clear_ends`

 The table is cleared. 

### `lt_add_iff_of_dvd`

 Among the multiples of i, those below J + i are those below J, and J itself. 

### `Marking`

 The proper multiples of i below J have been marked, J is the next one, and no other cell has
changed. 

### `mark_round`

 table[J] := 1; J := J + i. 

### `mark_ends`

 The proper multiples of i are marked, in m / i - 1 rounds. 

### `Sieved`

 The candidate is i, and the numbers below c have been dealt with: the primes below c stand at
out, and their number is in the local Count; a cell of the table holds 0 unless its index is a
proper multiple of a prime below c; no cell outside the m cells from out and the table has
changed. 

### `take_ends`

 A prime candidate is written to the list, and its proper multiples are marked. 

### `next_ends`

 i := i + 1. 

### `round_ends`

 One round of the main loop: the candidate i is dealt with, and the next candidate is i + 1. 

### `_root_.Light.sieve_meets`

 **sieve(m, out, fr)** writes the primes up to m in ascending order to out and returns their
number.  Only the m cells from out and the m + 1 cells from fr may change. 
