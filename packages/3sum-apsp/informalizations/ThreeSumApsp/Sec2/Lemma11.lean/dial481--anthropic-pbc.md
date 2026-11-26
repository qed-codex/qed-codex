---
{
  "module": "ThreeSumApsp/Sec2/Lemma11.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma11.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Lemma11.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 2.4.3, second half: Lemma 11

Few leaves contribute to a sparse set `U` of output strings.  From Section 2.4.3 on, `L = 19m`
(`N0_nineteen_mul`), and powers of 2 stand for powers of `D = 4^m`: `2^m = √D`
(`two_pow_eq_sqrt_D`), and the factor `2^{-m/9} = D^{-1/18}` is called `saving m`
(`saving_eq_D_rpow`).

* First inequality (`Lemma11.first_inequality`).  The leaves of `Leaves(U)` of order `d` number at
  most `|U| α_d`, charging each string for its leaves, and at most `β_d`, the number of all leaves
  of that order (`card_Leaves_filter_order_le`).  Sum the smaller bound over `0 ≤ d ≤ m`.
* Second inequality, for `L = 19m` (`Lemma11.second_inequality`).  Use `|U| α_d` for the orders
  `d ≤ m/9` and `β_d` for the others (`card_Leaves_le_split`).  The orders `d ≤ m/9` give
  `∑ α_d < 2^m · 2^{-m/9}` by the binomial theorem (`sum_alpha_small_orders_lt`); the orders
  `d > m/9` give `∑ β_d < 2 · 2^{-m/9} M` by equation (5) and a geometric series
  (`sum_beta_large_orders_lt`).


 ### The parameters from Section 2.4.3 on 

### `N0_nineteen_mul`

 Section 2.4.3: "From now on, we fix L = 19m, so that N₀ = 3^{18m}". 

### `M_pos`

 `M` is positive when `m ≤ L`. 

### `D_eq_two_pow`

 `D = 4^m = 2^{2m}`. 

### `two_pow_eq_sqrt_D`

 Section 2.4.3: "Recall that D = 4^m, so 2^m = √D". 

### `saving`

 The factor `2^{-m/9}` of Sections 2.4.3 and 2.4.4, by which the costs of the algorithm of
Theorem 5 lie below `N²`. 

### `saving_pos`

 `2^{-m/9}` is positive. 

### `saving_le_one`

 `2^{-m/9} ≤ 1`. 

### `saving_mul_two_rpow`

 `2^{-m/9} · 2^{m/9} = 1`. 

### `saving_eq_D_rpow`

 Section 2.4.3: "and 2^{-m/9} = D^{-1/18}." 

 ### The first inequality 

### `card_Leaves_filter_order_le`

 In the proof of Lemma 11: "We bound the number of leaves of order d in Leaves(U) in two
ways: by |U| α_d, charging each output string of U for its leaves of order d, and by β_d, the number
of all leaves of order d." Quoted again in Section 4.3: "At every order d, the pruned recursion of
Section 2.4 visits at most min{|U| α_d, β_d} leaves". 

### `Lemma11.first_inequality`

 **Lemma 11**, first inequality.  "For every set U of output strings whose inner sets have
exactly m elements, |Leaves(U)| ≤ ∑_{d=0}^{m} min{|U| α_d, β_d}". 

 ### The second inequality 

### `beta_le_M_mul`

 Equation (5) over the reals: `β_d ≤ M 2^{-d}` for `0 ≤ d ≤ m` and `L = 19m`. 

### `sum_beta_lt_of_subset`

 By (5), the orders `d ≥ a` contribute `∑ β_d ≤ M ∑_{d ≥ a} 2^{-d} < 2 · 2^{-a} M`. 

### `sum_beta_large_orders_lt`

 In the proof of Lemma 11: "The orders d > m/9 contribute at most
∑_{d>m/9} β_d ≤ M ∑_{d>m/9} 2^{-d} < 2 · 2^{-m/9} M by (5)." 

### `alpha_le`

 One term of the display in the proof of Lemma 11: `binom(m, d) 9^d = binom(m, d) 72^d 8^{-d}`,
which is at most `72^{m/9} binom(m, d) 8^{-d}` for `d ≤ m/9`.  The factor `1^{m-d}` makes the right
side a term of the expansion of `(1/8 + 1)^m`. 

### `sum_alpha_small_orders_le_aux`

 The first two steps of the display in the proof of Lemma 11:
`∑_{d ≤ m/9} binom(m, d) 9^d ≤ 72^{m/9} ∑_{d=0}^{m} binom(m, d) 8^{-d} = 72^{m/9} (9/8)^m`. 

### `sum_alpha_small_orders_lt`

 The display in the proof of Lemma 11: "∑_{d ≤ m/9} binom(m, d) 9^d ≤ 72^{m/9}
∑_{d=0}^{m} binom(m, d) 8^{-d} = 72^{m/9} (9/8)^m = (72 · (9/8)^9)^{m/9} < 256^{m/9} = 2^m ·
2^{-m/9}".

NOTE.  The strict inequality needs `m ≥ 1`, which is fixed in Section 2.3.3; for `m = 0` both ends
are 1. 

### `sum_alpha_small_orders_le`

 The bound of `sum_alpha_small_orders_lt` with `≤`, which also holds for `m = 0`. 

### `card_Leaves_le_split`

 In the proof of Lemma 11: "We use |U| α_d for the orders d ≤ m/9 and β_d for the orders
d > m/9". 

### `Lemma11.second_inequality`

 **Lemma 11**, second inequality.
"and if L = 19m, then |Leaves(U)| ≤ 2^{-m/9} (2^m |U| + 2M)." 

### `lemma_11`

 **Lemma 11**, both inequalities together.  "For every set U of output strings whose inner
sets have exactly m elements, |Leaves(U)| ≤ ∑_{d=0}^{m} min{|U| α_d, β_d}, and if L = 19m,
then |Leaves(U)| ≤ 2^{-m/9} (2^m |U| + 2M)." 
