---
{
  "module": "ThreeSumApsp/Sec4/Corollary26.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary26.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary26.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 26: the parameters `L = 21m`, `t = ⌈m/9⌉`

The proof of Corollary 26 from Theorem 30, in the five steps of the paper. The parts of these steps
that hold for all `L` and `t` are proved before (`Corollary26.setting_up` to
`dominated_cost8_of_eq_10`), and Corollary 31 uses them too. The exponents `γ` and `q` of the proof
are written `gammaOf 21 (1 / 9)` and `qOf (1 / 9)`: they are the `γ` and `q` of Corollary 31 at
`c = 21` and `θ = 1/9` (`Corollary26.gamma_eq`, `Corollary26.q_eq`). The result is
`Corollary26.costs`: for `N ≥ D^18` and `m = ⌈log_4 D⌉ ≥ 60` the hypothesis `N ≥ √K N₀` of Theorem
30 holds at `L = 21m` and `t = ⌈m/9⌉`, its preprocessing cost (8) (`cost8`) is `O(N²/D^{0.063})`,
and its query cost `L ∑_{d ≤ t} α_d` (`costQuery`) is `O(D^{0.437})`.

* Setting up. The inner dimension is padded to `D = 4^m` (`Corollary26.setting_up`). This changes no
  entry of the product (`Corollary26.padding`), it changes the bounds by a constant factor
  (`padded_le`), and the hypothesis reads `N ≥ 4^{18(m-1)}` (`Corollary26.hypothesis`). The number
  `t = ⌈m/9⌉` is `switchOf (1 / 9) m`, and `t ≤ m` (`switchOf_le`).
* Boxes. `ρ < 9/20` and `ρ^t ≤ (9/20)^{m/9} = D^{-γ}` with `γ = 0.0640…` (`Corollary26.rho_lt`,
  `Corollary26.rho_pow_le`, `Corollary26.gamma_digits`), so the first term of (8) is `O(m² N²/D^γ)`
  (`Corollary26.first_term`).
* Queries. `∑_{d ≤ t} α_d ≤ 72^t (9/8)^m < 72 D^q` with `q = 0.4277…` (`sum_alpha_le`,
  `Corollary26.sum_alpha_lt`, `Corollary26.q_digits`), so a query costs `O(m D^q)`
  (`Corollary26.query_cost`).
* Encodings. Inequality (10) bounds the last term of (8) and gives the hypothesis of Theorem 30
  (`Equation10.last_term`, `Equation10.tile_fits`). The standard bound on `K` (`Corollary26.le_K`)
  shows that the left-hand side of (10) is at most `√(21m+1) Λ^m` (`Corollary26.lhs10_le`);
  `Λ = 4.198… · 10^10` is below `4^18 = 6.871… · 10^10` by a factor of more than 1.63
  (`baseLambda_numeric`, `four_pow_eighteen_numeric`, `baseLambda_mul_lt`), and
  `1.63^m ≥ 4^18 √(21m+1)` for `m ≥ 60` (`Corollary26.threshold`). Together they give (10) for all
  `m ≥ 60` (`eq_10_corollary_26`).
* Conclusion. For `m ≥ 60` the hypothesis `N ≥ √K N₀` holds and (8) is `O(m² N²/D^γ)`
  (`Corollary26.tile_fits`, `dominated_cost8_of_eq_10`, `Corollary26.preprocessing`), the powers of
  `m` are absorbed into the exponents (`dominated_pow_mul_D_rpow`, `Corollary26.conclusion`), and
  the bounds are stated in the given `D` (`Corollary26.costs`). For `|W| ≤ N²/√D` queries the total
  is `O(N²/D^{0.063})` (`corollary_26_W`).

Bounds "up to a constant" are written with `Dominated`, in the one parameter `m` or in the record
`Sizes` of the given `D`, of `N` and of `m`. Two sentences of the proof are proved with the programs
(`wordRam_corollary_26`, `wordRam_corollary_26_wanted`): "(For m < 60, D is bounded by a constant,
and the corollary holds trivially.)" and "The bound for a set W follows by asking |W| queries." The
last section shows that the parameters of this proof are those of Corollary 31 and of Table 2 at
`c = 21` and `θ = 1/9`; nothing else rests on it.


 ### Setting up 

