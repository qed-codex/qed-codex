---
{
  "module": "src/Lib/Weil/Construction/ThetaDictionary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaDictionary.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaDictionary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The dictionary between vectors and theta functions

For rational vectors `γ` in `Eⁿ`, with real images in `ℂ^(Φ × n)`, this file defines the Riemann
form, the translations `T_γ` of functions on `ℂ^(Φ × n)` and the theta functions for a lattice.

* `New.ratShift_ratShift`, `New.mem_star_smul_idealLattice_iff`, `New.signedShift_add`: the law of
  composition of the translations `T_γ`, the duality of `δ̄ 𝔞₀ⁿ` and `δ⁻¹ 𝔞₀ⁿ` for the Riemann form,
  and the signs that make the translations a homomorphism on `𝔞₀ⁿ`.
* `New.Space.entireTheta_rho`: for a standard space, the Heisenberg translation `V.ϱ (finVec x)`,
  with `x = α⁻¹ γ` the finite image of a rational vector `γ`, acts on theta functions as `T_(-γ)`.
* `New.Space.range_apply_finVec_eq_range_ratShift_entireTheta`: for a standard space and `φ` in the
  finite part, the values of `φ` at the finite adelic vectors are the values
  `T_γ (entireTheta φ) 0`.
* `New.Space.isThetaFunction_iff`: for a standard space, the theta functions for `𝔞₀ⁿ` are the
  multiples of the theta function of the vacuum, because the Riemann form on `𝔞₀ⁿ` is unimodular.

Here `ℂ^(Φ × n)` stands for `InfinitePlace E × n → ℂ`, and `Φ w` is the embedding of `E` in `ℂ` that
the CM type chooses at the infinite place `w`.

Notions from other files:
* `realImage γ`: the entry at `(w, i)` is `Φ w (γ i)` divided by the `w`-part of the idele
  `scaleIdele E`; `finiteImage γ` is `α⁻¹ γ` in `(𝔸f E)ⁿ`, with `α` the finite part of this idele.
* `stdLattice E n`: the lattice `Ôⁿ` of integral finite adelic vectors; it is its own dual for the
  character `selfDualAddChar E`.
* `semichar x`: the value `selfDualAddChar E (traceOneAdele * half * star x ⬝ᵥ x)`, where
  `traceOneAdele` is the image of `traceOne = c₀ : E`, with `c₀ + c̄₀ = 1`.
* `𝒮 V` is the space of vectors of the Weil representation of a space `V`, with vacuum `V.vacElem`
  and Heisenberg action `V.ϱ`; `entireTheta φ` is the theta function of `φ`.
* `V.IsStd`: all signs of `V` are `+1` and its point is the identity matrix.

## Relation to the literature

Known result: the passage between the Fock model of the Weil representation and classical theta
functions. A principal polarization has one theta function up to a factor. Source: Beauville, Theta
functions, old and new, Theorem 3.5.


### `fockForm`

 The standard Hermitian form `u* z = ∑ conj (u x) z x` on `ℂ^X`. 

### `isAppellHumbert_fockForm`

 The standard Hermitian form has symmetric real part, and with the multiplier `1` it is an
Appell–Humbert datum for the zero lattice. 

### `isPosRiemann_fockForm`

 The standard Hermitian form is positive definite, so it is a positive Riemann form. 

### `realImage_apply`

 The entry of the real image of `γ` at `(w, i)` is `Φ w (γ i)` divided by the `w`-component of
the idele `scaleIdele E`. 

### `realImageHom`

 The real image of rational vectors as an additive map. 

### `injective_realImageHom`

 A rational vector is determined by its real image. 

### `idealLattice`

 The lattice `𝔞₀ⁿ` of `Eⁿ`: the vectors `γ` whose finite image `α⁻¹ γ` lies in `Ôⁿ`. 

### `smul_mem_idealLattice`

 The lattice `𝔞₀ⁿ` is stable under multiplication by the elements of `E` that are integral at
all finite places. 

### `ratShift`

 The translation `T_γ` of functions on `ℂ^(Φ × n)`: the translation by the real image of `γ`,
twisted by the exponential factor of the standard Hermitian form (`thetaShift`). 

### `ratRiemannForm`

 The Riemann form `{γ, γ'} = Im (u* u') / π` of rational vectors with real images `u`, `u'`. 

### `ratPhase`

 The commutator `exp (2 π i {γ, γ'})` of the translations `T_γ` and `T_γ'`. 

### `ratShift_ratShift`

 Let `E` be a CM field with Weil data, `γ`, `γ'` vectors of `Eⁿ`, and `F` any function on
`ℂ^(Φ × n)`. The translations `T_γ = ratShift γ` (translation by the real image of `γ`, twisted by
the exponential factor of the standard Hermitian form) obey the law of composition
`T_γ T_γ' F = exp (π i {γ, γ'}) T_(γ + γ') F`. Here `{γ, γ'} = ratRiemannForm γ γ' = Im (u* u') / π`
is the Riemann form of the real images `u`, `u'`. 

### `ratShift_comm`

 The commutator of `T_γ` and `T_γ'` is `exp (2 π i {γ, γ'})`. 

### `realHeisenberg_beta_mul_selfDualAddChar_eq_one`

 For rational vectors `γ, γ'` with finite images `x, x'`, the adelic Heisenberg cocycle, which is
the product of the real cocycle `β` of `realHeisenberg` at the real images (which is
`exp (-π i ratRiemannForm γ γ')`; see `exp_ratRiemannForm`) and of the finite character
`ψ₀ (x'* x / 2)`, is `1`. 

### `exp_ratRiemannForm`

 The product formula for the Heisenberg cocycle: for rational vectors `γ, γ'` with finite
images `x, x'`, the value `exp (π i {γ, γ'})`, which is inverse to the real cocycle, equals
`ψ₀ (x'* x / 2)`. Here `{γ, γ'}` is `ratRiemannForm γ γ'` and `half` is the adelic `1/2`. 

### `ratPhase_eq`

 The commutator of `T_γ` and `T_γ'` is `ψ₀ (x'* x)` for the finite images `x`, `x'`. 

### `ratPhase_smul_left`

 For the commutator of translations, multiplication by `star δ` is adjoint to that by `δ`. 

### `mem_idealLattice_iff_ratPhase`

 The lattice `𝔞₀ⁿ` is self-dual for the Riemann form: `γ` lies in it exactly when
`exp (2 π i {γ, y}) = 1` for all `y` in it. 

### `mem_star_smul_idealLattice_iff`

 For `δ ≠ 0`, the lattice `δ̄ 𝔞₀ⁿ` is dual to `δ⁻¹ 𝔞₀ⁿ` for the Riemann form: `γ` lies in it
exactly when the phase `exp (2 π i {γ, y})` is `1` for every `y` in `δ⁻¹ 𝔞₀ⁿ`. 

### `signedShift`

 The translation `T_γ` times the value of the semicharacter at the finite image of `γ`. For `γ`
in `𝔞₀ⁿ` this value is the sign `(-1) ^ |γ|²`, where `|γ|² = ∑ |Φ w (γ i)|²`; see
`New.exists_semichar_finiteImage_eq_neg_one_zpow`. 

### `semichar_finiteImage_add`

 Let `E` be a CM field with Weil data. These give a finite idele `α`, an algebraic integer `c₀`
of `E` with `c₀ + c̄₀ = 1`, and the character `ψ₀ = selfDualAddChar E` of the finite adeles, for
which `Ô` is self-dual. For a rational vector `γ` in `Eⁿ` put
`χ γ = semichar x = ψ₀ (c₀ x* x / 2)`, where `x = finiteImage γ = α⁻¹ γ` is a finite adelic vector.
If `γ` and `γ'` lie in the lattice `𝔞₀ⁿ = idealLattice E n`, that is, their finite images are
integral, then `χ (γ + γ') = χ γ * χ γ' * exp (π i {γ, γ'})`. Here `{γ, γ'} = Im (u* u') / π` is
the Riemann form `ratRiemannForm γ γ'`, with `u`, `u'` the real images of `γ`, `γ'`. 

### `signedShift_add`

 The signed translations are a homomorphism on `𝔞₀ⁿ`. 

### `IsThetaFunction`

 A theta function for a subgroup `Y` of `Eⁿ` is an entire function on `ℂ^(Φ × n)` that the
signed translations `signedShift γ`, `γ ∈ Y`, fix. 

### `IsThetaFunction.differentiable`

 The function is entire. 

### `IsThetaFunction.signedShift_eq`

 The signed translations along `Y` fix the function. 

### `canonicalMultiplier_realImage`

 If `b` multiplies the coordinates at the place `w` by `conj (Φ w traceOne)`, the canonical
multiplier `exp (π i R (b u, u))`, with `R` the Riemann form, at the real image `u` of `γ` is the
inverse of the semicharacter at the finite image; `traceOne` is `c₀ : E` with `c₀ + c̄₀ = 1`. 

### `normalizedShift_realImage`

 If `b` multiplies the coordinates at the place `w` by `conj (Φ w traceOne)`, the normalized
translation (the inverse of the canonical multiplier of `fockForm` times `thetaShift`) by the real
image of `γ` is the signed translation. 

### `im_traceOne_mul_normSq_realImage`

 For the entry `u` of the real image of `γ` at `x = (w, i)`, one has
`Im (Φ w c₀) |u|² = π |Φ w (γ i)|²`, where `c₀ = traceOne = (1 - ȷ⁻¹) / 2`. 

### `semichar_finiteImage_eq_exp`

 The semicharacter at the finite image of a rational vector `γ` is `exp (-π i |γ|²)`, where
`|γ|² = ∑ |Φ w (γ i)|²` is summed over the infinite places `w` and the coordinates `i`. 

### `exists_semichar_finiteImage_eq_neg_one_zpow`

 Let `E` be a CM field with Weil data, and let `Φ w` be the chosen complex embedding at each
infinite place `w`. For `γ` in the lattice `𝔞₀ⁿ`, the vectors of `Eⁿ` whose finite image `α⁻¹ γ`
lies in `Ôⁿ` (with `α` the idele of the Weil data), the number `|γ|² = ∑ |Φ w (γ i)|²` is an
integer. The semicharacter `semichar x = ψ₀(c₀ x* x / 2)` at `x = finiteImage γ` is the sign
`(-1) ^ |γ|²`. 

### `realLattice`

 The image of `𝔞₀ⁿ` in `ℂ^(Φ × n)`. 

### `instance : IsFullRankLattice (realLattice E n)`

 The image of `𝔞₀ⁿ` is a lattice of full rank in `ℂ^(Φ × n)`. 

### `Space.entireThetaHom`

 The theta function of a vector, as a linear map. 

### `Space.injective_entireThetaHom`

 A vector `φ` in the space `𝒮 V` of the Weil representation of `V` is determined by its theta
function `entireTheta φ` on `ℂ^(Φ × n)`. 

### `Space.entireTheta_vacElem_ne_zero`

 Let `V` be a space over a CM field `E` with Weil data. The theta function of its vacuum
`V.vacElem` (the Gaussian times the twisted lattice indicator, as a vector of `𝒮 V`) is not
identically zero. Here the theta function `entireTheta φ` of a vector `φ` sends `y` to the value of
`φ` at the real adelic vector `y` divided by the Gaussian `exp (-|y|² / 2)`. 

### `Space.entireTheta_rho`

 Let `V` be a standard space, meaning that all its signs are `+1` and its point is the identity,
and let `γ` be a vector of `Eⁿ` with finite image `x = α⁻¹ γ`. For every vector `φ` of `𝒮 V`, the
theta function of the translate of `φ` by the adelic vector `finVec x`, with finite part `α x = γ`
and real part zero, is `ratShift (-γ)` of the theta function `entireTheta φ`, that is, its
translate by minus the real image of `γ`, twisted by the exponential factor of the standard
Hermitian form. 

### `Space.range_apply_finVec_eq_range_ratShift_entireTheta`

 Let `V` be a standard space and let `φ` lie in its finite part, the span of the finite
translates of the vacuum. The values of `φ` at the finite adelic vectors are the values at `0` of
the translates `T_γ = ratShift γ` of the theta function of `φ`, for the rational vectors `γ`. 

### `Space.entireTheta_finHeisenbergOp`

 Let `V` be a standard space (all signs `+1`, point the identity matrix), `φ` a vector of its
Weil representation `𝒮 V`, and `γ` any vector of `Eⁿ` with finite image `x = α⁻¹ γ`, where `α` is
the idele of the Weil data. The operator `V.finHeisenbergOp x` is the Heisenberg action `ϱ(α x)`
scaled by the semicharacter `semichar x`. It sends the theta function `entireTheta φ` to
`signedShift (-γ)` of it, namely its translate by `T_(-γ)` times the semicharacter at the finite
image of `-γ`. 

### `Space.isThetaFunction_vacElem`

 For a standard space `V`, the theta function of the vacuum is a theta function for `𝔞₀ⁿ`. 

### `mem_thetaSpace_iff_isThetaFunction`

 Suppose that the linear map `b` multiplies the coordinates at the place `w` by
`conj (Φ w traceOne)`, where `traceOne` is `c₀ : E` with `c₀ + c̄₀ = 1`. A function `G` on
`ℂ^(Φ × n)` is a theta function for the image `realLattice E n` of the lattice `𝔞₀ⁿ`, the standard
Hermitian form `fockForm` and the canonical multiplier `exp (π i R (b u, u))`, `R` the Riemann
form, if and only if `G` is entire and fixed by the signed translations along `𝔞₀ⁿ`. 

### `isAppellHumbert_realLattice`

 Suppose that the linear map `b` multiplies the coordinates at the place `w` by
`conj (Φ w traceOne)`, where `traceOne` is `c₀ : E` with `c₀ + c̄₀ = 1`. The standard Hermitian
form `fockForm` and the canonical multiplier `χ u = exp (π i R (b u, u))`, with `R` the Riemann
form, are an Appell–Humbert datum for the image `L` of `𝔞₀ⁿ` in `ℂ^(Φ × n)`: the real part of the
form is symmetric and, on `L`, `|χ| = 1` and `χ (l + m) = χ l * χ m * exp (π i R (m, l))`. 

### `dualLattice_fockForm_le_realLattice`

 The image `realLattice E n` of `𝔞₀ⁿ` in `ℂ^(Φ × n)` is unimodular: if some multiplier `χ`
makes the standard Hermitian form `fockForm` an Appell–Humbert datum for it, it contains its dual
lattice, that is, every vector whose Riemann form with each element of the image is an integer. 

### `finrank_thetaSpace_realLattice`

 Suppose that the linear map `b` multiplies the coordinates at the place `w` by
`conj (Φ w traceOne)`, where `traceOne` is `c₀ : E` with `c₀ + c̄₀ = 1`. The theta functions for
the image `realLattice E n` of `𝔞₀ⁿ` in `ℂ^(Φ × n)`, the standard Hermitian form and the canonical
multiplier of `b` form a space of dimension `1`, as this lattice is unimodular. 

### `Space.isThetaFunction_iff`

 Let `V` be a standard space over the CM field `E` (all signs `+1`, point the identity matrix).
A function `F` on `ℂ^(Φ × n)` is a theta function for the lattice `𝔞₀ⁿ` of `Eⁿ`, that is, entire
and fixed by its signed translations, exactly when it is a multiple of the theta function of the
vacuum vector of `V`. 
