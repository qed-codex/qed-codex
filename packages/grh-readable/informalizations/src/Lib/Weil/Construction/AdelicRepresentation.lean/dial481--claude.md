---
{
  "module": "src/Lib/Weil/Construction/AdelicRepresentation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The adelic Weil representation on 𝒮(V) and its theta functional

The adelic Heisenberg datum β = `New.adelicHeisenberg E s` on `𝔸 ^ n`, with vacuum function e =
`New.vacuumFn`, splits into a real and a finite part. The data of the adelic Weil representation
(measure, multiplier Δ and action of the adelic unitary group `New.G E s`) are built as products of
the real and the finite data. For a hermitian space with a point `V` (`New.Space`), the space
`New.𝒮 V`, whose vectors are also called data, is the model `Model (adelicHeisenberg E s)`. It
carries the Heisenberg operators `New.Space.ϱ` (`ρ x` or `heisenbergOp x` on the model), the Weil
representation `New.Space.ω`, the inner product `New.Space.dataInner` (`⟨·, ·⟩`, conjugate linear on
the left) and the vacuum `New.Space.vacElem`. A theta functional is a bounded functional on the
model that is invariant under the rational vectors `New.Space.ratVectors` and normalised;
`New.Space.θ` is a definite choice of one. A vector `f : 𝒮 V` applied to `x` is its theta function
θ(ϱ(x) f), not the integrable function `f.1 x = ⟨ϱ(x) vac, f⟩`.

## Main definitions and results

* `New.adelicSum`: multiplication by the idele `New.WeilData.scaleIdele` identifies complex
  coordinates, indexed by pairs (infinite place, index), times finite adelic vectors with `𝔸 ^ n`.
  The bicharacter and `New.vacuumFn` become products of those of `New.Fock.realHeisenberg` and
  `New.stdLattice.finHeisenberg` (`New.Heisenberg.OrthogonalSum`). This scaling turns the adelic
  Gaussian into the standard one (`New.WeilData.conj_scaleIdele_mul`).
* `New.adelicAction`: the adelic unitary group `New.G` acts on `𝔸 ^ n` by matrices, keeping the
  bicharacter and the measure, and `Δ` satisfies the identity of `New.Heisenberg.MultiplierAction`
  with trivial cocycle.
* `New.Space.omega_rho`, `New.Space.dataInner_omega`, `New.Space.dataInner_vacElem_omega_vacElem`:
  `ω g` takes `ϱ x` to `ϱ (g x)`, keeps the inner product, and has overlap `(conj (Δ g))⁻¹` with the
  vacuum.
* `New.Space.exists_isThetaFunctional`, `New.Space.IsThetaFunctional.eq_smul`: a theta functional
  exists, and every invariant functional is a multiple of it.
* `New.Space.dataInner_eq_quotMean`, `New.Space.hasSum_dataInner`: the inner product as a mean of
  theta functions, and the product of two theta values as a sum of inner products.

Notions from other files:
* `New.adelicHeisenberg`: the Heisenberg datum on adelic n-space with bicharacter β(x,y)=ψ(½ȷ
  h(y,x)), h being the standard hermitian form of signs s and ȷ = −ȷ̄ the element `j` of the Weil
  data.
* `New.Heisenberg.OrthogonalSum`: an isomorphism W₁ × W₂ ≃ W along which the bicharacter and the
  vacuum function of W are the products of those of W₁ and W₂.
* `New.Heisenberg.MultiplierAction`: an action of a group on W that keeps β and the measure, with a
  multiplier Δ that satisfies the cocycle identity of the Weil representation.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places; `New.Space.vecAtPoint` sends
  y in E^n to the adelic vector x⁻¹y.
* `New.Heisenberg.IsVacuum.Model`: the space of integrable v with v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y),
  as a type.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.


 ## The adelic Heisenberg datum as sum of its real and finite parts 

### `WeilData.conj_scaleIdele_mul`

 At an infinite place `w`, the component κ_w of the idele κ = `scaleIdele E` satisfies
conj κ_w · κ_w · 2π Im(Φ_w ȷ) = 1, where `Φ w` is the embedding of the CM type at `w` and ȷ is the
element `j` of the Weil data. 

