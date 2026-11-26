---
{
  "module": "src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Galois conjugates of jets of theta functions and archimedean bounds for jets

An automorphism `σ` of `ℂ` over `K = ℚ(√-d)` acts on the jets of theta functions. This action is
realized as a `σ`-semilinear map `L` on `𝒮 V`, whose laws hold on `V.finitePart`. We then prove
archimedean bounds for the conjugates of the jets of admissible combinations of the operators
`New.Space.finHeisenbergOp` applied to the integral vacuum, moved by finite points of a pair of
groups.

## Main definitions and results

* `New.Parameters.exists_isJetConjugation`: existence of `L`;
  `New.Parameters.IsJetConjugation.exists_map_schrodingerOp`: its action on the vacuum `vacElem` and
  on the data `Ψ ⊗ vacElem` for Schwartz–Bruhat functions `Ψ`;
  `New.Parameters.IsJetConjugation.norm_map_intVacuum_le`: a bound, with constant `P.constantBound`,
  for the images of the translates of `ω g (intVacuum V)`; it rests on
  `New.Parameters.norm_omega_vac_le`.
* `New.Parameters.norm_jet_le_of_isVacuumCombination` and
  `New.Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination`: archimedean bounds for the
  conjugates by `σ ∈ Aut ℂ` of the jets, and for their Schur matrices;
  `New.Parameters.isVacuumCombination_of_isAdmissibleCombination` makes them apply to admissible
  combinations.

Notions from other files:
* `New.Parameters.E`: The field `P.E s = K(ζ)`, for a primitive root of unity `ζ` of order
  `P.q₁ s`; `P.Φ s` is the set of its infinite places, a group isomorphic to `Gal(E/K)`.
* `New.Parameters.jetScale`: A nonzero complex number, the period factor times the area scale over
  the period `Ω₀`, at which Taylor series of theta functions are scaled.
* `New.Parameters.bigOmega`: The real number Ω = exp(γ − Re L′/L(1, χ_K))·2π/rd_E, with γ Euler's
  constant and rd_E the root discriminant of E.
* `New.Parameters.intVacuum`: The vacuum of rank n multiplied by the n-th power of a fixed number
  that makes its values at finite vectors integral.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: For a space V of rank n, a Banach space of integrable functions on 𝔸^n on which the
  Heisenberg and Weil representations act. Applied to an adelic vector, `f : 𝒮 V` gives the value
  of its theta function.

## Relation to the literature

Related work: Bannai–Kobayashi, Algebraic theta functions and the p-adic interpolation of
Eisenstein–Kronecker numbers, 2010; Kings–Sprang, Eisenstein–Kronecker classes and integrality of
critical values, 2019; Katz, p-adic L-functions for CM fields, 1978.

The Galois action on theta functions with complex multiplication and on the finite Weil
representation is known; see `Lib.Weil.DualPair.KernelLaws` for sources.



## Galois conjugation of jets as a semilinear map

`New.Space.IsJetConjugate σ π t t' f f'` says that `σ` applied to the Taylor series of `f` at scale
`t` is that of `f'` at scale `t'`, with places renamed by `π⁻¹`. `New.Space.finitePart` is spanned
by the finite Heisenberg translates of the vacuum `vacElem`. `V.ϱ` and `V.ω` are the Heisenberg and
Weil representations, and `finVec x` is the adelic vector with finite part `α x` and zero
archimedean part, for the idele `α` of the Weil data.


### `New.Parameters.IsJetConjugation`

 `L` conjugates jets by `σ`, an automorphism of `ℂ` over `K`, at a scale `t` with `|t|² = 1/Ω`:
it is a `σ`-semilinear map on `𝒮 V` that on the finite part scales finite translations by the
finite adele `b`, `σ` acts on the character `selfDualAddChar` as multiplication by `b b̄` does, and
for `f` in the finite part the jets of `L f` at the scale `t` are the conjugates of the jets of `f`.
Here `V` is a space over `E P s = K(ζ)`, with `ζ` a root of unity of order `P.q₁ s`; `𝒮 V` is the
Banach space of functions on adelic vectors on which the Heisenberg and Weil representations act;
and `placePerm s σ` is the permutation of the infinite places of `E P s` induced by `σ`.
The law for the Weil operators is `New.Space.ScalesTranslations.map_omega`. 

### `New.Parameters.IsJetConjugation.norm_scale_sq`

 The scale `t` has `|t|² = 1/Ω`. 

### `New.Parameters.IsJetConjugation.scalesTranslations`

 `L` keeps `V.finitePart` and turns the translation by a finite `x` into that by `b x` there,
  and `σ (selfDualAddChar z) = selfDualAddChar (b b̄ z)`. 

### `New.Parameters.IsJetConjugation.isJetConjugate`

 For `f ∈ V.finitePart`, the jets of `L f` at scale `t` are the conjugates by `σ` of the
  jets of `f` at scale `P.jetScale s`. 

### `New.Space.map_selfDualAddChar_of_isJetConjugate`

 The Galois law of the additive character `selfDualAddChar` of the finite adeles, from the
standard space `V = stdSpace E Unit` of rank one. The translate of `F` by a finite adele `x` is
`V.ϱ (finVec x) F`.

Let `F` and `F'` lie in `V.finitePart`, with `F ≠ 0` and `t ≠ 0`. Suppose that for all `x` the ring
homomorphism `σ` takes the jets at scale `t` of the translate of `F` by `x` to the jets at scale
`t'` of the translate of `F'` by `b • x`, up to the permutation `e` of the infinite places. Then `σ`
takes `selfDualAddChar z` to `selfDualAddChar (b * star b * z)`. 

### `New.Parameters.exists_isJetConjugation`

 Galois conjugates of jets. Let `V` be a hermitian space over `E P s` that is standard: its signs
`ε` at the infinite places are `+1` and its point, an adelic basis that diagonalizes the form, is
the identity matrix.

Let `σ` be an automorphism of `ℂ` over `K`. Then there are a scale `t`, a finite adele `b` and a
`σ`-semilinear map `L` with the laws of `New.Parameters.IsJetConjugation`. First, `|t|² = 1/Ω` for
`Ω = P.bigOmega s = exp (γ - Re L'/L(1, χ_K)) * 2π / rd_E`, with `γ` Euler's constant, `χ_K` the
quadratic character of `K` and `rd_E` the root discriminant of `E`. Next, `L` keeps the span
`V.finitePart` of the finite translates of the vacuum; there it takes translation by `x` to
translation by `b x`, and the jets of `L f` at scale `t` are the `σ`-conjugates of those of `f` at
scale `P.jetScale s`. Finally `σ (selfDualAddChar z) = selfDualAddChar (b b̄ z)`. 

### `New.Parameters.norm_multiplierRatio`

 For an automorphism `σ` of `ℂ` over `K` and a finite unitary matrix `g`, the number
`multiplierRatio σ g = σ (Δ g) / Δ g` has modulus `1`. Here `Δ = New.finMultiplier` is the finite
part of the multiplier of the Weil representation. 

### `eq_zero_of_map_eq_zero`

 On a standard space `V` (all signs `+1`, the point the identity matrix), a map `L` that
conjugates jets is injective on `V.finitePart`, the span of the finite translates of the vacuum. 

### `map_apply_finVec`

 Let `V` be a hermitian space over `E P s`, a cyclotomic extension of `K P = ℚ(√-d)`, and let
`𝒮 V` be the Banach space of functions on adelic vectors on which the Heisenberg group acts. Let the
`σ`-semilinear map `L` on `𝒮 V` conjugate jets by the automorphism `σ` of `ℂ` over `K P` at the
scale `t`, scaling finite translations by the finite adele `b`. Let `f` lie in `V.finitePart`, the
span of the finite Heisenberg translates of the vacuum. Then `σ` takes the value of the theta
function of `f` at `finVec x` to that of `L f` at `finVec (b • x)`. Here `finVec x` is the adelic
vector with archimedean part zero and finite part `α x`, for the idele `α` of the Weil data. 

### `exists_map_schrodingerOp`

 Let `V` be a standard hermitian space over `E P s`, a cyclotomic extension of `K P = ℚ(√-d)`.
Let the `σ`-semilinear map `L` conjugate jets on the space `𝒮 V` of the Weil representation `V.ω`,
and let `R` be a set of finite places (`FinPlace`) of `E P s` disjoint from its complex conjugate.
There are a number `c ≠ 0` and a finite adele `u` with `u ū = 1` such that
`L vacElem = c ω(u) vacElem` and `L (Ψ ⊗ vacElem) = c ω(u) ((σ ∘ Ψ) ⊗ vacElem)` for all `Ψ`
Schwartz–Bruhat above `R`. Here `ω(u)` is `V.ω` at the point with archimedean part `1` and finite
part the scalar matrix `scalarFin n u`, `vacElem` is the vacuum, and `Ψ ⊗` is `V.schrodingerOp R Ψ`,
the combination of finite translations attached to `Ψ`. 


### Bounds for the values of the vacuum and of its conjugates

These bounds are uniform in the lattice. They enter Cauchy's estimate for the jets below.


### `New.Parameters.norm_vacuumFn_vecAtPoint_le`

 At `W.vecAtPoint γ`, the coordinates of a rational vector `γ` at the point of a definite space,
the vacuum function `vacuumFn` (a Gaussian times a phase supported on a lattice) is bounded by
`exp (-π ‖γ‖² / √d)`. Here `‖γ‖ = ‖W.archCoords γ‖` is the length of the archimedean
coordinates. 

### `New.Parameters.exists_intCast_eq_norm_archCoords_sq`

 Let `W` be a definite hermitian space over `E` (all signs `+1`), given by a matrix `J` over `E`
and a point `x ∈ GL_n(𝔸)` with `xᴴ J x = 1`. For `γ ∈ E^n`, `W.vecAtPoint γ = x⁻¹ γ`, and
`W.archCoords γ` is the vector of its components at all infinite places, in a Euclidean space.
Suppose that the finite parts of the coordinates of `x⁻¹ γ`, divided by the idele `α`, lie in the
ring `Ô` of finite adeles integral at every finite place. Then the squared length of
`W.archCoords γ` is an integer. Here `α = P.α s` is the inverse of a generator of the different of
`E / K` at the places dividing `(1 + √-d) / 2`, and `1` at the other finite places. 

### `New.Parameters.one_le_norm_archCoords_sub`

 Let `W` be a definite hermitian space (all signs `+1`) over `E = P.E s`, a cyclotomic extension
of `ℚ(√-d)`, given by a matrix `J` over `E` and a point `x ∈ GL_n(𝔸)` with `xᴴ J x = 1`. Let
`γ ≠ δ`, and let the finite parts of the coordinates of `x⁻¹ γ` and `x⁻¹ δ` become integral (lie in
`Ô`) after division by the idele `α` of the Weil data. Then `W.archCoords γ` and `W.archCoords δ`
have distance at least `1`. 

### `New.exp_neg_pi_div_mul_sq_le`

 Completing the square: `t D ≤ π t² / a + a D²` for `a > 0`, in exponential form. 

### `New.sqrt_mul_sq_add_le_of_le`

 If `δ ≤ 2 M`, then `√d (δ + 1)² + 3 δ ≤ 2 (2 d + 6) (M + 1)²`: the comparison of exponents in
`New.Parameters.norm_omega_vac_le`. 

### `New.Parameters.norm_omega_vac_le`

 In a definite space, given by a hermitian matrix and a point, the values of the vacuum moved
by the Weil operator `ω g` are bounded by `exp ((2 d + 6) (q₁ n + 1)²)`, uniformly in `g` and
in the argument. Here `n` is the rank, `g` is a point of the adelic unitary group for the signs
`+1`, `K = ℚ(√-d)`, and `q₁ = P.q₁ s` is the order of the root of unity that generates `P.E s`
over `K`. 

### `norm_map_intVacuum_le`

 Let `V` be a standard space of rank `n` (all signs `+1`, the point the identity matrix), and
let the `σ`-semilinear map `L` conjugate jets by `σ` at the scale `t`, scaling finite translations
by `b`. Then every value of `L ϱ(x) ω(g) (intVacuum V)`, for finite `x` and `g`, has norm at most
`exp (c (q₁ n + 1)²)`. Here `intVacuum V` is the integral multiple of the vacuum and `q₁ = P.q₁ s`
is the order of the root of unity that generates `E P s` over `K = ℚ(√-d)`. The real number
`c = P.constantBound` depends only on `P`: it is the sum of `P.vacuumBoundConst` (the constant in
the bound for the conjugates of the values of the integral vacuum), `2 d + 6` and a nonnegative
term. 


## Archimedean bounds for jets

`New.Space.jetSeries V c f` is the Taylor series of the theta function of `f` at scale `c`.
`New.jet ℂ Q` applies the differential operator `Q(∂)` at `0`.


### `FitsRanks.sum_diagramWeight_eq_boxes`

 Let `κ τ h` count the columns of height `h` at the place `τ`. If `κ` fits the ranks `card n` and
`card n'` (`New.FitsRanks`: no column has height strictly between them), then the row lengths
`diagramWeight` of the diagram formed by the columns of height below `card n'`, summed over all
places and the first `card n` rows, add up to the number of boxes of that diagram. 

### `HasConjugateGrowth`

 `HasConjugateGrowth σ Q T L w A` says that the values of `Q`, conjugated by `σ`, grow at most
exponentially: `‖σ Q(z)‖ ≤ A * exp (w + L R)` whenever `∑ ‖σ z_i‖ ^ 2 ≤ T (2 L + 2) R`. For an
automorphism `σ`, `Q` homogeneous of degree `L`, `T > 0` and `A ≥ 0` it says that `A * exp w` bounds
`T ^ (L / 2) * ‖(σ Q)(y)‖ * exp (-L |y|² / (2 L + 2))` for all `y`: put `σ z = √T y`. 

### `integral_exp_neg_inv_mul_normalizedVolume`

 Against `normalizedVolume ι`, which is Lebesgue measure on `ι → ℂ` divided by `π ^ card ι`, the
Gaussian `exp (-|y|² / a)` has integral `a ^ card ι`. 

### `norm_integral_normalizedVolume_le`

 A function on `ι → ℂ` bounded by `C * exp (-|y|² / a)` has integral of norm at most
`C * a ^ card ι` against `normalizedVolume ι`, for `a > 0`. This measure is Lebesgue measure
divided by `π ^ card ι`, so that `exp (-|y|²)` has integral `1`. 

### `norm_realVac`

 The vacuum `realVac y` has modulus `exp (-|y|² / 2)`. 

### `Parameters.jet_jetSeries_mul`

 A factor `c` in the scale of the Taylor series can be moved into the differential operator: the
jet along `Q` at scale `c * a` is the jet along `Q (c z)` at scale `a`. Here the jet `jet ℂ Q G` of
a power series `G` along a polynomial `Q` is `Q(∂) G` at `0`, and `V.jetSeries a F` is the Taylor
series at scale `a` of the theta function of `F`, a vector of the space `𝒮 V` on which the Weil
representation acts. 

### `Parameters.map_jet_eq_integral`

 Conjugates of jets as Gaussian integrals, on a space `V` whose signs `homSigns 1 1` are all
`+1`. Suppose that `σ` takes the Taylor series of `F` at scale `P.jetScale s` to that of `F'` at
scale `t`, up to the permutation `placePerm s σ` that `σ` induces on the infinite places `P.Φ s` of
`P.E s`. Then the conjugate of the jet of `F` along `Q` is the integral, for Lebesgue measure
divided by `π` in each complex coordinate, of the values of `F'` at `realVec y` against the vacuum
`realVac y = exp (-|y|² / 2)` and the polynomial `Q`, with conjugated coefficients and permuted
places, evaluated at `t ȳ`. 

### `Parameters.norm_jet_translate_le`

 Cauchy's estimate for the jets of one finite translate `ϱ(x) ω(g) (intVacuum V)` of the integral
vacuum `intVacuum V` of a standard space `V` (all signs `+1`, the point the identity matrix), at
scale `c * P.jetScale s`. If `0 ≤ A`, `‖σ c‖ ^ 2 / P.bigOmega s ≤ T`, and
`‖σ Q(z)‖ ≤ A * exp (w + L R)` whenever `∑ ‖σ z_i‖ ^ 2 ≤ T (2 L + 2) R`, then the conjugate by `σ`
of the jet along `Q` has norm at most `exp (P.constantBound * (P.q₁ s * card (n' × n) + 1) ^ 2 +
w) * (2 L + 2) ^ card (P.Φ s × n' × n)` times `A`. 

### `Parameters.IsVacuumCombination`

 `P.IsVacuumCombination V B f` says that `f = ∑ r x • V.finHeisenbergOp x (intVacuum V)` is a
finite combination of Heisenberg translates of the integral vacuum by finite adelic vectors `x`,
with `∑ ‖σ (r x)‖ ≤ B` for every field automorphism `σ` of `ℂ`. The operator
`V.finHeisenbergOp x` is `V.ϱ (finVec x)` times the root of unity `stdLattice.semichar x`. 

### `Parameters.isVacuumCombination_of_isAdmissibleCombination`

 An admissible combination `f = ∑ r x • V.finHeisenbergOp x (intVacuum V)` of size `B` is a
vacuum combination of size `B`. Admissible means that `r` has support in `A`, that each `d * r x` is
integral at the primes not dividing `q`, and, since the argument `True` turns this condition on,
that `∑ ‖σ (r x)‖ ≤ B` for every automorphism `σ` of `ℂ`. Only the last condition is kept. 

### `Parameters.isVacuumCombination_finHeisenbergOp`

 A single Heisenberg translate `V.finHeisenbergOp x (intVacuum V)` of the integral vacuum is a
vacuum combination with coefficient bound `1`. 

### `Parameters.jetSizeBound`

 The factor in the size bounds for the jets of a combination of translates of the integral vacuum
whose coefficients have total size `B`, for a growth rate `L` and an extra exponent `w`. It equals
`B * exp (P.constantBound * (P.q₁ s * card (n' × n) + 1) ^ 2) * exp w` times
`(2 L + 2) ^ card (P.Φ s × n' × n)`. 

### `Parameters.jetSizeBound_eq`

 The factor `P.jetSizeBound s n n' B L w` in closed form: it is `B * (exp (P.constantBound *
(P.q₁ s * card (n' × n) + 1) ^ 2 + w) * (2 * L + 2) ^ card (P.Φ s × n' × n))`. 

### `Parameters.norm_map_pairChar`

 Let `a` and `b` be automorphic characters of the norm-one adeles that have a weight: on points
`u` with integral finite part, `a u = ∏ u_v ^ ea v * ∏ ψ w (u mod w)`, over the infinite places `v`
and the finite places `w`, and the same for `b` with `eb` and `ψ'`. Then the conjugates over `P.K`
of the value `a(det h) b(det g)⁻¹` of `pairChar a b` at finite points `g` and `h` have norm one. 

### `Parameters.norm_jet_le_of_isVacuumCombination`

 Size of jets. Let `f = ∑ r x • (translate by x of the integral vacuum)` be a finite combination,
on the space of maps between the standard hermitian spaces of ranks `n` and `n'` over `P.E s`, with
`∑ ‖τ (r x)‖ ≤ B` for every automorphism `τ` of `ℂ`. Move it by the points `g` and `h` of the finite
adelic unitary groups under the Weil representation `pairWeil` of the dual pair, twisted by
automorphic characters `a` and `b`, and take the Taylor series of its theta function at scale
`c * P.jetScale s`. The jet along `Q` is `Q(∂)` of this series at `0`. If `0 ≤ A`,
`‖σ c‖ ^ 2 / P.bigOmega s ≤ T`, and `‖σ Q(z)‖ ≤ A * exp (w + L R)` whenever
`∑ ‖σ z_i‖ ^ 2 ≤ T (2 L + 2) R`, then the conjugate by `σ` of the jet has norm at most
`P.jetSizeBound s n n' B L w * A`. 

### `sqrt_prod_pow_le_exp`

 Let `L > 0`, `u` and `R` be real numbers, and let `(τ, i)` run over `Φ × I` for a finite type
`Φ` and a finite set `I` of natural numbers. If the nonnegative numbers `ρ τ i` have sum at most
`exp u * (2 L + 2) * R`, then for all exponents `l (τ, i) : ℕ` the square root of the monomial
`∏ ρ ^ l` is at most `exp (w + L R)`, where `2 w = ∑ (l / L + log l! + l * u)`. 

### `schurGrowthExponent`

 The exponent `∑ (l / L + log l! + l * u) / 2` in the growth bound for Schur matrices. Here
`κ τ h` counts the columns of height `h` at the place `τ`, and `l` runs over the lengths of the
first `card n` rows, at all places, of the diagram formed by the columns of height below
`card n'`. The bound `rankAt (fun _ ↦ n')` is `card n'` at every place, so the length of row `i` at
`τ`, a value of `diagramWeight`, is the sum of `κ τ h` over `i < h < card n'`. 

### `Parameters.hasConjugateGrowth_schurCoeffPoly`

 Growth of the matrix coefficients `z ↦ y ⬝ᵥ schur κ z *ᵥ ξ` of the Schur matrix of a lift weight
`κ`. If the conjugate by `σ` of the covector `y` has dual norm at most one for the Gram norm
`√(weylNormSq ·)`, the conjugated values are at most that norm of the conjugate of `ξ` times
`exp (w + L R)` whenever `∑ ‖σ z_i‖ ^ 2 ≤ exp u * (2 L + 2) * R`, where
`w = schurGrowthExponent n n' κ L u` is half the sum of `l / L + log l! + l * u` over the row
lengths `l`. Here `κ τ h` counts the columns of height `h` at the place `τ`, and
`IsLiftWeight n n' κ eb e` says that `card n < card n'`, that no column has height strictly between
these ranks, and that `e τ = eb τ + κ τ (card n)`. 

### `Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination`

 Size of Schur jets. Let `f = ∑ r x • (translate by x of the integral vacuum)` be a finite
combination with `∑ ‖τ (r x)‖ ≤ B` for every automorphism `τ` of `ℂ`. It lies in the space `𝒮` of
the Weil representation `pairWeil` of the dual pair of the standard hermitian spaces `stdSpace`
(form and point the identity matrix) of ranks `n` and `n'` over `E = P.E s`. This representation is
twisted by automorphic characters `a` and `b` of weights `ea`, `eb` (an exponent for each infinite
place) and tame parts `ψ`, `ψ'` (a character of each residue field). Move `f` by the points `g` and
`h` of the finite adelic unitary groups `Gf`, and let `F` be the Taylor series of its theta function
at scale `c * P.jetScale s`, where `P.jetScale s = P.periodFactor s * √(2π / √d) / Ω₀` is a nonzero
number and `Ω₀` is the period of `K = ℚ(√-d)`. Let `κ` be a lift weight and `t = ‖σ c‖ ^ 2 / Ω`,
where `Ω = P.bigOmega s = exp (γ - Re L'/L(1, χ_K)) * 2π / rd_E`, with `γ` Euler's constant, `χ_K`
the quadratic character of `K` and `rd_E` the root discriminant of `E`.

Let `schurJet κ F` be the matrix whose entries are `Q(∂) F` at `0`, for `Q` the polynomial entries
of the Schur matrix `schur κ z`. For every positive integer `L`, it multiplies the Gram norm
`√(weylNormSq ·)` of the conjugate of `ξ` by at most `P.jetSizeBound s n n' B L w`, where
`w = schurGrowthExponent n n' κ L (log t)` is half the sum of `l / L + log l! + l * log t` over the
row lengths `l`. This factor is `B * exp w` times `(2 L + 2) ^ card (P.Φ s × n' × n)` times a
constant that depends only on `P`, `s` and the ranks (`jetSizeBound_eq`). A lift weight
(`IsLiftWeight`) has `card n < card n'`, no column of height strictly between the ranks, and
determinant exponent `e τ = eb τ + κ τ (card n)`. 
