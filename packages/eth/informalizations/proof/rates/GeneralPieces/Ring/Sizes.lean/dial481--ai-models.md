---
{
  "module": "proof/rates/GeneralPieces/Ring/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Ring/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers in the proof of the theorem on the pieces with ρ = 1/√2: sizes

Part of the paragraph "Sizes and operations" of that proof in Appendix B, as far as it states
numbers, with the numbers of the appendix:
the number Δ of the partitions of 0, …, 4h is at most (4h+1)·p(4h) (`Delta_le`); each entry of the
table of t_n·a' is a sum of at most 8h entries of the table of a', multiplied by integers of
absolute value at most 4h·2^{5h} (`coef_opMon_cons`, `card_terms_le`, `abs_mult_l_le`,
`abs_mult_k_le`); a monomial of weight at most h has at most h factors (`length_le`); all entries of
all
tables are at most (32h²·2^{5h})^h ≤ 2^{12h²} in absolute value (`abs_entry_le`, `pow_le`,
`abs_entry_le'`); each factor of displays (54) and (55) is a combination of entries with the
coefficients
of a^⟨i⟩ or b (`coef_op`), whose absolute values add up to at most 2^{3h} (`l1_angle_aFam_le`) and
h! (`l1_bFam_le`).
The recursion for the entries is taken from the integer matrices `ClauseBound.Boson.op`, which are
defined by (O2); `GeneralPieces.stBridge` says they are the matrices of the operators a[r]. The
running times are not part of this file. 

 ### The list of partitions 

### `Delta`

 Δ, the number of the partitions of 0, 1, …, 4h. 

### `p_mono`

 p is nondecreasing. 

### `Delta_le`

 Δ ≤ (4h+1)·p(4h). 

 ### One step of the computation of the tables 

### `bet_eq`

 The coefficient `ClauseBound.Boson.bet n r` of the matrices `ClauseBound.Boson.op` is C(r−1,
n−1) for r ≠ 0. 

### `coef_opMon_cons`

 By (O2), since ∇_k t^σ = k·m_k(σ)·t^σ/t_k and the coefficient of t^{σ'} in t_l·f is that of
t^{σ'}/t_l in f: an entry of the table of t_n·a' as a combination of entries of the table of a'.
The sums run over the different parts l of σ' and k of σ. Proved from the recursion that defines the
matrices `ClauseBound.Boson.op`, which is (O2), through `GeneralPieces.stBridge`. 

### `card_le_wt`

 A partition has at most as many parts as its weight. 

### `card_terms_le`

 The sum has at most 8h terms. 

### `mul_count_le_wt`

 k·m_k(σ) ≤ |σ|. 

### `abs_mult_l_le`

 The multipliers of the first sum are at most 4h·2^{5h} in absolute value. 

### `abs_mult_k_le`

 The multipliers of the second sum are at most 4h·2^{5h} in absolute value. 

 ### All entries of all tables 

### `length_le`

 A monomial has at most as many factors as its weight; so a monomial of weight at most h has at
most h factors. 

### `abs_entry_le`

 An entry of the table of a monomial with q factors, each t_n with n ≤ h, is at most
(32h²·2^{5h})^q in absolute value. 

### `pow_le`

 (32h²·2^{5h})^h ≤ 2^{12h²}, for h ≥ 1. 

### `abs_entry_le'`

 All entries of the tables of the monomials of weight at most h are at most 2^{12h²} in absolute
value. 

 ### The sum of the absolute values of the coefficients 

### `l1`

 The sum of the absolute values of the coefficients of a polynomial. 

### `l1_y_le`

 The coefficients of y_n add up to at most 2^n. 

### `l1_aFam_le`

 The absolute values of the coefficients of a^μ add up to at most ∏_i 2^{μ_i} = 2^{|μ|}. 

### `coeff_angle`

 The coefficients of a^⟨i⟩: C(h'+h, i) times those of a at the monomials of weight h' ≤ h, and 0
at the others. 

### `l1_angle_le`

 The absolute values of the coefficients of a^⟨i⟩ add up to at most 2^{2h} times the sum for a. 

### `l1_angle_aFam_le`

 The absolute values of the coefficients of a^⟨i⟩, for a = a^μ and a partition μ of h, add up to
at most 2^{2h}·∏_i 2^{μ_i} = 2^{3h}. 

### `zz_pos`

 z_μ ≥ 1. 

### `l1_bFam_le`

 b^μ has one coefficient, h!/z_μ with h = |μ|; it is at most h!. 

 ### The factors of displays (54) and (55) 

### `coef_op`

 Each coefficient of a[r]·t^σ is a combination of entries of the tables of the monomials of a,
with the coefficients of a. 

### `abs_coef_op_le`

 If all monomials of a have weight at most h, a coefficient of a[r]·t^σ at listed partitions is
at most 2^{12h²} times the sum of the absolute values of the coefficients of a. 

### `abs_factor_a_le`

 The factors with a^⟨i⟩ in (54) and (55) are at most 2^{3h}·2^{12h²} in absolute value. 

### `abs_factor_b_le`

 The factors with b in (54) and (55) are at most h!·2^{12h²} in absolute value. 
