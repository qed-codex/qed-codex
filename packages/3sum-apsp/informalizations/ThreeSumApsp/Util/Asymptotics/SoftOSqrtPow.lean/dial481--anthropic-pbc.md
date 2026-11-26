---
{
  "module": "ThreeSumApsp/Util/Asymptotics/SoftOSqrtPow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/SoftOSqrtPow.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Asymptotics/SoftOSqrtPow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Bounds of the form "a polylogarithm times a power of √n"

`SoftOSqrtPow F i` says that `F n ≤ K (⌊log₂ n⌋ + 1)^e (⌊√n⌋ + 1)^i` for all `n ≥ 2`, for some
constants `K` and `e`.  In the notation of the paper this is `F(n) = Õ((√n)^i) = Õ(n^{i/2})`
(`SoftOSqrtPow.isPowPolylog`): the index 0 stands for a polylogarithm, 2 for `Õ(n)`, 3 for
`Õ(n^{3/2})`.

It is the calculus `Scale.SoftO` on the scale `sqrtScale`, which counts the powers of `⌊√n⌋ + 1` and
not those of `⌊log₂ n⌋ + 1`.  The logarithm of a function with such a bound is polylogarithmic
(`SoftOSqrtPow.natLog_comp`).  The tactic `growth_sqrt` proves a bound for an explicit expression
in `n`, `⌊√n⌋` and logarithms by following the expression, and no constant is ever written out.


### `natLog_succ_le`

 `⌊log₂ n⌋ + 1 ≤ 4 ln n` for `n ≥ 2`. 

### `natSqrt_succ_le`

 `⌊√n⌋ + 1 ≤ 2 √n` for `n ≥ 1`. 

### `sqrtScale`

 The scale of the bounds `Õ(n^{i/2})`, for `n ≥ 2`: powers of `⌊√n⌋ + 1` are counted, powers of
`⌊log₂ n⌋ + 1` are not. 

### `SoftOSqrtPow`

 `F(n) ≤ K (⌊log₂ n⌋ + 1)^e (⌊√n⌋ + 1)^i` for all `n ≥ 2`, for some `K` and `e`. 

### `natLog`

 The function `⌊log₂ n⌋` is a polylogarithm. 

### `natSqrt`

 The function `⌊√n⌋` has the first power of `√n`. 

### `self`

 `n` itself is at most `(⌊√n⌋ + 1)²`. 

### `natLog_comp`

 The logarithm of a function with such a bound is a polylogarithm. 

### `isPowPolylog`

 In the notation of the paper: `F(n) = Õ(n^{i/2})`. 

### `growth_sqrt`

 Proves `SoftOSqrtPow F i` as `growth` does.  The given facts bound the quantities that occur,
other than `n`, `⌊√n⌋` and binary logarithms. 
