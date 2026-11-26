---
{
  "module": "ThreeSumApsp/Sec4/ParameterSteps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/ParameterSteps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/ParameterSteps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4: the steps of the proof of Corollary 26 that hold for all parameters

The proof of Corollary 31 begins: "We repeat the proof of Corollary 26 with L := ⌈cm⌉ and t :=
⌈θm⌉". This file has the parts of the proof of Corollary 26 that mention neither `L = 21m` nor
`t = ⌈m/9⌉`, under the headings of that proof. Both corollaries use them.

* Setting up. The inner dimension is padded to `D = 4^m` with `m = ⌈log_4 D⌉`
  (`Corollary26.setting_up`). This changes no entry of the product (`Corollary26.padding`), and it
  changes the bounds by a constant factor (`padded_le`). The switching order `t = ⌈θm⌉` is
  `switchOf θ m`, and `t ≤ m` (`switchOf_le`).
* Queries. `∑_{d ≤ t} α_d ≤ (9x)^t (1 + 1/x)^m` for every `x ≥ 1/9` (`sum_alpha_le`), and for
  `x = (1-θ)/θ` the right-hand side at `t = θm` is `D^q` (`rpow_mul_pow_eq_D_rpow_qOf`).
* Encodings. Inequality (10), whose left-hand side is `lhs10 L m γ`, bounds the last term of (8) and
  gives the hypothesis `N ≥ √K N₀` of Theorem 30 (`Equation10.last_term`, `Equation10.tile_fits`).
* Conclusion. The expression (8) from a bound on its first term and (10)
  (`dominated_cost8_of_eq_10`).

Bounds "up to a constant" are written with `Dominated`, in the one parameter `m` or in the record
`Sizes` of the given inner dimension, of `N` and of `m`.


 ### Setting up 

### `Corollary26.setting_up`

 Proof of Corollary 26, "Setting up": for "m := ⌈log_4 D⌉" and `D ≥ 2` the padded inner dimension
satisfies `D ≤ 4^m` and "4^m < 4D", and "the original D was larger than 4^{m-1}". 

### `Corollary26.padding`

 Proof of Corollary 26, "Setting up": "pad the inner dimension to 4^m < 4D with zero columns of X
and zero rows of Y. This changes no entry of XY". 

### `Sizes`

 The numbers in which the bounds of Section 4.4 are stated. 

### `Sizes.D₀`

 The given inner dimension, before the padding. 

### `Sizes.N`

 The size of the product: the matrices are `N × D₀` and `D₀ × N`. 

### `Sizes.m`

 The padded inner dimension is `D = 4^m`. 

### `Sizes.SetUp`

 Proof of Corollary 26, "Setting up": "m := ⌈log_4 D⌉", for a given inner dimension `D₀ ≥ 2`. 

### `Sizes.SetUp.le`

 The padded inner dimension is at least the given one. 

### `Sizes.SetUp.lt`

 "4^m < 4D". 

### `Sizes.SetUp.gt`

 "the original D was larger than 4^{m-1}". 

### `Sizes.SetUp.m_pos`

 `m ≥ 1`, because `2 ≤ D₀ ≤ 4^m`. 

### `padded_le`

 Proof of Corollary 26, "Setting up": padding "changes D by a factor less than 4, which only
affects the constants". A bound `D^a log^k D` in the padded `D = 4^m` is, up to a constant, the same
bound in the original inner dimension `D₀`. (Corollary 26 has `k = 0`; the bounds of Corollary 31
have logarithms.) 

### `switchOf`

 The switching order `t = ⌈θm⌉`: "t := ⌈m/9⌉" in the proof of Corollary 26, where `θ = 1/9`, and
"t := ⌈θm⌉" in the proof of Corollary 31. 

### `switchOf_le`

 The hypothesis `t ≤ m` of Theorem 30 holds for `t = ⌈θm⌉` with `θ ≤ 1`. 

 ### Queries 

### `sum_alpha_le`

 Proof of Corollary 26, "Queries": "A query reads ∑_{d≤t} α_d numbers, and we bound this sum as
in the proof of Lemma 11. Since 9^d = 72^d 8^{-d} ≤ 72^t 8^{-d} for d ≤ t", the sum `∑_{d ≤ t} α_d`
is at most `72^t ∑_{d=0}^{m} binom(m, d) 8^{-d} = 72^t (9/8)^m`. Here any `x > 0` with `9x ≥ 1`
stands for 8, because the proof of Corollary 31 makes "the same calculation with x := (1-θ)/θ in
place of 8". 

### `rpow_mul_pow_eq_D_rpow_qOf`

 `(9x)^{θm} (1+1/x)^m = D^q` for "x := (1-θ)/θ". 

 ### Encodings 

### `lhs10`

 The left-hand side of (10): "D^γ · 10^L / (√K N₀)", with `D = 4^m`. Inequality (10) says that it
is at most `N`. 

### `Equation10.last_term`

 Proof of Corollary 26: (10) implies "that the last term of (8) is at most N²/D^γ", "by
rearranging". 

### `Equation10.tile_fits`

 Proof of Corollary 26: (10) implies "that N ≥ √K N₀", "because 10^L ≥ M = K N₀² and D^γ ≥ 1"
(here `γ ≥ 0`). 

 ### Conclusion 

### `dominated_cost8_of_eq_10`

 The expression (8) from its two terms, with `L` and `t` given as functions of `m`. If the first
term, without its factor `N²`, is `O(G)`, where `G ≥ D^{-γ}`, then (8) is `O(G N²)` wherever (10)
holds. 
