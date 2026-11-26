---
{
  "module": "src/Lib/SiegelWeil/OneVector/SiegelClassSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/SiegelClassSum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/SiegelClassSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Siegel–Weil for one vector, Siegel's class sum formula and the ratio of masses

This file derives Siegel's formula for representation numbers from the Siegel–Weil formula
`New.SiegelWeil.siegel_weil`. It applies that formula to the hyperbolic plane and to the positive
definite space `stdSpace E κ` with form x*x, of rank at least 3. Laplace's integral for 1/Γ supplies
the archimedean factor.

## Main definitions and results

* `New.SiegelWeil.siegel_weil_one_vector`: the mean of `∑_ξ Ψ(h⁻¹ ξ)` is `Ψ(0)` plus the sum over
  β in E⁺ of the integrals `∫ Ψ(x) ψ(β x* x / 2) dx`.
* `New.SiegelWeil.siegel_weil_fourierCoeff`: the part of this formula that counts the vectors of
  one norm α ≠ 0, detected by a phase.
* `New.normDensity`: the density at α of a function Φ₀ of finite adelic vectors, a Fourier integral
  over the self-adjoint finite adeles.
* `New.classSum_eq_mul_normDensity`: for totally positive α, the class sum (`New.classSum`) of the
  numbers of representations of α by x*x, weighted by Φ₀, is the class sum of 1 times |D_E|^(1/4),
  the factors at the infinite places and the density of Φ₀ at α.
* One step of the mass formula, with an error term: `New.abs_log_mass_ratio_sub_le` estimates the
  ratio of the masses `New.mass E (j + 1)` and `New.mass E j` of the genera of standard lattices. It
  applies Siegel's formula `New.classSum_eq_mul_normDensity` to the vectors of norm `1` in the
  standard lattice, whose class sum is `New.mass E j` by `New.classSum_card_norm_one_eq_mass`, and
  bounds the density by a Gauss sum estimate.

Notions from other files:
* `New.SiegelWeil.mixedValue`: the slice f[x], the value of a test function f at a point x in the
  Schrödinger model. The function x ↦ f[x] is called the Schrödinger function of f.
* `New.SiegelWeil.Lagrangian.zeroTerm`: the functional ev_L attached to a Lagrangian L, the value
  at 0 in a Schrödinger model along L.
* `New.classSum`: the sum of a function over the classes of a level, weighted by 1/#Aut.
* `New.mass`: the mass of the genus of O_E^l, the sum of 1/#Aut over its classes.

## Relation to the literature

Known result: Siegel's formula for representing a number by a hermitian form. Here it is stated for
the representations of a totally positive number by a sum of at least three norms over a CM field
with enough roots of unity, a splitting character and a self-dual lattice, at any level and for any
nonnegative invariant test function. The singular series is left as one adelic Fourier integral, and
the formula is read off from the Siegel–Weil formula. The local densities are not evaluated: for the
standard lattice the integral is estimated by Gauss sums and a zeta value. Source: A. Weil, Acta
Math. 113 (1965), Thm 5 for one vector; classically, C. L. Siegel, Ann. of Math. 36 (1935), and
H. Braun, Zur Theorie der hermitischen Formen, Abh. Math. Sem. Hamburg 14 (1941).

Known result: Mass formula for unimodular hermitian lattices, as the ratio of consecutive masses.
Only this ratio in large rank is obtained, up to an explicit error that depends on the field only
through its degree, for CM fields with enough roots of unity (so unramified over the real subfield),
a splitting character and a self-dual rank-one lattice. It is derived from Siegel's formula for
vectors of norm one and a Gauss sum bound. Source: W. T. Gan, J. Hanke, J.-K. Yu, On an exact mass
formula of Shimura, Duke Math. J. 107 (2001); M. Kirschmer, Definite quadratic and hermitian forms
with small class number (2016), 4.2.7, 4.2.9.


 ### The Siegel–Weil formula for the hyperbolic plane 

### `New.SiegelWeil.shearSplitting`

 The splitting of the hyperbolic plane with basis `l`, `k` in which the first frame is
`l + j⁻¹ a k`, which spans an isotropic line for `a` in `E⁺`, and the second is `k`. The complement
of the two frames is `stdSpace E Empty`, of rank 0, so its embedding `i` is `0`. Here `j` is the
purely imaginary element of the Weil data. 

### `New.SiegelWeil.eq_lagrangian_of_notMem_range_shear`

 A Lagrangian of the hyperbolic plane, that is, an isotropic line, that is none of the lines of
the `l + j⁻¹ a k` with `a ∈ E⁺` (the first frames of the `shearSplitting a`) is the line of `k`. 

### `New.SiegelWeil.zeroTerm_shearSplitting`

 Let `f` be a test function for the hyperbolic plane and `stdSpace E κ` with Schrödinger function
`Ψ`. Its zero term (the value at `0` in the Schrödinger model) along the isotropic line of
`l + j⁻¹ β k`, the frame of `shearSplitting β`, is `∫ Ψ(x) ψ(β x* x / 2) dx`, with `ψ` the standard
character `stdAddChar E`. 

### `New.SiegelWeil.siegel_weil_one_vector`

 **The Siegel–Weil formula for one vector**, for `stdSpace E κ` of rank at least 3. Let `l`, `k`
be the standard basis of the hyperbolic plane and `j` the purely imaginary element of the Weil data.
The zero terms along the isotropic lines of `l + j⁻¹ β k` (the splittings `shearSplitting β`), for
`β` in the maximal real subfield `E⁺`, are summable in operator norm. For a test function `f` with
Schrödinger function `Ψ` (slices for `hyperbolicSplitting`), the integral over the unitary quotient
(for `quotMeasure`) of the theta value of `ω(1, h) f`, which is `splitWeil (1, h) f`, equals the
total measure times the sum of `Ψ(0)` and these zero terms, which are computed in
`zeroTerm_shearSplitting`. 

 ### The vectors of one norm, detected by a phase 

### `New.exists_fundamentalDomain_real`

 With `R = E⁺` the maximal real subfield of `E`, let `ι` be the diagonal map from `R` to the
product of the real functions on the places and the self-adjoint finite adeles (`Φ v` is the
embedding at the place `v`). Then there is a bounded measurable `Ω` of volume `|D_E|^(-1/4)` such
that every point has exactly one translate by `R` in `Ω ×ˢ selfAdjointCodifferent E 1`, where
`selfAdjointCodifferent E 1` is the group of self-adjoint finite adeles in the inverse different. 

### `New.realAdele`

 An adele of the real subfield `E⁺`, given by its real components and its finite part, as a
self-adjoint adele of `E`. 

### `New.exists_isAddFundamentalDomain_realAdele`

 There are an injective additive map `ι` from `E⁺` to pairs of real components and self-adjoint
finite adeles, compatible with the diagonal embedding through `realAdele`, and a bounded set `Ω` of
real components such that `Ω ×ˢ selfAdjointCodifferent E 1` (the second factor is the inverse
different) is a fundamental domain for the image of `ι`. For self-adjoint `β`, the integral over it
of `z ↦ ψ(z β / 2)`, times `|D_E|^(1/4)`, is `1` if `β = 0` and `0` otherwise. 

### `New.star_adeleMatrix_mulVec_dotProduct`

 An adelic isometry keeps the norm of a rational vector: for `h` in the adelic unitary group and
a rational `ξ`, the vector `h⁻¹ ξ` has the norm `ξ* ξ`, read as a principal adele. 

### `New.integrable_and_integral_eq_tsum_of_fundamentalDomain`

 Unfolding over a fundamental domain `D` of a countable group `Γ` of translations, enumerated by
`e`: if `P (e i +ᵥ z) = T i (F z)` for continuous linear functionals `T i` with summable norms and
`F` is integrable on `D`, then `P` is integrable and `∫ P = ∑' i, T i (∫_D F)`. 

### `New.SiegelWeil.siegel_weil_fourierCoeff`

 **The Fourier coefficient at `α` of the Siegel–Weil formula for one vector.** Let `κ` have at
least 3 elements. Let `Ψ` be the Schrödinger function of a datum `f` on `Hom` from the hyperbolic
plane to the standard definite space `stdSpace E κ` (J = 1, the form being the sum of the norms of
the coordinates). Let `α ≠ 0` lie in `E⁺`, and for an adele `z` of `E⁺` let
`P z = ∫ Ψ(x) ψ(z (x* x - α) / 2) dx`. Then `P` is integrable. The sum of `Ψ(h⁻¹ ξ)` over the
rational `ξ` with `ξ* ξ = α` converges and is a function on the unitary quotient of `stdSpace E κ`,
and its mean is `|D_E|^(1/4) ∫ P`. The measure of `z` is Lebesgue measure at the infinite places and
gives the codifferent the volume `1`; the factor `|D_E|^(1/4)` makes the covolume of `E⁺` equal to
`1`. 

 ### The factors at the infinite places and the class sum 

### `New.normDensity`

 The density of `Φ₀` at `α`: the condition `x* x = α` is detected by the phase
`ψ_f(z (x* x - α) / 2)`, integrated over the self-adjoint finite adeles `z`. The measure of `z`
gives the codifferent the volume `1`, and that of each coordinate of `x` gives `Ô` the volume
`volÔ E`. 

### `New.SiegelWeil.exists_mixedValue_eq_gaussian_mul`

 For every Schwartz–Bruhat function `Φ₀` on the finite vectors there is a test function `f` on
`Hom` from the hyperbolic plane to `stdSpace E κ` (the space with form x*x) with the following
property. Its value `mixedValue` at the column `x`, in the Schrödinger model attached to
`hyperbolicSplitting` (the splitting with `l` the first and `k` the second basis vector), is
`exp (-∑ᵥ (x*x)ᵥ) Φ₀(x_f)`. This is a Gaussian at infinity times `Φ₀` at the finite places. 

### `New.integral_fourierChar_mul_inv_pow`

 Laplace's integral for 1/Γ: for an integer k ≥ 1 and real x ≥ 0, the integral over real z of
e^{2πixz} (1 + 2πiz)^{−(k+1)} equals x^k e^{−x} / k!. 

### `New.integral_fourierChar_mul_gaussian_pow`

 For `n ≥ 2` and `a ≥ 0`, the integral over real `t` of `𝐞 (a t)` times the `n`-th power of the
Gaussian integral `∫_ℂ exp (-(1 + 2πit) |w|²) dw` is `πⁿ aⁿ⁻¹ e^(-a) / (n-1)!`, by Laplace's
integral for 1/Γ. This is Fourier inversion for the fiber integrals of `exp (-x* x)` on `ℂⁿ`: the
sphere `x* x = a` has the mass `πⁿ aⁿ⁻¹ / (n-1)!` for the measure `dx / d(x* x)`. 

### `New.integral_gaussian_mul_stdAddChar`

 By Fubini, the integral over the adelic vectors `x` of the Gaussian times `Φ₀`, twisted by the
phase `ψ (z (x* x - α) / 2)`, with `ψ = stdAddChar E` and `z` read as an adele by `realAdele` (real
components at the infinite places, `z.2` at the finite ones), is the product over the real
components `t` of `z` of `𝐞 (α t)` times a Gaussian integral over `ℂⁿ`, times the integral over the
finite adelic vectors. Here `α` at an infinite place `v` is read as the real part of its embedding
`Φ v α` of the CM type. 

### `New.classSum_eq_mul_integral`

 Let `c` be a function on the finite unitary group `Gf E κ` of x*x that is right invariant under
a level `K` (an open subgroup of the stabilizer `K₀` of the standard lattice) and, read on the
adelic group, left invariant under the rational points `Γ`. Its class sum is the index
`stdLevelIndex K = [K₀ : K]` times its integral over the adelic quotient, for the measure
`quotMeasure`. 

### `New.classSum_eq_mul_normDensity`

 **Vectors of one norm.** Let `n = card κ ≥ 3`, let `K` be a level (an open subgroup of the
stabilizer of `Ôⁿ` in the finite adelic unitary group), `Φ₀ ≥ 0` locally constant, `K`-invariant and
of compact support, and `α ∈ E⁺` totally positive. The sum of `Φ₀(h⁻¹ x)` over the `x ∈ Eⁿ` with
`x* x = α` converges. Its class sum of level `K` (the sum over the classes, weighted by the inverse
orders of their automorphism groups) is the class sum of `1` times `|D_E|^(1/4)`, times the factors
`πⁿ τ(α)^(n-1) / (n-1)!` over the infinite places (where `τ = Φ v` is the embedding of the CM type
at the place `v`), times the density `New.normDensity` of `Φ₀` at `α`. That density is the integral
of `Φ₀(x) ψ_f(z (x* x - α) / 2)` over the finite vectors `x` and the self-adjoint finite adeles `z`,
with the codifferent of volume `1` and `Ô` of volume `volÔ E`.

This is Siegel's formula for the mean number of vectors of given norm (Weil's Siegel–Weil formula
for one vector, value by value), for the definite form `x* x` of rank at least 3 over a CM field. 

 ## Estimate for the ratio of consecutive masses 

