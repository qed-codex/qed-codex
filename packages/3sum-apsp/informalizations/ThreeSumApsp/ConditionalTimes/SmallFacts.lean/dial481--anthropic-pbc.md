---
{
  "module": "ThreeSumApsp/ConditionalTimes/SmallFacts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/SmallFacts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/SmallFacts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Small facts for the deductions of Sections 5.1 and 5.2

* The claims give their bounds with a constant of unknown sign. `le_abs_mul_of_le_mul` replaces it
  by its absolute value at the moment the bound is used.
* `logU u = log (max u 2)` is nonnegative, and at most `log n` for `u ≤ n`.
* `countBound n d p` is the bound of Corollary 38. Its proof adds `productBound n D* p`, the bound
  of Corollary 26, and `buildBound n d p`, the time of Lemma 37.

In all files on the three conditional lemmas, `TimeModel`, `Claim` and `Closure` are those of the
namespace `ConditionalTimes`. That record is a parameter of the lemmas: it is given no reading, and
nothing connects it with the record for the deductions of Section 3 and Corollary 39, which is read
by programs.


### `le_abs_mul_of_le_mul`

 A bound `C g` with `g ≥ 0` and a constant of unknown sign is a bound `|C| g`. 

### `logU_nonneg`

 `logU u ≥ 0`. 

### `logU_le_log`

 `logU u ≤ log n` for `u ≤ n` and `n ≥ 2`. 

### `countBound`

 The bound of Corollary 38: `|P| n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n`, with
`p = |P|`. 

### `countBound_nonneg`

 The bound of Corollary 38 is nonnegative. 

### `productBound`

 The bound of Corollary 26 for `w` wanted entries: `w D^{0.437} + N²/D^{0.063}`. 

### `productBound_nonneg`

 The bound of Corollary 26 is nonnegative. 

### `buildBound`

 The time of Lemma 37 in the proof of Corollary 38, with `s = blockLen n d` and the inner
dimension `D* = Dstar n d`: `n D* + (n d s + d s² + |P|) (log n + 1)`, with `p = |P|`. 

### `buildBound_nonneg`

 The time of Lemma 37 is nonnegative. 
