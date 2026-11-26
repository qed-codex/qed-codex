---
{
  "module": "ThreeSumApsp/RunningTimes/Sec4/Corollary31_32/Arithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary31_32/Arithmetic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec4/Corollary31_32/Arithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Changing the bounds of the running-time statements of Section 4

The running-time statements of Section 4 say "there are programs and a constant `C` such that the
time is at most `C f(x)` on the inputs `x` of a domain".  Such a statement stays true for a smaller
domain and for every bound `g` with `f = O(g)` there: `exists_isDataStructure_of_dominated` for a
data structure and `exists_solves_of_dominated` for a program that computes the wanted entries.

This file has the bounds `f = O(g)` that Section 4.4 uses, for functions `N`, `d`, `w` of the input
(the size, the inner dimension and the number of wanted entries):

* with `d ≥ 1`, the logarithmic factors are absorbed by a smaller `γ` and a larger `q`
  (`dominated_preprocessing`, `dominated_query`, `dominated_wanted_sparse`);
* with `d ≥ 2`, `log d + 1 = O(log d)` (`dominated_preprocessing_log`, `dominated_query_log`,
  `dominated_wanted_log`, `dominated_wanted_add`).


 ## The hypotheses on the input 

### `WordRam.Items.thinDom.one_le_D`

 The inner dimension of an input with `1 ≤ lo ≤ D` is at least 1, as a real number. 

### `WordRam.Items.thinDom.two_le_D`

 The inner dimension of an input with `2 ≤ D` is at least 2, as a real number. 

### `WordRam.Items.thinDom.mono`

 The lower bound on the inner dimension may be lowered. 

 ## The logarithmic factors are absorbed (`d ≥ 1`) 

### `dominated_sq_mul_rpow_mul_log`

 `N² d^a (log d + 1)^e = O(N² / d^γ')` for `a < -γ'`. 

### `dominated_preprocessing`

 The logarithmic factor of the preprocessing is absorbed by a smaller `γ`. 

### `dominated_query`

 The logarithmic factor of a query is absorbed by a larger exponent. 

### `dominated_wanted_sparse`

 Corollary 32: for at most `N² / d^κ` wanted entries, every `γ'` below `γ` and below `κ - q`
absorbs the logarithmic factors. 

 ## `log d + 1 = O(log d)` (`d ≥ 2`) 

### `dominated_log_add_one`

 `log d + 1 = O(log d)`. 

### `dominated_preprocessing_log`

 The preprocessing, with `log d` for `log d + 1`. 

### `dominated_query_log`

 A query, with `log d` for `log d + 1`. 

### `dominated_wanted_log`

 Corollary 32: the time for at most `N² / d^κ` wanted entries is
`O(N² log² d (d^{-γ} + d^{q-κ}))`. 

### `dominated_wanted_add`

 Proof of Theorem 25: the preprocessing and, for each of `w` positions, one query with an
exponent `q ≤ q'` take `O(N² log² d / d^γ + w d^{q'} log d)` time, with `log d` for `log d + 1`. 