### `realSigns`

 The sign function on pairs (infinite place, coordinate) that returns the sign of the
coordinate, ignoring the place. 

### `adelicSum`

 The isomorphism (y,z) ↦ κ·(y,z), κ = `scaleIdele E`, from complex coordinates y (indexed by
pairs (infinite place, index)) times finite adelic vectors z onto 𝔸^n. Along it the bicharacter β of
`adelicHeisenberg E s` and `New.vacuumFn` are the products of the real ones, for the signs
`realSigns E s`, and the finite ones. 

### `adeleMatrix_mulVec_adelicSum`

 Along `New.adelicSum` the matrix of `g` acts on the complex coordinates by the block diagonal
matrix `blockU g.1` of its infinite components `g.1 w`, and on the finite adelic vector by its
finite component `g.2`. 


## Multiplier, vacuum measure and action of the adelic unitary group

* `New.weilMultiplier`: the multiplier `Δ`, the product of the real ones `New.Fock.realMultiplier`
  and the finite one `New.finMultiplier`.
* `New.vacuumMeasure`, `New.isVacuum_vacuumFn`: a Haar measure on `𝔸 ^ n` for which
  `New.vacuumFn` is a vacuum.
* `New.adelicAction`: the action of `New.G E s` by matrices, with multiplier `Δ`.


### `weilMultiplier`

 The multiplier Δ(g) = Δ_f(g_f) ∏_w conj(det d_w) of an element g of the adelic unitary group
`G E s`: the product runs over the infinite places w, d_w is the block of g_w on the coordinates of
sign −1, and Δ_f is `New.finMultiplier`, the multiplier of the action `finAction` on finite adelic
vectors. 

### `vacuumMeasure`

 The Haar measure on 𝔸^n that is the image of the product of `New.Fock.normalizedVolume` and
`New.latticeMeasure` under the isomorphism `New.adelicSum` from real and finite coordinates. The
isomorphism does not depend on the signs, so the signs `1` are used. 

### `isVacuum_vacuumFn`

 The function `New.vacuumFn` (Gaussian at infinity times twisted lattice indicator at finite
places) is a vacuum, in the sense of `New.Heisenberg.IsVacuum`, for the bicharacter β of signs s and
the measure `New.vacuumMeasure`: it is the product of a real and a finite vacuum. 

### `instance : DistribMulAction (G E s) (n → 𝔸 E)`

 The adelic unitary group `G E s` acts on 𝔸^n through `G.toUnitary`, by its matrix. 

### `adelicAction`

 The continuous, β- and measure-preserving action of the adelic unitary group on 𝔸^n by matrices.
Its multiplier is `New.weilMultiplier`, which satisfies the identity of
`New.Heisenberg.MultiplierAction` with trivial cocycle. 

### `weilMultiplier_inv`

 The multiplier of `g⁻¹` is the complex conjugate of the multiplier of `g`. 

### `weilMultiplier_ne_zero`

 The multiplier `weilMultiplier g` = Δ_f(g_f) ∏_w conj(det d_w) of `g` in the adelic unitary
group `G E s` does not vanish. Here w runs over the infinite places, d_w is the block of g_w on the
coordinates of sign −1, and Δ_f = `finMultiplier`. It is a factor of the left side of the cocycle
identity. 

 ## The space 𝒮(V) and its operators 

### `𝒮`

 The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
under the L¹ norm; it depends only on the signs of V. 

### `heisenbergRep`

 The Heisenberg representation y ↦ ϱ(y) of (𝔸^n, β) on the Banach space 𝒮(V). 

### `ϱ`

 The Heisenberg operator of an adelic vector `y` on `𝒮 V`. 

### `ω`

 The Weil representation: the homomorphism from the adelic unitary group to the bounded operators
on 𝒮(V), ω(g)c = Δ(g) ∫ c(y) ϱ(gy) vac dy, where Δ is `New.weilMultiplier`. 

### `dataInner`

 The bounded sesquilinear form ⟨c, c′⟩ = ∫ c̄ c′ over 𝔸^n on 𝒮(V), on the underlying integrable
functions, conjugate-linear in the first variable. 

