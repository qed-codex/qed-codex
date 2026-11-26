---
{
  "module": "proof/variables/RecursionToBound/Numbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Numbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Numbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem D (a) along the printed Step 5: the numbers

* `eps_between`: «Take ε ≤ 1 between e and 2e» (Step 5 of Appendix D): ε = min(a/b, 1) is such a
  number if a/b is in [e, 2e] and e ≤ 1.
* `occBoundIsThePrinted`: 2·(θ₀ + … + θ_(k−1)) + 2 ≤ 2·(8k/ε)^(3k) + 2, where θ₀, …, θ_(k−1) are the
  k thresholds of Calabro's sparsification algorithm that `thresholds` computes; from the two
  statements on these thresholds `SparsificationLemma.Cal.StDegSum` and
  `SparsificationLemma.Cal.StDegLe`.
* `boundsGrowWithDelta`: each of the four bounds is made of sums, products, powers and rounded
  logarithms of Δ with coefficients that are not negative.
* `cutOffIsIdle`: k ≤ k⁴ ≤ log n gives 2^k ≤ n.
* `outputsAreWithinTheSetting`: «so log Δ ≤ 3k·log(8k/e) + 2 … which is at most 4kC₀·log log n for
  large n». Here n is large if log log n ≥ 40 and n is at least the n₀ of «Setting and parameters»
  (`MainTheoremForms.SettingN0Stmt`), which gives Δ ≤ n^(1/(40C₀)) ≤ n. For the bound n ≥
  29·⌈log₂(2Δ)⌉ + 19: ⌈log₂(2Δ)⌉ ≤ log n + 2 and 30·log n ≤ n because (log n)³ ≤ n². 

 ### ε 

### `epsOf_pos`

 ε > 0 for a fraction with positive numerator and denominator. 

### `epsOf_le_one`

 ε ≤ 1. 

### `epsOf_cast`

 ε as a real number is min(a/b, 1). 

### `pos_of_le_div`

 A fraction a/b that is at least e > 0 has a > 0 and b > 0. 

### `eps_between`

 «Take ε ≤ 1 between e and 2e»: if e ≤ a/b ≤ 2e and e ≤ 1, then e ≤ ε ≤ 2e and ε ≤ 1 for ε =
min(a/b, 1). 

 ### The bound on the occurrences 

### `occBoundIsThePrinted`

 «So every variable occurs in at most 2(8k/ε)^(3k) + 2 clauses of each output» (Step 5 of
Appendix D): the bound that the function computes is at most the printed one. 

 ### The bounds grow with Δ 

### `LD_mono`

 ⌈log₂(2Δ)⌉ grows with Δ. 

### `objMax_mono`

 The bound on the number of objects grows with Δ. 

### `boundsGrowWithDelta`

 The bounds on the total, on P, on the number of profiles and on the size s̄ of a check grow with
Δ. 

 ### The cut-off of k 

### `cutOffIsIdle`

 In the range of Theorem D (a) the cut-off of k at ⌊log₂(n+1)⌋ does nothing. 

 ### Logarithms 

### `pow_eq_two_rpow`

 x^j = 2^{j·log x} for x > 0. 

### `lg_eight_mul`

 log(8x) = 3 + log x for x > 0. 

### `lg_eight_div`

 log(8k/e) = 3 + log(k/e) for k, e > 0. 

### `lg_div_le`

 «As e ≥ (log n)^(−C₀) and k ≤ (log n)^(1/4)»: log(k/e) ≤ (C₀ + 1/4)·log log n, for k ≥ 1. 

### `lg_le_of_le_pow`

 If Δ ≤ 2·a^j + 2 with a ≥ 1, then log Δ ≤ j·log a + 2, for Δ ≥ 1. 

### `lin_lg_le`

 If log n ≥ 900, then 29·(log n + 2) + 19 ≤ n. 

### `LD_le_lg`

 ⌈log₂(2Δ)⌉ ≤ log n + 2 for Δ ≤ n, n ≥ 1. 

 ### Every Δ up to the bound on the occurrences is within «Setting and parameters» 

### `outputsAreWithinTheSetting`

 «… so log Δ ≤ 3k·log(8k/e) + 2 = O(k·log(k/e)). As e ≥ (log n)^(−C₀) and k ≤ (log n)^(1/4), this
is at most 3k(3 + (C₀ + 1/4)·log log n) + 2, which is at most 4kC₀·log log n for large n, because C₀
≥ 1» (Step 5 of Appendix D), for every Δ from 2 to the bound on the occurrences; with Δ ≤ n + 1 and
n ≥ 29·⌈log₂(2Δ)⌉ + 19. 
