---
{
  "module": "ThreeSumApsp/RunningTimes/FromClaims/Bounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/FromClaims/Bounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/FromClaims/Bounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From a realized running time to a program with the paper's bound

A claim gives a running time `T` with `T ≤ C X`, where `X` is the bound that the paper prints, and
`RealizedWithin` gives a program that takes `c T + c` steps.  This file puts the two together.

* Bounds in several parameters, valid on a domain on which `X ≥ 1`: `exists_solves`, and
  `exists_solves_nonneg` with `exists_solves_pair` for two programs with one slope and one constant.
* Bounds `O(n^a (log n)^e)` in one size, valid for all large `n`: `solvedAt_of_realized`, and for
  every exponent `κ` of the magnitude `solvedInTime_of_claim` and `solvedInPolylogTime_of_claim`.
* An instance with numbers bounded by `n^κ` is also one with numbers bounded by `n^κ'`, `κ ≤ κ'`
  (`solvedInTimeAt_mono`), so that a bound for all `κ ≥ 1` is a bound for all `κ`
  (`solvedInTime_of_one_le`).


 ## Bounds on a domain 

### `mul_add_le_of_le_mul`

 `c T + c ≤ (c |C| + c) X` if `T ≤ C X`, `X ≥ 1` and `c ≥ 0`. 

### `cast_pow_eq`

 The bound `U = N^c` on the numbers, as a real number. 

### `exists_solves_nonneg`

 If the running time `T` is realized, and `T ≤ C X` and `X ≥ 1` on the instances in `dom'`, whose
numbers are bounded by the `κ`-th power of the size, then a program solves them in `O(X)` steps. 

### `exists_solves`

 `exists_solves_nonneg` without the sign of the constant: the form of the items with one program.


### `exists_solves_pair`

 Two programs, each with its slope and its constant, have one slope and one constant in common.


 ## Bounds in one size, for all large sizes 

### `solvedAt_of_realized`

 From a realized running time with a bound for all large sizes to a program with that bound. 

### `solvedInTime_of_claim`

 A claim "solved in `O(n^a)` time on numbers of absolute value at most `n^κ`, for every `κ`", in
a reading `S` of "is solved in time T" that is realized, gives programs. 

### `solvedInPolylogTime_of_claim`

 A claim "solved in `O(n^a (log n)^{O(1)})` time on numbers of absolute value at most `n^κ`, for
every `κ`", in a reading `S` of "is solved in time T" that is realized, gives programs. 

### `solvedInTimeAt_mono`

 The bound `U` is not in the memory: a program for numbers within `n^κ'` serves numbers within
`n^κ`, for `κ ≤ κ'`.  (At size 0, where `0^0 > 0^1`, the input is empty.) 

### `solvedInTime_of_one_le`

 Some claims of the paper are about `κ ≥ 1`; the items are about all `κ`. 
