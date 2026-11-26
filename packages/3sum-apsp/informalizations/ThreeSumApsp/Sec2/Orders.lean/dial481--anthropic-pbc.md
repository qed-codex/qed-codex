---
{
  "module": "ThreeSumApsp/Sec2/Orders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Orders.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Orders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 2.4.3, first half: the orders of the leaves and equation (5)

A leaf that contributes to an output string with inner set `Q` is free at the `m` levels of `Q` and
fixed at the other levels.  Its order is `m` minus the number of levels at which it chooses `P₀`.

* One level.  A term contributes to `z` exactly if `z = z₀` or the term is the private term of `z`
  (`Term.contributes_iff`), so a leaf contributing to a string chooses `P₀` only at levels of the
  inner set (`P0Levels_subset`).  The numbers of terms of each kind that contribute to a variable,
  and of variables of each kind to which a term contributes, are read off the ten terms.
* Counts.  `10^m` leaves contribute to a string: ten terms for each level of `Q`
  (`card_filter_contributes`).  The other counts sort strings by the set of levels at which they
  have a letter of a given kind (`Finset.card_pi_places_card`, `Finset.card_places_card`): `α_d` of
  the leaves contributing to a string have order `d` (`sec2_card_contributing_of_order`), the whole
  tree has `β_d` leaves of order `d` (`card_filter_order_eq`), with `β₀ = M` (`beta_zero_eq_M`), and
  a leaf of order `d` contributes to `binom(L-m+d, d)` strings (`sec2_card_outStr_of_leaf`). Figure
  6 shows these numbers for `L = 6` and `m = 2` (`figure_6`).
* Equation (5): the quotient `β_d / β_{d-1}` comes from the recurrence of the binomial coefficients
  (`Equation5.ratio_nat`, `eq_5_ratio`); for `L = 19m` it is less than `1/2` (`eq_5_bound`); so
  `β_d ≤ 2^{-d} M` by induction on `d` (`eq_5`).


 ### One level: which terms contribute to which variables 

### `OutVar.privateTerm_eq_P0_iff`

 The private term of `z` is `P₀` exactly if `z = z₀`. 

### `card_term_P0`

 One term is `P₀`. 

### `card_term_ne_P0`

 Nine terms are different from `P₀`. 

### `card_contributing_P0`

 Among the terms contributing to `z`, the number of those equal to `P₀`: one if `z = z₀`, none if
`z = z_ij`. 

### `card_contributing_ne_P0`

 Among the terms contributing to `z`, the number of those different from `P₀`: nine if `z = z₀`,
one if `z = z_ij`. 

### `card_contributing_term`

 The number of terms contributing to `z`: ten if `z = z₀`, one if `z = z_ij`. 

### `card_contributed_inner`

 Among the output variables to which `lam` contributes, exactly one is inner. 

### `card_contributed_outer`

 Among the output variables to which `lam` contributes, the number of outer ones: none if
`lam = P₀`, one if `lam = P_ij`. 

 ### The order of a leaf 

### `mem_P0Levels`

 Membership in the set of levels at which a leaf chooses `P₀`. 

### `mem_innerSetO`

 Membership in the inner set of an output string. 

### `P0Levels_subset`

 Section 2.4.3: "A leaf contributing to an output string chooses P₀ only at levels of the output
string's inner set". 

### `order_nonneg`

 Section 2.4.3: "so its order is at least 0." 

### `order_le`

 In the proof of Lemma 11: "every leaf of Leaves(U) has an order 0 ≤ d ≤ m".  The upper
bound holds for every leaf. 

### `order_eq_iff`

 A leaf has order `d` exactly if it chooses `P₀` at `m - d` levels. 

 ### The counts 

### `card_filter_contributes`

 Section 2.4.3: "A single output string has 10^m […] leaves contributing to it." 

### `sec2_card_contributing_of_order`

 Section 2.4.3: "exactly α_d := binom(m, d) 9^d leaves of order d contribute to an output
string".  As everywhere in Section 2.4.3, the output strings are those whose inner sets have exactly
m elements. 

### `card_filter_order_eq`

 Section 2.4.3: "The total number of leaves of order d in the entire recursion tree is
β_d := binom(L, m-d) 9^{L-m+d}".

NOTE.  `d ≤ m` and `m ≤ L` are left implicit in the paper. 

### `beta_zero`

 Section 2.4.3: "In particular, β₀ = binom(L, m) 9^{L-m}". 

### `beta_zero_eq_M`

 Section 2.4.3: "β₀ = binom(L, m) 9^{L-m} = M". 

### `sec2_card_outStr_of_leaf`

 Section 2.4.3: "A leaf of order d contributes to binom(L-m+d, d) output strings, one for each
inner set of size m that contains the m-d levels at which it chooses P₀."  Only the number is
stated.  As everywhere in Section 2.4.3, the output strings are those whose inner sets have exactly
m elements.

NOTE.  `m ≤ L` is left implicit in the paper. 

### `beta_pos`

 `β_d` is positive when `m ≤ L`. 

### `Equation5.ratio_nat`

 The equality in equation (5) without division: `β_d (L-m+d) = 9 (m-d+1) β_{d-1}` for
`1 ≤ d ≤ m ≤ L`. 

### `eq_5_ratio`

 Section 2.4.3, the equality in equation (5), for every `L ≥ m` (it is used again as equation (7)
in Section 4.3): "β_d / β_{d-1} = 9(m-d+1) / (L-m+d)" for `1 ≤ d ≤ m`.

NOTE.  The paper prints the equality under `L = 19m` in (5) and under `L ≥ 10m` in (7); here it is
stated for every `L ≥ m`. 

### `eq_5_bound`

 Section 2.4.3, the inequalities in equation (5): "if L = 19m, then for 1 ≤ d ≤ m we have
β_d / β_{d-1} = 9(m-d+1)/(L-m+d) ≤ 9m/(18m+1) < 1/2". 

### `eq_5`

 **Equation (5)**, conclusion: if `L = 19m` then "β_d ≤ 2^{-d} M", for `0 ≤ d ≤ m`.
The inequality is multiplied out. 

### `figure_6`

 Figure 6, for `L = 6`, `m = 2` and the output string `w = z₁₃ z₀ z₂₁ z₃₃ z₀ z₁₂` of
Figure 4: its private leaf is `P₁₃ P₀ P₂₁ P₃₃ P₀ P₁₂`, and the numbers of the figure, evaluated:
`α₀ = 1`, `α₁ = 18`, `α₂ = 81`, `binom(5, 1) = 5` and `binom(6, 2) = 15` (the "1 output string" of
the private leaf, `binom(4, 0) = 1`, is left out).  That `α_d` leaves of order `d` contribute to
`w`, and that a leaf of order `d` contributes to `binom(L-m+d, d)` output strings, is stated in
general by `sec2_card_contributing_of_order` and `sec2_card_outStr_of_leaf`. 
