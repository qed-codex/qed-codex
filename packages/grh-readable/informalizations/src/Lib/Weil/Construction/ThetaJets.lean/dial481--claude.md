---
{
  "module": "src/Lib/Weil/Construction/ThetaJets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Jet series of theta functions and translation by rational vectors

Let V be a hermitian space with a point over a CM field E, with data space 𝒮(V). Let `α` be
the finite idele of the Weil data, let `finVec x` be the adelic vector `(0, α x)`, let
`finiteImage γ` be `α⁻¹ γ` in `(𝔸f E)ⁿ` (finite adeles) for γ in Eⁿ, so that
`finVec (finiteImage γ)` is `(0, γ)`, and let `V.ϱ (finVec x)` be translation along a finite vector
`x`. The file turns theta functions into Taylor series and Schur jet matrices, and defines when the
jets of two data are conjugate. For a standard space V it shows that translation by the finite image
of a rational vector acts on theta functions as the opposite real translation.

## Main definitions and results

* `New.Space.jetSeries`: the series of the theta values of `f` along the monomials; for standard `V`
  and `f` in the finite part it is the Taylor series of the theta function of `f`, scaled by `a`.
* `New.schurJet`: the matrix of jets of a power series along the entries of the Schur matrix.
* `New.Space.IsJetConjugate`: the jets of `f'` are the `σ`-conjugates of the jets of `f`, up to a
  permutation of the infinite places.
* `New.entireTheta_translate_finiteImage`: for standard `V`, `New.Space.entireTheta` turns
  translation by `finiteImage γ` into the twisted translation by `-realImage γ`.
* `New.semichar_finiteImage`: the semicharacter at the finite image of a rational vector is the
  inverse of the canonical multiplier at minus its real image.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.Space.θ`, `New.Space.integrated`: The theta functional on the space `New.𝒮 V` of data, and
  the datum v ⊗ f for v in the Fock space and f in `New.𝒮 V`.
* `New.WeilData`: supplies the purely imaginary `j` (ȷ) in E, the finite idele `α` and the integer
  `traceOne` (c₀) with c₀ + c̄₀ = 1.
* `New.Space.entireTheta` sends `f` to `y ↦ f(y) exp(|y|²/2)` on real points; `New.Space.ϱ` is
  Heisenberg translation; `New.Space.finitePart` is the span of the finite translates of the vacuum.

## Relation to the literature

Known result: the theta functions of the Fock model of the adelic Weil representation. Source: Weil,
Sur certains groupes d'opérateurs unitaires. Part of a known result: Adelic Weil representation of a
unitary group and the invariant theta functional. See `Lib.Weil.MixedModel.ZeroTerm`.

See also `Lib.Weil.CompactLift.DefiniteThetaLift` and `Lib.Weil.DualPair.KernelLaws`.



## Standard spaces, Taylor series of theta functions and Schur jets

A weight `κ` gives the number `κ τ h` of columns of height `h` at the place `τ`.
`New.WeylIndexFamily (fun τ ↦ n) κ` indexes the coordinates of weight `κ` in rank `n` at each place.
`New.schur κ z` is the matrix of `z` in these coordinates. `New.jet R P F` is `P(∂) F` at `0`.


### `Space.IsStd`

 The space `V` is standard: all its signs are `+1` and its point is the identity matrix. This
describes the standard space `stdSpace E n` without fixing the form in which the signs are
written. 

### `Space.IsStd.signs_eq_one`

 All signs at the infinite places are `+1`. 

### `Space.IsStd.point_eq_one`

 The point of `V` is the identity matrix. 

### `Space.jetSeries`

 The series in which the coefficient of `z ^ α` is `a ^ |α| / α!` times the theta functional of
`v ⊗ f`, where `v` is the Fock vector of the monomial `z ^ α`. If all signs of `V` are `+1` and `f`
lies in the finite part, it is the Taylor series at `0` of `z ↦ V.entireTheta f (a • z)`; this is
proved on each line through `0` in `New.Space.taylor_line_eq_subst_jetSeries`. 

### `Space.jet_jetSeries_eq_theta`

 `V.jetSeries a f` is the power series in variables indexed by `InfinitePlace E × n` whose
`z ^ α` coefficient is `a ^ |α| / α!` times `V.θ (V.integrated v f)`, with `v` the Fock vector of
`z ^ α`. Its jet `P(∂) (V.jetSeries a f)` at `0` is `V.θ` of `v ⊗ f` (`V.integrated v f`), where `v`
is the Fock vector of the polynomial `z ↦ P(a z)`. 

### `boxes`

 The number of boxes in the columns of height below `N`, where `κ τ h` is the number of columns
of height `h` at the place `τ`. 

### `schurJet`

 The matrix of jets of a power series `F` in the entries of matrices `z τ` of size `n' × n`: the
entry at `(i', i)` is `P(∂) F` at `0`, for `P` the polynomial at `(i', i)` in `schur κ z`. 

 ## Conjugate jets and the constant term 

### `IsJetConjugate`

 The jets of `f'` at scale `t'` are the `σ`-conjugates of the jets of `f` at scale `t`: applying
`σ` to the coefficients of the series of `f` gives the series of `f'` with each variable
`(v, i)` renamed `(π⁻¹ v, i)`, where `π` permutes the infinite places `v` of `E`. 

### `constantCoeff_jetSeries`

 The constant term of the scaled Taylor series of `f` is the theta functional of the projection
of `f` onto the real vacuum. 


## Rational vectors, translation of theta functions and the finite semicharacter

The laws for the translation and for the semicharacter follow from the invariance of vectors and
cocycles under rational points.


 ### Rational vectors at the real and at the finite places 

### `realImage`

 The archimedean image of γ in E^n in Fock's coordinates: the complex vector with the entry √(2π
Im τ(ȷ))·τ(γ_i) at (τ, i), where τ(c) is written `Φ τ c`. 