### `Corollary26.hypothesis`

 Proof of Corollary 26, "Setting up": "since the original D was larger than 4^{m-1}, the
assumption N ≥ D^18 now reads N ≥ 4^{18(m-1)}". 

 ### Boxes 

### `Corollary26.rho_lt`

 Proof of Corollary 26: "ρ = 9m/(L-m+1) = 9m/(20m+1) < 9/20, so 1/(1-ρ) < 2". 

### `Corollary26.rho_pow_le`

 Proof of Corollary 26: "since t ≥ m/9, also ρ^t ≤ (9/20)^{m/9} = D^{-γ}". 

### `Corollary26.gamma_eq`

 Proof of Corollary 26: "γ := ln(20/9)/(9 ln 4)". This is the `γ` of Corollary 31 at `c = 21` and
`θ = 1/9`, where `ρ_c = 9/20`; the statements of this file write it `gammaOf 21 (1 / 9)`. 

### `Corollary26.gamma_digits`

 Proof of Corollary 26: "γ := ln(20/9)/(9 ln 4) = 0.0640…". The digits come from the bounds on
logarithms proved for Table 2. 

### `Corollary26.first_term`

 Proof of Corollary 26: "Hence the first term of (8) is O(m² N²/D^γ)". The common factor `N²` is
left out. 

 ### Queries 

### `rpow_div_nine_eq`

 `72^{m/9} (9/8)^m = D^q`: at `θ = 1/9` the number `x = (1-θ)/θ` is 8. 

### `Corollary26.sum_alpha_lt`

 Proof of Corollary 26, the display of the step "Queries": "∑_{d=0}^{t} binom(m, d) 9^d ≤ 72^t
∑_{d=0}^{m} binom(m, d) 8^{-d} = 72^t (9/8)^m < 72 · (72 · (9/8)^9)^{m/9} = 72 D^q", with
`t = ⌈m/9⌉`. 

### `Corollary26.q_eq`

 Proof of Corollary 26: "q := ln(72 · (9/8)^9)/(9 ln 4)". This is the `q` of Corollary 31 at
`θ = 1/9`; the statements of this file write it `qOf (1 / 9)`. 

### `Corollary26.q_digits`

 Proof of Corollary 26: "q := ln(72 · (9/8)^9)/(9 ln 4) = 0.4277…". The digits come from the
bounds on logarithms proved for Table 2. 

### `Corollary26.query_cost`

 Proof of Corollary 26: "Hence a query takes O(L D^q) = O(m D^q) time." 

 ### Encodings 

### `Corollary26.le_K`

 Proof of Corollary 26: "the standard bound [...] gives K = binom(21m, m) ≥ 1/(21m+1) ·
(21^21/20^20)^m". 

### `baseLambda`

 The base `Λ` of the proof of Corollary 26: "Λ := 10^21 · (20/9)^{1/9} / ((21^21/20^20)^{1/2} ·
3^20)". 

### `Corollary26.lhs10_le`

 Proof of Corollary 26: "the left-hand side of (10) is at most √(21m+1) · Λ^m". 

### `baseLambda_numeric`

 Proof of Corollary 26: `Λ` "= 4.198… · 10^10". Eighteenth powers are compared: `Λ^18` is a
rational number. 

### `four_pow_eighteen_numeric`

 Proof of Corollary 26: "Its base 4^18 = 6.871… · 10^10". 

### `baseLambda_mul_lt`

 Proof of Corollary 26: `4^18` "is larger than Λ by a factor of more than 1.63". 

### `Corollary26.threshold`

 Proof of Corollary 26: "1.63^m ≥ 4^18 √(21m+1), which is the case for all m ≥ 60". 

### `eq_10_corollary_26`

 Equation (10), `D^γ · 10^L / (√K N₀) ≤ N`, where it is printed, in the proof of Corollary 26.
There `D = 4^m`, "L := 21m", "γ := ln(20/9)/(9 ln 4)", "K = binom(21m, m)", "N₀ = 3^{20m}", and "the
assumption N ≥ D^18 now reads N ≥ 4^{18(m-1)}". The inequality "holds whenever
1.63^m ≥ 4^18 √(21m+1), which is the case for all m ≥ 60". 

 ### Conclusion 

