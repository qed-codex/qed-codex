---
{
  "module": "src/Lib/DiscreteSeries/Character/MultiplicityOrbitalIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/MultiplicityOrbitalIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/MultiplicityOrbitalIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# K-type multiplicities of the discrete series and orbital integrals as Laurent polynomials

Let `G = New.USign ε` be the unitary group of `diag ε`, and let `K = New.maxCompactU ε` be its
subgroup of unitary matrices. Let `ψ = New.HCParam.dsCoeff l` be the discrete series coefficient
with parameter `l = 2λ`. On the torus `New.diagTorus ε`, consider the normalised orbital integral
Θ(x) = `New.HCParam.formalDegree l` ∫_G ψ(g⁻¹ x g) dg. Θ times suitable products of differences
`x_a - x_b` is a Laurent polynomial, and the integrality of the multiplicities is the key input for
this.

## Main definitions and results

* `New.Orbital.exists_kType_multiplicity`: for a dominant weight ν and a large gap,
  `formalDegree * ∫_G ∫_K conj (kTypeChar ν k) ψ(g⁻¹ k g)` is a natural number, `1` for ν equal to
  the lowest `K`-type `New.HCParam.lowestKType l` and `0` for ν off
  `lowestKType l + New.HCParam.rootCone l`.
* `New.Orbital.integrable_mul_dsCoeff_conj`: for the gap 500 n³ + 10 n⁵, the orbital integrals times
  a power of the product over the noncompact roots converge absolutely, uniformly on `K`.
* `New.Orbital.IsConeSeriesMultiple`: `P` is `D` times a formal series with coefficient `1` at
  `x^a` whose exponents lie in alternants of weights in `a` plus the root cone.
* `New.Orbital.exists_laurent_orbital_integral`: the orbital integral times the denominators is a
  Laurent polynomial that is such a multiple.

Notions from other files:
* `New.weightMinors`: the coefficient m_ν of a highest vector of weight ν, a product of principal
  minors and a power of the determinant.
* `New.HCParam.HasLargeGap`: l = 2λ is a parameter with |λ_i - λ_j| ≥ 500 n³ + A whenever
  ε_i ≠ ε_j.
* `New.IsKDominant ε (-l) ν`, below "`K`-dominant in the order of `-l`": `ν j ≤ ν i` whenever
  `ε i = ε j` and `l j < l i`, so ν is dominant for the compact roots that are positive for l.
* `New.HCParam.lowestKType`: Λ = λ + ρ - 2ρ_c, the highest weight of the lowest K-type.
* `New.HCParam.formalDegree`: for signs ε and l = 2λ, the reciprocal of the integral of |c_λ|² over
  U(diag ε) for the compact dual measure.

## Relation to the literature

See `Lib.DiscreteSeries.Character.FormalDegree`.



## Multiplicities of K-types computed via characters

`K` carries the Haar probability measure `New.haarK ε`. `New.HCParam.kTypeChar ν` is the mean over
conjugation by `K` of `New.weightMinors ν`, divided by `New.HCParam.kTypeNormSq ν`.


### `integral_mul_conj_kTypeChar`

 For continuous `f`, the integral over `K` of `f` against `conj (kTypeChar ν)` is the mean over
`y ∈ K` of the integrals of `k ↦ f (y k y⁻¹)` against `conj (weightMinors ν)`, divided by
`kTypeNormSq ν`. 

### `integral_conj_kTypeChar`

 Orthogonality to the trivial character: `∫_K conj (kTypeChar ν)` is `1` for `ν = 0` and `0`
otherwise. 

### `mean_coefficient_lowering`

 Let `l` have a large gap and let `ν` be `K`-dominant in the order of `-l`. For
`u = l.dsGenerator` and `ι = hg.toL2` the embedding of the discrete series module in `L²`, let
`φ w = ∫_K conj (weightMinors ν k) * ⟪ι u, rightRegularL2 x (rightRegularL2 k w)⟫`. For indices
`a`, `c` with `ε a = ε c` and `l c ≤ l a`, applying the matrix unit `E c a` to a vector `y` of the
module multiplies `φ (ι y)` by `ν c` if `c = a`, and by `0` otherwise. 

### `exists_isKHighest_inner_eq_mean_coefficient`

 Let `l = 2λ` have a large gap and let `ν` be `K`-dominant in the order of `-l`. Let `φ` be the
mean `w ↦ ∫_K conj (weightMinors ν k) * ⟪ι u, rightRegularL2 x (rightRegularL2 k w)⟫`, where
`weightMinors ν` is the product of principal minors of weight `ν`, `u = l.dsGenerator` is `c_λ` as
generator of the discrete series module `U(𝔤)c_λ`, and `ι = hg.toL2` (`f ↦ √deg_λ · f`) is its
embedding in `L²`. Let `s` bound the excess of the `K`-Casimir eigenvalue of `ν` over that of the
lowest `K`-type. Then some vector of weight `ν` in step `s` of the filtration (increasing
finite-dimensional subspaces, each stable under `E c a` for `ε a = ε c`), killed by the compact
raising operators, represents `y ↦ φ (ι y)` on every step. 

### `mean_coefficient_eq_sum_norm_sq`

 Let `n` be nonempty, let `l = 2λ` have a large gap (`hg : l.HasLargeGap A`), and let `ν` be
`K`-dominant in the order of `-l`. Let `s` bound the excess of the `K`-Casimir eigenvalue of `ν`
over that of the lowest `K`-type. Let `b` be an orthonormal basis of the space `V` of `K`-highest
vectors of weight `ν` in step `s` of the filtration (increasing finite-dimensional subspaces, each
stable under `E c a` for `ε a = ε c`) of the discrete series module `U(𝔤)c_λ` generated by
`dsGenerator = c_λ`; its elements are functions on the group, and `b i x` is the value at `x`. Then
the mean `∫_K conj (weightMinors ν k) * dsCoeff (x * k * x⁻¹)`, divided by
`ν.kTypeNormSq = ∫_K |weightMinors ν k|²`, is `∑ i, |b i x|²`. Here `dsCoeff` is `c_λ`,
`weightMinors ν` is the product of principal minors of weight `ν`, and `K` carries Haar measure of
mass one. 

### `exists_kType_multiplicity`

 Let `n` be nonempty, let `l = 2λ` have a large gap (`New.HCParam.HasLargeGap` with constant `A`)
and let `ν` be `K`-dominant in the order of `-l`. Put `R g = ∫_K ψ(g⁻¹ k g) conj (kTypeChar ν k) dk`
with `ψ = New.HCParam.dsCoeff l` the discrete series coefficient and `kTypeChar ν` the character of
the `K`-type of highest weight `ν`. Then `R` is integrable over the group, and
`formalDegree l * ∫ R` is a natural number `m`, the multiplicity of that `K`-type: `m = 1` for the
lowest `K`-type `ν = lowestKType l`, and `m = 0` unless `ν - lowestKType l` lies in the cone
`rootCone l` of positive roots. Here `m` is the dimension of the space of `K`-highest vectors of
weight `ν` in a large step of the filtration of the discrete series; no formula for `m` is given. 


## Orbital integrals times root products as Laurent polynomials

The idea: let D be a power of the product of `x_a - x_b` over `ε a ≠ ε b`, `l a < l b`. Then D Θ
converges and extends to a continuous class function on K. Its coefficients against the characters
of K are integers (`New.Orbital.exists_kType_multiplicity`) and square-summable, so only finitely
many are not zero.

Conventions: `ℂ[n → ℤ]` is the ring of Laurent polynomials, `P.coeff` the coefficient function,
`New.Orbital.torusEval x` evaluation at a point of the torus. `New.HCParam.rootProd l r` is the
product of `x_a - x_b` over the pairs with `r (ε a) (ε b)`, `l b < l a`. `New.Orbital.alternant ε μ`
is the alternant ∑ sgn(w) x^(μ ∘ w) over the permutations w that preserve `ε`; for injective `l`,
δ = `l.lowerCount Eq` is the exponent whose alternant is the Weyl denominator `l.rootProd Eq`.


### `New.Orbital.IsConeSeriesMultiple`

 `P` is `D` times a formal series `t` with `t a = 1`, each of whose exponents occurs in the
alternant `New.Orbital.alternant ε μ` for some `μ` such that `μ - a` lies in the cone of positive
roots `New.HCParam.rootCone l`. 

### `New.Orbital.sq_norm_mul_norm_prod_sub_le`

 Let `n` be nonempty, `u` in `U(diag ε)` and `t` a point of the torus, and put `g = u⁻¹ t u`.
For the operator norms `(‖u‖ / 2)² |∏ (t_a - t_b)| ≤ (2 ‖g‖)^m`, the product being over the
`m` pairs in `oppositePairs ε`, those with `ε a = 1 ≠ ε b`. 

### `New.Orbital.integrable_mul_dsCoeff_conj`

 Let `n` be nonempty, let `l = 2λ` have a large gap for `A = 10 (card n)⁵`, and let
`K = U(diag ε) ∩ U(n)`. Let `d` be a continuous class function on `K` whose value at `diag(x)` is
`D(x)^N`, with `N = 4 (card n)² + 1` and `D(x) = ((-l).rootProd Ne)(x) = ∏ (x_a - x_b)` over the
pairs with `ε a ≠ ε b` and `l a < l b` (the noncompact roots positive for `-l`). Let
`ψ g k = l.dsCoeff (g⁻¹ k g)`, where `l.dsCoeff` is the function `c_λ`. Then `g ↦ d * ψ g` on
`U(diag ε)`, with values in the continuous functions on `K` with the supremum norm, is integrable.
In particular the orbital integral of `l.dsCoeff` converges absolutely at each point of the torus
with distinct entries, where `d` is not zero. 

### `New.Orbital.finite_support_inner_of_int`

 If all coefficients of a vector against an orthonormal family are integers, only finitely many
are not zero: they tend to zero by Bessel's inequality. 

### `New.Orbital.kTypeChar_mul_mul_inv`

 The character `kTypeChar ν`, being a mean over conjugates, is a class function on K. 

### `New.Orbital.exists_alternant_eq_rootProd_mul`

 Weyl's formula for any exponent γ, for injective `l`. Let ν be dominant for K and let
δ = `l.lowerCount Eq`. If every function `t` antisymmetric under the Weyl group of K has
`t γ = s * t (ν + δ)`, then `s` times the character of ν is a Laurent polynomial `P` on the torus,
and the Weyl denominator `l.rootProd Eq` times `P` is the alternant of γ. 

### `New.Orbital.mem_closure_of_conj_eq`

 Let `h` be a continuous class function on K, and suppose that for each Laurent polynomial the
set `S` contains a class function equal on the torus to the mean of the polynomial over the Weyl
group W of K (the permutations that preserve `ε`). Then `h` is a uniform limit of functions
from `S`. 

### `New.Orbital.IsWeylFamily`

 Weyl's formula for a family of class functions: `X γ` is a class function on K that equals the
Laurent polynomial `Y γ` on the torus, and the Weyl denominator `l.rootProd Eq` times `Y γ` is
the alternant of γ. 

### `New.Orbital.IsWeylFamily.apply_conj`

 `X γ` is a class function with restriction `Y γ` to the torus. 

### `New.Orbital.IsWeylFamily.alternant_eq`

 The alternant of γ is the Weyl denominator times `Y γ`. 

### `torusEval_rootProd_mul`

 Let `X`, `Y` satisfy Weyl's formula (`IsWeylFamily`). Replacing each monomial `x ^ γ` of `p`
by `Y γ` and multiplying by the Weyl denominator antisymmetrises `p` over the Weyl group
of K. 

### `linearCombination_apply_conj`

 Let `X`, `Y` satisfy Weyl's formula and let `l` be injective. If the antisymmetrisation of
`p` over the Weyl group of K is the Weyl denominator times `q` on the torus, then the combination
of the `X γ` with the coefficients of `p` is `q` on the torus. 

### `linearCombination_rootProd_mul_apply_conj`

 Let `X`, `Y` satisfy Weyl's formula and let `l` be injective. The combination of the `X γ`
with the coefficients of `l.rootProd Eq * p` is, on the torus, the symmetrisation of `p` over the
Weyl group of K, because the Weyl denominator is antisymmetric. 

### `exists_apply_conj_eq`

 Let `X`, `Y` satisfy Weyl's formula and let `l` be injective. A Laurent polynomial `D` that
is symmetric under the Weyl group of K extends from the torus to a continuous class function
on K. 

### `inner_toLp_mul`

 Brauer's rule. Let `l` be injective, and let `X`, `Y` be a Weyl family for `l`: each `X γ` is a
continuous class function on K = U(diag ε) ∩ U(n) that equals the Laurent polynomial `Y γ` on the
diagonal torus, and the Weyl denominator of `l` times `Y γ` is the alternant of `γ`. If a continuous
`d` on K satisfies `d (y diag(x) y⁻¹) = D(x)` for a Laurent polynomial `D = ∑ a_β x ^ β`, then
`⟪X γ, d f⟫ = ∑ a_β ⟪X (-β + γ), f⟫` in L²(K) for the Haar measure of mass one. 

### `eq_linearCombination`

 Completeness. Let `X`, `Y` satisfy Weyl's formula, let `l` be injective and let `e` be an
orthonormal family in L²(K) whose span contains every `X γ`. A continuous class function with
finitely many coefficients `a i` against `e` is `∑ a i • e i`. 

### `torusEval_linearCombination_alternant`

 Let `X`, `Y` satisfy Weyl's formula. On the torus, a combination of alternants is the Weyl
denominator times the same combination of the class functions `X γ`. 

### `New.Orbital.IsStraightening`

 Straightening of exponents: every function `t` antisymmetric under the Weyl group of K has
`t γ = s γ * t (ν γ + δ)` with `ν γ` dominant, where δ = `l.lowerCount Eq`. 

### `New.Orbital.IsStraightening.isKDominant`

 `ν γ` is dominant for K, so it is the highest weight of a K-type. 

### `New.Orbital.IsStraightening.apply_eq`

 The value of an antisymmetric function at γ is `s γ` times its value at `ν γ + δ`. 

### `New.Orbital.virtualChar`

 The virtual character of K attached to the exponent γ: `s γ` times `kTypeChar (ν γ)`, which
is the character of the K-type with highest weight `ν γ` when this weight is dominant. 

### `coeff_alternant`

 For a straightening `s`, `ν`, injective `l` and dominant μ, the coefficient of `x ^ γ` in
the alternant of μ + δ, where δ = `l.lowerCount Eq`, is `s γ` if `ν γ = μ` and `0` otherwise. 

### `apply_add_lowerCount`

 For a straightening `s`, `ν` and injective `l`, an exponent `μ + δ` with μ dominant is
already straight: its weight is μ and its sign is `1`. Here δ = `l.lowerCount Eq`. 

### `exists_isWeylFamily`

 For a straightening `s`, `ν` of exponents and injective `l`, the virtual characters
`s γ • kTypeChar (ν γ)` satisfy Weyl's formula for suitable Laurent polynomials `Y γ`. 

### `inner_virtualChar`

 For a straightening `s`, `ν` of exponents and injective `l`, the inner product in L²(K) of
the virtual characters of γ and μ is the coefficient of `x ^ γ` in the alternant of μ. 

### `orthonormal_virtualChar`

 For a straightening `s`, `ν` of exponents and injective `l`, the virtual characters of the
exponents μ + δ with μ dominant, that is, the characters of the K-types, are orthonormal
in L²(K). Here δ = `l.lowerCount Eq`. 

### `virtualChar_mem_span`

 For a straightening `s`, `ν` of exponents and injective `l`, every virtual character is in
the span of the characters of the K-types. 

### `New.Orbital.integral_mul_dsCoeff_apply_conj`

 Let the class function `d` on K equal `D` on the torus, let `ψ g k = l.dsCoeff (g⁻¹ k g)` and
let `g ↦ d * ψ g` be integrable. Its integral over G is then a class function on K, equal on the
torus to `D` times the orbital integral of the discrete series coefficient `l.dsCoeff`. 

### `New.Orbital.inner_virtualChar_formalDegree_smul_integral`

 Let `ψ g k = l.dsCoeff (g⁻¹ k g)`, let `d` be a class function on K that equals `D` on the
torus, with `g ↦ d * ψ g` integrable, and let `m γ` be the formal degree times the integral over G
of the coefficient of `ψ g` against the character of `ν γ`, assumed integrable. Let `l` be
injective and let the virtual characters of `s`, `ν` satisfy Weyl's formula. Then the inner product
in L²(K) of the virtual character of γ with `l.formalDegree • ∫ d * ψ g` is
`∑ D_β s (-β + γ) m (-β + γ)`, by Brauer's rule. 

### `New.Orbital.exists_int_rootProd_pow`

 The powers of `l.rootProd r` have integer coefficients. 

### `New.Orbital.IsOrbitalLaurent`

 The Laurent polynomial `P` is `Vc D Θ`. Here Θ(x) = deg ∫ ψ(g⁻¹ x g) dg is the normalised
orbital integral of ψ = `l.dsCoeff` on the diagonal torus, `Vc = l.rootProd Eq` is the Weyl
denominator of K, Λ = `l.lowestKType` and δ = `l.lowerCount Eq`. 

### `New.Orbital.IsOrbitalLaurent.antisymm`

 `P` is antisymmetric under the Weyl group of K. 

### `New.Orbital.IsOrbitalLaurent.torusEval_eq`

 On the torus, `P = Vc D Θ`. 

### `New.Orbital.IsOrbitalLaurent.isConeSeriesMultiple`

 `P` is `D` times a series with coefficient `1` at Λ + δ that lives in the Weyl translates
  of Λ + δ + `l.rootCone`. 

### `New.Orbital.exists_classFun_orbital_integral`

 Let `l` have a large gap and let the virtual characters of a straightening `s`, `ν` satisfy
Weyl's formula. With `D` the N-th power of the noncompact root product `(-l).rootProd Ne` and N = 4
(card n)² + 1, some continuous function `h` on K and multiplicities `m γ` of the K-types `ν γ`
satisfy: `h` is a class function equal to `D` times the normalised orbital integral on the torus;
its coefficient against the virtual character of γ is `∑ D_β s (-β + γ) m (-β + γ)`; `m γ = 1` at
the lowest K-type; and `m γ ≠ 0` only if `ν γ - l.lowestKType` lies in `l.rootCone`, the cone of
positive roots. 

### `New.Orbital.exists_laurent_orbital_integral`

 The normalised orbital integral Θ(x) = deg ∫ ψ(g⁻¹ x g) dg, for ψ = `l.dsCoeff` and `l` with a
large gap, becomes a Laurent polynomial once its denominators are cleared; here `n` is nonempty, and
`HasLargeGap` with constant 10 (card n)⁵ means a gap of at least 500 (card n)³ + 10 (card n)⁵. Let
`D` be the N-th power of ∏ (x_a - x_b) over `ε a ≠ ε b`, `l a < l b`, with N = 4 (card n)² + 1 so
that the integral times `D` converges uniformly in x. Then `Vc D Θ`, with `Vc = l.rootProd Eq` the
Weyl denominator of K, is a Laurent polynomial `P` satisfying `New.Orbital.IsOrbitalLaurent`, namely
antisymmetry of `P` and conditions on the leading term and support of `P / D` stated via
Λ = `l.lowestKType` and δ = `l.lowerCount Eq`.

This is the first step to Harish-Chandra's formula for elliptic orbital integrals; the Laurent
polynomial `P` is computed in `Lib.DiscreteSeries.Character.FormalDegree`. 
