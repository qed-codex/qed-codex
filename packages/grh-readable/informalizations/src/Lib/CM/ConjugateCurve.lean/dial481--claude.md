---
{
  "module": "src/Lib/CM/ConjugateCurve.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/ConjugateCurve.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/ConjugateCurve.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Galois conjugates of CM curves: conjugate sections, isogenies and translates of θ

Let `σ` be a field automorphism of `ℂ`, and let `C`, `C'` be CM data (`New.CMLattice`) with
`C'.a₁ = σ C.a₁`, so that their cubics y² + a₁xy = x³ + x are conjugate under `σ`. Write `θ`, `θ'`
for their theta functions, and `New.taylorVia σ f` for the Taylor series of `f` at 0 with `σ`
applied to its coefficients. The bare letter `σ` is the automorphism, while `C.σ` is the sigma
function of the lattice of `C`. For `σ ∈ Aut(ℂ/K)` with `K = ℚ(√-d)` (`quadInt d` is the image of
`𝓞_K` in `ℂ`, fixed by `σ`), a conjugate CM datum exists, and conjugation extends to isogenies and
to translates of `θ`; this is a step towards `New.CMLattice.complex_multiplication_theta`.

## Main definitions and results

* `New.thetaQuotient`: the quotient `θ' / σ θ` of power series, by which the theta functions differ.
* `New.taylorAtZero_monomialSection`, `New.exists_conjugate_section`: monomial sections, and hence
  all sections `f` of degree `m` of `C`, have conjugates with Taylor series `(θ' / σ θ) ^ m * σ f`;
  the second lemma transports points as well.
* `New.CMLattice.exists_galConjugate_of_g₂_g₃`, `New.CMLattice.galConjugate`: a lattice with the
  invariants `σ g₂`, `σ g₃` carries a CM datum with the number `σ a₁`, and one such datum is chosen.
* `New.CMLattice.thetaQuotient_eq_one`, `New.CMLattice.taylorAtZero_theta_eq_taylorVia`: for a CM
  datum `D` with invariant `σ a₁`, the Taylor series of the theta function is the conjugate of that
  of `θ`.
* `New.CMLattice.exists_taylorVia_twistedTranslate_theta`: when the lattice of `C` is `Ω 𝓞_K` and
  `S` is a finite subset of `K`, there is a period `v` of `D` such that, for all `s ∈ S`, the Taylor
  series of the translate by `s v` of the theta function of `D` is the conjugate of that of the
  translate of `θ` by `s Ω`.

Notions from other files:
* `New.CMLattice.θ`: The twisted translate (`twistedTranslate 1 u f` is
  `z ↦ exp(−π(zū + |u|²/2)/area Λ) f(z + u)`) of the sigma function `C.σ` by the point t of order
  two, normalised to 1 at 0; it vanishes exactly on t + Λ.
* `New.CMLattice.translatedX`, `New.CMLattice.translatedY`: The coordinates x(z) = ℘(z + t) − ℘(t)
  and y(z) = ½(℘′(z + t) − a₁x(z)) of the curve.
* `New.CMLattice.sections`: The sections of degree m: theta functions for the lattice Λ with
  hermitian form mH and multiplier χ^m, for the hermitian form H and multiplier χ of `θ`.
* `PeriodPair.IsIsogeny`: L.IsIsogeny M a N says that a maps the periods of L to those of M and that
  a·ā·area(L) = N·area(M).
* `New.CMLattice.monomialSection`: For j = (a, b, c), the section θ^a·(C.σ²)^b·G^c of degree
  a + 2b + 3c, with C.σ the sigma function and G = `New.CMLattice.translatedYThetaCube`.

## Relation to the literature

Part of a known result: Main theorem of complex multiplication for elliptic curves, soft form. See
`Lib.CM.ChowlaSelberg`. No reciprocity law is used: the conjugate lattice comes from uniformisation,
and points are matched by transporting sections.



## Transport of sections and points to a conjugate curve

The series of `x` and `y` are conjugate because they solve the same differential system.


### `thetaQuotient`

 The power series θ′/σθ: the Taylor series of the theta function of C' times the inverse of
the σ-conjugate of that of C. 

### `map_taylorAtZero_translatedX_and_translatedY`

 For CM lattices `C`, `C'` and a ring automorphism `σ` of `ℂ` with `C'.a₁ = σ C.a₁`, the Taylor
series at 0 of `C'.translatedX` and `C'.translatedY` are obtained from those of `C` by applying `σ`
to the coefficients. Here `translatedX` is x(z) = ℘(z + t) − ℘(t) and `translatedY` is
y(z) = ½(℘′(z + t) − a₁x(z)), with ℘ the Weierstrass function of the lattice and `t` its point of
order two. 

### `taylorAtZero_monomialSection`

 Let the invariant `a₁` of the CM datum `C'` be the conjugate of that of `C` by the automorphism
`σ` of `ℂ`. For exponents `j = (a, b, c)`, the Taylor series of the monomial section
`θ' ^ a * (C'.σ ^ 2) ^ b * C'.translatedYThetaCube ^ c` of `C'` is the conjugate of the series of
that of `C` times `(θ' / σ θ) ^ (a + 2 b + 3 c)`, where `θ' / σ θ` is `New.thetaQuotient`. 

### `exists_conjugate_factor_of_mem`

 The case `θ' z = 0` of `exists_conjugate_point`: if `z` is congruent to the point `t` of `C'`,
the values at `z` of `θ'`, `C'.σ ^ 2` and of the entire function `translatedYThetaCube` = `yθ'³` are
`μ`, `μ²`, `μ³` times the `σ`-conjugates of those of `C` at its point `t`, for some `μ ≠ 0`. 

### `exists_conjugate_point_of_notMem`

 The case `θ' z ≠ 0` of `exists_conjugate_point`, where `θ'` is the theta function `C'.θ`: let
`σ` be an automorphism of `ℂ`, let `C`, `C'` be CM lattices with `C'.a₁ = σ C.a₁`, and let `z`
satisfy `z + C'.t ∉ C'.Λ`, i.e. `z` is not congruent to the point `t` of order two of `C'`. Then for
some `u` and some `μ ≠ 0`, the values at `z` of `C'.θ`, `C'.σ ^ 2` (the sigma function squared) and
`C'.translatedYThetaCube` (equal to `yθ³` off `t + Λ`, with `y` = `translatedY`) are `μ`, `μ²`, `μ³`
times the `σ`-images of the corresponding values for `C` at `u`. 

### `exists_conjugate_point`

 Let the invariant `a₁` of the CM datum `C'` be the `σ`-conjugate of that of `C`. A point `z` of
`C'` has a matching point `u` of `C`: the values at `z` of the generators `θ'` (the theta function
of `C'`), `C'.σ ^ 2` (the square of the sigma function of the lattice) and `C'.translatedYThetaCube`
(the entire function `yθ'³`) are the conjugates of the values at `u` of those of `C`, up to factors
`μ`, `μ²`, `μ³` with `μ ≠ 0`. If `θ'` vanishes at `z`, then `u` is the point `t` of order two
of `C`. 

### `exists_conjugate_section`

 If the invariant `a₁` of `C'` is the `σ`-conjugate of that of `C`, a point `z` of `C'` has a
matching point `u` of `C` and a factor `μ ≠ 0`: every section `f` of degree `m` of `C` (a theta
function for its lattice) has a conjugate section `g` of `C'`, with Taylor series
`(θ' / σ θ) ^ m * σ f`, where `θ' / σ θ` is `New.thetaQuotient`, and value `g z = μ ^ m * σ (f u)`.
If `θ'` vanishes at `z`, then `u` is the point `t` of order two of `C`. 

 ### Conjugate isogenies 

### `exists_conj_isogeny_sections`

 Let `σ` be an automorphism of `ℂ` over `ℚ(√-d)`, with `d` a prime `≡ 7 (mod 8)`. Let `a` be an
isogeny from `C` to `D` of degree `N`, that is `a Λ_C ⊆ Λ_D` and `|a|² area C = N area D`. Let `C'`,
`D'` be CM data for any `d'` whose invariants `a₁` (square roots of `12 ℘(t)`) are the
`σ`-conjugates of those of `C`, `D`. There are sections `A`, `B` of `C'` (theta functions for its
lattice) of degrees `2 N`, `N`, corresponding to the sections `D.σ (a * z) ^ 2` and `D.θ (a * z)` of
`C`. They have the values 0 and 1 at 0. `A` vanishes at the point `t` of order two of `C'` only if
`a` takes the point `t` of `C` to a period of `D`. The series of `B` is `(θ' / σ θ) ^ N` (see
`New.thetaQuotient`) times the conjugate series of `D.θ (a * z)`. And `A / B ^ 2` is
`D'.σ ^ 2 / D'.θ ^ 2` taken at `σ a * z`. 

### `conj_isogeny_mul_mem_lattice`

 Let `a` be an isogeny of degree `N` from `C` to `D` (it maps periods to periods and
`a * conj a * area C = N * area D`), and let the invariants `a₁` of `C'`, `D'` be the
`σ`-conjugates of those of `C`, `D`, for `σ` an automorphism of `ℂ` over `ℚ(√-d)`. Then `σ a`
takes periods of `C'` to periods of `D'`. 

### `mul_t_mem_of_conj_isogeny_mul_t_mem`

 Let `a` be an isogeny of degree `N` from `C` to `D`, and let the invariants `a₁` of `C'`, `D'`
be the `σ`-conjugates of those of `C`, `D`. If `σ a` takes the point `t` of order two of `C'` to a
period of `D'`, then `a` takes the point `t` of `C` to a period of `D`. 

### `map_eq_self_of_mem_quadInt`

 An automorphism of `ℂ` over `K` fixes the elements of `quadInt d`, the image of `𝓞_K` in `ℂ`. 

 ### The conjugate CM datum 

### `exists_galConjugate_of_g₂_g₃`

 Let `d` be a prime `≡ 7 (mod 8)` and `K = ℚ(√-d)`. A CM datum is a lattice stable under `𝓞 K`
with a point `t` of order two such that neither `ω t` nor `ω̄ t` lies in it (`ω = (1 + √-d)/2`),
scaled so `℘''(t) = 2`, and with a square root `a₁` of `12 ℘(t)`. For a CM datum `C` and an
automorphism `σ` of `ℂ` over `K`, every lattice `L` whose invariants are `σ C.g₂` and `σ C.g₃`
carries a CM datum whose `a₁` is `σ C.a₁`. 

### `exists_galConjugate`

 For a CM datum `C` with `d` a prime `≡ 7 (mod 8)` and an automorphism `σ` of `ℂ` over
`K = ℚ(√-d)` there is a CM datum whose number `a₁` is the conjugate `σ C.a₁` of that of `C`.
The proof takes the lattice with the invariants `σ g₂`, `σ g₃`. 

### `galConjugate`

 The conjugate curve: a chosen CM lattice whose number `a₁` is `σ C.a₁`, see
`New.CMLattice.galConjugate_a₁`. 

### `galConjugate_a₁`

 For `d` a prime `≡ 7 mod 8` and `σ` an automorphism of `ℂ` fixing `QuadField d = ℚ(√-d)`, the
Galois conjugate `C.galConjugate σ` of a CM lattice `C` has number `a₁` equal to `σ C.a₁`. Here `a₁`
is the chosen square root of `12 ℘(t)`, for `t` the 2-torsion point of `C`. 

 ### The theta function of a conjugate datum 

### `CMLattice.exists_eq_const_mul_twistedTranslate_theta`

 A section is fixed by its zeros up to a constant. Let `a ≠ 0` and let `g(z) = (T_u θ)(a z)`,
with `θ` and the twisted translation `T_u` formed for a CM datum `E`, be a section of degree `m` of
`C`. A section `f` of degree `m` of `C` that vanishes at the zeros of `g` is a constant multiple of
`g`. 

### `rescale_thetaQuotient_of_conj_isogeny`

 Let `a ≠ 0` be an isogeny from `C` to `D` of degree `N`, let the invariants `a₁` of `C'`, `D'`
be the `σ`-conjugates of those of `C`, `D`, and let `σ a` be an isogeny from `C'` to `D'` of
degree `N` (the classes `PrimeSevenModEight` say that `d`, `d'` are primes ≡ 7 mod 8). Then the
quotient `θ' / σ θ` of Taylor series of theta functions (`thetaQuotient`) for `D` and `D'`, taken
at `σ a * z`, is the `N`-th power of that for `C` and `C'`. 

### `one_lt_norm_quadGen`

 For a prime `d ≡ 7 (mod 8)` the number `ω = (1 + i√d) / 2` has modulus greater than 1. 

### `thetaQuotient_eq_one`

 Let `d` be a prime `≡ 7 (mod 8)` and `σ` an automorphism of `ℂ` over `ℚ(√-d)`. Let `C`, `D` be
CM lattices, each a lattice stable under `𝓞_K` with a point `t` of order two scaled so that
`℘''(t) = 2`, a square root `a₁` of `12 ℘(t)`, and a theta function. If `D.a₁ = σ C.a₁`, the Taylor
series of the theta function of `D` is the `σ`-conjugate of that of `C`: the quotient `θ' / σ θ` is
1. 

### `taylorAtZero_monomialSection_eq_taylorVia`

 If `D.a₁ = σ C.a₁` for an automorphism `σ` of `ℂ` over `K`, the Taylor series at 0 of every
monomial section of `D` is the `σ`-conjugate of that of `C`. 

### `taylorAtZero_theta_eq_taylorVia`

 If `D.a₁ = σ C.a₁` for an automorphism `σ` of `ℂ` over `K`, the Taylor series at 0 of the
theta function of `D` is the `σ`-conjugate of that of `C`. 

 ### Translates of θ by torsion points 

### `twistedTranslate_add_self_apply_neg`

 The twisted translate of `θ` by `u + u` takes the value `θ u` at `-u`. 

### `twistedTranslate_add_self_apply_zero`

 If `θ u = 0`, the twisted translate of `θ` by `u + u` takes the value `-1` at 0. 

### `twistedTranslate_theta_add_two_mul`

 Let `N u` be a period of `C` for a natural number `N`, and let `l` be a period. Then the
twisted translate `z ↦ exp (-π (z ū + |u|² / 2) / area Λ) * θ (z + u)` of the theta function by the
point `u + 2 N l` is its twisted translate by `u`. 

### `twistedTranslate_theta_eq_of_isIntegral`

 Let `e` and `m` be nonzero natural numbers such that `Ω e` and `m s Ω` are periods of `C`, and
let `(s' - s) / (2 m e)` be integral. Then the translate of `θ` by `s' Ω` is its translate by
`s Ω`. 

### `twistedTranslate_theta_comp_intCast_mul_mem`

 Let `n` be an integer with `n s ∈ 𝓞_K`, and let `v` be a period of `C`. The translate of
`θ` by `s v`, taken at `n z`, is a section of degree `n²`. 

### `exists_forall_apply_mul_eq_pow_mul`

 Suppose that for all `m`, every section `f` of `D` of degree `m` has a `σ`-conjugate section of
`C` with value `μ ^ m * σ (f u')` at `u`, `σ` being an automorphism of `ℂ` over `K`. Then for
`a ∈ quadInt d` there is one `N` such that, for all `m` and all such `f`, every entire function with
Taylor series conjugate to that of `f` takes the value `μ ^ (m N) * σ (f (a u'))` at `a u`. 

### `apply_mul_eq_zero_iff_of_transport`

 In the situation of `exists_forall_apply_mul_eq_pow_mul` (each section `f` of degree `m` of `D`
gives a section of `C` with conjugate series and value `μ ^ m * σ (f u')` at `u`; `a ∈ quadInt d`)
let `μ ≠ 0`. If the Taylor series of the entire function `g` is conjugate to that of the section `f`
of `D`, then `g` vanishes at `a u` exactly when `f` vanishes at `a u'`. 

### `exists_quadInt_of_twistedTranslate_theta_eq_zero`

 If `n ≠ 0`, the lattice of `C` is `2 n² w 𝓞_K` and the translate of `θ` by `2 n² s w` vanishes
at `n z`, then `z = (b - 2 n s) w` for some `b ∈ quadInt d`. 

### `eq_one_of_taylorVia_twistedTranslate_theta`

 `sections m` are the theta functions with form `m H` and multiplier `χ^m`;
`twistedTranslate m y f` is `z ↦ exp(−mπ(zȳ + |y|²/2)/A) f(z + y)`, `A` the area of `Λ`; `quadInt d`
is the image of `𝓞_K` in `ℂ`. Suppose the Taylor series of `C.θ` at 0 is the `σ`-conjugate of that
of `D.θ`. Suppose also that each degree-`m` section `f` of `D` gives a section `g` of `C` with
conjugate series and `g w = μ^m σ(f w')`, where `μ ≠ 0`. Let `n s ∈ quadInt d` and `2 n² w' ∈ D.Λ`.
If `c` times the degree-1 translate of `C.θ` by `s 2n² w`, at `n z`, is a degree-`n²` section whose
series is the conjugate of that of the translate of `D.θ` by `s 2n² w'` at `n z`, then `c = 1`. 

### `exists_taylorVia_twistedTranslate_theta`

 Let `d` be a prime `≡ 7 (mod 8)` and `K = ℚ(√-d)`. Let `C`, `D` be CM lattices, each a lattice
stable under `𝓞_K` with a point `t` of order two scaled so that `℘''(t) = 2`, a square root `a₁` of
`12 ℘(t)`, and a theta function `θ`. Suppose `D.a₁ = σ C.a₁` for an automorphism `σ` of `ℂ` over
`K`, and the lattice of `C` is `Ω 𝓞_K`. Then for every finite set `S ⊆ K` there is a period `v` of
`D` such that, for all `s ∈ S`, applying `σ` to the Taylor coefficients at 0 of the translate of `θ`
by `s Ω` gives those of the translate by `s v` of the theta function of `D`. The translate by `u` is
the twisted one, `z ↦ exp (-π (z ū + |u|² / 2) / area Λ) * θ (z + u)`. 