### `Sizes.Large26`

 The range of the step "Conclusion": "m ≥ 60", and "N ≥ 4^{18(m-1)}". 

### `Sizes.Large26.lhs10_le`

 Inequality (10) holds in this range (`eq_10_corollary_26`). 

### `Corollary26.tile_fits`

 Proof of Corollary 26, "Conclusion": "For m ≥ 60, Theorem 30 thus applies": its hypothesis
`N ≥ √K N₀` holds. 

### `Corollary26.preprocessing`

 Proof of Corollary 26, "Conclusion": "The preprocessing takes O(m² N²/D^γ) time and space". 

### `dominated_pow_mul_D_rpow`

 Proof of Corollary 26, "Conclusion": "Since m = O(log D) and the exponents γ - 0.063 and 0.437 -
q are positive, we have m² = O(D^{γ-0.063}) and m = O(D^{0.437-q})". In general, `m^e D^a = O(D^b)`
for `D = 4^m` and `a < b`. 

### `Corollary26.conclusion`

 Proof of Corollary 26, "Conclusion", with `D = 4^m`: "which gives the bounds O(N²/D^{0.063}) and
O(D^{0.437}) of the corollary". 

### `Sizes.Corollary26`

 The instances of Corollary 26 from the threshold on: `N ≥ D^{18}` and `m = ⌈log_4 D⌉ ≥ 60`. 

### `Sizes.Corollary26.setUp`

 `D ≥ 2`, since `m = 0` for `D ≤ 1`. 

### `Sizes.Corollary26.large`

 After "Setting up", these instances are in the range of the step "Conclusion". 

### `Corollary26.costs`

 Corollary 26, the costs of Theorem 30 at "L := 21m and t := ⌈m/9⌉", in terms of the given `D`:
there is a constant `C` such that for all `N ≥ D^{18}` with `m = ⌈log_4 D⌉ ≥ 60` the hypothesis
`N ≥ √K N₀` of Theorem 30 holds, the expression (8) is at most `C N²/D^{0.063}`, and the query cost
is at most `C D^{0.437}`. 

### `corollary_26_W`

 Corollary 26: `|W| D^{0.437} + N²/D^{0.063}` "is O(N²/D^{0.063}) whenever |W| ≤ N²/√D"
(with constant 2).

NOTE.  The paper states no lower bound on `D`; `D ≥ 1` is assumed, as in `Items.Corollary_26`. 

 ### The parameters `c = 21` and `θ = 1/9` of Corollary 31 and Table 2

The sentence before Corollary 26 says: "It is the entry c = 21, q = 0.43 of Table 2". The parameters
of the proof above are those of Corollary 31 at `c = 21`, `θ = 1/9`: this holds for `L`
(`levelsOf_21`), for `γ` and `q` (`Corollary26.gamma_eq` and `Corollary26.q_eq` above), and for `Λ`
(`baseLambda_eq_exp_lnΛ`). The condition `ε < R_c(γ)` holds at `ε = 1/18` (`Corollary26.Rc_digits`),
and `N ≥ D^18` gives the condition `D ≤ N^{0.056}` of the row `c = 21` of the table, which is
`table_2_c21` (`Corollary26.row_condition`). Nothing else rests on this section. 

### `levelsOf_21`

 "L := 21m" is the `L = ⌈cm⌉` of Corollary 31 at `c = 21`. 

### `baseLambda_eq_exp_lnΛ`

 Section 4.4: the `Λ` of (11), whose logarithm is `lnΛ c γ`, is "the general form of the base Λ
above". At `c = 21` and `θ = 1/9` it is the `Λ` of the proof of Corollary 26. 

### `Corollary26.Rc_digits`

 At `c = 21` and `θ = 1/9` the number `R_c(γ)` lies between 0.0566 and 0.0567, so the condition
`ε < R_c(γ)` of Corollary 31 holds at `ε = 1/18`. 

### `Corollary26.row_condition`

 Table 2: "every entry of the row holds whenever D ≤ N^ε", and the row `c = 21` has `ε = 0.056`.
Under the hypothesis `N ≥ D^{18}` of Corollary 26 this condition holds: `D ≤ N^{1/18}`, and
`1/18 < 0.056`. 
