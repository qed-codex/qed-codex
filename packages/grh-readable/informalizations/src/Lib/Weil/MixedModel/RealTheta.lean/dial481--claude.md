---
{
  "module": "src/Lib/Weil/MixedModel/RealTheta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/RealTheta.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/RealTheta.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Real data, the entire theta function, and the real vacuum in the mixed model

A datum f in `New.𝒮` V is a function on adelic vectors, f(x) = θ(ϱ(x)f), where θ is the theta
functional and ϱ the Heisenberg operators. For v in Fock space we write v ⊗ f = ∫ v(y) ϱ(y) f dy
over real vectors y, and compute its inner products and theta value. If all signs are +1 and f is
fixed by the real vacuum projection, then the theta function Θ_f(y) = f(y) exp(|y|²/2) is entire.
The last part computes the real vacuum and the map `T 0` in a mixed Schrödinger model `T`.

## Main definitions and results

* `New.Space.eq_zero_of_apply_realVec_eq_zero`: f is determined by its values on real vectors, by
  strong approximation and quasi-periodicity under rational vectors.
* `New.Space.entireTheta`: the function Θ_f(y) = f(y) exp(|y|²/2).
* `New.Space.entireTheta_eq_integral`, `New.Space.differentiable_entireTheta`: if all signs are +1
  and inserting the Gaussian as real vector (`New.Space.projReal`) fixes f, then Θ_f is an integral
  against the kernel exp(∑ y_p conj w_p), hence entire.
* `New.Space.theta_integrated_polyVector_eq_integral_entireTheta`: if all signs are +1, the theta
  value of v_P ⊗ f for a polynomial vector v_P is ∫ P(conj y) Θ_f(y) exp(−|y|²) dy.
* `New.Space.Splitting.IsAdapted.omega_projReal_of_isMixedLaw`: in a mixed Schrödinger model `T`,
  the value `T x (ω(g) P f)` is a Gaussian in the real point `x`, for `P` the real vacuum projection
  and `g` adapted to the splitting.
* `New.Space.Splitting.IsAdapted.exists_apply_zero_omega_integrated_eq`: `T 0 ∘ ω(g)` acts on the
  real part by a bounded map of Fock spaces. Here `V.integrated v f`, written v ⊗ f, gives `f` the
  real part `v`, and `V.projReal` is the case of the real vacuum.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.realVec`: the additive map from ℂ^{places × n} to 𝔸^n that multiplies the coordinates at τ by
  (2π Im τȷ)^(−1/2) and puts zero at the finite places.
* `New.Fock.realVac`: the function on ℂ^ι sending x to exp(−|x|²/2).
* `New.Space.Splitting.IsMixedLaw`: the law of a mixed Schrödinger model `T x : 𝒮 V → 𝒮 V₀`,
  `x ∈ 𝔸ᵖ`: for `y = l a + ι w + k b`, `T x (ϱ y f)` is `β (2 x + a) b` times `ϱ w (T (x + a) f)`.

## Relation to the literature

Known; see `Lib.Weil.Fock.OscillatorPair` and `Lib.Weil.MixedModel.ZeroTerm` for sources.


 ## Inner products and theta values of real data 

### `map_integrated_eq_integral_realVec`

 For v in the Fock space, f in 𝒮(V) and a bounded linear map T from 𝒮(V) to a Banach space,
T(v ⊗ f) = ∫ v(y) T(ϱ(y) f) dy, with y over real vectors in Fock coordinates (`New.realVec`). 

### `dataInner_integrated`

 For v, w in the Fock space and f, f′ in 𝒮(V), ⟨v ⊗ f, w ⊗ f′⟩ = ⟨v, w⟩ · ⟨Pf, Pf′⟩, where
v ⊗ f = ∫ v(y) ϱ(y) f dy over real vectors y and P is the real vacuum projection. 

### `eq_zero_of_integrated_eq_zero`

 If v ⊗ f = 0 for v in the Fock space and f in 𝒮(V) with Pf ≠ 0, then v = 0. Here
v ⊗ f = ∫ v(y) ϱ(y) f dy over real vectors y and P is the real vacuum projection. 

### `theta_integrated`

 For `v` in the Fock space and `f` in 𝒮(V), `θ(v ⊗ f) = ∫ v(y) f(realVec y) dy`, where
`v ⊗ f = ∫ v(y) ϱ(y)f dy` is `New.Space.integrated` and `f(x) = θ(ϱ(x)f)`. Here `y` runs over
complex vectors indexed by (infinite place, coordinate) with the measure
`New.Fock.normalizedVolume`, and `realVec` turns `y` into an adelic vector by scaling the
coordinates at `τ` by `(2π Im τ(ȷ))^(−1/2)`, with zero at the finite places. 


## The theta function on real vectors

A datum f in `New.𝒮` V is applied to an adelic vector x as f(x) = θ(ϱ(x)f), θ the theta functional
of V. Here this function is restricted to real vectors, `New.realVec` y, with y in complex Fock
coordinates and finite part zero.


### `entireTheta`

 For f in 𝒮(V), the function Θ_f(y) = θ(ϱ(y)f)·exp(|y|²/2) of a real vector y in Fock
coordinates, placed in the adelic vectors with finite part zero. 

### `eq_zero_of_apply_realVec_eq_zero`

 An element f of 𝒮(V) whose values f(y) = θ(ϱ(y)f) vanish at all adelic vectors y with finite
part zero is zero. 

### `entireTheta_eq_integral`

 If all signs are +1 and inserting the Gaussian as real vector fixes f, then
Θ_f(y) = ∫ exp(∑_p y_p conj w_p) exp(−|w|²/2) f(w) dw, over real vectors w with Lebesgue
measure divided by π to the number of coordinates. 

### `differentiable_entireTheta`

 Suppose all signs `s` are +1 and `f` is fixed by the real vacuum projection
`f ↦ ∫ exp(−|y|²/2) ϱ(y)f dy` (`projReal`). Then `Θ_f(y) = θ(ϱ(y)f)·exp(|y|²/2)` is complex
differentiable everywhere as a function of the complex vector `y`, indexed by (infinite place,
coordinate), that gives a real vector in Fock coordinates. 

### `theta_integrated_polyVector_eq_integral_entireTheta`

 Let all signs be +1, let `P` be a complex polynomial in the Fock coordinates, and let `f` be an
element of 𝒮(V). Then `θ(v_P ⊗ f) = ∫ P(conj y) Θ_f(y) exp(−|y|²) dy`, where
`v_P(x) = P(ζ(x))·exp(−|x|²/2)`, with ζ the holomorphic coordinates (`holomorphicCoord`), here
ζ(x) = conj x since all signs are +1, is the polynomial vector (`New.Fock.polyVector`) and
`v ⊗ f = ∫ v(y) ϱ(y)f dy` (`New.Space.integrated`). Here `Θ_f(y) = θ(ϱ(y)f)·exp(|y|²/2)`
(`entireTheta`), and `y` runs over complex vectors indexed by (infinite place, coordinate) with the
measure `New.Fock.normalizedVolume`. 


## The real vacuum in a mixed Schrödinger model

A splitting `D` (`New.Space.Splitting`) writes `V` as `l Eᵖ ⊕ ι V₀ ⊕ k Eᵖ` with `l`, `k` isotropic
and dual. Only the infinite places are treated. The last three results concern an element `g` of
`G E s` adapted to some `t` in `GL_p(𝔸)` (`New.Space.Splitting.IsAdapted`): the matrix
`g⁻¹ (l (t⁻¹)ᴴ, k t, ι)` has orthonormal columns at the infinite places and integral finite entries.


### `realMatrix`

 The archimedean part of an adelic matrix A as one complex matrix, block diagonal over the
infinite places, whose block at τ is the τ-component of A. 

### `realVec_realCoordSum`

 In the coordinates of the orthogonal sum of `s` and `s₀` (`New.Fock.realCoordSum`, whose `equiv`
joins a pair into one function on places × (n ⊕ n₀); `⊕ᵥ` joins two vectors likewise), `realVec` of
a pair is the pair of the `realVec`s. 

### `realVec_realMatrix_mulVec`

 Acting by `realMatrix A` in Fock's coordinates is acting by `A` on real adelic vectors. 

### `conjTranspose_realMatrix_mul_self`

 If `A` has orthonormal columns at the infinite places (and integral finite entries), then
`realMatrix A` has orthonormal columns. 

### `beta_eq_coords`

 For a splitting of V over V₀, write y = la + ιw + kb and y' = la' + ιw' + kb'. Then
β(y,y') = ψ(½ȷ(a'*b + b'*a)) β₀(w,w'), with β₀ the bicharacter for the signs of V₀. 

### `isMixedLaw_comp_rho`

 If a bounded map `L : 𝒮 V → 𝒮 V₀` is (a) invariant under the Heisenberg operators along `k`
and (b) intertwines those of `V₀`, then the family `x ↦ L ϱ(l x)` obeys the law of a mixed
model. 

### `integral_beta_mul_realVac`

 The Gaussian integral along the isotropic frame `k`. With e(y) = exp(−|y|²/2) and β the
bicharacter of `realHeisenberg 1` on ℂ^ι, the integral of β(2x + c, b) e(c) e(b) over b is
exp(−|x|²) e(x + c)² 2^|ι|. 

### `IsAdapted.omega_projReal_of_isMixedLaw`

 The real vacuum is a Gaussian in the mixed model. Let `T` obey the law of a mixed model
(`IsMixedLaw`) for the splitting `D`, and let `g` be adapted to `t` (`IsAdapted`). With `P`, `P₀`
the real vacuum projections of `V`, `V₀`, we have
`T x (ω(g) P f) = exp(−|a|²) P₀ (T 0 (ω(g) P f))` at the point `x = (t⁻¹)ᴴ (realVec a)`. 

### `IsAdapted.exists_apply_zero_omega_integrated_eq`

 Let `T` obey the law of a mixed model (`IsMixedLaw`) for the splitting `D`, and let `g` be
adapted to `t` (`IsAdapted`). Then there is a bounded map `L` between the Fock spaces of `V` and
`V₀` with `T 0 (ω(g)(v ⊗ f)) = L v ⊗ T 0 (ω(g) P f)`, where `P` is the projection on the real
vacuum and `⊗` stands for `New.Space.integrated`. 

### `IsAdapted.exists_map_vacVector_apply_zero_omega_eq`

 Let `D` split `V` as `(l E^p ⊕ k E^p) ⊥ i V₀`, and let the maps `T x : 𝒮 V → 𝒮 V₀` (`x` in
`𝔸^p`) obey the law of the mixed Schrödinger model (`IsMixedLaw`). Let `g` in `G E s`, acting on
𝒮(V) by `ω` with ω(g)ϱ(y) = ϱ(g y)ω(g), be adapted to `t` (`D.frameAt g t` is orthonormal at
infinity and integral) in `GL_p(𝔸)`. Then there is a bounded map `L` from the Fock space of `V` to
that of `V₀` that sends the vacuum (Gaussian) to the vacuum and satisfies
`T 0 (ω(g)(v ⊗ f)) = L v ⊗ T 0 (ω(g)(P f))` for all `v` and `f`, where `v ⊗ f = ∫ v(y) ϱ(y)f dy` is
`New.Space.integrated` and `P` is the real vacuum projection `projReal`. 
