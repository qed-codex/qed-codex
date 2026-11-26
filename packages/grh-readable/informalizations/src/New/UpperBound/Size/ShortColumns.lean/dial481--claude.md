---
{
  "module": "src/New/UpperBound/Size/ShortColumns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prime-by-prime divisibility measures; short forms span the ramified source forms

This file defines numbers that measure, prime by prime, how divisible the chain of theta lifts on
source forms must be, and shows that short algebraic forms span. `New.AlgForm` is the space of
algebraic forms of weight (κ, e) on the definite unitary group of `New.stdSpace`, with right
translation `New.algFormRep`. The source forms `New.Data.SourceForm` form its subspace fixed by
`New.Data.levelX` 0. `New.Data.piNPlaces` is the set of the f primes dividing π, where ππ̄ = N and f
is the number of infinite places of E. Short forms span at a free level.

## Main definitions and results

* `New.Data.localPrimeSum`: the exponent asked at p for a height y at an infinite place σ.
* `New.Data.localPrimeSumTotal`, `New.Data.gain`: the sum of these exponents over all infinite
  places, and the total exponent asked of the m lifts.
* `New.IsShort`: the values of a form are p-adically integral, and their conjugates under Aut(ℂ)
  have squared norm at most B.
* `New.span_isShort_eq_top`: at a free level K ≤ `New.stdLevel` the short forms span, for an
  explicit B.
* `New.Data.scalingGenerator`: for w ∣ π a scaling z_w at w (`New.Data.IsScalingAt`) of order N − 1
  modulo w.
* `New.Data.ramifiedSourceForms`: the source forms whose translates by the powers of each z_w have
  mean 0; `New.Data.ramifiedSourceForms_eq_range`: they are the image of ∏_{w∣π} (1 − z_w).
* `New.Data.span_isShort_ramifiedSourceForms_eq_top`: the short ramified source forms span the
  ramified source forms.

Notions from other files:
* `New.Parameters`: The fixed parameters: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a
  prime `d` with `d ≡ q₀/2 - 1 mod q₀`.
* `New.weylGauge`: The gauge of ξ at g: the largest p-adic absolute value of a coordinate of
  g⁻¹·ι(ξ), with g⁻¹ acting in weight (κ, e).
* `New.weylNormSq`: The squared norm ξ* G ξ for the integer Gram matrix G = `New.weylGram`.
* `New.Data.chosenLevel`: The principal congruence subgroup of level `New.Data.piM`, whose prime
  divisors are the chosen places.

## Role in the proof

The exponents are used in `New.UpperBound.Divisibility.LocalDivisibility`, the short forms in
`New.Reduction.ShortAndEnough` and `New.Determinant.AuxiliaryForms.SpanningForms`.



## Prime-by-prime measures of the divisibility asked of the lifted map

The infinite places of E form the group (ℤ/q₁)^×, where q₁ = `New.Data.q₁` is a multiple of q₀. The
a-places (`New.Data.aPlaces`) are the places whose class is 1 modulo q₀; the b-places
(`New.Data.bPlaces`) are a set of places of class −1 modulo q₀, part of the data. The numbers m (of
lifts), k, x, x₁, b and the long order a = xb (`New.Data.a`) are those of `New.Data`.

* `New.Data.IsSmallNonsplit`, `New.Data.IsPlusMinusOneModLifts`, `New.Data.IsExceptional`: the
  classes of primes in the local proof; `New.Data.ceilLogLifts`: the base-p logarithm of m, rounded
  up.


### `localPrimeSum`

 The prime sum s_p(y, σ) = v(π_p) ∑_{e ∈ I_p} (y/p^e − w(u(−p^e) σ))⁺. Here v(π_p) is
`New.piPrimeValuation` (1/2 if p = d, and 1 otherwise), I_p is `New.positivePartnerExponents` (the
odd numbers if p is inert, all e ≥ 1 if p = d, none if p splits), and w is `New.Data.weight` (b on
the set `New.Data.bPlaces`, a/x₁ elsewhere). The infinite places form the group (ℤ/q₁)^×, with
q₁ = `New.Data.q₁`; u(ν) = `New.Data.placeOfInt` ν is the place given by the class of ν if ν is
prime to q₁, and the identity place otherwise. 

### `localPrimeSumTotal`

 The total F(p) = ∑_σ s_p(w(σ), σ) of the prime sums s_p = `New.Data.localPrimeSum` p over the
infinite places σ, with w = `New.Data.weight`. 

### `gain`

 The divisibility asked of the chain of m lifts at p: gain(p) = m(∑_τ s_p(a, τ) + k F(p)). The
sum runs over the a-places τ (`New.Data.aPlaces`, the infinite places of class 1 modulo q₀), s_p is
`New.Data.localPrimeSum` p and F(p) is `New.Data.localPrimeSumTotal` p. 

### `IsSmallNonsplit`

 The natural number p satisfies p < x₁ and χ_K(p) ≠ 1; for prime p, this says that p is below
x₁ and inert or ramified in the quadratic field of the character χ_K = `New.chiK`. 

### `IsPlusMinusOneModLifts`

 The number m of lifts divides p − 1 (truncated at 0) or p + 1; for a prime p, this says
p ≡ ±1 modulo m. 

### `loss`

 The unit of the allowed losses at a non-split p < x₁: f a (log b)²/p, times m if p ≡ ±1 modulo
m. 

### `ceilLogLifts`

 The least natural number 𝔯 with m ≤ p^𝔯 (for p > 1). 

### `transferExponent`

 The natural number ν_p = 𝔯f(n_m + 𝔯), with 𝔯 = `New.Data.ceilLogLifts` p and f the number of
infinite places of E. Here n_j = k + j(t + 1) (`New.Data.n`) is the rank of the space X_j of stage
j, and m is the number of lifts. 

### `collisionExponent`

 The natural number j_p = ⌈2mfa/p⌉, with f the number of infinite places of E. 

### `o₀`

 The order o₀ in (ℤ/q₀)^× of the class of the infinite place named by −p
(`New.Data.placeOfInt`). The places form the group (ℤ/q₁)^×, where q₁ = q₀ · `New.towerDeg` s and
s = `D.towerExp`, and `New.Parameters.placeClass` reduces modulo the divisor q₀ of q₁. For p prime
to q₀, o₀ is the order of −p in (ℤ/q₀)^×. 

### `IsExceptional`

 p is exceptional if χ_K(p) = −1, p is not ±1 modulo the number m of lifts, and the order
o₀ = `New.Data.o₀` p is odd and at most 𝔯 = `New.Data.ceilLogLifts` p. Then, for e = o₀, the
infinite place named by −p^e is an a-place. 

### `IsCollision`

 A collision outside ev: e lies in I_p = `New.positivePartnerExponents`, and both τ and its
product with the place named by −p^e are a-places not in ev. 

### `collisionSum`

 The sum of a/p^e over all pairs (τ, e) that are collisions outside ev
(`New.Data.IsCollision`). 


## Short forms and the ramified source forms

* `New.Data.finrank_ker_ramifyingOp_le`: the kernel of ∏_{w∈s} (1 − z_w) has dimension at most
  #s/(N − 1) times the dimension of the source forms.
* `New.Data.isShort_ramifyingOp`: ∏_{w∈s} (1 − z_w) keeps integrality and at most multiplies the
  squared-norm bound by 4^#s.


 ### Short forms 

### `IsShort`

 A form φ is B-short if each value φ(g) is integral for Weyl's lattice at g at every p-adic
embedding, and all conjugates of φ(g) under Aut(ℂ) have squared norm at most B. 

### `IsShort.sub_translate`

 Let G_f = `Gf E n` be the unitary group of the form ∑ xᵢx̄ᵢ over the finite adeles of the CM
field E, and φ an algebraic form on G_f of weight (κ, e): at the infinite place τ the Young diagram
has κ τ h columns of height h, and e τ is the power of the determinant. Let φ be B-short, and let
k ∈ G_f have integral entries (`New.stdLevel`). Then φ minus its right translate by k is
4B-short. 

### `norm_weylEval_le_one_of_integral`

 Let y be an array over ℂ_p with entries of absolute value at most 1. The evaluation vector
`New.weylEval` at y has norm at most 1: its coordinates are the values at y of the products of
minors `New.nablaBasis`, which are polynomials with integer coefficients. 

### `weylRep_mul_weylRep_zero`

 The product of the actions of `G` in weight (κ, e) and of `Z` in weight (κ, 0) is the product
of the powers `(det G_τ) ^ e_τ` times the Schur matrix of `G Z`. The Schur matrix `schur κ z` is the
map that a family `z` of matrices induces on the Weyl module of the diagram with `κ τ h` columns
of height `h` at `τ`. 

### `norm_weylRep_mulVec_det_smul_weylEval_le_one`

 Let g lie in G_f = `Gf E n`, the unitary group of rank n over the finite adeles of the CM field
E. A family h of invertible matrices h_τ, indexed by the infinite places τ, acts in weight (κ, e)
(`New.weylRep`) by ∏_τ det(h_τ)^(e_τ) times its action on the Weyl module whose Young diagram at τ
has κ τ h columns of height h.

Let Y₀ and Y_τ be invertible matrices over E such that g⁻¹Y₀ and each g^(−e_τ)Y_τ are integral
(entries in Ô), and let the entries of y be integral elements of ℂ_p. Act on the evaluation vector
at y by Y₀ in weight (κ, 0), multiply by ∏_τ det Y_τ, and act by g⁻¹ in weight (κ, e): the result
has coordinates of absolute value at most 1. Here E goes to ℂ_p by `New.weightEmbedding` at τ, for
the chosen embedding ιₚ of ℂ, and its finite adeles by the extension `New.adeleExtension` of that
map. 

### `weylNormSq_det_smul_weylRep_mulVec_weylEval_le`

 Consider the Weyl module whose Young diagram at the infinite place τ of E has κ τ h columns of
height h. A family Y₀ of invertible matrices indexed by the infinite places acts on it by
`New.weylRep` κ 0 Y₀.

Let R be at least the rank n, let the complex matrices of the families Y₀ and Y have entries of
absolute value at most R, and let y have entries of absolute value at most 1. Let M be at least n·f
plus the number of boxes of κ in columns of height below n (`New.boxes`), where f is the number of
infinite places, and let R^(6M) ≤ B. Then ∏_τ det Y_τ times the image under Y₀ of the evaluation
vector at y has squared norm at most B. 

### `isShort_deltaForm`

 Let K be a level of the finite adelic unitary group G_f that is free: Γ ∩ gKg⁻¹ is trivial for
every g, where Γ is the group of rational points. Let x be in G_f and let v be a coordinate vector
of weight (κ, e). Suppose that for every prime p and every embedding ι of ℂ in ℂ_p the coordinates
of x⁻¹·ι(v) have absolute value at most 1 (`New.weylGauge`), and that every conjugate of v under
Aut(ℂ) has squared norm at most B (`New.weylNormSq`). Then the delta form at x made from v is
B-short (`New.IsShort`): its values are integral at every p-adic embedding and their conjugates have
squared norm at most B. The delta form is supported on ΓxK, and its value at y is the sum of γ⁻¹·v
over the rational γ with x⁻¹γy ∈ K. 

### `span_isShort_eq_top`

 Consider algebraic forms on the finite adelic unitary group G_f of rank n over E, of weight (κ,
e): at the infinite place τ the Young diagram has κ τ h columns of height h, and e τ is the power of
the determinant. Let K be a level that is free: Γ ∩ gKg⁻¹ is trivial for every g, where Γ is the
group of rational points. Let N ≠ 0 be a natural number in the different of E, f the number of
infinite places, and M at least n·f plus the number of boxes of κ in columns of height below n. If
B ≥ C^(6M), where C = 6N(fn)² is `New.Space.shortBasisConst` E n N, the forms fixed by K are spanned
by the B-short ones. 

### `algFormCentralRep`

 The representation of the norm-one finite adeles, acting by translation by scalar matrices,
on algebraic forms of weight (κ, e) on which J acts through χ. 

### `coe_algFormCentralRep_apply`

 For `φ` in the level space of `algFormRep κ e` for `J` and `χ`, the form underlying
`algFormCentralRep z φ` is `φ` right-translated by the scalar matrix `scalarFin n z` under
`algFormRep κ e`. 

### `sum_pow_apply_eq_zero_iff_exists_eq_sub`

 Let `T` be an endomorphism of a complex vector space with `T ^ r = 1`, where `r ≠ 0`. The
vectors `T ^ i φ`, `0 ≤ i < r`, have sum `0` if and only if `φ = ψ - T ψ` for some vector `ψ`. 

### `iInf_ker_sum_pow_eq_range`

 Let `π` be a complex representation of a commutative group and `z w` a finite family of
elements with `π (z w) ^ r = 1`, where `r ≠ 0`. The vectors whose translates by `z w ^ i`,
`0 ≤ i < r`, have sum `0` for each `w` are the image of the product of the operators `1 - z w`. 

### `relIndex_mul_finrank_levelSpace`

 For levels `K' ≤ K` such that `classAut stdRatPoints K g` and `classAut stdRatPoints K' g` are
trivial for every `g`, the dimension of `levelSpace (algFormRep κ e) K'` is `[K : K']` times the
dimension of `levelSpace (algFormRep κ e) K`. 

### `span_setOf_mem_eq_top_of_eq_range`

 If a set `S` spans a vector space and an endomorphism `f` with image `W` maps `S` into `T`,
then the elements of `W` that lie in `T` span `W`. 

 ### The levels and the scaling generators at the primes dividing `D.piN` 

### `not_isChosen_of_N_mem`

 Neither a place `w` above the prime `D.N` nor its conjugate is a chosen place
(`New.Data.IsChosen`), as the chosen places lie above the smaller primes `D.levelPrime i`. 

### `mem_levelX`

 Let `D` be admissible data, with CM field `E = D.E` and integer `π = D.piN` of `E` with `π π̄`
prime. The chain of theta lifts passes through hermitian spaces `X_j` of rank `D.n j`, with basis
indexed by `D.X j` and last index `Sum.inr ()`. An element `k` of the finite adelic unitary group
`Gf D.E (D.X j)` of `X_j` lies in the level `D.levelX j` if and only if it lies in `D.chosenLevel`
and, at every prime `w` dividing `π`, the last row of `k_w - 1` vanishes modulo `w`. Here
`k_w = k.atPlace w` is the component of `k` at `w`, and `v` is the valuation of the completion
`E_w`, which gives a uniformizer the value `exp (-1)`. 

### `inf_supportedOn_le_chosenLevel`

 Let `S` be a set of places above `N`, and take the finite adelic unitary group of the space
`X_j` of stage `j`. An integral element (`stdLevel`) with component `1` off `S` and its conjugates
lies in the principal congruence subgroup `D.chosenLevel`. 

### `IsScalingAt`

 The scalings at a prime `w` dividing `π = D.piN`: the integral ideles of norm one that are `1`
off `w` and its conjugate. 

### `exists_isScalingAt_valuation_pow_iff`

 Let `D` be admissible data, with CM field `E = D.E`, prime `N = D.N` and integer `π = D.piN` of
`E` with `π π̄ = N`. Let `w` be a prime of `E` dividing `π`; its residue field has `N` elements.
There is a scaling `z` at `w` whose component `z_w` generates the units of the residue field:
`z_w ^ i` is congruent to `1` modulo `w` if and only if `N - 1` divides `i`. 

### `scalingGenerator`

 A chosen scaling `z_w` at a prime `w` dividing `π`: it is integral, it is `1` off `w` and its
conjugate, and its component at `w` has order `N - 1` modulo `w`, so it reduces to a generator of
the units of the residue field. 

### `valuation_scalingGenerator_pow_sub_one_lt_one_iff`

 The `i`-th power of the component at `w` of the chosen scaling `z_w = D.scalingGenerator w` is
congruent to `1` modulo `w` if and only if `N - 1` divides `i`. 

### `scalarFin_mem_maxCompactAt_of_isScalingAt`

 The scalar matrix of a scaling `z` at `w` (integral, and `1` off `w` and its conjugate) lies in
the maximal compact subgroup at `w`. 

### `scalarFin_scalingGenerator_mem_maxCompactAt`

 The scalar matrix of the chosen scaling `z_w = D.scalingGenerator w` lies in the maximal compact
subgroup at `w`. 

### `scalarFin_scalingGenerator_mem_chosenLevel`

 The scalar matrix, of size `D.X j`, of the chosen scaling `z_w = D.scalingGenerator w` lies in
the principal congruence subgroup `D.chosenLevel`. 

### `scalarFin_scalingGenerator_pow_mem_levelX_iff`

 Let `D` be admissible data (`New.Data`), with CM field `E = D.E`, prime `N = D.N` and integer
`π = D.piN` of `E` with `π π̄ = N`, and let `w` be a prime dividing `π`. The chosen scaling
`z_w = D.scalingGenerator w` is an integral finite idele with `z_w z̄_w = 1` that is `1` off `w` and
its conjugate and has order `N - 1` modulo `w`; `scalarFin (D.X j) z_w` is its scalar matrix with
rows indexed by `D.X j`. The `i`-th power of this matrix lies in the level `D.levelX j` if and only
if `N - 1` divides `i`. 

 ### Ramified source forms 

### `centralRep`

 The representation of the norm-one finite adeles U(1)(𝔸_f) on source forms, by right translation
by scalar matrices. 

### `coe_centralRep_apply`

 On the underlying forms, `z` acts by right translation by its scalar matrix. 

### `algFormCentralRep_scalingGenerator_pow`

 Let `D` be admissible data for the parameters `P`, with CM field `E = D.E`, prime `N = D.N` and
integer `π = D.piN` of `E` with `π π̄ = N`, and let `w` be a prime dividing `π`. The finite adelic
unitary group of `X_j` acts by right translation (`algFormRep`) on the algebraic forms whose weight
at each infinite place `τ` has `D.columnCount τ h` columns of height `h` and last entry
`D.lastEntry j τ`; `levelSpace` is the subspace fixed by the level `D.levelX j`. On it a finite
idele `z` with `z z̄ = 1` acts by translation by its scalar matrix (`algFormCentralRep`). For
`z = D.scalingGenerator w`, which is `1` off `w` and its conjugate and has order `N - 1` modulo `w`,
the `(N - 1)`-th power of this operator is the identity. 

### `ramifiedSourceForms`

 The ramified source forms: those for which, at each `w ∣ π`, the translates by the powers
`z_w ^ i`, `0 ≤ i < N - 1`, of the chosen scaling `z_w = D.scalingGenerator w` have sum `0`. 

### `ramifyingOp`

 The product over `w ∈ s` of the operators `1 - z_w` on source forms, where
`z_w = D.scalingGenerator w` acts through `D.centralRep`. 

### `ramifiedSourceForms_eq_range`

 For admissible data `D`, let `π = D.piN` be the integer of `E` with `π π̄ = N`, the prime `D.N`.
For each prime `w` dividing `π` the chosen scaling `z_w = D.scalingGenerator w` acts on source forms
by right translation by its scalar matrix. The ramified source forms, those whose translates by
`z_w ^ i`, `0 ≤ i < N - 1`, have sum `0` for each `w`, are the image of `D.ramifyingOp univ`, the
product of the operators `1 - z_w` over all `w` dividing `π`. 

### `sum_scalingGenerator_pow_eq_zero_iff_exists_eq_sub`

 Let `D` be admissible data for the parameters `P`, with CM field `E = D.E`, prime `N = D.N` and
integer `π = D.piN` of `E` with `π π̄ = N`, and let `w` be a prime dividing `π`. The finite adelic
unitary group of `X_j` acts by right translation (`algFormRep`) on the algebraic forms whose weight
at each infinite place `τ` has `D.columnCount τ h` columns of height `h` and last entry
`D.lastEntry j τ`. Let `φ` lie in the subspace (`levelSpace`) fixed by the level `D.levelX j`. The
finite idele `z_w = D.scalingGenerator w` is `1` off `w` and its conjugate, has order `N - 1` modulo
`w`, and acts through its scalar matrix (`scalarFin`). The translates of `φ` by `z_w ^ i`,
`0 ≤ i < N - 1`, have sum `0` if and only if `φ = ψ - z_w ψ` for a form `ψ` of the same weight and
level. 

### `exists_eq_sub_scalingGenerator`

 For admissible data `D`, let `π = D.piN` be the integer of `E` with `π π̄ = N`, the prime `D.N`.
The source forms `D.SourceForm` are the algebraic forms on the unitary group of `X_0`, of the weight
of `X_0`, fixed by the level `D.levelX 0`. For a prime `u` dividing `π` the chosen scaling
`z_u = D.scalingGenerator u` acts on them by right translation by its scalar matrix. Let `φ` be a
ramified source form: for each `u` its translates by `z_u ^ i`, `0 ≤ i < N - 1`, have sum `0`. Then
for each prime `w` dividing `π` there is a source form `ψ` with `φ = ψ - z_w ψ`. 

### `sum_height_mul_columnCount_le`

 At each infinite place `τ`, the sum over heights `h` below the rank of `X_0` of
`h * D.columnCount τ h` is at most `a = D.a`. Here `D.columnCount τ h` counts the columns of height
`h` in the Young diagram of the weight of `D`. So that diagram has at most `a` boxes in those
columns. 

### `N_sub_one_le_relIndex_levelX`

 If a level `K` contains the scalar matrix of the chosen scaling `z_w = D.scalingGenerator w`,
then the index in `K` of its intersection with the level `D.levelX 0` is at least `N - 1`. 

### `coe_mem_levelSpace_sup_zpowers`

 For admissible data `D`, a source form `φ` fixed by the norm-one finite idele `z` under
`D.centralRep` is fixed by right translation by the group generated by `D.levelX 0` and the scalar
matrix `scalarFin (D.X 0) z`. 

### `finrank_ker_one_sub_scalingGenerator_le`

 For admissible data `D`, let `w` be a prime of `E` dividing `π = D.piN`, where `π π̄ = N` is the
prime `D.N`. The chosen scaling `z_w = D.scalingGenerator w` acts on the space `D.SourceForm` of
source forms through `D.centralRep`, by right translation by its scalar matrix. The source forms
fixed by `z_w` form a subspace of dimension at most `1 / (N - 1)` times the dimension of all source
forms. 

### `_root_.New.finrank_ker_mul_le`

 The kernel of a product of two endomorphisms of a finite-dimensional space has dimension at most
the sum of the dimensions of the two kernels. 

### `ramifyingOp_cons`

 Adding a prime `w ∉ s` to `s` multiplies `D.ramifyingOp s` on the left by `1 - z_w`, where
`z_w = D.scalingGenerator w` acts on source forms through `D.centralRep`. 

### `finrank_ker_ramifyingOp_le`

 For admissible data `D`, let `s` be a finite set of primes of `E` dividing `π = D.piN`, where
`π π̄ = N` is the prime `D.N`. For `w ∈ s` the chosen scaling `z_w = D.scalingGenerator w` acts on
the space `D.SourceForm` of source forms by right translation by its scalar matrix. The kernel of
`D.ramifyingOp s`, the product of the operators `1 - z_w` over `w ∈ s`, has dimension at most
`#s / (N - 1)` times the dimension of all source forms. 

### `le_finrank_ramifiedSourceForms`

 The ramified source forms have dimension at least `1 - f / (N - 1)` times the dimension of all
source forms, where `f` is the number of infinite places of `E`. 

### `f_div_N_sub_one_le`

 The proportion `f / (N - 1)` is at most `b⁻⁸`, because `f ≤ b` and `b⁹ + 1 ≤ N`. 

### `isShort_ramifyingOp`

 If the source form `φ` is `B`-short, then `D.ramifyingOp s φ`, its image under the product of
the operators `1 - z_w` over `w ∈ s`, with `z_w = D.scalingGenerator w` acting by its scalar matrix,
is `4 ^ #s * B`-short. 

### `span_isShort_eq_top`

 For admissible data `D` (`New.Data`), let `f = D.f` be the number of infinite places of the
field `D.E`, let `x` and `b` be the scales of `D` and `a = x b`, so that
`D.errorUnit = f a (log b)³`. The source forms are spanned by those that are `B`-short for
`B = exp D.errorUnit / 4 ^ f`: their values are `p`-adically integral for every `p`, and all
conjugates of the values have squared norm at most `B`. 

### `span_isShort_ramifiedSourceForms_eq_top`

 The ramified source forms `D.ramifiedSourceForms` are spanned by those that are `B`-short for
`B = exp D.errorUnit`: their values are `p`-adically integral for every `p`, and all conjugates of
the values have squared norm at most `B`. 
