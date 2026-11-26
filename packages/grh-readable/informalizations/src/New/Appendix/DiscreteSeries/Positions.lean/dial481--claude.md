---
{
  "module": "src/New/Appendix/DiscreteSeries/Positions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Positions.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/Positions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Positions of a smaller unitary group, and the two traces

A position of `U(η)` in `U(ε)` consists of independent vectors `v₁, …, v_{j₀}` and an isometry `i₀`
into their orthogonal complement. It is stationary for two weights `μ`, `μ'` if `μ` moves `v_j` to
`v_{j + 1}` for `j < j₀` and compresses to `μ'` on the image of `i₀`, and `i₀` is the identity on
the common coordinates `X`. For a matrix `Y` that lowers the flag of the `v_j` together with its
adjoint, and induces `Y'` on the image of `i₀`, we compute `tr Y - tr Y'` and `tr μ Y - tr μ' Y'`.

Notions from other files:
* `signMatrix ε` is the diagonal matrix of the signs `ε i = ±1`, and `USign ε` its unitary group.
* `HCParam ε` consists of the integer vectors on `n`, used as doubled Harish-Chandra parameters
  `l = 2 λ`; `l.lowestKType` is the weight of the lowest `K`-type and `intDiagonal w` the diagonal
  matrix of a weight `w`.
* `l.phase k (Y, Y')` is `tr μ Y - tr μ' Y'` for the weights `μ`, `μ'` of the lowest `K`-types of
  `l` and `k`.


### `formAdjoint`

 The adjoint `A†` of `A : (ℂ^m, η) → (ℂ^n, ε)` for the two hermitian forms. 

### `initCols`

 The columns `v₁, …, v_{j₀ - 1}` of `v = (v₁, …, v_{j₀})`, where `j₀ = d + 1`. 

### `IsPosition`

 A position of `U(η)` in `U(ε)`, where the ranks differ by `2 j₀ - 1` and `j₀ = d + 1`. It
consists of independent vectors `v₁, …, v_{j₀}`, the columns of `v`, whose pairings for the form
`ε` vanish except that the pairing of `v_{j₀}` with itself is `±1`, and of an isometry `i₀` into
their orthogonal complement. 

### `IsPosition.card_eq`

 The ranks differ by `2 j₀ - 1`. 

### `IsPosition.independent`

 The vectors `v₁, …, v_{j₀}` are independent. 

### `IsPosition.gram_eq_zero`

 The product of `v_i` and `v_j` vanishes unless `i = j = j₀`. 

### `IsPosition.gram_last_eq_sign`

 The pairing of `v_{j₀}` with itself, which can be negative, is `±1`. 

### `IsPosition.isometry`

 The map `i₀` is an isometry. 

### `IsPosition.orthogonal`

 The image of `i₀` is orthogonal to `v₁, …, v_{j₀}`. 

### `LowersFlag`

 Let `A_{≤ j}` be the span of the columns `v₁, …, v_j` of `v`. Then `Y` maps `A_{≤ j}` into
`A_{≤ j - 1}` for `j ≤ j₀ = d + 1`, and `σ` is the sum of the coefficients of `v_j` in
`Y v_{j + 1}` over `j < j₀`, which is determined by `Y` if the `v_j` are independent. 

### `InducesOn`

 `Y` acts by `Y'` on the image of `i₀`, modulo the span `A_{≤ j₀ - 1}` of `v₁, …, v_{j₀ - 1}`. 

### `IsStationary`

 A stationary position. Let `μ`, `μ'` be the weights of the lowest `K`-types of `l`, `k`, as
diagonal matrices. Then `μ` moves `v_j` to `v_{j + 1}` for `j < j₀` and compresses to `μ'`, and `i₀`
is the identity on `ℂ^X`, where `e` and `e'` place `X` among the coordinates `n` and `m`. 

### `IsStationary.shift`

 `μ v_j = v_{j + 1}` for `j < j₀`. 

### `IsStationary.adjoint_weight_mul_eq`

 `i₀† μ i₀ = μ'`. 

### `IsStationary.apply_inl`

 `i₀ = 1` on `ℂ^X`. 

### `formAdjoint_mul`

 The adjoint for the forms reverses products: `(A A')† = A'† A†`. 

### `formAdjoint_val`

 On the group `U(ε)` the adjoint for the form is the inverse. 

### `formAdjoint_sub_one`

 For `g` in `U(ε)` the adjoint of `g - 1` is `g⁻¹ - 1`. 

### `isometry_of_formAdjoint_mul_self`

 A map `A` with `A† A = 1` is an isometry. 

### `formAdjoint_inclMatrix`

 Let `τ` take values among the coordinates of sign `+1`. Then the adjoint for the forms `ε` and
`1` of the matrix with columns the standard vectors at `τ x` is its usual adjoint. 

### `orthogonal_initCols`

 In a position (`hP : IsPosition ε η d v i₀`), the span of all the columns of `v` is orthogonal,
for the form `ε`, to the span of its first `d` columns `initCols v`:
`vᴴ * signMatrix ε * initCols v = 0`. 

### `initCols_isotropic`

 In a position (`hP : IsPosition ε η d v i₀`), the span of the first `d` columns `initCols v` of
`v` is orthogonal, for the form `ε`, to the span of all the columns of `v`:
`(initCols v)ᴴ * signMatrix ε * v = 0`. 

### `exists_mul_eq_zero_and_mul_eq_one`

 Let `(v, i₀)` be a position (`IsPosition`): the columns `v₁, …, v_{j₀}` of `v`, where
`j₀ = d + 1`, are independent, and `i₀` is an isometry into their orthogonal complement for the
forms with signs `η` and `ε`. Then some matrix `Z` gives coordinates along all the `v_j` and
vanishes on the image of `i₀`: it satisfies `Z i₀ = 0` and `Z v = 1`. 

### `exists_mul_eq_zero_and_mul_initCols_eq_one`

 Let `(v, i₀)` be a position (`IsPosition`): the columns `v₁, …, v_{j₀}` of `v`, where
`j₀ = d + 1`, are independent, and `i₀` is an isometry into their orthogonal complement for the
forms with signs `η` and `ε`. Then some matrix `Z` gives coordinates along the first `j₀ - 1` of
these vectors, the columns of `initCols v`, and vanishes on the image of `i₀`. 

### `hasLeftInv`

 The columns of `i₀` and the vectors `v₁, …, v_{j₀}` of a position are independent. 

### `exists_eq_of_orthogonal`

 Let `(v, i₀)` be a position of `U(η)` in `U(ε)` (`IsPosition`): the columns `v₁, …, v_{j₀}` of
`v`, where `j₀ = d + 1`, are independent, their pairings for the form with signs `ε` vanish except
that of `v_{j₀}` with itself, which is `±1`, and `i₀` is an isometry into their orthogonal
complement. Let `A` be the span of `v₁, …, v_{j₀ - 1}`, the columns of `initCols v`. If the columns
of `M` are orthogonal to `A`, then they are linear combinations, with coefficient matrix `T`, of
the columns of `i₀` and of `v`. 

### `trace_mul_eq_of_mul_initCols_eq_zero`

 Let `(v, i₀)` be a position (`IsPosition`): the columns `v₁, …, v_{j₀}` of `v`, where
`j₀ = d + 1`, are independent with vanishing pairings for the form with signs `ε`, except that of
`v_{j₀}` with itself, and `i₀` is an isometry into their orthogonal complement. Let `Y` map the
span of the `v_j` into `A`, the span of the first `j₀ - 1` of them (the columns of `initCols v`),
with matrix `N`, and let it act by `Y'` on the image of `i₀` modulo `A` (`InducesOn`). If `M`
vanishes on `A` and has its image in the orthogonal complement of `A`, then
`tr M Y = tr (i₀† M i₀) Y'`, with `i₀†` the adjoint for the two forms. 

### `trace_mul_eq_trace_add_sum_of_inducesOn`

 Let `(v, i₀)` be a position (`IsPosition`): the columns `v₁, …, v_{j₀}` of `v`, where
`j₀ = d + 1`, are independent with vanishing pairings for the form with signs `ε`, except that of
`v_{j₀}` with itself, and `i₀` is an isometry into their orthogonal complement. Let `i₀†` be its
adjoint for the two forms, and let `μ` be self-adjoint and send each `v_j`, for `j < j₀`, to
`v_{t j}`, where `t` is any map of indices. Let `Y` and its adjoint `Y†` map the span of all the
`v_j` into the span `A` of the first `j₀ - 1` of them, with the matrices `N` and `N'`, and let
`Y` act by `Y'` on the image of `i₀` modulo `A` (`InducesOn`). Then
`tr μ Y = tr (i₀† μ i₀) Y' + ∑ N j (t j) + conj (∑ N' j (t j))`. The terms come from a split of
`μ` into a self-adjoint rest that vanishes on `A`, its part `μ₁` on `A`, and the adjoint of
`μ₁`. 

### `lowersFlag_unique`

 Let `(v, i₀)` be a position (`IsPosition`); only the independence of the columns
`v₁, …, v_{j₀}` of `v`, where `j₀ = d + 1`, matters here. Let `Y` lower their flag
(`LowersFlag`): it sends `v₁` to `0` and each `v_{j + 1}` into the span of `v₁, …, v_j`. Then the
sum `σ` of the coefficients of `v_j` in `Y v_{j + 1}` is determined by `Y`. 

### `LowersFlag.mul`

 Let `g₁ - 1` and `g₂ - 1` lower the flag of the columns `v₁, …, v_{d + 1}` of `v`
(`LowersFlag`): they send `v₁` to `0` and each `v_{j + 1}` into the span of `v₁, …, v_j`, and the
coefficients of `v_j` in the images of the `v_{j + 1}` add up to `σ₁` and to `σ₂`. Then
`g₁ g₂ - 1` lowers the flag with sum `σ₁ + σ₂`, as `(g₁ - 1) (g₂ - 1)` lowers it by two steps. 

### `IsStationary.pow_mulVec_col_zero`

 In a stationary position `(v, i₀)` for the parameters `l` and `k` let `μ` be the weight of the
lowest `K`-type of `l`, as a diagonal matrix. Then `μ ^ a v₁ = v_{a + 1}` for `a < j₀ = d + 1`. 

### `IsStationary.gram_pow_mulVec`

 Let `μ`, `μ'` be the weights of the lowest `K`-types of the parameters `l` of `U(ε)` and `k` of
`U(η)`, as diagonal matrices. Let `(v, i₀)` be a stationary position (`IsStationary`): a position in
which `μ v_j = v_{j + 1}` for `j < j₀ = d + 1`, and `i₀† μ i₀ = μ'`. If `a + b ≤ 2 d`, the pairing
of `μ ^ a v₁` and `μ ^ b v₁` for the hermitian form with signs `ε` is the pairing of `v_{j₀}` with
itself (which is `±1`) if `a + b = 2 d`, and `0` otherwise. 

### `IsPosition.trace_eq`

 Let `(v, i₀)` be a position of `U(η)` in `U(ε)` (`IsPosition`): the columns `v₁, …, v_{j₀}` of
`v`, where `j₀ = d + 1`, are independent with vanishing pairings for the form with signs `ε`,
except that of `v_{j₀}` with itself, and `i₀` is an isometry into their orthogonal complement. Let
`Y` and its adjoint `Y†` for the form lower the flag of the `v_j` (`LowersFlag`: each `v_j` goes
into the span of the earlier ones), and let `Y` act by `Y'` on the image of `i₀` modulo the span of
`v₁, …, v_{j₀ - 1}` (`InducesOn`). Then `tr Y = tr Y'`. 

### `IsStationary.phase_eq`

 Let `μ`, `μ'` be the weights of the lowest `K`-types of the parameters `l` of `U(ε)` and `k` of
`U(η)`, as diagonal matrices. Let `(v, i₀)` be a stationary position (`IsStationary`): a position in
which `μ v_j = v_{j + 1}` for `j < j₀ = d + 1`, and `i₀† μ i₀ = μ'`. Let `Y` and its adjoint `Y†`
lower the flag of the `v_j` (`LowersFlag`), with sums `σ` and `σ'` of the coefficients next to the
diagonal, and let `Y` act by `Y'` on the image of `i₀` modulo the span of `v₁, …, v_{j₀ - 1}`
(`InducesOn`). Then the phase `l.phase k (Y, Y') = tr μ Y - tr μ' Y'` equals `σ + conj σ'`. 

### `IsStationary.trace_eq_and_phase_eq`

 **Two traces.** Let `μ`, `μ'` be the weights of the lowest `K`-types of the parameters `l` of
`U(ε)` and `k` of `U(η)`, as diagonal matrices. Let `(v, i₀)` be a stationary position
(`IsStationary`): the columns `v₁, …, v_{j₀}` of `v`, where `j₀ = d + 1`, and an isometry `i₀`
into their orthogonal complement, with `μ v_j = v_{j + 1}` for `j < j₀` and `i₀† μ i₀ = μ'`. Let
`Y` and its adjoint `Y†` lower the flag of the `v_j` (`LowersFlag`), with sums `σ` and `σ'` of the
coefficients next to the diagonal, and let `Y` induce `Y'` on the image of `i₀` modulo the span of
`v₁, …, v_{j₀ - 1}` (`InducesOn`). Then `Y` and `Y'` have the same trace, and the phase
`tr μ Y - tr μ' Y'` is `σ + conj σ'`. 