### `New.mass_eq_mass_succ_mul_normDensity`

 Siegel's formula for the vectors of norm `1` in `L = Ô^(j+1)`, `j ≥ 2`: `mass_j` is `mass_{j+1}`
times `|D_E|^(1/4) (π^(j+1) / j!)^f` times the density of the indicator of `L` at `1` (see
`New.normDensity`). Here `mass_j` is the mass of the genus of `O_E^j`, `f` is the number of
infinite places and `rd_E` the root discriminant, so `|D_E| = (rd_E^f)²`. 

### `New.norm_sub_one_le_of_normDensity_eq`

 The density of the indicator of `L = Ôⁿ` at `1` (`New.normDensity`) is close to
`vol L = volÔ E ^ n`, with `volÔ E` the measure of `Ô`: if it is `x · vol L ≠ 0`, then
`|x - 1| ≤ 2^(-u-1)`, for `n ≥ 4 u + 12` and `8 f ≤ 2^u`, with `f` the number of infinite
places. 

### `New.abs_log_mass_ratio_sub_le`

 **Masses.** The logarithm of `mass_{j+1} / mass_j`, the ratio of the masses of the genera of
`O_E^(j+1)` and `O_E^j`, is `f log (rd_E^(j+1/2) j! / (2π)^(j+1))` up to `2 / 2^u`, for
`j ≥ 4 u + 12` and `8 f ≤ 2^u`. Here `f` is the number of infinite places and `rd_E` the root
discriminant. This is an approximate form of the mass formula for unitary groups (Shimura 1997). 