### `vacElem`

 The vacuum: the function e (Gaussian times twisted lattice indicator) as an element of 𝒮(V). 

 ### Real and finite coordinates 

### `realVec`

 The additive map from complex vectors indexed by pairs (infinite place τ, coordinate i) to 𝔸^n
that multiplies the coordinates at τ by (2π Im τ(ȷ))^(−1/2), ȷ being the element `j` of the Weil
data, and puts zero at the finite places. 

### `realCoord`

 The archimedean part of an adelic vector y in Fock coordinates: the complex numbers (2π Im
τ(ȷ))^{1/2}·y_{i,τ}, indexed by infinite places τ and coordinates i. 

### `finCoord`

 For an adelic vector y, the finite adelic vector with coordinates α⁻¹ times the finite part
of y_i, α the finite idele of the Weil data. 

### `finVec`

 The adelic vector with finite part αx (α the finite idele of the Weil data) and zero real part,
for a finite adelic vector x. 

### `realVec_realCoord_add`

 An adelic vector `y` is the real vector of its archimedean coordinates plus its finite part. 

### `adelicSum_real_eq_realVec`

 Along `adelicSum`, real coordinates `y` with zero finite part give the adelic vector
`realVec y`. 

### `_root_.Circle.coe_prod`

 The coercion to `ℂ` of a finite product of elements of the circle is the product of their
coercions. 

### `adelicHeisenberg_beta_eq_prod`

 The bicharacter `β` of the adelic Heisenberg datum of signs `s` is the product, over the
coordinates `i`, of the bicharacters of the lines of sign `s i`. 

### `vacuumFn_eq_prod`

 The vacuum function of `𝔸^n` is the product, over the coordinates, of the vacuum functions of
the lines. 

 ## Laws of the Weil representation 

### `map_eq_integral_dataInner`

 Superposition: a bounded linear map `T` from `𝒮 V` to a complex Banach space is determined by
its values on the translates ϱ(y) vac of the vacuum `vacElem`. Specifically, `T f` = ∫ ⟨ϱ(y) vac, f⟩
T(ϱ(y) vac) dy, where ⟨·,·⟩ is `dataInner` and the integral over y ∈ 𝔸^n is taken against
`vacuumMeasure`. That measure is the Haar measure on 𝔸^n given by the product of the normalized
volume on the real coordinates and the lattice measure on the finite coordinates. 

### `continuous_omega`

 The Weil representation `(g, f) ↦ ω(g) f` is jointly continuous. 

### `omega_rho`

 The Weil operators intertwine the Heisenberg operators: ω(g)ϱ(x)f = ϱ(gx)ω(g)f for g in G, x
an adelic vector and f in 𝒮(V). 

### `dataInner_rho`

 The Heisenberg operators `ϱ x` keep the inner product. 

### `dataInner_omega`

 The Weil operators `ω g` keep the inner product. 

### `eq_zero_of_dataInner_self`

 The inner product is definite: `⟨f, f⟩ = 0` forces `f = 0`. 

### `dataInner_vacElem_vacElem`

 The vacuum has inner square one. 

### `dataInner_vacElem_rho_vacElem`

 The Heisenberg matrix coefficient of `vacElem` at `y` is the vacuum function `New.vacuumFn` at
`y`. 

### `dataInner_vacElem_omega_vacElem`

 For a hermitian space `V` over a CM field `E` with Weil data, and `g` in the adelic unitary
group `G E s`, let `vacElem` be the vacuum vector of `𝒮 V` (a Gaussian times a twisted lattice
indicator). The matrix coefficient ⟨vac, ω(g) vac⟩ (`dataInner`, conjugate-linear in the first
variable) equals (conj Δ(g))⁻¹. Here Δ(g) = Δ_f(g_f) ∏_w conj(det d_w) is the multiplier
`New.weilMultiplier`, with d_w the block of g_w on the coordinates of sign −1. 

### `norm_omega_le`

 The operator norm of `ω g` is at most the norm of the vacuum times `|Δ g|`. 

### `dataInner_omega_vacElem_rho`

 For `g` in the adelic unitary group, the inner product `dataInner` of ω(g) vac with its
