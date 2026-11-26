---
{
  "module": "src/Lib/CM/Sigma/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sigma and Weierstrass functions, lattice invariants and lattices with complex multiplication

Let `L` be a period pair with lattice Λ, Weierstrass function ℘ and invariants g₂, g₃. The sigma
function `PeriodPair.σ` is built as an odd theta function for the form H(l, z) = (π/A)·l̄·z, where A
is the area of Λ; it differs from the classical sigma function by a factor exp(cz²). Its addition
formula and the description of the theta functions for twice the form give the duplication formula
of σ and the classical facts on ℘.

## Main definitions and results

* `New.IsAppellHumbert.theta_eq_zero_iff_mem_lattice`, `New.IsAppellHumbert.deriv_theta_ne_zero`,
  `New.IsAppellHumbert.thetaSpace_two_eq_span_pair`: a theta function f ≠ 0 for (H, χ) with
  f(0) = 0 has simple zeros exactly on Λ, and ℘f² and f² span the theta functions for (2H, χ²);
  `New.IsAppellHumbert.thetaSpace_two_eq_span` collects the three.
* `PeriodPair.σ`, `New.sigma_add_mul_sigma_sub`: for u and v outside Λ,
  σ(u + v)σ(u − v) = (℘(v) − ℘(u))σ(u)²σ(v)².
* `PeriodPair.exists_weierstrassP_eq_of_cubic`: every point of `y² = 4x³ - g₂x - g₃` is
  `(℘ z, ℘' z)`.
* `New.sigma_two_mul`: the duplication formula `σ(2z) = -℘'(z) σ(z)⁴`.
* `New.CMLattice d`: a lattice `Λ` with a point `t` of order two such that `℘''(t) = 2` and a
  square root `a₁` of `12 ℘(t)`. For `d ≠ 0` the lattice is also stable under multiplication by
  `New.quadInt d`, and neither `ω t` nor `ω̄ t` lies in it, where `ω = New.quadGen d`.
* `New.exists_lattice_eq_mul_tau`: every lattice is a(ℤτ + ℤ) with τ in the upper half plane.
* `New.g₂_eq_eisenstein`, `New.g₃_eq_eisenstein`, `New.g₂_pow_three_sub_g₃_sq_eq_discriminant`: g₂,
  g₃ and g₂³ − 27 g₃² of that lattice in terms of E₄(τ), E₆(τ) and Δ(τ).
* `New.exists_lattice_of_g₂_g₃`: conversely, every pair (a, b) with a³ − 27 b² ≠ 0 is (g₂, g₃) of a
  lattice (uniformization). The proof finds τ as a zero of a form of weight 12 that tends to 1 at
  the cusp: without a zero, its inverse would be a nonzero modular form of negative weight.

Notions from other files:
* `New.RealComplexForm.thetaSpace` Λ B χ: the entire f with f(z + l) = χ(l)·exp(B(l, z) + B(l,
  l)/2)·f(z) for l ∈ Λ. A `New.ThetaTori.LatticeForm Λ` is a form B that carries Λ in its type.
* `New.RealComplexForm.riemannForm`: the Riemann form of B, E(u, v) = Im(B(u, v) − B(v, u))/(2π).
* `New.IsAppellHumbert`: Appell–Humbert data: Re B is symmetric, and on Λ one has |χ| = 1 and
  χ(l + m) = χ(l)χ(m)·exp(πi E(m, l)).

## Relation to the literature

Known result: Sigma and theta functions of a lattice, their addition and doubling formulas, and
uniformisation. Here sigma is the odd section of a canonical factor of automorphy rather than a
product, and the origin is moved to a point of order two. Uniformisation comes from the vanishing of
modular forms of negative weight. Source: J. Silverman, The Arithmetic of Elliptic Curves, VI, and
Advanced Topics (1994), I.5; A. Weil, Elliptic Functions according to Eisenstein and Kronecker
(1976); for uniformisation, A. Sutherland, 18.783 Lecture 15 (2023), Cor. 15.12.



## The sigma function of a lattice and its addition formula

The sigma function is not defined by the Weierstrass product.


### `PeriodPair.eq_of_eq_off_lattice`

 Two entire functions `f` and `g` that agree off the translate `-t + L.lattice` of the lattice
of `L` agree everywhere. 

### `PeriodPair.area`

 The area of the period parallelogram spanned by `ω₁` and `ω₂`. 

### `PeriodPair.hermitianForm`

 The hermitian form (l, z) ↦ (π/A)·l̄·z on ℂ, A the area of the lattice of L, as a map
real-linear in l and complex-linear in z. 

### `PeriodPair.IsIsogeny`

 Multiplication by a maps the lattice of L into that of M, and a·ā·area(L) = N·area(M). For a ≠ 0
this says that multiplication by a is an isogeny of degree N from L to M. 

### `sigmaSign`

 The multiplier of the sigma function: `1` on twice the lattice, `-1` elsewhere. 

### `riemannForm_hermitianForm`

 The Riemann form of the hermitian form (π/A)·l̄z of a period lattice of area A takes (u, v)
to Im(ūv)/A. 

### `exists_riemannForm_periods_eq_sign`

 For some `k = ±1` the Riemann form of `L.hermitianForm` takes the value `k` at the two
periods. 

### `isAppellHumbert_hermitianForm`

 The form H(l, z) = (π/A)·l̄·z and the multiplier `New.sigmaSign` are Appell–Humbert data
for the lattice. 

### `exists_isIsogeny_of_mul_mem_lattice`

 If multiplication by the complex number a maps the lattice of L into the lattice of M, then
a·ā·area(L) = N·area(M) for some natural number N. 

### `instance : IsPosRiemann L.hermitianForm`

 The Riemann form `E` of `L.hermitianForm` is positive: `E(u, iu) > 0` for every `u ≠ 0`. 

### `riemannForm_periods_mul_eq_sub`

 Expansion of `w` in the periods through the Riemann form `E` of `L.hermitianForm`:
`E(ω₁, ω₂) w = E(w, ω₂) ω₁ - E(w, ω₁) ω₂`. 

### `addSubgroupOf_dualLattice_nsmul_eq_range`

 Let `Λ` be the lattice of the period pair `L`, with covolume `A`, and let `H = L.hermitianForm`
be the hermitian form `(l, z) ↦ (π / A) · l̄ · z`. For `m ≠ 0`, `Λ` is `m` times the dual lattice of
`m H`, that is, of the points `v` at which the Riemann form of `m H` is integral against every
`l ∈ Λ`. Both sides are read as subgroups of that dual lattice. 

### `IsAppellHumbert.finrank_thetaSpace_nsmul`

 For Appell–Humbert data `(H, χ)` with `H = L.hermitianForm` and `m ≠ 0`, the theta functions
for `(m H, χ ^ m)` form a space of dimension `m`.

This is Frobenius's dimension formula for theta functions, in one variable. 

### `_root_.PeriodPair.weierstrassPMulSq`

 The function `℘ f²` for the lattice of `L`, given the value `f′²` at the lattice points,
where `℘` has its poles. 

### `_root_.PeriodPair.weierstrassPMulSq_of_notMem`

 Off the lattice the value of `℘ f²` is the product of `℘` and `f²`. 

### `differentiable_weierstrassPMulSq`

 For an entire function `f` vanishing at every point of the period lattice of `L`, the function
`L.weierstrassPMulSq f` is entire. This function equals `℘ f²` off the lattice and takes the value
`f′(l)²` at each lattice point `l`, where `℘` has its poles. 

### `theta_eq_zero_of_mem_lattice`

 A theta function that vanishes at `0` vanishes on the lattice. 

### `weierstrassPMulSq_mem_thetaSpace`

 If `f` is a theta function for `(H, χ)` with `f 0 = 0`, then `℘ f²` is a theta function for
`(2 H, χ²)`. Here `H` is `L.hermitianForm`. 

### `linearIndependent_sq_weierstrassPMulSq`

 If an entire function `f ≠ 0` vanishes on the lattice, then `f²` and `℘ f²` are linearly
independent. 

### `IsAppellHumbert.thetaSpace_two_eq_span_pair`

 For Appell–Humbert data `(H, χ)` with `H = L.hermitianForm` and a theta function `f ≠ 0` with
`f 0 = 0`, the functions `℘ f²` (`L.weierstrassPMulSq f`) and `f²` span the theta functions for
`(2 H, χ²)`. 

### `IsAppellHumbert.weierstrassPMulSq_ne_zero`

 For Appell–Humbert data `(L.hermitianForm, χ)` and a theta function `f ≠ 0` with `f 0 = 0`,
the functions `℘ f²` and `f` have no common zero. 

### `IsAppellHumbert.theta_eq_zero_iff_mem_lattice`

 For Appell–Humbert data `(L.hermitianForm, χ)`, the zeros of a theta function `f ≠ 0` with
`f 0 = 0` are the lattice points. 

### `IsAppellHumbert.deriv_theta_ne_zero`

 For Appell–Humbert data `(L.hermitianForm, χ)`, a theta function `f ≠ 0` with `f 0 = 0` has
simple zeros at the lattice points. 

### `IsAppellHumbert.thetaSpace_two_eq_span`

 Let `(H, χ)` be Appell–Humbert data with `H = L.hermitianForm` (see `New.IsAppellHumbert`) and
`f ≠ 0` a theta function for them with `f 0 = 0`. The theorem combines three facts: the zeros of `f`
are the lattice points, they are simple, and `℘ f²` and `f²` span the theta functions for
`(2 H, χ²)`. 

### `comp_neg_mem_thetaSpace`

 If `f` is a theta function for `L.hermitianForm` and `sigmaSign L`, then so is `z ↦ f (-z)`. 

### `theta_half_period_eq_neg`

 For `l = m ω₁ + ω₂`, a theta function `f` for `L.hermitianForm` and `sigmaSign L` satisfies
`f (l / 2) = -f (-l / 2)`. 

### `not_even_of_mem_thetaSpace`

 A theta function `f ≠ 0` for `L.hermitianForm` and the multiplier `sigmaSign L` is not even. 

### `sub_comp_neg_ne_zero_of_mem_thetaSpace`

 For a theta function `f ≠ 0` for `L.hermitianForm` and the multiplier `sigmaSign L`, the
function `z ↦ f z - f (-z)` is not zero. 

### `exists_odd_mem_thetaSpace_deriv_eq_one`

 There is an odd theta function with derivative `1` at `0` for `L.hermitianForm` and the
multiplier `sigmaSign L` (`1` on twice the lattice, `-1` elsewhere): an entire `f` with `f
(z + l) = sigmaSign L l * exp (H l z + H l l / 2) * f z` for lattice points `l`. Here `H` is
`L.hermitianForm`, the form `H l z = (π / A) * conj l * z` with `A` the area of the lattice.

Classically this follows from the quasi-periodicity of the Weierstrass sigma function and Legendre's
relation: every lattice has an odd entire function with derivative 1 at 0 satisfying the normalised
transformation law. 

### `_root_.PeriodPair.σ`

 The sigma function of `L`: an odd theta function for `L.hermitianForm` and the multiplier
`sigmaSign L`, with derivative `1` at `0`. 

### `sigma_add_of_mem_lattice`

 The functional equation of the sigma function: for a lattice point `l` and
`H = L.hermitianForm`, `σ (z + l) = sigmaSign L l * exp (H l z + H l l / 2) * σ z`. 

### `sigma_eq_zero_iff`

 The sigma function `L.σ` of `L` vanishes at `z` if and only if `z` lies in the period lattice of
`L`. 

### `deriv_sigma_ne_zero`

 At every point `z` of the period lattice of `L`, the derivative of the sigma function `L.σ` is
non-zero, so the zeros of `L.σ` are simple. 

### `thetaSpace_two_eq_span_sigma`

 Let H be the hermitian form (π/A)·l̄·z of the lattice of L, of area A, and χ the multiplier of σ
(1 on twice the lattice, −1 elsewhere). The entire function `℘ σ²` (`weierstrassPMulSq`) and σ²
span the theta functions for (2H, χ²). 

### `sigma_add_mul_sigma_sub_mem_thetaSpace`

 For every v the function z ↦ σ(z + v)σ(z − v) is a theta function for twice the hermitian form
of the lattice and the square of the multiplier of σ. 

### `sigma_add_mul_sigma_sub`

 The addition formula of the sigma function: for `u` and `v` off the lattice,
`σ (u + v) σ (u - v) = (℘ v - ℘ u) σ(u)² σ(v)²`. 


## Points of the Weierstrass cubic and derivatives of ℘

* `New.deriv_derivWeierstrassP`: `℘'' = 6 ℘² - g₂/2` off the lattice.


### `PeriodPair.exists_weierstrassP_eq_of_cubic`

 Every complex solution (x, y) of y² = 4x³ − g₂x − g₃ is (℘(z), ℘′(z)) for some z outside the
lattice of L. 

### `New.sigma_two_mul`

 Duplication formula for the sigma function σ of L: for z outside the lattice,
σ(2z) = −℘′(z)·σ(z)⁴. 

### `New.deriv_derivWeierstrassP`

 The second derivative of the Weierstrass function ℘ of L: for z outside the lattice,
℘′′(z) = 6℘(z)² − g₂/2. 


## Lattices with complex multiplication and their coordinates

* `New.CMLattice.translatedX`, `New.CMLattice.translatedY`: the coordinates
  `x = ℘(z + t) - ℘(t)` and `y = (℘'(z + t) - a₁ x) / 2`.


 ### Taylor series 

### `taylorAtZero`

 The Taylor series ∑ f⁽ⁿ⁾(0) zⁿ/n! at 0 of a function f : ℂ → ℂ, as a formal power series. 

### `taylorVia`

 The Taylor series of f at 0 with the ring homomorphism ι : ℂ → K applied to its
coefficients. 

### `linearSeries`

 The linear form ∑ c_i z_i, as a power series in the variables z_i. 

 ### Lattices with complex multiplication 

### `quadGen`

 The complex number ω = (1 + i√d)/2. 

### `quadInt`

 The image in ℂ of the ring of integers of K = ℚ(i√d), as a subring of ℂ. 

### `CMLattice`

 A lattice `Λ` with a point `t` of order two modulo `Λ`, scaled so that `℘''(t) = 2`, and a
square root `a₁` of `12 ℘(t)`. If `d ≠ 0`, then moreover `Λ` is stable under the ring of integers of
`ℚ(√-d)`, and neither `ω t` nor `ω̄ t` lies in `Λ`, where `ω = (1 + √-d) / 2`. For `d = 0` these two
conditions are void. 

### `CMLattice.t`

 The point `t`, of order two modulo the lattice. 

### `CMLattice.a₁`

 A square root of `12 ℘(t)`. 

### `CMLattice.g₂_eq`

 The scaling of the lattice: `g₂ = 12 ℘(t)² - 4`, which says `℘''(t) = 2` because
  `℘'' = 6 ℘² - g₂ / 2` off the lattice. 

### `CMLattice.mul_mem_of_quadInt`

 If `d ≠ 0`, the lattice is stable under the ring of integers of `ℚ(√-d)`. 

### `CMLattice.two_t_mem`

 `2 t` lies in the lattice. 

### `CMLattice.t_notMem`

 `t` does not lie in the lattice. 

### `CMLattice.quadGen_mul_t_notMem`

 If `d ≠ 0`, neither `ω t` nor `ω̄ t` lies in the lattice, where `ω = (1 + √-d) / 2`. 

### `CMLattice.a₁_sq`

 `a₁² = 12 ℘(t)`. 

 ### Sections and the functions θ, x, y 

### `Λ`

 The period lattice Λ ⊂ ℂ of `C`. 

### `twistedTranslate`

 The twisted translation T of degree m by the point y, for the form mH with
H = `C.hermitianForm`: (T f)(z) = exp(−mπ(zȳ + |y|²/2)/A)·f(z + y), A the area of Λ. 

### `multiplier`

 The multiplier χ : l ↦ ±exp(2πi E(l,t)), with sign + exactly when l/2 ∈ Λ, and E the Riemann
form of H = `C.hermitianForm`. 

### `sections`

 The sections of degree m: theta functions for the lattice Λ with hermitian form mH and
multiplier χ^m. 

### `θ`

 The function z ↦ (T_tσ)(z)/(T_tσ)(0): the twisted translate of the sigma function by the
2-torsion point t, normalised to 1 at 0. 

### `translatedX`

 The function x(z) = ℘(z + t) − ℘(t) for the lattice Λ and its 2-torsion point t. 

### `translatedY`

 The function y(z) = ½(℘′(z + t) − a₁x(z)), where x(z) = ℘(z + t) − ℘(t). 

### `translatedYThetaCube`

 The entire function G = σ·(σ′θ − σ·(θ′ + ½a₁θ)), written as a pointwise product of functions. It
equals yθ³ off t + Λ, with y = `C.translatedY`. 

### `translatedY_zero`

 The function `y = C.translatedY`, given by `y(z) = ½(℘′(z + t) − a₁(℘(z + t) − ℘(t)))`, vanishes
at `0`, since `℘'` vanishes at the point `t` of order two. 


## The invariants g₂, g₃, Δ and lattices with given invariants

* `New.weierstrass_disc_ne_zero`: g₂³ − 27 g₃² ≠ 0, because Δ has no zero.


### `area_eq_norm_sq_mul_abs_im`

 The area of the period parallelogram is |ω₂|²·|Im(ω₁/ω₂)|. 

### `riemannZeta_six_eq`

 The special value ζ(6) = π⁶/945. 

### `exists_lattice_eq_mul_tau`

 Every period lattice is a(ℤτ + ℤ) with a ≠ 0 and τ in the upper half plane: e enumerates it by
(m, n) ↦ a(mτ + n). The area of its period parallelogram (`PeriodPair.area`) is then |a|² Im τ. 

### `G_eq_riemannZeta_mul_eisenstein`

 If the lattice of L is a(ℤτ + ℤ), enumerated by e, then for k ≥ 3 the lattice sum `L.G k` of the
k-th inverse powers is 2ζ(k)E_k(τ)/aᵏ, where E_k is the normalised Eisenstein series of weight k. 

### `g₂_eq_eisenstein`

 If the lattice of L is a(ℤτ + ℤ), enumerated by e, then g₂ = (2π/a)⁴ E₄(τ)/12, where E₄ is the
normalised Eisenstein series of weight 4. 

### `g₃_eq_eisenstein`

 If the lattice of L is a(ℤτ + ℤ), enumerated by e, then g₃ = (2π/a)⁶ E₆(τ)/216, where E₆ is the
normalised Eisenstein series of weight 6. 

### `g₂_pow_three_sub_g₃_sq_eq_discriminant`

 If the lattice of L is a(ℤτ + ℤ), enumerated by e, then g₂³ − 27 g₃² = (2π/a)¹² Δ(τ), where Δ
is the modular discriminant. 

### `exists_g₂_g₃_eq_pow_mul_eisenstein`

 For τ in the upper half plane and w ≠ 0 some period lattice has the invariants
g₂ = w⁴E₄(τ)/12 and g₃ = w⁶E₆(τ)/216. The proof uses the lattice (2π/w)(ℤτ + ℤ). 

### `exists_lattice_of_E₄_cube_mul_eq`

 If a³ − 27b² ≠ 0 and E₄(τ)³·(a³ − 27b²) = (12a)³·Δ(τ) at a point τ of the upper half plane,
then some period lattice has g₂ = a and g₃ = b. 

### `exists_eq_zero_of_weight_twelve_of_tendsto_one`

 A modular form `g` of weight 12 for the full modular group (`𝒮ℒ`, the image of SL₂(ℤ) in
GL₂(ℝ)) that tends to 1 at the cusp `i∞` has a zero in the upper half plane. 

### `tendsto_E₄_atImInfty`

 The Eisenstein series E₄ tends to 1 at the cusp i∞. 

### `exists_lattice_of_g₂_g₃`

 For complex numbers a, b with a³ − 27b² ≠ 0 there is a period lattice L with Weierstrass
invariants g₂(L) = a and g₃(L) = b.
This is the existence part of the uniformisation theorem for elliptic curves over ℂ. 
