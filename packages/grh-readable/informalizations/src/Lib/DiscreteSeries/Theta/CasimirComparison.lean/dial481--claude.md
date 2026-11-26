---
{
  "module": "src/Lib/DiscreteSeries/Theta/CasimirComparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/CasimirComparison.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/CasimirComparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Casimir elements of an oscillator pair

An oscillator pair is given by a `FockDualPair` `T` with `n = card R` rows and `n' = card C`
columns; the first group acts on the rows. This file proves that, with the centres (the weights of
the twisting characters) removed, the Casimir elements of the two groups differ by the constant
`n n' (n - n') / 4`, and that for matching parameters the numbers `|u|² - |ρ|²` and `|u'|² - |ρ'|²`
differ by the same constant, where `u`, `u'` are the centred parameters, that is, the entries
shifted by the centres. By `HCParam.HasGap.casimirValue_sub_centre` these numbers are the centred
Casimir values.

The notions that the statements use:
* a parameter `l : HCParam ε` is an integer vector that stands for `l = 2λ`; `l.HasGap h` says that
  its entries are distinct, of the parity of `n - 1`, and at least `2h` apart where the signs `ε`
  differ;
* for symmetric `r`, `twoRho l r` is the sum of the roots selected by `r` that are positive for `l`,
  so `twoRho l ⊤` is `2ρ`, and `l.casimirValue` is `|λ|² - |ρ|²`;
* `T.oscRows` is the oscillator action of `gl R` on polynomials, and `T.swap` is the same pair with
  rows and columns exchanged;
* `T.centredParam l r` is `2u_r = l r - 2γ + n'` with `γ = T.rowShift` the scalar on the diagonal of
  the row action (`T.columnShift` is that of the column action `T.swap.oscRows`), and
  `IsMatch T l l'` says that `l` and `l'` have gap `500 (n + n')³`, that each row is matched with a
  column or has `|2u_r| < n - n'`, and that each column is matched with a row or has
  `|2u'_c| < n' - n`; the row `r` and the column `c` are matched if `u_r = -u'_c` and
  `T.globalSign * ε r * ε' c * 2u_r > |n - n'|`.

## Relation to the literature

Known result: the constant difference of the centred Casimir elements of the two groups of an
oscillator pair, a case of the correspondence of infinitesimal characters. Source: compare A. Paul,
First occurrence for the dual pairs (U(p,q), U(r,s)), Canad. J. Math. 51 (1999), Theorem 2.11.

See also `Lib.DiscreteSeries.Theta.LocalCorrespondence`.


### `three_mul_sum_range_two_mul_sub_sq`

 The sum `∑ (2k - c)²` over `k < d`, times `3`, in closed form. 

### `three_mul_sum_sq_of_injOn`

 A set of `d` distinct integers of the parity of `d - 1` and of modulus below `d` is
`{1 - d, 3 - d, …, d - 1}`, so the sum of their squares is `d (d² - 1) / 3`. 

### `three_mul_sum_twoRho_sq`

 For a vector `l` with distinct entries, `twoRho l ⊤ = 2ρ` is the sum of the roots positive for
`l`. The squares of its entries sum to `N (N² - 1) / 3` with `N = card n`, that is,
`|ρ|² = N (N² - 1) / 12`. 

### `sum_twoRho_eq_zero`

 For a symmetric relation `r`, the entries of `twoRho l r` sum to zero. 

### `HCParam.HasGap.two_mul_sum_lowestKType`

 For a parameter `l = 2λ` with a gap (distinct entries of the parity of `n - 1`, those of
different signs `ε` far apart), the lowest K-type and `λ` have the same sum of entries. 

### `HCParam.HasGap.casimirValue_sub_centre`

 Let `l = 2λ` be a parameter with a gap (distinct entries of the parity of `n - 1`, those of
different signs far apart), with Casimir value `κ = |λ|² - |ρ|²` and lowest K-type `μ`. For any
scalar `w`, the value with the centre `w` removed, `κ - 2w ∑ μ_a + n w²`, is
`∑ (λ_a - w)² - n (n² - 1) / 12`, where `n` is the number of entries. 

### `FockDualPair.centredParam_injective`

 The centred parameters `l r - 2γ + card C` of a vector `l` with distinct entries are
distinct. 

### `IsMatch.three_mul_sum_sq_sub_of_le`

 Let `l`, `l'` be matching parameters of the pair `T`: they have a large gap, and each row and
column is matched, with opposite centred parameters, or has a small one. Let `n' ≤ n` for
`n = card R` and `n' = card C`. The squares of the centred parameters `l r - 2 T.rowShift + n'` of
the rows and `l' c - 2 T.columnShift + n` of the columns (the rows of `T.swap`) differ in sum by
`d₀ (d₀² - 1) / 3` with `d₀ = n - n'`, the share of the unmatched rows. 

### `IsMatch.three_mul_sum_sq_sub`

 For matching parameters `l`, `l'` of the pair `T`, the squares of the centred parameters
`l r - 2γ + n'` of the rows and `l' c - 2γ' + n` of the columns differ in sum by `d₀ (d₀² - 1) / 3`,
where `n = card R`, `n' = card C`, and `d₀ = n - n'` may have either sign. 

### `sum_add_scalar_mul_add_scalar`

 For a square array `F` in a complex algebra, adding a scalar `t` to the diagonal adds
`2t ∑ F_aa + n t²` to `∑ F_ab F_ba`, where `n = card R`. 

### `sum_mul_eq_normal_order`

 Normal ordering. Let `x`, `d` be arrays in a complex algebra with
`d_rc x_rc' = x_rc' d_rc + δ_cc'`. With `n = card R` and `n' = card C`, the Casimir sum of the
elements `∑ c, x_ac d_bc + (n'/2) δ_ab` is `D₄ + (n + n') D₂ + n n'² / 4`, where
`D₄ = ∑ x_ac x_bc' d_bc d_ac'` and `D₂ = ∑ x_rc d_rc`. 

### `GlModule.centredCasimir`

 The Casimir element with the centre `w` removed: it is formed with `E_ab - w δ_ab` in place of
`E_ab`. 

### `GlModule.centredCasimir_apply`

 On a vector of weight `ν`, the Casimir element with the centre `w` removed is
`Ω - 2w ∑ ν_a + n w²`, where `n = card R`. Here `Ω = ρ.casimirK 1` is the full Casimir element
`∑ E_ab E_ba`: all signs are `1`, so every pair of indices counts. 

### `centre`

 The centre `w` of the action on the rows: the scalar `T.rowShift` on the diagonal is `w + n'/2`.
It is the weight of the character of the determinant by which the action is twisted. 

### `raise`

 The operator `x_rc`: for the variable `T.varEquiv (r, c)` of `MvPolynomial ι ℂ` attached to the
entry `(r, c)`, multiplication by the variable where its sign `T.indexSign` is `+`, minus the
derivative where it is `-`. 

### `lower`

 The operator `d_rc`: for the variable `T.varEquiv (r, c)` of `MvPolynomial ι ℂ` attached to the
entry `(r, c)`, the derivative where the sign `T.indexSign` of the variable is `+`, multiplication
by the variable where it is `-`. 

### `quarticOp`

 The operator `D₄ = ∑ x_ac x_bc' d_bc d_ac'` of a Fock dual pair, over all rows `a`, `b` and
columns `c`, `c'`. 

### `quadraticOp`

 The operator `D₂ = ∑ x_rc d_rc` of a Fock dual pair, over all rows `r` and columns `c`. 

### `lower_mul_raise`

 The canonical commutation relation `d_rc x_r'c' = x_r'c' d_rc + δ_rr' δ_cc'` of the operators
`T.lower` and `T.raise`. 

### `sum_columns_eq_quarticOp`

 `D₄` summed first over the columns: since the `d_rc` commute, the last two factors may be
exchanged. 

### `sign_mul_sign`

 For signs `δ` and a sign `s` (read in `ℂ`), the factor that is `1` if `δ a = δ b` and `s`
otherwise, times the same factor for `(b, a)`, is `1`. So these factors drop out of a Casimir
element. 

### `oscRows_E_sub_centre`

 The row action of the matrix unit `(a, b)` less `T.centre = T.rowShift - n'/2` on the diagonal
is `∑ c, x_ac d_bc + (n'/2) δ_ab`, times the sign `T.globalSign` of the pair where the signs `ε a`,
`ε b` differ; here `n' = card C`, `x = T.raise` and `d = T.lower`. 

### `swap_oscRows_E_sub_centre`

 The column action of the matrix unit `(a, b)` less `T.swap.centre = T.columnShift - n/2` on the
diagonal is `-(∑ r, x_rb d_ra + (n/2) δ_ab)`, times the sign `T.globalSign` of the pair where the
signs `ε' a`, `ε' b` differ; here `n = card R`, `x = T.raise`, `d = T.lower`, and `T.swap` is `T`
with rows and columns exchanged. 

### `centredCasimir_oscRows`

 The Casimir element of the row action `T.oscRows` with the centre `T.centre` removed is
`D₄ + (n + n') D₂ + n n'² / 4`, where `D₄ = T.quarticOp`, `D₂ = T.quadraticOp`, `n = card R` and
`n' = card C`. 

### `centredCasimir_swap_oscRows`

 The Casimir element of the column action `T.swap.oscRows` with the centre `T.swap.centre`
removed is `D₄ + (n + n') D₂ + n² n' / 4`, where `D₄ = T.quarticOp`, `D₂ = T.quadraticOp`,
`n = card R` and `n' = card C`. 

### `centredCasimir_swap_oscRows_eq_add`

 The centred Casimir element of the column action `T.swap.oscRows` is that of the row action
`T.oscRows` plus the constant `n n' d₀ / 4`, where `n = card R`, `n' = card C` and `d₀ = n - n'`. 

### `sum_centredParam_sq`

 The squares of the centred parameters `T.centredParam l r = l r - 2γ + n'` (with
`γ = T.rowShift`, `n' = card C`) sum to four times the sum of the squares of `λ_r - T.centre`, for
`l = 2λ`. 

### `IsMatch.centred_casimirValue_eq`

 For matching parameters `l = 2λ`, `l' = 2λ'` of the pair `T` (both of large gap, with centred
parameters that are opposite or small), `|u|² - |ρ|² + n n' d₀ / 4 = |u'|² - |ρ'|²`. Here
`u = λ - T.centre` and `u' = λ' - T.swap.centre`, with the centres `T.rowShift - n'/2` and
`T.columnShift - n/2` of the row and column actions; `|u|²` is the sum of squares, `n = card R`,
`n' = card C`, `d₀ = n - n'`, and `n (n² - 1) / 12`, `n' (n'² - 1) / 12` are `|ρ|²`, `|ρ'|²`. 
