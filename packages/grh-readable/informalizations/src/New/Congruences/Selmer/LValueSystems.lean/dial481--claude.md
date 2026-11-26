---
{
  "module": "src/New/Congruences/Selmer/LValueSystems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Stickelberger systems of the L-values

The integral measure of a ramified pair is mapped to the group rings of the class groups `Cl_Q`. Its
Euler factors give the norm relation, and its values at twists give the ratios of `L`-values. In
this file `ϑ` is the character of the system, `τ` a tame character and `ξ` a twist.

* `New.Data.CriticalPair.stickelbergerChar`: the character `ϑ` of the system.
* `New.Selmer.exists_stickelbergerSystem_β_le_and_norm_eq`: the system of a ramified pair and a
  sign.

Notions from other files:
* `New.Selmer.StickelbergerSystem`: elements `Θ_Q` of the group rings of the class groups `Cl_Q`
  with a norm relation. Its number `β` is `v(1(Θ_∅)) + ∑_e 2 v(ϑ(g) - 1)`, over the exponents `e`,
  where `g` is the Galois element of the system and `v` is `ellVal`, the `ℓ`-adic valuation
  truncated below at `0`.
* `badPlaces D ℓ`: for the data `D` (a number field `E` and primes `p₀`, `p₁`, `N`), the finite
  set of places of `E` dividing `ℓ p₀ p₁ N`. A modulus is auxiliary if its places have prime norm
  and it is disjoint from this set, from the conjugate of this set and from its own conjugate.
* `New.Data.CriticalPair.ratio`: the ratio |L(z, (ντ^δ)⁻¹)| / |L(z, ν⁻¹)| for a tame character τ and
  a sign δ. Both L-functions omit the Euler factors at the chosen places and their conjugates; the
  numerator also omits those at the places of the modulus of τ and their conjugates.
* `New.IsFromU1`: a Galois character `ψ` is a character for `Q` if `ψ(Art x) = η(x / x̄)` for an
  idele class character `η` of modulus `Q` that is trivial at the places over `ℓ`.
* `New.Data.CriticalPair.IsTwistMeasure`: values, one for each tame character, that are an integral
  measure, take Euler factors when a place is added and give powers of the ratio at twists.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `not_isChosen_of_notMem_badPlaces`

 Let `p₀`, `p₁` and `N` be the three primes of the data `D` and `E` its number field. A place `v`
of `E` outside `badPlaces D ℓ`, the finite set of places dividing `ℓ p₀ p₁ N`, does not lie over
`ℓ`, and neither `v` nor its conjugate is chosen (the chosen places divide a fixed integer of norm
`p₀ p₁`). 

### `_root_.New.Data.CriticalPair.stickelbergerChar`

 A pair `p = (ν, z)` consists of a character `ν` of `U(1)(𝔸)` and an integer `z`. For such a pair
and a sign `δ` this is `ϑ`: the `ℓ`-adic Galois character (avatar) that class field theory attaches
to the algebraic Hecke character of `E` given by the base change of `ν ^ (-δ)`. 

### `charUnramifiedAt_zpow_neg_of_notMem_badPlaces`

 Let `p = (ν, z)` be a pair, so that the residue characters of `ν` are trivial outside the chosen
places, and `δ` a sign. The algebraic Hecke character of the base change of `ν ^ (-δ)` to the field
`E` of the data `D` is unramified at every place outside `badPlaces D ℓ`, the places dividing
`ℓ p₀ p₁ N`, where `p₀`, `p₁` and `N` are the three primes of `D`. 

### `stickelbergerChar_eq_one_of_mem_inertiaAbove`

 Let `ℓ` be a prime, `p = (ν, z)` a pair and `δ` a sign, and let `ϑ = p.stickelbergerChar δ` be
the `ℓ`-adic Galois character attached to the base change of `ν ^ (-δ)` to the field `E` of the data
`D`. Then `ϑ` is trivial on the inertia groups at all places outside `badPlaces D ℓ`, the places
dividing `ℓ p₀ p₁ N`, where `p₀`, `p₁` and `N` are the three primes of `D`. 

### `stickelbergerChar_tameGenerator_ne_one_and_pow_eq_one`

 Let `p = (ν, z)` be a ramified pair: the residue characters of `ν` are nontrivial exactly at the
chosen places, which divide a fixed integer of norm `p₀ p₁`. Let `w` be a chosen place not above
`ℓ`, let `δ` be a sign and let `ϑ = p.stickelbergerChar δ` be the `ℓ`-adic Galois character attached
to the base change of `ν ^ (-δ)`. At the tame generator of `w` (an inertia element) the value of
`ϑ` is not `1` and is a root of unity of order dividing `N w - 1`, with `N w` the norm of `w`. 

### `stickelbergerChar_mul_invAvatar_frob`

 Let `p = (ν, z)` be a pair, `δ` a sign and `τ` a tame character: a character of `U(1)(𝔸)` of
weight `0` with residue characters trivial outside a finite set `τ.Q` of places, its modulus. Let
`ϑ = p.stickelbergerChar δ` and `ψ = τ.invAvatar` be the `ℓ`-adic Galois characters (avatars)
attached to the base changes of `ν ^ (-δ)` and `τ⁻¹` to `E`. Let `v` be a place not dividing
`ℓ p₀ p₁ N`, with `v` and its conjugate outside `τ.Q`, and let `φ` be an arithmetic Frobenius
element at a place `A` over `v`. Then `ϑ(φ) ψ(φ) = ι(y) ^ δ`, where `ι` is the fixed isomorphism of
`ℂ` with `ℚ̄_ℓ` and `y` is the value of the base change to `E` of `ν τ ^ δ` at the chosen
uniformiser at `v`. 

### `exists_finPart_baseChange_eq`

 For every point `x` of `U(1)(𝔸)` there is a finite idele `y` such that every tame character
takes at `x` the value of its base change at `y`. 

### `_root_.New.Data.TameChar.zpowOfAuxiliary`

 The power `τ ^ δ` of a tame character `τ`, as a tame character of modulus `I`, where `I` is an
auxiliary set outside which the residue characters of `τ` are trivial. 

### `exists_groupRingEval_eq_of_isIntegralMeasure`

 Let `F` be a function on tame characters `τ` that is an integral measure: on each modulus `I` it
is `τ ↦ ∑ j, α j τ(u j)` for finitely many points `u j` and coefficients `α j` that are integral
away from the norm of `I`. Write `Cl_I` for `U1ClassGroup I`, the finite ideles `x` of `E` with
`x x̄ = 1` modulo those in `Eˣ` and the units `≡ 1` at `I`, and `ι` for the isomorphism of `ℂ` with
`ℚ̄_ℓ`. There are elements `Θ_I` of the group rings of the `Cl_I` such that `Θ_∅` has the value
`ι F(1)` at the trivial character and the following holds. Let `I` be auxiliary: its places have
prime norm, and it is disjoint from the places dividing `ℓ p₀ p₁ N`, their conjugates and its own
conjugate. Let the residue characters of `τ` be trivial outside `I`, and let `ψ`, the `ℓ`-adic
Galois character of `τ⁻¹`, be a character for `I` (`IsFromU1`): `ψ(Art x) = η(x / x̄)` for an idele
class character `η` of modulus `I` trivial at the places over `ℓ`. Then `ψ(Θ_I) = ι F(τ ^ δ)`, where
`τ ^ δ` is regarded as a tame character of modulus `I` (`zpowOfAuxiliary`). 

### `ellVal_stickelbergerChar_tameGenerator_sub_one_le`

 Let `p = (ν, z)` be a ramified pair (the residue characters of `ν` are nontrivial exactly at the
chosen places), `δ` a sign, `w` a chosen place not above `ℓ` and `ϑ = p.stickelbergerChar δ`, the
`ℓ`-adic Galois character attached to the base change of `ν ^ (-δ)`. At the tame generator `g₀` of
`w` the valuation `ellVal` of `ϑ(g₀) - 1` is at most that of `N w - 1`, with `N w` the norm of
`w`. 

### `apply_insert_eq_mul_eulerFactor`

 Let `p = (ν, z)` be a pair, and let `F` be a twist measure of `p` with Euler exponents `K`: a
function on tame characters which, when a place `v` is added to the modulus of `τ`, is multiplied by
the factors `1 - y ^ (±1) (N v) ^ (-e)`, `e ∈ K`, with `y` the value of `ν τ` at `v`. Let `δ` be a
sign, `v` a place outside the modulus `Q` of `τ` such that `Q` and `insert v Q` are auxiliary, and
`φ` an arithmetic Frobenius element at a place over `v`. Then, in passing from modulus `Q` to
`insert v Q`, the value `ι F(τ ^ δ)` is multiplied by the product of `1 - a ^ (±1) (N v) ^ (-e)`
over `e ∈ K` and both signs. Here `a = ϑ(φ) ψ(φ)`, where `ϑ = p.stickelbergerChar δ` and
`ψ = τ.invAvatar` are the `ℓ`-adic Galois characters attached to `ν ^ (-δ)` and `τ⁻¹`. 

### `norm_apply_twist`

 Let `p = (ν, z)` be a pair and `F` a twist measure of `p` with parameter `m`: at a twist `ξ` of
modulus `Q` it has the value `F(1) (N Q) ^ m r(ξ) ^ (m + 1)`, where
`r(ξ) = |L(z, (ν ξ)⁻¹)| / |L(z, ν⁻¹)|` is the ratio of `L`-values without Euler factors at the
chosen places and, above, at `Q`. A twist is a tame character whose residue characters are
nontrivial at every place of the modulus. If `Q` is auxiliary, then `N Q` is an `ℓ`-adic unit, and
the norm of `ι F(ξ ^ δ)` is that of `ι F(1)` times the `(m + 1)`-th power of that of `p.ratio ξ δ`,
the ratio `r(ξ ^ δ)`. 

### `exists_stickelbergerSystem_β_le_and_norm_eq`

 Let `D` be the data, `ℓ` a prime with an isomorphism `ιℓ` of `ℂ` with `ℚ̄_ℓ` (`PadicIso ℓ`), `δ`
a sign, and `p = (ν, z)` a ramified pair: the residue characters of the character `ν` of `U(1)(𝔸)`
are nontrivial exactly at the chosen places, which divide a fixed integer of norm `p₀ p₁`. Let `w`
be a chosen place not above `ℓ` and `g₀` its tame generator, an inertia element.

Then there is a Stickelberger system for `badPlaces D ℓ` and `g₀`: a Galois character `ϑ`, exponents
`e`, and for every finite set `Q` of places an element `Θ_Q` of the group ring of the class group
`Cl_Q` of `U(1)` of modulus `Q`, such that adding a place to `Q` multiplies the values by Euler
factors in `ϑ` and the `e`. Its number `β = v(1(Θ_∅)) + ∑_e 2 v(ϑ(g₀) - 1)`, with `v = ellVal` the
`ℓ`-adic valuation truncated below at `0`, is at most `v(1(Θ_∅)) + 4 v(N w - 1)`.

Let `ξ` be a twist (a weight `0` character of `U(1)(𝔸)` with residue characters nontrivial exactly
at a finite set `Q`, its modulus). Suppose that `Q` is auxiliary and that `ψ`, the `ℓ`-adic Galois
character of `ξ⁻¹`, is a character for `Q`. Let `r = p.ratio ξ δ`, the ratio
`|L(z, (ν ξ^δ)⁻¹)| / |L(z, ν⁻¹)|` without Euler factors at chosen places and, above, at `Q`. Then
`‖ψ(Θ_Q)‖ = ‖1(Θ_∅)‖ ‖ιℓ(r)‖ ^ i`, where `i = 2` if `z = 1` and `i = 1` otherwise. 

### `ellVal_le_of_norm_eq_mul_pow`

 Let `‖x‖ = ‖x₀‖ ‖r‖ ^ i` with `x₀ ≠ 0` integral and `i ≥ 1`. If `v(x) ≤ v(x₀) + c`, then
`v(r) ≤ c`, where `v` is the valuation `ellVal`. 

### `exists_stickelbergerSystem_ellVal_ratio_le`

 Let `D` be the data, `ℓ` a prime with an isomorphism `ιℓ` of `ℂ` with `ℚ̄_ℓ` (`PadicIso ℓ`), and
`v = ellVal` the `ℓ`-adic valuation truncated below at `0`. Let `δ` be a sign, `p = (ν, z)` a
ramified pair (residue characters of `ν` nontrivial exactly at the chosen places) and `w` a chosen
place not above `ℓ`.

There is a Stickelberger system, with number `β = v(1(Θ_∅)) + ∑_e 2 v(ϑ(g₀) - 1)` (`e` over the
Euler exponents, `g₀` the tame generator of `w`), with the following property. Let `ξ` be a twist
(residue characters nontrivial exactly at its modulus `Q`) such that `Q` is auxiliary and the Galois
character `ψ` of `ξ⁻¹` is a character for `Q`. If `v(ψ(Θ_Q)) ≤ β + c`, then
`v(ιℓ(r)) ≤ 4 v(w.q - 1) + c`, where `w.q` is the norm of `w`, for the ratio
`r = |L(z, (ν ξ^δ)⁻¹)| / |L(z, ν⁻¹)|` of `L`-values without Euler factors at chosen places and,
above, at `Q` (`p.ratio ξ δ`). 
