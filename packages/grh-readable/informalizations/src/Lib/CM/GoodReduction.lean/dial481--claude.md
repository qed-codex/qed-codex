---
{
  "module": "src/Lib/CM/GoodReduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/GoodReduction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/GoodReduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# CM lattices as multiples of fractional ideals, and good reduction of CM curves

Let `K = ℚ(√-d) ⊂ ℂ` (`New.QuadField`), where `d` is a prime `≡ 7 mod 8` (`New.PrimeSevenModEight`).
We show that the lattice of every datum `New.CMLattice d` is a multiple `u 𝔞` of a fractional ideal
of `K` and that every ideal gives one, and we compute the covolumes. We then follow isogenies of
degree two through the class group. This shows that the discriminant of a CM lattice, normalised by
`℘''(t) = 2`, is a unit at every prime, as it is for a curve with good reduction.

## Main definitions and results

* `New.CMLattice.latticeModule`: the lattice of a datum as an `𝓞 K`-module;
  `New.QuadField.scaledIdeal`: `(u, 𝔞) ↦ u 𝔞`.
* `New.CMLattice.exists_latticeModule_eq_scaledIdeal`: the lattice of every datum has the form
  `u 𝔞`.
* `New.QuadField.exists_cmLattice_latticeModule_eq_scaledIdeal`: every `𝔞` has a multiple `u 𝔞` that
  is the lattice of a datum.
* `New.QuadField.area_eq_of_eq_scaledIdeal`: the covolume of `u 𝔞` is `|u|² N(𝔞) √d / 2`.
* `PeriodPair.IsOrderTwo.scaledDisc_sum_prod`, `PeriodPair.IsOrderTwo.scaledDisc_mul_of_isogeny`:
  identities for the discriminants `s(u)` of a lattice scaled to `℘''(u) = 2` at the points `u` of
  order two.
* `New.CMLattice.norm_scaledDisc_le_one`, `New.CMLattice.prod_scaledDisc_t`: for a family of data,
  one in each ideal class, the numbers `s(u)` are integral, and those at the points `t` have the
  product `±1`.
* `New.CMLattice.norm_disc_eq_one`: the discriminant `a₁⁴ - 64` of a CM lattice is a unit at every
  prime.

Notions from other files:
* `New.CMLattice d`: a period lattice `Λ` stable under `𝓞 K`, with a point `t` of order two and a
  number `a₁`.
* `PeriodPair.area`: the area `|Im(ω̄₁ω₂)|` of the fundamental parallelogram spanned by the periods
  `ω₁`, `ω₂` of a period pair.

## Relation to the literature

Known result: lattices stable under `𝓞 K` are the multiples of fractional ideals. Source: Silverman,
Advanced topics in the arithmetic of elliptic curves.

Known result: Siegel units. For a torsion point `u`, the twelfth power of Klein's form at `u` times
the discriminant is an algebraic integer, and a unit if two different primes of `K` divide the
annihilator of `u`. The file proves the case of the point `t`, whose annihilator is `(2)`; there the
number is the discriminant `a₁⁴ - 64`. Source: Kubert, Lang, Modular Units. Up to sign the numbers
`s(u)` are the 24-th powers of Weber's functions. Source: Birch, Weber's class invariants, 1969.



## CM lattices and multiples of fractional ideals

A datum `New.CMLattice d` is a lattice `Λ` stable under `𝓞 K` with a point `t` of order two such
that `ω t, ω̄ t ∉ Λ`, scaled to `℘''(t) = 2`, and a square root `a₁` of `12 ℘(t)`. The number
`ω = (1 + √-d) / 2` is `New.quadGen` in `ℂ` and `New.QuadField.betaK` in `𝓞 K`; `quadInt d` is the
image of `𝓞 K` in `ℂ`.


### `CMLattice.latticeModule`

 The lattice Λ of a CM datum regarded as an 𝒪_K-submodule of ℂ. 

### `QuadField.scaledIdeal`

 The monoid homomorphism (u, 𝔞) ↦ u𝔞 from pairs of a nonzero complex number and a nonzero
fractional ideal of K to 𝓞_K-submodules of ℂ. 

### `QuadField.mem_scaledIdeal`

 Membership in `u 𝔞`, for `x = (u, 𝔞)`: `z = u y` for some `y` in `𝔞`. 

### `QuadField.linearIndependent_mul_basis`

 For a ℤ-basis b₀, b₁ of a fractional ideal of K = ℚ(√−d) and a nonzero complex number c, the
numbers cb₀, cb₁ are linearly independent over ℝ. 

### `QuadField.not_lattice_le_comap_half`

 If the real part of a is that of ω = (1 + √−d)/2, then multiplication by a/2 does not map a
lattice into itself. 

### `weierstrassP_mul_eq_of_mul_mem_iff`

 If `L' = c L` for lattices `L`, `L'` and `c ≠ 0`, then `℘_{L'}(c z) = c⁻² ℘_L(z)`. 

### `g₂_eq_of_mul_mem_iff`

 If `L' = c L` for lattices `L`, `L'` and `c ≠ 0`, then `g₂(L') = c⁻⁴ g₂(L)`. 

### `exists_mem_lattice_quadGen_mul_half_notMem`

 Every lattice `L` has a point `l` such that neither `ω l / 2` nor `ω̄ l / 2` lies in `L`, where
`ω = (1 + √-d) / 2` is `quadGen d`. 

### `QuadField.exists_cmLattice_latticeModule_eq_scaledIdeal`

 For `d` a prime ≡ 7 mod 8 and `K = ℚ(√-d)`, every nonzero fractional ideal 𝔠 of K has a multiple
u𝔠, u ∈ ℂ^×, that is the lattice of a CM datum. Such a datum is a lattice stable under 𝓞_K with a
point t of order two such that ℘''(t) = 2 and ωt, ω̄t are not in it, where ω = (1 + √-d)/2, together
with a square root of 12℘(t). 

### `QuadField.exists_eq_scaledIdeal_mul_of_mk_eq_one`

 If the fractional ideal 𝔠 has trivial class, then every 𝓞_K-submodule N of ℂ equals u𝔠N for
some u ∈ ℂ^×. 

### `CMLattice.exists_latticeModule_eq_scaledIdeal`

 The lattice of a CM datum is `u 𝔞` for some `u` in `ℂˣ` and nonzero fractional ideal `𝔞`. 

### `CMLattice.exists_latticeModule_eq_scaledIdeal_mul`

 For a nonzero fractional ideal `𝔠` and a CM datum with lattice `Λ`, some multiple `u 𝔠 Λ`,
`u` in `ℂˣ`, is the lattice of a CM datum. 

### `QuadField.latticeEquiv`

 If the lattice Λ of C is u𝔞, with x = (u, 𝔞), then multiplication by u is an additive
isomorphism 𝔞 ≅ Λ. 

### `QuadField.area_eq_of_eq_scaledIdeal`

 Let d be a prime ≡ 7 mod 8. If the lattice of C equals u𝔞, with x = (u, 𝔞), u ∈ ℂ^× and 𝔞 a
nonzero fractional ideal of K = ℚ(√−d), then its area is |u|²·N(𝔞)·√d/2. 


## Good reduction of the CM curve

For a point `u` of order two, `s(u)` is the discriminant of the lattice scaled to `℘''(u) = 2`. Here
`t` is the point `C.t` of a datum `C`, and `ω = (1 + √-d) / 2` is `quadGen d`.


### `IsOrderTwo`

 `u` represents a point of order two on `ℂ / L`. 

### `IsOrderTwo.notMem`

 The point is not the origin. 

### `IsOrderTwo.add_self_mem`

 Twice the point is the origin. 

### `scaledDisc`

 The number `s(u) = 288 ℘(u)² / ℘''(u) - 64`. For a point `u` of order two it is the
discriminant of the lattice after the scaling that makes `℘''(u) = 2`. 

### `deriv_derivWeierstrassP_eq_sumInvPow`

 Off the lattice, `℘''(u)` is six times the sum of `(l - u)⁻⁴` over the lattice. 

### `IsOrderTwo.weierstrassP_ne`

 If `u₁`, `u₂`, `u₃` are points of order two whose sum is a period, then `℘(u₁) ≠ ℘(u₂)`. 

### `IsOrderTwo.sum_eq_zero_and_deriv_derivWeierstrassP_eq`

 Let `u₁`, `u₂`, `u₃` be points of order two of `ℂ / L` whose sum is a period, with
`eᵢ = ℘(uᵢ)`. The `eᵢ` are the three roots of the cubic `4 X³ - g₂ X - g₃`, so their sum is `0`
and `℘''(u₁) = 2 (e₁ - e₂) (e₁ - e₃)`. 

### `IsOrderTwo.scaledDisc_eq`

 Let `u₁`, `u₂`, `u₃` be points of order two whose sum is a period, with `eᵢ = ℘(uᵢ)`. With
`δ₁ = e₂ - e₃`, `δ₂ = e₃ - e₁`, `δ₃ = e₁ - e₂` we have `s(u₁) = -16 δ₁² / (δ₂ δ₃)`, where `s` is
`scaledDisc`. 

### `IsOrderTwo.scaledDisc_sum_prod`

 For three points `uᵢ` of order two of `ℂ / L` whose sum is a period, the numbers `s(uᵢ)` (see
`scaledDisc`) have the sum `-48` and the product `-2¹²`. 

### `sumInvPow_four_of_two_cosets`

 If `c⁻¹ L'` is the union of the cosets `L - u` and `L`, with `u ∉ L`, then the sum
`L'.sumInvPow (c y) 4` of `(l - c y)⁻⁴` over `l ∈ L'` is `c⁻⁴` times the total of the sums of
`(l - (u + y))⁻⁴` and of `(l - y)⁻⁴` over `l ∈ L`. 

### `deriv_derivWeierstrassP_of_two_cosets`

 If `c⁻¹ L'` is the union of `L - u` and `L`, with `u ∉ L`, then, away from the lattices,
`℘''_{L'}(c y) = c⁻⁴ (℘''(u + y) + ℘''(y))`. 

### `g₂_eq_of_two_cosets`

 If `c⁻¹ L'` is the union of `L - u` and `L`, with `u ∉ L`, then
`g₂(L') = c⁻⁴ (g₂(L) + 10 ℘''(u))`. 

### `IsOrderTwo.scaledDisc_mul_of_isogeny`

 Let `u₁, u₂, u₃` be points of order two modulo `L` whose sum is a period, and let `c ≠ 0` be
such that `L' = c (L + ℤ u₁)`, that is, `c x ∈ L'` if and only if `x + u₁` or `x` lies in `L`. Write
`s(u) = 288 ℘(u)² / ℘''(u) - 64` (`scaledDisc`), computed with the ℘-function of the lattice in
question. Then `s(u₁)` for `L` and `s(c u₂)` for `L'` have the product `2¹²`. 

### `norm_sub_le_one`

 The difference of two integral elements of `ℂ_[p]` is integral. 

### `norm_sq_eq_of_norm_add_le_one`

 If two elements `x, y` of `ℂ_[p]` have an integral sum and a product of norm `> 1`, then the
norm of that product is `‖x‖²` (the two norms are equal). 

### `norm_le_one_of_cycle`

 Let `s, s', s₀` be functions with values in `ℂ_[p]` on a finite group such that, for all `c`,
`s(c) + s'(c) + s₀(c)` and `s(c) s'(g c)` are integral and `s(g c) s₀(g c) = -s(c)`. Then `s` is
integral: a norm `‖s(c)‖ > 1` would be replaced by its square root at each step `c ↦ g c`, and the
steps return to `c`. 

### `scaledDisc_t`

 At the point `t` of a CM lattice the number `s` (see `scaledDisc`) is `a₁⁴ - 64`, where `a₁` is
the chosen square root of `12 ℘(t)`. 

### `one_sub_eq_quadGen_or_conj`

 If `b` is `ω = (1 + √-d) / 2` or `ω̄`, then so is `1 - b`. 

### `isOrderTwo_mul_t`

 For a CM lattice with point `t`, the points `ω t` and `ω̄ t` have order two; here
`ω = (1 + √-d) / 2` is `quadGen d`. 

### `scaledDisc_sum_prod`

 For `b = ω` or `ω̄`, where `ω = (1 + √-d) / 2`, the points of order two of a CM lattice are
`b t`, `(1 - b) t` and `t`. So their numbers `scaledDisc` have the sum `-48` and the product
`-2¹²`. 

### `halfIdeal`

 The fractional ideal generated by `1` and `e / 2`. For `e = ω̄` it is the inverse of the prime
`(2, ω)` above `2`, and for `e = ω` the inverse of the prime `(2, ω̄)`. 

### `mul_mem_iff_of_halfIdeal`

 Let `b` be `ω` or `ω̄`, given by the integer `e` of `ℚ(√-d)`. If the lattice `Λ'` of `D` is `c`
times the product of `halfIdeal e = (1, b / 2)` and the lattice `Λ` of `C`, then `c z ∈ Λ'` if and
only if `z + b t` or `z` lies in `Λ`: indeed `Λ + (b / 2) Λ = Λ + ℤ b t`. Here
`ω = (1 + √-d) / 2`, `t` is the distinguished point of order two of `C` and `scaledIdeal d (c, 𝔞)`
is the module `c 𝔞`. 

### `scaledDisc_two_isogeny`

 Let `b` be `ω` or `ω̄` and let multiplication by `c` be an isogeny of degree two from `C` to `D`
with kernel generated by `b t`, that is, `c z` is in the lattice of `D` if and only if `z + b t` or
`z` is in that of `C`. Then `s_C(b t) s_D((1 - b) t) = 2¹²` and `s_D(b t) s_D(t) = -s_C(b t)`,
where `s` is `scaledDisc` and `t` denotes the point of the datum in question. 

### `IsInClass`

 The lattice of `C` is a multiple of a fractional ideal in the class `𝒞`. 

### `exists_forall_isInClass`

 There is a family of CM lattices indexed by the ideal classes, with the lattice of index `𝒞`
a multiple of an ideal in the class `𝒞` (`IsInClass`), that contains the given lattice `C`. 

### `IsInClass.exists_eq_scaledIdeal_mul`

 If the ideal class of the CM lattice `D` (in the sense of `IsInClass`) is that of `C` times the
class of the fractional ideal `𝔟`, then the lattice of `D` is a multiple of `𝔟` times the lattice
of `C`. 

### `exists_class_scaledDisc_mul`

 For `b = ω` or `ω̄`, with `ω = (1 + √-d) / 2`, there is an ideal class `𝔤` such that, for any CM
lattices `C` in a class `𝒞` and `D` in the class `𝔤 𝒞`, we have `s_C(b t) s_D((1 - b) t) = 2¹²` and
`s_D(b t) s_D(t) = -s_C(b t)`, where `s` is `scaledDisc` and `t` is the point of order two of the
datum in question. 

### `norm_scaledDisc_le_one`

 Let `d` be a prime `≡ 7 mod 8`, `ι : ℂ →+* ℂ_[p]` an embedding for a prime `p`, and `D 𝒞` a CM
lattice in each ideal class `𝒞`, with its point `t` of order two. Then
`scaledDisc u = 288 ℘(u)² / ℘''(u) - 64` for the lattice of `D 𝒞` satisfies `‖ι (scaledDisc u)‖ ≤ 1`
at the three points `u = ω t, ω̄ t, t` of order two, where `ω = (1 + √-d) / 2`. At a point of order
two, `scaledDisc` is the discriminant of the lattice after rescaling so that `℘''(u) = 2`. 

### `prod_scaledDisc_t`

 For a family `D` of CM lattices, the lattice `D 𝒞` being a multiple of an ideal in the class `𝒞`
(`IsInClass`), the numbers `s = scaledDisc` at their distinguished points `t` of order two
have the product `±1`, the sign being `(-1)` to the class number. 

### `norm_disc_eq_one`

 Let `C` be a CM lattice for a prime `d ≡ 7 mod 8`, normalised so that its point `t` of order two
has `℘''(t) = 2`, and let `ι` be a ring homomorphism `ℂ → ℂ_[p]`. Then `a₁⁴ - 64`, where
`a₁² = 12 ℘(t)`, has norm `1`. This number is the discriminant `g₂³ - 27 g₃²` of the lattice
(`disc_eq`).

This is the unit property of Siegel units (Ramachandra, Robert) at the point `t` of order two only,
expressed as norm 1 of the normalised discriminant under every ring homomorphism `ℂ → ℂ_[p]`. 

### `norm_lt_one_of_eq_mul_add_mul`

 For a prime `p`, an element of `ℂ_[p]` of the form `x u + y v` with `x, y` integral and
`‖u‖, ‖v‖ < 1` has norm `< 1`. 
