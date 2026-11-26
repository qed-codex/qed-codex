---
{
  "module": "ThreeSumApsp/TimeClaims/Sec3/Theorem21_22.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Theorem21_22.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/TimeClaims/Sec3/Theorem21_22.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Running-time claims of Section 3.4: Theorems 21 and 22

All lemmas are about an arbitrary interpretation `M : DetTimeModel` of "is solved in time T".  They
are deductions between running-time sentences: those of the paper for Theorem 22, and for
Theorem 21, which the paper cites, those of the route taken here.

* Theorem 21(a) from two reductions, [CH20, Theorem 5.1] followed by [VW13, Theorem 4.3]:
  `Theorem21a.of_CH20_VW13`.  The sizes, numbers of instances and extra times compose
  by the rules for `n^{a+o(1)}`.
* Theorem 21(b) for the (min,+)-product from [VW13, Theorem 3.3] and [VW18, Theorem 4.2]:
  `Theorem21b.minPlus_of_VW13_VW18`.  The time of the first reduction is again a good
  time (`GoodTime.mul_logU`), and `log (cU) = O(log U)` (`dominated_logU_mul`).
* Theorem 21(b) for APSP by repeated squaring: `Theorem21b.apsp_of_minPlus`, whose
  arithmetic is `dominated_repeatedSquaring`.
* "Plug Theorem 19 into Theorem 21": `threeSum_of_uniform_theorem_21a`,
  `minPlus_of_uniform_theorem_21b`, `apsp_of_uniform_theorem_21b`.
* Theorem 22: the roundings such as `n^{2-1/1296+o(1)} ≤ O(n^{1.99923})`
  (`Claim.SolvedAlongPow.mono`).


 ## Theorem 21(a) 

### `Theorem21a.of_CH20_VW13`

 Theorem 21(a) from two reductions: [CH20, Theorem 5.1] followed by [VW13, Theorem 4.3]. 

 ## Theorem 21(b): the (min,+)-product 

### `GoodTime.one_add_logU_le`

 A good time is at least `1 + log u`. 

### `GoodTime.nonneg`

 A good time is nonnegative. 

### `GoodTime.mul_logU`

 The time `C T(s) log U` that [VW13, Theorem 3.3] gives for Negative Triangle is again a good
time. 

### `Theorem21b.minPlus_of_VW13_VW18`

 Theorem 21(b), (min,+)-product, from two reductions: [VW13, Theorem 3.3] followed by
[VW18, Theorem 4.2]. 

 ## Theorem 21(b): APSP 

### `Squaring`

 The quantities in the arithmetic of repeated squaring. 

### `Squaring.n`

 The number of vertices. 

### `Squaring.V`

 Stands for the time `T(⌈n^{1/3}⌉)`. 

### `Squaring.W`

 Stands for `log U`, where `U` bounds the entries. 

### `dominated_repeatedSquaring`

 The arithmetic of repeated squaring:
`(⌈log₂ n⌉ + 1) (C n² V W² + C₀ n² (1 + W)) = O(n² V log³ n)`, if `0 ≤ W ≤ B log n` and
`V ≥ 1 + W`. 

### `Theorem21b.apsp_of_minPlus`

 Theorem 21(b), APSP: repeated squaring on top of the
(min,+)-product. 

 ## "Plug Theorem 19 into Theorem 21"

The time of Theorem 19 is `uniformTime K δ e s u = K s^{3-δ} (log s + 1)^e (1 + log u)²`.
Theorem 21 evaluates it at sizes `s(n)` and bounds `u(n) ≤ c n^κ` on the numbers, and multiplies it
by powers of `n` and logarithms.  So each bound is a product of functions of known classes. 

### `goodTime_uniformTime`

 The running time `K s^{3-δ} (log s + 1)^e (1 + log u)²` satisfies the requirements of
Theorem 21(b) as rendered by `GoodTime`: it is at least `s² (1 + log u)`, and divided by `s` it is
nondecreasing in `s` ("for which T(s)/s is nondecreasing"). 

### `isPowPolylog_uniformTime_cbrtCeil`

 The time of Theorem 19 on `⌈n^{1/3}⌉` vertices per part, with weights up to `c n^κ`, is
`Õ(n^{1-δ/3})`. 

### `threeSum_of_uniform_theorem_21a`

 "Plug Theorem 19 into Theorem 21", 3SUM, in general form: with exponent `3 - δ` for Exact
Triangle the time for 3SUM is `n^{2-δ/2+o(1)}`. 

### `minPlus_of_uniform_theorem_21b`

 "Plug Theorem 19 into Theorem 21", (min,+)-product, in general form: with exponent `3 - δ` for
Exact Triangle the time is `O(n^{3-δ/3} (log n)^{O(1)})`. 

### `apsp_of_uniform_theorem_21b`

 "Plug Theorem 19 into Theorem 21", APSP, in general form. 

 ## Theorem 22 

### `Claim.SolvedAlongPow.mono`

 The roundings of Theorem 22, such as "n^{2-1/1296+o(1)} ≤ O(n^{1.99923})", at the level of
claims: an inclusion between two classes of running times carries over to the claims. 
