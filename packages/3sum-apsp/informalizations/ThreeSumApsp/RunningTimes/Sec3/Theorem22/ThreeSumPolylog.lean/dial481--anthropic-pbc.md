---
{
  "module": "ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumPolylog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumPolylog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22/ThreeSumPolylog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# 3SUM with polylogarithmic factors only

Theorem 22 states the time `n^{2−δ/2+o(1)}` for 3SUM, where `n^{3−δ}` is the time for Exact
Triangle. The two reductions as programmed here (`ChanHe.claim_CH20_Theorem_5_1`, `isHost_c3`) lose
polylogarithmic factors only: 3SUM on `n` numbers makes `(log n)^{O(1)}` instances of
Convolution-3SUM of length `N = n (log n)^{O(1)}`, and each of them `2t` instances of Exact Triangle
on `t = ⌊√N⌋ + 1` vertices per part. So the time is `O(n^{2−δ/2} (log n)^{O(1)})`.

The route: Convolution-3SUM from Exact Triangle (`c3_solvedIn_explicit`); its time at the lengths
`N = Õ(n)` is `Õ(n^{2−δ/2})` (`Polylog.c3_class`, by the closure lemmas of `IsPowPolylog`); the sum
over the instances of `ChanHe.claim_CH20_Theorem_5_1` (`threeSum_polylog_claim`); the transfer to
the word RAM (`threeSum_solvedInPolylogTime`, the result).


### `Polylog.c3_class`

 The time of Convolution-3SUM at the lengths `N n = Õ(n)` and the bounds `mag n` that the
reduction from 3SUM asks for is `Õ(n^{2−δ/2})`. 

### `threeSum_polylog_claim`

 **3SUM in time `O(n^{2−δ/2} (log n)^{O(1)})`** by programs of the light language, if Exact
Triangle is solved in the uniform time with exponent `3 − δ`. 

### `threeSum_solvedInPolylogTime`

 3SUM in time `O(n^{2−δ/2} (log n)^{O(1)})` on the word RAM, if Exact Triangle is solved in the
uniform time with exponent `3 − δ`. 