translate ϱ(y) ω(g) vac is `vacuumFn` evaluated at the adelic vector g⁻¹y. `vacuumFn` is the adelic
vacuum function: for x it is exp(−π ∑_{i,τ} Im(τȷ)|x_{i,τ}|²) · ψ_f(½c₀ȷ x_f*x_f) when the finite
part x_f lies in αÔ^n, and 0 otherwise. 

### `dataInner_omega_vacElem_omega`

 The inner product of the vacuum moved by `h` with its image under `ω g` is the inverse of the
conjugate of the multiplier of `h⁻¹ g h`. 

### `ext_of_vacElem`

 Two bounded linear maps from `𝒮 V` to a complex Banach space that agree on `ω g (ϱ y vacElem)`
for one `g` and all adelic `y` are equal. 


## Existence and uniqueness of theta functionals

The tool is Fourier analysis on the compact quotient of `𝔸^n` by `Λ = V.ratVectors`, whose
characters are `x ↦ β x (V.vecAtPoint γ) ^ 2`, `γ ∈ E^n` (`New.Space.isDualFamily_beta_sq`).


### `ratVectors`

 The rational points of V: the additive subgroup of 𝔸^n of the vectors x⁻¹y, y in E^n, where x is
the point `V.x` of V. 

### `mem_ratVectors_iff`

 An adelic vector `y` is a rational vector of `V` exactly when `V.x *ᵥ y` has rational
coordinates. 

### `beta_vecAtPoint_eq_one`

 The rational points of V are isotropic: the bicharacter β of `adelicHeisenberg E s` is `1` on
pairs of them. 

 ### Invariant functionals and the summation formula 

### `IsRatInvariant`

 A bounded functional ℓ on `Model (adelicHeisenberg E s)` is invariant under the rational
Heisenberg operators: ℓ(ρ(γ)v) = ℓ(v) for all v and all γ in `V.ratVectors`, where ρ(γ) =
`heisenbergOp γ` is the Heisenberg operator of γ. 

### `IsThetaFunctional`

 A theta functional of V: a bounded functional θ on `Model (adelicHeisenberg E s)` such that
(1) θ is invariant under the rational Heisenberg operators (`IsRatInvariant`), and
(2) the mean of |θ(ρ(x) vac)|² over x in 𝔸^n modulo `V.ratVectors` (`quotMean`, for the Haar
probability measure of the quotient) is 1. 

### `IsThetaFunctional.quotMean_eq_one`

 For a theta functional θ, the mean of |θ(ρ(x) vac)|² over 𝔸^n modulo the rational points
is 1. 

### `isDualFamily_beta_sq`

 Self-duality of the rational points: let β(x, y) = ψ(½ȷ h(y, x)) be the bicharacter of
`adelicHeisenberg E s`, with h the hermitian form of matrix `stdForm E s`, and let
`V.vecAtPoint γ = x⁻¹γ` for the point `x` of V. Then `γ ↦ (x ↦ β x (V.vecAtPoint γ) ^ 2)` is an
injective homomorphism from `E^n` to the unitary characters of `𝔸^n` trivial on `V.ratVectors`, and
the common kernel of these characters lies in `V.ratVectors`. The square removes the factor `1 / 2`
in `β`. 

### `summable_modelInner`

 For f', f in the model, the series of ⟨f', ρ(x⁻¹γ) f⟩ over the rational vectors γ ∈ E^n is
summable. 

