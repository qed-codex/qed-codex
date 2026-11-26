---
{
  "module": "src/Lib/DiscreteSeries/Theta/FockJointHarmonics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/FockJointHarmonics.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/FockJointHarmonics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weights of matched pairs and uniqueness of joint harmonics in Fock space

This file studies the weights of matched pairs of the parameters `l` and `l'` of a dual pair
`T : New.FockDualPair`. It proves that the joint harmonic is unique up to a scalar, and that one of
its two weights suffices for this. Here `New.FockDualPair.IsMatchedPair` says that row `r` is
matched with column `c`.

The proof of uniqueness has three steps.
* The weights relative to the vacuum: `New.IsMatch.relWeight_eq_neg`,
  `New.IsMatch.sign_mul_relWeight_nonneg`.
* Both polarisations in a raising operator kill a highest harmonic polynomial, and a row has
  variables of one sign: `New.DiscreteSeries.polarisation_eq_zero_of_isCompactPrimitive`,
  `New.DiscreteSeries.polarisation_self_eq_smul_of_isCompactPrimitive`.
* Such a polynomial does not vanish at the 0-1 matrix of the matching:
  `New.IsMatch.eval_matchingPoint_ne_zero`.

## Main definitions and results

* `New.IsMatch.unique`, `New.IsJointHarmonic.exists_eq_smul_of_row_weight`,
  `New.IsJointHarmonic.exists_eq_smul_of_column_weight`: the joint harmonic is unique up to a
  scalar, and one of its two weights suffices for this.
* `New.IsMatch.eval_matchingPoint_ne_zero`: a pre-joint harmonic does not vanish at the point
  `New.FockDualPair.matchingPoint`, the 0-1 matrix of the matching.

Notions from other files:
* `New.HCParam.HasGap`: `l.HasGap h` says that the entries of `l = 2λ` are distinct and congruent to
  `n − 1` mod 2, where `n` is their number, and `|λ_i − λ_j| ≥ h` whenever `ε_i ≠ ε_j`.
* `New.HCParam.IsKHighest`: `x` is a `K`-highest vector of weight `ν`: each `E a a` acts on it by
  `ν a`, and it is killed by the compact raising operators, the `E a b` with `ε a = ε b` and
  `l b < l a`. The second condition alone is `New.GlModule.IsCompactPrimitive`.
* `New.HCParam.lowestKType`: for a parameter `l = 2λ`, the integer vector `λ + ρ − 2ρ_c`, which is
  the highest weight of the lowest `K`-type.
* `New.FockDualPair.IsPreJointHarmonic`: `Φ ≠ 0` is killed by the compact raising operators of the
  columns and by the Laplacians of both sides, and is `K`-highest of weight `l.lowestKType` for
  rows.
* `New.FockDualPair.relWeight`: the entry in row `r` of the lowest `K`-type for `l`, minus the
  weight of the vacuum on a row of sign `ε r`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Theta.LocalCorrespondence` for sources.


 ### The weights of rows and columns relative to the vacuum 

### `HCParam.HasGap.two_mul_relWeight`

 Let `l` be a parameter with a gap (only distinctness and parity of its entries matter). Twice
`T.relWeight l r`, the entry of the lowest `K`-type minus the weight of the vacuum in row `r`, is
`l r + ∑ j, ε r * ε j * sign (l j - l r) - 2γ + card C - ∑ c, η (r, c)`, where `γ` is the constant
of the row action and `η (r, c)` the sign of the variable `(r, c)`. 

### `IsMatch.hasLargeGap`

 If the parameters `l` of the rows and `l'` of the columns are matched, then `l` has the gap
`500 * card R ^ 3 + A` for every `A` up to the number `card ι` of variables. 

### `IsMatch.col_eq_of_isMatchedPair`

 If `l` and `l'` match, a row is matched with at most one column. 

### `IsMatch.row_eq_of_isMatchedPair`

 If `l` and `l'` match, a column is matched with at most one row. 

### `IsMatch.sum_cols_le_sum_rows`

 Let `l`, `l'` match. Then `∑ c, G c ≤ ∑ r, F r`, provided that `G c ≤ F r` when row `r` is
matched with column `c`, that `0 ≤ F r` when the centred parameter `l r - 2γ + card C` is less than
`card R - card C` in absolute value, and that `G c ≤ 0` when `l' c - 2γ' + card R` is less than
`card C - card R` in absolute value. 

### `IsMatch.relWeight_eq_neg`

 Let `l`, `l'` match. If row `r` is matched with column `c`, then Λ_r − v_r = −(Λ'_c − v'_c),
where Λ, Λ' are the lowest `K`-types of `l`, `l'` and v, v' the weights of the vacuum `1` for the
row and the column action. 

### `IsMatch.sign_mul_relWeight_nonneg`

 Let `l`, `l'` match and let `s` be a sign. If `s` times the centred parameter
`l r - 2 * γ + card C` exceeds `card C - card R`, then `T.relWeight l r`, the weight of the lowest
`K`-type in row `r` relative to the vacuum, has the sign `s` or is zero. 

 ### Highest harmonic polynomials

A compact raising operator `E a b` is the difference of two polarisations. 

### `DiscreteSeries.polarisation_one_eq_of_lt`

 Let `P` be killed by the compact raising operators of the rows for `l`, and let `ε a = ε b` and
`l b < l a`. Then the two polarisations whose difference is `E a b P` are equal: `∑ X_ac ∂_bc P`
over the columns `c` where `(b, c)` has sign `1`, and `∑ X_bc ∂_ac P` over those where it has sign
`-1`. 

### `DiscreteSeries.inner_polarisation_eq_zero`

 Let the entries of `l` be distinct, let `P` be killed by the compact raising operators of the
rows for `l` and by the Laplacians of the columns. For rows `a`, `b` of equal sign, the
polarisations `∑ X_bc ∂_ac P` over the columns `c` where `(a, c)` has sign `-s` and `∑ X_ac ∂_bc P`
over those where it has sign `s` are orthogonal for the Fischer inner product. For `s = 1` and
`a ≠ b` these are the two parts of `E a b P`. 

### `DiscreteSeries.polarisation_eq_zero_of_isCompactPrimitive`

 Let the entries of `l` be distinct, let `P` be killed by the compact raising operators of the
rows for `l` and by the Laplacians of the columns. If the rows `a`, `b` have equal sign and
`s * l b < s * l a`, then the polarisation `∑ X_ac ∂_bc P` over the columns `c` where `(b, c)` has
sign `s` is zero. 

### `DiscreteSeries.polarisation_self_eq_smul_of_isCompactPrimitive`

 Let the entries of `l` be distinct, let `P` be killed by the compact raising operators of the
rows for `l` and by the Laplacians of the columns, and let `E a a` act on it by the entry `Λ_a` of
the lowest `K`-type. Put `k = s * (Λ_a - v)`, where `v` is the weight of the vacuum in row `a`. If
`k ≥ 0`, then `P` has degree `k` in the variables of sign `s` of row `a`, and it does not depend on
the variables of sign `-s` of that row. 

### `DiscreteSeries.polarisation_eq_of_isCompactPrimitive`

 Let the entries of `l` be distinct, and let `P` be killed by the compact raising operators of
the rows and by the Laplacians of the columns. Fix a row `a` and a sign `s`. The polarisation
`∑ c, X_ac ∂P/∂X_bc` over the variables `X_bc` of sign `s` vanishes if `ε a = ε b` and
`s * l b < s * l a`. If `E a a` acts on `P` by the entry of the lowest `K`-type, and the weight
`T.relWeight l a` relative to the vacuum has sign `s` or is zero, then `P` is homogeneous of degree
`s * T.relWeight l a` in the variables of sign `s` of row `a` and free of those of sign `-s`. 

### `FockDualPair.IsTermwiseHarmonic.isLaplaceHarmonic`

 If each mixed derivative `∂_ac ∂_bc Φ` with `ε a ≠ ε b` vanishes, then the Laplacians of the
rows, which are sums of such derivatives up to sign, kill `Φ`. 

### `FockDualPair.IsJointHighest.isPreJointHarmonic`

 Let `Φ ≠ 0` be termwise harmonic along rows and columns and `K`-highest for both actions, with
the lowest `K`-type of `l` as weight for the row action and any weight `ν` for the column action.
Then `Φ` is a pre-joint harmonic: nonzero, killed by the compact raising operators of the columns
and by the Laplacians of both sides, and highest of weight `l.lowestKType` for the rows. 

### `FockDualPair.IsPreJointHarmonic.sub_smul`

 A combination `P - c • Q` of pre-joint harmonics (nonzero polynomials killed by the Laplacians
and the compact raising operators of both sides, of weight `l.lowestKType` for the rows) is again
one, unless it is zero. 

 ### The value at the matrix of the matching 

### `FockDualPair.matchingPoint`

 The 0-1 matrix of the matching, as a point of `ι → ℂ`: the coordinate of the variable `(r, c)`
is `1` if row `r` is matched with column `c`, and `0` if not. 

### `FockDualPair.matchingPoint_ne_zero_iff`

 The coordinate `(r, c)` of the 0-1 matrix of the matching is nonzero exactly when row `r` is
matched with column `c`. 

### `DiscreteSeries.IsEigenDirection`

 The variable `i` is an eigendirection of `F` at the point `x` if `F` is an eigenvector of a
linear vector field `∑ k ∈ S, X (a k) * ∂ (b k)` of which exactly one term, a multiple of `∂ i`,
is nonzero at `x`. 

### `DiscreteSeries.IsEigenDirection.intro`

 The vector field has the terms `X (a k) * ∂ (b k)` for `k ∈ S` and the eigenvalue `μ` on
  `F`. Its term of index `j` differentiates in `i`, and `X (a k)` is nonzero at `x` only for
  `k = j`. 

### `DiscreteSeries.bind₁_X_add_C_pderiv`

 The translation `G ↦ G (X + x)` commutes with partial derivatives. 

### `DiscreteSeries.coeff_zero_bind₁_X_add_C`

 The constant coefficient of `G (X + x)` is the value of `G` at `x`. 

### `DiscreteSeries.exists_not_isEigenDirection`

 A nonzero polynomial `F` that vanishes at `x` depends on a variable `i` that is not an
eigendirection at `x`: `F` is an eigenvector of no linear vector field `∑ k, X (a k) * ∂ (b k)`
whose only nonzero term at `x` is a multiple of `∂ i`. 

### `IsMatch.lt_or_exists_isMatchedPair`

 Let `l`, `l'` match and let `s` be the sign of the variable `(r, c)`. Call an integer large if
it exceeds `card C - card R`, and let `ξ = l r - 2γ + card C`, with `γ = T.rowShift` the constant of
the row action, be the centred parameter of row `r`. Either `-s * ξ` is large, or one of three pairs
is matched: `(r, c)` itself, with `s * ξ` large; a pair `(r, d)` with `ε' d = ε' c` and
`s * l' d < s * l' c`; or a pair `(a, c)` with `ε a = ε r` and `s * l r < s * l a`. 

### `IsMatch.isEigenDirection_of_polarisation`

 Let `l`, `l'` match and let row `a` be matched with column `c`. If `F` is an eigenvector of the
polarisation `∑ X_ad ∂_rd` from row `r` to row `a`, summed over the columns `d` where `(r, d)` has
the sign of `(r, c)`, then `(r, c)` is an eigendirection of `F` at the 0-1 matrix of the
matching. 

### `IsMatch.isEigenDirection_of_swap_polarisation`

 Let `l`, `l'` match and let row `r` be matched with column `d`. If `F` is an eigenvector of the
polarisation from column `c` to column `d` over the variables with the sign of `(r, c)`, then
`(r, c)` is an eigendirection of `F` at the 0-1 matrix of the matching. 

### `IsMatch.eval_matchingPoint_ne_zero`

 Let `l`, `l'` match. A pre-joint harmonic `F` (nonzero, killed by the Laplacians and the compact
raising operators of both sides, of weight `l.lowestKType` for the rows) does not vanish at the
point `T.matchingPoint l l'`, the 0-1 matrix of the matching. 

### `IsMatch.unique`

 Uniqueness of the joint harmonic up to a scalar. If the parameters `l` of the rows and `l'` of
the columns match, then any two pre-joint harmonics of `T` (nonzero polynomials killed by the
Laplacians and the compact raising operators of both sides, of weight `l.lowestKType` for the rows)
are proportional.

This proves the case of the multiplicity one part of Howe's (GL, GL)-duality that is used. 

### `IsJointHarmonic.exists_eq_smul_of_row_weight`

 Let `Φ` be a joint harmonic for `T`, `l`, `l'`: a nonzero polynomial, with `l` and `l'`
matching, that is `K`-highest for the row and column actions with the weights of the two lowest
`K`-types, and termwise harmonic for `T` and `T.swap`. Termwise harmonic means no monomial contains
two variables of one column from rows of opposite signs, or two variables of one row from columns of
opposite signs. Then every polynomial `P` that is termwise harmonic in both ways, is `K`-highest of
weight `l.lowestKType` for the row action `T.oscRows`, and is killed by the compact raising
operators for `l'` of the column action `T.swap.oscRows` is a scalar multiple `c • Φ`. 

### `IsJointHarmonic.exists_eq_smul_of_column_weight`

 Let `T` be a dual pair in Fock space, whose variables in `ι` are indexed by rows `R` and columns
`C`, and let `Φ` be a joint harmonic for matching `l`, `l'`. That is, `Φ ≠ 0` is `K`-highest, of the
weights of the lowest `K`-types, for the row action `T.oscRows` and the column action
`T.swap.oscRows`, and it is termwise harmonic for `T` and `T.swap`: no monomial has two variables of
one column from rows of opposite signs, or two variables of one row from columns of opposite signs.
Then every polynomial `P` satisfying both termwise harmonic conditions, killed by the compact
raising operators of the row action for `l`, and `K`-highest of weight `l'.lowestKType` for the
column action, is a scalar multiple of `Φ`. 
