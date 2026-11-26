---
{
  "module": "src/New/Appendix/DiscreteSeries/GaussianShape.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/GaussianShape.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/GaussianShape.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Gaussian shape of the coefficient

Near `1` the coefficient `l.dsCoeff g` of a discrete series with a large gap is nearly the phase
`exp (tr μ log g)` times a number in `[0, 1]`, where `μ` is the weight `l.lowestKType`
(`exists_norm_dsCoeff_div_cexp_sub_le`). The coefficient is a mean over `K` of a quotient of
products of minors, and the estimates for one minor are multiplied over the sets `{i | t ≤ w i}` of
a weight `w`. In the comments, `λ^ρ` is `paramAddRho l`, `Q_w` is `gapWeightedNormSq w`, and `ĝ` is
`reducedExp ε l Z`. The Gaussian is `exp (-q)` with `q = Q_{-λ^ρ} (log g) / 4`; note `Q_{-w} = Q_w`.
Except in the first section, the norm of a matrix is the Frobenius norm.

* `USign ε` is the unitary group of the form `diag ε`; `K = maxCompactU ε` is its subgroup of
  unitary matrices, with the Haar measure `haarK ε` of mass one.
* `l : HCParam ε` is a doubled Harish-Chandra parameter `2λ`; `paramAddRho l` is `λ + ρ` and
  `l.lowestKType` is `λ + ρ - 2ρ_c`.
* `weightMinors w g` is the product over `t : ℤ` of the principal minors of `g` on the sets
  `{i | t ≤ w i}`, those with `t ≤ 0` divided by `det g`; `w.kTypeNormSq` is the mean of its
  squared modulus over `K`.
* `l.flenstedJensen g z` is the mean over `k ∈ K` of
  `weightMinors μ (g k) * conj (weightMinors μ k) / weightMinors (-paramAddRho l) (kᴴ z k)`,
  divided by `μ.kTypeNormSq` (Flensted-Jensen's integral); the matrix coefficient `l.dsCoeff` is
  defined through it.

## Relation to the literature

See `New.Appendix.DiscreteSeries.Periods` for related work.


### `one_le_pow_mul_kTypeNormSq`

 Let the parameter `l = 2λ` have gap `500 n ^ 3 + A` (the entries of `λ` are distinct, and those
with different signs `ε` are this far apart) and `|l i| ≤ L`. Then the mean `μ.kTypeNormSq` over
`K = maxCompactU ε` of the squared modulus of the highest weight coefficient `weightMinors μ`, for
`μ = l.lowestKType`, is at least `1 / (4 (2000 (n + L + 1) ^ 6) ^ (2 n ^ 2))`. 

### `exp_neg_le_kTypeNormSq`

 Let the parameter `l = 2λ` have gap `500 n ^ 3 + A` and `|l i| ≤ L`, and let `T` be at least
`1`, `n ^ 2` and `n ^ 2 log (n + L + 1)`. Then the mean `μ.kTypeNormSq` over `K = maxCompactU ε` of
the squared modulus of the highest weight coefficient `weightMinors μ`, for `μ = l.lowestKType`, is
at least `exp (-5000 T)`. The inverse of `μ.kTypeNormSq` plays the part of the dimension of the
lowest `K`-type, so this takes the place of the bound from Weyl's dimension formula. 

### `gapWeightedNormSq`

 The quadratic form `Q_w (X) = ∑_{i, j} |w i - w j| |X i j| ^ 2`. 

### `sum_norm_lie_coordProj_sq`

 Let the entries of `w` lie in `[a, b]`, and let `P_t = coordProj (t ≤ w ·)` be the projection
to the coordinates `{i | t ≤ w i}`. The squared Frobenius norms of the commutators `[P_t, X]`,
`a < t ≤ b`, add up to `Q_w (X) = ∑_{i, j} |w i - w j| |X i j| ^ 2`, because exactly
`|w i - w j|` of these sets separate `i` from `j`. 

### `sum_trace_coordProj_mul`

 If the entries of `w` lie in `[a, b]`, the projections `coordProj (t ≤ w ·)` to the coordinates
`{i | t ≤ w i}`, `a < t ≤ b`, add up to `diag w - a`; this is the resulting identity for their
traces against `X`. 

### `maxCompactU_conjTranspose_mul_self`

 An element of `K = maxCompactU ε` is a unitary matrix. 

### `norm_weightMinors_sq_le_exp`

 On `K = maxCompactU ε`, the product of principal minors `weightMinors w` decays like a Gaussian:
its squared modulus at `k` is at most `exp (-Q_w (k) / 2)`. 

### `exists_weightMinors_conj_reducedExp_eq_cexp`

 Let `l` have distinct entries, let `w` be a weight whose order is opposite to that of `l`, let
`Z` lie in the Lie algebra of `U(diag ε)` with Frobenius norm at most `δ ≤ 1 / 20`, and let
`k ∈ K = maxCompactU ε`. Put `ĝ = reducedExp ε l Z = exp (-u) exp Z exp (-v)`, where `u` and `v` are
the strictly lower and the strictly upper triangular part, in the order of decreasing `l`, of the
block diagonal part of `Z` (the entries `Z i j` with `ε i = ε j`). Then the highest weight
coefficient `weightMinors w (kᴴ ĝ k)` is `exp (tr (diag w * Z) + Q_w (Z) / 4 + r)` with
`|r| ≤ 10 ^ 5 δ (Q_w (Z) + Q_w (k))`. 

### `norm_trace_paramAddRho_sub_trace_lowestKType_le`

 The entries of `paramAddRho l - l.lowestKType = 2 ρ_c` (written `twoRho l (ε · = ε ·)`) are at
most `n` in modulus, so the traces of `Z` against the diagonal matrices of the two weights differ
by at most `n ^ 2 ‖Z‖` (Frobenius norm). 

### `gapWeightedNormSq_neg_paramAddRho_le`

 For `k ∈ K = maxCompactU ε` we have `Q_{-λ^ρ} (k) ≤ Q_μ (k) + 2 n ^ 2`. This holds because
`λ^ρ - μ = 2ρ_c` has entries at most `n` in modulus and `‖k‖ ^ 2 = n` (Frobenius norm). Here `2ρ_c`
is the sum of the compact roots (`ε i = ε j`) positive for `l`. 

### `exists_weightMinors_neg_paramAddRho_eq_cexp`

 Let `l = 2λ` be a parameter of gap `h` (the entries of `λ` are distinct, and those with
different signs `ε` are at least `h` apart), let `Z` lie in the Lie algebra of `U(diag ε)` with
Frobenius norm at most `δ ≤ 1 / 20`, and let `k ∈ K = maxCompactU ε`. Put
`λ^ρ = paramAddRho l = λ + ρ` and `μ = l.lowestKType = λ + ρ - 2ρ_c`, where `ρ` and `ρ_c` are the
half sums of the roots and of the compact roots that are positive for `λ`. Put also
`Q_w (X) = ∑_{i, j} |w i - w j| |X i j| ^ 2`, `q = Q_{-λ^ρ} (Z) / 4` and
`ĝ = reducedExp ε l Z = exp (-u) exp Z exp (-v)`, where `u` and `v` are the strictly lower and the
strictly upper triangular part, in the order of decreasing `l`, of the block diagonal part of `Z`
(the entries `Z i j` with `ε i = ε j`). Then the denominator `weightMinors (-λ^ρ) (kᴴ ĝ k)` of
Flensted-Jensen's integrand at `ĝ`, a product of principal minors, is `exp (q - tr μ Z - r)` with
`|r| ≤ 5 · 10 ^ 5 δ (q + Q_μ (k) + n ^ 2)`. 

### `flenstedJensen_div_exp_sub`

 Let `y` be invertible. Flensted-Jensen's integral `l.flenstedJensen g y` at the identity matrix
`g = 1` is the mean over `k ∈ K = maxCompactU ε` of `|weightMinors μ k| ^ 2 / weightMinors
(-paramAddRho l) (kᴴ y k)`, divided by the mean `μ.kTypeNormSq` of `|weightMinors μ k| ^ 2`. Suppose
that the denominator of the integrand is `exp (q - θ - r k)` for all `k ∈ K`, with `q` real and `θ`,
`r k` complex. Then `l.flenstedJensen 1 y / exp θ` differs from `exp (-q)` by the mean over `K` of
`|weightMinors μ k| ^ 2 exp (-q) (exp (r k) - 1)`, divided by `μ.kTypeNormSq`. 

### `mul_norm_exp_sub_one_le`

 Let `δ T ≤ 10 ^ (-12)`, `T ≥ 1`, `0 ≤ N ≤ T`, `0 ≤ m ≤ exp (-Q / 2)` and
`|r| ≤ 10 ^ 6 δ (q + Q + N)`, with `δ`, `q`, `Q` nonnegative. Then `m exp (-q) |exp r - 1|` is at
most `exp (-q) m / 10 + exp (-5100 T)`: either `r` is small, or `m exp (-q)` is. 

### `exists_norm_dsCoeff_div_cexp_sub_le`

 **Gaussian shape.** Let the parameter `l = 2λ` have gap `500 n ^ 3 + A` and `|l i| ≤ L`, let `T`
be at least `1`, `n ^ 2` and `n ^ 2 log (n + L + 1)`, and let `δ T ≤ 10 ^ (-12)`. For `g` in the
unitary group `USign ε` of the form `diag ε` with `‖g - 1‖ ≤ δ` (Frobenius norm), the discrete
series coefficient `l.dsCoeff g`, divided by the phase `exp (tr μ log g)`, is within
`ϱ / 10 + exp (-100 T)` of a number `ϱ ∈ [0, 1]`; the proof takes a Gaussian in `log g` for `ϱ`. 
