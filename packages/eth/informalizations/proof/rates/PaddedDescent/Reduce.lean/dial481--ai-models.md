---
{
  "module": "proof/rates/PaddedDescent/Reduce.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Reduce.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Reduce.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The rate statement reduced to one function, in one theorem. `inRateTM_of_algorithm`: fix numbers
C₀ and s₀ with 2^s₀ ≤ C₀. Let A be a
polynomial-time function (`PolyT`) of a bit string and a pad. Suppose that for every n with sOf n ≥
s₀ and every instance φ of 3-SAT on n
variables, A applied to the code of φ and the pad of length 2^(C₀·(n / 2^(sOf n) + 1)) returns the
bit «satisfiable». Then
`Sat3.InRateTM (3/19)` holds. For the n with sOf n < s₀ the machine uses exhaustive search, for
which that pad is long enough.


### `padLog`

 The logarithm of the length of the pad, as a function of the number n of variables: C₀·(n /
2^(sOf n) + 1), division rounded down. 

### `eOf`

 The same, read off the input string. 

### `sOf_polyT`

 `sOf` of a polynomial-time function is polynomial-time. 

### `eOf_polyT`

 The logarithm of the length of the pad is computed from the input in polynomial time. 

### `eOf_enc`

 On the code of an instance on n variables, `eOf` is `padLog` of n. 

### `le_padLog`

 If 2^(sOf n) ≤ C₀ then n ≤ C₀·(n / 2^(sOf n) + 1): the pad is long enough for exhaustive search. 

### `withBrute`

 The algorithm with its two branches: exhaustive search where sOf n < s₀, and A elsewhere. 

### `withBrute_polyT`

 The algorithm with its two branches is polynomial-time if `A` is. 

### `inRateTM_of_algorithm`

 The reduction. Let 2^s₀ ≤ C₀ and let `A` be a polynomial-time function of a bit string and a
list of units. If for every n with
sOf n ≥ s₀ and every instance φ of 3-SAT on n variables A (code of φ, the list of 2^(C₀·(n / 2^(sOf
n) + 1)) units) is the bit «satisfiable»,
then one Turing machine decides 3-SAT within C·2^{C·n/(log₂(n+2))^{3/19}} steps, for some constant
C. The division rounds down. 
