---
{
  "module": "src/New/Appendix/DiscreteSeries/Localization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Localization.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Localization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Localizing products of discrete series coefficients near the compact subgroups

This file treats a group `S` with a map `j : S →* U(ε) × U(η)` that satisfies
`New.DiscreteSeries.IsLaplaceDatum`. It proves facts about `New.HCParam.laplaceIntegrand`, the
product of the first discrete series coefficient, the conjugate of the second and `exp (-φ)`. It
shows that a coefficient with a large gap decays away from the maximal compact subgroup. It also
shows that, if `1 ≤ B` and both noncompact parts at `s` are small, the integrand takes the same
value at some `t` for which both components of `j t` are near `1`.

## Main definitions and results

* `New.DiscreteSeries.noncompactPart ε g`: the noncompact part `g - blockDiagPart ε g` of a
  matrix `g`.
* A coefficient with a large gap is small where the noncompact part of its argument is large
  (`New.DiscreteSeries.norm_dsCoeff_pow_four_le`).
* If `1 ≤ B` and both noncompact parts at `s` are small, then `laplaceIntegrand` takes the same
  value at some `t` for which both components of `j t` are near `1`
  (`New.DiscreteSeries.IsLaplaceDatum.exists_laplaceIntegrand_eq_and_norm_subOnePair_le`).

Notions from other files:
* `New.USign ε`: the unitary group `U(ε)` of the diagonal matrix `signMatrix ε` of the signs `ε`.
* `New.blockDiagPart ε g`: the compact part of `g`, which keeps the entries `g i j` with
  `ε i = ε j`.
* `New.HCParam.lowestKType l`, `New.HCParam.dsCoeff l`: the highest weight of the lowest `K`-type
  of the parameter `l`, and the matrix coefficient of that `K`-type.
* `New.DiscreteSeries.IsLaplaceDatum`: the properties of `j` and `φ` that Laplace's method uses.
* `New.HCParam.laplaceIntegrand`: the function to which Laplace's method applies.

## Relation to the literature

This file uses the discrete series coefficient that is known as Flensted-Jensen's function, the
coefficient of the lowest `K`-type of a discrete series
(defined in `Lib.DiscreteSeries.FlenstedJensen.Defs`).


 ### The relation `g ε gᴴ = ε` row by row 

### `noncompactPart`

 The noncompact part `A - blockDiagPart ε A` of a matrix `A` for the signs `ε`: it keeps the
entries `A i j` with `ε i ≠ ε j` and puts zero elsewhere. 

### `two_mul_re_sub_one_apply`

 Let `ε : n → ℤˣ` be a vector of signs and let `g` be in `U(ε) = USign ε`, the unitary group of
the diagonal matrix of `ε`. The entry `(i, i)` of the relation `g ε gᴴ = ε` reads
`2 re (x i i) = 2 ∑ j, ‖y i j‖² - ∑ j, ‖x i j‖²`, where `x = g - 1` and `y = noncompactPart ε g`
keeps the entries `g i j` with `ε i ≠ ε j` and is zero elsewhere. 

### `norm_sq_add_re_trace_le`

 Let `g` be in `U(ε) = USign ε`, the unitary group of the diagonal matrix of the signs
`ε : n → ℤˣ`. Let `v`, `w` be integer vectors with `a (v i)² ≤ w i` for all `i` and `w i ≤ C` at
each index whose sign differs from that of some other index. Then, in Frobenius norms,
`a ‖v (g - 1)‖² + 2 re tr (w (g - 1)) ≤ 2 C ‖y‖²`. Here `v` and `w` act as the diagonal matrices
`intDiagonal v` and `intDiagonal w`, and `y = noncompactPart ε g` keeps the entries `g i j` with
`ε i ≠ ε j` and is zero elsewhere. 

### `norm_sub_one_sq`

 Let `g` be in `U(ε) = USign ε`, the unitary group of the diagonal matrix of the signs
`ε : n → ℤˣ`. Then `‖g - 1‖² = 2 ‖y‖² - 2 re tr (g - 1)` in Frobenius norms, where
`y = noncompactPart ε g` keeps the entries `g i j` with `ε i ≠ ε j` and is zero elsewhere. 

### `norm_noncompactPart_inv`

 For `g` in `U(ε)`, the noncompact parts of `g⁻¹` and of `g` have the same Frobenius norm. 

 ### The block on `X` 

### `norm_sub_one_le_norm_mul_self_sub_one`

 A positive semidefinite matrix `z` is at least as close to `1` as `z²`, in Frobenius norm. 

### `offBlockIndicator`

 The indicator function of the coordinates off `X`: under `e : X ⊕ Fin M ≃ n` it is `0` on the
image of `X` and `1` on the image of `Fin M`. 

### `onBlock`

 The block of a matrix with rows and columns in `X`, seen in `n` through `e : X ⊕ Fin M ≃ n`. 

### `norm_sq_le_rows_add_columns_add_block`

 The square of the Frobenius norm of `A` is at most the sum of those of its rows off `X`, its
columns off `X` and its block `onBlock e A` on `X`, with `X` seen in `n` through `e`. Multiplication
by `intDiagonal (offBlockIndicator e)` on the left (right) keeps the rows (columns) off `X`. 

### `norm_onBlock_gram_sub_one_le`

 Let `g` be in `U(ε)`, the signs being `+1` on `X`, and let `a = onBlock e g` be the block of `g`
on `X`. Then `‖aᴴ a - 1‖` is at most the square of the norm of the rows of `g - 1` off `X`, which
left multiplication by the diagonal matrix `intDiagonal (offBlockIndicator e)` keeps. 

### `exists_unitary_sub_one_eq_inclMatrix`

 If `u` is unitary (`uᴴ * u = 1`) and `f : X ⊕ Y ≃ n` sends `X` to coordinates where `ε` is `1`,
then `u`, extended by `1` on the coordinates from `Y`, is an element `s` of `USign ε`: `s -
1 = inclMatrix ℂ (f ∘ .inl) * (u - 1) * (inclMatrix ℂ (f ∘ .inl))ᴴ`. Here `inclMatrix ℂ (f ∘ .inl)`
is the matrix of the inclusion of `X` in `n`. 

 ### The phases at the logarithms 

### `hasSum_trace_geom`

 For `‖A‖ ≤ 1 / 2` (Frobenius norm) and `0 ≤ r ≤ 1`, the geometric series of `(1 + r • A)⁻¹` may
be multiplied by `D` and `A` and traced term by term. 

### `phase_sub`

 The difference `l.phase k (Y, Y') = tr (μ Y) - tr (μ' Y')` of the two phases, for the weights
`μ`, `μ'` of the lowest `K`-types of `l` and `k`, is compatible with subtraction of pairs. 

### `IsLaplaceDatum.phase_pow_mul`

 For a pair of matrices put `l.phase k (Y, Y') = tr (μ Y) - tr (μ' Y')`, where `μ` and `μ'` are
the diagonal matrices of the weights of the lowest `K`-types of the parameters `l` and `k`. Let
`j : S →* U(ε) × U(η)` and `φ : S → ℂ` satisfy `IsLaplaceDatum`, of which two conditions are used:
`φ` is additive, and `l.phase k (g - 1, g' - 1) = φ s` for `(g, g') = j s`. Then
`l.phase k ((g - 1) ^ (i + 1), (g' - 1) ^ (i + 1))` is `φ s` for `i = 0` and `0` for `i > 0`. 

### `IsLaplaceDatum.phase_logOneAdd`

 Let `l`, `k` be doubled Harish-Chandra parameters for the signs `ε`, `η`. For a pair of matrices
put `l.phase k (Y, Y') = tr (μ Y) - tr (μ' Y')`, where `μ` and `μ'` are the diagonal matrices of the
weights of the lowest `K`-types of `l` and `k`. Let `j : S →* U(ε) × U(η)` and `φ : S → ℂ` satisfy
`IsLaplaceDatum`. In particular the function `φ` is additive, and `l.phase k (g - 1, g' - 1) = φ s`
for `(g, g') = j s`, where `(g - 1, g' - 1) = subOnePair j s`. If `g - 1` and `g' - 1` have
Frobenius norm at most `1 / 2`, then `l.phase k (log g, log g')` is again `φ s`. Here
`log g = logOneAdd (g - 1)`, and `logOneAdd Y` is the logarithm of `1 + Y`. 

 ### Left translation by `U(X)` 

### `principalMinor_eq_ite_det`

 If `x - 1` vanishes in the rows `i` with `w i ≠ 0`, then the principal minor of `x` on
`{i | c ≤ w i}` is `det x` for `c ≤ 0` and `1` for `c > 0`. 

### `weightMinors_mul_eq_of_zero_weight_block`

 Let `x` be invertible, with `x i j = 0` for `w i ≠ w j` and with `x - 1` vanishing in the rows
`i` with `w i ≠ 0`. Then left multiplication by `x` preserves `weightMinors w`, the coefficient of
a highest vector of weight `w`. 

### `inclMatrix_mul_mul_conjTranspose_apply_eq_zero`

 A matrix `u` on `X`, placed by `inclMatrix` in the rows and columns in the image of `σ`,
vanishes in the other rows and in the other columns. 

### `apply_eq_zero_of_sub_one_eq_inclMatrix`

 Let `A - 1` be a matrix `u` on `X` placed, by `inclMatrix`, in the rows and columns in the image
of `σ`. If a function `f` is constant on the image of `σ`, then `A i j = 0` for `f i ≠ f j`. 

### `mem_blockDiagAlg_of_sub_one_eq_inclMatrix`

 Let `A - 1` be a matrix `u` on `X` placed, by `inclMatrix`, in the rows and columns in the image
of `σ`, where the sign is `+1`. Then `A` is block diagonal for the signs `ε`. 

### `sub_one_apply_eq_zero_of_weight_ne_zero`

 Let `A - 1` be a matrix `u` on `X` placed, by `inclMatrix`, in the rows and columns in the image
of `σ`, where the weight `w` is `0`. Then `A - 1` vanishes in the rows `i` with `w i ≠ 0`. 

### `intDiagonal_mul_sub_one_eq_zero`

 Let `A - 1` be a matrix `u` on `X` placed, by `inclMatrix`, in the rows and columns in the image
of `σ`, where the weight `w` is `0`. Then the diagonal matrix of `w` kills `A - 1`. 

### `dsCoeff_mul_eq_of_sub_one_eq_inclMatrix`

 Let `g₀ ∈ U(ε)` be such that `g₀ - 1` is a matrix `x` on `X` placed, by `inclMatrix`, in the
rows and columns in the image of `σ : X → n`, where the sign is `+1` and the weight `l.lowestKType`
of the lowest `K`-type of the parameter `l` is `0`. Then left translation by `g₀` preserves the
discrete series coefficient `l.dsCoeff`. 

### `norm_noncompactPart_mul_of_mem_blockDiagAlg`

 Left translation by a block diagonal element `g₀` of `U(ε)` preserves the Frobenius norm of the
noncompact part. 

 ### Decay away from the maximal compact subgroup 

### `one_add_sum_le_prod_one_add`

 For nonnegative reals `μ i`, one has `1 + ∑ μ i ≤ ∏ (1 + μ i)`. 

### `one_add_norm_sq_le_norm_det_one_add`

 For a complex square matrix `A` with its Frobenius norm, `1 + ‖A‖² ≤ |det (1 + Aᴴ A)|`. 

### `conjTranspose_blockDiagPart_mul_blockDiagPart`

 The part of `gᴴ ε g = ε` that commutes with `ε` reads `aᴴ a = 1 + yᴴ y`, for the compact part
`a = blockDiagPart ε g` and the noncompact part `y = noncompactPart ε g`. 

### `norm_dsCoeff_pow_four_le`

 Let the doubled Harish-Chandra parameter `l : HCParam ε` satisfy `l.HasLargeGap h`, i.e. have
gap `c = 500 (card n)³ + h`: its entries are distinct, have the parity of `card n - 1`, and differ
by at least `2 c` where the signs `ε` differ. Then for `g` in `USign ε`, the unitary group of
`diag ε`, `‖l.dsCoeff g‖ ^ 4` is at most `(1 + ‖y‖²)⁻¹ ^ h`, where the noncompact part
`y = noncompactPart ε g` keeps the entries `g i j` with `ε i ≠ ε j` and is zero elsewhere. 

### `IsLaplaceDatum.norm_intDiagonal_mul_subOnePair_sq_le`

 Let `l`, `k` be doubled Harish-Chandra parameters for the signs `ε`, `η`, and let
`j : S →* U(ε) × U(η)` (`U(ε) = USign ε`) satisfy `IsLaplaceDatum` for the splitting
`e : X ⊕ Fin M ≃ n` and the map `τ : X → m`. Then the weights `μ`, `μ'` of the lowest `K`-types of
`l` and `k` are `0` on the images of `X` under `e` and `τ`. Elsewhere `μ` is in `[-3 B, -B]`. `μ'`
is nonnegative, and at most `3 B` if `η` takes both signs. For `(g, g') = j s` the number
`φ s = tr (μ (g - 1)) - tr (μ' (g' - 1))` is imaginary. Assume `1 ≤ B`. The rows of
`g - 1 = (subOnePair j s).1` off `X` have squared norm at most `6 (‖y‖² + ‖y'‖²)`. Here
`y = noncompactPart ε g` and `y' = noncompactPart η g'` keep the entries at indices of opposite
signs. 

### `IsLaplaceDatum.norm_subOnePair_mul_intDiagonal_sq_le`

 In the setting of `IsLaplaceDatum.norm_intDiagonal_mul_subOnePair_sq_le`, let `(g, g') = j s`.
The columns of `g - 1 = (subOnePair j s).1` off `X` have squared norm at most `6 (‖y‖² + ‖y'‖²)`,
for the noncompact parts `y = noncompactPart ε g` and `y' = noncompactPart η g'`. 

### `IsLaplaceDatum.exists_laplaceIntegrand_eq_and_onBlock_eq`

 Let `l`, `k` be doubled Harish-Chandra parameters for the signs `ε`, `η`, and let
`j : S →* U(ε) × U(η)` satisfy `IsLaplaceDatum`. Its image then contains `U(X)`, placed by
`e : X ⊕ Fin M ≃ n` in the first factor and by `τ : X → m` in the second, on indices where the sign
is `+1` and the weight of the lowest `K`-type is `0`; the bounds on the weights in terms of `B` are
not used. Let `u ∈ U(X)`. For each `s` there is `t` such that the block `onBlock e` on `X` of the
first component of `j t` is `u` times that of `j s`, while `laplaceIntegrand` and the norms of both
noncompact parts agree at `s` and `t`. 

### `IsLaplaceDatum.norm_snd_sq`

 Let `j` satisfy `IsLaplaceDatum`, of which only `tr (g - 1) = tr (g' - 1)` is used. For
`(g, g') = j s` with noncompact parts `y = noncompactPart ε g` and `y' = noncompactPart η g'`, one
has `‖g' - 1‖² = ‖g - 1‖² - 2 ‖y‖² + 2 ‖y'‖²`. 

### `IsLaplaceDatum.exists_laplaceIntegrand_eq_and_norm_subOnePair_le`

 **Localization.** Let `l`, `k` be doubled Harish-Chandra parameters for the signs `ε`, `η`, with
weights `μ`, `μ'` of the lowest `K`-types, and let `j : S →* U(ε) × U(η)` satisfy `IsLaplaceDatum`:
its image contains `U(X)` diagonally on indices of weight `0`; for `(g, g') = j s` the traces of
`g - 1` and `g' - 1` agree and `φ s = tr (μ (g - 1)) - tr (μ' (g' - 1))` is imaginary and additive
in `s`; `μ` lies in `[-3 B, -B]` off `X` and `μ'` is nonnegative and, if `η` takes both signs, at
most `3 B`. Let `1 ≤ B`, so that `μ` is negative off `X`, and `0 < r ≤ 1 / 6`. If the noncompact
parts `y`, `y'` of the components of `j s` have `‖y‖² + ‖y'‖² ≤ r²`, then `laplaceIntegrand` has the
same value at `s` and at some `t` such that both components of `subOnePair j t = j t - 1` have
Frobenius norm at most `4 r`. 
