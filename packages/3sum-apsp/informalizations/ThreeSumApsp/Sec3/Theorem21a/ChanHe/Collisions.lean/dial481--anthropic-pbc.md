---
{
  "module": "ThreeSumApsp/Sec3/Theorem21a/ChanHe/Collisions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Collisions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21a/ChanHe/Collisions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(a), the reduction of Chan and He: the choice of the modulus

For Theorem 21(a): the deterministic reduction from 3SUM to
Convolution-3SUM after [CH20, Theorem 5.1] hashes the numbers by `x ↦ x mod pq`, for two primes
`p` and `q` that it finds by exhaustive search among the primes up to `m = mPar n U`.  This file
shows that both searches succeed and that few elements are badly hashed.

* An ordered pair of distinct elements of a set `S` collides modulo `M` if `M` divides their
  difference; `coll S M` counts these ordered pairs.  An element that collides with another one is
  heavy.  There are at most as many heavy elements as colliding pairs (`card_heavy_le_coll`).  The
  count is determined by the sizes of the residue classes (`coll_eq_sum`); the proofs below do not
  need this, a program that computes the count does.
* A nonzero difference has at most `Λ = Lam U` prime divisors.  So, summed over the candidates `q`
  in the set `Q` of primes that a search goes through, the pairs that collide modulo `M₀ q` number
  at most `Λ` times those that collide modulo `M₀` (`sum_coll_mul_le`).
* By counting (the finite form of Markov's inequality and of the union bound, which [CH20] uses),
  some candidate is, for each of the three sets, at most three times as bad as the average
  (`Finset.exists_forall_mul_card_le_mul_sum`, `exists_prime_coll_le`). So both searches succeed
  (`firstP_spec`, `secondP_spec`), and the modulus `pq` leaves at most `9Λ²|S|²/|Q|²` colliding
  pairs in each set `S` (`modulus_spec`).
* There are at least `wPar n U` primes up to `mPar n U` (`wPar_le_card_primesLE`, from the bound
  `2^m ≤ (m + 1) lcm(1, …, m)` of Mathlib).  With that many candidates a set `S` has at most
  `|S|²/(2n)` heavy elements (`card_heavy_modulus_le`, `le_card_primesLE_mPar_sq`).


 ## Colliding pairs and heavy elements 

### `natCast_dvd_sub_iff_emod_eq`

 Two integers are congruent modulo `M` iff they have the same remainder. 

### `card_heavy_le_coll`

 Each heavy element is the first component of a colliding pair. 

### `coll_le_sq`

 There are at most `|S|²` colliding ordered pairs. 

### `coll_eq_sum`

 The collision count is determined by the sizes of the buckets: an element collides with the
other members of its bucket. 

### `Lam_pos`

 `Lam U` is at least 1. 

### `card_prime_divisors_le`

 A nonzero integer of absolute value at most `2U` is divisible by at most `Lam U` primes,
because their product divides it. 

### `sum_coll_mul_le`

 Double counting.  Summed over the candidates `q ∈ Q`, the pairs that collide modulo `M₀ q`
number at most `Lam U` times those that collide modulo `M₀`: such a pair collides modulo `M₀`, and
`q` divides its difference.  Coprimality of `q` and `M₀` is not used, so the two primes of a modulus
are allowed to coincide. 

 ## The two searches succeed 

### `pick_mem`

 On a nonempty set, `pick` returns a member. 

### `exists_prime_coll_le`

 Some candidate `q` is good for the three sets at once: in each of them at most the fraction
`3Λ/|Q|` of the pairs that collide modulo `M₀` still collide modulo `M₀ q`. 

### `firstP_spec`

 The first search succeeds: `firstP` lies in `Q` and passes its three tests. 

### `secondP_spec`

 The second search succeeds, for any first factor `p`. 

### `modulus_spec`

 Both searches succeed, and the modulus leaves at most `9Λ²|S|²/|Q|²` colliding pairs in each of
the three sets.  (A search that fails returns 1, which is not in `Q`.) 

### `modulus_bounds`

 The modulus lies between 1 and `m²` when all primes in `Q` are at most `m`. 

### `nonempty_of_le_card_sq`

 The hypothesis of `card_heavy_modulus_le` on the number of candidates implies that there is
one. 

### `card_heavy_modulus_le`

 With at least `√(18n) Λ` primes to choose from, each of the three sets `S` has at most
`|S|²/(2n)` heavy elements.  This is why the sizes of the sets fall doubly exponentially along the
recursion. 

 ## Enough primes 

### `wPar_le_card_primesLE`

 There are at least `wPar n U` primes up to `mPar n U`. 

### `le_card_primesLE_mPar_sq`

 The primes up to `mPar n U` are enough for `card_heavy_modulus_le`. 
