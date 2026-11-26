---
{
  "module": "ThreeSumApsp/Spec/Sec3/Theorem17/Choice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Choice.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Spec/Sec3/Theorem17/Choice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The prime that is chosen (proof of Theorem 17)

`chosenPrime n D AB BC AC` is the first prime of the window `√D/2 ≤ p < √D` at which the count,
computed with Strassen's algorithm from the three lists of weights, is smallest.  Here
`triOf n AB BC AC` is the instance of Exact Triangle whose weights are read from the three lists:
`w(a,b)` at `a n + b` of `AB`, `w(b,c)` at `b n + c` of `BC`, `w(a,c)` at `a n + c` of `AC`.

* The computed count is the count of the proof of Theorem 17 at every prime of the window
  (`countOf_eq`), so the chosen prime is a selected prime in the sense of the proof of Theorem 17,
  "We select the prime with the smallest count" (`chosenPrime_isSelected`).  It lies between 2 and
  `⌊√D⌋` (`two_le_chosenPrime`, `chosenPrime_le_sqrt`).
* A program finds it in one pass over the primes: `bestOf f L i` is the best of the first `i`
  elements of a list (`bestOf_one`, `bestOf_succ`, `bestOf_length`).
* The paper bounds the weights by `n^ν`; a program has a bound `U`.  `kappaOf n U` is the least
  exponent `κ ≥ 1` with `U ≤ n^κ`, and with it the bound of the proof of Theorem 17 on the number
  `F(p)` of false positives, that is, of triples with `S(a,b,c) ≠ 0` and `p ∣ S(a,b,c)`, holds for
  the chosen prime (`F_chosenPrime_le`).


 ## The chosen prime 

### `chosenPrime`

 "We select the prime with the smallest count" (the first such prime; 0 if the window has no
prime). 

### `chosenPrime_isSelected`

 **The chosen prime is a selected prime** (proof of Theorem 17: "We select the prime with the
smallest count"). 

### `chosenPrime_mem`

 The chosen prime is a prime of the window. 

### `chosenPrime_mem_primesList`

 The chosen number is in the list of the primes of the window. 

### `two_le_chosenPrime`

 The chosen prime is at least 2. 

### `chosenPrime_le_sqrt`

 The chosen prime is at most `⌊√D⌋`. 

 ## The smallest count, by one pass 

### `bestOf`

 The first of the first `i` elements of a list at which `f` is smallest; 0 for `i = 0`. 

### `bestOf_one`

 The first element is the best of one. 

### `bestOf_succ`

 One more element: it is the best so far exactly if `f` is smaller there. 

### `bestOf_length`

 The best of all the elements is what `List.argmin` returns. 

 ## False positives, in terms of a bound on the weights 

### `kappaOf`

 The least exponent `κ ≥ 1` with `U ≤ n^κ`. 

### `one_le_kappaOf`

 The exponent is at least 1. 

### `le_rpow_kappaOf`

 `U ≤ n^κ` for this exponent. 

### `kappaOf_le`

 It is the least such exponent. 

### `weightsPolyBounded_kappaOf`

 Weights of absolute value at most `U` are at most `n^κ`. 

### `F_chosenPrime_le`

 **The number of false positives of the chosen prime** (proof of Theorem 17:
"F(p) = O(n³ log(3n^ν)/√D) = O(ν n³ log n/√D)"), with the constant `Hashing.falsePositiveConst`. 
