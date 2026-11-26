---
{
  "module": "src/New/Reduction/Data/FieldsAndPlaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The parameters q₀ and d, the field E = K(ζ), its infinite places and its roots of unity

Fix a multiple `q₀` of `18480` and a prime `d ≡ q₀/2 - 1 mod q₀`. Let `K = ℚ(√-d)`, and let
`E = K(ζ)` with `ζ` of order `q₁ = q₀ * towerDeg s`. The file counts the places, describes how they
act on `ζ`, shows that every root of unity of `E` is a power of `ζ`, and writes norms from `E` to
`K` as products over the embeddings `Φ v`. In the comments `c = ⌊log₃ s⌋ + 5`, so that
`towerDeg s = 3^c 2^s`, `φ` is Euler's totient function, and `P.Φ s` is the type of infinite places
of `E`.

## Main definitions and results

* `New.Parameters`: a multiple `q₀` of `18480` and a prime `d ≡ q₀/2 - 1 mod q₀`. Then `d ≡ 7 mod 8`
  and `(p / d) = 1` for each prime `p ∣ q₁` (`New.Parameters.chiK_eq_one_of_dvd`).
* `New.Parameters.irreducible_cyclotomic`: the cyclotomic polynomial of order `q₁` is irreducible
  over `K`, so `Gal(E/K) = (ℤ/q₁)ˣ`. `E` embeds in `ℚ(ζ_{q₁ d})`, hence is abelian over `ℚ`.
* `New.Parameters.galOfPlace`, `New.Parameters.placeMulEquiv`: the infinite places of `E` form a
  group, identified with `Gal(E/K)` and `(ℤ/q₁)ˣ`. Composing a fixed embedding of `E` in `ℂ` over
  `K` with these automorphisms gives one embedding for each infinite place, the CM type of `E`.
* `New.Parameters.numInfPlaces_E`, `New.Parameters.card_placeClass_eq_one_eq_towerDeg`: there are
  `towerDeg s * φ(q₀)` places, `towerDeg s` of them of class `1` modulo `q₀`; this rests on
  `cyclotomic q₁ = (cyclotomic q₀)(X ^ towerDeg s)` (`New.Parameters.expand_towerDeg_cyclotomic`).
* `New.Parameters.exists_zeta_pow_eq`: every root of unity of `E` is a power of `ζ`.
* `New.Parameters.prod_phi_eq_norm`: the product of the images of `y` under the `K`-embeddings `Φ v`
  of `E` in `ℂ` is the norm of `y` from `E` to `K`.

The basic facts on the field `E` are proved in `Lib` or in
`New.Derivatives.Field.PrimeDecomposition`:
* the ring of integers: `New.Parameters.adjoin_betaKInE_zetaInt_eq_top`, in the latter file;
* the different of `E` over its real subfield and the places fixed by conjugation:
  `New.differentIdeal_eq_top_of_add_star_eq_one`, `New.two_notMem_of_star_eq` and
  `New.exists_sq_eq_q_of_star_eq` in `Lib`, `New.Parameters.natCast_eq_neg_one_of_star_eq` in the
  latter file.

Notions from other files:
* `New.chiK d` is the Legendre symbol `(· / d)`, the character of `ℚ(√-d)` for `d ≡ 3 mod 4`.
* `New.CMType E` is a choice, for each infinite place of the CM field `E`, of an embedding in `ℂ`
  that induces it; `Φ v` is the embedding chosen at `v`.



## The parameters q₀, d, the field E and its group Φ of infinite places

* `New.Parameters.q₂` and `New.Parameters.bigOmega`: the number `(q₀ d) ^ (s + 6)`, and a real
  constant built from `L'/L(1, χ_K)` and the root discriminant of `E`.


### `New.Parameters`

 The fixed parameters: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a prime `d` with
`d ≡ q₀/2 - 1 mod q₀`. The congruence is stated as: `q₀` divides `2 (d + 1)` but not `d + 1`.
The first part forces `q₀ ≠ 0`; as `q₀` is even, it says that `q₀/2` divides `d + 1`, and the
second part says that the quotient is odd. The exponent `ε` of the scales is not a field: it enters
only the existence of admissible data (`New.eventually_exists_data`). 

### `New.Parameters.q₀`

 The modulus `q₀`. 

### `New.Parameters.d`

 The prime `d` with `K = ℚ(√-d)`. 

### `New.Parameters.dvd_q₀`

 `q₀` is a multiple of `18480 = 16 · 3 · 5 · 7 · 11`. 

### `New.Parameters.d_prime`

 `d` is prime. 

### `New.Parameters.q₀_dvd_and_not_dvd`

 `d ≡ q₀/2 - 1 mod q₀`, stated as: `q₀` divides `2 (d + 1)` but not `d + 1`. 

### `instPrimeSevenModEight`

 The prime `d` is congruent to 7 modulo 8: `d + 1` is an odd multiple of `q₀/2`, and `16` divides
`q₀`. 

### `_root_.New.l₀`

 The number `l₀`: for `s ≥ 1`, the least power of `3` above `27 s`. 

### `_root_.New.towerDeg`

 The ratio `q₁ / q₀ = 3 l₀ 2 ^ s`; see `towerDeg_eq`. 

### `q₁`

 The order `q₁ = q₀ * towerDeg s` of the root of unity `ζ` that generates `E` over `K`. 

### `dvd_d_add_one_div_four_of_dvd_q₁`

 Let `P : Parameters` consist of the modulus `q₀` and the prime `d ≡ q₀/2 - 1 mod q₀`. Every
prime `p` dividing `P.q₁ s = q₀ * towerDeg s`, where `towerDeg s` is a power of `3` times `2 ^ s`,
divides `(d + 1) / 4`, the norm of `(1 + √-d) / 2`. 

### `sixty_four_lt_d`

 The prime `d` exceeds `64`, as `2 (d + 1)` is a positive multiple of `q₀ ≥ 18480`. 

### `chiK_eq_one_of_dvd`

 Let `P : Parameters` consist of the modulus `q₀` and the prime `d ≡ q₀/2 - 1 mod q₀`. For every
prime `p` dividing `P.q₁ s = q₀ * towerDeg s`, the Legendre symbol `chiK d p = (p / d)` is `1`,
which is the criterion for `p` to split in `K = ℚ(√-d)`. 

### `thirteen_le_of_chiK_ne_one`

 A prime that does not split in `K = ℚ(√-d)`, that is `χ_K(p) ≠ 1`, is at least `13`. 

 ### The fields `K` and `E` 

### `K`

 The imaginary quadratic field K = ℚ(i√d), as a subfield of ℂ. 

### `q₂`

 The number `q₂ = (q₀ d) ^ (s + 6)`, a multiple of `q₁ d`; the three primes of the data are `≡ 1`
modulo its square. 

### `q₁_mul_d_dvd_q₂`

 Let `P` consist of the modulus `q₀` and the prime `d`. The product `q₁ d`, where
`q₁ = q₀ * towerDeg s = q₀ * 3 ^ (⌊log₃ s⌋ + 5) * 2 ^ s` is the order of `ζ`, divides
`q₂ = (q₀ d) ^ (s + 6)`. 

### `E`

 The field E = K(ζ) obtained from K by adjoining a primitive root of unity ζ of order q₁ = 3^c
2^s q₀. 

### `Φ`

 The infinite places of the field E = K(ζ) at level s; they carry the group structure of
Gal(E/K) (`New.Parameters.galOfPlace`). 

### `bigOmega`

 The real number exp(γ − Re L′/L(1, χ_K))·2π/rd_E, with γ Euler's constant and rd_E the
root discriminant of E. 

### `irreducible_cyclotomic`

 Let `P : Parameters` consist of the modulus `q₀` and the prime `d`, and let `s` be a natural
number. For `P.q₁ s = q₀ * towerDeg s`, the cyclotomic polynomial of order `P.q₁ s` is irreducible
over the quadratic field `P.K = ℚ(√-d)`. 

### `toCycloField`

 A chosen ℚ-algebra embedding of E = K(ζ), ζ of order q₁, into the cyclotomic field
ℚ(ζ_{q₁d}). 

 ### The infinite places of `E` as a group 

### `algHom_eq_of_mk_eq`

 Two `K`-embeddings of `E` in `ℂ` that induce the same infinite place are equal. 

### `instance : CommGroup (P.Φ s)`

 The infinite places of E form a commutative group. The law is transported from Gal(E/K) along
the bijection that sends g to the place of a fixed embedding of E over K composed with g. 

### `galOfPlace`

 The isomorphism v ↦ σ_v from the group of infinite places of E to Gal(E/K). The place that
corresponds to a in (ℤ/q₁)^× goes to the automorphism ζ ↦ ζ^a. 

### `placeMulEquiv`

 The group isomorphism from the group of infinite places of E to (ℤ/q₁)^×. It is the composite of
`New.Parameters.galOfPlace` with the isomorphism Gal(E/K) ≅ (ℤ/q₁)^× given by the action on ζ. 

### `placeOfInt`

 The infinite place of E named by the class of the integer ν modulo q₁ if ν is prime to q₁, and
the identity place otherwise. 

### `placeClass`

 For a divisor m of q₁, the homomorphism from the group of infinite places of E, identified with
(ℤ/q₁)^×, to (ℤ/m)^× given by reduction modulo m. 

### `ζ`

 A chosen primitive q₁-th root of unity ζ in E. 

### `instance : CMType (P.E s)`

 The CM type of E: the embedding at the place v is a fixed embedding of E over K composed with
the automorphism `New.Parameters.galOfPlace` s v. 

### `phi_algebraMap`

 For each infinite place `v` of `E`, the embedding `Φ v` of `E` into `ℂ` chosen at `v` restricts
on `K` to the inclusion of `K` in `ℂ`: `Φ v (algebraMap K E x) = x`. 


## The order of Φ, classes of places and the action on roots of unity

`New.Parameters.placeClass` is the class of a place modulo a divisor of `q₁`, and
`New.Parameters.placeOfInt` is the place named by an integer prime to `q₁` (the identity for other
integers).

* `New.Parameters.galOfPlace_zeta`, `New.Parameters.galOfPlace_placeOfInt_zeta`: a place acts on `ζ`
  by raising it to the power that names it.


### `expand_pow_cyclotomic`

 If the prime `p` divides `N`, then substituting `X ^ (p ^ k)` in the cyclotomic polynomial of
order `N` gives that of order `N p ^ k`, over any commutative ring `R`. 

### `numInfPlaces_E`

 The number of infinite places `Core.numInfPlaces` of E = K(ζ), ζ of order q₁ = 3^c 2^s q₀, is
3^c 2^s φ(q₀), where 3^c 2^s = `New.towerDeg` s and φ is Euler's totient function. 

### `card_placeClass_eq_one_eq_towerDeg`

 Given that `P.q₀` divides `P.q₁ s` (`h_dvd`), exactly `towerDeg s = P.q₁ s / P.q₀` elements `v`
of `P.Φ s`, the infinite places of `P.E s`, have class `1` modulo `P.q₀`
(`New.Parameters.placeClass`). 

 ### The action on the root of unity, and places named by integers 

### `phi_mul`

 The embedding `Φ (v * v')` at the place `v * v'` is `Φ v` composed with the automorphism
`P.galOfPlace s v'` of `P.E s` attached to `v'`: `Φ (v * v') x = Φ v (P.galOfPlace s v' x)`. 

### `star_zeta`

 The involution `star` of the CM field `E` inverts `ζ`. 

### `galOfPlace_zeta`

 The automorphism attached to the place `v` raises `ζ` to the residue modulo `q₁` that names
`v`, that is, the image of `v` in `(ℤ/q₁)ˣ` under `New.Parameters.placeMulEquiv`. 

### `placeOfInt_pow`

 The `i`-th power of the place named by `ν` is the place named by `ν ^ i`. This holds also for
`ν` not prime to `q₁`, when both sides are the identity place. 

### `placeMulEquiv_placeOfInt`

 For `ν` prime to `q₀`, the place named by `ν` (`New.Parameters.placeOfInt`) corresponds to the
residue of `ν` under the isomorphism of the group of places with `(ℤ/q₁)ˣ`. 

### `placeClass_placeOfInt`

 For `ν` prime to `q₀`, the place named by `ν` (`New.Parameters.placeOfInt`) has class `ν` modulo
each divisor `m` of `q₁`, `placeClass` being the reduction to `(ℤ/m)ˣ` of `(ℤ/q₁)ˣ`. 

### `galOfPlace_placeOfInt_zeta`

 For an integer ν prime to q₀, the element of Gal(E/K) attached to the infinite place named by ν
(`New.Parameters.placeOfInt`) sends the chosen primitive q₁-th root of unity ζ to ζ^ν. 

### `d_pow_ne_neg_one`

 For parameters `P`, no power of the prime `d` is congruent to `-1` modulo `q₀`. As `d` is odd
and `q₀` divides `2 (d + 1)` but not `d + 1`, we have `d ^ 2 = 1` in `ZMod q₀`, and the powers `1`
and `d` of `d` both differ from `-1`. 

### `placeClass_placeOfInt_eq_neg_one_iff`

 Let `ν` be an integer and suppose `q₀ ∣ q₁`. The place `P.placeOfInt s ν` of `E` is the one that
corresponds to `ν mod q₁` under the isomorphism of the group of places with `(ℤ/q₁)ˣ` if `ν` is a
unit modulo `q₁`, and the identity place otherwise; `P.placeClass h_dvd` reduces the element of
`(ℤ/q₁)ˣ` of a place modulo `q₀`. This class is `-1` if and only if `ν ≡ -1` modulo `q₀`. 

 ## Roots of unity of E and norms to K 

### `exists_zeta_pow_eq`

 For parameters `P : Parameters` and a level `s` (both implicit), every root of unity `y`
(element of finite order) of the field `P.E s` is a power `ζ P s ^ k` with `k < P.q₁ s`. 

### `norm_zeta_eq_one`

 The norm of `ζ` from `E` to `K` is `1`, as `q₁ ≠ 2`. 

### `prod_phi_eq_norm`

 Let `Φ v` be the embedding of `E` in `ℂ` chosen at the infinite place `v`: it induces `v` and
fixes `K = ℚ(√-d)`, and each `K`-embedding of `E` is `Φ v` for exactly one place `v`. The product
over all `v` of the images `Φ v y` is the norm of `y` from `E` to `K`, seen in `ℂ`. 
