---
{
  "module": "ThreeSumApsp/ConditionalTimes/Theorem35.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Theorem35.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Theorem35.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 35 from Corollary 38, Lemma 36 and the restart argument

The proof takes `d = ⌊n^{1/40}⌋` in Lemma 36 and answers every comparison count by Corollary 38.

1. (min,+)-product, APSP and Exact Triangle: a counting call costs `O(n^{2.0229} log n)`
   (`exists_counting_call_le`, from `theorem_35_counting_call`), so the `Õ(n/d)` calls of
   Lemma 36(a) and the `Õ(n³/d)` further time give `Õ(n^{3-1/40+0.0229})`
   (`lasVegasInPolylog_of_corollary_38_lemma_36a`).
2. 3SUM: a comparison count of Lemma 36(b), with `O(n²/d)` pairs, costs `Õ(n^{1.9979})`
   (`isPowPolylog_countBound_listLen`, `lasVegasInPolylog_threeSum_of_corollary_38_lemma_36b`).
3. The logarithms are absorbed, and restarting gives the bounds with high probability
   (`lasVegasIn_and_whpIn_of_polylog`).

Sums and products of running times are handled by the closure properties of the classes `O(n^a)`
and `Õ(n^a)`. About `d` they need `d = O(n^{1/40})` and `1/d = O(n^{-1/40})` (`isBigOPow_listLen`,
`isBigOPow_inv_listLen`); the hypotheses of Lemma 36 and Corollary 38 need `1 ≤ d ≤ n` and
`d ≤ n^{1/40}` (`theorem_35_d`). The statements `theorem_35_min_plus_total`,
`theorem_35_further_time`, `theorem_35_three_sum_count` and `theorem_35_three_sum_total` check the
same sums with the paper's powers of the logarithm; they are not used here, where only the classes
matter.


### `LasVegasInPolylog`

 A Las Vegas algorithm solves the problem in `Õ(n^a)` expected time. 

 ### The length `d = ⌊n^{1/40}⌋` of the lists 

### `one_le_listLen_and_listLen_le`

 `1 ≤ d ≤ n`, the hypothesis of Lemma 36. 

### `isPowPolylog_of_mul_listLen`

 If `f(n) d = Õ(n^a)`, then `f(n) = Õ(n^{a-1/40})`. 

 ### (min,+)-product, APSP and Exact Triangle 

### `exists_counting_call_le`

 "answer every comparison count by Corollary 38": the `d` comparison counts of a counting call,
with `n²` pairs in all, cost `O(n^{2.0229} log n)`. The hypothesis is the bound of Corollary 38. 

### `lasVegasInPolylog_of_corollary_38_lemma_36a`

 Proof of Theorem 35, "(min,+)-product, APSP, and Exact Triangle": "So the Õ(n/d)
counting calls of Lemma 36(a) cost Õ((n/d) n^{2.0229}) = Õ(n^{3-1/40+0.0229})", for any one of the
problems for which Lemma 36(a) is assumed. 

 ### 3SUM 

### `isPowPolylog_countBound_listLen`

 "a comparison count of Lemma 36(b) costs ... O(n^{1.9979} log n)": the bound of Corollary 38 at
`d = ⌊n^{1/40}⌋` and `⌈K n²/d⌉` pairs. 

### `lasVegasInPolylog_threeSum_of_corollary_38_lemma_36b`

 Proof of Theorem 35, "3SUM": "a comparison count of Lemma 36(b) costs ...
O(n^{1.9979} log n), so 3SUM can also be solved in Õ(n^{1.9979}) ... expected time." 

 ### Absorbing the logarithms, and high probability 

### `isPowPolylog_logb_two`

 `log₂ n = Õ(1)`. 

### `lasVegasIn_and_whpIn_of_polylog`

 Proof of Theorem 35: "Õ(n^a) ≤ O(n^b)" for `a < b`, at the level of claims, and "The bounds also
hold with probability 1 - n^{-c} for any constant c", by restarting. The factor `log n` of the
restarts is absorbed because `a < b`; `b > 0` absorbs the `+ 1` in the length `T n + 1` of a run. 

### `conditional_theorem_35`

 The deduction of all the bounds of **Theorem 35** (and of the second half of
Theorem 2) from Corollary 38, Lemma 36 and the restart argument: "Let d := ⌊n^{1/40}⌋, apply
Lemma 36 with this d, and answer every comparison count by Corollary 38." `listLen n` is this d.
This theorem does not prove Theorem 35: every hypothesis is a running-time claim about `M` that is
assumed here, and Lemma 36 rests on results cited from [CVX22]. 
