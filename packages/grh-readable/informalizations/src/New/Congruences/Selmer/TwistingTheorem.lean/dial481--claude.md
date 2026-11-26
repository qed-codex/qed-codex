---
{
  "module": "src/New/Congruences/Selmer/TwistingTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The twisting theorem

The general twisting theorem is applied to the Selmer data of finitely many representations of
main-summand type and to the Stickelberger systems of the ramified pairs, and the Galois character
it gives is read as the `ℓ`-adic avatar of a tame character.

* `New.Selmer.SelmerDatum.TwistedLengthLe.hasDivisibleSelmerLengthLe`: a bound for the twisted
  Selmer group of a datum bounds the crystalline Selmer group of the twisted representation.
* `New.Selmer.exists_mFoldTwist_hasDivisibleSelmerLengthLe`: one tame character whose first `D.m`
  powers have small ramification, short Selmer groups on the main summands, and ratios of `L`-values
  of small valuation.

Notions from other files:
* `New.Selmer.HasDivisibleSelmerLengthLe`: a bound for the length of the Selmer group of a twisted
  representation with coefficients in `Frac(O) / O`.
* `New.Selmer.IsMainSummandLike`: the hypotheses on an `ℓ`-adic representation of the Galois group
  of `D.E` under which its Selmer groups are estimated.
* `New.Selmer.SelmerDatum`: a lattice `T` with Galois action, local conditions and an inertial
  element that acts by a scalar.
* `New.Selmer.twistError`: the number `e'_ℓ = (4 f + 3) r v(D.chosenGroupOrder) + 2 ^ (-ℓ)`.
* `New.Data.MFoldTwist`: a tame character whose tame part has non-trivial `n`-th power at every
  place of its modulus `Q`, for `1 ≤ n ≤ D.m`.
* `New.Data.CriticalPair.ratio`: the ratio `|L(z, (νϑ^s)⁻¹)| / |L(z, ν⁻¹)|` for a sign `s`, without
  the Euler factors at the chosen places, the modulus and their conjugates.

## Relation to the literature

For finitely many main summands of Galois representations of lifts, one finite-order anticyclotomic
twist ramified at new primes makes, for each of its first m powers, all Selmer groups short and the
ratios of twisted to untwisted Hecke values barely divisible by ℓ. This limits congruences. Twists
of ℓ-power order at new primes that kill a Selmer group or keep L-values barely divisible are known
in the literature. Related work: Mazur–Rubin, Diophantine stability, 2018; Kriz–Nordentoft,
Horizontal p-adic L-functions, 2023; Hida, Non-vanishing modulo p of Hecke L-values, 2004.


### `norm_inv_le_exp_of_ellVal_le`

 If the image of a complex number `x` under `ιℓ : ℂ ≃ ℚ̄_ℓ` has `ℓ`-adic valuation at most `c`,
then the image of `x⁻¹` has norm at most `ℓ ^ c`. 

### `mapRel_crysRelations_subset`

 Let `u` be a Galois representation over a coefficient ring `O ≤ O'`, and let `ψ` be an
`O'`-valued character that is trivial on the chosen decomposition groups above `ℓ`. A linear
relation that holds on the crystalline cocycles of `u` at a place above `ℓ`, with its coefficients
mapped to `O'`, is such a relation for the twist by `ψ` of the extension of `u` to `O'`. 

### `IsSmallTwist.isAuxTwist`

 Let `S₀` be a finite set of places of `E` containing those above `ℓ`, and let `Q` be auxiliary
for `S₀`: its places have prime norm, and `Q`, its conjugate `Q̄` and `S₀` are pairwise disjoint.
Let `ψ` satisfy `IsSmallTwist T Y ε Q ψ`, the list of conclusions of `exists_anticyclotomic_twist`
for Galois lattices with local conditions `T i` and families `Y k` of group ring elements, both
attached to `S₀` and `g₀ ∈ Gal(Ω/E)`. Only two clauses are used, which involve neither `T` nor `Y`:
`ψ` comes by `x ↦ x / x̄` from an idele class character of modulus `Q` trivial above `ℓ`, and the
valuations of `ψ γ_w - 1` for tame inertia generators `γ_w`, `w ∈ Q ∪ Q̄`, have sum at most `ε`.
Then `IsAuxTwist S₀ Q ψ ε` holds: `Q` is auxiliary for `S₀` and prime to `ℓ`, `ψ` has the form
above, and the sum of these valuations over `w ∈ Q` is at most `ε`. 

### `divisibleSelmerLength_le_divisibleLength`

 Let `T` be a Selmer datum over `O₀`: a Galois lattice `T.ρ` unramified outside the finite set
`T.places ⊆ S₀`, with modules of local cocycles at the places above `ℓ` and an inertial element
`T.γ` that acts by a scalar. Let `O` be a discrete valuation ring, `e : O₀ → O` a ring map, `ρ` the
twist by the `O`-valued character `ψ` of `T.ρ` extended along `e`, and `S = T.places ∪ Q ∪ Q̄`. The
group `Sel_Q(T ψ)`, of length `T.divisibleLength Q e ψ`, consists of the cocycles for `ρ` unramified
outside `S` that obey the images under `e` of the relations `T.classRelations`. If the set of linear
relations `L` contains these images, then the module of cocycles for `ρ` unramified outside `S` that
obey `L` is at most as long as `Sel_Q(T ψ)`, both with coefficients in `Frac(O) / O`. 

### `SelmerDatum.apply_γ_eq_one`

 Let `T` be a Selmer datum for `S₀`: a Galois lattice unramified outside `S₀` with local
conditions above `ℓ` and an element `T.γ`, inertial at a place of `S₀`, that acts by a scalar. Let
`Q` be auxiliary for `S₀`, so that neither `Q` nor `Q̄` meets `S₀`. A character `ψ` that comes by
`x ↦ x / x̄` from an idele class character of modulus `Q` trivial above `ℓ` is trivial at `T.γ`. 

### `SelmerDatum.TwistedLengthLe.hasDivisibleSelmerLengthLe`

 Let `D` be admissible data, with CM field `D.E`, primes `p₀, p₁` and level `D.N`;
`badPlaces D ℓ` is the set of places dividing `ℓ p₀ p₁ D.N`. Let `R` be an `ℓ`-adic representation
of the Galois group of `D.E`, and `T` a Selmer datum over `O` whose representation `T.ρ` is
conjugate to `R` over `ℚ̄_ℓ`, whose places are those above `ℓ p₀ p₁` and whose local conditions are
the crystalline ones; the inertial element `T.γ` acts by the scalar `T.ζ`. Let the places of `Q`
have prime norm, with `Q`, `Q̄` and the bad places pairwise disjoint, and let `ψ` come by
`x ↦ x / x̄` from an idele class character of modulus `Q` trivial above `ℓ`. Suppose that for all
large coefficient rings `O' ⊇ O` the character `ψ` has values in `O'` and `Sel_Q(T ψ)` has length at
most `b`, where `O' / ℓ` has length `1`. Then for all large `O'` there is a lattice in `ψ R` on
which `T.γ` acts by `T.ζ` and whose crystalline Selmer group for `Q` and `T.γ` has length at most
`b`. 

### `four_mul_ellVal_levelPrime_sub_one_add_le_twistError`

 For each of the two primes `p_i = D.levelPrime i` of the admissible data `D`, the number
`4 v(p_i - 1) + 2 ^ (-ℓ)` is at most
`twistError ℓ D = (4 D.f + 3) D.r v(D.chosenGroupOrder) + 2 ^ (-ℓ)`, where `v` is the `ℓ`-adic
valuation with `v(ℓ) = 1`. 

### `invAvatar_pow`

 For a tame character `τ` and `j : ℕ`, `(τ.pow j).invAvatar`, the `ℓ`-adic Galois character
attached to the inverse of `τ ^ j`, is the `j`-th power of `τ.invAvatar`. 

### `tamePart_ne_one_of_invAvatar_ne_one`

 Let `τ` be a character of `U(1)(𝔸)` of weight `0` for the CM field `D.E` whose tame part, a
character `τ.tamePart w` of the residue field at each finite place `w`, is supported on `τ.Q`. Let
`τ.invAvatar` be the `ℓ`-adic Galois character that class field theory and the fixed isomorphism
`ℂ ≃ ℚ̄_ℓ` attach to the base change of `τ⁻¹` to `D.E`. If it is non-trivial at an element `g` of an
inertia group above a place `w` of `τ.Q`, then the tame part of `τ` at `w` is non-trivial. 

### `exists_selmerData_isTorsionLevel`

 Let `D` be admissible data, with CM field `D.E` and primes `p₀, p₁`, and let `badPlaces D ℓ` be
the places dividing `ℓ p₀ p₁ D.N`. Fix an isomorphism `ℂ ≃ ℚ̄_ℓ` and finitely many `ℓ`-adic
representations `R i` of the Galois group of `D.E` that satisfy `IsMainSummandLike`. Let `w` be a
chosen place, that is, one dividing the factor `D.piM` of `p₀ p₁`, prime to `ℓ`. Let
`c = (4 f + 3) · D.r · v(D.chosenGroupOrder)`, where `f = D.f` is the number of infinite places of
`D.E`, `v` is the `ℓ`-adic valuation and `D.chosenGroupOrder` is the product of the orders of
`GL (D.r * D.t)` over the residue fields of the chosen places. Over some coefficient ring `O` every
`R i` has a lattice that carries a Selmer datum `T i` for the bad places and a generator `g₀` of
tame inertia at `w`. It is unramified outside `ℓ p₀ p₁` and its local conditions are the crystalline
ones. Its error term `(T i).β`, a sum of a global term and of local terms among which is the
valuation of `det((T i).ρ g₀ - 1)`, is at most `c` when `O / ℓ` is given length `1`. Finally
`IsTorsionLevel T (c + 2)` holds: `c + 2` exceeds each such `β` by more than `1`, and the residue
field of `O` has more than `2 rank(T i) len(O / ℓ ^ (c + 2)) + 1` elements. 

### `exists_mFoldTwist_hasDivisibleSelmerLengthLe`

 The twisting theorem. Let `D` be admissible data for the parameters `P` (a modulus and the field
`K = ℚ(√-d)`), with CM field `D.E`, primes `p₀, p₁` and level `D.N`. The bad places are those
dividing `ℓ p₀ p₁ D.N`; the chosen places are those dividing the factor `D.piM` of `p₀ p₁` from `K`.
Fix an isomorphism `ιℓ : ℂ ≃ ℚ̄_ℓ` (the datum `ι`) and finitely many `ℓ`-adic representations `R i`
of the Galois group of `D.E` that satisfy `IsMainSummandLike D t J` for some `t` and `J`:
`R^c ≅ R^∨(1 - t)`, `J` gives the jumps at the complex embeddings, the image is large and inertia
above `p₀ p₁` is controlled. Let
`e'_ℓ = twistError ℓ D = (4 D.f + 3) D.r v(D.chosenGroupOrder) + 2 ^ (-ℓ)`, with `v` the `ℓ`-adic
valuation. Then there is a character `τ` of `U(1)(𝔸)` of weight `0`, tamely ramified on a finite set
`Q` of places, such that each power `ξ = τ ^ j` with `1 ≤ j ≤ D.m` is ramified at every place of
`Q = ξ.Q` (`D.MFoldTwist`) and satisfies:
* the `ℓ`-adic Galois character `ψ = ξ.invAvatar` attached to `ξ⁻¹` is anticyclotomic and trivial
  above `ℓ`; the places of `Q` have prime norm, and `Q`, `Q̄` and the bad places are pairwise
  disjoint; `∑ v(ψ γ_w - 1) ≤ e'_ℓ` for some tame inertia generators `γ_w`, `w ∈ Q`;
* for each `i` there are an inertial element `γ` away from `ℓ` and a scalar `ζ`, with `ζ - 1` a
  unit, such that over all large coefficient rings `O` the element `γ` acts by `ζ` on a lattice in
  `ψ R i`, and the module of cocycles with coefficients in `Frac(O) / O` that are unramified outside
  `ℓ p₀ p₁`, `Q`, `Q̄`, crystalline above `ℓ` and zero at `γ` has length at most `e'_ℓ` (`O / ℓ` has
  length `1`);
* for each pair `p = (ν, z)` of a character `ν` of `U(1)(𝔸)` of weight `-c` and an integer
  `1 ≤ z ≤ D.t` with `z ≤ c ≤ 4 D.b`, the tame part of `ν` being non-trivial exactly at the chosen
  places, and each sign `s = ±1`, the image under `ιℓ` of `|L(z, (ν ξ^s)⁻¹)| / |L(z, ν⁻¹)|` has
  valuation at most `e'_ℓ`. The Euler factors at the chosen places, in the numerator also at `Q`,
  and at their conjugates are omitted. 
