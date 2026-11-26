---
{
  "module": "src/Lib/CM/Integrality/IsogenyIntegrality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/IsogenyIntegrality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/IsogenyIntegrality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Isogenies and translates act integrally on expansions

Let `p` be a prime and `ιₚ : ℂ →+* ℂ_[p]` a fixed embedding. For a lattice `Λ` of a `CMLattice`, the
function `y_Λ = translatedY` is the second Weierstrass coordinate at `z + t` in the model of the
lattice, `(℘′(z + t) - a₁ x(z)) / 2` with `x(z) = ℘(z + t) - ℘(t)`, `a₁` the `xy`-coefficient of
that Weierstrass model and `t` the chosen point of order two, and `translatedYThetaCube` is the
entire extension of `y θ³`, where `θ` is the theta function of degree one, normalised by `θ(0) = 1`.
The ring `integralSeriesRing` is `𝒪[[y_Λ]]`, the integral power series in the Taylor series of
`y_Λ`, and `taylorVia ιₚ f` is the Taylor series of `f` at `0` with `ιₚ` applied to its
coefficients.

* `New.CMLattice.exists_rescale_theta_eq_theta_pow_mul`: an isogeny of degree `N` pulls `θ` back to
  `θ ^ N` times an integral series in `y`.
* `New.CMLattice.rescale_translatedY_mem_integralSeriesRing`: an isogeny pulls `y` back to an
  integral series in `y`.
* `New.CMLattice.norm_le_one_of_mapsTo_lattice`: the multiplier of an isogeny is integral at `p`.
* `New.CMLattice.exists_rescale_twistedTranslate_eq_theta_pow_mul`: the pull-back of a torsion
  translate of `θ`.

The pull-back statements rest on the integrality principle for sections with integral torsion
values, and the integrality of the multiplier follows from the pull-back of `y`.

## Relation to the literature

Known result: an isogeny of elliptic curves with good reduction acts on the formal groups by an
integral power series. Background: Silverman, *The Arithmetic of Elliptic Curves*, Chapters IV and
VII.


### `exists_rescale_eq_theta_pow_mul`

 Let multiplication by `a` be an isogeny of degree `N` from the lattice `Λ` of `C` to the lattice
`Λ'` of `C'`, and let `G` be a section of degree `n` for `C'` (a theta function of that degree)
with integral torsion values (their images under `ιₚ` have norm at most `1`). Then the series of
`G(a z)` (Taylor series at `0`, mapped to `ℂ_[p]` by `ιₚ`) is the `N n`-th power of that of
`θ_Λ = C.θ` times an element of `C.integralSeriesRing`, the ring of integral power series in the
series of `y_Λ = C.translatedY`. 

### `exists_rescale_theta_eq_theta_pow_mul`

 Let multiplication by `a` be an isogeny of degree `N` from the lattice `Λ` of `C` to the lattice
`Λ'` of `C'`, and let `θ` be the normalised theta function of degree one. Then the series of
`θ_Λ'(a z)` (Taylor series at `0`, mapped to `ℂ_[p]` by `ιₚ`) is the `N`-th power of that of `θ_Λ`
times an element of `C.integralSeriesRing`. That ring consists of the integral power series in the
series of `y_Λ = C.translatedY`, where `y(z) = ½(℘′(z + t) − a₁ x(z))`, `x(z) = ℘(z + t) − ℘(t)` and
`t` is the chosen point of order two. 

### `rescale_translatedY_mem_integralSeriesRing`

 Let multiplication by `a` be an isogeny of degree `N` from the lattice `Λ` of `C` to the lattice
`Λ'` of `C'`, and write `y = translatedY`, that is, `y(z) = ½(℘′(z + t) − a₁ x(z))` with
`x(z) = ℘(z + t) − ℘(t)` for the chosen point `t` of order two of each lattice. Then the series of
`y_Λ'(a z)` (Taylor series at `0`, mapped to `ℂ_[p]` by `ιₚ`) lies in `C.integralSeriesRing`, the
ring of integral power series in the series of `y_Λ`. 

### `rescale_translatedY_mem_and_rescale_theta_eq`

 Let `d` be a prime that is 7 modulo 8 and `ιₚ : ℂ → ℂ_[p]` a `p`-adic place. Let `C`, `C'` have
lattices `Λ`, `Λ'`, and suppose multiplication by `a` maps `Λ` into `Λ'` with
`a ā area(Λ) = N area(Λ')`; for `a ≠ 0` this makes it an isogeny of degree `N`. Write
`y = translatedY`, that is `y(z) = ½(℘′(z + t) − a₁x(z))` with `x(z) = ℘(z + t) − ℘(t)`, and
`𝒪[[y_Λ]] = C.integralSeriesRing` for the ring of integral power series over `ℂ_[p]` in the Taylor
series of `y_Λ`. Then the Taylor series at `0` of `y_Λ'(a z)`, with coefficients mapped by `ιₚ`,
lies in `𝒪[[y_Λ]]`, and that of the theta function `θ_Λ'(a z)` is the `N`-th power of that of `θ_Λ`
times an element of `𝒪[[y_Λ]]`. This corollary collects `rescale_translatedY_mem_integralSeriesRing`
and `exists_rescale_theta_eq_theta_pow_mul`. 

### `norm_le_one_of_mapsTo_lattice`

 If multiplication by `a` maps the lattice `Λ` of `C` into the lattice `Λ'` of `C'`, then `a` is
integral at `p`: its image under the embedding `ιₚ : ℂ →+* ℂ_[p]` has norm at most `1`. This relies
on both lattices carrying the normalisation of `CMLattice`, namely `℘''(t) = 2` at the chosen point
`t` of order two, with `d` a prime congruent to 7 mod 8. 

### `exists_rescale_twistedTranslate_eq_theta_pow_mul`

 Let `δ ≠ 0`, let multiplication by the conjugate `δ̄` be an isogeny of degree `N` of the
lattice `Λ` to itself, and let `δ v ∈ Λ`. Let `T_v θ = C.twistedTranslate 1 v C.θ`, the function
`z ↦ exp(-π (z v̄ + |v|²/2) / A) θ(z + v)` with `A` the area of `Λ`. Then the series of
`(T_v θ)(δ̄ z)` (Taylor series at `0`, mapped to `ℂ_[p]` by `ιₚ`) is the `N`-th power of that of
`θ` times an element of `C.integralSeriesRing`, the ring of integral power series in the series of
`y_Λ = C.translatedY`. 
