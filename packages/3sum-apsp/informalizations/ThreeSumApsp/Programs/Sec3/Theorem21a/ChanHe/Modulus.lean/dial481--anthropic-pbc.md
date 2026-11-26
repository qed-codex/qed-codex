---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Modulus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Modulus.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21a/ChanHe/Modulus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The reduction from 3SUM to Convolution-3SUM: the modulus of a node

For Theorem 21(a).  The modulus of a node of the recursion tree of
[CH20, Theorem 5.1] is the product of two primes up to m: p₁ is the least prime q such that the
three sets have few colliding pairs modulo q (`firstP`), and p₂ the least prime q such that few of
these pairs still collide modulo p₁ q (`secondP`).

* search(mult, s₁, l₁, s₂, l₂, s₃, l₃, b₁, b₂, b₃, np, pr, cnt, fr) runs through the primes q in
  ascending order and returns the first one for which each of the three sets has at most bᵢ / np
  colliding pairs modulo mult · q (`Good`), and 1 if there is none (`search_spec`).  It always runs
  through all candidates.  A round (`searchRound_ends`) makes three tests (`check_ends`,
  `searchChecks_ends`) and records the candidate; that the first good element of the sorted list is
  the least good element of the set is `pick_filter`.
* modulus calls search twice, as in the definitions of the two primes, with three calls of coll in
  between, and returns the product; if there is no prime at all it returns 1 (`modulus_spec`).


 ## The least good element of a set is the first good element of its sorted list 

### `hit`

 The first good element of a list, and 0 if there is none. 

### `hit_snoc`

 One more candidate: it counts if it is good and no earlier one was. 

### `hit_take_succ`

 The first good element among the first t + 1 elements of a list. 

### `pick_filter`

 The least good element of a set of positive numbers, from its sorted list. 

### `pick_bounds`

 The least element of a set of primes up to m, or 1, lies between 1 and m. 

 ## One test of a candidate 

### `Mult`

 The local variables of search: the arguments mult, s₁, l₁, s₂, l₂, s₃, l₃, b₁, b₂, b₃, np, pr,
cnt, fr; the number of the candidate; the first good candidate found so far (0 if none); the modulus
mult · q; a number of colliding pairs; and whether the candidate has passed all tests so far.  Local
0 also takes the result. 

### `checkStmt`

 One test: pairs := coll(len, s, modulus, cnt, fr); if b < pairs * np then passed := 0.  The set
has its length in local xl and its address in local xs, and the bound b is in local xb. 

### `check_ends`

 **One test** leaves the number of colliding pairs in the local Pairs, and puts 0 in the local
Passed if it is too large.  The locals are arbitrary, since the test is made for each of
the three sets; hloc says what the test reads, and for a state that is written as a list it holds by
definition.  The bound must not stand in Pairs, which the call overwrites (hxb). 

 ## The search 

### `searchChecks`

 The three tests of a candidate. 

### `searchRecord`

 The candidate is recorded: if passed = 1 and found = 0 then found := mem[pr + t]. 

### `searchRound`

 A round of search, for candidate number t: modulus := mult * mem[pr + t]; passed := 1; the three
tests; the candidate is recorded. 

### `searchBody`

 search(mult, s₁, l₁, s₂, l₂, s₃, l₃, b₁, b₂, b₃, np, pr, cnt, fr): found := 0; a round for each
t < np; return found, or 1 if found = 0. 

### `Env.Ok.np_le`

 There are at most m² + 1 primes up to m.  (This is the shape y ≤ M + 1 that `mul_le_word` asks
for, with M = m².) 

### `collNeed_ok_of_search`

 What is allowed for search covers what coll needs one level of calls further down. 

### `tChecks`

 The time of the three tests of a candidate. 

### `searchChecks_ends`

 **The three tests** leave 1 in the local Passed if the candidate is good, and 0 if not. 

### `SearchArgs.candidates`

 The candidates of search: the primes up to m, in ascending order. 

### `SearchInv`

 The state before candidate number t is tested: the local Found holds the first good candidate
among the first t (0 if there is none), the locals Modulus, Pairs and Passed hold anything, and no
cell below the free pointer has changed. 

### `searchRecord_ends`

 **The candidate is recorded** if it is good and no earlier one was. 

### `searchRound_ends`

 **A round of search** tests candidate number t and records it if it is the first good one.  The
conclusion has the form that `Ends.for` asks of a round: the counter is unchanged, and the invariant
holds once it is increased. 

### `search_spec`

 **search** meets its specification. 

 ## The modulus 

### `Set1`

 The local variables of modulus: the arguments s₁, l₁, s₂, l₂, s₃, l₃, Λ, np, pr, cnt, fr; the
two primes; and the numbers of colliding pairs of the three sets modulo the first prime.  Local 0
also takes the result. 

### `modulusColls`

 The numbers of colliding pairs of the three sets modulo the first prime. 

### `modulusMain`

 The two searches of modulus, with the three calls of coll between them, and the product. 

### `modulusBody`

 modulus(s₁, l₁, s₂, l₂, s₃, l₃, Λ, np, pr, cnt, fr) returns 1 if there is no prime, and the
product of the two primes otherwise. 

### `NodeArgs.firstSearch`

 The arguments of the first search: the moduli are the primes, and the bounds are 3 Λ lᵢ². 

### `NodeArgs.secondSearch`

 The arguments of the second search: the moduli are the multiples of p₁ by the primes, and the
bounds are 3 Λ times the numbers of colliding pairs modulo p₁. 

### `search_meets_firstP`

 The first search returns the first prime of the node. 

### `search_meets_secondP`

 The second search returns the second prime of the node. 

### `three_lam_mul_le`

 The bounds that are handed to search fit in a word: 3 Λ x for x up to (n + 1)². 

### `three_lam_sq_le`

 The same for a length and its square. 

### `three_lam_coll_le`

 The same for a number of colliding pairs. 

### `Slot.Ok.coll_meets`

 coll, called for a set of a node. 

### `modulusColls_ends`

 **The three calls of coll** between the two searches leave the numbers of colliding pairs modulo
p₁ in Pairs1, Pairs2, Pairs3 and change no cell below the free pointer. 

### `modulusMain_ends`

 **The main part of modulus** returns the product of the two primes of the node. 

### `modulus_spec`

 **modulus** meets its specification. 

### `modulusSpec_of`

 The modulus, in a program that holds modulus and search, from the specification of coll. 
