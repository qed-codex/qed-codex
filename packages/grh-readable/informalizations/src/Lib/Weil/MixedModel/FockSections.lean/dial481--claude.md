---
{
  "module": "src/Lib/Weil/MixedModel/FockSections.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/FockSections.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/FockSections.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mixed Schrödinger–Fock models and rapid sections with prescribed values

A mixed model reads a vector `Φ` of a large Fock space `New.Fock.fockSpace` as a function
`x ↦ h.slice x Φ` on `ℂ ^ p` with values in a smaller Fock space. An adapted splitting of a
hermitian space induces one at the infinite places (`New.Space.Splitting.IsAdapted.mixedModel`). A
vector is a Schwartz vector (`New.Exchange.IsSchwartzVector`) if all its moments `fockMoment N
v = ∫⁻ y, (1 + ‖y‖) ^ N * ‖v y‖ ∂normalizedVolume` are finite; `New.Fock.realWeil` is the Weil
representation.

The file shows that the values of a mixed model decay rapidly. It also constructs Schwartz vectors
with prescribed smooth compactly supported values, using Fourier inversion in `x` and non-stationary
phase.

## Main definitions and results

* `New.Fock.MixedModel`: the structure, described by the action of the Heisenberg operators
  `New.Fock.realHeisenbergOp` and by the value of the vacuum.
* `New.Fock.MixedModel.exists_fockMoment_slice_le`: the values decay rapidly in `x`, in the moments
  `New.Fock.fockMoment`.
* `New.Fock.MixedModel.exists_isSchwartzVector_slice_eq`: if `τ` is smooth of compact support, `u`
  is a smooth unitary family and `ξ` is a Schwartz vector, then `x ↦ τ x • realWeil (u x) ξ` is
  `x ↦ h.slice x Φ` for a Schwartz vector `Φ`.

Notions from other files:
* `New.Fock.fockSpace`: the Fock space: integrable functions c on ℂ^ι with c(x) = ∫ c(y)β(y,x)e(x−y)
  dy, e the Gaussian exp(−|x|²/2), under the L¹ norm for the measure `New.Fock.normalizedVolume` on
  ℂ^ι.
* `New.Fock.vacVector`: the Gaussian exp(−|x|²/2) regarded as an element of the Fock space.
* `New.Fock.realHeisenberg`: for signs ε, the Heisenberg datum on ℂ^ι given by the continuous
  unit-modulus bicharacter β(x,y) = exp((y*εx − x*εy)/2) = exp(i Im y*εx), where ε stands for
  `signMatrix ε`, the diagonal matrix of the signs.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.


 ## Mixed Schrödinger–Fock models and rapid decay of their values 

### `MixedModel`

 A mixed (Schrödinger–Fock) model for a decomposition `ℂ^ι' = L ℂ^p + I ℂ^ι + K ℂ^p`: a vector
`v` of the large Fock space is read as the function `a ↦ slice a v` on `ℂ^p` with values in the
small one. The Heisenberg operator of `L a' + I w + K b` translates `a` by `a'`, acts by `w`
on the value and multiplies by `exp (i Im b* (2 a + a'))`. The vacuum is `exp (-|a|²)` times
the small vacuum. 

### `MixedModel.L`

 The matrix of the directions that translate the argument in `ℂ^p`. 

### `MixedModel.K`

 The matrix of the directions that multiply by a character of `ℂ^p`. 

### `MixedModel.I`

 The matrix of the directions that act on the values, in the small Fock space. 

### `MixedModel.slice`

 The value at `a ∈ ℂ^p`: a bounded map from the large Fock space to the small one. 

### `MixedModel.exists_decomp`

 Every vector `y` is `L a + I w + K b` with `a`, `w`, `b` given by matrices applied to `y`, so
  that their norms are bounded by a multiple of that of `y`. 

### `MixedModel.slice_realHeisenbergOp`

 The Heisenberg operator of `L a' + I w + K b` translates the argument by `a'`, applies the
  operator of `w` to the value and multiplies by the phase `β (2 a + a') b`. 

### `MixedModel.slice_vac`

 The vacuum is the Gaussian `exp (-|a|²)` times the vacuum of the small space. 

### `MixedModel.exists_fockMoment_slice_le`

 Rapid decay in a mixed model: for all `N`, `M` there is a finite `C` with
`(1 + ‖a‖) ^ M * fockMoment N (slice a v) ≤ C * fockMoment (N + M) v` for all `a` and `v`. 

### `MixedModel.isSchwartzVector_slice`

 In a mixed model, each value of a Schwartz vector (one with all moments finite) is a Schwartz
vector. 

 ## Rapid sections with prescribed values 

### `realHeisenbergOp_vacVector_apply`

 The coherent state at `a`, the translate of the vacuum by `a`, takes at `w` the value of the
bicharacter at `(a, w)` times the vacuum at `w - a`, both exponentials. 

### `exists_smooth_exponent_coherent`

 Let `A x` be a smooth family of real-linear maps from `ℂ ^ ι` to `ℂ ^ ι'`. The value at `w` of
the coherent state at `A x y` (the translate `realHeisenbergOp (A x y) vacVector` of the vacuum) is
`exp q`, with `q` smooth in `((y, w), x)` and homogeneous of degree two in `(y, w)`. 

### `exists_norm_fourier_coherent_le`

 For `d` smooth of compact support and `A x` a smooth family of real-linear maps, the Fourier
transform in `x` of `d x` times the value at `w` of the coherent state
`realHeisenbergOp (A x y) vacVector` decays rapidly in `b` and `w`, with polynomial growth in `y`:
for all `M`, `n` its product with `(1 + ‖b‖) ^ M * (1 + ‖w‖) ^ n` is at most
`C * (1 + ‖y‖) ^ (2 * M + n)`. 

### `lintegral_fockMoment_realHeisenbergOp_fourier_ne_top`

 Finite moments of the superposition that `MixedModel.exists_isSchwartzVector_slice_eq`
integrates. Let `d` be smooth with compact support on `ℂ ^ p`, let `A x` be a smooth family of
real-linear maps from `ℂ ^ ι` to `ℂ ^ ι'`, let `ξ` be a Schwartz vector of the small Fock space and
`k` a continuous linear map. Put `G y x = d x • ξ y • realHeisenbergOp (A x y) vacVector` and let
`Ĝ y` be the Fourier transform of `G y` in `x`. Then for every `N` the integral over `(y, b)` of the
moment `fockMoment N (realHeisenbergOp (k b) (Ĝ y b))` is finite. 

### `realHeisenberg_β_eq_fourierChar`

 At `(x + x, -π i b)`, the bicharacter of the positive signature is the Fourier character: both
are `exp (π i ∑ₖ (xₖ b̄ₖ + x̄ₖ bₖ))`. 

### `MixedModel.exists_isSchwartzVector_slice_eq`

 Let `τ` be smooth with compact support on `ℂ ^ p`, let `u x` be elements of the unitary group
`USign ε` of the signature `ε` whose matrices depend smoothly on `x`, and let `ξ` be a Schwartz
vector of the small Fock space. Then some Schwartz vector `Φ` of the large Fock space has the value
`τ x • realWeil (u x) ξ` at every `x` in the mixed model `h`. 
