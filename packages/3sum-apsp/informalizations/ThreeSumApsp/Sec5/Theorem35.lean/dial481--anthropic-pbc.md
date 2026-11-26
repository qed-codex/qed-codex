---
{
  "module": "ThreeSumApsp/Sec5/Theorem35.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Theorem35.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Theorem35.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Proof of Theorem 35: the arithmetic

Theorem 35 gives Las Vegas algorithms for 3SUM on `n` real numbers in `O(n^{1.998})` expected time,
and for the (min,+)-product, APSP and Exact Triangle with real inputs in `O(n^{2.998})` expected
time.  The proof takes `d := ⌊n^{1/40}⌋` (`listLen`), applies Lemma 36 with this `d`, and answers
every comparison count by Corollary 38.  The reductions behind Lemma 36 are cited and running times
are not defined here; this file checks the sums of the proof, in its order.  All that the sums use
about `d` is `1 ≤ d ≤ n^{1/40}` (`one_le_listLen`, `listLen_le_rpow`) and `1/d = O(n^{-1/40})`
(`isBigOPow_inv_listLen`).
* `d` meets the hypotheses of Lemma 36 and of Corollary 38 (`theorem_35_d`);
* a counting call costs `O(n^{2.0229} log n)` (`theorem_35_counting_call`, from
  `listLen_mul_sq_div_le` and `listLen_mul_rpow_le`), and forming its lists `O(n^{1.05})`
  (`theorem_35_forming_lists`);
* the `Õ(n/d)` counting calls cost `O(n^{2.998})` (`theorem_35_min_plus_total`), and so does the
  further time `Õ(n³/d)` (`theorem_35_further_time`);
* for 3SUM a comparison count costs `O(n^{1.9979} log n)` (`theorem_35_three_sum_count`), which
  gives `O(n^{1.998})` in all (`theorem_35_three_sum_total`);
* "with probability 1 - n^{-c}": Markov's inequality for one run (`theorem_35_one_run`) and
  independent restarts (`theorem_35_restarts`).


 ### The parameter d := ⌊n^{1/40}⌋ 

### `one_le_listLen`

 d ≥ 1. 

### `listLen_le_rpow`

 d ≤ n^{1/40}. 

### `isBigOPow_listLen`

 `d = O(n^{1/40})`. 

### `isBigOPow_inv_listLen`

 `1/d = O(n^{-1/40})`. 

### `isBigOPow_div_listLen`

 If `f(n) = O(n^a)`, then `f(n)/d = O(n^{a-1/40})`. 

### `isBigOPow_sq_div_listLen_rpow`

 `n²/d^{0.126} = O(n^{2-0.126/40})`. 

### `listLen_mul_sq_div_le`

 Proof of Theorem 35: "d · n²/d^{0.126} ≤ n^{2+0.874/40} ≤ n^{2.0219}". 

### `listLen_mul_rpow_le`

 Proof of Theorem 35: "d · n^{2-1/440} ≤ n^{2+1/40-1/440} ≤ n^{2.0228}". 

### `theorem_35_d`

 Proof of Theorem 35: "Let d := ⌊n^{1/40}⌋, apply Lemma 36 with this d, and answer every
comparison count by Corollary 38." This d satisfies the hypotheses 1 ≤ d ≤ n of Lemma 36 and d ≤
n^{1/40} of Corollary 38. 

### `theorem_35_counting_call`

 Proof of Theorem 35: "the d comparison counts of a counting call cost ∑_{k ∈ [d]} O(|P_k|
n^{0.0229} + n²/d^{0.126} + n^{2-1/440} log n) = O(n^{2.0229} log n), since ∑_k |P_k| = n²". `p k`
is |P_k|. 

### `theorem_35_forming_lists`

 Proof of Theorem 35: "forming the lists costs O(nd²) = O(n^{1.05})". 

### `theorem_35_min_plus_total`

 Proof of Theorem 35: "So the Õ(n/d) counting calls of Lemma 36(a) cost Õ((n/d) n^{2.0229}) =
Õ(n^{3-1/40+0.0229}) ≤ O(n^{2.998})". 

### `theorem_35_further_time`

 Proof of Theorem 35: "and its additional time is Õ(n³/d) = Õ(n^{2.975})" (which is
O(n^{2.998})). 

### `theorem_35_three_sum_count`

 Proof of Theorem 35, 3SUM: "a comparison count of Lemma 36(b) costs O((n²/d) n^{0.0229} +
n²/d^{0.126} + n^{2-1/440} log n) = O(n^{2-1/40+0.0229} log n) = O(n^{1.9979} log n)". 

### `theorem_35_three_sum_total`

 Proof of Theorem 35, 3SUM: "so 3SUM can also be solved in Õ(n^{1.9979}) ≤ O(n^{1.998}) expected
time"; the further time Õ(n²/d) of Lemma 36(b) is within the same bound. 

### `theorem_35_one_run`

 Proof of Theorem 35, "Las Vegas, and high probability": "we stop a run that exceeds twice the
bound on its expected time".  By Markov's inequality such a run is stopped with probability at most
1/2.  `T` is the running time of a run and `B` the bound on its expectation. 

### `theorem_35_restarts`

 Proof of Theorem 35: "and start again, and c log₂ n runs all fail with probability at most
n^{-c}".  `T i` is the running time of the i-th run; the runs are independent, and there are m ≥ c
log₂ n of them. (The m runs take 2Bm time in all, a factor O(log n) more than B; the bounds of
Theorem 35 still hold because `theorem_35_min_plus_total` and `theorem_35_three_sum_total` hold for
every power of the logarithm.) 
