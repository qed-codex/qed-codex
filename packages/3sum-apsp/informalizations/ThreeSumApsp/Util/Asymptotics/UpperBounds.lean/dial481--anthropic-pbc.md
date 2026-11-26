---
{
  "module": "ThreeSumApsp/Util/Asymptotics/UpperBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/UpperBounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/UpperBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# One-sided bounds `O(n^a)`, `Õ(n^a)` and `n^{a+o(1)}`

A running time is bounded from above only. `UpperBigOPow f a`, `UpperPowPolylog f a` and
`UpperPowLittleO f a` say that `f(n)` is eventually at most `C n^a`, at most `C n^a (log n)^e`, and
at most `n^{a+ε(n)}` with `ε(n) → 0`, where `IsBigOPow`, `IsPowPolylog` and `IsPowLittleO` say this
of `|f(n)|`.

A bound on `|f|` is a bound on `f` (`IsBigOPow.upperBigOPow`), and the function may be replaced by a
smaller one (`mono_left`); these two lemmas have the same names for the three classes. For `Õ(n^a)`
and `n^{a+o(1)}` a bound on `f` is a bound by a nonnegative function of the class that bounds `|f|`
(`UpperPowPolylog.exists_isPowPolylog`). For `Õ(n^a)` the closure properties follow: a bound on `f`
is a bound on `|f|` if `f` is eventually nonnegative (`UpperPowPolylog.isPowPolylog`), sums,
nonnegative constant factors, products with a nonnegative factor, a larger exponent (`mono`).
Logarithms and the `o(1)` are absorbed by a strictly larger exponent
(`UpperPowPolylog.upperBigOPow`, `UpperPowLittleO.upperBigOPow`).


### `UpperBigOPow`

 `f(n) = O(n^a)`, as an upper bound. 

### `UpperPowPolylog`

 `f(n) = O(n^a (log n)^{O(1)})`, as an upper bound. 

### `UpperPowLittleO`

 There is a sequence `ε(n) → 0` with `f(n) ≤ n^{a+ε(n)}` for all large `n`: a bound on `f` and
not on `|f|` (that is `IsPowLittleO`). 

 ### `O(n^a)` from above 

### `IsBigOPow.upperBigOPow`

 `f = O(n^a)` is in particular an upper bound on `f`. 

### `mono_left`

 The function may be replaced by one that is eventually at most as large. 

 ### `Õ(n^a)` from above 

### `IsPowPolylog.upperPowPolylog`

 `f = Õ(n^a)` is in particular an upper bound on `f`. 

### `mono_left`

 The function may be replaced by one that is eventually at most as large. 

### `exists_isPowPolylog`

 An upper bound `Õ(n^a)` is a bound by a nonnegative function of the class `Õ(n^a)`. 

### `isPowPolylog`

 For a function that is eventually nonnegative, the bound on `f` is a bound on `|f|`. 

### `mono`

 The exponent may be raised. 

### `add`

 `Õ(n^a) + Õ(n^a) = Õ(n^a)`, from above. 

### `const_mul`

 Nonnegative constant factors are absorbed. 

### `mul`

 `Õ(n^a) · Õ(n^b) = Õ(n^(a+b))`, from above, if the second factor is eventually nonnegative. 

### `upperBigOPow`

 Logarithms are absorbed: `Õ(n^a) ⊆ O(n^b)` for `a < b`, from above. 

 ### `n^{a+o(1)}` from above 

### `IsPowLittleO.upperPowLittleO`

 `f = n^{a+o(1)}` is in particular an upper bound on `f`. 

### `mono_left`

 The function may be replaced by one that is eventually at most as large. 

### `exists_isPowLittleO`

 An upper bound `n^{a+o(1)}` is a bound by a nonnegative function of the class `n^{a+o(1)}`. 

### `upperBigOPow`

 The `o(1)` is absorbed: `n^{a+o(1)} ⊆ O(n^b)` for `a < b`, from above. 