### `isContPeriodic`

 For rationally invariant functionals ℓ', ℓ, the function x ↦ ℓ(ρ(x) f) · conj(ℓ'(ρ(x) f')) is
continuous and periodic under `V.ratVectors`. 

### `quotMean_eq_mul_modelInner`

 For rationally invariant functionals `ℓ'`, `ℓ`, the mean of `ℓ (ρ x f) * conj (ℓ' (ρ x f'))`
over `x` modulo the rational points is `c ⟨f', f⟩`, where `c` is the same mean for
`f' = f = vacElem`. 

### `hasSum_modelInner`

 The summation formula. For rationally invariant functionals `ℓ'`, `ℓ`, let `c` be the mean of
`ℓ (ρ x vacElem) * conj (ℓ' (ρ x vacElem))` over `x` modulo the rational points. Then the series of
`c ⟨f', ρ (V.vecAtPoint γ) f⟩` over `γ ∈ E^n` converges to `ℓ f * conj (ℓ' f')`. 

### `tendsto_sum_modelInner_heisenbergOp`

 For u in the model, the partial sums of the functionals `f ↦ ⟨u, ρ (V.vecAtPoint γ) f⟩` over
finite sets of γ ∈ E^n converge pointwise to the full series. 

### `ratSum`

 For u in the model, the bounded functional `f ↦ ∑' γ, ⟨u, ρ (V.vecAtPoint γ) f⟩`, a sum over the
rational vectors γ ∈ E^n. 

### `isRatInvariant_ratSum`

 The functional `V.ratSum u` is rationally invariant: translating by a rational vector
reindexes the series, and the factors of β are `1` on rational vectors. 

### `exists_isThetaFunctional`

 Every space V has a theta functional: a bounded functional θ on `Model (adelicHeisenberg E s)`,
invariant under the rational Heisenberg operators, with |θ(ρ(x)vac)|² of mean 1 over 𝔸^n modulo the
rational points. 

 ### Uniqueness of the theta functional 

### `exists_eq_apply_smul`

 Let θ be a theta functional of V: a bounded functional on the Heisenberg model
`Model (adelicHeisenberg E s)`, invariant under the Heisenberg operators ρ(γ) for γ in
`V.ratVectors`, and normalised so that the mean of |θ(ρ(x)vac)|² over 𝔸^n modulo `V.ratVectors`
is 1. Then there is a vector u in the model such that every bounded functional ℓ invariant under the
same operators equals ℓ(u) • θ. 

### `eq_smul`

 If θ is a theta functional of V, every bounded functional ℓ on `Model (adelicHeisenberg E s)`
invariant under the Heisenberg operators ρ(γ), γ a rational point of V, is a complex multiple of
θ. 

### `injective_apply_heisenbergOp`

 If θ is a theta functional of V, a vector `f` of the model is determined by its theta function
`x ↦ θ (ρ x f)` on `𝔸^n`. 


## The theta functional of a space

* `New.lineTheta`, `New.exists_isThetaFunctional_signedSpace`: a theta functional of the standard
  space whose values on translates of the vacuum are products of rank one values; this fixes its
  phase.


 ### The theta functional of the standard space 

### `lineTheta`

 For a sign c and an adele a, the number θ(ϱ(a)vac), θ a chosen theta functional of the
standard line of sign c. 

### `exists_isThetaFunctional_signedSpace`

 The standard space `signedSpace E s` has a theta functional θ with θ(ϱ(x)vac) = ∏_i
θ_i(ϱ(x_i)vac) for all x in 𝔸^n. Here θ is a bounded functional on the Heisenberg model
`Model (adelicHeisenberg E s)`, invariant under the rational Heisenberg operators and with mean of
|θ(ϱ(x)vac)|² equal to 1. Also, ϱ(x) = `heisenbergOp x`, vac is the vacuum vector, and
θ_i(ϱ(x_i)vac) = `lineTheta (s i) (x i)` for a chosen theta functional θ_i of the line of sign
s_i. 

### `IsThetaFunctional.comp`

 Transport of theta functionals. Let `θ` be a theta functional of `V`, and `T` a `σ`-semilinear
map that intertwines the Heisenberg operators along an isomorphism `φ` of adelic vectors. If `φ`
sends the rational vectors of `V₁` to those of `V` and `T vacElem` has inner square one, then
`σ ∘ θ ∘ T` is a theta functional of `V₁`. 

 ### The choice of the theta functional of `V` 

### `rawTheta`

 The functional θ₀ = θ_s ∘ ω(g) on 𝒮(V), where θ_s is the theta functional of the standard space
of signs s chosen in `New.exists_isThetaFunctional_signedSpace`, and g is a chosen element carrying
the rational vectors of V to those of the standard space. Such a g exists by Landherr's theorem
(`New.Space.exists_mapsTo_ratVectors`), so the second branch of the definition does not occur. 

### `θ`

 The theta functional of `V`. It equals `New.Space.rawTheta` (`New.Space.theta_eq_rawTheta`),
since `ϱ 0` is the identity. The factor `ϱ 0` makes `V.θ f = f 0` hold by definition, where
`f x = V.rawTheta (ϱ x f)` is the theta function of `f`. 

### `isThetaFunctional_rawTheta`

 The functional `V.rawTheta` is a theta functional of `V`: it is invariant under the rational
points, and |θ(ϱ(x)vac)|² has mean 1 over adelic vectors x modulo these. 

### `instance : FunLike (𝒮 V) (n → 𝔸 E) ℂ`

 A vector `f` is read as its theta function: `f x` is θ(ϱ(x) f). 

 ### Local operators 

### `integrated`

 The bounded bilinear map (v, f) ↦ v ⊗ f = ∫ v(y) ϱ(y)f dy, for v in the Fock space, f in
𝒮(V), y over real vectors in Fock coordinates. 

### `finHeisenbergOp`

 For a finite adelic vector x, the operator ϱ_f(x) = ψ(½c₀ȷαᾱ x*x) ϱ(αx) on 𝒮(V), α the finite
idele of the Weil data, where c₀ = `traceOneAdele` is integral with c₀ + c̄₀ = 1. The scalar is
`semichar x`; with it these operators represent the lattice Ô^n. 

### `projOn`

 For a set S of finite places, the operator P^S on 𝒮(V): the mean over y in Ô^n of
`New.Space.finHeisenbergOp` at the part of y above S ∪ S̄. 

### `projReal`

 The real vacuum projection: the bounded operator f ↦ ∫ exp(−|y|²/2) ϱ(y)f dy on 𝒮(V), y over
real vectors in Fock coordinates with measure `New.Fock.normalizedVolume`. 

### `ratMap`

 For a matrix i over E and spaces V, V' with adelic frames x, x', the adelic matrix x⁻¹ i x'. 


## Laws of theta functions

Convention: applying `f : 𝒮 V` to an adelic vector gives the theta function `f x = θ (ϱ x f)`, while
`f.1 x` is the value of the underlying integrable function.


### `apply_eq_rawTheta`

 The value of `f : 𝒮 V` at an adelic vector `x` is its theta function at `x`: the theta
functional `V.rawTheta` (see `New.Space.rawTheta`) applied to the Heisenberg translate `V.ϱ x f`. 

### `rho_apply`

 The theta function of a translate: `(ϱ y f) x = β x y * f (x + y)`. 

### `apply_vecAtPoint_add`

 Quasi-periodicity under rational vectors: for γ in E^n with adelic vector γ′ = `V.vecAtPoint γ`
(that is, x⁻¹γ for the point x of `V`) and any adelic x, we have β(γ′, x) f(γ′ + x) = f(x), where
f(x) = θ(ϱ(x)f). Here β(x, y) = ψ(½ȷ h(y, x)) is the bicharacter of the Heisenberg datum
`adelicHeisenberg E s`, and h is the hermitian form with matrix `stdForm E s`. 

### `dataInner_eq_quotMean`

 The form ⟨f, f'⟩ on 𝒮(V) equals the mean of conj(f(x)) f'(x) over adelic vectors x modulo
the rational vectors of V, data being read as functions by f(x) = θ(ϱ(x)f). 

### `theta_rho`

 For `f : 𝒮 V` and `y : n → 𝔸 E`, the theta functional `V.θ` takes the Heisenberg translate
`V.ϱ y f` of `f` by `y` to the value `f y`. 

### `norm_apply_le`

 A theta function is bounded by the norm of the theta functional times the norm of `f`. 

### `hasSum_dataInner`

 For f, f' in 𝒮(V), the family ⟨f', ϱ(γ)f⟩, γ running over the rational vectors of V, is summable
with sum θ(f) times the complex conjugate of θ(f').

This is Fourier inversion at 0 on the compact group of adelic vectors modulo rational vectors, for
the function x ↦ θ(ϱ(x)f)·conj(θ(ϱ(x)f')), whose Fourier coefficients, suitably indexed, are the
⟨f', ϱ(γ)f⟩. 