### `exists_finiteImage_approx`

 For `F` in the finite part (the span of the finite translates of the vacuum) and a finite adelic
vector `x` there is a rational `γ` whose finite image is congruent to `x` modulo `Ôⁿ` and such that
the Heisenberg translations `ϱ` along `finVec (finiteImage γ)` and `finVec x` agree on `F`. 

### `vecAtPoint_eq_adelicSum`

 For a standard space (signs `+1`, point `1`), the adelic vector `x⁻¹γ` attached to `γ` at the
point `x` corresponds under `adelicSum`, the splitting of adelic vectors into real and finite
coordinates, to the pair of `realImage γ` and `finiteImage γ`. 

### `entireTheta_translate_finiteImage`

 Let `V` be a standard space (all signs +1, point the identity), let B l z = l* z, and let
γ ∈ E^n. The theta function `entireTheta` (Θ_f(y) = θ(ϱ(y)f)·exp(|y|²/2)) of the Heisenberg
translate of f by `finVec (finiteImage γ)` is `thetaShift B (-realImage γ)` applied to
`entireTheta f`. Here `finVec (finiteImage γ)` is the adelic vector with finite part γ and real part
zero, and `thetaShift B a F z = exp(−(B a z + B a a/2))·F(z + a)`. 

 ### The product formula 

### `semichar_finiteImage`

 Let `B l z = l* z` and let `b` multiply the coordinates at each place `τ` (embedding `Φ τ`) by
the conjugate of `τ(t)`, with `t = traceOne`. The semicharacter `ψ₀(t x* x / 2)`, with
`ψ₀ = selfDualAddChar E`, at the finite image `x` of `γ` is the inverse of the canonical multiplier
`y ↦ exp(π i B.riemannForm (b y) y)` of `B` and `b` at minus the real image, by the product formula
for the cocycle `β(t γ, γ)`. 
