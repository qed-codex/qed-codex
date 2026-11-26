---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Hashing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Hashing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Hashing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Hashing modulo a prime (proof of Theorem 17), on numbers and lists

The reduction of Theorem 17 hashes the weights modulo a prime `p` of the window `√D/2 ≤ p < √D` and
selects the prime with the fewest triples `(a,b,c)` with `S(a,b,c) ≡ 0 (mod p)`, where
`S(a,b,c) = w(a,b) + w(b,c) + w(a,c)`.  This file has the parts of this step that a program
computes:

* the residue of a weight as a natural number below `p` (`resid`, `residList`);
* the entries of the matrices `P` and `Q` of the proof of Theorem 17 as unit vectors (`cycVec_matP`,
  `cycVec_matQ`), and the count of the triples, read off the vectors of `PQ` (`countZeroMod_eq`);
* the primes of the window by comparisons of integers (`primesList`, `primesInRange_eq`).


 ## Residues 

### `resid`

 The residue of `w` modulo `p` in `{0, …, p − 1}`. 

### `resid_cast`

 The residue, as an integer. 

### `resid_lt`

 The residue is less than `p`. 

### `resid_eq_iff`

 The residue is the number below `p` that is congruent to `w`. 

### `resid_neg`

 The residue of `-w` from the residue of `w`. 

### `residList`

 The residues of a list. 

### `getD_residList`

 The residues of a list, read with a default: beyond the end of the list both sides are 0. 

### `dblList`

 The table `p, 2p, 4p, …, 2^len p`. 

### `bitLen`

 The number of binary digits of `U`: the least `len` with `U < 2^len`. 

 ## The count of the proof of Theorem 17 

### `cycVec_matP`

 Proof of Theorem 17: the entry `P[a,c] = x^{w(a,c) mod p}` is a unit vector. 

### `cycVec_matQ`

 Proof of Theorem 17: the entry `Q[c,b] = x^{w(b,c) mod p}` is a unit vector. 

### `countZeroMod_eq`

 Proof of Theorem 17: the count of the triples with `S(a,b,c) ≡ 0 (mod p)` is "the sum over the
pairs (a,b) ∈ A × B of the coefficient of x^{-w(a,b) mod p} in (PQ)[a,b]". 

 ## The primes of the window 

### `primesList`

 The primes `p` with `√D/2 ≤ p < √D`, by integer comparisons: `D ≤ 4p²` and `p² < D`. 

### `primesInRange_eq`

 The comparisons with `√D` are comparisons of integers. 

### `mem_primesList`

 The primes of the window, without the bound `q < D` of the search. 

### `le_sqrt_of_mem_primesList`

 A prime of the window is at most `⌊√D⌋`. 

### `length_primesList_le`

 The window has at most `⌊√D⌋` primes. 
