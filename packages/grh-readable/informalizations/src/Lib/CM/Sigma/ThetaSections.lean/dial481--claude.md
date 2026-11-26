---
{
  "module": "src/Lib/CM/Sigma/ThetaSections.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/ThetaSections.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/ThetaSections.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta functions of a CM elliptic curve: Weierstrass equation and spanning monomials

Let `C : New.CMLattice d` be a CM datum with lattice Λ, point t of order two and constant a₁. Let
H(l, z) = π l̄ z / area(Λ), and let σ be the sigma function of Λ. Let θ be the twisted translate of
σ by t with θ(0) = 1 and multiplier χ = `New.CMLattice.multiplier`. Write x(z) = ℘(z + t) − ℘(t),
y(z) = ½(℘′(z + t) − a₁x(z)) and G = `New.CMLattice.translatedYThetaCube`; `New.CMLattice.sections`
m is the space of theta functions for Λ, the form mH and χ^m. The file proves an addition formula
for θ and the Weierstrass equation for x, y and for σ², θ, G, shows that the monomials θ^a σ^{2b}
G^c with c ≤ 1 span the sections of each degree, and transfers the identities to the Taylor series
of x and y at 0.

## Main definitions and results

* `New.CMLattice.theta_add_mul_theta_sub`, `New.CMLattice.theta_sq`: the addition formula for
  θ(z + w)θ(z − w) with z off t + Λ, and θ² = (℘ − ℘(t))σ² off Λ.
* `New.CMLattice.deriv_translatedX_sq`, `New.CMLattice.weierstrass_equation`,
  `New.CMLattice.deriv_translatedY_eq`: off t + Λ, x′² = x(4x² + a₁²x + 4), y² + a₁xy = x³ + x and
  y′ = 1 + 3x² − a₁y.
* `New.CMLattice.translatedYThetaCube_sq_add`: G² + a₁σ²θG = σ⁶ + σ²θ⁴ everywhere.
* `New.CMLattice.comp_mul_mem_sections`, `New.CMLattice.twistedTranslate_comp_mem`: for d a
  prime ≡ 7 mod 8, sections pull back along isogenies z ↦ az, and z ↦ (T_uθ)(δ̄z) is a section of
  degree N when z ↦ δ̄z is a degree-N isogeny of C to itself and δu lies in Λ.
* `New.CMLattice.exists_mul_eq_of_mem_sections`: division by a section z ↦ (T_uθ)(az) with a ≠ 0,
  where T_u = `D.twistedTranslate 1 u` and θ belong to a CM datum D. The zeros of such a section are
  simple (`New.CMLattice.deriv_twistedTranslate_theta_comp_mul_ne_zero`).
* `New.CMLattice.monomialDeg`, `New.CMLattice.monomialSection`: the degree a + 2b + 3c of a triple
  (a, b, c) and the monomial θ^a σ^{2b} G^c.
* `New.CMLattice.sections_le_span_monomialSection`: the monomials with c ≤ 1, a + 2b + 3c = m (the
  triples in `New.CMLattice.spanningExponents` m) span the sections of degree m.

Notions from other files:
* `New.CMLattice`: A lattice `Λ` stable under the integers of `ℚ(√-d)`, with a point `t` of order
  two modulo `Λ` such that `ω t`, `ω̄ t ∉ Λ` for `ω = (1 + √-d) / 2`, scaled so that `℘''(t) = 2`,
  and a square root `a₁` of `12 ℘(t)`. The conditions on `ℚ(√-d)` and `ω` are void for `d = 0`.
* `PeriodPair.σ`: the sigma function of the lattice, a chosen odd theta function for the form H and
  the multiplier `New.sigmaSign`, with derivative 1 at 0.
* `New.sigmaSign`: The multiplier of σ: 1 at w if w/2 lies in Λ, and −1 otherwise.
* `New.IsAppellHumbert` B χ, for a form B on a lattice L: Re B is symmetric, and on L one has
  |χ| = 1 and χ(l + m) = χ(l)χ(m)·exp(πi E(m, l)), E the Riemann form of B.
* `New.CMLattice.translatedYThetaCube`: The entire function G = σ·(σ′θ − σ·(θ′ + ½a₁θ)), written as
  a pointwise product of functions.

## Relation to the literature

Known results: sigma and theta functions of a lattice, their addition formulas, the Weierstrass
equation and the elliptic functions with poles at one point are classical. See `Lib.CM.Sigma.Basic`
for the sigma function used here and for sources.


 ### The function θ: multiplier, zeros, parity and square 

### `isAppellHumbert_multiplier`

 The multiplier χ of a CM lattice satisfies the Appell–Humbert condition for the hermitian form H
of Λ. 

### `theta_mem`

 The function `θ` of a CM lattice `C` is a section of degree one, meaning a theta function for
`Λ` with hermitian form H and multiplier χ. Here `θ` is related to the sigma function σ of `Λ` by
σ² = θ²·x off t + Λ, where x(z) = ℘(z + t) − ℘(t). 

### `theta_eq_zero_iff`

 For a CM lattice `C` (a lattice `Λ` with a point `t` of order two modulo `Λ`, scaled so that
`℘''(t) = 2`), the function `C.θ` vanishes at `z` exactly when `z + t ∈ Λ`. So its zero set is the
translate `−t + Λ`. 

### `deriv_θ_ne_zero`

 The zeros of θ, the twisted translate of the sigma function by t normalised to θ(0) = 1, are
simple: where z + t lies in the lattice Λ, that is, where θ vanishes, the derivative of θ is not
zero. 

### `twistedTranslate_theta_of_mem`

 The twisted translation by a point l of the lattice Λ, θ ↦ (z ↦ exp(−H(l, z) − H(l,
l)/2)·θ(z + l)), multiplies θ by χ(l), the multiplier of θ at l. 

### `mem_sections_iff_twistedTranslate`

 A function F is a section of degree n exactly when it is entire and, for every l in the lattice
Λ, the twisted translation of degree n by l, F ↦ (z ↦ exp(−n(H(l, z) + H(l, l)/2))·F(z + l)),
multiplies F by χ(l)ⁿ, with χ the multiplier of θ. 

### `multiplier_eq_neg_sigmaSign`

 For z in Λ, the multiplier χ(z) = ±exp(2πi E(z, t)) of θ (sign + exactly when z/2 ∈ Λ), with E
the Riemann form of H, E(u, v) = Im(ū v)/area(Λ), and t the point of order two, is minus the sigma
sign of 2t + z, that is −1 if t + z/2 lies in Λ and 1 otherwise. 

### `twistedTranslate_theta_eq_neg_iff`

 For a point `l` of the lattice `Λ` of `C`, the twisted translation of degree `1` by `l` is
`(T f)(z) = exp(−π(z l̄ + |l|²/2)/A)·f(z + l)`, with `A` the area of `Λ`. It takes `C.θ` to `−C.θ`
exactly when `l/2 ≡ t` modulo `Λ`, with `t` the point of order two of `C`. 

### `sigma_add_two_t`

 The functional equation of the sigma function for the period 2t of Λ:
σ(z + 2t) = −exp(2H(t, z) + 2H(t, t))·σ(z). 

### `theta_neg`

 The function θ, the normalised translate of the sigma function of Λ by the point t of order two
of C, is even: θ(−z) = θ(z). 

### `theta_sq`

 For z outside the lattice Λ, θ(z)² = (℘(z) − ℘(t))·σ(z)², with σ the sigma function of Λ, t the
point of order two of C and θ the twisted translate of σ by t with θ(0) = 1. 

 ### The curve in the coordinates x, y, and the addition formula for θ 

### `g₃_eq`

 The invariant g₃ equals 4℘(t)³ − g₂℘(t): this is the equation ℘′² = 4℘³ − g₂℘ − g₃ at the
point t, where ℘′ vanishes. 

### `disc_eq`

 Let `C` be a CM lattice: a lattice `Λ` with a point `t` of order two modulo `Λ`, scaled so that
`℘''(t) = 2`, together with a square root `a₁` of `12 ℘(t)`. Then the discriminant g₂³ − 27g₃² of
`Λ` equals a₁⁴ − 64. 

### `translatedX_neg`

 The function `x(z) = ℘(z + t) - ℘(t)` is even, because `℘` is even and `2 t ∈ Λ`. 

### `deriv_translatedX`

 The derivative of x is 2y + a₁x, with x(z) = ℘(z + t) − ℘(t) (`translatedX`) and
y(z) = ½(℘′(z + t) − a₁x(z)) (`translatedY`). 

### `deriv_translatedY_eq`

 Let t be the point of order two of C and a₁ the chosen square root of 12℘(t). For z with z + t ∉
Λ, the derivative of y at z is 1 + 3x(z)² − a₁y(z). Here x(z) = ℘(z + t) − ℘(t) is `translatedX` and
y(z) = ½(℘′(z + t) − a₁x(z)) is `translatedY`. 

### `deriv_translatedX_sq`

 Let ℘ be the Weierstrass function of the lattice `Λ` of `C`, let `t` be its point of order two
(normalised so that ℘''(t) = 2), and let `a₁` be the chosen square root of 12℘(t). Then the function
`x(z) = ℘(z + t) - ℘(t)` satisfies the differential equation `x'² = x (4 x² + a₁² x + 4)` away from
its poles `t + Λ`. 

### `weierstrass_equation`

 For the lattice `Λ` of `C`, with Weierstrass function ℘ of `Λ`, let `t` be the point of order
two of `C` (normalised so that ℘''(t) = 2) and let `a₁` be the chosen square root of 12℘(t). If
z + t ∉ Λ, then x(z) = ℘(z + t) − ℘(t) (`translatedX`) and y(z) = ½(℘′(z + t) − a₁x(z))
(`translatedY`) satisfy the Weierstrass equation y(z)² + a₁x(z)y(z) = x(z)³ + x(z). 

### `theta_add_mul_theta_sub`

 Addition formula: if z + t ∉ Λ, then θ(z + w)θ(z − w) = θ(z)²(θ(w)² − x(z)σ(w)²) for all complex
w, where x(z) = ℘(z + t) − ℘(t) is `translatedX` and σ is the sigma function of Λ. 

### `deriv_translatedY_zero`

 The function `y = C.translatedY`, given by `y(z) = ½(℘′(z + t) − a₁(℘(z + t) − ℘(t)))` for the
point `t` of order two of the CM lattice `C`, has derivative `1` at `0`. 

### `exists_mul_sigma_sq_eq_translatedX_mul_theta_sq`

 Let `C` be a lattice `Λ` with a point `t` of order two modulo `Λ` (with the normalisations of
`CMLattice d`). Let `σ` be the sigma function of `Λ`, and let `θ` (`C.θ`) be the translate of `σ` by
`t` multiplied by an exponential factor, normalised so that `θ(0) = 1`. Then there is a constant `K`
with `K σ(z)² = x(z) θ(z)²` for all `z ∉ Λ − t`, where `x(z) = ℘(z + t) − ℘(t)`. 

### `isOpen_setOf_add_t_notMem`

 The complement of t + Λ, the set on which x and y are holomorphic, is open. 

### `mul_sigma_mul_deriv_sigma_eq_of_mul_sigma_sq_eq`

 The derivative of an identity Kσ² = xθ² that holds off t + Λ, with K a constant: off t + Λ,
2Kσσ′ = (2y + a₁x)θ² + 2xθθ′. 

### `sigma_sq_eq_translatedX_mul_theta_sq`

 Let Λ be the lattice of `C` with 2-torsion point t, σ the sigma function of Λ, θ = `C.θ`, and
x(z) = ℘(z + t) − ℘(t) the function `translatedX`. For z with z + t ∉ Λ (so that x(z) is defined),
σ(z)² = x(z)·θ(z)². 

### `translatedX_mul_translatedX_add_t`

 Let ℘ be the Weierstrass function of the lattice `Λ` of `C`, and let `t` be its point of order
two modulo `Λ`, normalised so that ℘''(t) = 2. For `x(z) = ℘(z + t) - ℘(t)`, the identity
`x(z) x(z + t) = 1` holds away from the zeros `Λ` and the poles `t + Λ` of `x`. 

### `translatedYThetaCube_eq_translatedY_mul_theta_cube`

 Let t be the point of order two of C, a₁ the chosen square root of 12℘(t), σ the sigma function
of Λ, and θ its normalised translate by t. For z with z + t ∉ Λ, the entire function
G = `translatedYThetaCube` = σ·(σ′θ − σ·(θ′ + ½a₁θ)) has the value y(z)θ(z)³. Here
y(z) = ½(℘′(z + t) − a₁(℘(z + t) − ℘(t))) is `translatedY`. 

### `sigma_sq_eq_and_translatedYThetaCube_eq`

 For z with z + t ∉ Λ, both σ(z)² = x(z)θ(z)² and G(z) = y(z)θ(z)³, with x(z) = ℘(z + t) − ℘(t),
y(z) = ½(℘′(z + t) − a₁x(z)) and G = `translatedYThetaCube`: powers of θ clear the poles of x and
y. 

### `translatedYThetaCube_sq_add`

 For all complex z, G² + a₁σ²θG = σ⁶ + σ²θ⁴, where G = `New.CMLattice.translatedYThetaCube`. This
is the curve equation y² + a₁xy = x³ + x multiplied by θ⁶, with G in the role of yθ³. 

 ### Isogenies and the multiplier of θ 

### `hermitianForm_mul_of_isIsogeny`

 Let multiplication by a map the lattice Λ of C into the lattice Λ′ of C′ with degree N, that is,
a·ā·area(Λ) = N·area(Λ′). Then the hermitian forms H of Λ and H′ of Λ′ satisfy
H′(au, av) = N·H(u, v). 

### `twistedTranslate_comp_isogeny`

 Twisted translation commutes with pull-back along an isogeny. Here the twisted translation of
degree m by y for a lattice of area A is (Tf)(z) = exp(−mπ(zȳ + |y|²/2)/A)·f(z + y). Let
multiplication by a map the lattice Λ of C into the lattice Λ′ of C′ with degree N, that is,
a·ā·area(Λ) = N·area(Λ′); then for every degree n, function G and complex number u, the twisted
translate by u, for Λ and degree nN, of z ↦ G(az) is z ↦ (T′G)(az), where T′ is the twisted
translation by au for Λ′ and degree n. 

### `multiplier_quadGen_mul`

 Let d be a prime ≡ 7 mod 8. For z in Λ and a equal to (1 + √−d)/2 or its conjugate, the
multiplier of θ at az is 1. 

### `mul_mem_or_mul_sub_t_mem`

 Let d be a prime ≡ 7 mod 8, ω = (1 + √−d)/2 and t the point of order two of C. If `z` is `ω` or
`ω̄` and `2 x ∈ Λ`, then `z x` or `z (x - t)` lies in `Λ`. 

### `multiplier_eq_canonicalMultiplier`

 Let d be a prime ≡ 7 mod 8. For z in Λ, the multiplier χ(z) is the canonical one
`New.ThetaTori.canonicalMultiplier` for multiplication by ω̄, that is χ(z) = exp(πi E(ω̄z, z)), with
ω = (1 + √−d)/2 and E the Riemann form of H. The linear map z ↦ ω̄z is written as ω̄ times the
identity map `1`. 

### `exists_int_twistedTranslate_theta_eq_neg_one_zpow`

 Let d be a prime ≡ 7 mod 8, let Λ be the lattice of `C` (stable under the ring of integers of
ℚ(√-d)) with area A, and let l ∈ Λ. Then |l|²√d/(2A) is an integer n. Moreover, the twisted
translate `C.twistedTranslate 1 l C.θ`, z ↦ exp(−π(z l̄ + |l|²/2)/A)·θ(z + l) with θ = `C.θ`, equals
(−1)ⁿθ. 

### `multiplier_mul_of_isIsogeny`

 Let C, C′ be CM data for a prime d ≡ 7 mod 8, with aΛ ⊂ Λ′ and a·ā·area(Λ) = N·area(Λ′), N
natural. For l in Λ, the multipliers χ of C and χ′ of C′ satisfy χ′(al) = χ(l)^N. 

### `comp_mul_mem_sections`

 Let C, C′ be CM data for a prime d ≡ 7 mod 8, with aΛ ⊂ Λ′ and a·ā·area(Λ) = N·area(Λ′), N
natural. If g is a section of degree k for C′, that is a theta function for Λ′ with form kH′ and
multiplier χ′^k, then z ↦ g(az) is a section of degree kN for C. 


## Monomials spanning the sections of each degree; division of sections

With θ of degree 1, σ² of degree 2 and G of degree 3 (G is the entire function equal to yθ³ off
t + Λ), the spanning result is proved by repeated division by θ.

`New.CMLattice.twistedTranslate m u` is the translation by u twisted by
exp(−m(H(u, z) + H(u, u)/2)). θ is the section of degree 1 with θ(0) = 1; it vanishes exactly on
t + Λ.


### `mem_sections_iff`

 A function F is a section of degree n exactly when it is entire and, for every l in the lattice
Λ, F(z + l) = (χ(l)·exp(H(l, z) + H(l, l)/2))ⁿ·F(z), with χ the multiplier and H the hermitian form
of C. 

### `deriv_add_of_mem_sections`

 At a zero z of a section F of degree n, the derivative obeys the same law as F: for l in the
lattice Λ, F′(z + l) = (χ(l)·exp(H(l, z) + H(l, l)/2))ⁿ·F′(z), with χ the multiplier and H the
hermitian form of C. 

### `monomialDeg`

 The degree a + 2b + 3c of a triple of exponents (a, b, c): the degree of the monomial
`New.CMLattice.monomialSection` of the triple as a section. 

### `monomialSection`

 The monomial θ^a·(σ²)^b·G^c of a triple of exponents (a, b, c).
Here σ is the sigma function of the lattice and G = `New.CMLattice.translatedYThetaCube` is the
entire function equal to yθ³ off t + Λ. The factors θ, σ², G are sections of degree 1, 2, 3. 

### `monomialSection_eq`

 For a CM lattice `C` with lattice `Λ`, Weierstrass function ℘, sigma function σ, point of order
two `t`, and constant `a₁`, let x(z) = ℘(z + t) − ℘(t) and y(z) = ½(℘′(z + t) − a₁x(z)). Let G be
the entire function equal to yθ³ off t + Λ, and let the monomial of e = (a, b, c) be θ^a·(σ²)^b·G^c,
a section of degree a + 2b + 3c. If z + t ∉ Λ, this monomial at z equals θ(z)^{a+2b+3c} x(z)^b
y(z)^c. 

### `monomialSection_mem`

 For a triple e = (a, b, c), the monomial `C.monomialSection e` = θ^a(σ²)^b G^c is a section of
degree `monomialDeg e` = a + 2b + 3c. That is, it is a theta function for the lattice Λ of `C` with
hermitian form (a + 2b + 3c)H and multiplier χ^(a+2b+3c). 

### `sections_zero_le_const`

 Every section of degree 0, that is, every entire Λ-periodic function, is constant. The right
side 1 is the unit of the semiring of subspaces of the algebra ℂ → ℂ: the constant functions. 

### `deriv_twistedTranslate_theta_comp_mul_ne_zero`

 For a ≠ 0, the zeros of z ↦ (T_uθ)(az) are simple, where T_u = `C.twistedTranslate 1 u` is the
twisted translation by u. 

### `differentiable_ite_deriv_div_deriv`

 Let f and g be entire functions such that the zeros of g are simple and f vanishes at each of
them. Then f/g, with the value f′(z)/g′(z) at a zero z of g, is entire. 

### `exists_mul_eq_of_mem_sections`

 Let g be a section of degree m of C of the form g(z) = (T_uθ)(az), where a ≠ 0, T_u =
`D.twistedTranslate 1 u`, and θ belongs to an arbitrary CM datum D, not necessarily C. A section f
of degree m + k that vanishes at every zero of g is c·g for a section c of degree k. This is stated
with c in any subspace S that contains the sections of degree k, so that a known bound on these
(`New.CMLattice.sections_zero_le_const`, or `New.CMLattice.sections_le_span_monomialSection` in its
induction) can be passed directly. 

### `monomialSection_neg_t_ne_zero`

 The monomial σ^{2b}·G^c, with G = `New.CMLattice.translatedYThetaCube`, has no factor θ and does
not vanish at the zero −t of θ. 

### `spanningExponents`

 The triples (a, b, c) with c ≤ 1 and degree a + 2b + 3c = m. 

### `mul_theta_mem_span_monomialSection`

 Multiplication by θ takes the span of the monomials θ^a σ^{2b} G^c with c ≤ 1 and
a + 2b + 3c = m into the span of those with c ≤ 1 and a + 2b + 3c = m + 1. 

### `sections_le_span_monomialSection`

 Let Λ be the lattice of `C`, with 2-torsion point t, and put x(z) = ℘(z + t) − ℘(t). A section
of degree m is a theta function for Λ with hermitian form mH and multiplier χ^m. Every section of
degree m is a complex linear combination of the functions θ^a σ^{2b} G^c with c ≤ 1 and
a + 2b + 3c = m, which are the monomials `monomialSection` of the triples in `spanningExponents m`;
here θ = `C.θ`, σ is the sigma function of Λ, and G is the entire function equal to yθ³ off t + Λ.
Off t + Λ such a monomial equals θ^m x^b y^c.

Part of Weierstrass's theorem on elliptic functions, stated for sections: a section of degree m
divided by θ^m is an elliptic function with poles of order at most m on t + Λ, hence a polynomial in
x and y.

This gives the upper bound in Frobenius's dimension formula for theta functions, in one complex
variable and for the lattice of `C` only, as spanning by explicit monomials. 

### `twistedTranslate_comp_mem`

 Let d be a prime ≡ 7 mod 8, and let Λ be the lattice of `C`, of area A. Let δ be a complex
number such that multiplication by δ̄ maps Λ into Λ with degree δδ̄ = N, and let u be a point with
δu ∈ Λ. Then z ↦ (T_uθ)(δ̄z) is a section of degree N, that is, a theta function for Λ with
hermitian form NH and multiplier χ^N; here θ = `C.θ` and T_u = `C.twistedTranslate 1 u` is (T_u
f)(z) = exp(−π(zū + |u|²/2)/A)·f(z + u). 


## Taylor series of x and y: Weierstrass equation and derivatives

The functions x (`New.CMLattice.translatedX`) and y (`New.CMLattice.translatedY`) are holomorphic
at `0`. Their Taylor series, moved to a field `K` along a ring homomorphism `ι : ℂ →+* K`
(`New.taylorVia`), satisfy the same identities as the functions.

* `New.CMLattice.taylorVia_curve_eq`: the Weierstrass equation `y² + a₁ x y = x³ + x`.
* `New.CMLattice.derivative_taylorVia_translatedX`,
  `New.CMLattice.derivative_taylorVia_translatedY`: `x' = 2 y + a₁ x` and
  `y' = 1 + 3 x² - a₁ y`.


### `derivative_taylorVia`

 The formal derivative of the Taylor series of `f` at `0`, moved to `K` along `ι`, is the Taylor
series of the derivative of `f`. 

### `taylorAtZero_congr`

 Functions that agree off `t + Λ` agree near `0`, so they have the same Taylor series at `0`. 

### `taylorAtZero_monomialSection_eq`

 The Taylor series at `0` of the monomial of `e = (a, b, c)` is
`θ ^ (a + 2 b + 3 c) x ^ b y ^ c`, formed with the Taylor series of `θ`, `x = C.translatedX` and
`y = C.translatedY`. 

### `taylorVia_curve_eq`

 The Taylor series at `0` of `x = C.translatedX` and `y = C.translatedY`, moved to `K` along
`ι`, satisfy the Weierstrass equation `y² + a₁ x y = x³ + x`. 

### `derivative_taylorVia_translatedX`

 The Taylor series at `0` of `x = C.translatedX` and `y = C.translatedY`, moved to `K` along
`ι`, satisfy `x' = 2 y + a₁ x`. 

### `derivative_taylorVia_translatedY`

 The Taylor series at `0` of `x = C.translatedX` and `y = C.translatedY`, moved to `K` along
`ι`, satisfy `y' = 1 + 3 x² - a₁ y`. 
