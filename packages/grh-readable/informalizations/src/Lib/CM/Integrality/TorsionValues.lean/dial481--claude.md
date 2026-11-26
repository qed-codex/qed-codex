---
{
  "module": "src/Lib/CM/Integrality/TorsionValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/TorsionValues.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/TorsionValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrality of values of sections at torsion points

The file defines the value `torsionValue` at a point of a function with a degree `n` (the function
value times an exponential factor that depends on `n`), which is used for sections at torsion
points, and the property `HasIntegralValues`. For a prime `d ≡ 7 (mod 8)` the file shows that `a₁`
is integral, that `max (|σ[u]|_p, |θ[u]|_p) = 1` at torsion points, and that monomials in `θ`, `σ²`
and the section `translatedYThetaCube` have integral torsion values. Here `translatedYThetaCube` is
`y θ³`, where `y` is the coordinate `translatedY` in the cubic `y² + a₁ x y = x³ + x`.

Notions from other files:
* `CMLattice d`: a lattice `Λ` with a point `t` of order two in `ℂ / Λ` and a coefficient `a₁` of
  its cubic. For `d ≠ 0` the lattice has complex multiplication by the integers of `ℚ(√-d)`.
* `σ` and `θ`: the sigma function of `Λ`, normalised so that twisted translation by a period
  multiplies it by a sign, and the theta function that vanishes exactly on `-t + Λ`.
* `twistedTranslate n v G`: the translate of a function `G` by `v`, multiplied by the exponential
  factor of `n` times the Hermitian form `H(l, z) = (π / area Λ) l̄ z`.
* `ιₚ`: the fixed embedding of `ℂ` into `ℂ_p` (`PadicPlace p`); integral means of norm at most `1`,
  that is, lying in `valRingCp p`, the set of elements of `ℂ_p` of norm at most `1`.

## Main definitions and results

* `New.CMLattice.torsionValue`, `New.CMLattice.HasIntegralValues`: the torsion value `G[u]` and the
  property that all of these are integral at torsion points.
* `New.CMLattice.norm_a₁_le_one`: `a₁` is integral, because `a₁ ^ 4 - 64` is a unit.
* `New.CMLattice.torsionValue_mul`, `New.CMLattice.torsionValue_comp_isogeny`,
  `New.CMLattice.torsionValue_twistedTranslate`: the rules for products, pull-backs and translates.
* `New.CMLattice.max_norm_torsionValue`: `max (|σ[u]|_p, |θ[u]|_p) = 1` at torsion points.
* `New.CMLattice.hasIntegralValues_monomialSection`: monomials have integral torsion values.

## Relation to the literature

Known result: the Weber invariants of discriminant `-d` with `d ≡ 7 mod 8` are integral. Source:
Birch, *Weber's class invariants*.

Known result: the integrality of Siegel functions at torsion points. Source: Kubert and Lang,
*Modular Units*.


 ## Integrality of the coefficient `a₁` 

### `norm_le_one_of_sq_add_mul_eq`

 If `g ^ 2 + u g = v` in `ℂ_p` and `‖u‖, ‖v‖ ≤ 1`, then `‖g‖ ≤ 1`: a root of a monic quadratic
with integral coefficients is integral. 

### `norm_a₁_le_one`

 For a prime `d ≡ 7 (mod 8)` the coefficient `a₁` of the cubic of a CM lattice is integral in
`ℂ_p`. 


## Torsion values and their norms

The proof of `max_norm_torsionValue` rests on three facts: doubling raises the norm of the nonzero
pair `(θ[u]², σ[u]²)` to the fourth power, this norm depends only on `u` modulo `Λ`, and modulo
`Λ` the orbit of a torsion point under doubling is finite.


### `IsTorsion`

 `u` lies in `ℚ Λ`, that is, it represents a torsion point of `ℂ / Λ`. 

### `torsionValue`

 The torsion value `G[u]` of a function `G` with the degree `n`: the value at `0` of the twisted
translate of `G` by `u` for `n` times the Hermitian form of the lattice. 

### `IsTorsion.add`

 The sum of two torsion points is a torsion point. 

### `IsTorsion.mul_of_isogeny`

 An isogeny `z ↦ a z` between the lattices takes torsion points to torsion points. 

### `torsionValue_eq`

 The torsion value of `G` at `u` is `G(u) exp (-n π |u|² / (2 area Λ))`. 

### `torsionValue_mul`

 Products: degrees add and torsion values multiply. 

### `torsionValue_eq_mul_theta_pow`

 If `G(u) = θ(u) ^ n c`, then `G[u] = θ[u] ^ n c` for the torsion values in the degrees `n` of
`G` and `1` of `θ`; so `G[u] / θ[u] ^ n = G(u) / θ(u) ^ n` off the zeros of `θ`. 

### `torsionValue_comp_isogeny`

 Pull-backs: if `z ↦ a z` is an isogeny of degree `N` from the lattice of `C` to that of `C'`,
then with the degree `n N` the function `G(a z)` has at `u` the torsion value `G[a u]`. 

### `pi_mul_I_mul_riemannForm_eq`

 `π i` times the Riemann form (the alternating form) of `n` times the Hermitian form of the
lattice, at `(u, v)`, is `-n π i Im (u v̄) / area Λ`. 

### `torsionValue_twistedTranslate`

 Translates: the twisted translate of `G` by `v` (for `n` times the Hermitian form) has at `u`
the torsion value `G[u + v]` times `exp (-n π i Im (u v̄) / area Λ)`. 

### `norm_torsionValue_twistedTranslate`

 For torsion points `u`, `v` the twisted translate of `G` by `v` has at `u` a torsion value of
the same `p`-adic norm as `G[u + v]`: the two differ by a root of unity. 

### `HasIntegralValues`

 The torsion values of `G` with the degree `n` are all integral in `ℂ_p`: for every torsion
point `u`, the image of `G[u]` under `ιₚ` has norm at most `1`. 

### `HasIntegralValues.mul`

 If `F` and `G` have integral torsion values (`HasIntegralValues`) in the degrees `m` and `n`,
so has `F G` in the degree `m + n`. 

### `HasIntegralValues.pow`

 If `G` has integral torsion values in the degree `n`, so has `G ^ k` in the degree `k n`. 

### `HasIntegralValues.comp_isogeny`

 If `G` has integral torsion values on the target of an isogeny `z ↦ a z` of degree `N`, so has
`G(a z)` on the source, with the degree multiplied by `N`. 

### `HasIntegralValues.translate`

 If `G` has integral torsion values in the degree `n`, so has its twisted translate by a torsion
point `v`. 

### `squarePair`

 The pair `w(u) = (θ[u]², σ[u]²)` of squared torsion values of degree `1`, read in `ℂ_p`. 

### `squarePair_ne_zero`

 The pair `w(u)` is never zero, because `t ∉ Λ`. 

### `norm_squarePair_add_of_mem`

 For a torsion point `u` the norm in `ℂ_p × ℂ_p` of `w(u) = (θ[u]², σ[u]²)` depends only on `u`
modulo `Λ`: twisted translation by a period multiplies `θ` and `σ` by a sign. 

### `torsionValue_two_mul`

 In the degree `1` the torsion value of `G` at `2 u` is that of `G(2 z)`, with the degree `4`,
at `u`. 

### `torsionValue_theta_two_mul`

 For a prime `d ≡ 7 (mod 8)` the doubling formula for `θ` holds for torsion values:
`θ[2 u] = θ[u] ^ 4 - σ[u] ^ 4`. 

### `torsionValue_sigma_two_mul_sq`

 For a prime `d ≡ 7 (mod 8)` the doubling formula for `σ²` holds for torsion values:
`σ[2 u]² = θ[u]² σ[u]² (4 θ[u] ^ 4 + a₁² θ[u]² σ[u]² + 4 σ[u] ^ 4)`. 

### `squarePair_two_mul`

 For a prime `d ≡ 7 (mod 8)`, doubling acts on `w(u) = (θ[u]², σ[u]²)` through `doublingForms`,
the quartic forms `(w₀² - w₁²)²` and `w₀ w₁ (4 w₀² + a₁² w₀ w₁ + 4 w₁²)`. 

### `squarePair_two_pow_mul`

 For a prime `d ≡ 7 (mod 8)` the pair `w(2 ^ j u)` is the `j`-th iterate of the map
`doublingForms (ιₚ C.a₁)`, whose two quartic forms are given in `squarePair_two_mul`, at
`w(u) = (θ[u]², σ[u]²)`. 

### `norm_squarePair_two_pow_mul`

 For a prime `d ≡ 7 (mod 8)`, doubling `j` times raises the norm of `w(u) = (θ[u]², σ[u]²)` to
the power `4 ^ j`. 

### `exists_ne_two_pow_modEq`

 Among the powers of `2`, two with different exponents are congruent modulo `n ≠ 0`. 

### `norm_squarePair`

 For a prime `d ≡ 7 (mod 8)` the pair `w(u) = (θ[u]², σ[u]²)` has norm `1` in `ℂ_p × ℂ_p` at
every torsion point `u`. 

### `max_norm_torsionValue`

 For `d` a prime `≡ 7 (mod 8)`, a `p`-adic place `ιₚ` and a torsion point `u` (`u ∈ ℚ Λ`),
consider the degree-`1` torsion values `σ[u]` and `θ[u]` of the sigma function `σ` and of `C.θ`.
These are the values at `0` of their twisted translates by `u` for the Hermitian form of the
lattice. The larger of `‖ιₚ σ[u]‖` and `‖ιₚ θ[u]‖` is `1`. This is a form of the integrality of
Siegel functions at torsion points. 

### `hasIntegralValues_sigma`

 For a CM lattice `C` with `d` a prime `≡ 7 (mod 8)`, the sigma function `C.σ` has integral
torsion values in degree `1` at the chosen place `ιₚ` above `p`: for every torsion point `u`, the
image of `σ[u]` under `ιₚ` has norm at most `1` in `ℂ_p`.

This is a local analogue of the integrality of the Siegel function at torsion points (Ramachandra,
Robert): only at the chosen place above `p`, for these CM lattices, and with the normalization of
`torsionValue`. 

### `hasIntegralValues_theta`

 For a prime `d ≡ 7 (mod 8)` the theta function has integral torsion values in the degree `1`. 

### `torsionValue_translatedYThetaCube_sq_add`

 For a prime `d ≡ 7 (mod 8)` the torsion values of `y θ³` (`translatedYThetaCube`) satisfy the
monic quadratic equation that the cubic gives after multiplication by `θ ^ 6`. 

### `hasIntegralValues_translatedYThetaCube`

 For a prime `d ≡ 7 (mod 8)` the section `y θ³` has integral torsion values in the degree `3`,
as roots of monic quadratic equations with integral coefficients. 

### `hasIntegralValues_monomialSection`

 For `d` a prime `≡ 7 (mod 8)` and a `p`-adic place `ιₚ`, take a triple `(a, b, c)` and the
monomial `θ^a (σ²)^b G^c` (`monomialSection`), a section of degree `a + 2b + 3c`. Here `σ` is the
sigma function of the lattice and `G = translatedYThetaCube` is the entire function equal to `y θ³`
off `t + Λ`. For every torsion point `u`, the torsion value of this monomial in degree `a + 2b + 3c`
at `u` has `ιₚ`-image of norm at most `1`. 
