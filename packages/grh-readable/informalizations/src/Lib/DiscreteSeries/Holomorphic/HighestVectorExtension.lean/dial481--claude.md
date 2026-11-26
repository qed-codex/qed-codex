---
{
  "module": "src/Lib/DiscreteSeries/Holomorphic/HighestVectorExtension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/HighestVectorExtension.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Holomorphic/HighestVectorExtension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponentials in U(diag ε) and holomorphic extension of coefficients of highest vectors

The group is `New.USign ε = U(diag ε)` with compact subgroup `New.maxCompactU ε = U(diag ε) ∩ U(n)`.
Every element of the compact subgroup is an exponential, and every element of the group is a product
of two exponentials, so each element is joined to `1` by an analytic path in the group. A function
`F` on a product of copies of this group is holomorphic of weight `u` for the order `o`
(`New.IsHolOfWeight ε o u F ε'`) if it extends analytically to products `h * b` of tuples by
`F' (h * b) = (∏ τ, diagChar (u τ) (b τ)) * F h`. Here each `b τ` is triangular for `o`, and `h τ`,
`b τ` are block diagonal for `ε'` (no condition for `ε' = 1`). For injective `o`, products of
principal minors `New.weightMinors` of dominant weights (`weightMinors l g` is the product over
integers `t` of the principal minor of `g` on `{i | t ≤ l i}`, divided by `det g` when `t ≤ 0`) and
coefficients of highest vectors are such functions. For dominant weights the file computes their
weighted means over circles and, for a single copy of the group, their integrals against
`conj (weightMinors w)` over `New.maxCompactU ε`.

## Main definitions and results

* `New.exists_expU_eq_maxCompactU`: an element of the compact subgroup
  `New.maxCompactU ε = U(diag ε) ∩ U(n)` is the exponential of a block diagonal element of the Lie
  algebra (take the logarithm by the functional calculus).
* `New.exists_eq_expU_mul_expU`: every element of the group is a product of two exponentials, by the
  polar decomposition `New.exists_polar`.
* `New.isHolOfWeight_weightMinors`, `New.HCParam.IsKHighest.isHolOfWeight_coeffMap`: products of
  principal minors `New.weightMinors` and coefficients of highest vectors are holomorphic of a
  weight (`New.IsHolOfWeight`).
* `New.IsHolOfWeight.integral_mul_conj_weightMinors`: the integral of `F` against
  `conj (weightMinors w)` over the compact group `New.maxCompactU ε`.

Notions from other files:
* `New.unitaryLie J`, `New.expU`: the Lie algebra of U(J), made of the matrices `X` with
  `Xᴴ J + J X = 0`, and its exponential map to U(J).
* `New.blockDiagAlg ε`: the matrices that commute with `diag ε` (`New.signMatrix ε`), that is the
  block diagonal matrices for the signs `ε`.
* `New.IsBorelMatrix o b`: `b` is invertible and `b i j = 0` whenever `o j < o i`.
* `New.diagChar w b`: the product `∏ i, b i i ^ w i` of powers of the diagonal entries.
* `New.IsKDominant ε o w`: `w j ≤ w i` whenever `ε i = ε j` and `o i < o j`.

## Relation to the literature

Known result: the coefficient of the highest vector of a holomorphic discrete series representation
and its reproducing property. Here the setting is powers of U(p,q), using functions on the group
that extend holomorphically to the group times a Borel subgroup instead of the bounded domain.
Source: Harish-Chandra, Representations of semisimple Lie groups IV-VI, Amer. J. Math. 77 (1955), 78
(1956); A. Knapp (1986); A. Koranyi, A simplified approach to the holomorphic discrete series, arXiv
2312.16350.


 ## Exponentials in U(diag ε) and its maximal compact subgroup 

### `New.exists_expU_eq_maxCompactU`

 Every `k` in `K = U(diag ε) ∩ U(n)` is `exp X` for some `X` in the Lie algebra of `U(diag ε)`
that commutes with `diag ε`. 

### `New.exists_eq_expU_mul_expU`

 Every element of `U(diag ε)` is a product of two exponentials. 


## Holomorphic functions of weight u: coefficients of highest vectors and circle means

The extension of coefficients and the circle mean both use a local factorisation `y = a * b` near
`1` with `b` triangular, which the inverse function theorem gives (`New.exists_borel_chart`).


### `lowerMask`

 The part of a matrix strictly below the diagonal for the order `o`, inside the blocks of `ε`. 

### `lowerLiePart`

 The real linear map `X ↦ N - J Nᴴ J` on complex matrices, where `J = diag ε` and `N` is
`lowerMask ε' o X` plus `c` times the diagonal of `X`. 

### `lowerLiePart_mem_unitaryLie`

 The values of `lowerLiePart` lie in the Lie algebra of `U(diag ε)`. 

### `exists_borel_chart`

 A chart at `1` adapted to the triangular matrices. Let `E` send `0` to `1` with strict
derivative the identity. Let `L` be real linear, with every `E (L Z)` block diagonal for `ε`, and
let `L Z` and `Z` have the same entries below the diagonal inside the blocks (`lowerMask` keeps
these entries). Then there is `ψ` with `ψ 1 = 0` and derivative the identity at `1` such that each
block diagonal `y` near `1` is the product of the block diagonal matrices `E (L (ψ y))` and
`1 + (1 - L) (ψ y)`, the second being invertible and triangular for the order `o`. 

### `hasFDerivAt_of_rays`

 Let `D` be a continuous family of `ℂ`-linear maps from `E` to a Banach space `X`. If
`t ↦ f (t • Y)` has derivative `D (t • Y) Y` at every real `t`, for all `Y`, then `f` is complex
differentiable at `0` with derivative `D 0`. 

### `DiscreteSeries.continuous_weightMinors`

 The product of principal minors `weightMinors w` is continuous along a continuous family of
invertible matrices. 

### `kTypeNormSq_pos`

 For an integer vector `w`, let `w.kTypeNormSq` be the integral of the squared norm of
`weightMinors w k` (a product of principal minors of `k`) for the Haar measure of
`K = U(diag ε) ∩ U(n)`. It is positive. 

### `isBorelMatrix_diagonal`

 For `|s| = 1` the matrix `diag (s ^ o)` is invertible and triangular for the order `o`. 

### `exists_analytic_path`

 Let `ε'` be `1` or `ε`. An element of `U(diag ε)` that is block diagonal for `ε'` is joined to
`1` by a real analytic path of such elements. 

### `IsHolOfWeight.continuous`

 A function on a product of copies of `U(diag ε)` that is holomorphic of weight `u` (with no
block condition) is continuous. 

### `IsHolOfWeight.apply_mul_diagTorus`

 A function `F` that is holomorphic of weight `u` (with no block condition) transforms by the
character `u` under right translation by `diagTorus ε t = diag t`, for `t` with `|t i| = 1`. 

### `isHolOfWeight_weightMinors`

 For injective `o`, weights `u τ` that are dominant within the blocks of `ε'` for the order `o`,
and invertible `a`, the function `g ↦ ∏ τ, weightMinors (u τ) (a * g τ)`, a product of principal
minors, is holomorphic of weight `u`: it extends analytically to products `g * b`, with `g` and `b`
block diagonal for `ε'` and `b` triangular, picking up the factor `∏ τ, diagChar (u τ) (b τ)`. 

### `IsBorelMatrix.exists_eq_diagonal_exp`

 Let `o` be injective. An element of `U(diag ε)` that is triangular for the order `o` is
diagonal, with entries `exp (θ i * I)` of norm one. 

### `HCParam.IsKHighest.apply_triangular`

 Let `x` be a highest vector of weight `u` in the `gl n`-module `ρ` for the blocks of `ε'` and
the order `-o`, with `o` injective: `E a a` acts on `x` by `u a`, and `E a b` kills it if
`ε' a = ε' b` and `o a < o b`. Then a matrix `Y` that is block diagonal for `ε'` and upper
triangular for `o` acts on `x` by the scalar `∑ a, u a * Y a a`. 

### `HCParam.IsKHighest.coef_mul_triangular`

 Let `x` be a highest vector of weight `u` for the order `-o` and the blocks of `ε'` (see
`New.HCParam.IsKHighest.apply_triangular`), with `o` injective, and let `c` be a coefficient map for
`ρ` (`s ↦ c (h * expU (s • Y)) v` has derivative `c (h * expU (s • Y)) (ρ Y v)` for `Y` in the Lie
algebra). Right multiplication by an element `t` of `U(diag ε)` that is triangular for `o`
multiplies `c h x` by `diagChar u t = ∏ i, t i i ^ u i`. 

### `HCParam.IsKHighest.diagChar_smul_coeffMap_eq`

 Under the hypotheses of `New.HCParam.IsKHighest.coef_mul_triangular` (`x` highest of weight
`u`, `c` a coefficient map), the vector `diagChar u b • c h x` depends only on the product `h * b`
of `h` in `U(diag ε)` and an invertible triangular matrix `b`. 

### `exp_lowerLiePart_zero_mem_blockDiagAlg`

 The exponential of `lowerLiePart ε ε' o 0 Z = N - J Nᴴ J` is block diagonal for `ε'`. Here
`J = diag ε` and `N` is the part of `Z` below the diagonal for `o` inside the blocks of `ε'`. 

### `HCParam.IsKHighest.apply_lowerLiePart_zero`

 Let `x` be highest of weight `u` for the order `-o` and the blocks of `ε'`, with `o` injective.
Then `lowerLiePart ε ε' o 0 Y = N - J Nᴴ J` acts on `x` as `N = lowerMask ε' o Y`: the strictly
upper triangular part `J Nᴴ J` kills `x`. 

### `lowerMask_lowerLiePart_zero`

 The matrices `lowerLiePart ε ε' o 0 Z` and `Z` have the same entries below the diagonal for `o`
inside the blocks of `ε'`. 

### `HCParam.IsKHighest.differentiableAt_coeffMap_expU`

 Let `x` be highest for the order `-o` and the blocks of `ε'`, with `o` injective, and let `c` be
a continuous coefficient map for `ρ` (its derivative along `exp (s • Y)` is given by `ρ Y`). Write
`v Z = lowerLiePart ε ε' o 0 Z = N - J Nᴴ J`, with `J = diag ε` and `N` the part of `Z` below the
diagonal inside the blocks of `ε'`. Then `Z ↦ c (h * exp (v Z)) x` is complex differentiable at `0`,
although `v` is only real linear. 

### `HCParam.IsKHighest.isHolOfWeight_coeffMap`

 Let `o` be injective. For each `τ` let `x τ` be a `K`-highest vector of weight `u τ` in the
`gl n`-module `ρ τ` for the parameter `-o` and signs `ε'`: each `E a a` acts on it by `u τ a`, and
`E a b` kills it when `ε' a = ε' b` and `o a < o b`. Let `c τ` be a continuous coefficient map for
`ρ τ`: the maps `c τ h : M → X` are linear, and `t ↦ c τ (h * exp (t • Y)) v` has derivative
`c τ (h * exp (t • Y)) (ρ τ Y v)` for `Y` in the Lie algebra of `U(diag ε)`. Let `ℓ` be a continuous
multilinear form. Then `h ↦ ℓ fun τ ↦ c τ (h τ) (x τ)` is holomorphic of weight `u`: it extends
analytically to products `h * b` with `b` invertible and triangular for `o` and `h`, `b` block
diagonal for `ε'`, with factor `∏ τ, diagChar (u τ) (b τ)`. 

### `IsCircleFactorization`

 The translates of `x` by the circle `diag (s ^ o)` factor through an entire curve `A` from `1`
and a fixed block diagonal triangular `b`: `diag (s ^ o) * x = A s * (diag (s ^ o) * b)` for
`|s| = 1`. The diagonal of `b` gives the product of minors `weightMinors w x`. 

### `IsCircleFactorization.mem_blockDiagAlg`

 `b` is block diagonal for `ε`. 

### `IsCircleFactorization.isBorelMatrix`

 `b` is invertible and triangular for the order `o`. 

### `IsCircleFactorization.analyticAt`

 `A` is entire. 

### `IsCircleFactorization.apply_zero`

 `A` starts at the identity. 

### `IsCircleFactorization.weightMinors_eq`

 The product of minors `weightMinors w x` is `∏ i, b i i ^ w i`. 

### `IsCircleFactorization.diagonal_mul_eq`

 The factorisation on the unit circle. 

### `diagonal_mul_one_add_lowerMask`

 For `|s| = 1`, conjugation by `diag (s ^ o)` multiplies the entry `(i, j)` of `lowerMask ε o Z`
(the entries `Z i j` with `o j < o i` and `ε i = ε j`, others `0`) by `s ^ (o i - o j)`, a natural
power of `s`. 

### `isBorelMatrix_one_add_lowerMask`

 For injective `o` the matrix `1 + lowerMask ε o Z`, which has diagonal entries `1` and off the
diagonal the entries `Z i j` with `o j < o i` and `ε i = ε j` (others `0`), is invertible and
triangular for the order `-o`. 

### `eventually_exists_isCircleFactorization`

 Let `o` be injective, `w` dominant within the blocks of `ε` (`w j ≤ w i` whenever `ε i = ε j`
and `o i < o j`) and `P` a neighbourhood of `1`. Then each block diagonal `x` (commuting with
`diag ε`) near `1` has a circle factorisation (`New.IsCircleFactorization`), and its entire curve
`A` maps the closed unit disc into `P`. Such a factorisation is an entire curve `A` from `1` and a
fixed block diagonal `b`, triangular for `o`, with `diag (s ^ o) * x = A s * (diag (s ^ o) * b)` for
`|s| = 1`, where the diagonal of `b` gives `weightMinors w x`. 

### `circle_mean_of_isCircleFactorization`

 The circle mean at a point with a circle factorisation, for injective `o`. Let `F'` extend `F`
to products `h * b` with factor `∏ τ, diagChar (u τ) (b τ)`, as in `New.IsHolOfWeight`, with blocks
given by `ε'`. Let each `g τ` be block diagonal with circle factorisation
`diag (s ^ o) * g τ = A τ s * (diag (s ^ o) * b τ)` (`New.IsCircleFactorization`), and let `F'` be
analytic along `A` over the closed unit disc. Then for `q` analytic on the disc the mean over
`|s| = 1` of `F (diag (s ^ o) * g) * ((∏ τ, ∏ i, (s ^ o i) ^ u τ i)⁻¹ * q s)` is
`q 0 * (∏ τ, weightMinors (u τ) (g τ)) * F 1`. 

### `IsHolOfWeight.circle_mean_weightMinors`

 The mean over the circle `diag (s ^ o)` of a function of weight `u`. Let `o` be injective and
`ε'` be `1` or `ε`, and let `F` on `(USign ε)^Φ`, the tuples in the unitary group of `diag ε`, be
holomorphic of weight `u` for `o` and `ε'` (`IsHolOfWeight`), with each `u τ` `K`-dominant:
`u τ j ≤ u τ i` whenever `ε' i = ε' j` and `o i < o j`. Let each `g τ` commute with `diag ε'` and
let `q` be analytic on a neighbourhood of the closed unit disc. Then the mean over `|s| = 1` of
`F (diag (s ^ o) * g) * ((∏ τ, ∏ i, (s ^ o i) ^ u τ i)⁻¹ * q s)` is
`q 0 * (∏ τ, weightMinors (u τ) (g τ)) * F 1`, where `weightMinors l g` is the product over all
integers `t` of the principal minor of `g` on `{i | t ≤ l i}`, divided by `det g` when `t ≤ 0`. 

### `IsHolOfWeight.integral_mul_conj_weightMinors`

 Let `o` be injective. Let `F` on a single copy of `U(diag ε)` be continuous and holomorphic of
weight `w`, with blocks given by `ε` and `w` dominant within the blocks (`w j ≤ w i` whenever
`ε i = ε j` and `o i < o j`). Then the integral of `F k * conj (weightMinors w k)` against the Haar
probability measure `haarK ε` of `K = U(diag ε) ∩ U(n)` is `w.kTypeNormSq * F 1`, where
`w.kTypeNormSq = ∫ ‖weightMinors w k‖ ^ 2`. A case of Schur's orthogonality relations for `K`:
integration against `conj (weightMinors w) / w.kTypeNormSq` fixes the highest vectors of weight
`w`. 
