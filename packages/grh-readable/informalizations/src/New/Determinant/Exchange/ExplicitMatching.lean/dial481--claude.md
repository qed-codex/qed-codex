---
{
  "module": "src/New/Determinant/Exchange/ExplicitMatching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/ExplicitMatching.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/ExplicitMatching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit real data: the exchange identity for a definite space with determinant data

`New.Rows.exists_stdClassSum_eq_mul_integral_modKernel` follows from the identity
`New.Exchange.exchange_identity` for the positive definite standard space `I_a` of rank `card a`,
with the real data made explicit as products of determinants.

Its archimedean step, `New.Rows.exists_mul_apply_eq_apply_matchedPoly`, takes an identity between
functionals on two Fock spaces that holds for one polynomial and its translates, and moves it to
explicit products of determinants.

## Main definitions and results

* `New.Rows.matchedPoly`: the explicit polynomial for the pair of signs on `b` and on `n`.
* `New.Rows.realPairWeil_stackedDetProd`, `New.Rows.realPairWeil_matchedPoly`: the laws of
  `New.Rows.stackedDetProd` and `New.Rows.matchedPoly` under the real Weil representation
  `New.realPairWeil`.
* `New.Rows.exists_mul_apply_eq_apply_matchedPoly`: the matching of `New.Rows.stackedDetProd` with
  `New.Rows.matchedPoly`.
* `New.Rows.exists_stdClassSum_eq_mul_integral_modKernel`: a multiple, possibly zero, of the class
  sum equals a non-zero multiple of the integral over the group of the complementary space.
* `New.Rows.exists_mul_stdClassSum_eq_integral_modKernel`: the same identity divided by its non-zero
  constant, with the characters absorbed into the kernels and a free character for `I_a`.

Notions from other files:
* `New.GInf`: The archimedean unitary group G_∞ for signs s: one copy of the complex unitary group
  U(diag s) for each infinite place of E.
* `New.PairFock`, `New.Fock.polyVector`, `New.realPairWeil`: the Fock space of a pair of signs, the
  vector in it attached to a polynomial, and the real Weil representation of the pair on it.
* `New.Rows.stackedDetProd`: The product over τ and k of the determinants of M_{τk} stacked over the
  variable matrix x_τ (`New.Rows.stackedDet`), columns ordered by e.
* `New.AreMatched`: Φ lives on the rows `a` of k⁻¹ and Ψ on the columns `b` of k, for k in GL_n(O),
  and there the values differ by the factor χ(det k). Here the subring O is always `⊤`.
* `New.Exchange.lValueProd`: The number (∏_{w ∈ S} Nw)^(e²) · ∏_{z=1}^{e} |L^S(z, ν)|², for a
  natural number e.

## Relation to the literature

A multiple of a theta kernel summed over a definite unitary group equals a kernel integrated over a
unitary group of no larger rank, with explicit determinant polynomials on both sides. The size of
the multiple is given by Hecke L-values and the conductor up to one fixed factor, which may be zero.
The first term identity between theta integrals of complementary spaces and the harmonic polynomials
given by determinants are known in the literature. Related work: Gan–Qiu–Takeda, The regularized
Siegel–Weil formula, 2014 (after Kudla–Rallis, 1994; Ichino, 2004); Kashiwara–Vergne, On the
Segal–Shale–Weil representations and harmonic polynomials, 1978; Böcherer–Schulze-Pillot, Siegel
modular forms and theta series attached to quaternion algebras, 1991.



## Archimedean step for products of determinants in Fock space

Let the pair be U(signs on `n`) × U(`a`). As seen by functionals invariant under U(`a`), a mean over
a circle in the torus removes all variables but one square block, and averaging over U(`a`)
(`New.exists_forall_eq_mul_map_det_pow`) leaves a multiple of the product of determinants for the
standard frame `(1 0)`. Polarisation passes from the unitary translates of that frame to all
matrices, since the products of determinants lie in a module that is irreducible under the unitary
group (`New.exists_pairedDetProd_eq_sum_unitary`).


### `blockSigns`

 The signs on `b ≃ p ⊕ l` that are `+1` on `p` and `-1` on `l`. 

### `posBlockEmb`

 The embedding of the compact groups `U(m)`, one for each infinite place, as the positive block
of the unitary group of signs `blockSigns j`. 

### `coe_inv_posBlockEmb`

 At each place, the inverse of the image of `k` has the matrix of the image of `k⁻¹`. 

### `posBlockEmb_mem_blockDiagAlg`

 At each place, the image of `k` lies in `blockDiagAlg (blockSigns j)`, the algebra of matrices
that commute with the diagonal matrix of the signs, that is, are block diagonal for them. 

### `principalMinor_posBlockEmb_eq_det`

 At each place `τ`, the principal minor of `posBlockEmb j k τ` on the indices `i` with
`blockSigns j i = 1` (the positive block) equals the determinant of `k τ`. 

### `principalMinor_posBlockEmb_eq_one`

 At each place, the negative block of the image of `k` has determinant `1`. 

### `matchedPoly`

 The polynomial `∏_τ det (y⁻_τ) ^ (card (ι τ) + card n - 2 * card l) ∏_{τ, k} det (η_{τ k} y_τ)`,
where `y⁻_τ` is the `l × l` block of variables with both signs negative and `y_τ` the `m × p` block
with both signs positive. The first determinant is `variableMinor` (a minor of the matrix of
variables at `τ`) and the last product is `pairedDetProd`. The subtraction in the exponent is
truncated; it is exact when `2 * card l ≤ card n`. 

### `matchedPoly_smul`

 Scaling all matrices by `w` multiplies `matchedPoly` by `(w ^ card p) ^ card (ι τ)` for each
place `τ`, as each factor that depends on the matrices is a `p × p` determinant. 

### `posFockVector`

 The Fock vector of a polynomial in the variables `a × m`. The map `renameRowsCols` reads them as
variables `a × n` through the positive block of `j`, and `polyVector` sends a polynomial to its
product with the Gaussian in the Fock space `fockSpace`. The signs of the variables are the products
`homSigns` of a row sign and a column sign, repeated at every infinite place by `realSigns`. 

### `differentiable_apply_bind₁_pow_smul`

 For a linear form `L` on polynomials and exponents `w`, the value of `L` at `P` with each
variable `x` multiplied by `s ^ w x` is differentiable in `s`. 

### `realPairWeil_stackedDetProd`

 Fix `j : m ⊕ l ≃ n`, with signs `blockSigns j` equal to `+1` on `m` and `-1` on `l`, and fix
`e : p ⊕ a ≃ m`. `ι τ` indexes `p × m` matrices `η τ i` at each infinite place `τ`. The polynomial
`stackedDetProd e η` is the product of the determinants of `η τ i` stacked over the `a × m` matrix
of variables, with columns ordered by `e`. `posFockVector j` turns it into a vector in the Fock
space of the pair U(`blockSigns j`) × U(`a`).

Let `γ τ = card l - card (ι τ)`, so that `realPairWeil γ 0` is the real Weil representation in which
`(x, u)` is twisted by `∏_τ (det u_τ) ^ γ τ` and not by `det x`. Let `k` be in the group `GInf E 1`,
one copy of U(`m`) for each infinite place, and let `posBlockEmb j k` be its image in the block with
signs `+1`. Then `(posBlockEmb j k, u)` carries this vector for the matrices `η * (kᵀ)⁻¹` to that
for `η`, times the factor `∏_τ (det k_τ) ^ (- card (ι τ))`, which does not depend on `u`. 

### `realPairWeil_matchedPoly`

 Let `γ τ = card l - card (ι τ)` and take the real Weil representation `realPairWeil γ 0` of the
pair of unitary groups with signs `blockSigns f`, `blockSigns j`, in which `(x, y)` is twisted by
`∏_τ (det y_τ) ^ γ τ` and not by `det x`. For `k` in U(`m`) at each place, the point
`posBlockEmb j k`, its image in the positive block of the second group, carries the Fock vector
(`polyVector`) of `matchedPoly` for `η` to that for `η * kᵀ`, times the factor
`∏_τ (det k_τ) ^ (- card (ι τ))`. 

### `standardFrame`

 The standard frame `(1 0)` for `m ≃ p ⊕ a`: the `p × m` matrix whose row `k` is the standard
basis vector at `e (inl k)`. 

### `frameTorus`

 For `|z| = 1`, the point of `U(m)` that is, at every infinite place, the diagonal matrix with
entries `z⁻¹ ^ 2` on `p` and `z⁻¹` on `a`, for `m ≃ p ⊕ a`. 

### `det_frameTorus`

 At each place, `frameTorus E e z` has determinant `z⁻¹ ^ (2 * card p + card a)`. 

### `stackedDet_standardFrame`

 For the standard frame `(1 0)`, the stacked determinant at `τ` is the minor of the variables in
the columns `e ∘ inr`. 

### `exists_mul_eq_circle_mean`

 Let `γ τ = card l - card (ι τ)` and let `y` lie in `PairFock`, the Fock space of the pair
U(signs on `n`) × U(`a`), on which `(x, u)` acts by the real Weil representation `realPairWeil γ 0`,
twisted by `∏_τ (det u_τ) ^ γ τ` and not by `det x`.

For `|z| = 1`, `frameTorus E e z` is the diagonal point of U(`m`) with entries `z⁻²` on `p` and
`z⁻¹` on `a`, put by `posBlockEmb j` in the positive block, and `diagTorus 1 t` is the diagonal
matrix with entries `t`. The vector `Ω z` is `y` moved by the pair of this point and the scalar
`z⁻¹` in U(`a`), times `z⁻¹ ^ (card a * ∑ τ, card (ι τ))`. There is a number `κ` such that, for
every functional `ℓ` invariant under U(`a`), the mean of `ℓ (Ω z)` over the circle is `κ` times `ℓ`
at the Fock vector (`posFockVector`) of `stackedDetProd e` for the standard frame. 

### `exists_eval_stackedDet_eq`

 At each point `x` there are an `m × p` matrix `Y` and a number `d` with
`det (ξ; x τ) = d * det (ξ * Y)` for all `p × m` matrices `ξ`; here `ξ` is stacked over `x τ`, with
columns ordered by `e`. 

### `exists_stackedDetProd_eq_sum_unitary`

 Let `a` be non-empty and fix `f : p ⊕ l ≃ b`, `j : m ⊕ l ≃ n`, `e : p ⊕ a ≃ m`. For `p × m`
matrices `ξ τ i`, indexed by `ι τ` at each infinite place `τ`, `stackedDetProd e ξ` is the product
of the determinants of `ξ τ i` stacked over an `a × m` matrix of variables, and `matchedPoly f j ξ`
the product of the `det (ξ τ i * y_τ)`, with `y_τ` an `m × p` block of variables, and a fixed
polynomial. Both are finite combinations, with the same coefficients, of the same polynomials for
the unitary translates `frame k τ i = standardFrame e * (k τ)ᵀ` of `standardFrame e`, the `p × m`
matrix `(1 0)`, with `k τ` in U(`m`). 

### `exists_mul_apply_eq_apply_matchedPoly`

 Let `a` be non-empty, fix `f : p ⊕ l ≃ b`, `j : m ⊕ l ≃ n`, which give signs `+1` on `p`, `m`
and `-1` on `l` (`blockSigns`), and `e : p ⊕ a ≃ m`, and let `γ τ = card l - card (ι τ)`.

There is a polynomial `Q₀` such that every vector `v` has a number `κ` with the following property.
Let `ℓ g` be continuous functionals and `ℓ'` a linear form on polynomials such that (a)
`ℓ g (realPairWeil γ 0 (x₁, x₂) w) = ℓ (g x₁) w`; (b) `ℓ x v = ℓ' Q` whenever `x` carries the Fock
vector of `Q₀` to that of a polynomial `Q`. Then `κ * ℓ 1` at the Fock vector of
`stackedDetProd e η` is `ℓ' (matchedPoly f j η)` for all matrices `η`. 

### `exists_clm_eq_thetaIntegral_modDatum`

 Let `I_a` be the positive definite standard space `stdSpace E a` and let `Φ` be a function on
matrices modulo `𝔪`. The theta integral over `U(I_a)` with characters `α`, `β`, at a point `g` of
`U(S)`, is a continuous linear functional of the real part `w` of the datum `modDatum`, whose finite
part is given by `Φ`. 

### `exists_linearMap_eq_integral_modKernel`

 Let `𝔪` not be the unit ideal, and let `Φ`, `Ψ` be matched functions for `χ` (`AreMatched`). Fix
`g` in `G E t`. Integrate over the quotient of `G E s` by the rational points of `S`
(`quotMeasure`). The integrand is the theta kernel `modKernel` of `(S, T)` at `(x, g)`, twisted by
`α`, `β`, with data `Ψ`, `Q`. The integral is a linear form `ℓ` in the polynomial `Q`. 

### `integral_modKernel_stackedDetProd`

 Let `W` have `card l` negative signs and let `I_a` be the positive definite standard space
`stdSpace E a`. Let the character `α` be tame for `(𝔪, χ)` of weight `card l - card (ι τ)`. Let `Φ`
have a matched function `Ψ` for `χ⁻¹` (`AreMatched`): for invertible `k` modulo `𝔪` they vanish off
the rows `a` of `k⁻¹` and the columns `b` of `k` respectively, with `Φ = χ⁻¹ (det k) Ψ` there. Take
the theta kernel `modKernel` of `(W, I_a)` with the characters `α`, `1` and the data `Φ`,
`stackedDetProd e η`; `modKernelStdSpace` is its restriction to the finite points `h` of `U(I_a)`.
The integral of the kernel over `U(I_a)` is the class sum of this restriction: the sum of its values
over the double cosets of the rational points and of the integral finite points `stdLevel E a`, each
divided by the number of automorphisms of the class. 

### `exists_stdClassSum_eq_of_exchange`

 Let `W` and `V'` both have `card l` negative signs (`j` and `f` split their bases by sign), let
`I_a` be the positive definite standard space `stdSpace E a` with `a` non-empty, and let `σ` give
`n = b ⊕ a`; `e` orders the columns of the determinants, of which `ι τ` indexes those at the place
`τ`. There is a polynomial `Q₀` such that every real datum `v`, a vector in the Fock space
`PairFock` of `(W, I_a)`, has a number `c'` with the following property. Let the character `α` be
tame for `(𝔪, χ)` of weight `card l - card (ι τ)`, let `Φ`, `Ψ` be matched functions for `χ⁻¹`, and
suppose that at every point the theta integral over `U(I_a)` with datum `Φ`, `v` is `c` times the
integral over `U(V')` of the kernel with data `Ψ`, `Q₀`. Then `c'` times the class sum for `Φ`,
`stackedDetProd e η` is `c` times the integral for `Ψ`, `matchedPoly f j η`. Here
`stackedDetProd e η` is the product of the determinants of the `p × m` matrices `η τ i` stacked over
the variables `a × m`, and `matchedPoly f j η` the product of the `det (η τ i * y_τ)`, with `y_τ`
the block of `n × b` variables with both signs `+1`, and of powers of the determinants of the blocks
with both signs `-1`. The class sum `stdClassSum` runs over the double cosets of the finite points
of `U(I_a)` by the rational points and the integral points `stdLevel E a`, each weighted by the
inverse of its number of automorphisms. 

### `exists_stdClassSum_eq_mul_integral_modKernel`

 Explicit exchange of theta kernels. Index types stand for their cardinalities. Let `W` of rank
`n` and `V'` of rank `b` both have `l` negative signs (`j : m ⊕ l ≃ n` and `f : p ⊕ l ≃ b` split
their bases by sign), let `I_a` be the positive definite standard space, and let `n = b + a` (by
`σ`), `a = b + 2 d` and `n = 2 l + 2 s₀` with `s₀ ≥ 1`; `e : p ⊕ a ≃ m` orders the columns of the
determinants, of which `ι τ` indexes those at the place `τ`. The kernels carry the standard
characters: `υ ^ l` for `W` and `V'`, and `1` for `I_a`, where `υ` is `upsilonU1`, the character of
the Weil data on `U(1)`.

There are numbers `C > 0` and `c'`, possibly `c' = 0`, such that every character `α` of weight
`-card (ι τ)` that is tamely ramified exactly at the places of `𝔪 ≠ 1`, with character `χ` of the
residue ring, has a number `c` with (a) and (b). (a) `‖c‖² = C * lValueProd 𝔪.places ν⁻¹ d ≠ 0` for
`ν = α / υ ^ s₀`. Here `lValueProd 𝔪.places μ d`, for a character `μ`, is the norm factor
`(∏_{w ∣ 𝔪} Nw) ^ (d ^ 2)` times `∏_{1 ≤ z ≤ d} |L^S(z, μ)| ^ 2`, where `L^S(z, μ)` is the Euler
product at `z` of the base change of `μ` outside the places `S` of `𝔪` and their conjugates.
(b) For all matrices `η`, all `g` and all matched functions `Φ`, `Ψ` for `χ⁻¹` (`AreMatched`: for
invertible `k` modulo `𝔪` they vanish off the rows `a` of `k⁻¹` and the columns `b` of `k`
respectively, with `Φ = χ⁻¹ (det k) Ψ` there), the number `c'` times the class sum at the level
`stdLevel E a` over finite points `h` of `U(I_a)` of `α (det h)` times the kernel of `(W, I_a)` with
data `Φ`, `stackedDetProd e η` (read in the variables `a × n` through `j`) equals `c α (det g)`
times the integral over `x` in `U(V')` of `α (det x)⁻¹` times the kernel of `(V', W)` with data `Ψ`,
`matchedPoly f j η`. The first polynomial is the product of the determinants of `η τ k` stacked over
the `a × m` matrix of variables; the second is the product of the `det (η τ k * y_τ)`, for `y_τ` the
`m × p` block of variables with positive signs, and of powers of the determinants of the `l × l`
blocks with negative signs. 

### `exists_mul_stdClassSum_eq_integral_modKernel`

 Index types stand for their cardinalities. Let `W` of rank `n` and `V'` of rank `b` both have
`l` negative signs, let `I_a` be the positive definite standard space, and let `n = b + a` (by `σ`),
`a = b + 2 d` and `2 l + 2 ≤ n`; `e : p ⊕ a ≃ m` orders the columns of the determinants. The finite
sets `ι τ` index the determinants at the infinite place `τ`, and `η` gives one `p × m` matrix for
each of them.

There is a number `C`, which may be `0`, with the following property. Every character `α` of weight
`l - card (ι τ)` that is tame for `(𝔪, χ)` has a number `c` with (a) and (b). (a)
`‖c‖² = C / lValueProd 𝔪.places μ d` for `μ = α⁻¹ υ ^ (b + d)`, where `υ` is `upsilonU1`, the
character of the Weil data on `U(1)`, and the denominator, which is non-zero here, is `(∏_{w ∣ 𝔪}
Nw) ^ (d ^ 2) * ∏_{1 ≤ z ≤ d} |L^S(z, μ)| ^ 2`, with `L^S` the Euler product of the base change of
`μ` outside the places `S` of `𝔪` and their conjugates. (b) Let `η`, `β`, `g` be given and let `Φ`,
`Ψ` be matched functions for `χ⁻¹` (`AreMatched`: for invertible `k` modulo `𝔪` they vanish off the
rows `a` of `k⁻¹` and the columns `b` of `k` respectively, with `Φ = χ⁻¹ (det k) Ψ` there). Then `c`
times the class sum over `U(I_a)` of the kernel of `(W, I_a)` with characters `α`, `β` and data `Φ`,
`stackedDetProd e η` equals the integral over `U(V')` of the kernel of `(V', W)` with characters
`α / β`, `α` and data `Ψ`, `matchedPoly f j η`. 

### `areMatched_det_one`

 Let `b` be empty, so that `σ` identifies `a` with `n`. The functions `χ ∘ det` on `a × n`
matrices and `1` on `n × b` matrices are matched functions for `χ⁻¹` (`AreMatched`): they live on
the rows of the inverses and on the columns of invertible matrices, with values differing by `χ⁻¹`
of the determinant. 

### `integral_one_quotMeasure_of_isEmpty`

 Let `V'` be a hermitian space over the CM field `E` of rank zero (`b` is empty), with signs `t`
at the infinite places. The quotient of its adelic unitary group `G E t` by the rational points,
with the measure `quotMeasure`, has volume `1`. 

### `matchedPoly_of_isEmpty`

 For `b` empty the polynomial `matchedPoly` is `1`, being a product of empty determinants. 

### `modKernel_one_of_isEmpty`

 Let `V'`, `W` be hermitian spaces over the CM field `E` with signs `t`, `s` at the infinite
places, and let `V'` have rank zero. The theta kernel `modKernel` of `(V', W)` twisted by the
characters `α`, `β` of the norm-one ideles, for the constant function `1` modulo `𝔪` and the
constant polynomial `1`, takes the value `α (det g)` at `(x, g)`: the theta series is a sum over
the zero space. 

### `integral_modKernel_matchedPoly_of_isEmpty`

 For a space `V'` of rank zero and a hermitian space `W` with signs `s`, the integral over the
quotient of `U(V')` by its rational points (`quotMeasure`) of `α (det x)⁻¹` times the theta kernel
`modKernel` of `(V', W)` at `(x, g)`, with both characters `υ ^ l` (`upsilonU1` is `υ`) and data the
constant function `1` modulo `𝔪` and `matchedPoly f j η` (here the constant polynomial `1`), is
`1`. 
