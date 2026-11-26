---
{
  "module": "ThreeSumApsp/Statements/Exponents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/Exponents.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/Exponents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# From a real exponent to a rational one

An item statement bounds the steps of a program by `C (n^a + 1)`, with real numbers `C` and `a`.
The end statement uses Lean's core library only.  It asks for a step bound `T` with natural values
that depends on the size alone, and it writes `T(n) = O(n^r)`, for a rational `r = p/q`, as
`T(n)^q ≤ K n^p`.  Here the first bound, rounded up, is shown to be a bound of the second kind
(`bigO_stepBound`), and a program that meets the first is shown to meet the second
(`SolvedInTime.endStatement`).  The program and the slope of the word size stay the same.


### `rpow_pow_den`

 For a rational `r = p/q ≥ 0`: `(n^r)^q = n^p`. 

### `bigO_of_le_rpow`

 A function with `T(n) ≤ C n^r` from `n = 2` on is `O(n^r)` in the sense of the end statement. 

### `stepBound`

 The bound `C (n^a + 1)` of `SolvedInTimeAt` for `e = 0`, rounded up. 

### `bigO_stepBound`

 The rounded bound is `O(n^r)` in the sense of the end statement. 

### `SolvedInTime.endStatement`

 **A bound `O(n^a)` of an item statement, with `a` the rational `r`, is the bound `O(n^r)` of the
end statement**, with the same program and the same slope. 
