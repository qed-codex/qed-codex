---
{
  "module": "src/New/Derivatives/Field/WeilData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weil data of the CM field E = K(ζ) and the number s₀

Let `K = ℚ(√-d) ⊆ ℂ` and `E = P.E s = K(ζ)`, with `ζ` a primitive root of unity of order `q₁`;
`star` is complex conjugation on `E`. The infinite places `v` of `E` form a group isomorphic to
`Gal(E/K)` and to `(ℤ/q₁)ˣ`, and `v • w` is the pullback of a finite place `w` along the
automorphism `P.galOfPlace s v`. This file describes the places of `E` above a prime
`p ≡ 1` mod `q₁ d` and builds the Weil data of `E`. From the idele α of these data it defines the
number s₀ = `New.Parameters.vacuumRoot`, a root of `(chiFin α)⁻¹`, and computes the absolute
values of its conjugates over `K`.

## Main definitions and results

* `New.Parameters.q_eq_of_modEq_one`, `New.Parameters.nonempty_infinitePlace_equiv_finPlace`: for
  `p ≡ 1` mod `q₁ d` the places above `p` have norm `p`. If `a ∈ 𝓞 E` has `a ā = p c` with `c : ℕ`
  prime to `p`, those that divide `a` are in bijection with the infinite places.
* `New.Parameters.α`: the idele with component 1/P'(ζ) at the places that divide
  `New.Parameters.betaKInE` and 1 elsewhere.
* `New.Parameters.instWeilDataE`: the Weil data, with ȷ = −1/√−d.
* `New.Parameters.norm_gal_vacuumRoot`: for every automorphism `σ` of `ℂ` over `K`, ‖σ s₀‖ ^ 2 is
  the root discriminant of `E` divided by `√d`.

Notions from other files:
* `New.Parameters`: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a prime `d` with
  `d ≡ q₀/2 - 1 mod q₀`; `New.Parameters.q₁` is `3 ^ c * 2 ^ s * q₀`, with `c = ⌊log₃ s⌋ + 5`.
* `New.Parameters.Φ`: `P.Φ s` is the group of infinite places of `E`. It is distinct from the bare
  `Φ` of the CM type of `E` (`New.CMType`): `Φ v : E →+* ℂ` is the embedding over `K` inducing `v`.
* `New.WeilData`: an imaginary element ȷ, a finite idele α and a splitting character υ.
* `New.chiFin`: the character x ↦ υ(x)|x|^(−1/2) of the finite ideles of `E`, x being extended by
  1 at infinity.
* `New.Parameters.relDifferentGen`: P'(ζ), the value at `ζ` of the derivative of the cyclotomic
  polynomial of order `q₁`; it generates the different of `E/K`.



## Places above a prime congruent to `1` modulo `q₁ d`

Such a prime `p` has trivial Frobenius element.


### `smul_eq_self_iff_eq_one`

 Let `p ≡ 1` modulo `q₁ d` be prime and `w` a place of `E` above `p`. An infinite place `v`, read
as an element of `Gal(E/K)`, fixes `w` if and only if it is the identity. 

### `q_eq_of_modEq_one`

 If `p ≡ 1` modulo `q₁ d` is prime, every finite place `w` of `E` above `p` has absolute norm
`w.q = p`. 

### `star_mem_iff_notMem`

 Let `E = P.E s`, the field generated over `K` by a primitive `P.q₁ s`-th root of unity. Let `w`
be a finite place of `E` above a prime `p ≡ 1` modulo `P.q₁ s * P.d`. Let `a` in `𝓞 E` satisfy
`a * star a = p * c`, with `c` a natural number prime to `p`. Then `w` contains exactly one of `a`
and `star a`. 

### `intValuation_eq_of_mul_star`

 Let `E = P.E s`, the field generated over `K = ℚ(√-d)` by a primitive `P.q₁ s`-th root of unity.
Let `p ≡ 1` modulo `P.q₁ s * P.d` be prime. Let `a` in `𝓞 E` satisfy `a * star a = p * c`, with `c`
a natural number prime to `p`. A finite place `w` of `E` above `p` that divides `a` divides it
exactly once: `w.intValuation a = exp (-1)`. 

### `eq_of_smul_eq_or_smul_eq_star`

 Let `E = P.E s`, the field generated over `K` by a primitive `P.q₁ s`-th root of unity. Let `w`
be a finite place of `E` above a prime `p ≡ 1` modulo `P.q₁ s * P.d`. Let `u` and `v` be infinite
places in `P.Φ s`, read as elements of `Gal(E/K)`. If `v • w` is `u • w` or its conjugate
`star (u • w)`, then `u = v`. 

### `nonempty_infinitePlace_equiv_finPlace`

 Let `E = P.E s`, and let `p ≡ 1` modulo `P.q₁ s * P.d` be prime. Let `a` in `𝓞 E` satisfy
`a * star a = p * c`, where `star` is complex conjugation and `c` is a natural number prime to `p`.
Then the infinite places of `E` (the type `P.Φ s`) are in bijection with the finite places above `p`
that contain `a`. 


## The idele α and the Weil data of E

* `New.Parameters.v_alpha_mul_star_mul_relDifferentGen`: α·ᾱ·P'(ζ) is a unit at every finite place.


### `diagonalAtPlaces`

 The multiplicative map `E → 𝔸f E` that puts `x` at the places of `S` and `1` at the other
places. With `e` the idempotent of `S` it is `x ↦ e x + (1 - e)`. 

### `diagonalAtPlaces_apply`

 The component of `diagonalAtPlaces S x` at `w` is `x` if `w ∈ S` and `1` otherwise. 

### `valuation_map_relDifferentGen`

 For every injective ring endomorphism `f` of `𝓞 (P.E s)` and every finite place `w` of
`E = P.E s`, the elements `f (P.relDifferentGen s)` and `P.relDifferentGen s` have the same `w`-adic
valuation. 

### `valuation_star_relDifferentGen`

 The generator `relDifferentGen` of the different of `E/K` has the same valuation at a finite
place `w` and at its conjugate `w̄`. 

### `betaKInE_mem_or_star_mem`

 A finite place that divides the generator `relDifferentGen` of the different of `E/K` divides
`betaKInE = (1 + √-d) / 2` or its conjugate. 

### `α`

 The finite idele `α` of `E`: its component is the inverse of the generator `relDifferentGen` of
the different of `E / K` at the places dividing `betaKInE = (1 + √-d) / 2`, and `1` at the other
places. 

### `alpha_apply`

 At each finite place `w` of `E`, the component of the idele `α` is the image of the inverse of
`relDifferentGen` if `betaKInE ∈ w`, and `1` otherwise. 

### `inv_alpha_apply`

 At each finite place `w` of `E`, the component of the idele `α⁻¹` is the image of
`relDifferentGen` if `betaKInE ∈ w`, and `1` otherwise. 

### `inv_alpha_mem`

 The idele `α⁻¹` is integral: it lies in `Ô`, the finite adeles integral at every place. 

### `v_alpha_apply`

 The valuation of `α` at `w` is the inverse of that of `relDifferentGen` if `w` divides
`betaKInE`, and `1` otherwise. 

### `v_star_alpha_apply`

 The valuation of `star α` (the complex conjugate of `α`) at `w` is the inverse of that of
`relDifferentGen` if `w` divides the conjugate `star betaKInE` of `betaKInE`, and `1` otherwise. 

### `v_alpha_mul_star_mul_relDifferentGen`

 Let `α = P.α s` be the finite idele of `E` whose component is `1 / P'(ζ)` at the places dividing
`betaKInE = (1 + √-d) / 2` and `1` elsewhere. At every finite place `w` the product
`α * star α.val * P'(ζ)` is a unit, where `star` is complex conjugation: its valuation equals
`1`. 

### `q₁_mul_alpha_mem`

 Let `α = P.α s` be the finite idele of `E` whose component is `1 / P'(ζ)` at the places dividing
`betaKInE = (1 + √-d) / 2` and `1` elsewhere. The order `q₁` of `ζ` is a denominator of `α`: the
product `q₁ α` lies in `Ô`, the finite adeles integral at every place. 

### `twelve_dvd_q₁`

 The order `q₁` of `ζ` is a multiple of `12`. 

### `norm_zeta_pow_eq_one`

 The powers of `ζ`, that is the roots of unity of `E` (see `exists_zeta_pow_eq`), have norm `1`
over `K`. 

### `norm_zeta_sub_one_eq_one`

 For the chosen primitive `q₁`-th root of unity `ζ` of `E = K(ζ)`, the element `ζ - 1` has norm
`1` over `K`. 

### `exists_unit_prod_phi_eq_one_and_mul_star_eq`

 For parameters `P` and a level `s`, every root of unity of the CM field `E = P.E s = K(ζ)`,
with `K = ℚ(√-d)`, is `δ / δ̄` for a unit `δ` of norm `1` over `K`. Here `star` is complex
conjugation, and the norm is written as the product, over the infinite places `w` of `E`, of the
images of `δ` under the embeddings `Φ w : E → ℂ` over `K` chosen at these places. 

### `v_neg_inv_sqrtNegDInE_mul_alpha_mul_star`

 Let `α = P.α s` be the finite idele of `E` whose component is `1 / P'(ζ)` at the places dividing
`betaKInE = (1 + √-d) / 2` and `1` elsewhere. At every finite place `w` of `E`, the order of
`(-1/√-d) α ᾱ` is minus the order `m` of the different of `E/ℚ`: its multiplicative valuation is
`exp m`. 

### `instWeilDataE`

 `-1/√(-d)`, the idele `α` and a splitting character `υ` are Weil data for `E`. The character
`υ` exists because every root of unity is `δ / δ̄` for a unit `δ` of norm `1` over `K`. 

### `weilData_j_eq`

 The purely imaginary element `ȷ` of the Weil data of `E` is `-1/√(-d)`. 

### `phi_weilData_j`

 Every embedding of the CM type sends `ȷ` to `i / √d`. 

### `traceOne_eq_betaKInE`

 The number `(1 - ȷ⁻¹) / 2` is the generator `(1 + √(-d)) / 2` of the integers of `K`. 

### `v_weilData_j_mul_alpha_mul_star`

 Let `𝔞₀` be the ideal of the idele `α`. Then `ȷ 𝔞₀ 𝔞̄₀` is the inverse different of `E`: at
every finite place `w` the order of `ȷ α ᾱ` is minus the order of the different. 


## The number s₀ and the absolute values of its conjugates

The number s₀ = `New.Parameters.vacuumRoot` is the principal `f`-th root of `(chiFin α)⁻¹`, where
`f` is the number of infinite places of `E`.


### `vacuumRoot`

 The principal f-th root of the complex number (chiFin α)⁻¹ = υ(α)⁻¹|α|^(1/2), where
α = `New.Parameters.α`, υ is the splitting character of the Weil data of E, |α| is the idele norm
and f is the number of infinite places of E. 

### `vacuumRoot_pow_numInfPlaces`

 The power of `s₀ = vacuumRoot P s` by the number of infinite places of `E` is `(chiFin α)⁻¹`,
where `chiFin α = υ(α) |α|^(-1/2)` for the idele `α` and the splitting character `υ` of `E`. 

### `exists_chiFin_alpha_pow_mem`

 A positive power of `chiFin α` lies in `K`: it is the norm to `K` of an element of `E`. 

### `exists_vacuumRoot_pow_mem`

 A positive power of `s₀ = vacuumRoot P s`, a root of `(chiFin α)⁻¹`, lies in `K = ℚ(√-d)`. 

### `ideleAbs_alpha_eq_prod`

 The idele norm of the finite idele `α = P.α s`, extended by `1` at infinity, is the product of
the absolute values of the generator `relDifferentGen` of the different of `E/K` at all infinite
places `v` of `E` (the type `P.Φ s`). 

### `norm_gal_vacuumRoot`

 Let `E = K(ζ)` with `K = ℚ(√-d)`, and let `f` be the number of infinite places of `E`. Let
`α = P.α s` be the finite idele of `E` with component `1 / P'(ζ)` at the places dividing
`(1 + √-d) / 2` and `1` elsewhere. The number `s₀ = vacuumRoot P s` is the principal `f`-th root of
`υ(α)⁻¹ |α|^(1/2)`, with `|α|` the idele norm. For every automorphism `σ` of `ℂ` over `K`, the
square `‖σ s₀‖ ^ 2` is the root discriminant of `E` divided by `√d`. 
