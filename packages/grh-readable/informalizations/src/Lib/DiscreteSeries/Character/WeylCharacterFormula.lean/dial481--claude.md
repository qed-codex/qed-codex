---
{
  "module": "src/Lib/DiscreteSeries/Character/WeylCharacterFormula.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/WeylCharacterFormula.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/WeylCharacterFormula.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Laurent polynomials on the torus and Weyl's character and dimension formulas

Let `ε : n → ℤˣ` be a family of signs and `K = New.maxCompactU ε` the group of unitary matrices in
the unitary group of `New.signMatrix ε`. Its Weyl group consists of the permutations `w` with
`ε ∘ w = ε`. Laurent polynomials are the elements of `ℂ[n → ℤ]`; they are evaluated on the diagonal
torus by `New.Orbital.torusEval`.

## Main definitions and results

* `New.HCParam.rootProd l r`: the product `∏ (x_a - x_b)` over the pairs with `r (ε a) (ε b)` and
  `l b < l a`, where `r` is `Eq` for the compact roots and `Ne` for the noncompact roots.
  `New.Orbital.rootProd_mem_leadingMonomials` finds its top monomial, whose exponent
  `New.HCParam.lowerCount l r a` counts such `b`.
* `New.Orbital.alternant`, `New.Orbital.IsWeylAntisymm`: the alternants `∑ sgn(w) x ^ (μ ∘ w)` over
  the Weyl group, and functions of the exponent that are antisymmetric.
* `New.HCParam.kTypeChar`: the average over conjugation of the matrix coefficient
  `New.weightMinors ν` (a product of principal minors), divided by `New.HCParam.kTypeNormSq ν`.
* `New.Orbital.weyl_character_kTypeChar`, `New.Orbital.weyl_denominator`: Weyl's character and
  denominator formulas for `K`. The first joins
  `New.Orbital.exists_kTypeChar_diagTorusK_eq_torusEval` (the character is a Laurent polynomial) and
  `New.Orbital.torusEval_rootProd_mul_kTypeChar_eq_alternant` (the formula).
* `New.weyl_dimension_formula`: Weyl's dimension formula for `U(n)`.
* `New.Variety.trace_weylRep`: Weyl's character formula at a tuple `g` of invertible matrices with
  distinct eigenvalues, reduced to the diagonal case `New.weyl_character` by conjugation.

Notions from other files:
* `New.HCParam ε`: integer vectors `n → ℤ`, used as weights and as doubled parameters `l = 2λ`.
* `New.HCParam.lowestKType`: the integer vector `Λ = λ + ρ - 2ρ_c` for a parameter `l = 2λ`, the
  highest weight of the lowest `K`-type. With all signs `1` one has `ρ_c = ρ`.
* `New.weylRep κ e`: the representation of `∏_τ GL(n_τ)` sending `g` to `∏_τ det(g_τ) ^ e_τ` times
  the Schur matrix `New.schur κ g`.

## Relation to the literature

Known result: Weyl character formula for U(n) and products of unitary groups. Here the formula for
`K` is deduced from the one for Schur modules at diagonal matrices (`New.weyl_character`): by
Schur's lemma, normalised means over conjugation of products of principal minors are traces of
twisted Schur modules. The dimension formula is obtained by a limit at 1, and the formula for
`∏_τ GL_a(ℂ)` at elements with distinct eigenvalues by diagonalisation. Source: H. Weyl, The
Classical Groups (1939), ch. VII; Fulton and Harris, Representation Theory (1991), Lectures 24-25.

See also `Lib.DiscreteSeries.Character.FormalDegree`.



## Laurent polynomials on the torus, Weyl denominators and alternants

`New.IsKDominant ε (-l) ν` says `ν j ≤ ν i` if `ε i = ε j` and `l j < l i`. `δ` is
`New.HCParam.lowerCount l Eq`, the top exponent of the product over the compact roots.


### `torusEval`

 For a tuple `x` of unit complex numbers, the algebra homomorphism from Laurent polynomials to
`ℂ` sending the monomial of exponent `γ` to `∏ x_a ^ γ_a`. 

### `torusEval_eq_sum`

 The value of a Laurent polynomial `P` at `x` is the sum over the exponents `γ` of the
coefficient at `γ` times the monomial `∏ x_a ^ γ_a`. 

### `oppositePairs`

 The finite set of pairs of indices `(a, b)` with `ε a = 1` and `ε b = -1`. 

### `alternant`

 The Laurent polynomial `∑ sgn(w) x ^ (l ∘ w)`, summed over the permutations `w` that preserve
the signs `ε` (the Weyl group of `K`). 

### `IsWeylAntisymm`

 The function `t` on `ℤⁿ` is antisymmetric under the Weyl group of `K`:
`t (γ ∘ w) = sgn(w) t γ` for the permutations `w` preserving the signs `ε`. 

### `leadingMonomials`

 The monoid of pairs `(a, P)`, where `P` is a Laurent polynomial with coefficient `1` at `x ^ a`,
all exponents `γ` of `P` are nonnegative, and every `γ` other than `a` has a lower level:
`l ⬝ᵥ γ < l ⬝ᵥ a`. 

### `single_sub_single_mem_leadingMonomials`

 If `l b < l a`, then `x_a` is the monomial of highest level `l ⬝ᵥ γ` of the binomial
`x_a - x_b`. 

### `_root_.New.HCParam.rootProd`

 The Laurent polynomial `∏ (x_a - x_b)` over the pairs `(a, b)` with `r (ε a) (ε b)` and
`l b < l a`. It is a partial Weyl denominator (Vandermonde product) for the order given by `l`. 

### `_root_.New.HCParam.lowerCount`

 The number of `b` with `r (ε a) (ε b)` and `l b < l a`. As a function of `a`, it is the exponent
of the product of the first terms `x_a` of the factors of `New.HCParam.rootProd l r`. 

 ### Top monomials, alternants and class functions 

### `rootProd_mem_leadingMonomials`

 Let the level `o` keep the strict order of `l`. Then `l.rootProd r`, the product of
`x_a - x_b` over `r (ε a) (ε b)` and `l b < l a`, is a polynomial whose only monomial of highest
level `o ⬝ᵥ γ` has exponent `l.lowerCount r` (the number of such `b`) and coefficient `1`. 

### `torusEval_rootProd`

 The value at `x` of `l.rootProd r` is the product of `x a - x b` over the pairs with
`r (ε a) (ε b)` and `l b < l a`. 

### `torusEval_rootProd_ne_zero`

 The product `l.rootProd r` of binomials `x_a - x_b` with `l b < l a` does not vanish at a point
of the torus with distinct coordinates. 

### `alternant_apply`

 The coefficient of `x ^ γ` in the alternant of `ν` is the sum of the signs of the permutations
`w` that preserve `ε` and satisfy `ν ∘ w = γ`. 

### `torusEval_alternant`

 At a point `x` of the torus, the alternant of `ν` is the determinant of the matrix with
`(a, b)` entry `x a ^ ν b` if `ε a = ε b` and `0` otherwise. 

### `eq_of_torusEval_eq`

 A Laurent polynomial is determined by its values on the torus. 

### `denseRange_torusEval`

 Weierstrass approximation on a torus: Laurent polynomials are uniformly dense in the
continuous complex functions on (S¹)ⁿ. 

### `torusEval_comp_perm`

 Permuting the coordinates of the point is the same as permuting the exponents of `P`. 

### `torusEval_comp_eq_mul_iff`

 Permuting the variables by `w` multiplies the values of `P` on the torus by `c` exactly when
permuting the exponents by `w` multiplies the coefficients of `P` by `c`. 

### `isWeylAntisymm_alternant`

 Alternants are antisymmetric under the Weyl group of `K`: the coefficient of `x ^ γ` in
`alternant ε ν` is antisymmetric as a function of `γ`. 

### `apply_comp_perm_of_conj_invariant`

 Let `K = maxCompactU ε`, and let `diagTorusK x` be the diagonal matrix with entries `x`. If `f`
on the torus and `d` on `K` satisfy `d (y * diagTorusK x * y⁻¹) = f x` for all `y` and `x`, then `f`
is invariant under every permutation `w` of the coordinates that preserves the signs `ε`. 

### `torusEval_rootProd_noncompact`

 For injective `l`, the product `l.rootProd Ne` of `x a - x b` over `ε a ≠ ε b` and `l b < l a`
(the positive noncompact roots) is, up to a sign that does not depend on `x`, the product of
`x a - x b` over the pairs `oppositePairs ε` with `ε a = 1`, `ε b = -1`. 

### `torusEval_rootProd_noncompact_comp`

 For injective `l`, the values of the product `l.rootProd Ne` over the positive noncompact roots
are invariant under the permutations `w` of the coordinates that preserve the signs `ε`. 

 ### Antisymmetric functions and dominant weights 

### `alternant_coeff_of_isKDominant`

 Let `l` be injective and let `δ = l.lowerCount Eq` count, at `a`, the `b` with `ε a = ε b` and
`l b < l a`. For weights `ν` and `ν'` that are monotone in `l` on each class of `ε` (dominant), the
coefficient of the alternant of `ν + δ` at `ν' + δ` is `1` if `ν' = ν` and `0` otherwise. 

### `exists_perm_comp_eq_and_apply_le_apply`

 Let `l` be injective. Every exponent `γ` can be sorted by a permutation `w` that preserves the
signs `ε`: the exponent `γ ∘ w` is monotone in `l` on each class of `ε`. 

### `isKDominant_sub_lowerCount`

 Let `l` be injective and `γ` strictly monotone in `l` on each class of `ε`. Then
`γ - l.lowerCount Eq` is still monotone in `l` on each class (dominant); here `l.lowerCount Eq a`
counts the `b` with `ε a = ε b` and `l b < l a`. 

### `exists_sign_isKDominant`

 Let `l` be injective and let `l.lowerCount Eq a` count the `b` with `ε a = ε b` and `l b < l a`.
For every exponent `γ` there are an integer `s` and a weight `ν`, monotone in `l` on each class of
`ε` (dominant), such that `t γ = s * t (ν + l.lowerCount Eq)` for every function `t` that is
antisymmetric under the permutations preserving `ε`. 

 ## Characters of K-types and Weyl's character formula for K 

### `_root_.New.HCParam.kTypeChar`

 The continuous function `g ↦ (∫ y, New.weightMinors ν (y⁻¹ g y)) / ∫ k, |New.weightMinors ν k|²`
on `K`, for Haar measure of mass one. It is defined for every `ν`. If `l` is injective and `ν` is
dominant for the order of `l`, it is the character of highest weight `ν` on the torus (see
`New.Orbital.weyl_character_kTypeChar`). 

### `exists_maxCompactU_of_blocks`

 Given unitary matrices `g τ` on the blocks `{i | ε i = τ}`, there is an element `y` of `K` whose
matrix is the block diagonal matrix of the `g τ`, reindexed by `n`. Its diagonal blocks are the
`g τ`. 

### `exists_eq_const_add_partition`

 Let `q τ` enumerate the block `{i | ε i = τ}` by increasing `l`, and let `ν` be dominant:
`ν j ≤ ν i` if `ε i = ε j` and `l j < l i`. Then on each block, read by decreasing `l`, the weight
`ν` is a constant `e τ` plus the partition `New.diagramWeight` of `κ`: its value at `(τ, k)` is the
sum of `κ τ h` for `k < h < N τ`, where `N τ = rankAt _ τ` is the size of the block. 

### `prod_weightMinors_toSquareBlock`

 On an element `k` of `K`, which is block diagonal for `ε`, the function `New.weightMinors ν`
(the product of determinant powers and principal minors with highest weight `ν`) is the product of
the same functions on the diagonal blocks of `k`. 

### `kTypeChar_diagTorusK_eq_trace_schur`

 Suppose that, with respect to numberings `p τ` of the blocks `{i | ε i = τ}`, the weight `ν` is
a constant `e τ` plus the partition `New.diagramWeight` of `κ` (whose `k`th part is the sum of the
`κ τ h` with `k < h < #block`). Here `New.HCParam.kTypeChar ν` is the function `g ↦ (∫ y,
weightMinors ν (y⁻¹ g y)) / ∫ k, |weightMinors ν k|²` on `K = U(diag ε) ∩ U(n)`, for Haar measure of
mass one; for dominant `ν` it is the character of highest weight `ν`. The claim is that at the
diagonal matrix `diagTorusK x` with entries `x`, `kTypeChar ν` is the trace of `New.schur κ` (the
matrix of the Schur module of `κ`), twisted on each block by the power `e τ` of the determinant. 

### `filter_lt_eq_map_Iio`

 If `q τ` enumerates the block of sign `τ` by increasing `l`, then the indices of this block at
which `l` is below `l (q τ j)` are the `q τ i` with `i < j`. 

### `torusEval_rootProd_eq_prod_vandermonde`

 If `q τ` enumerates the block of sign `τ` by increasing `l`, then on the torus the product over
the compact roots is the product over the blocks of Vandermonde determinants. 

### `exists_kTypeChar_diagTorusK_eq_trace_schur`

 Let `l` be injective and `ν` dominant for the order of `l`. Enumerate each block `{i | ε i = τ}`
by increasing `l`, through `q τ`. Then on the block, read by decreasing `l`, the weight `ν` is a
constant `e τ` plus the partition `New.diagramWeight` of some `κ` (value at `(τ, k)`: the sum of
`κ τ h` for `k < h < rankAt _ τ`, the block size), and on the torus `New.HCParam.kTypeChar ν` is the
trace of `New.schur κ` twisted by the powers `e τ` of the determinants of the blocks. 

### `exists_kTypeChar_diagTorusK_eq_torusEval`

 If `l` is injective and `ν` is dominant for the order of `l`, then on the diagonal torus
`New.HCParam.kTypeChar ν` is given by a Laurent polynomial. 

### `torusEval_rootProd_mul_kTypeChar_eq_alternant`

 Weyl's character formula for `K` at a point `x` of the torus. Let `l` be injective and `ν`
dominant for the order of `l`. The product of `x a - x b` over `ε a = ε b`, `l b < l a`, times
`New.HCParam.kTypeChar ν` at the diagonal matrix with entries `x`, is
`∑ sgn(w) x ^ ((ν + δ) ∘ w)`, where `δ a` is the number of such `b` and `w` runs over the
permutations preserving `ε`. 

### `weyl_character_kTypeChar`

 Weyl's character formula for `K`. Let `l` be injective and `ν` dominant for `K` in the order of
`l`: `ν b ≤ ν a` if `ε a = ε b` and `l b < l a` (this is `New.IsKDominant ε (-l) ν`). Let `χ x` be
`New.HCParam.kTypeChar ν` at the diagonal matrix with entries `x`. (a) `χ` is given by a Laurent
polynomial in `x`; (b) `∏ (x a - x b) * χ x = ∑ sgn(w) x ^ ((ν + δ) ∘ w)`, the product over
`ε a = ε b`, `l b < l a`, with `δ a` the number of such `b`, the sum over the permutations
preserving `ε`. 

### `weyl_denominator`

 Weyl's denominator formula for `K`: for injective `l`, the product of `x a - x b` over
`ε a = ε b`, `l b < l a` is `∑ sgn(w) x ^ (δ ∘ w)` over the permutations `w` that preserve
`ε`, where `δ a` is the number of such `b`. 

### `exists_conj_diagTorusK`

 Every element of the compact group `K` is conjugate in `K` to an element of the diagonal
torus. 


## Weyl's dimension formula for U(n)

`New.weyl_dimension_formula` evaluates `Λ.kTypeNormSq = ∫ |New.weightMinors Λ k|² dk` over `U(n)`
(all signs `1`). In the classical theory this is the reciprocal of the dimension of the
representation of highest weight `Λ = λ - ρ`, where `ρ` is half the sum of the positive roots.


### `New.HCParam.prod_prod_lowerCount_sub`

 For an injective `l` with all signs `1`, the numbers `δ i = l.lowerCount Eq i` of the `j` with
`l j < l i` run through `0, …, n - 1`, so their Vandermonde product, taken in the order of `l`, is
`∏_{i < n} i !`. 

### `New.weyl_dimension_formula`

 Weyl's dimension formula for `U(n)`. Let `l = 2λ` be a parameter for all signs `1` (distinct
entries congruent to `n - 1` mod 2; the gap `h` plays no role as all signs are equal) and
`Λ = l.lowestKType = λ - ρ`. The number `Λ.kTypeNormSq` is the integral of `|New.weightMinors Λ k|²`
over `U(n)` for Haar measure of mass one, and `New.weylDimensionPoly l` is the product of `λᵢ - λⱼ`
over `λⱼ < λᵢ`, divided by `∏_{i < n} i !`. The statement says that the inverse of the former is
the latter. By Schur orthogonality the inverse of the former is the dimension of the representation
of highest weight `Λ` (compare `New.IsHCParam.prod_formalDegree`). 


## Weyl's character formula at regular elements via Vandermonde determinants

* `New.Variety.det_zpow_add`: a common integer shift of the exponents comes out of a generalised
  Vandermonde determinant in nonzero numbers.
* `New.Variety.trace_weylRep`: the character formula at elements with distinct eigenvalues.


### `det_zpow_add`

 If the `r i` are nonzero, a common integer shift `d` of the exponents comes out of
`det (r i ^ (d + k j))` as the factor `(∏ r i) ^ d`. 

### `trace_weylRep`

 Weyl's character formula: if each g_v in GL_a(ℂ) has distinct eigenvalues x_{v,i}, the trace of
`New.weylRep κ e` (the Schur module of κ twisted by the powers e_v of the determinants) at g times
∏_v det(x_{v,i}^j) equals ∏_v det(x_{v,i}^(e_v + λ_{v,a−1−j} + j)), with 0 ≤ i, j < a, λ_{v,k} the
sum of the κ v h for k < h < a (`rankAt fun _ ↦ Fin a` gives every block the size a), and λ the
weight `New.diagramWeight` of κ.

Known result: Weyl's character formula for GL_a. 
