---
{
  "module": "ThreeSumApsp/Util/Asymptotics/PowLittleO.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/PowLittleO.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/PowLittleO.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Calculating with `n^{a+o(1)}`

`IsPowLittleO f a` reads `f(n) = n^{a+o(1)}` as an upper bound on `|f(n)|`: there is a sequence
`ε(n) → 0` with `|f(n)| ≤ n^{a+ε(n)}` for all large `n`. This says the same as `f(n) = O(n^{a+η})`
for every `η > 0` (`isPowLittleO_iff`). In the second form the rules of the notation follow from the
rules for `O`:

* the exponent may grow (`IsPowLittleO.mono`), and a strictly larger exponent absorbs the `o(1)`
  (`IsPowLittleO.isBigOPow`);
* sums, products and constant factors (`IsPowLittleO.add`, `IsPowLittleO.mul`,
  `IsPowLittleO.const_mul`);
* `(n^{d+o(1)})^{c+o(1)} = n^{cd+o(1)}` for `c, d ≥ 0` (`IsPowLittleO.comp`);
* `O(n^a)` and `O(n^a (log n)^{O(1)})` are `n^{a+o(1)}` (`IsBigOPow.isPowLittleO`,
  `IsPowPolylog.isPowLittleO`).


 ### The two readings of the notation 

### `IsPowLittleO.eventually_abs_le`

 The `o(1)` is absorbed: if `f = n^{a+o(1)}` and `a < b`, then `|f n| ≤ n ^ b` for all large `n`.


### `IsPowLittleO.of_eventually_abs_le`

 If for every `η > 0`, `|f(n)| ≤ n^{a+η}` for all large `n`, then `f(n) = n^{a+o(1)}`. For
`ε(n)` take the excess of the exponent that is needed at `n`: the number with
`n^{a+ε(n)} = max(|f(n)|, n^a)`. 

### `isPowLittleO_iff`

 `f(n) = n^{a+o(1)}` if and only if `f(n) = O(n^{a+η})` for every `η > 0`. 

 ### The rules 

### `IsPowLittleO.mono`

 `n^{a+o(1)} ⊆ n^{b+o(1)}` for `a ≤ b`. 

### `IsPowLittleO.isBigOPow`

 `n^{a+o(1)} ⊆ O(n^b)` for `a < b`. 

### `IsBigOPow.isPowLittleO`

 `O(n^a) ⊆ n^{a+o(1)}`. 

### `IsPowPolylog.isPowLittleO`

 `O(n^a (log n)^{O(1)}) ⊆ n^{a+o(1)}`. 

### `IsPowLittleO.add`

 `n^{a+o(1)} + n^{a+o(1)} = n^{a+o(1)}`. 

### `IsPowLittleO.mul`

 `n^{a+o(1)} · n^{b+o(1)} = n^{a+b+o(1)}`. 

### `IsPowLittleO.const_mul`

 Constant factors are absorbed. 

 ### Composition 

### `exists_pos_add_mul_add_le`

 For `c, d ≥ 0` and `η > 0` there is `t > 0` with `(c + t)(d + t) ≤ cd + η`. 

### `IsPowLittleO.comp`

 `(n^{d+o(1)})^{c+o(1)} = n^{cd+o(1)}`: if `T(s) = s^{c+o(1)}` and `size(n) = n^{d+o(1)}` then
`T(size(n)) = n^{cd+o(1)}`, for `c, d ≥ 0`. The sizes need not tend to infinity. 
