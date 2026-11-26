---
{
  "module": "src/Lib/SiegelWeil/RallisInner/SharpData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/RallisInner/SharpData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/RallisInner/SharpData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rallis' inner product formula for sharp data and injectivity of the theta lift

This file proves Rallis' inner product formula for the theta lift `New.Space.lift` from `U(S)` to
`U(T)` when `rk T > 2 rk S`, for data `v ⊗ F` with `F` sharp (`New.SiegelWeil.IsSharp`). It starts
from `New.SiegelWeil.inner_product_formula`. For `v` an edge from type `e`, the lift is injective
on `J`-invariant forms of type `e`. The file then derives `IsSharp` from `New.SiegelWeil.IsSharpFn`,
a condition on a level `J` and a function `Ψ` on matrices modulo 𝔪, if all signs of `S` agree or
𝔪 ≠ (1), with `S₀` the set of places of 𝔪𝔪̄ and the mass `c` the mean of `|Ψ|²` over the index of
`J`. Finally it computes the vacuum sum in rank one as a partial Hecke L-value over a partial
Euler product.

## Main definitions and results

* `New.SiegelWeil.IsSharp.petersson_lift_eq_integral`: for a sharp datum the Petersson product
  (`New.Space.petersson`) of two lifts is a real integral against the series
  `New.SiegelWeil.rallisSeries` of the places off `S₀`. The finite points are cut into cosets in
  `New.SiegelWeil.IsSharp.hasSum_integral_weilMatrixCoeff_mul`.
* `New.SiegelWeil.exists_petersson_formLift_eq_rallisSeries`: for `v` an edge (`New.IsEdge`) from
  type `e`, the lift is injective on `J`-invariant forms of type `e`, and the product of two lifts
  is a multiple of the pairing with the series; `New.SiegelWeil.rallis_inner_product_cosetTerm`
  expands the series.
* `New.SiegelWeil.IsSharpFn.isSharp`: if all signs of `S` agree or 𝔪 ≠ (1), a function on matrices
  modulo 𝔪 that is sharp for a level J (`New.SiegelWeil.IsSharpFn`) gives a finite datum whose
  matrix coefficient is constant on J and zero at the other points integral off 𝔪𝔪̄
  (`New.SiegelWeil.IsSharp`). `New.SiegelWeil.isSharp_vacuumDatum_of_mul_eq_one` is the case of the
  principal level.
* `New.vacuumSum_eq_L_div_eulerProd`: in rank one and for target rank 2k with k > 1, the sum
  `New.SiegelWeil.vacuumSum` of the vacuum coefficient over the cosets at the places off a set and
  its conjugate, where the tame part is trivial, is a partial Hecke L-value at k over the partial
  Euler product of the signs `New.placeSign` (a partial value of ζ_F at 2k if E is unramified
  over its real subfield F).

Notions from other files:
* `New.Space.integrated`: the datum v ⊗ F = ∫ v(y) ϱ(y) F dy, for v in the Fock model and ϱ the
  Heisenberg operators of the real vectors y.
* `New.IsEdge`: what the formula uses of the real vector v and the types e, e'. The vector of the
  joint harmonic of corresponding parameters is an edge between the types of these parameters
  (`New.ParamsCorrespond.isEdge_jointHarmonic`).
* `New.Modulus.liftFn`: a function of vectors modulo 𝔪, read on finite adelic vectors: its value at
  the reduction if the components at the places of 𝔪 are integral, and 0 otherwise.
* `New.SiegelWeil.IsSharp` (from `Lib.SiegelWeil.RallisInner.Doubling`): `F` is a vacuum off a
  set `S₀` of places; at the finite points integral off `S₀` the coefficient `⟨F, ω(g) F⟩` is
  `⟨F, F⟩` on `J ∩ stdLevel E n` and zero otherwise, and `⟨F, F⟩` over the index of
  `J ∩ stdLevel E n` in `stdLevel E n` is the mass `c`.

## Relation to the literature

Rallis inner product formula by doubling. Here the unramified integrals are left as a convergent
sum over cosets. For its sources see `Lib.SiegelWeil.RallisInner.Doubling`.

Non-vanishing of theta lifts in large rank. Here it is proved for unitary groups with target rank
more than twice the source rank, for finite data sharp at a level and without L-functions. If the
lift vanishes, the real matrix coefficient of the datum convolves the form to zero. Source:
S. Rallis, Injectivity properties of liftings associated to Weil representations, Compositio 52
(1984); J.-S. Li, Non-vanishing theorems for the cohomology of certain arithmetic quotients,
Crelle 428 (1992).

Critical Hecke L-values of CM fields as squared norms of theta lifts from U(1). Here the values are
taken at integers k at least 2, and the trivial character of U(1) is lifted to a definite U(2k),
with the tame Hecke character entering through the splitting. The squared norm is an explicit
constant times the L-value, and the lift is integral. Galois conjugates of the lift belong to
conjugate characters. This file contains only the local sum and the Euler product; the norm formula
is `New.LValueData.inner_trivialLift_self_eq_L`. Source: G. Shimura, On some arithmetic properties
of modular forms of one and several variables, Ann. of Math. 102 (1975); method: T. Yang, Theta
liftings and Hecke L-functions, J. reine angew. Math. 485 (1997); Harris, Li, Skinner, The Rallis
inner product formula and p-adic L-functions (2005); Finis, Ann. of Math. 163 (2006).



## Rallis' inner product formula for sharp data, and injectivity

Rallis' inner product formula for the theta lift `New.Space.lift` from `U(S)` to `U(T)` in the range
`rk T > 2 rk S`, for data `φ = v ⊗ F` (`New.Space.integrated`) with `v` in the Fock space and `F` a
sharp finite datum (`New.SiegelWeil.IsSharp`): a vacuum off a set `S₀` of places, whose matrix
coefficient at the points integral off `S₀` is supported on `J ∩ stdLevel E n` and constant there,
of mass `c`.

The proofs start from the doubling formula `New.SiegelWeil.inner_product_formula`, an integral over
`U(S)(𝔸)`.


### `IsSharp.isOpen_level`

 If the finite datum `F` is sharp for the group `J`, then `J` is open. 

### `IsSharp.integral_ite_eq_mass`

 For `F` sharp for `J`, of mass `c`, the function equal to `⟨F, F⟩` on `J ⊓ stdLevel E n` and to
zero elsewhere has integral `c` over the finite points, for the Haar measure that gives
`stdLevel E n` volume `1`. 

### `weilMatrixCoeff_integrated`

 Let `F` be a finite datum, `v` a vector of the Fock space and `φ = v ⊗ F`. The matrix
coefficient of `φ` at the point `(x, g)` is the real coefficient `⟨v, Ω(x) v⟩` times the finite
coefficient `⟨F, ω(g) F⟩`. Here `Ω(x) = realPairWeil γ γ' (x, 1)`, with `γ'` the weight of `b` and
any `γ`. 

### `IsSharp.weilMatrixCoeff_integrated_mul`

 The coefficient of a sharp datum. Let `F` be sharp for `J` off `S₀`, `v` a vector of the Fock
space and `φ = v ⊗ F`. For a real point `x`, a finite point `u` supported on `S₀ᶜ` and its conjugate
and a finite point `g` integral off `S₀`, `⟨φ, ω(x u g) φ⟩` is the product of the real coefficient
`⟨v, Ω(x) v⟩`, the coefficient of the vacuum at `u`, and `⟨F, F⟩` times the indicator of
`J ⊓ stdLevel E n` at `g`. Here `Ω(x) = realPairWeil γ γ' (x, 1)`, with `γ'` the weight of `b` and
any `γ`. 

### `IsSharp.inf_supportedOn_le`

 Let `b` have weight `γ'` and tame part `ψ`, and let `F` be sharp for `J` off `S₀` (see
`IsSharp`). Then `J` contains every point of `stdLevel E n`, the stabiliser in `G_f` of `Ô ^ n`,
whose component is 1 at every place outside `S₀ᶜ` and the conjugate places of `S₀ᶜ`. 

### `IsSharp.isUnramifiedOn`

 Let `b` have a weight and a tame part. If `F` is sharp, a vacuum off `S₀`, then `b ∘ det` is
trivial on the integral points supported on the places of `S₀ᶜ` and their conjugates. 

### `_root_.New.hasSum_setIntegral_mul_coset`

 Cutting an integral over a group into cosets. Let `μ` be left invariant on `H`, let `L` be a
measurable subgroup with countably many cosets, represented by the points `r q`. The integral of an
integrable `Φ` is the sum over the cosets `q` of the integrals of `g ↦ Φ (r q * g)` over `L`. 

### `IsSharp.hasSum_integral_weilMatrixCoeff_mul`

 Let `F` be sharp for `J` off `S₀`, of mass `c`, let `v` be a vector of the Fock space,
`φ = v ⊗ F` and `x` a real point, and let `P` be a right `J`-invariant function on the finite
points. If `g ↦ ⟨φ, ω(x g) φ⟩ P(g)` is integrable, its integral is the sum, over the cosets `q` of
the points integral off `S₀`, of `c ⟨v, Ω(x) v⟩` times the coefficient of the vacuum and the value
of `P` at `cosetRep q`, the representative of `q` supported on `S₀ᶜ` and its conjugate. Here
`Ω(x) = realPairWeil γ γ' (x, 1)`, with `γ'` the weight of `b` and any `γ`. 

### `IsSharp.petersson_lift_eq_integral`

 Inner product formula. Let `2 * card n < card m`, let `F` be sharp for `J` off `S₀` with mass
`c` (see `IsSharp`), let `v` be a Fock-space vector, and let `Θ` be the lift by `v ⊗ F` for the
characters `a`, `b`. Let `y`, `y'` be rapidly decreasing automorphic functions with `y` fixed by
`J`. Let `z = rallisSeries (card m) b S₀ᶜ y` be the series `∑ mc(q) R(q) y` over the cosets `q` of
the finite points integral at `S₀ᶜ`, with `mc` the vacuum coefficient. Then `⟨Θ y', Θ y⟩` equals the
volume of `[U(T)]` times `c` times the absolutely convergent integral of `⟨v, Ω(x) v⟩ ⟨y', R(x) z⟩`
over the real points `x` of `U(S)`. Here `R` is right translation and
`Ω(x) = realPairWeil γ γ' (x, 1)`, with `γ'` the weight of `b` and `γ` arbitrary. 

### `realConv_eq_zero_of_lift_eq_zero`

 Let `card m > 2 * card n` and let `F` on `Hom(S, T)` be sharp for `J` off `S₀` with mass `c`
(see `IsSharp`). Let `y` be automorphic, rapidly decreasing and fixed by `J`, let `v` be a
Fock-space vector and let `a`, `b` be characters. If the theta lift of `y` by `v ⊗ F` for
`pairThetaKer S T a b` vanishes and `x ↦ ⟨v, Ω(x) v⟩` is integrable, then its convolution `realConv`
with `y` is zero. Here `Ω(x) = realPairWeil γ γ' (x, 1)`, with `γ'` the weight of `b`. 

### `exists_petersson_formLift_eq_rallisSeries`

 Injectivity and norm of the lift, in Weil's range `2 * card n < card m`. Let the vector `v` of
the Fock space be an edge (a real datum that carries type `e` to type `e'`, such as the vector of
the joint harmonic of corresponding parameters) for the weights `γ`, `γ'`. There is `C ≠ 0`,
depending only on these real data and the spaces, with the following property. Let `a`, `b` be
characters of weights `γ`, `γ'`, let the finite datum `F` be sharp for `J`
off `S₀`, of mass `c` (see `IsSharp`), and let `L` be the lift by `v ⊗ F`. On the forms `y` of type
`e` fixed by `J` the lift is injective, and `⟨L y', L y⟩` is `C c` times the Petersson product of
`y'` with the series `rallisSeries` of `y` off `S₀`, for all forms `y'` of type `e`. 

### `rallis_inner_product_cosetTerm`

 Rallis' inner product formula with the series written out as a sum over cosets. Let
`2 * card n < card m` and let `v` be an edge from type `e` to type `e'` for the weights `γ`, `γ'`.
There is `A ≠ 0`, depending only on the spaces `S`, `T` and the real data, with the following
property. Let `a`, `b` be characters of weights `γ`, `γ'`, let the finite datum `F` be sharp for `J`
off `S₀`, of mass `c`, and let `L` be the lift by `v ⊗ F`. Then `L` is injective on the forms of
type `e` fixed by `J`, and for such a form `y` and any form `y'` of type `e`, `⟨L y', L y⟩` is the
absolutely convergent sum of `A * c` times `cosetTerm` (the vacuum coefficient at `q` times
`⟨y', R(q) y⟩`) over the cosets `q` of the points integral off `S₀`. 


## Sharp data modulo 𝔪 and the vacuum sum in rank one

A modulus 𝔪 (`New.Modulus`) is a nonzero ideal of O_E prime to its conjugate; `𝔪.ResidueRing` is
O_E/𝔪 and `𝔪.places` the set of places dividing 𝔪.


### `SiegelWeil.IsSharpFn`

 A function `Ψ ≠ 0` on matrices modulo `𝔪` is sharp for a group `J` with `J(𝔪) ≤ J ≤ K₀` if `J`
fixes `Ψ ⊗ vac` and, for a fixed matrix `A`, the matrix `A x` lies in the image of `J` whenever
`Ψ x ≠ 0`. Here `K₀ = stdLevel E n` is the group of integral points, `J(𝔪)` consists of those that
are `1` modulo `𝔪`, and `Ψ ⊗ vac = vacuumDatum S T 𝔪 Ψ`. 

### `SiegelWeil.IsSharpFn.principal_le`

 The principal level of `𝔪` lies in `J`. 

### `SiegelWeil.IsSharpFn.le_stdLevel`

 The points of `J` are integral. 

### `SiegelWeil.IsSharpFn.ne_zero`

 The function is not zero. 

### `SiegelWeil.IsSharpFn.fixes`

 The group `J` fixes the datum `Ψ ⊗ vac`. 

### `SiegelWeil.IsSharpFn.exists_mul_eq`

 On the support of `Ψ` the matrix `A x` is the reduction of a point of `J`. 

### `SiegelWeil.IsSharpFn.isPrimitiveMatrix`

 If `Ψ` is sharp for `J`, then at a place of `𝔪` every matrix in the support of the lift of `Ψ`
to finite adelic vectors is primitive: integral with an integral left inverse. 

### `SiegelWeil.IsSharpFn.eq_zero_or_eq_zero`

 Let `Ψ` be sharp for `J` and let the integral point `g` lie outside `J`. Then `x` and `x ḡ`,
where `ḡ` is `g` modulo `𝔪`, are not both in the support of `Ψ`. 

### `SiegelWeil.pairWeil_stdLevel_vacuumDatum`

 An integral finite point `k` of `U(S)` sends the datum `Ψ ⊗ vac` to `b(det k)⁻¹` times the datum
of `x ↦ Ψ (x k̄)`, where `k̄` is `k` modulo `𝔪`. 

### `SiegelWeil.IsSharpFn.weilMatrixCoeff_eq_zero_of_mem_stdLevel_of_notMem`

 Let `Ψ` be sharp for `J` and let the integral point `g` lie outside `J`. Then the matrix
coefficient at `g` of the datum `Ψ ⊗ vac` is zero. 

### `SiegelWeil.IsSharpFn.weilMatrixCoeff_eq_zero_of_notMem_stdLevel`

 Let `Ψ` be sharp for `J` and let the finite point `g` be integral off `𝔪 𝔪̄` but not everywhere.
Then the matrix coefficient at `g` of the datum `Ψ ⊗ vac` is zero. 

### `SiegelWeil.IsSharpFn.isSharp`

 The coefficient of a sharp datum. Let the signs of `S` agree or `𝔪 ≠ (1)`, and let `Ψ` be sharp
for `J` relative to `b` (`IsSharpFn`): `Ψ ≠ 0` is a function on `m × n` matrices modulo `𝔪`,
`J(𝔪) ≤ J ≤ K₀` with `K₀ = stdLevel E n`, `J` fixes `Ψ ⊗ vac`, and for a fixed matrix `A` the matrix
`A x` lies in the image of `J` whenever `Ψ x ≠ 0`. Then `Ψ ⊗ vac` (`vacuumDatum`) satisfies
`IsSharp` for `J` off the places of `𝔪 𝔪̄`: its matrix coefficient at the finite points integral off
`𝔪 𝔪̄` is the mean of `|Ψ|²` times the indicator of `J`, and its mass is this mean divided by the
index `[K₀ : J ∩ K₀]`. 

### `SiegelWeil.isSharpFn_of_mul_eq_one`

 Let `b` have weight `γ` and tame part `ψ` trivial at every finite place not dividing `𝔪`. Let
`F ≠ 0` be a function on `m × n` matrices modulo `𝔪` with `A * x = 1` whenever `F x ≠ 0`. Then `F`
is sharp (`IsSharpFn`) for the principal level `J(𝔪) = 𝔪.levelOfSubgroup ⊥`, the points of
`stdLevel E n` that are `1` modulo `𝔪`: `J(𝔪)` fixes `F ⊗ vac`, and `A x` lies in the trivial image
of `J(𝔪)` modulo `𝔪` whenever `F x ≠ 0`. Examples are the point datum, which is the indicator of the
matrix with blocks `1` and `0`, and the constant `1` for `𝔪 = (1)`. 

### `SiegelWeil.isSharp_vacuumDatum_of_mul_eq_one`

 The case of the principal level. Let the signs of `S` agree or `𝔪 ≠ (1)`, let `b` have trivial
tame part off `𝔪`, and let `F ≠ 0` be supported in `{x | A x = 1}`. Then the datum
`vacuumDatum S T 𝔪 F`, which is `F` at `𝔪` and the vacuum elsewhere, satisfies `IsSharp` for
`J(𝔪)` off the places of `𝔪 𝔪̄`. Its mass is the mean of `|F|²` divided by the order of
`GL_n(𝓞/𝔪)`. 

 ### The value of the vacuum coefficient 

### `AutChar.HasWeight.apply_eq_one`

 Let the character `b` have weight `l` and tame part `ψ` (`New.AutChar.HasWeight`). Then `b` is
trivial at an adelic point `u` of `U(1)` that is `1` at infinity, integral at the finite places,
and `1` at every finite place where `ψ` is not trivial. 

### `SiegelWeil.vacuumCoeff_eq_spaceChar`

 Let the finite unitary point `γ` be supported on the places in `A` and their conjugates, and
let the character `b` have a weight and a tame part `ψ` that is trivial there. Let `y` saturate `γ`,
that is `y Ôⁿ = Ôⁿ ∩ γ⁻¹ Ôⁿ`, and let `c` be an idele of the ideal `𝔣` of `det y` that is `1` at
the other places. Then the vacuum coefficient `(b(det γ) * finMultiplier γ ^ M)⁻¹` is
`χ(c) |c| ^ (M / 2) = χ(𝔣) N𝔣 ^ (-M / 2)`, where `χ = b.spaceChar M` is the splitting character. 

 ### The vacuum sum in rank one 

### `placeSign`

 The sign −1 if w precedes w̄ in a fixed well-ordering, else 1: so 1 if w = w̄, and one of
each sign on a split pair. The product over the places w above a place of norm q of the real
subfield F of the factors 1 − ε_w q_w^(−k) is 1 − q^(−2k) if this place is split or inert, an
inverse Euler factor of ζ_F(2k). 

### `placeSign_factor_mul`

 At a place `w` that differs from its conjugate `w̄`, the signs `placeSign` of `w` and `w̄`
are opposite, so `(1 - ε_w̄ x) (1 - ε_w x) = 1 - x ^ 2`. 

### `glMultiplier_singleGL_uniformizer_zpow`

 The value of the multiplier `glMultiplier` of the Weil representation at `singleGL w (ϖ_w ^ z)`,
the adelic point that is the power `z` of the uniformiser at `w` and `1` elsewhere: it is
`(υ(ϖ_w) √q_w) ^ (-z)` for `z ≤ 0` and `1` for `z ≥ 0`. 

### `mem_localIntGL_unit_iff`

 In rank one a point at `w` lies in the integral level `localIntGL Unit w` exactly when its
determinant has order zero. 

### `vacuumCoeff_ofSplitPlace_uniformizer_zpow`

 The vacuum coefficient in rank one at a split place `w`. Here `vacuumCoeff M b g = (b(det g) *
finMultiplier g ^ M)⁻¹` is the factor by which `g` changes the matrix coefficient of a vacuum. Let
`ν` have weight `l` and tame part `ψ`, trivial at `w` and `w̄`. Let `γ = ofSplitPlace (ϖ_w ^ z)` be
the unitary point with component `ϖ_w ^ z` at `w`, its conjugate inverse at `w̄` and `1` elsewhere.
Write `υ` for the splitting character (`upsilonU1` on `U(1)`), and
`ν̃(ϖ_u) = ν.baseChange.atUniformizer u` for the value of the base change of `ν`. Then
`vacuumCoeff (2 k) (ν υ ^ k) γ` is `(ν̃(ϖ_u) / q_u ^ k) ^ |z|`, with `u = w̄` if `z ≥ 0` and `u = w`
otherwise, where `q_u` is the norm of `u`. 

### `exists_hasSum_vacuumCoeff_at_place`

 Let `ν` have weight `l` and tame part `ψ`, trivial at the place `w` and at its conjugate `w̄`,
and let `k > 1`.
There is a family `r` of finite points of `U(1)` supported at `w` and `w̄` such that (a) `r`
represents the cosets of the points integral at `w`, and (b) the sum over `r` of the vacuum
coefficients `vacuumCoeff (2 k) (ν υ ^ k)` is the product over `u ∈ {w, w̄}` of
`(1 - ε_u q_u ^ (-k)) / (1 - ν̃(ϖ_u)⁻¹ q_u ^ (-k))`, where `ν̃` is the base change `ν.baseChange`.
Here `ε = placeSign` is the sign that is `1` when `u = ū` (inert or ramified), and `-1` for one
place and `1` for the other of a split pair `u ≠ ū` (fixed by a well-ordering); `υ` is the splitting
character, `upsilonU1` its restriction to `U(1)`, and `localLevel Unit {w}` consists of the points
integral at `w`. 

### `vacuumSum_pair`

 The sum of the vacuum coefficients at one place of the real subfield. Let `ν` have weight `l`
and tame part `ψ`, trivial at `w` and `w̄`, and let `k > 1`. In rank one the sum `vacuumSum` at
`{w, w̄}` of the coefficients `vacuumCoeff (2 k) (ν υ ^ k)` is the product over `u ∈ {w, w̄}` of
`(1 - ε_u q_u ^ (-k)) / (1 - ν̃(ϖ_u)⁻¹ q_u ^ (-k))`. Here `υ` is the splitting character
(`upsilonU1` on `U(1)`), `ε` is `placeSign`, `ν̃` is the base change `ν.baseChange`, `ϖ_u` is
the uniformiser at `u` and `q_u` the norm of `u`. 

### `vacuumSum_eq_L_div_eulerProd`

 The Euler product in rank one. Let `ν` have weight `l` and tame part `ψ`, trivial off the set
`S` of places, let `D = S ∪ S̄`, and let the second space have rank `card m = 2 k` with `k > 1`. The
sum `vacuumSum` of the coefficients `vacuumCoeff (2 k) (ν υ ^ k)` over the cosets at the places off
`D` is `L^D(k)` divided by the Euler product at `k` of the signs `placeSign` off `D`. Here `υ` is
the splitting character (`upsilonU1` on `U(1)`), and `L^D = ν⁻¹.L S` is the `L`-function of the base
change of `ν⁻¹` without the factors at `D`, equal to `ν.L S` (`New.AutChar.HasWeight.L_inv`). If `E`
is unramified over its real subfield `F` off `D`, the denominator is the value at `2 k` of the zeta
function of `F` without the places below `D`. 
